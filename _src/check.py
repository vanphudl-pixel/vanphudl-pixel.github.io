"""Quality gate. Run AFTER build_site.py. Exit code 1 on any problem.
Checks: every language has every article, no forbidden claims, every internal link
and image on every page resolves to a real file, sitemap is valid."""
import importlib, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from content._langs import NEW as _NEWL
LANGS = ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he"] + _NEWL
BASE = "https://vanphudalat.com/"
problems = []

C = {l: importlib.import_module(f"content.{l}").C for l in LANGS}
_EV = importlib.import_module("content.ev").EV
_XA = importlib.import_module("content.extra_a").ART
_XB = importlib.import_module("content.extra_b").ART
_HUB = importlib.import_module("content.placeshub")
_FAQ = importlib.import_module("content.artfaq").FAQ
ref = C["en"]
for l in LANGS:
    c = C[l]
    for sec in ["ui", "home", "routes", "blog"]:
        miss = set(ref[sec]) - set(c[sec])
        if miss:
            problems.append(f"{l}: section {sec} missing keys {miss}")
    # Owner 2026-11-01: new articles only in the focus languages; other languages may lack the newest keys,
    # but must keep en order, and the focus languages must have every article.
    if l in ("vi", "en", "zh", "ru", "ko", "id"):
        if list(c["articles"]) != list(ref["articles"]):
            problems.append(f"{l}: article keys/order differ from en")
    elif [k for k in ref["articles"] if k in c["articles"]] != list(c["articles"]):
        problems.append(f"{l}: article keys not in en order or unknown keys")
    slugs = [a[0] for a in c["articles"].values()]
    if len(slugs) != len(set(slugs)):
        problems.append(f"{l}: duplicate article slugs")
    for k, a in c["articles"].items():
        if len(a) != 7:
            problems.append(f"{l}/{k}: article tuple must have 7 fields")
        elif not (HERE.parent / "img" / f"{a[5]}.jpg").exists():
            problems.append(f"{l}/{k}: image img/{a[5]}.jpg does not exist")
    # Business rules: never mention driving licences, never state electric-scooter range in km
    # covers the language file, the electric-scooter page (ev.py) and the extra rental articles (extra_a/extra_b)
    txt = (repr(importlib.import_module('content.streets_vi').__dict__.get('S')) if l == 'vi' else '') + repr(c) + repr(_EV.get(l)) + repr(_XA.get(l)) + repr(_XB.get(l)) + repr(_HUB.T.get(l)) + repr(_HUB.EXTRA_T.get(l)) + repr(_FAQ.get(l))
    for pat in [r"licen", r"(?<!с)права", r"驾照", r"면허", r"免許", r"ใบขับขี่", r"\bSIM\b", r"\blesen\b", r"bằng lái", r"Führerschein", r"\bpermis\b", r"licencia", r"carnet de conducir", r"carné", r"רישיון", r"patente", r"rijbewijs", r"ប័ណ្ណបើកបរ", r"ໃບຂັບຂີ່", r"လိုင်စင်", r"per carica", r"per lading", r"ដុង", r"ດົ່ງ", r"ဒေါင်",
                r"\d+\s?(km|公里|км|กม|킬로)\s*(per charge|на заряд|充电|충전|充電|ต่อการชาร์จ|mỗi lần sạc)",
                r"(per charge|par charge|por carga|pro (Akku)?ladung|mỗi lần sạc|на (одном |полном )?заряде|充满电约|満充電で約|완충 시 약|1회 충전 약|ชาร์จเต็มวิ่ง|sekali isi|setiap cas|בטעינה|לטעינה)",
                r"120\s?(kg|кг|公斤|กก|ק\"ג)",
                r"\d[\d.,\u00a0\u202f ]*\d\s?(đ\b|₫|донг|ดอง|דונג|越南盾|ドン)", r"120[.,\u00a0\u202f ]?000\s?VND|\b120k\b"]:
        if re.search(pat, txt, re.I):
            problems.append(f"{l}: forbidden wording /{pat}/")

# Licence pillar page (content/licence.py, owner allowed licence wording ONLY here, 2026-10-28):
# every language present, every non-licence rule still enforced (currency, range wording, no 120 kg / 120k).
# Same checks for the night-bus arrival pillar (content/arrive.py): it may name the licence only to link to the licence page.
for _PN in ("licence", "arrive", "routeshub"):
  _P = importlib.import_module(f"content.{_PN}")
  if set(_P.T) != set(LANGS):
    problems.append(f"{_PN}: languages differ from site languages: {set(LANGS) ^ set(_P.T)}")
  for l, t in _P.T.items():
      txt = repr(t)
      for pat in [r"per carica", r"per lading", r"ដុង", r"ດົ່ງ", r"ဒေါင်",
                  r"(per charge|par charge|por carga|pro (Akku)?ladung|mỗi lần sạc|на (одном |полном )?заряде|充满电约|満充電で約|완충 시 약|1회 충전 약|ชาร์จเต็มวิ่ง|sekali isi|setiap cas|בטעינה|לטעינה)",
                  r"120\s?(kg|кг|公斤|กก)", r"\d[\d.,\u00a0\u202f ]*\d\s?(đ\b|₫|донг|ดอง|דונג|越南盾|ドン)", r"120[.,\u00a0\u202f ]?000\s?VND|\b120k\b",
                  r"international driving permit|1949|1968"]:
          if re.search(pat, txt, re.I):
              problems.append(f"{_PN}/{l}: forbidden wording /{pat}/")
      if '"' in t.get("title", "") + t.get("desc", ""):
          problems.append(f"{_PN}/{l}: ASCII quote in title/desc breaks the meta tag")

# core pages (rental home, electric scooter page) in the 6 focus languages: meta description <= 160 characters (audit 2026-11-12)
_ST = importlib.import_module("content.seo_titles")
for _blk in ("HOME", "EV"):
    for _l in ("vi", "en", "ru", "zh", "ko", "id"):
        if len(getattr(_ST, _blk)[_l][1]) > 160:
            problems.append(f"seo_titles {_blk}/{_l}: meta description longer than 160 characters")
# every page: internal links and images must exist
pages = list(ROOT.rglob("index.html"))
pages = [p for p in pages if "_src" not in p.parts]
# Audit 2026-11-12 (owner approved): built-page rules
_NOIDX = {BASE + str(p.parent.relative_to(ROOT)).replace("\\", "/").strip(".").lstrip("/") + ("/" if str(p.parent.relative_to(ROOT)) != "." else "")
          for p in pages if 'name="robots" content="noindex"' in p.read_text(encoding="utf-8")}
_OLD_LOAD = re.compile(r'(?<![\d–-])140\s?(kg|кг|公斤|킬로그램|กก\.|กิโลกรัม|ק"ג|ק״ג|ກິໂລ|ကီလို|គីឡូក្រាម)')
_OLD_RANGE = re.compile(r"(35\s?[〜～~–-]\s?40|60\s?[〜～~–-]\s?70)\s?km")
_CTA_FAQ = re.compile(r'"@type": "Question", "name": "(Ready to|Sẵn sàng|이제 빌려|准备好|Готовы|Siap )')
_CORE = {"dalat-motorbike-rental", "electric-scooter-rental-dalat"}
for p in pages:
    _h = p.read_text(encoding="utf-8")
    _rel = str(p.parent.relative_to(ROOT)).replace("\\", "/")
    _vis = re.sub(r"<script.*?</script>", "", _h, flags=re.S)
    if _OLD_LOAD.search(_vis): problems.append(f"{_rel}: old electric-scooter load 140 kg (now 130 kg)")
    if _OLD_RANGE.search(_vis): problems.append(f"{_rel}: old battery range 35–40 / 60–70 km (now 25–30 / 50–60 km)")
    if _CTA_FAQ.search(_h): problems.append(f"{_rel}: call-to-action heading inside FAQPage")
    for _u in re.findall(r'<link rel="alternate" hreflang="[^"]+" href="([^"]+)"', _h):
        if _u in _NOIDX: problems.append(f"{_rel}: hreflang points to noindex page {_u}"); break
for p in pages:
    html = p.read_text(encoding="utf-8")
    page_url = BASE + str(p.parent.relative_to(ROOT)).replace("\\", "/").strip(".") + "/"
    page_url = page_url.replace("//", "/").replace("https:/", "https://")
    for ref_ in re.findall(r'(?:href|src)="([^"]+)"', html):
        if ref_.startswith(("http", "mailto:", "tel:", "data:", "#", "weixin:")):
            continue
        target = urlparse(urljoin(page_url, ref_)).path.lstrip("/")
        f = ROOT / target
        if target.endswith("/") or target == "":
            f = f / "index.html"
        if not f.exists():
            problems.append(f"broken link on {p.relative_to(ROOT)} -> {ref_}")

try:
    r = ET.parse(ROOT / "sitemap.xml").getroot()
    locs = [e.text for e in r.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    for u in locs:
        if not (ROOT / u.replace(BASE, "") / "index.html").exists():
            problems.append(f"sitemap url has no page: {u}")
        if u in _NOIDX:
            problems.append(f"sitemap lists noindex page: {u}")
    for e in r.iter("{http://www.w3.org/1999/xhtml}link"):
        if e.get("href") in _NOIDX:
            problems.append(f"sitemap hreflang points to noindex page: {e.get('href')}"); break
except Exception as e:
    problems.append(f"sitemap invalid: {e}")

print(f"pages: {len(pages)}, sitemap urls: {len(locs) if 'locs' in dir() else '?'}")
if problems:
    print("PROBLEMS:")
    print("\n".join(problems[:50])); import collections as _c; print(_c.Counter(re.sub(r"^[^:]*: ", "", x).split(" http")[0].split(" ->")[0][:60] for x in problems).most_common(12))
    sys.exit(1)
print("ALL CHECKS PASSED")
