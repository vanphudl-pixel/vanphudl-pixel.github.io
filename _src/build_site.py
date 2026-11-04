"""Build the whole multilingual site (home, routes, blog + 5 articles per language)
from content/<lang>.py. Output: /home/claude/site"""
import importlib, math, json, re, shutil, sys
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
BASE = "https://vanphudalat.com/"
OUT = HERE.parent  # repo root = published site
from content._langs import NEW as _NEWL, META as _META
LANGS = ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he"] + _NEWL
LABEL = {"en": "EN", "ru": "RU", "zh": "中文", "ko": "한국어", "ja": "日本語", "th": "ไทย", "id": "ID", "ms": "MY", "vi": "VI", "de": "DE", "fr": "FR", "es": "ES", "he": "עב"}
LOCALE = {"en": "en_US", "ru": "ru_RU", "zh": "zh_CN", "ko": "ko_KR", "ja": "ja_JP", "th": "th_TH", "id": "id_ID", "ms": "ms_MY", "vi": "vi_VN", "de": "de_DE", "fr": "fr_FR", "es": "es_ES", "he": "he_IL"}
for _l in _NEWL: LABEL[_l], LOCALE[_l] = _META[_l][0], _META[_l][1]
LAT, LON = 11.9510676, 108.4384077
GMAPS = "https://maps.app.goo.gl/ULvgaZFh4Q1kjTCe6"
YA_LINK = f"https://yandex.ru/maps/?pt={LON},{LAT}&z=17&l=map"
AMAP = f"https://uri.amap.com/marker?position={LON},{LAT}&name=Van%20Phu%20%E5%A4%A7%E5%8F%BB%E6%91%A9%E6%89%98%E8%BD%A6%E7%A7%9F%E8%B5%81&src=vanphudalat&coordinate=wgs84&callnative=1"
YA_WIDGET = f"https://yandex.ru/map-widget/v1/?ll={LON}%2C{LAT}&z=16&pt={LON}%2C{LAT}%2Cpm2rdm"
TG = "https://t.me/vanphudalat"
YT = "https://www.youtube.com/@DalatMotorbikeRentalVanPhu"
TG_CHANNEL = "https://t.me/dalat_life_vietnam"
ZALO = "https://zalo.me/0944081101"
TIKTOK = "https://www.tiktok.com/@bietthudalat"  # owner's TikTok channel about Da Lat villas (owner asked 2026-11-04 to show it on the site)
TT_LBL = {"vi": "villa Đà Lạt", "en": "Da Lat villas", "ru": "виллы в Далате", "zh": "大叻别墅", "ko": "달랏 빌라", "id": "vila di Da Lat"}
WA2 = "https://wa.me/84834622149"
TRIPADVISOR = "https://www.tripadvisor.com/Attraction_Review-g293922-d17622334-Reviews-Van_Phu_Dalat_Motorbike_Rental-Da_Lat_Lam_Dong_Province.html"
YANDEX_ORG = "https://yandex.com/maps/org/van_phu/50542551609/"
YANDEX_ORG_RU = "https://yandex.ru/maps/org/van_phu/50542551609/"
def ya_org(l): return YANDEX_ORG_RU if l == "ru" else YANDEX_ORG
def ya_name(l): return "Яндекс Карты" if l == "ru" else "Yandex Maps"

C = {l: importlib.import_module(f"content.{l}").C for l in LANGS}
from content.ev import EV
from content import seo_titles as _SEO
for _l in LANGS:
    C[_l]["home"]["title"], C[_l]["home"]["desc"] = _SEO.HOME[_l]
    EV[_l]["title"], EV[_l]["desc"] = _SEO.EV[_l]
from content.cluster import GROUP as CL_GROUP
from content.photos import ALT as PHOTO_ALT, HERO as PHOTO_HERO, INLINE as PHOTO_INLINE
import html as _html
def _esc(t): return _html.escape(t, quote=True)
def _ph_style(name):
    """portrait photos are capped in width so they don't fill a whole screen"""
    from PIL import Image as _I
    w, h = _I.open(Path(__file__).resolve().parent.parent / "img" / (name + ".jpg")).size
    return "width:100%;height:auto;border-radius:12px" + (";max-width:440px;display:block;margin:0 auto" if h > w else "")
from content import photomap as PM
from content import pagodamap as PG
from content import churchmap as CH
from content import halalid as HI
from content import about as AB
from content import villa as VL
from content import funnelid as FI
from content import sunflowermap as SF
from content import cloudmap as CL
from content import cafemap as CF
from content import bbqmap as BB
from content import hotelmap as HT
from content import fourstarmap as H4
from content import threestarmap as H3
from content import busmap as BU
from content import danangbusmap as DN
from content import waterfallmap as WF
from content import attractmap as AM
from content import flowermap as FM
from content import nightcafemap as NC
from content import nhatrangbusmap as NT
from content import nightmarketmap as NM
from content import festivalmap as FE
from content import placeshub as HUB
from content import placeshub_price as HUBP
from content import routenew as RN
from content import routecheckin as RC
from content import dayhub as DAY
from content import tourmap as TM
from content import licence as LIC
from content import arrive as ARR
from content import routeshub as RH
from content._route import legs as route_legs
from content.extra_a import ART as _A
from content.extra_b import ART as _B
for _l in LANGS:
    C[_l]["articles"].update({**_A, **_B}[_l])
C["en"]["dates"].update({"price": "2026-10-12", "evgas": "2026-10-12"})

TPL = (HERE / "template.html").read_text(encoding="utf-8")
# article order = order in content/en.py (oldest first); every language must have every key
ARTICLES = list(C["en"]["articles"].keys())
# Owner decision 2026-11-01: new articles are written only in FOCUS_LANGS (vi, en, zh, ru, ko, id).
# Older articles stay in all 18 languages. A language simply lacks the keys it was not written in:
# listings, "read also", hreflang, language bar and sitemap only use the languages that really have the article.
FOCUS_LANGS = ["vi", "en", "zh", "ru", "ko", "id"]
def arts(l): return [k for k in ARTICLES if k in C[l]["articles"]]
ART_LANGS = {k: [x for x in LANGS if k in C[x]["articles"]] for k in ARTICLES}
def langs_of(kind, key): return ART_LANGS[key] if kind == "art" else LANGS
DATES = C["en"].get("dates", {})
def adate(k): return DATES.get(k, "2026-10-10")
from content.artfaq import FAQ as AFAQ, UPDATED as AUPD, H as AFAQ_H
def mdate(l, k): return max(adate(k), AUPD.get(l, {}).get(k, adate(k)))
UPD = {"en": "Updated", "vi": "Cập nhật", "ru": "Обновлено", "zh": "更新于", "ko": "업데이트", "ja": "更新日", "th": "อัปเดต", "id": "Diperbarui",
       "ms": "Dikemas kini", "de": "Aktualisiert", "fr": "Mis à jour", "es": "Actualizado", "he": "עודכן", "it": "Aggiornato", "nl": "Bijgewerkt",
       "km": "ធ្វើបច្ចុប្បន្នភាព", "lo": "ອັບເດດ", "my": "နောက်ဆုံးပြင်ဆင်"}
_MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def fdate(l, d):
    y, m, dd = d.split("-")
    if l == "en": return f"{_MON[int(m) - 1]} {int(dd)}, {y}"
    if l in ("zh", "ja", "ko"): return d
    return f"{dd}/{m}/{y}"
CSS = re.search(r"<style>(.*?)</style>", TPL, re.S).group(1) + """
.upd{font-size:14px;opacity:.85;margin:6px 0 0}
.toc{columns:2;font-size:15px;padding-left:18px} .toc li{margin:2px 0}
.hublist{list-style:none;padding:0;display:grid;gap:10px} .hublist li{display:flex;gap:10px;align-items:flex-start;border-bottom:1px solid var(--line);padding-bottom:10px}
.chips{display:flex;flex-wrap:wrap;gap:8px} .chips a{border:1px solid var(--line);border-radius:999px;padding:6px 12px;text-decoration:none;font-size:14px}
img{height:auto}
.lead{font-size:17px}
.langs a{border:1px solid rgba(255,255,255,.5);color:#fff;border-radius:6px;padding:4px 8px;font-size:13px;text-decoration:none}
.langs a.on{background:#fff;color:var(--brand)}
table.price{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.price th,table.price td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line)}
table.price th{background:var(--brand2);font-size:14px}
table.price tr:last-child td{border-bottom:0}
.note{color:var(--muted);font-size:14px;margin-top:8px}
.checks{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.checks li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px 12px 40px;position:relative}
.checks li:before{content:"✓";position:absolute;left:14px;top:11px;color:var(--brand);font-weight:700}
.prose p{margin:0 0 12px}
.prose ul{padding-left:20px}
.prose li{margin-bottom:6px}
.crumbs{font-size:13px;opacity:.9;margin-bottom:8px}
.crumbs a{color:#fff}
.route{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:12px}
.route h3{margin:0 0 6px;font-size:18px}
.route .meta{font-size:13px;color:var(--muted);margin-bottom:8px}
.route p{margin:0 0 8px}
.cta-box{background:var(--brand);color:#fff;border-radius:14px;padding:20px;margin-top:8px}
.cta-box h2{color:#fff}
.cta-box p{margin:0 0 14px}
.rules{display:grid;gap:10px}
.rule{display:flex;align-items:center;gap:12px;background:#fff4e5;border:1px solid #f2c98a;border-radius:12px;padding:14px 16px}
.rule .ic{font-size:24px;flex:none}
.revs{display:grid;gap:12px;margin:10px 0 14px}
@media(min-width:720px){.revs{grid-template-columns:1fr 1fr}}
.rv{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.rv .st{color:#f5a623;letter-spacing:2px;font-size:15px}
.rv blockquote{margin:6px 0 8px;font-style:italic}
.rv figcaption{font-size:13px;color:var(--muted)}
.box{background:#e8f5fc;border:1px solid #9fd4ef;border-radius:14px;padding:18px;margin:8px 0 18px}
.box h2{font-size:19px;margin:0 0 6px}
.box p{margin:0 0 12px}
.posts{display:grid;gap:12px}
.post{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;text-decoration:none;color:var(--ink)}
.post b{display:block;font-size:17px;margin-bottom:4px;color:var(--brand)}
.post span{color:var(--muted);font-size:14px}
.tg{background:#229ED9;color:#fff}
.zalo{background:#0068FF;color:#fff}
.wechat{background:#07C160;color:#fff}
.float.f2{bottom:74px}
.float.tgf{background:#229ED9}
.float.zf{background:#0068FF}
.float.f3{bottom:132px}
.float.callf{background:#f2b632;color:#173d2d}
.btn.callb{background:#f2b632;color:#173d2d}
.yt{margin:0 0 20px;max-width:300px} .yt a{position:relative;display:block;aspect-ratio:9/16;border-radius:14px;overflow:hidden;background:#000} .yt img,.yt iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0} .yt span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:64px;height:64px;border-radius:50%;background:rgba(0,0,0,.65);color:#fff;font-size:28px;display:flex;align-items:center;justify-content:center} .yt figcaption{font-size:14px;color:var(--muted);margin-top:6px}
.fcalls{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 18px}
.fp{display:inline-flex;align-items:center;gap:6px;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);color:#fff;text-decoration:none;font-weight:600;font-size:14px}
.fp:hover{background:rgba(255,255,255,.18)}
.fp.call{background:#f2b632;border-color:#f2b632;color:#173d2d}
.fp.yt{background:#c4302b;border-color:#c4302b}
.contact{background:var(--brand2);border-radius:14px;padding:6px 18px}
.crow{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-top:1px dashed rgba(23,61,45,.18);line-height:1.5;font-size:15px}
.crow:first-child{border-top:0}
.crow i{font-style:normal;flex:0 0 26px;text-align:center;font-size:18px;line-height:1.35}
.crow div{min-width:0;overflow-wrap:anywhere}
.crow.muted{font-size:14px;opacity:.85}
.napbox{max-width:620px;margin:0 auto 18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 16px;text-align:left;font-size:14px;line-height:1.5}
.napbox .nt{font-weight:700;color:#fff;font-size:15px;margin-bottom:2px}
.napbox .nl{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-top:1px dashed rgba(255,255,255,.14)}
.napbox .nl i{font-style:normal;font-size:18px;flex:0 0 26px;text-align:center;line-height:1.3}
.napbox .nl div{min-width:0;overflow-wrap:anywhere}
.napbox .lbl{display:block;font-size:12px;opacity:.7;margin-bottom:1px}
.napbox b{color:#fff}
.napbox a{color:#fff;text-decoration:underline;text-underline-offset:2px}
.footcall{display:block;margin:0 0 8px;font-size:15px}.nap{margin:0 0 12px;font-size:14px;line-height:1.6}.nap b{color:#fff}.footcall a{color:#fff;font-weight:700;text-decoration:none}
html:lang(ko) h1,html:lang(ko) h2{word-break:keep-all}
html[dir=rtl] .checks li{padding:12px 40px 12px 14px}
html[dir=rtl] .checks li:before{left:auto;right:14px}
html[dir=rtl] ol{padding-left:0;padding-right:20px}
html[dir=rtl] .prose ul{padding-left:0;padding-right:20px}
html[dir=rtl] .langs,html[dir=rtl] .price,html[dir=rtl] table.price th,html[dir=rtl] table.price td{text-align:right}
footer a{color:inherit;text-decoration:underline}
.kw{margin:12px 0 0;font-size:14px}

/* ---- 2026-10 redesign: pine + dã quỳ ---- */
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/bvp-vietnamese-400.woff2) format("woff2");unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/bvp-latin-400.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:600;font-display:swap;src:url(/fonts/bvp-vietnamese-600.woff2) format("woff2");unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:600;font-display:swap;src:url(/fonts/bvp-latin-600.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/bvp-vietnamese-700.woff2) format("woff2");unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/bvp-latin-700.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:800;font-display:swap;src:url(/fonts/bvp-vietnamese-800.woff2) format("woff2");unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:"Be Vietnam Pro";font-style:normal;font-weight:800;font-display:swap;src:url(/fonts/bvp-latin-800.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}

:root{--bg:#eef3ef;--ink:#16241d;--muted:#55655c;--brand:#2f6b4f;--pine:#173d2d;--brand2:#e3ede6;--accent:#f2b632;--line:#d6dfd8}
body{font-family:"Be Vietnam Pro",system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","Noto Sans SC","Noto Sans Thai",sans-serif}
h1,h2,h3{letter-spacing:-.01em}
h2{font-weight:800}
.btn{border-radius:12px;transition:transform .12s ease}
.btn:active{transform:translateY(1px)}
.btn:focus-visible,a:focus-visible,summary:focus-visible,button:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
@media(max-width:720px){.top{flex-direction:column;align-items:stretch}.langs{display:flex;flex-wrap:wrap;gap:4px;width:100%}.langs a{flex:1 0 auto;padding:6px 4px;text-align:center;font-size:12px;white-space:nowrap}}
header{background:var(--pine)}
footer{background:var(--pine);color:#cfe0d5;padding:28px 16px 96px}
/* home */
.hh{background:var(--pine);color:#fff}
.hh .top{padding:12px 0}
.hh-hero{position:relative;min-height:min(78vh,640px);display:flex;align-items:flex-end;overflow:hidden;isolation:isolate}
.hh-hero .heroimg{position:absolute;inset:0;width:100%;height:100%;margin:0;border-radius:0;aspect-ratio:auto;object-fit:cover;z-index:-2}
.hh-hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(14,36,27,.88) 0%,rgba(14,36,27,.55) 45%,rgba(14,36,27,.05) 80%),linear-gradient(180deg,rgba(14,36,27,0) 40%,rgba(14,36,27,.85) 100%)}
@media(max-width:720px){.hh-hero:after{background:linear-gradient(180deg,rgba(14,36,27,.25) 0%,rgba(14,36,27,.7) 40%,rgba(14,36,27,.95) 100%)}}
.hh .wrap{max-width:1040px}
.hh-in{padding:48px 16px 40px;width:100%}
.hh h1{font-size:clamp(34px,6vw,60px);line-height:1.05;font-weight:800;margin:0 0 14px;max-width:14ch;text-shadow:0 2px 18px rgba(0,0,0,.25)}
.hh .lead{max-width:56ch;margin:0 0 22px;font-size:18px;opacity:.96}
.ticket{display:inline-flex;align-items:baseline;gap:8px;background:var(--accent);color:var(--pine);font-weight:800;font-size:clamp(20px,3vw,26px);padding:10px 22px 10px 26px;margin:0 0 22px;border-radius:6px;
 -webkit-mask:radial-gradient(circle 9px at 0 50%,#0000 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 9px at 100% 50%,#0000 98%,#000) right/51% 100% no-repeat;
 mask:radial-gradient(circle 9px at 0 50%,#0000 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 9px at 100% 50%,#0000 98%,#000) right/51% 100% no-repeat}
.hh .cta .btn.alt{background:rgba(255,255,255,.14);color:#fff;border:1px solid rgba(255,255,255,.55);backdrop-filter:blur(4px)}
.facts{background:var(--pine);color:#fff;border-top:1px solid rgba(255,255,255,.12)}
.facts ul{list-style:none;margin:0 auto;padding:14px 16px;max-width:1040px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px 18px}
.facts li{font-weight:600;font-size:15px;display:flex;gap:8px;align-items:center}
.facts li:before{content:"";flex:none;width:9px;height:9px;border-radius:50%;background:var(--accent)}
@media(max-width:720px){.facts ul{grid-template-columns:1fr 1fr}.hh-hero{min-height:560px}.hh .lead{font-size:16px}}
main.home{max-width:1040px}
main.home>section{padding:40px 0 8px}
table.price{display:table;padding:0;margin:0;font-weight:400;color:var(--ink)}
table.price th{font-weight:600}
main.home h2{font-size:clamp(23px,3vw,30px);margin-bottom:16px}
main.home table.price{font-size:17px}
main.home table.price td b{color:var(--pine);background:#fdf1cf;padding:3px 10px;border-radius:6px;white-space:nowrap}
@media(min-width:820px){main.home .checks{grid-template-columns:1fr 1fr}.two{display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:start}.two>section{padding-top:0}main.home .two .checks{grid-template-columns:1fr}}
main.home>.two{padding-top:40px}
main.home .card{padding:0 0 16px;overflow:hidden}
main.home .card img{width:100%;margin:0 0 12px;border-radius:0}
main.home .card b,main.home .card span{display:block;padding:0 16px}
main.home .card b{font-size:18px;color:var(--pine)}
ol.steps{list-style:none;padding:0;margin:0;display:grid;gap:12px;counter-reset:st}
@media(min-width:820px){ol.steps{grid-template-columns:repeat(4,1fr)}}
ol.steps li{counter-increment:st;background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;margin:0}
ol.steps li:before{content:counter(st);display:flex;width:34px;height:34px;border-radius:50%;background:var(--pine);color:var(--accent);font-weight:800;align-items:center;justify-content:center;margin-bottom:10px}
main.home .gallery{grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
main.home .gallery img{border-radius:14px}
.pmsec p .btn{margin:0 6px 8px 0}
main.home .faq details{border-radius:12px;padding:14px 16px}
main.home .faq details[open]{border-color:var(--brand)}
main.home .posts{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
html[dir=rtl] .hh h1,html[dir=rtl] .hh .lead{margin-left:auto}
html[dir=rtl] ol.steps{padding-right:0}
"""

# ------------------------------------------------------------------ URLs
# keyword slug of the rental landing page in each language
RENT = {"en": "dalat-motorbike-rental", "vi": "thue-xe-may-da-lat", "ru": "arenda-bayka-dalat",
        "zh": "dalat-motorbike-rental", "ko": "dalat-motorbike-rental", "ja": "dalat-motorbike-rental",
        "th": "dalat-motorbike-rental", "id": "sewa-motor-dalat", "ms": "sewa-motosikal-dalat",
        "de": "roller-mieten-dalat", "fr": "location-scooter-dalat", "es": "alquiler-moto-dalat",
        "he": "dalat-motorbike-rental"}
for _l in _NEWL: RENT[_l] = _META[_l][2]
def lang_root(l): return "" if l == "en" else f"{l}/"
def home_path(l): return lang_root(l) + RENT[l] + "/"
def halal_path(): return lang_root("id") + "restoran-halal-dalat/"  # Indonesian-only halal restaurant map (short URL)
def tour_path(): return lang_root("id") + HI.TOUR_SLUG
HALAL_OLD = "id/sewa-motor-dalat/restoran-halal-dalat/"  # previous URL, kept as a redirect
def routes_path(l): return lang_root(l) + C[l]["routes"]["slug"] + "/"
def blog_path(l): return lang_root(l) + "blog/"
def ev_path(l): return lang_root(l) + EV[l]["slug"] + "/"
def art_path(l, k): return blog_path(l) + C[l]["articles"][k][0] + "/"
def hub_path(l): return lang_root(l) + HUB.SLUG[l] + "/"
def day_path(l): return lang_root(l) + DAY.SLUG[l] + "/"
def tm_path(l): return lang_root(l) + TM.SLUG[l] + "/"
def lic_path(l): return lang_root(l) + LIC.SLUG[l] + "/"
LIC_LANGS = [x for x in LIC.LANGS if x in LIC.T]
LIC_FROM = {"lt-documents", "lt-ev-foreigners", "evrules", "lt-ev-experience", "lt-procedure"}  # articles that link to the licence page
def pil_path(M, l): return lang_root(l) + M.SLUG[l] + "/"
def arr_path(l): return pil_path(ARR, l)
ARR_LANGS = [x for x in ARR.LANGS if x in ARR.T]
def arr_link(l, me): return f'<p class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px">{ARR.ICON} <a href="{rel(me, arr_path(l))}"><b>{ARR.T[l]["h1"]}</b></a> →</p>' if l in ARR.T else ""
def lic_link(l, me): return f'<p class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px">🪪 <a href="{rel(me, lic_path(l))}"><b>{LIC.T[l]["h1"]}</b></a> →</p>' if l in LIC.T else ""

def path_of(l, kind, key=None):
    return {"home": home_path, "routes": routes_path, "blog": blog_path, "ev": ev_path}[kind](l) if kind != "art" else art_path(l, key)

def rel(frm, to):
    """relative link from page path `frm` to page path `to` (both like 'ru/blog/x/')."""
    depth = frm.count("/")
    r = "../" * depth + to
    return r or "./"

# ------------------------------------------------------------------ pieces
def wa_link(l):
    return "https://wa.me/84944081101?text=" + quote(C[l]["ui"]["wa_text"])

def btn(kind, l, cls_extra=""):
    u = C[l]["ui"]
    if kind == "wa": return f'<a class="btn wa" href="{wa_link(l)}" target="_blank" rel="noopener">{u["book_wa"]}</a>'
    if kind == "tg": return f'<a class="btn tg" href="{TG}" target="_blank" rel="noopener">{u["tg_btn"]}</a>'
    if kind == "zalo": return f'<a class="btn zalo" href="{ZALO}" target="_blank" rel="noopener">{u["zalo_btn"]}</a>'
    if kind == "wc": return '<button class="btn wechat wcbtn" type="button">WeChat: vanphudalat</button>'
    if kind == "gmap": return f'<a class="btn alt" href="{GMAPS}" target="_blank" rel="noopener">{u["open_map"]}</a>'
    if kind == "amap": return f'<a class="btn alt" href="{AMAP}" target="_blank" rel="noopener">在高德地图中打开</a>'
    if kind == "yamap": return f'<a class="btn alt" href="{YANDEX_ORG_RU}" target="_blank" rel="noopener">Открыть в Яндекс Картах</a>'
    raise KeyError(kind)

HERO = {"ru": ["tg", "wa", "yamap", "wc"], "zh": ["wc", "wa", "amap", "gmap"], "vi": ["zalo", "wa", "gmap"]}
def hero_btns(l): return "\n".join(btn(k, l) for k in HERO.get(l, ["wa", "gmap"])) + f'\n<a class="btn callb" href="{TEL}">📞 {CALL[l][0]} {phone_txt(l)}</a>'

TEL = "tel:+84944081101"
CALL = {"vi": ("Gọi", "Điện thoại"), "en": ("Call", "Phone"), "ru": ("Позвонить", "Телефон"), "zh": ("电话", "电话"), "ko": ("전화", "전화"),
        "ja": ("電話", "電話"), "th": ("โทร", "โทรศัพท์"), "id": ("Telepon", "Telepon"), "ms": ("Telefon", "Telefon"), "de": ("Anrufen", "Telefon"),
        "fr": ("Appeler", "Téléphone"), "es": ("Llamar", "Teléfono"), "he": ("התקשרו", "טלפון"), "it": ("Chiama", "Telefono"), "nl": ("Bellen", "Telefoon"),
        "km": ("ហៅ", "ទូរស័ព្ទ"), "lo": ("ໂທ", "ໂທລະສັບ"), "my": ("ဖုန်းခေါ်", "ဖုန်း")}
# Owner's YouTube clips: by Google Maps cid (map/hub rows) and by article key (article pages)
VIDEO_CID = {"10570931153699557351": "gA532ZVEENM",   # Domaine de Marie (Mai Anh Dao church)
             "4046450182113774666": "sbj0q40Xq7w",    # Da Lat Cathedral (Chicken church)
             "ChIJgxSFnygTcTER6-xbx0o255o": "on6LKx_BZNo"}  # Don Bosco church (Salesian)
EV_VIDEO = "vJebSgBDFOo"  # owner's Shorts of the electric-scooter fleet at the shop (uploaded 2026-10-28)
VIDEO_ART = {"domainedemarie": "gA532ZVEENM", "lt-ev-foreigners": EV_VIDEO, "lt-ev-city": EV_VIDEO}
VIDEO_DATE = {"gA532ZVEENM": "2026-10-14", "vJebSgBDFOo": "2026-10-28"}  # upload dates for VideoObject schema
VLBL = {"vi": "Xem video", "en": "Watch the video", "ru": "Смотреть видео", "zh": "观看视频", "ko": "영상 보기", "ja": "動画を見る", "th": "ดูวิดีโอ",
        "id": "Tonton video", "ms": "Tonton video", "de": "Video ansehen", "fr": "Voir la vidéo", "es": "Ver el vídeo", "he": "צפו בסרטון",
        "it": "Guarda il video", "nl": "Bekijk de video", "km": "មើលវីដេអូ", "lo": "ເບິ່ງວິດີໂອ", "my": "ဗီဒီယိုကြည့်ရန်"}
def gmap(cid, lat=None, lng=None):
    """Google Maps link: numeric cid, or a place_id (ChIJ…) via the official Maps URL API."""
    if str(cid).startswith("ChIJ"):
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}&query_place_id={cid}"
    return f"https://maps.google.com/?cid={cid}"

def vlink(l, cid):
    v = VIDEO_CID.get(cid)
    return f' · <a href="https://www.youtube.com/shorts/{v}" target="_blank" rel="noopener">▶ {VLBL[l]}</a>' if v else ""
def vbox(l, v, title):
    return (f'<figure class="yt"><a href="https://www.youtube.com/shorts/{v}" target="_blank" rel="noopener" data-yt="{v}" aria-label="{VLBL[l]}: {title}">'
            f'<img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="{title}" loading="lazy" width="480" height="360"><span>▶</span></a>'
            f'<figcaption>▶ {VLBL[l]}</figcaption></figure>')
def phone_txt(l): return "0944 081 101" if l == "vi" else "+84 944 081 101"
TEL2 = "tel:+84834622149"
def phone2_txt(l): return "0834 622 149" if l == "vi" else "+84 834 622 149"
def call_float(l, pos): return f'<a class="float {pos} callf" href="{TEL}" aria-label="{CALL[l][1]} {phone_txt(l)}">📞 {CALL[l][0]}</a>'
def floats(l):
    if l == "ru":
        return call_float(l, "f3") + f'\n<a class="float f2 tgf" href="{TG}" target="_blank" rel="noopener">Telegram</a>\n<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'
    if l == "vi":
        return call_float(l, "f3") + f'\n<a class="float f2 zf" href="{ZALO}" target="_blank" rel="noopener">Zalo</a>\n<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'
    return call_float(l, "f2") + f'\n<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'

# Google Maps reviews block (real reviews only — never on-site star widgets)
REV = {
 "en": ("Guest reviews", "Read what real guests say about us on Google Maps — and leave your own review after your ride.", "★ Read reviews on Google Maps"),
 "ru": ("Отзывы гостей", "Почитайте настоящие отзывы наших гостей в Google Maps — и оставьте свой после поездки.", "★ Отзывы в Google Maps"),
 "zh": ("客人评价", "在 Google 地图上查看真实客人的评价，骑行结束后也欢迎留下您的评价。", "★ 查看 Google 地图评价"),
 "ko": ("고객 리뷰", "Google 지도에서 실제 고객들의 리뷰를 확인하고, 여행 후 리뷰도 남겨 주세요.", "★ Google 지도 리뷰 보기"),
 "ja": ("お客様の口コミ", "Googleマップで実際のお客様の口コミをご覧ください。ご利用後のレビューも大歓迎です。", "★ Googleマップの口コミを見る"),
 "th": ("รีวิวจากลูกค้า", "อ่านรีวิวจริงจากลูกค้าของเราบน Google Maps และฝากรีวิวของคุณหลังขี่เสร็จได้เลย", "★ อ่านรีวิวบน Google Maps"),
 "id": ("Ulasan tamu", "Baca ulasan asli dari tamu kami di Google Maps — dan tinggalkan ulasan Anda setelah berkendara.", "★ Lihat ulasan di Google Maps"),
 "ms": ("Ulasan pelanggan", "Baca ulasan sebenar pelanggan kami di Google Maps — dan tinggalkan ulasan anda selepas menunggang.", "★ Baca ulasan di Google Maps"),
 "vi": ("Đánh giá của khách", "Xem đánh giá thật của khách trên Google Maps — và để lại đánh giá của bạn sau chuyến đi.", "★ Xem đánh giá trên Google Maps"),
 "de": ("Bewertungen unserer Gäste", "Lies echte Bewertungen unserer Gäste auf Google Maps — und hinterlass deine eigene nach der Tour.", "★ Bewertungen auf Google Maps"),
 "fr": ("Avis de nos clients", "Lisez les vrais avis de nos clients sur Google Maps — et laissez le vôtre après votre balade.", "★ Voir les avis sur Google Maps"),
 "es": ("Opiniones de clientes", "Lee opiniones reales de nuestros clientes en Google Maps — y deja la tuya después de tu ruta.", "★ Ver opiniones en Google Maps"),
 "he": ("ביקורות של לקוחות", "קראו ביקורות אמיתיות של הלקוחות שלנו ב-Google Maps — והשאירו ביקורת משלכם אחרי הנסיעה.", "★ ביקורות ב-Google Maps"),
}
for _l in _NEWL: REV[_l] = importlib.import_module(f"content.{_l}").REV_
def rev_btn(l): return f'<a class="btn alt" href="{GMAPS}" target="_blank" rel="noopener" style="border:1px solid var(--line)">{REV[l][2]}</a>'
def map_path(M, l): return lang_root(l) + (M.SLUG[l] if isinstance(M.SLUG, dict) else M.SLUG) + "/"
def pm_path(l): return map_path(PM, l)
def hub_btn(l, me):
    if l not in HUB.LANGS: return ""
    return f'<a class="btn" href="{rel(me, lang_root(l) + HUB.SLUG[l] + "/")}">🧭 {HUB.T[l]["h1"].format(n=len(HUB.spots(l)))} →</a> '
def pm_section(l, me):
    if l not in PM.LANGS: return ""
    t = PM.T[l]
    g = PG.T[l]
    return (f'<section class="pmsec"><h2>📍 {t["h1"]}</h2><p>{t["lead"]}</p><p>{hub_btn(l, me)}<a class="btn" href="{rel(me, pm_path(l))}">{t["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(PG, l))}" style="border:1px solid var(--line)">🛕 {g["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(CH, l))}" style="border:1px solid var(--line)">⛪ {CH.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(SF, l))}" style="border:1px solid var(--line)">🌼 {SF.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(CL, l))}" style="border:1px solid var(--line)">☁️ {CL.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(WF, l))}" style="border:1px solid var(--line)">💧 {WF.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(CF, l))}" style="border:1px solid var(--line)">☕ {CF.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(NC, l))}" style="border:1px solid var(--line)">🌃 {NC.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(NM, l))}" style="border:1px solid var(--line)">🍜 {NM.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(BB, l))}" style="border:1px solid var(--line)">🍖 {BB.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(HT, l))}" style="border:1px solid var(--line)">🏨 {HT.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(H4, l))}" style="border:1px solid var(--line)">🛎️ {H4.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(H3, l))}" style="border:1px solid var(--line)">🛏️ {H3.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(BU, l))}" style="border:1px solid var(--line)">🚌 {BU.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(DN, l))}" style="border:1px solid var(--line)">🚌 {DN.T[l]["h1"]} →</a> '
            f'<a class="btn alt" href="{rel(me, map_path(NT, l))}" style="border:1px solid var(--line)">🚐 {NT.T[l]["h1"]} →</a>'
            + (f' <a class="btn alt" href="{rel(me, halal_path())}" style="border:1px solid var(--line)">🥘 {HI.H1} →</a>' if l == "id" else "")
            + (f' <a class="btn alt" href="{rel(me, lang_root(l) + DAY.SLUG[l] + "/")}" style="border:1px solid var(--line)">🛵 {DAY.T[l]["h1"]} →</a>' if l in DAY.LANGS else "") + '</p></section>')
# Real Google Maps reviews, quoted verbatim (excerpts marked with …), shown in the original language.
# Shown as visible quotes only: no Review/AggregateRating schema, because Google's rules forbid
# marking up reviews copied from another site (Google Maps). Add new ones only from real reviews.
REVIEWS = [
 ("jan", "Jan B. P.", "en", "Best motorbike renting site in Da Lat. Motorbikes were really good (air blade 125cc). Phu was fenomenal. We highly recommend this place."),
 ("keziah", "Keziah S.", "en", "It's great to rent a motorbike to explore Dalat for flexible plans! Mr. Phu was very accommodating to my requests (regarding the timing) and even extension. He's also punctual and motorbike was in very good condition ❤"),
 ("marina", "Марина М.", "ru", "Брали 2 байка, оба в отличном состоянии, новые, плавные, тянут любую горку, тормоза хорошие… Владелец всегда на связи, приятные люди."),
 ("elvan", "Elvan T.", "en", "This is a highly recommended motorbike rental service in Dalat, everything is just so easy and owner Phu send the motorbike to my hotel as I have contacted him few days before I checked in hotel. Phu is friendly and humble… everything just settled at the door step."),
 ("peter", "Peter C.", "en", "Good bike and good experience with the owner. Will rent here again."),
]
def rev_cards(ids=None):
    out = []
    for rid, who, rl, txt in REVIEWS:
        if ids and rid not in ids: continue
        out.append(f'<figure class="rv"><div class="st" aria-label="5/5">★★★★★</div><blockquote lang="{rl}" dir="ltr">“{txt}”</blockquote>'
                   f'<figcaption dir="ltr">— {who} · <a href="{GMAPS}" target="_blank" rel="noopener">Google Maps</a></figcaption></figure>')
    return '<div class="revs">' + "".join(out) + '</div>'
def rev_more(l):
    b = f'<a class="btn alt" href="{TRIPADVISOR}" target="_blank" rel="noopener" style="border:1px solid var(--line)">★ Tripadvisor</a>'
    return b + f' <a class="btn alt" href="{ya_org(l)}" target="_blank" rel="noopener" style="border:1px solid var(--line)">★ {ya_name(l)}</a>'
def rev_section(l, ids=None): return f'<section><h2>{REV[l][0]}</h2><p>{REV[l][1]}</p>{rev_cards(ids)}<p>{rev_btn(l)} {rev_more(l)}</p></section>'

def contact_box(l):
    u = C[l]["ui"]
    if l == "ru":
        b = f'<a class="btn tg" href="{TG_CHANNEL}" target="_blank" rel="noopener">{u["box_btn"]}</a>'
    elif l == "zh":
        b = ('<img src="/img/wechat-qr.png" alt="微信二维码 vanphudalat — 大叻租摩托车" width="280" height="375" '
             'style="display:block;max-width:280px;width:100%;height:auto;border-radius:12px;margin:0 0 12px;background:#fff">'
             + btn("wc", l))
    elif l == "vi":
        b = btn("zalo", l)
    else:
        b = f'<a class="btn wa" href="{wa_link(l)}" target="_blank" rel="noopener">{u["box_btn"]}</a>'
    return f'<div class="box"><h2>{u["box_title"]}</h2><p>{u["box_text"]}</p>{b}</div>'

def kw_rent(l): return C[l]["ui"]["alt"].split(" — ")[0]

def cta_box(l, frm):
    u = C[l]["ui"]
    first = {"ru": "tg", "vi": "zalo", "zh": "wc"}.get(l)
    btns = (btn(first, l) + "\n" if first else "") + btn("wa", l)
    return f"""<div class="cta-box"><h2>{u["cta_title"]}</h2><p>{u["cta_text"]}</p>
<div class="cta">{btns}
<a class="btn alt" href="{rel(frm, home_path(l))}">{u["cta_prices"]}</a>
{rev_btn(l)}</div>
<p class="kw"><a href="{rel(frm, home_path(l))}">{kw_rent(l)}</a> · <a href="{rel(frm, ev_path(l))}">{EV[l]["h1"]}</a></p></div>"""

OLD_ADDR = "Khu Quy Hoạch/L8 Đường Bùi Thị Xuân, Xuân Hương - Đà Lạt, Lâm Đồng 670000"
NAP_MAP = OLD_ADDR
NAP_REAL = "1/15/5 Thông Thiên Học, Xuân Hương - Đà Lạt, Lâm Đồng 670000"
SHOP_ADDR_LBL = {  # label above the shop address on the rental home page (for guests booking a Grab to the shop)
 "vi": "Địa chỉ tiệm (để đặt Grab):", "en": "Shop address (for Grab):", "ru": "Адрес магазина (для Grab):", "zh": "店铺地址（打 Grab 前往）：",
 "ko": "가게 주소 (Grab 이용 시):", "ja": "店舗住所（Grabで行く場合）：", "th": "ที่อยู่ร้าน (สำหรับเรียก Grab):", "id": "Alamat toko (untuk Grab):",
 "ms": "Alamat kedai (untuk Grab):", "de": "Shop-Adresse (für Grab):", "fr": "Adresse de la boutique (pour Grab) :", "es": "Dirección de la tienda (para Grab):",
 "he": "כתובת החנות (לנסיעה ב-Grab):", "it": "Indirizzo del negozio (per Grab):", "nl": "Winkeladres (voor Grab):", "km": "អាសយដ្ឋានហាង (សម្រាប់ Grab)៖",
 "lo": "ທີ່ຢູ່ຮ້ານ (ສຳລັບ Grab):", "my": "ဆိုင်လိပ်စာ (Grab အတွက်):"}
NAP_LBL = {  # (title, Google Maps address label, actual shop location label)
 "vi": ("Văn Phú Đà Lạt – Dịch vụ cho thuê xe máy uy tín", "Địa chỉ Google Maps (đồng bộ):", "Vị trí cửa hàng thực tế:"),
 "en": ("Van Phu Dalat – Motorbike Rental", "Google Maps address:", "Actual shop location:"),
 "ru": ("Van Phu Dalat – аренда байков", "Адрес в Google Maps:", "Фактическое расположение:"),
 "zh": ("Van Phu 大叻摩托车租赁", "Google 地图地址：", "店铺实际位置："),
 "ko": ("Van Phu 달랏 오토바이 렌탈", "Google 지도 주소:", "실제 가게 위치:"),
 "ja": ("Van Phu ダラット バイクレンタル", "Google マップの住所：", "実際の店舗所在地："),
 "th": ("Van Phu Dalat – เช่ามอเตอร์ไซค์", "ที่อยู่ใน Google Maps:", "ที่ตั้งร้านจริง:"),
 "id": ("Van Phu Dalat – Sewa Motor", "Alamat Google Maps:", "Lokasi toko sebenarnya:"),
 "ms": ("Van Phu Dalat – Sewa Motosikal", "Alamat Google Maps:", "Lokasi kedai sebenar:"),
 "de": ("Van Phu Dalat – Rollervermietung", "Adresse auf Google Maps:", "Tatsächlicher Standort:"),
 "fr": ("Van Phu Dalat – Location de scooters", "Adresse Google Maps :", "Emplacement réel de la boutique :"),
 "es": ("Van Phu Dalat – Alquiler de motos", "Dirección en Google Maps:", "Ubicación real de la tienda:"),
 "he": ("Van Phu Dalat – השכרת קטנועים", "הכתובת ב-Google Maps:", "מיקום החנות בפועל:"),
 "it": ("Van Phu Dalat – Noleggio scooter", "Indirizzo su Google Maps:", "Posizione reale del negozio:"),
 "nl": ("Van Phu Dalat – Scooterverhuur", "Adres op Google Maps:", "Werkelijke locatie van de winkel:"),
 "km": ("Van Phu Dalat – ជួលម៉ូតូ", "អាសយដ្ឋាន Google Maps៖", "ទីតាំងហាងពិតប្រាកដ៖"),
 "lo": ("Van Phu Dalat – ເຊົ່າລົດຈັກ", "ທີ່ຢູ່ໃນ Google Maps:", "ທີ່ຕັ້ງຮ້ານຕົວຈິງ:"),
 "my": ("Van Phu Dalat – ဆိုင်ကယ်ငှား", "Google Maps လိပ်စာ:", "ဆိုင်တည်နေရာအမှန်:"),
}
def nap_block(l):
    t, a, b = NAP_LBL.get(l, NAP_LBL["en"])
    return (f'<div class="napbox" lang="vi"><div class="nt">{t}</div>'
            f'<div class="nl"><i>📍</i><div><span class="lbl" lang="{l}">{b}</span><b>{NAP_REAL}</b></div></div>'
            f'<div class="nl"><i>🗺️</i><div><span class="lbl" lang="{l}">{a}</span><a href="{GMAPS}" target="_blank" rel="noopener">{NAP_MAP}</a></div></div>'
            f'<div class="nl"><i>📞</i><div>0944 081 101 · 0834 622 149</div></div></div>')
OLD_ADDR_LBL = {"vi": "Địa chỉ cũ (trên Google Maps):", "en": "Old address (as shown on Google Maps):", "ru": "Старый адрес (как в Google Maps):",
    "zh": "旧地址（Google 地图显示）：", "ko": "이전 주소 (Google 지도 표기):", "ja": "旧住所（Google マップ表記）：", "th": "ที่อยู่เดิม (ตามที่แสดงใน Google Maps):",
    "id": "Alamat lama (di Google Maps):", "ms": "Alamat lama (di Google Maps):", "de": "Alte Adresse (so auf Google Maps):", "fr": "Ancienne adresse (affichée sur Google Maps) :",
    "es": "Dirección antigua (como aparece en Google Maps):", "he": "כתובת קודמת (כפי שמופיעה ב-Google Maps):", "it": "Vecchio indirizzo (come su Google Maps):",
    "nl": "Oud adres (zoals op Google Maps):", "km": "អាសយដ្ឋានចាស់ (នៅលើ Google Maps)៖", "lo": "ທີ່ຢູ່ເກົ່າ (ຕາມ Google Maps):", "my": "လိပ်စာဟောင်း (Google Maps တွင်):"}
def old_addr_row(l): return f'<p><b>{OLD_ADDR_LBL.get(l, OLD_ADDR_LBL["en"])}</b> <a href="{GMAPS}" target="_blank" rel="noopener">{OLD_ADDR}</a></p>'
def contacts(l):
    h = C[l]["home"]
    rows = [("📞", f'<b>{CALL[l][1]}:</b> <a href="{TEL}">{phone_txt(l)}</a> · <a href="{TEL2}">{phone2_txt(l)}</a>'),
            ("💬", f'<b>WhatsApp:</b> <a href="{wa_link(l)}">+84 944 081 101</a> · <a href="{WA2}">+84 834 622 149</a>'),
            ("📱", f'<b>Zalo:</b> <a href="{ZALO}">0944 081 101</a>'),
            ("✈️", f'<b>Telegram:</b> <a href="{TG}">@vanphudalat</a>')]
    if l == "ru":
        rows.append(("📢", f'<b>Telegram-канал:</b> <a href="{TG_CHANNEL}">@dalat_life_vietnam</a>'))
    rows += [("🗨️", '<b>WeChat:</b> vanphudalat'),
             ("👍", '<b>Facebook:</b> <a href="https://www.facebook.com/vanphudalat">facebook.com/vanphudalat</a>'),
             ("▶️", f'<b>YouTube:</b> <a href="{YT}" target="_blank" rel="noopener">@DalatMotorbikeRentalVanPhu</a>'),
             ("🎵", f'<b>TikTok:</b> <a href="{TIKTOK}" target="_blank" rel="noopener">@bietthudalat</a> ({TT_LBL.get(l, TT_LBL["en"])})'),
             ("🦉", f'<b>Tripadvisor:</b> <a href="{TRIPADVISOR}" target="_blank" rel="noopener">Van Phu Dalat Motorbike Rental</a>'),
             ("🧭", f'<b>{ya_name(l)}:</b> <a href="{ya_org(l)}" target="_blank" rel="noopener">Van Phu</a>'),
             ("📍", f'<b>{h["addr_label"]}</b> {h["address"]}')]
    out = "".join(f'<div class="crow"><i>{i}</i><div>{c}</div></div>' for i, c in rows)
    return f'<div class="contact">{out}<div class="crow muted"><i>🗺️</i><div><b>{OLD_ADDR_LBL.get(l, OLD_ADDR_LBL["en"])}</b> <a href="{GMAPS}" target="_blank" rel="noopener">{OLD_ADDR}</a></div></div></div>'

def langbar(l, kind, key, frm):
    out = ""
    for x in langs_of(kind, key):
        cls = ' class="on" aria-current="page"' if x == l else ""
        out += f'<a href="{rel(frm, path_of(x, kind, key))}" hreflang="{x}" data-l="{x}"{cls}>{LABEL[x]}</a>'
    return f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{out}</div></div>'

def ldjson(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>"

def head(l, kind, key, title, desc, ld, img="electric-row"):
    me = path_of(l, kind, key)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + path_of(x, kind, key)}">\n' for x in langs_of(kind, key))
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE + path_of("en", kind, key)}">\n'
    return f"""<!doctype html>
<html lang="{l}"{' dir="rtl"' if l == "he" else ""}>
<head>
<meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[l]}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE + me}">
<meta property="og:image" content="{BASE}img/{img}.jpg">
{"".join(ldjson(x) for x in ld)}
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>"""

def id_funnel():
    """Indonesian-only funnel block above the footer of every /id/ page (content/funnelid.py)."""
    asks = "".join(f'<a class="btn wa" href="https://wa.me/84944081101?text={quote(m)}" target="_blank" rel="noopener">{_esc(b)}</a>' for b, m in FI.ASKS)
    faq = "".join(f'<details><summary>{_esc(q)}</summary><p>{_esc(a)}</p></details>' for q, a in FI.FAQ)
    return (f'<div class="wrap idf" style="padding-bottom:24px"><section class="box" id="konsultasi"><h2>{_esc(FI.H2)}</h2><p>{_esc(FI.LEAD)}</p><div class="cta">{asks}</div>'
            f'<p>{_esc(FI.HALAL_LINE)} <a href="/{halal_path()}">{_esc(FI.HALAL_LINK)}</a>.</p></section>'
            f'<section><h2>{_esc(FI.REV_H)}</h2>{rev_cards(FI.REV_IDS)}</section>'
            f'<section class="faq"><h2>{_esc(FI.FAQ_H)}</h2>{faq}</section></div>')

def foot(l, root_redirect=False, frm=None):
    u = C[l]["ui"]
    redirect = ""
    if root_redirect:
        redirect = ("(function(){if(/bot|crawl|spider|slurp|yandex|google|bing|baidu/i.test(navigator.userAgent))return;let p=null;try{p=localStorage.getItem('lang')}catch(e){}"
                    "const ok=" + json.dumps(LANGS) + ";let t=p;if(!t){const ls=navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'en'];"
                    "for(const x of ls){let n=x.toLowerCase().slice(0,2);if(n==='in')n='id';if(n==='iw')n='he';if(ok.includes(n)){t=n;break}}}"
                    "if(t&&t!=='en'&&ok.includes(t))location.replace(t+'/');})();")
    kw = ""
    if frm is not None:
        kw = f'<br><a href="{rel(frm, home_path(l))}">{kw_rent(l)}</a> · <a href="{rel(frm, ev_path(l))}">{EV[l]["h1"]}</a> · <a href="{rel(frm, routes_path(l))}">{C[l]["routes"]["h1"]}</a>'
        if l in AB.LANGS:
            kw += f' · <a href="{rel(frm, about_path(l))}">{AB.T[l]["foot"]}</a>'
        if l == "vi":
            kw += f' · <a href="{rel(frm, home_path("vi") + "phuong-xuan-huong/")}">Thuê xe máy theo tuyến đường phường Xuân Hương</a>'
    pre = id_funnel() if l == "id" else ""
    return pre + f"""<footer><div class="fcalls"><a class="fp call" href="{TEL}">📞 {CALL[l][1]}: {phone_txt(l)}</a><a class="fp" href="{TEL2}">📞 {phone2_txt(l)}</a><a class="fp yt" href="{YT}" target="_blank" rel="noopener">▶ YouTube</a></div>{nap_block(l)}{u["footer"]}{kw}</footer>
{floats(l)}
<div class="lb" id="lb"><img alt=""></div>
<script>
document.querySelectorAll('.langs a').forEach(a=>a.addEventListener('click',()=>{{try{{localStorage.setItem('lang',a.dataset.l)}}catch(e){{}}}}));
document.querySelectorAll('.wcbtn').forEach(b=>b.onclick=()=>{{try{{navigator.clipboard.writeText('vanphudalat')}}catch(e){{}};b.textContent={json.dumps(u["copied"], ensure_ascii=False)};setTimeout(()=>b.textContent='WeChat: vanphudalat',2000)}});
document.querySelectorAll('.yt a[data-yt]').forEach(a=>a.onclick=e=>{{e.preventDefault();a.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+a.dataset.yt+'?autoplay=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="video"></iframe>'}});
const lb=document.getElementById('lb');document.querySelectorAll('.gallery img').forEach(i=>i.onclick=()=>{{lb.querySelector('img').src=i.dataset.full||i.src;lb.classList.add('on')}});lb.onclick=()=>lb.classList.remove('on');
{redirect}
</script>
</body>
</html>
"""

def business_ld(l, url):
    h, u = C[l]["home"], C[l]["ui"]
    return {"@context": "https://schema.org", "@type": ["LocalBusiness", "AutoRental"], "@id": BASE + "#business",
            "name": "Van Phu Dalat Motorbike Rental", "alternateName": ["Thuê xe máy Đà Lạt Văn Phú", "Văn Phú Đà Lạt", "Dalat Motorbike Rental"],
            "areaServed": {"@type": "City", "name": "Da Lat", "alternateName": ["Đà Lạt", "Dalat"]},
            "currenciesAccepted": "VND", "foundingDate": AB.SINCE,
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "opens": "04:30", "closes": "21:00"}],
            "knowsAbout": ["motorbike rental", "scooter rental", "electric scooter rental", "Da Lat motorbike routes"],
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in
                               ["Free helmet", "Phone holder", "1 liter of fuel (gas scooters)", "Free hotel delivery in central Da Lat (2+ days)", "No cash deposit (passport or ID held)"]],
            "description": h["desc"], "url": BASE + home_path("en"), "image": BASE + "img/electric-row.jpg",
            "telephone": "+84944081101", "contactPoint": [{"@type": "ContactPoint", "telephone": t, "contactType": "customer service", "areaServed": "VN", "availableLanguage": ["Vietnamese", "English"]} for t in ("+84944081101", "+84834622149")], "priceRange": "120,000–150,000 VND",
            "address": {"@type": "PostalAddress", "streetAddress": "1/15/5 Thông Thiên Học", "addressLocality": "Xuân Hương – Đà Lạt", "addressRegion": "Lâm Đồng", "postalCode": "670000", "addressCountry": "VN"},
            "disambiguatingDescription": "Địa chỉ mới: 1/15/5 Thông Thiên Học, Xuân Hương – Đà Lạt, Lâm Đồng. Địa chỉ trên Google Maps (cùng một cửa hàng): Khu Quy Hoạch/L8 Đường Bùi Thị Xuân, Xuân Hương - Đà Lạt, Lâm Đồng 670000. Vị trí thực tế: 1/15/5 Thông Thiên Học, Xuân Hương - Đà Lạt, Lâm Đồng 670000.",
            "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON}, "hasMap": GMAPS,
            "sameAs": ["https://www.facebook.com/vanphudalat", YT, TIKTOK, TG, ZALO, TRIPADVISOR, YANDEX_ORG],
            "makesOffer": [{"@type": "Offer", "name": n, "price": "150000", "priceCurrency": "VND"}
                           for n in ["Honda Vision 110cc", "Honda Air Blade 125cc", h["electric_name"]]] + [{"@type": "Offer", "name": "Manual bike (Sirius FI, Wave RSX)", "price": "120000", "priceCurrency": "VND"}]}

# --- About / Giới thiệu (owner asked 2026-11-04, vi + en; no prices on these blocks) ---
def about_path(l): return AB.SLUG[l]
def about_l(l): return l if l in AB.LANGS else "en"
PERSON_ID = BASE + "#phu"
def person_ld():
    return {"@type": "Person", "@id": PERSON_ID, "name": "Ngô Văn Phú", "alternateName": "Phu", "jobTitle": "Owner",
            "image": f"{BASE}img/{AB.IMG}.jpg", "url": BASE + about_path("en"), "worksFor": {"@id": BASE + "#business"},
            "knowsLanguage": ["vi", "en"], "sameAs": [YT, TIKTOK, "https://www.facebook.com/vanphudalat"]}
def _owner_card(l, frm, cls, bold, txt, link):
    pre = "../" * frm.count("/")
    return (f'<div class="{cls}" style="display:flex;gap:14px;align-items:center;border:1px solid var(--line);border-radius:12px;padding:14px;margin:24px 0">'
            f'<img src="{pre}img/{AB.IMG}.jpg" alt="Ngô Văn Phú – Văn Phú Đà Lạt" width="72" height="72" loading="lazy" style="width:72px;height:72px;border-radius:50%;object-fit:cover;flex:none">'
            f'<p style="margin:0"><b>{bold}</b> – {txt} <a href="{rel(frm, about_path(l))}">{link} →</a></p></div>')
def author_box(l, frm):
    if l not in AB.LANGS: return ""
    t = AB.T[l]; return _owner_card(l, frm, "author-box", t["author"], t["author_txt"], t["author_link"])
def meet_owner(l, frm):
    if l not in AB.LANGS: return ""
    t = AB.T[l]; return _owner_card(l, frm, "meet-owner", t["meet"], t["meet_txt"], t["meet_link"])

def posts(l, frm, keys):
    a = C[l]["articles"]
    return '<div class="posts">' + "".join(
        f'<a class="post" href="{rel(frm, art_path(l, k))}"><b>{a[k][2]}</b><span>{a[k][3]}</span></a>' for k in keys) + "</div>"

# ------------------------------------------------------------------ pages
# Manual bikes (xe số Sirius FI / Wave RSX): owner asked 2026-11-04 to show 120,000 VND/day in the price table of every rental page.
XS_NAME = {"vi": "Xe số (Sirius FI, Wave RSX)", "en": "Manual bike (Sirius FI, Wave RSX)", "ru": "Байк с механикой (Sirius FI, Wave RSX)",
  "zh": "手动挡摩托车（Sirius FI、Wave RSX）", "ko": "기어 오토바이 (Sirius FI, Wave RSX)", "ja": "マニュアルバイク（Sirius FI・Wave RSX）",
  "th": "รถเกียร์ (Sirius FI, Wave RSX)", "id": "Motor bebek (Sirius FI, Wave RSX)", "ms": "Motosikal kapcai (Sirius FI, Wave RSX)",
  "de": "Schaltmoped (Sirius FI, Wave RSX)", "fr": "Moto à vitesses (Sirius FI, Wave RSX)", "es": "Moto de marchas (Sirius FI, Wave RSX)",
  "he": "אופנוע ידני (Sirius FI, Wave RSX)", "it": "Moto con marce (Sirius FI, Wave RSX)", "nl": "Schakelbrommer (Sirius FI, Wave RSX)",
  "km": "ម៉ូតូលេខ (Sirius FI, Wave RSX)", "lo": "ລົດເກຍ (Sirius FI, Wave RSX)", "my": "ဂီယာဆိုင်ကယ် (Sirius FI, Wave RSX)"}
def xs_price(l): return C[l]["home"].get("price_cell", "150,000 VND").replace("150", "120")
def xs_row(l, me):
    n = XS_NAME.get(l, XS_NAME["en"])
    if l == "vi": n = f'<a href="{rel(me, home_path("vi") + "thue-xe-so-da-lat/")}">{n}</a>'
    return f'<tr><td>{n}</td><td><b>{xs_price(l)}</b></td></tr>'

def page_home(l):
    h, u = C[l]["home"], C[l]["ui"]
    me = home_path(l)
    pre = rel(me, "")
    if pre == "./": pre = ""
    url = BASE + me
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in h["faq"]]}
    alt = u["alt"]
    conds = "".join(f"<li><b>{b}</b> — {t}</li>" for b, t in h["conditions"])
    steps = "".join(f"<li>{s}</li>" for s in h["steps"])
    facts = "".join(f"<li>{h['conditions'][i][0]}</li>" for i in (0, 2, 3, 4))
    rules = "".join(f'<div class="rule"><span class="ic">{ic}</span><b>{r}</b></div>' for ic, r in zip(["🚫🍺", "🚦"], h["rules"]))
    why = "".join(f"<p>{p}</p>" for p in h["why"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in h["faq"])
    if l == "ru":
        mp = f'<iframe class="map" src="{YA_WIDGET}" loading="lazy" title="Яндекс Карты" allowfullscreen></iframe><p class="note"><a href="{YANDEX_ORG_RU}" target="_blank" rel="noopener">Яндекс Карты</a> · <a href="{GMAPS}" target="_blank" rel="noopener">Google Maps</a></p>'
    else:
        mp = f'<iframe class="map" src="https://maps.google.com/maps?q={LAT},{LON}&hl={l}&z=17&output=embed" loading="lazy" title="Google Maps"></iframe><p class="note"><a href="{GMAPS}" target="_blank" rel="noopener">Google Maps</a>' + (f' · <a href="{AMAP}" target="_blank" rel="noopener">高德地图</a>' if l == "zh" else "") + '</p>'
    imgs = [("electric-row", 1), ("airblade", 2), ("electric-helmets", 3), ("fleet-gas", 4), ("vision-white", 5), ("guest-1", 6), ("guest-2", 7)]
    galts = h.get("gallery_alts")
    gallery = "".join(f'<img src="{pre}img/{n}.jpg" alt="{galts[i-1] if galts else f"{alt} {i}"}" loading="lazy">' for n, i in imgs)
    cmp_sec = ""
    if h.get("compare"):
        hd = "".join(f"<th>{c}</th>" for c in h["compare_head"])
        rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in h["compare"])
        cmp_sec = f'<section><h2>{h["h_compare"]}</h2><div style="overflow-x:auto"><table class="price">{"<tr>"+hd+"</tr>"}{rows}</table></div></section>'
    tips_sec = ""
    if h.get("tips"):
        tips_sec = '<section class="prose"><h2>' + h["h_tips"] + '</h2><ul>' + "".join(f"<li><b>{b}</b> — {t}</li>" for b, t in h["tips"]) + "</ul></section>"
    upd = f'<p class="note">{h["updated"]}</p>' if h.get("updated") else ""
    body = f"""
<header class="hh"><div class="wrap">{langbar(l, "home", None, me)}</div>
<div class="hh-hero">
 <img class="heroimg" src="{pre}img/electric-row.jpg" alt="{alt}" width="1200" height="675">
 <div class="wrap hh-in">
 <h1>{h["h1"]}</h1>
 <p class="lead">{h["lead"]}</p>
 <div class="ticket">{h["price_badge"]}</div>
 <div class="cta">{hero_btns(l)}</div>
<p class="shopaddr" style="margin:12px 0 0;font-size:15px;color:#fff;opacity:.95"><b>{SHOP_ADDR_LBL.get(l, SHOP_ADDR_LBL["en"])}</b><br>1/15/5 Thông Thiên Học, Xuân Hương – Đà Lạt, Lâm Đồng</p>
</div></div>
<div class="facts"><ul>{facts}</ul></div></header>
<main class="wrap home">
 <div class="two"><section><h2>{h["h_prices"]}</h2>
  <table class="price"><tr><th>{h["th_bike"]}</th><th>{h["th_price"]}</th></tr>
  <tr><td>Honda Vision 110cc</td><td><b>{h.get("price_cell", "150,000 VND")}</b></td></tr>
  <tr><td>Honda Air Blade 125cc</td><td><b>{h.get("price_cell", "150,000 VND")}</b></td></tr>
  <tr><td>{h["electric_name"]}</td><td><b>{h.get("price_cell", "150,000 VND")}</b></td></tr>{xs_row(l, me)}</table>
  <p class="note">{h["price_note"]}</p>{upd}</section>
 <section><h2>{h["h_conditions"]}</h2><ul class="checks">{conds}</ul></section></div>
 {cmp_sec}
 <section><h2>{h["h_fleet"]}</h2><div class="grid">
  <div class="card"><img src="{pre}img/vision-white.jpg" alt="Honda Vision 110cc — {alt}" loading="lazy"><b>Honda Vision 110cc</b><span>{h["vision"]}</span></div>
  <div class="card"><img src="{pre}img/airblade.jpg" alt="Honda Air Blade 125cc — {alt}" loading="lazy"><b>Honda Air Blade 125cc</b><span>{h["airblade"]}</span></div>
  <div class="card"><img src="{pre}img/electric-helmets.jpg" alt="{h["electric_name"]} — {alt}" loading="lazy"><b><a href="{rel(me, ev_path(l))}">{h["electric_name"]}</a></b><span>{h["electric"]} <a href="{rel(me, ev_path(l))}">{EV[l]["more"]}</a></span></div>
 </div></section>
 <section><h2>{h["h_how"]}</h2><ol class="steps">{steps}</ol></section>
 {tips_sec}
 <section><h2>{h["h_rules"]}</h2><div class="rules">{rules}</div></section>
 <section class="prose"><h2>{h["h_why"]}</h2>{why}
  <p><a class="btn alt" href="{rel(me, routes_path(l))}" style="border:1px solid var(--line)">{h["routes_btn"]}</a></p></section>
 <section><h2>{h["h_photos"]}</h2><div class="gallery">{gallery}</div></section>
 {meet_owner(l, me)}
 {rev_section(l)}
 {pm_section(l, me)}
 <section class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px"><p>{FE.T[l]["desc"]}</p><p><a class="btn" href="{rel(me, map_path(FE, l))}">🌸 {FE.T[l]["h1"]} →</a></p></section>
 <section class="faq"><h2>{h["h_faq"]}</h2>{faq}</section>
 <section><h2>{u["blog_h"]}</h2>{posts(l, me, arts(l)[::-1][:6])}</section>
 <section><h2>{h["h_map"]}</h2>{mp}</section>
 <section>{contact_box(l)}</section>
 <section><h2>{h["h_contacts"]}</h2>{contacts(l)}</section>
</main>
"""
    return head(l, "home", None, h["title"], h["desc"], [business_ld(l, url), faq_ld]) + body + foot(l, frm=me)

def crumbs(l, me, items):
    u = C[l]["ui"]
    parts = [f'<a href="{rel(me, home_path(l))}">{u["crumbs_home"]}</a>']
    for name, path in items:
        parts.append(f'<a href="{rel(me, path)}">{name}</a>' if path else name)
    return '<div class="crumbs">' + " › ".join(parts) + "</div>"

def crumbs_ld(l, items):
    u = C[l]["ui"]
    el = [{"@type": "ListItem", "position": 1, "name": u["crumbs_home"], "item": BASE + home_path(l)}]
    for i, (n, p) in enumerate(items, 2):
        el.append({"@type": "ListItem", "position": i, "name": n, "item": BASE + p})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}

def _rh_link(l, me, key):
    if key.startswith("art:"): return rel(me, art_path(l, key[4:]))
    return {"day": lambda: rel(me, day_path(l)) if l in DAY.LANGS else None, "tm": lambda: rel(me, tm_path(l)) if l in TM.LANGS else None,
            "hub": lambda: rel(me, hub_path(l)) if l in HUB.LANGS else None, "pm": lambda: rel(me, pm_path(l)), "wf": lambda: rel(me, map_path(WF, l)),
            "cl": lambda: rel(me, map_path(CL, l)), "lic": lambda: rel(me, lic_path(l)), "arr": lambda: rel(me, arr_path(l)), "ev": lambda: rel(me, ev_path(l))}[key]()
def page_routes(l):
    r, u = C[l]["routes"], C[l]["ui"]
    me = routes_path(l)
    items = "".join(f'<div class="route"><h3>{i}. {t}</h3><div class="meta">{m}</div><p>{d}</p><p><i>{tip}</i></p></div>'
                    for i, (t, m, d, tip) in enumerate(r["items"], 1))
    tips = "".join(f"<li>{t}</li>" for t in r["tips"])
    x = RH.T.get(l)
    hub = ""; lds_extra = []
    if x:
        rows = "".join(f'<tr><td>{t}</td><td>{x["km"].format(d=d)}</td><td>{x["why"][w]}</td><td><b>{x["bike"][b]}</b></td></tr>'
                       for (t, *_), (d, w, b) in zip(r["items"], RH.ROWS))
        def chips(keys, labels):
            return "".join(f'<a href="{h}">{labels[k]} →</a>' for k in keys for h in [_rh_link(l, me, k)] if h)
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in x["faq"])
        hub = f"""
 <section><h2>{x["h_bike"]}</h2><p>{x["bike_intro"]}</p><table class="price"><tr>{"".join(f"<th>{c}</th>" for c in x["cols"])}</tr>{rows}</table></section>
 <section class="prose"><h2>{x["ev_h"]}</h2>{x["ev_html"]}<p><a class="btn alt" href="{rel(me, ev_path(l))}" style="border:1px solid var(--line)">⚡ {EV[l]["h1"]} →</a></p></section>
 <section><h2>{x["plan_h"]}</h2><p class="chips">{chips(RH.PLAN, x["plan"])}</p></section>
 <section><h2>{x["before_h"]}</h2><p class="chips">{chips(RH.BEFORE, x["before"])}</p></section>
 <section class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px"><h2>{x["cta_h"]}</h2><p>{x["cta"]}</p><p><a class="btn" href="{rel(me, home_path(l))}">{kw_rent(l)} →</a></p></section>
 <section class="faq"><h2>{x["faq_h"]}</h2>{faq}</section>"""
        lds_extra = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x["faq"]]},
                     {"@context": "https://schema.org", "@type": "ItemList", "name": r["h_list"], "itemListElement": [{"@type": "ListItem", "position": i, "name": t} for i, (t, *_) in enumerate(r["items"], 1)]}]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": r["h1"], "description": r["desc"], "inLanguage": l, "mainEntityOfPage": BASE + me,
           "image": BASE + "img/airblade.jpg", "datePublished": "2026-10-10", "dateModified": RH.UPDATED if x else "2026-10-10",
           "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}}
    body = f"""
<header><div class="wrap">{langbar(l, "routes", None, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_routes"], None)])}
 <h1>{r["h1"]}</h1><p class="lead">{r["lead"]}</p>{f'<p class="upd"><time datetime="{RH.UPDATED}">{UPD[l]}: {fdate(l, RH.UPDATED)}</time></p>' if x else ""}
 <div class="cta">{hero_btns(l)}</div>
</div></div></header>
<main class="wrap">
 <section><h2>{r["h_list"]}</h2>{items}</section>{hub}
 <section><h2>{r["h_tips"]}</h2><ul class="checks">{tips}</ul></section>
 <section>{contact_box(l)}{cta_box(l, me)}</section>
 <section><h2>{u["blog_h"]}</h2>{posts(l, me, arts(l)[::-1][:6])}</section>
</main>
"""
    return head(l, "routes", None, r["title"], r["desc"], [art, business_ld(l, BASE + me), crumbs_ld(l, [(u["crumbs_routes"], me)])] + lds_extra, "airblade") + body + foot(l, frm=me)

def page_blog(l):
    b, u = C[l]["blog"], C[l]["ui"]
    me = blog_path(l)
    r = C[l]["routes"]
    extra = f'<a class="post" href="{rel(me, routes_path(l))}"><b>{r["h1"]}</b><span>{r["desc"]}</span></a>'
    if l == "vi":
        extra = f'<a class="post" href="{rel(me, home_path("vi") + "phuong-xuan-huong/")}"><b>Thuê xe máy Đà Lạt theo tuyến đường — phường Xuân Hương</b><span>Giao xe tận nơi theo từng con đường khu trung tâm: Bùi Thị Xuân, Phan Bội Châu, Trần Phú, Trương Công Định…</span></a>' + extra
    if l in DAY.LANGS:
        extra = f'<a class="post" href="{rel(me, lang_root(l) + DAY.SLUG[l] + "/")}"><b>{DAY.T[l]["h1"]}</b><span>{DAY.T[l]["desc"]}</span></a>' + extra
    if l in HUB.LANGS:
        _n = len(HUB.spots(l)); _t = HUB.T[l]
        extra = f'<a class="post" href="{rel(me, lang_root(l) + HUB.SLUG[l] + "/")}"><b>{_t["h1"].format(n=_n)}</b><span>{_t["desc"].format(n=_n)}</span></a>' + extra
    body = f"""
<header><div class="wrap">{langbar(l, "blog", None, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_blog"], None)])}
 <h1>{b["h1"]}</h1><p class="lead">{b["lead"]}</p>
</div></div></header>
<main class="wrap">
 <section>{posts(l, me, arts(l)[::-1]).replace("</div>", extra + "</div>", 1)}</section>
 <section>{contact_box(l)}{cta_box(l, me)}</section>
</main>
"""
    return head(l, "blog", None, b["title"], b["desc"], [crumbs_ld(l, [(u["crumbs_blog"], me)])]) + body + foot(l, frm=me)

def page_article(l, k):
    slug, title, h1, desc, lead, img, html = C[l]["articles"][k]
    img = PHOTO_HERO.get(k, img)
    for n, ph in sorted(PHOTO_INLINE.get(k, []), key=lambda x: -x[0] if x[0] >= 0 else 10**6):
        pos = [m.start() for m in re.finditer("<h2", html)]
        if pos: i = pos[n] if -len(pos) <= n < len(pos) else pos[-1]; html = html[:i] + "{PHOTO:" + ph + "}\n" + html[i:]
    u = C[l]["ui"]
    me = art_path(l, k)
    pre = "../" * me.count("/")
    html = html.replace("{ROUTES}", rel(me, routes_path(l))).replace("{HOME}", rel(me, home_path(l))).replace("{EV}", rel(me, ev_path(l))).replace("{IMG}", pre + "img/").replace("{PM}", rel(me, pm_path(l)))
    html = re.sub(r"\{ART:([a-z0-9-]+)\}", lambda m: rel(me, art_path(l, m.group(1))), html)
    _phs = re.findall(r"\{PHOTO:([a-z0-9-]+)\}", html)
    html = re.sub(r"\{PHOTO:([a-z0-9-]+)\}", lambda m: f'<p><img src="{pre}img/{m.group(1)}.jpg" alt="{_esc(PHOTO_ALT.get(l, {}).get(m.group(1)) or PHOTO_ALT["en"][m.group(1)])}" loading="lazy" style="{_ph_style(m.group(1))}"></p>', html)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "inLanguage": l,
           "mainEntityOfPage": BASE + me, "image": [f"{BASE}img/{x}.jpg" for x in dict.fromkeys([img] + _phs)], "datePublished": adate(k), "dateModified": mdate(l, k),
           "author": person_ld(),
           "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}}
    _sib = [x for x in arts(l)[::-1] if x != k and k in CL_GROUP and CL_GROUP.get(x) == CL_GROUP[k]]
    others = (_sib + [x for x in arts(l)[::-1] if x != k and x not in _sib])[:3]
    qa = AFAQ.get(l, {}).get(k, [])
    faq_html = (f'<section class="faq"><h2>{AFAQ_H[l]}</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa) + "</section>") if qa else ""
    lds = [art, crumbs_ld(l, [(u["crumbs_blog"], blog_path(l)), (h1, me)])]
    if qa:
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
    body = f"""
<header><div class="wrap">{langbar(l, "art", k, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_blog"], blog_path(l))])}
 <h1>{h1}</h1><p class="lead">{lead}</p><p class="upd"><time datetime="{mdate(l, k)}">{UPD[l]}: {fdate(l, mdate(l, k))}</time></p>
 <img class="heroimg" src="{pre}img/{img}.jpg" alt="{h1}" width="1200" height="675">
</div></div></header>
<main class="wrap">
 <section class="prose">{vbox(l, VIDEO_ART[k], h1) if k in VIDEO_ART else ""}{html}{lic_link(l, me) if k in LIC_FROM else ""}{arr_link(l, me) if k in ARR.FROM else ""}{author_box(l, me)}</section>
 {faq_html}
 <section>{contact_box(l)}{cta_box(l, me)}</section>
 <section><h2>{u["read_also"]}</h2>{posts(l, me, others)}</section>
</main>
"""
    return head(l, "art", k, title, desc, lds, img) + body + foot(l, frm=me)

# old URLs from the previous site on this domain -> new pages
OLD = {"thuexemaydalat/": ("vi", "home"), "motorbike-rental-in-dalat-for-foreigners-easy-safe-fast/": ("en", "home")}

def page_redirect_to(l, to):
    return f"""<!doctype html>
<html lang="{l}"><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<title>{C[l]["home"]["title"]}</title>
<link rel="canonical" href="{BASE + to}">
<meta http-equiv="refresh" content="0; url={BASE + to}">
</head><body><a href="{BASE + to}">{C[l]["home"]["title"]}</a></body></html>
"""

def page_redirect(l):
    """language root (/, /vi/, /ru/...) -> keyword rental page. Meta refresh 0 is read by
    Google/Yandex/Bing as a permanent redirect; '/' also picks the visitor's language."""
    to = home_path(l)
    js = ""
    if l == "en":
        js = ("<script>(function(){var p=null;try{p=localStorage.getItem('lang')}catch(e){}"
              "var m=" + json.dumps({x: home_path(x) for x in LANGS}) + ";var t=p;"
              "if(!t){var ls=navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'en'];"
              "for(var i=0;i<ls.length;i++){var n=ls[i].toLowerCase().slice(0,2);if(n==='in')n='id';if(n==='iw')n='he';if(m[n]){t=n;break}}}"
              "if(!m[t])t='en';location.replace('/'+m[t]);})();</script>")
    return f"""<!doctype html>
<html lang="{l}"><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<title>{C[l]["home"]["title"]}</title>
<link rel="canonical" href="{BASE + to}">
{js}<meta http-equiv="refresh" content="0; url={BASE + to}">
</head><body><a href="{BASE + to}">{C[l]["home"]["title"]}</a></body></html>
"""

def page_ev(l):
    e, u = EV[l], C[l]["ui"]
    me = ev_path(l)
    pre = rel(me, "")
    facts = "".join(f"<tr><td>{k}</td><td><b>{v}</b></td></tr>" for k, v in e["facts"])
    good = "".join(f"<li>{t}</li>" for t in e["good"])
    notes = "".join(f"<li>{t}</li>" for t in e["notes"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in e["faq"])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in e["faq"]]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": e["h1"], "serviceType": "Electric scooter rental",
           "provider": {"@id": BASE + "#business"}, "areaServed": "Da Lat, Vietnam", "url": BASE + me,
           "offers": {"@type": "Offer", "price": "150000", "priceCurrency": "VND"}}
    body = f"""
<header><div class="wrap">{langbar(l, "ev", None, me)}
<div class="hero">{crumbs(l, me, [(e["crumb"], None)])}
 <h1>{e["h1"]}</h1><p class="lead">{e["lead"]}</p>
 <div class="cta">{hero_btns(l)}</div>
</div></div></header>
<main class="wrap">
 <section><img src="{pre}img/electric-row.jpg" alt="{e["h1"]}" style="width:100%;border-radius:12px" loading="lazy"></section>
 <section>{vbox(l, EV_VIDEO, e["h1"])}</section>
 <section><h2>{e["h_facts"]}</h2><table class="price">{facts}</table>{lic_link(l, me)}</section>
 <section><h2>{e["h_good"]}</h2><ul class="checks">{good}</ul></section>
 <section><h2>{e["h_note"]}</h2><ul class="checks">{notes}</ul></section>
 <section><h2>{e["h_faq"]}</h2>{faq}</section>
 {rev_section(l, ("keziah", "peter", "jan"))}
 <section>{contact_box(l)}{cta_box(l, me)}</section>
 <section><h2>{u["blog_h"]}</h2>{posts(l, me, arts(l)[::-1][:3])}</section>
</main>
"""
    return head(l, "ev", None, e["title"], e["desc"], [svc, faq_ld, crumbs_ld(l, [(e["crumb"], me)])], "electric-row") + body + foot(l, frm=me)

# ------------------------------------------------------------------ write
# ---- speed: serve WebP copies of every JPG (full size for the hero, small for lazy images)
from PIL import Image as _Im
_WEBP = {}
def _webp(name, kind):
    """img/<name>.jpg -> img/w/<name>.webp (<=1200px) or img/t/<name>.webp (<=560px); returns (path, w, h) or None"""
    key = (name, kind)
    if key in _WEBP: return _WEBP[key]
    src = OUT / "img" / (name + ".jpg")
    if not src.exists(): _WEBP[key] = None; return None
    dst = OUT / "img" / kind / (name + ".webp")
    im = _Im.open(src); w0, h0 = im.size
    mx = 1200 if kind == "w" else 560
    w, h = (w0, h0) if w0 <= mx else (mx, round(h0 * mx / w0))
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        dst.parent.mkdir(parents=True, exist_ok=True)
        im.convert("RGB").resize((w, h), _Im.LANCZOS).save(dst, "WEBP", quality=70 if kind == "w" else 66, method=6)
    _WEBP[key] = (f"{kind}/{name}.webp", w, h); return _WEBP[key]
_IMG_RE = re.compile(r'<img ([^>]*?)src="([^"]*?)img/([a-z0-9/_-]+)\.jpg"([^>]*)>')
def speed(html):
    def sub(m):
        a, pre, name, b = m.groups(); attrs = a + b
        hero = "heroimg" in attrs
        r = _webp(name, "w" if hero else "t")
        if not r: return m.group(0)
        path, w, h = r
        extra = ""
        if "width=" not in attrs: extra += f' width="{w}" height="{h}"'
        if hero: extra += ' fetchpriority="high" decoding="async"'
        else:
            extra += ' decoding="async"'
            if "loading=" not in attrs: extra += ' loading="lazy"'
            full = _webp(name, "w")
            if full: extra += f' data-full="{pre}img/{full[0]}"'
        return f'<img {a}src="{pre}img/{path}"{b}{extra}>'
    return _IMG_RE.sub(sub, html)

GA_ID = "G-EY9EPL0MQ0"
GA = ('<script async src="https://www.googletagmanager.com/gtag/js?id=' + GA_ID + '"></script>'
      '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
      "gtag('js',new Date());gtag('config','" + GA_ID + "');"
      "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;"
      "var h=a.getAttribute('href')||'',m=/wa\\.me|whatsapp/i.test(h)?'whatsapp':/zalo\\.me/i.test(h)?'zalo':/t\\.me\\//i.test(h)?'telegram':"
      "/^tel:/i.test(h)?'phone':/weixin|wechat/i.test(h)?'wechat':/maps\\.app\\.goo\\.gl|google\\.[a-z.]+\\/maps/i.test(h)?'google_maps':'';"
      "if(m)gtag('event','contact_click',{method:m,link_url:h,page_path:location.pathname});},true);</script>")

def add_ga(html):
    if "googletagmanager.com/gtag/js" in html:
        return html
    i = html.find('<meta charset="utf-8">')
    if i < 0:
        return html
    i += len('<meta charset="utf-8">')
    return html[:i] + GA + html[i:]

# Content-Security-Policy (meta tag: GitHub Pages cannot send HTTP headers). Allows only what the pages use:
# own files, inline CSS/JS already in the pages, Google Tag Manager, YouTube/Maps embeds, Zalo/WhatsApp/Telegram links (links need no CSP).
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; "
       "style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; "
       "frame-src https://www.youtube-nocookie.com https://www.youtube.com https://maps.google.com https://www.google.com; "
       "connect-src 'self' https:; object-src 'none'; base-uri 'self'")
def add_csp(html):
    tag = f'<meta http-equiv="Content-Security-Policy" content="{CSP}">'
    if 'http-equiv="Content-Security-Policy"' in html:
        return html
    return html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + tag, 1) if '<meta charset="utf-8">' in html else html
# PWA: install-to-home-screen manifest, theme colour and offline service worker (sw.js and manifest.json live at the site root).
PWA_HEAD = '<link rel="manifest" href="/manifest.json"><meta name="theme-color" content="#0f5c3c">'
PWA_JS = "<script>if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){});});}</script>"
def add_pwa(html):
    if 'rel="manifest"' in html:
        return html
    if '<meta charset="utf-8">' in html:
        html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + PWA_HEAD, 1)
    return html.replace('</body>', PWA_JS + '</body>', 1) if '</body>' in html else html
# ---- structured data on every indexable page (owner asked 2026-10-28):
# the shop's LocalBusiness/AutoRental entity (hours 04:30–21:00, priceRange, geo) and a FAQPage built only from Q&A that is visible
# on the page (<details> blocks and genuine question <h2>s). Contact/CTA headings ("Questions about Da Lat?", "Ready to rent?")
# are excluded: their "answer" is a booking box, not an answer.
_LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
def _plain(x): return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
def _cta_heads():
    out = set()
    for _l in LANGS:
        for x in (contact_box(_l) + cta_box(_l, home_path(_l))).split("<h2")[1:]:
            out.add(_plain(x.split(">", 1)[1].split("</h2>")[0]))
    return out
_CTA_H = None
def _faq_from_page(html):
    global _CTA_H
    if _CTA_H is None: _CTA_H = _cta_heads()
    qa = [(_plain(q), _plain(a)) for q, a in re.findall(r"<details><summary>(.*?)</summary>(.*?)</details>", html, re.S)]
    main = html.split("<main", 1)[-1]
    parts = re.split(r"(<h2>[^<]{8,}[?？]</h2>)", main)
    for i in range(1, len(parts) - 1, 2):
        q = _plain(parts[i]); body = re.split(r"<h2|<section|</section>|<details", parts[i + 1])[0]
        a = _plain(body)
        if q in _CTA_H or "wa.me/" in body or "tel:" in body or len(a) < 40: continue
        qa.append((q, a[:1000]))
    seen, out = set(), []
    for q, a in qa:
        if q and a and q not in seen: seen.add(q); out.append((q, a))
    return out
def add_ld(path, html):
    if 'http-equiv="refresh"' in html or 'name="robots" content="noindex"' in html or "</head>" not in html: return html
    types = []
    for x in _LD_RE.findall(html):
        try: t = json.loads(x).get("@type")
        except Exception: continue
        types += t if isinstance(t, list) else [t]
    add = []
    if "AutoRental" not in types:
        m = re.search(r'<html lang="([a-z]+)"', html); _l = m.group(1) if m and m.group(1) in C else "en"
        add.append(business_ld(_l, BASE + path))
    if "VideoObject" not in types:
        for v, name in dict(re.findall(r'data-yt="([\w-]+)" aria-label="[^:"]*: ([^"]+)"', html)).items():
            add.append({"@context": "https://schema.org", "@type": "VideoObject", "name": _html.unescape(name),
                        "description": (_plain(m.group(1)) if (m := re.search(r'<meta name="description" content="([^"]*)"', html)) else _html.unescape(name)),
                        "thumbnailUrl": [f"https://i.ytimg.com/vi/{v}/hqdefault.jpg"], "uploadDate": VIDEO_DATE.get(v, "2026-10-10"),
                        "embedUrl": f"https://www.youtube.com/embed/{v}", "url": f"https://www.youtube.com/shorts/{v}",
                        "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}})
    if "FAQPage" not in types:
        qa = _faq_from_page(html)
        if qa:
            add.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
    return html.replace("</head>", "".join(ldjson(x) for x in add) + "</head>", 1) if add else html

# ---- Site menu (owner asked 2026-11-04): 5 items + "Book" button under the logo; the language bar stays as it is.
NAV = {  # (rental, electric, where to go, guides, about, book)
 "vi": ("Thuê xe", "Xe điện", "Đi đâu", "Cẩm nang", "Giới thiệu", "Đặt xe"),
 "en": ("Rental", "Electric", "Where to go", "Guides", "About", "Book"),
 "ru": ("Аренда", "Электро", "Куда поехать", "Статьи", "О нас", "Забронировать"),
 "zh": ("租车", "电动车", "去哪玩", "攻略", "关于我们", "预订"),
 "ko": ("렌탈", "전기 스쿠터", "어디 갈까", "가이드", "소개", "예약"),
 "ja": ("レンタル", "電動バイク", "行き先", "ガイド", "", "予約"),
 "th": ("เช่ารถ", "รถไฟฟ้า", "เที่ยวไหนดี", "คู่มือ", "", "จอง"),
 "id": ("Sewa", "Listrik", "Mau ke mana", "Panduan", "Tentang", "Pesan"),
 "ms": ("Sewa", "Elektrik", "Ke mana", "Panduan", "", "Tempah"),
 "de": ("Mieten", "E-Roller", "Wohin", "Ratgeber", "", "Buchen"),
 "fr": ("Location", "Électrique", "Où aller", "Guides", "", "Réserver"),
 "es": ("Alquiler", "Eléctrica", "Adónde ir", "Guías", "", "Reservar"),
 "he": ("השכרה", "חשמלי", "לאן לנסוע", "מדריכים", "", "להזמין"),
 "it": ("Noleggio", "Elettrico", "Dove andare", "Guide", "", "Prenota"),
 "nl": ("Huren", "Elektrisch", "Waarheen", "Gidsen", "", "Boeken"),
 "km": ("ជួលម៉ូតូ", "ម៉ូតូអគ្គិសនី", "ទៅណា", "មគ្គុទ្ទេសក៍", "", "កក់"),
 "lo": ("ເຊົ່າລົດ", "ລົດໄຟຟ້າ", "ໄປໃສດີ", "ຄູ່ມື", "", "ຈອງ"),
 "my": ("ငှားရန်", "လျှပ်စစ်", "ဘယ်သွားမလဲ", "လမ်းညွှန်", "", "ကြိုတင်မှာ"),
}
NAV_CSS = ('<style>.mnav{display:flex;gap:6px;overflow-x:auto;padding:0 0 12px;scrollbar-width:none;-webkit-overflow-scrolling:touch}'
           '.mnav::-webkit-scrollbar{display:none}.mnav a{flex:none;color:#fff;text-decoration:none;font-size:14px;font-weight:600;padding:7px 12px;border-radius:999px;background:rgba(255,255,255,.1);white-space:nowrap}'
           '.mnav a.on{background:#fff;color:var(--brand)}.mnav a.bk{background:var(--accent);color:#1d2a24;margin-inline-start:auto}'
           '@media(max-width:720px){.mnav{flex-wrap:wrap;overflow:visible}.mnav a{font-size:13px;padding:6px 11px}.mnav a.bk{display:none}}</style>')
def nav_html(l, path):
    n = NAV.get(l, NAV["en"])
    items = [(n[0], home_path(l)), (n[1], ev_path(l)), (n[2], routes_path(l)), (n[3], blog_path(l))]
    if l in AB.LANGS and n[4]: items.append((n[4], about_path(l)))
    cur = max((p for _, p in items if path.startswith(p) and (p != home_path(l) or path == p)), key=len, default=None)
    out = "".join(f'<a href="/{p}"{" class=" + chr(34) + "on" + chr(34) + " aria-current=" + chr(34) + "page" + chr(34) if p == cur else ""}>{x}</a>' for x, p in items)
    bk = ZALO if l == "vi" else wa_link(l)
    return f'<nav class="mnav" aria-label="Menu">{out}<a class="bk" href="{bk}" target="_blank" rel="noopener">💬 {n[5]}</a></nav>'
def add_nav(path, html):
    i = html.find('<div class="top">')
    if i < 0 or 'class="mnav"' in html or 'http-equiv="refresh"' in html: return html
    m = re.search(r'<html lang="([a-z]+)"', html); l = m.group(1) if m and m.group(1) in C else "en"
    depth, j = 0, i
    for t_ in re.finditer(r"<div\b|</div>", html[i:]):
        depth += 1 if t_.group(0) == "<div" else -1
        if depth == 0: j = i + t_.end(); break
    html = html[:j] + nav_html(l, path) + html[j:]
    return html.replace("</head>", NAV_CSS + "</head>", 1)

def write(path, html):
    html = add_nav(path, html)
    html = add_pwa(add_csp(add_ga(speed(add_ld(path, html)))))
    p = OUT / path / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")

# images live in <repo>/img and are referenced directly; nothing is deleted here

for old, (l_, k_) in OLD.items():
    write(old, page_redirect_to(l_, path_of(l_, k_)))

groups = [("home", None), ("ev", None), ("routes", None), ("blog", None)] + [("art", k) for k in ARTICLES]
for l in LANGS:
    write(home_path(l), page_home(l))
    write(lang_root(l), page_redirect(l))
    write(routes_path(l), page_routes(l))
    write(blog_path(l), page_blog(l))
    write(ev_path(l), page_ev(l))
    for k in arts(l):
        write(art_path(l, k), page_article(l, k))

# ------------------------------------------------------------------ Vietnamese-only street pages (phường Xuân Hương)
from content import streets_vi as ST
def st_hub_path(): return home_path("vi") + ST.HUB_SLUG + "/"
def st_path(s): return home_path("vi") + s[0] + "/"
def st_head(me, title, desc, lds, img):
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE + me}">
<meta property="og:type" content="article"><meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/{img}.jpg">
{"".join(ldjson(x) for x in lds)}
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>"""
def st_top(me):
    return f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs"><a href="{rel(me, home_path("vi"))}" class="on" data-l="vi">VI</a></div></div>'
def st_deliv(s):
    if s[3]:
        return (f"Văn Phú giao xe miễn phí tới khách sạn, homestay ở khu trung tâm Đà Lạt khi thuê từ 2 ngày. Đoạn đường {s[1]} nơi bạn ở có thể nằm ngoài vùng trung tâm — "
                f"gọi 0944 081 101 hoặc 0834 622 149, hay nhắn Zalo kèm định vị để được báo ngay có giao được không. Thuê 1 ngày thì ghé tiệm 1/15/5 Thông Thiên Học (mở cửa từ 4:30 sáng).")
    return (f"Có. Thuê từ 2 ngày, Văn Phú giao xe miễn phí tận khách sạn, homestay trên đường {s[1]} (khu trung tâm Đà Lạt). "
            f"Thuê 1 ngày thì ghé tiệm 1/15/5 Thông Thiên Học, rất gần — tiệm mở cửa từ 4:30 sáng.")
def page_street(i, s):
    slug, name, area, outer, intro, tip, img = s
    me = st_path(s)
    pre = "../" * me.count("/")
    alabel, ideas = ST.AREAS[area]
    ideas_html = "".join("<li>" + re.sub(r"\{ART:([a-z0-9-]+)\}", lambda m: rel(me, art_path("vi", m.group(1))), x) + "</li>" for x in ideas)
    h1 = f"Thuê xe máy Đà Lạt đường {name} — giao xe tận nơi"
    title = f"Thuê xe máy Đà Lạt đường {name} | Giao xe tận nơi – Văn Phú"
    desc = (f"Thuê xe máy ở đường {name}, Đà Lạt: Honda Vision, Air Blade 125cc, xe điện 150.000 VND/ngày. "
            f"Không cọc tiền, kèm mũ bảo hiểm, giao xe tận khách sạn khi thuê từ 2 ngày. Gọi 0944 081 101.")
    deliv = st_deliv(s)
    qa = [(q.format(name=name), a.format(name=name, deliv=deliv)) for q, a in ST.FAQ]
    same = [x for x in ST.S if x[2] == area and x[0] != slug]
    k = [x[0] for x in ST.S].index(slug)
    near = (same[k % max(len(same), 1):] + same[:k % max(len(same), 1)])[:4]
    near_html = " · ".join(f'<a href="{rel(me, st_path(x))}">Thuê xe máy đường {x[1]}</a>' for x in near)
    ev = rel(me, ev_path("vi"))
    hub = rel(me, st_hub_path())
    body = f"""
<header><div class="wrap">{st_top(me)}
<div class="hero">{crumbs("vi", me, [("Phường Xuân Hương", st_hub_path()), (f"Đường {name}", None)])}
 <h1>{h1}</h1><p class="lead">{intro}</p><p class="upd"><time datetime="{ST.UPDATED}">{UPD["vi"]}: {fdate("vi", ST.UPDATED)}</time></p>
 <div class="cta">{hero_btns("vi")}</div>
</div></div></header>
<main class="wrap">
<section class="prose">
<p><img src="{pre}img/{img}.jpg" alt="Thuê xe máy Đà Lạt đường {name} — Văn Phú" loading="lazy" style="{_ph_style(img)}"></p>
<h2>Giá thuê xe máy ở đường {name}</h2>
<table class="price"><tr><th>Xe</th><th>Giá</th></tr>
<tr><td>Honda Vision 110cc</td><td><b>150.000 VND/ngày</b></td></tr>
<tr><td>Honda Air Blade 125cc</td><td><b>150.000 VND/ngày</b></td></tr>
<tr><td><a href="{ev}">Xe máy điện</a></td><td><b>150.000 VND/ngày</b></td></tr>
<tr><td><a href="{rel(me, home_path("vi") + "thue-xe-so-da-lat/")}">Xe số (Sirius FI, Wave RSX)</a></td><td><b>120.000 VND/ngày</b></td></tr></table>
<p>Giá cố định cho mọi xe, không phụ phí. Một ngày thuê tính từ lúc nhận xe đến 21:00 cùng ngày.</p>
<h2>Giao xe đến đường {name}</h2>
<p>{deliv}</p>
<h2>Thủ tục thuê xe nhanh gọn</h2>
<ul>
<li>Để lại CCCD hoặc hộ chiếu — không cọc tiền mặt; tiền thuê trả trước.</li>
<li>Chạy thử và cùng quay video tình trạng xe trước khi đi.</li>
<li>Mỗi xe kèm mũ bảo hiểm và giá đỡ điện thoại; xe xăng giao kèm 1 lít xăng.</li>
<li>Không uống rượu bia khi lái xe và chấp hành nghiêm luật giao thông Việt Nam.</li>
</ul>
<h2>Từ đường {name} đi đâu? ({alabel})</h2>
<ul>{ideas_html}</ul>
<p><b>Mẹo:</b> {tip}</p>
<h2>Xe xăng hay xe điện?</h2>
<p>Xe máy điện êm, dễ chạy, hợp dạo phố: mỗi xe có 2 pin, một pin đi được khoảng 25–30 km, tổng cộng khoảng 50–60 km; đổi pin tại tiệm 20.000 VND/lần. Xe điện chở tối đa 2 người với tổng cân nặng dưới 140 kg và không nên đi các đèo dài dốc như Prenn, Mimosa, Langbiang — những cung đó nên chọn Honda Air Blade 125cc. <a href="{ev}">Xem chi tiết xe máy điện</a>.</p>
<p>Các đường khác gần đây: {near_html} · <a href="{hub}">Tất cả tuyến đường phường Xuân Hương</a></p>
</section>
<section class="faq"><h2>Câu hỏi thường gặp</h2>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa)}</section>
<section>{contact_box("vi")}{cta_box("vi", me)}</section>
</main>
"""
    biz = business_ld("vi", BASE + home_path("vi"))
    svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Thuê xe máy Đà Lạt đường {name}", "serviceType": "Cho thuê xe máy",
           "provider": {"@id": BASE + "#business"}, "areaServed": {"@type": "Place", "name": f"Đường {name}, phường Xuân Hương – Đà Lạt, Lâm Đồng"},
           "offers": {"@type": "Offer", "price": "150000", "priceCurrency": "VND"}, "url": BASE + me}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}
    lds = [biz, svc, faq_ld, crumbs_ld("vi", [("Phường Xuân Hương", st_hub_path()), (f"Đường {name}", me)])]
    return st_head(me, title, desc, lds, img) + body + foot("vi", frm=me)
def page_street_hub():
    me = st_hub_path()
    groups = ""
    for a, (label, _) in ST.AREAS.items():
        items = "".join(f'<a class="post" href="{rel(me, st_path(s))}"><b>Thuê xe máy đường {s[1]}</b><span>{s[4][:110].rsplit(" ", 1)[0]}…</span></a>' for s in ST.S if s[2] == a)
        groups += f'<section><h2>{label}</h2><div class="posts">{items}</div></section>'
    title = "Thuê xe máy Đà Lạt phường Xuân Hương — giao xe tận nơi | Văn Phú"
    desc = "Thuê xe máy giao tận nơi theo từng tuyến đường phường Xuân Hương – Đà Lạt: Vision, Air Blade, xe điện 150.000 VND/ngày, không cọc tiền."
    body = f"""
<header><div class="wrap">{st_top(me)}
<div class="hero">{crumbs("vi", me, [("Phường Xuân Hương", None)])}
 <h1>Thuê xe máy Đà Lạt theo tuyến đường — phường Xuân Hương</h1>
 <p class="lead">Phường Xuân Hương – Đà Lạt gồm khu trung tâm cũ (phường 1, 2, 3, 4, 10 trước đây). Chọn con đường nơi bạn ở để xem cách nhận xe, giao xe và gợi ý lộ trình. Thuê từ 2 ngày được giao xe miễn phí tận khách sạn khu trung tâm.</p>
 <div class="cta">{hero_btns("vi")}</div>
</div></div></header>
<main class="wrap">{groups}
<section>{contact_box("vi")}{cta_box("vi", me)}</section>
</main>
"""
    lds = [business_ld("vi", BASE + home_path("vi")), crumbs_ld("vi", [("Phường Xuân Hương", me)])]
    return st_head(me, title, desc, lds, "honda-vision-hotel-delivery-dalat") + body + foot("vi", frm=me)
write(st_hub_path(), page_street_hub())
for _i, _s in enumerate(ST.S):
    write(st_path(_s), page_street(_i, _s))


# ------------------------------------------------------------------ Vietnamese-only manual-bike (xe số) rental page
XS_PATH = home_path("vi") + "thue-xe-so-da-lat/"
def page_xeso():
    me = XS_PATH
    title = "Thuê xe số Đà Lạt: Sirius FI, Wave RSX – giao xe tận nơi | Văn Phú"
    desc = "Thuê xe số Sirius FI và Wave RSX ở Đà Lạt tại Văn Phú: không cọc tiền, kèm mũ bảo hiểm, mở cửa 4:30 sáng, giao xe miễn phí tới khách sạn khi thuê từ 2 ngày. Chạy thử và quay video tình trạng xe."
    faq = [
        ("Thuê xe số Sirius FI hay Wave RSX ở Đà Lạt?", "Sirius FI dễ đi trong phố và đường đèo nhẹ; Wave RSX gọn, nhẹ và hợp người mới chạy xe số. Bạn có thể xem cả hai xe tại tiệm 1/15/5 Thông Thiên Học và chọn xe trước khi nhận."),
        ("Thuê xe số ở Văn Phú có cần đặt cọc tiền không?", "Không. Văn Phú không giữ tiền cọc, chỉ giữ CCCD hoặc hộ chiếu trong thời gian thuê và trả lại khi bạn trả xe."),
        ("Có mũ bảo hiểm khi thuê xe số không?", "Có. Mỗi xe số đều kèm mũ bảo hiểm và giá đỡ điện thoại; xe được giao sẵn 1 lít xăng."),
        ("Văn Phú có giao xe số tận khách sạn không?", "Có. Khi thuê từ 2 ngày, Văn Phú giao xe miễn phí tới khách sạn, homestay trong khu trung tâm Đà Lạt."),
    ]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    faq_html = "".join(f"<details><summary><b>{q}</b></summary><p>{a}</p></details>" for q, a in faq)
    body = f"""
<header><div class="wrap">{st_top(me)}
<div class="hero">{crumbs("vi", me, [("Thuê xe số Đà Lạt", None)])}
 <h1>Thuê xe số Đà Lạt: Sirius FI và Wave RSX</h1>
 <p class="lead">Văn Phú cho thuê xe số Yamaha Sirius FI và Honda Wave RSX tại Đà Lạt. Không cọc tiền, kèm mũ bảo hiểm, mở cửa từ 4:30 sáng mỗi ngày.</p>
 <div class="ticket">120.000 VND / ngày</div>
 <div class="cta">{hero_btns("vi")}</div>
</div></div></header>
<main class="wrap">
<section>
 <h2>Xe số Sirius FI và Wave RSX</h2>
 <p>Hai dòng xe số phổ biến nhất khi đi lại ở Đà Lạt. Xe được bảo dưỡng thường xuyên và giao sẵn 1 lít xăng. Nếu chưa biết chọn xe nào, nhắn tin hoặc ghé tiệm để xem trực tiếp.</p>
 <div class="posts">
  <a class="post" href="#sirius"><b>Thuê xe Sirius FI Đà Lạt</b><span>Yamaha Sirius FI, xe số phổ biến, đi trong phố và đường đèo nhẹ.</span></a>
  <a class="post" href="#wave"><b>Thuê xe Wave RSX Đà Lạt</b><span>Honda Wave RSX, gọn và nhẹ, hợp người mới chạy xe số.</span></a>
 </div>
 <div class="posts">
  <figure style="margin:0"><img src="{rel(me, "/img/xeso-fleet.jpg")}" alt="Xe số Sirius FI và Wave RSX cho thuê tại Văn Phú Đà Lạt" loading="lazy" style="width:100%;border-radius:12px"></figure>
  <figure style="margin:0"><img src="{rel(me, "/img/xeso-pair.jpg")}" alt="Honda Wave RSX cho thuê ở Đà Lạt" loading="lazy" style="width:100%;border-radius:12px"></figure>
 </div>
</section>
<section id="sirius">
 <h2>Thuê xe Sirius FI Đà Lạt</h2>
 <p>Yamaha Sirius FI là xe số phun xăng điện tử, khởi động dễ, chạy êm trong phố. Xe phù hợp cho khách đi lại hằng ngày, đi cà phê, đi chợ đêm hoặc chạy đường đèo nhẹ quanh Đà Lạt.</p>
</section>
<section id="wave">
 <h2>Thuê xe Wave RSX Đà Lạt</h2>
 <p>Honda Wave RSX là xe số nhẹ, dễ điều khiển, phụ tùng phổ biến. Xe hợp người mới chạy xe số và khách đi quãng ngắn trong thành phố.</p>
</section>
<section>
 <h2>Điều kiện thuê xe số</h2>
 <ul>
  <li><b>Giá 120.000 VND/ngày</b> cho mỗi xe số, thanh toán khi nhận xe.</li>
  <li><b>Không cọc tiền:</b> chỉ giữ CCCD hoặc hộ chiếu trong thời gian thuê.</li>
  <li><b>Kèm mũ bảo hiểm</b> và giá đỡ điện thoại; xe được giao sẵn 1 lít xăng.</li>
  <li><b>Giao xe miễn phí</b> tới khách sạn, homestay khu trung tâm Đà Lạt khi thuê từ 2 ngày.</li>
  <li><b>Chạy thử và quay video</b> tình trạng xe trước khi nhận, để bảo vệ cả hai bên.</li>
 </ul>
</section>
<section>
 <h2>Câu hỏi thường gặp</h2>
 {faq_html}
</section>
<section>{contact_box("vi")}{cta_box("vi", me)}</section>
</main>
"""
    lds = [business_ld("vi", BASE + me), crumbs_ld("vi", [("Thuê xe số Đà Lạt", me)]), faq_ld]
    return st_head(me, title, desc, lds, "xeso-fleet") + body + foot("vi", frm=me)
write(XS_PATH, page_xeso())

def villa_path(l): return VL.SLUG[l]
def page_about(l):
    t, me = AB.T[l], about_path(l)
    pre = "../" * me.count("/")
    u = C[l]["ui"]
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + about_path(x)}">\n' for x in AB.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + about_path("en")}">\n'
    pl = dict(person_ld()); pl["description"] = t["desc"]
    lds = [{"@context": "https://schema.org", "@type": "AboutPage", "url": BASE + me, "inLanguage": l, "name": t["title"], "mainEntity": pl},
           crumbs_ld(l, [(t["crumb"], me)])]
    head_html = head(l, "home", None, t["title"], t["desc"], lds, AB.IMG)
    head_html = re.sub(r'<link rel="canonical" href="[^"]*">\n(?:<link rel="alternate"[^\n]*\n)*', f'<link rel="canonical" href="{BASE + me}">\n' + alts, head_html, count=1)
    head_html = head_html.replace(f'<meta property="og:url" content="{BASE + home_path(l)}">', f'<meta property="og:url" content="{BASE + me}">')
    lb = "".join(f'<a href="{rel(me, about_path(x))}" hreflang="{x}" data-l="{x}"{" class=" + chr(34) + "on" + chr(34) + " aria-current=" + chr(34) + "page" + chr(34) if x == l else ""}>{LABEL[x]}</a>' for x in AB.LANGS)
    tgt = {"home": home_path(l), "routes": routes_path(l)}
    def _sl(n, k):
        if k == "tiktok": return f'<a href="{rel(me, villa_path(l))}">{n}</a>'
        return f'<a href="{rel(me, tgt[k])}">{n}</a>' if k else n
    svc = "".join(f'<li><b>{_sl(n, k)}</b> – {d}</li>' for n, d, k in t["services"])
    intro = "".join(f"<p>{x}</p>" for x in t["intro"])
    body = f"""
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{lb}</div></div>
<div class="hero">{crumbs(l, me, [(t["crumb"], None)])}
 <div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap">
  <img src="{pre}img/{AB.IMG}.jpg" alt="{t["alt"]}" width="160" height="160" style="width:160px;height:160px;border-radius:50%;object-fit:cover">
  <div><h1>{t["h1"]}</h1><p class="lead">{t["sub"]}</p></div>
 </div>
</div></div></header>
<main class="wrap">
 <section class="prose">{intro}
  <h2>{t["h_services"]}</h2><ul>{svc}</ul>
  <h2>{t["h_tt"]}</h2><p>{t["tt"]}</p><p><a class="btn alt" href="{rel(me, villa_path(l))}" style="border:1px solid var(--line)">🎵 {VL.T[l]["link_about"]} →</a></p>
  <h2>{t["h_more"]}</h2><p>{t["more"]}</p>
  <p><a class="btn alt" href="{rel(me, routes_path(l))}" style="border:1px solid var(--line)">{C[l]["routes"]["h1"]} →</a> <a class="btn alt" href="{rel(me, pm_path(l))}" style="border:1px solid var(--line)">📍 {PM.T[l]["h1"]} →</a></p>
 </section>
 <section><h2>{t["h_contact"]}</h2>{contacts(l)}</section>
 {rev_section(l)}
 <section>{contact_box(l)}</section>
</main>
"""
    return head_html + body + foot(l, frm=me)
for _l in AB.LANGS:
    write(about_path(_l), page_about(_l))

# ------------------------------------------------------------------ Villa Đà Lạt page (owner asked 2026-11-04): whole TikTok channel embedded
CSP_TT = CSP.replace("script-src 'self' 'unsafe-inline' https://www.googletagmanager.com",
                     "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.tiktok.com https://*.tiktok.com https://*.ttwstatic.com https://*.tiktokcdn.com https://*.tiktokcdn-us.com https://*.byteoversea.com https://*.ibytedtos.com"
               ).replace("frame-src ", "frame-src https://www.tiktok.com https://*.tiktok.com ")
def page_villa(l):
    t, me = VL.T[l], villa_path(l)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + villa_path(x)}">\n' for x in VL.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + villa_path("en")}">\n'
    lds = [{"@context": "https://schema.org", "@type": "CollectionPage", "url": BASE + me, "inLanguage": l, "name": t["title"], "description": t["desc"],
            "about": {"@type": "Service", "name": t["crumb"], "provider": {"@id": BASE + "#business"}, "areaServed": "Da Lat"}, "sameAs": [TIKTOK]},
           crumbs_ld(l, [(t["crumb"], me)])]
    head_html = head(l, "home", None, t["title"], t["desc"], lds)
    head_html = re.sub(r'<link rel="canonical" href="[^"]*">\n(?:<link rel="alternate"[^\n]*\n)*', f'<link rel="canonical" href="{BASE + me}">\n' + alts, head_html, count=1)
    head_html = head_html.replace(f'<meta property="og:url" content="{BASE + home_path(l)}">', f'<meta property="og:url" content="{BASE + me}">')
    head_html = head_html.replace('<meta charset="utf-8">', f'<meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="{CSP_TT}">', 1)
    lb = "".join(f'<a href="{rel(me, villa_path(x))}" hreflang="{x}" data-l="{x}"{" class=" + chr(34) + "on" + chr(34) + " aria-current=" + chr(34) + "page" + chr(34) if x == l else ""}>{LABEL[x]}</a>' for x in VL.LANGS)
    from urllib.parse import quote
    if l == "vi":
        b = f'<a class="btn zalo" href="{ZALO}" target="_blank" rel="noopener">{t["btn"]}</a>'
    elif l == "ru":
        b = f'<a class="btn tg" href="{TG}" target="_blank" rel="noopener">{t["btn"]}</a>'
    elif l == "zh":
        b = ('<img src="/img/wechat-qr.png" alt="微信二维码 vanphudalat" width="280" height="375" '
             'style="display:block;max-width:280px;width:100%;height:auto;border-radius:12px;margin:0 0 12px;background:#fff">' + btn("wc", l))
    else:
        b = f'<a class="btn wa" href="https://wa.me/84944081101?text={quote(t["msg"])}" target="_blank" rel="noopener">{t["btn"]}</a>'
    how = "".join(f"<li>{x}</li>" for x in t["how"])
    vids = [(u, re.search(r"/video/(\d+)", u).group(1)) for u in VL.VIDEOS if re.search(r"/video/(\d+)", u)]
    if vids:
        clips = ('<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;align-items:start">'
                 + "".join(f'<blockquote class="tiktok-embed" cite="{u}" data-video-id="{i}" style="max-width:605px;min-width:288px;margin:0"><section><a target="_blank" rel="noopener" href="{u}">TikTok @bietthudalat</a></section></blockquote>' for u, i in vids)
                 + '</div>')
        tt_js = '<script async src="https://www.tiktok.com/embed.js"></script>'
    else:
        clips = (f'<a href="{TIKTOK}" target="_blank" rel="noopener" style="display:flex;gap:14px;align-items:center;padding:18px;border:1px solid var(--line);border-radius:16px;background:#fff;text-decoration:none;color:inherit;max-width:520px;margin:0 auto">'
                 f'<span style="font-size:40px;line-height:1">🎵</span><span><b style="font-size:1.1em">@bietthudalat</b><br>{t["lead"].split(". ")[0].replace("<b>","").replace("</b>","")}.</span></a>')
        tt_js = ""
    body = f"""
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{lb}</div></div>
<div class="hero">{crumbs(l, me, [(t["crumb"], None)])}
 <h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
</div></div></header>
<main class="wrap">
 <section class="prose"><h2>{t["h_how"]}</h2><ol>{how}</ol></section>
 <section><h2>{t["h_clips"]}</h2>
  {clips}
  <p style="text-align:center"><a class="btn alt" href="{TIKTOK}" target="_blank" rel="noopener" style="border:1px solid var(--line)">🎵 {t["fallback"]}</a></p>
 </section>
 <section><div class="box"><h2>{t["h_book"]}</h2><p>{t["book_txt"]}</p>{b}</div></section>
 <section><h2>{AB.T[l]["h_contact"]}</h2>{contacts(l)}</section>
</main>
{tt_js}
"""
    return head_html + body + foot(l, frm=me)
for _l in VL.LANGS:
    write(villa_path(_l), page_villa(_l))

# ------------------------------------------------------------------ Indonesian-only halal restaurant map
def page_halal():
    me = halal_path()
    def top():
        return f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs"><a href="{rel(me, home_path("id"))}" class="on" data-l="id">ID</a></div></div>'
    cards = "".join(
        f'<div class="card"><b>{i}. {n}</b>'
        f'<p>⭐ {r} dari {c} ulasan Google · 🕒 {h}</p>'
        f'<p>{d}</p><p><i>{t}</i></p>'
        f'<p><a href="{gmap(pid, la, ln)}" target="_blank" rel="noopener">📍 Buka di Google Maps</a></p></div>'
        for i, (n, r, c, la, ln, pid, h, d, t) in enumerate(HI.SPOTS, 1))
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HI.FAQ]}
    faq_html = "".join(f"<details><summary><b>{q}</b></summary><p>{a}</p></details>" for q, a in HI.FAQ)
    tips = "".join(f"<li>{t}</li>" for t in HI.TIPS)
    body = f"""
<header><div class="wrap">{top()}
<div class="hero">{crumbs("id", me, [(HI.H1, None)])}
 <h1>{HI.H1}</h1>
 <p class="lead">{HI.LEAD}</p>
 <div class="cta">{hero_btns("id")}</div>
</div></div></header>
<main class="wrap">
<section>
 <h2>Peta restoran halal di Đà Lạt</h2>
 <iframe src="https://maps.google.com/maps?q=restoran+halal+Dalat&amp;hl=id&amp;z=14&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Peta restoran halal di Đà Lạt" style="width:100%;height:360px;border:0;border-radius:12px"></iframe>
 <p class="kw">Peta ini hasil pencarian Google Maps. Lima tempat di bawah adalah pilihan kami dari hasil itu.</p>
</section>
<section>
 <h2>5 restoran halal di Đà Lạt</h2>
 <div class="grid">{cards}</div>
</section>
<section>
 <h2>Tips untuk Muslim traveler</h2>
 <h3>{HI.PRAYER_H3}</h3>
 <ul>{"".join(f"<li>{x}</li>" for x in HI.PRAYER)}</ul>
 <h3>{HI.FOOD_H3}</h3>
 <ul>{"".join(f"<li>{x}</li>" for x in HI.FOOD_TIPS)}</ul>
</section>
<section>
 <h2>Keliling Đà Lạt dengan motor</h2>
 <p>Mau rute sehari lengkap? Lihat <a href="{rel(me, tour_path())}">tur motor Dalat untuk wisatawan Muslim</a>.</p>
 <p>{HI.CTA_TEXT} Cek <a href="{rel(me, home_path("id"))}">sewa motor di Dalat: harga dan syarat di Văn Phú</a>.</p>
</section>
<section>
 <h2>Sebelum berkunjung</h2>
 <ul>{tips}</ul>
</section>
<section>
 <h2>Pertanyaan umum</h2>
 {faq_html}
</section>
<section>{contact_box("id")}{cta_box("id", me)}</section>
</main>
"""
    lds = [business_ld("id", BASE + me), crumbs_ld("id", [(HI.H1, me)]), faq_ld]
    html = st_head(me, HI.TITLE, HI.DESC, lds, "electric-row").replace('<html lang="vi">', '<html lang="id">').replace('content="vi_VN"', 'content="id_ID"')
    return html + body + foot("id", frm=me)
write(halal_path(), page_halal())

# ------------------------------------------------------------------ Indonesian-only motorbike tour for Muslim travellers
def page_tour():
    me = tour_path()
    top = f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs"><a href="{rel(me, home_path("id"))}" class="on" data-l="id">ID</a></div></div>'
    route = "".join(f"<li><b>{t}</b><br>{d}</li>" for t, d in HI.TOUR_ROUTE)
    tips = "".join(f"<li>{t}</li>" for t in HI.TOUR_TIPS)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HI.TOUR_FAQ]}
    faq_html = "".join(f"<details><summary><b>{q}</b></summary><p>{a}</p></details>" for q, a in HI.TOUR_FAQ)
    body = f"""
<header><div class="wrap">{top}
<div class="hero">{crumbs("id", me, [(HI.TOUR_H1, None)])}
 <h1>{HI.TOUR_H1}</h1>
 <p class="lead">{HI.TOUR_LEAD}</p>
 <div class="cta">{hero_btns("id")}</div>
</div></div></header>
<main class="wrap">
<section>
 <h2>Rute sehari di Dalat</h2>
 <ol>{route}</ol>
</section>
<section>
 <h2>Makan dan sholat di sepanjang jalan</h2>
 <p>Semua restoran dan tempat sholat yang disebut di sini ada di <a href="{rel(me, halal_path())}">daftar restoran halal Dalat</a>, lengkap dengan jam buka dan arah ke setiap tempat.</p>
</section>
<section>
 <h2>Tips berkendara</h2>
 <ul>{tips}</ul>
</section>
<section>
 <h2>Pertanyaan umum</h2>
 {faq_html}
</section>
<section>
 <h2>Sewa motor untuk tur Anda</h2>
 <p>Ambil motor di <a href="{rel(me, home_path("id"))}">tiệm Văn Phú</a> dan mulai tur dari sana. Harga, syarat, dan pilihan motor ada di halaman sewa motor Dalat.</p>
</section>
<section>{contact_box("id")}{cta_box("id", me)}</section>
</main>
"""
    lds = [business_ld("id", BASE + me), crumbs_ld("id", [(HI.TOUR_H1, me)]), faq_ld]
    html = st_head(me, HI.TOUR_TITLE, HI.TOUR_DESC, lds, "electric-row").replace('<html lang="vi">', '<html lang="id">').replace('content="vi_VN"', 'content="id_ID"')
    return html + body + foot("id", frm=me)
write(tour_path(), page_tour())

# ------------------------------------------------------------------ Guide articles (vi + en), checked against owner-confirmed rules
from content import guides as GD
def guide_path(l, g): return home_path(l) + g["slug"]
def page_guide(l, i):
    g = GD.GUIDES[l][i]
    me = guide_path(l, g)
    langlink = f'<div class="langs"><a href="{rel(me, home_path(l))}" class="on" data-l="{l}">{l.upper()}</a></div>'
    top = f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div>{langlink}</div>'
    others = [o for j, o in enumerate(GD.GUIDES[l]) if j != i]
    related = "".join(f'<li><a href="{rel(me, guide_path(l, o))}">{o["h1"]}</a></li>' for o in others) + (f'<li><a href="{rel(me, lic_path(l))}">{LIC.T[l]["h1"]}</a></li>' if l in LIC.T else "")
    secs = "".join(f"<section><h2>{h}</h2>{body}</section>" for h, body in g["sections"])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    faq_html = "".join(f"<details><summary><b>{q}</b></summary><p>{a}</p></details>" for q, a in g["faq"])
    rel_label = {"vi": "Đọc thêm", "en": "Read more"}[l]
    body = f"""
<header><div class="wrap">{top}
<div class="hero">{crumbs(l, me, [(g["h1"], None)])}
 <h1>{g["h1"]}</h1>
 <p class="lead">{g["lead"]}</p>
 <div class="cta">{hero_btns(l)}</div>
</div></div></header>
<main class="wrap">
{secs}
<section><h2>{"Câu hỏi thường gặp" if l == "vi" else "Frequently asked questions"}</h2>{faq_html}</section>
<section><h2>{rel_label}</h2><ul>{related}</ul></section>
<section>{contact_box(l)}{cta_box(l, me)}</section>
</main>
"""
    lds = [business_ld(l, BASE + me), crumbs_ld(l, [(g["h1"], me)]), faq_ld]
    html = st_head(me, g["title"], g["desc"], lds, "electric-row").replace('<html lang="vi">', f'<html lang="{l}">').replace('content="vi_VN"', f'content="{ {"vi":"vi_VN","en":"en_US"}[l] }"')
    return html + body + foot(l, frm=me)
for _l in GD.GUIDES:
    for _i in range(len(GD.GUIDES[_l])):
        write(guide_path(_l, GD.GUIDES[_l][_i]), page_guide(_l, _i))
write(HALAL_OLD, f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<link rel="canonical" href="{BASE + halal_path()}">
<meta http-equiv="refresh" content="0; url={BASE + halal_path()}">
<title>{HI.TITLE}</title>
<script>location.replace("/{halal_path()}"+location.search+location.hash)</script>
</head><body><a href="/{halal_path()}">{HI.H1}</a></body></html>""")

# ------------------------------------------------------------------ Vietnamese-only Honda Vision rental page
VS_PATH = home_path("vi") + "thue-xe-honda-vision-da-lat/"
def page_vision():
    me = VS_PATH
    title = "Thuê xe Honda Vision Đà Lạt – xe tay ga nhẹ, giao xe tận nơi | Văn Phú"
    desc = "Thuê xe Honda Vision ở Đà Lạt tại Văn Phú: xe tay ga nhẹ, dễ dắt, không cọc tiền, kèm mũ bảo hiểm, mở cửa 4:30 sáng, giao xe miễn phí tới khách sạn khi thuê từ 2 ngày."
    faq = [
        ("Honda Vision có dễ đi cho người mới không?", "Có. Vision là xe tay ga, không cần sang số hay côn, nhẹ và dễ dắt. Xe hợp cho người mới chạy xe máy và khách đi trong phố Đà Lạt."),
        ("Nên thuê Honda Vision hay Honda Air Blade ở Đà Lạt?", "Vision hợp đi trong phố và quãng ngắn quanh trung tâm, nhẹ và dễ dắt. Air Blade 125cc khỏe hơn, hợp đèo dốc và ngoại ô, hoặc chở 2 người leo dốc."),
        ("Thuê Honda Vision ở Văn Phú có cần đặt cọc không?", "Không. Văn Phú không giữ tiền cọc, chỉ giữ CCCD hoặc hộ chiếu trong thời gian thuê và trả lại khi bạn trả xe."),
        ("Có mũ bảo hiểm khi thuê Honda Vision không?", "Có. Mỗi xe đều kèm mũ bảo hiểm và giá đỡ điện thoại; xe xăng được giao sẵn 1 lít xăng."),
    ]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    faq_html = "".join(f"<details><summary><b>{q}</b></summary><p>{a}</p></details>" for q, a in faq)
    body = f"""
<header><div class="wrap">{st_top(me)}
<div class="hero">{crumbs("vi", me, [("Thuê xe Honda Vision Đà Lạt", None)])}
 <h1>Thuê xe Honda Vision Đà Lạt</h1>
 <p class="lead">Văn Phú cho thuê Honda Vision 110cc tại Đà Lạt: xe tay ga nhẹ, dễ dắt, giá cố định. Không cọc tiền, kèm mũ bảo hiểm, mở cửa từ 4:30 sáng mỗi ngày.</p>
 <div class="ticket">150.000 VND / ngày</div>
 <div class="cta">{hero_btns("vi")}</div>
</div></div></header>
<main class="wrap">
<section>
 <h2>Vì sao chọn Honda Vision ở Văn Phú</h2>
 <ul>
  <li><b>Tay ga, không số, không côn:</b> chỉ cần ga và phanh, dễ đi cho người mới.</li>
  <li><b>Nhẹ và dễ dắt:</b> thuận tiện khi đỗ xe, quay đầu trong phố hẹp và khu chợ.</li>
  <li><b>Hợp đi trong phố:</b> cà phê, chợ đêm, chợ Đà Lạt và các điểm quanh trung tâm.</li>
 </ul>
 <div class="posts">
  <figure style="margin:0"><img src="{rel(me, "/img/vision-white.jpg")}" alt="Honda Vision cho thuê tại Văn Phú Đà Lạt" loading="lazy" style="width:100%;border-radius:12px"></figure>
  <figure style="margin:0"><img src="{rel(me, "/img/honda-vision-cafe-garden-dalat.jpg")}" alt="Honda Vision thuê ở Đà Lạt đậu trước quán cà phê" loading="lazy" style="width:100%;border-radius:12px"></figure>
 </div>
</section>
<section>
 <h2>Điều kiện thuê Honda Vision</h2>
 <ul>
  <li><b>Giá 150.000 VND/ngày</b>, thanh toán khi nhận xe, không phụ phí.</li>
  <li><b>Không cọc tiền:</b> chỉ giữ CCCD hoặc hộ chiếu trong thời gian thuê.</li>
  <li><b>Kèm mũ bảo hiểm</b> và giá đỡ điện thoại; xe xăng được giao sẵn 1 lít xăng.</li>
  <li><b>Giao xe miễn phí</b> tới khách sạn, homestay khu trung tâm Đà Lạt khi thuê từ 2 ngày.</li>
  <li><b>Chạy thử và quay video</b> tình trạng xe trước khi nhận, để bảo vệ cả hai bên.</li>
 </ul>
 <p>Muốn xe số thay vì tay ga? Xem <a href="{rel(me, XS_PATH)}">thuê xe số Sirius FI và Wave RSX ở Đà Lạt</a>. Xem tất cả loại xe và giá tại <a href="{rel(me, home_path("vi"))}">trang thuê xe máy Đà Lạt</a>.</p>
</section>
<section>
 <h2>Câu hỏi thường gặp</h2>
 {faq_html}
</section>
<section>{contact_box("vi")}{cta_box("vi", me)}</section>
</main>
"""
    lds = [business_ld("vi", BASE + me), crumbs_ld("vi", [("Thuê xe Honda Vision Đà Lạt", me)]), faq_ld]
    return st_head(me, title, desc, lds, "vision-white") + body + foot("vi", frm=me)
write(VS_PATH, page_vision())

# ------------------------------------------------------------------ photo-spot map (en / vi / th)
def pm_km(a, b):
    import math
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))
def page_photomap(l, M=PM):
    t = M.T[l]; me = map_path(M, l)
    pre = rel(me, "")
    bar = "".join(f'<a href="{rel(me, map_path(M, x))}" hreflang="{x}" data-l="{x}"{" class=\"on\" aria-current=\"page\"" if x == l else ""}>{LABEL[x]}</a>' for x in M.LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + map_path(M, x)}">\n' for x in M.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + map_path(M, "en")}">\n'
    pts = []
    rows = ""
    _route = getattr(M, "ROUTE", False)
    _legs = route_legs(M.SPOTS) if _route else []
    for i, (sid, lat, lng, cid, ev, h) in enumerate(M.SPOTS, 1):
        n, best, d = t["s"][sid]
        hr = t["h"].get(h, h)
        g = gmap(cid, lat, lng)
        ph = M.img_link(sid)
        own = (OUT / "img" / "spots" / f"{sid}.jpg").exists()
        thumb = f'<img src="{pre}img/spots/{sid}.jpg" alt="{n}" loading="lazy" style="width:96px;height:72px;object-fit:cover;border-radius:8px;flex:none">' if own else ""
        pts.append({"i": i, "n": n, "lat": lat, "lng": lng, "ev": ev, "g": g, "b": best, "h": hr, "p": ph})
        guide = getattr(M, "GUIDES", {"pink": "domainedemarie"}).get(sid)
        nm = f'<a href="{rel(me, art_path(l, guide))}">{n}</a>' if guide and guide in C[l]["articles"] else n
        rows += (f'<li id="s{i}"><span class="pmn {"ev" if ev else "gas"}">{i}</span>{thumb}<div><b>{nm}</b><br><small>{(f"+{_legs[i-1]:.1f} km {t['leg']} · ") if _route else f"≈ {pm_km(M.CENTER, (lat, lng)):.1f} km · "}{t["hours"]}: {hr} · {t["best"]}: {best}</small>'
                 f'<br>{d}{(f"<br>🎟 <b>{t[chr(112)+chr(114)+chr(105)+chr(99)+chr(101)+chr(95)+chr(108)]}:</b> " + M.PRICE[l][sid]) if l in getattr(M, "PRICE", {}) else ""}<br><a href="{g}" target="_blank" rel="noopener">📍 {t["dir"]}</a> · <a href="{ph}" target="_blank" rel="noopener">📷 {t["photo"]}</a>{vlink(l, cid)}</div></li>')
    seasons = "".join(f"<li><b>{a}</b> — {b}</li>" for a, b in t.get("season", []))
    tips = "".join(f"<li>{x}</li>" for x in t["tips"])
    pdf = f"{pre}files/{getattr(M, 'PDF', 'VanPhu-Dalat-Photo-Map')}-{l.upper()}.pdf"
    pdf_btn = f'<a class="btn wa" href="{pdf}" download>⬇ {t["pdf"]}</a>' if getattr(M, "PDF", "VanPhu-Dalat-Photo-Map") else ""
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": t["h1"], "itemListElement": [
        {"@type": "ListItem", "position": p["i"], "item": {"@type": "TouristAttraction", "name": p["n"], "geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lng"]}, "hasMap": p["g"]}} for p in pts]}
    js = json.dumps(pts, ensure_ascii=False)
    _ak = getattr(M, "ARTICLE", None)
    art_link = f' <a href="{rel(me, art_path(l, _ak))}" style="color:#fff;text-decoration:underline">{C[l]["articles"][_ak][2]} →</a>' if _ak and _ak in C[l]["articles"] else ""
    if getattr(M, "ROUTE", False) and l in DAY.LANGS:
        art_link = f' <a href="{rel(me, lang_root(l) + DAY.SLUG[l] + "/")}" style="color:#fff;text-decoration:underline">{DAY.T[l]["h1"]} →</a>'
    return f"""<!doctype html>
<html lang="{l}"{' dir="rtl"' if l == "he" else ""}><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}"><link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="website"><meta property="og:locale" content="{LOCALE[l]}"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}"><meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/electric-row.jpg">
{ldjson(ld)}
<link rel="stylesheet" href="/vendor/leaflet/leaflet.css">
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}
#pmap{{height:460px;border-radius:14px;border:1px solid var(--line)}}
.pmlist{{list-style:none;padding:0;display:grid;gap:10px}} .pmlist li{{display:flex;gap:10px;align-items:flex-start;border-bottom:1px solid var(--line);padding-bottom:10px}}
.pmn{{flex:none;width:28px;height:28px;border-radius:50%;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px}} .pmn.ev{{background:#0f7a4f}} .pmn.gas{{background:#c06a00}}
.pmk{{background:none;border:none}} .pmk span{{display:flex;width:26px;height:26px;border-radius:50%;color:#fff;font:700 12px sans-serif;align-items:center;justify-content:center;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}}
.pmleg{{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;margin:8px 0}}
</style></head><body>
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{bar}</div></div>
<div class="hero"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}{art_link}</p>
<div class="cta">{pdf_btn}<a class="btn alt" href="{rel(me, home_path(l))}">{t["cta_h"]}</a></div></div></div></header>
<main class="wrap">
<section><div id="pmap" role="img" aria-label="{t["h1"]}"></div>
<div class="pmleg"><span><span class="pmn ev" style="display:inline-flex;width:14px;height:14px"></span> {t["ev"]}</span><span><span class="pmn gas" style="display:inline-flex;width:14px;height:14px"></span> {t["gas"]}</span></div>
<p class="note">{(t["total"].format(km=round(sum(_legs))) + " · ") if _route else ""}{t["check"]} · ≈ {t["km"]}</p></section>
<section><ol class="pmlist">{rows}</ol></section>
<section class="prose">{"" if _route else f'<h2>{t["season_h"]}</h2><ul>{seasons}</ul>'}<h2>{t["tips_h"]}</h2><ul>{tips}</ul></section>
<section>{arr_link(l, me) if M.__name__.split(".")[-1] in ARR.MAPS_FROM else ""}{cta_box(l, me)}</section>
</main>
<script src="/vendor/leaflet/leaflet.js"></script>
<script>
(function(){{if(!window.L)return;var P={js};
var m=L.map('pmap',{{scrollWheelZoom:false}});L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',{{maxZoom:18,attribution:'&copy; OpenStreetMap'}}).addTo(m);
var b=[];P.forEach(function(p){{var c=p.ev?'#0f7a4f':'#c06a00';var k=L.marker([p.lat,p.lng],{{icon:L.divIcon({{className:'pmk',html:'<span style="background:'+c+'">'+p.i+'</span>',iconSize:[26,26],iconAnchor:[13,13]}})}}).addTo(m);
k.bindPopup('<b>'+p.i+'. '+p.n+'</b><br>{t["hours"]}: '+p.h+'<br>{t["best"]}: '+p.b+'<br><a href='+JSON.stringify(p.g)+' target=_blank rel=noopener>📍 {t["dir"]}</a> · <a href='+JSON.stringify(p.p)+' target=_blank rel=noopener>📷 {t["photo"]}</a>');b.push([p.lat,p.lng]);}});
L.marker([{LAT},{LON}],{{icon:L.divIcon({{className:'pmk',html:'<span style="background:#1a1a1a;width:auto;padding:0 8px;border-radius:12px">Van Phu</span>',iconSize:[70,26],iconAnchor:[35,13]}})}}).addTo(m).bindPopup('<b>{t["shop"]}</b><br><a href="{GMAPS}" target="_blank" rel="noopener">{t["dir"]} →</a>');
{'L.polyline([['+str(LAT)+','+str(LON)+']].concat(b).concat([['+str(LAT)+','+str(LON)+']]),{color:\'#0f7a4f\',weight:3,opacity:.55,dashArray:\'6 8\'}).addTo(m);' if _route else ''}
m.fitBounds(b,{{padding:[20,20]}});}})();
</script>
""" + foot(l, frm=me)

# ------------------------------------------------------------------ places hub (pillar page, vi + en)
THEMES = [RN, RC, PM, WF, AM, FM, PG, CH, SF, CL, CF, NC, NM, BB, FE, HT, H4, H3, BU, DN, NT]
_TNAME = {M.__name__.split(".")[-1]: M for M in THEMES}
def hub_link(l, me, key):
    if key == "routes": return rel(me, routes_path(l))
    if key == "ev": return rel(me, ev_path(l))
    if key == "hub": return rel(me, hub_path(l))
    if key == "day": return rel(me, day_path(l))
    if key.startswith("art:"): return rel(me, art_path(l, key[4:]))
    if key.startswith("map:"): return rel(me, map_path(_TNAME[key[4:]], l))
    raise KeyError(key)
def page_hub(l):
    t = HUB.T[l]; me = hub_path(l); pre = rel(me, "")
    sp = HUB.spots(l); n = len(sp)
    far = max(sp, key=lambda x: pm_km((LAT, LON), (x[1], x[2])))
    gas = [x[6][0].split(" (")[0] for x in sp if not x[4]]
    fill = {"n": n, "ev_n": sum(1 for x in sp if x[4]), "gas_names": ", ".join(gas), "far_name": far[6][0].split(" (")[0], "far_km": f"{pm_km((LAT, LON), (far[1], far[2])):.0f}", "center_max": f"{math.ceil(max(pm_km((LAT, LON), (x[1], x[2])) for x in sp if x[7] == "center")):.0f}"}
    bar = "".join(f'<a href="{rel(me, hub_path(x))}" hreflang="{x}" data-l="{x}"{" class=\"on\" aria-current=\"page\"" if x == l else ""}>{LABEL[x]}</a>' for x in HUB.LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + hub_path(x)}">\n' for x in HUB.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + hub_path("en")}">\n'
    pts, secs, i = [], "", 0
    for z in HUB.ZONES:
        zs = sorted([x for x in sp if x[7] == z], key=lambda x: pm_km((LAT, LON), (x[1], x[2])))
        if not zs: continue
        rows = ""
        for sid, lat, lng, cid, ev, h, (nm, best, d), _z, M in zs:
            i += 1
            g = gmap(cid, lat, lng)
            hr = PM.T[l]["h"].get(h, h)
            ak = HUB.GUIDE.get(sid)
            name = f'<a href="{rel(me, art_path(l, ak))}">{nm}</a>' if ak else nm
            links = f'<a href="{g}" target="_blank" rel="noopener">📍 {t["dir"]}</a>'
            links += vlink(l, cid)
            if M is not None: links += f' · <a href="{rel(me, map_path(M, l))}">🗺 {t["themap"]}: {M.T[l]["h1"]}</a>'
            if ak: links += f' · <a href="{rel(me, art_path(l, ak))}">📖 {t["guide"]}</a>'
            km_ = pm_km((LAT, LON), (lat, lng))
            rows += (f'<li><span class="pmn {"ev" if ev else "gas"}">{i}</span><div><b>{name}</b><br><small>≈ {km_:.1f} {t["km"]} · {t["hours"]}: {hr} · {t["best"]}: {best}</small><br>{d}{(f"<br>🎟 <b>{HUBP.LABEL[l]}:</b> " + HUBP.PRICE[l][sid]) if sid in HUBP.PRICE.get(l, {}) else ""}<br>{links}</div></li>')
            pts.append({"i": i, "n": nm, "lat": lat, "lng": lng, "ev": ev, "g": g, "b": best, "h": hr})
        q, sub = t["zones"][z]
        secs += f'<section id="{z}"><h2>{q}</h2><p>{sub}</p><ol class="hublist">{rows}</ol></section>'
    faqs = [(q, a.format(**fill), lk) for q, a, lk in t["faq"]]
    faq_html = "".join(f'<section id="q{j}"><h2>{q}</h2><p>{a}</p>' + (('<p class="chips">' + "".join(f'<a href="{hub_link(l, me, k)}">{x} →</a>' for k, x in lk) + "</p>") if lk else "") + "</section>" for j, (q, a, lk) in enumerate(faqs, 1))
    toc = "".join(f'<li><a href="#{z}">{t["zones"][z][0]}</a></li>' for z in HUB.ZONES) + "".join(f'<li><a href="#q{j}">{q}</a></li>' for j, (q, a, lk) in enumerate(faqs, 1))
    themes = "".join(f'<a href="{rel(me, map_path(M, l))}">{M.T[l]["h1"]}</a>' for M in THEMES if l in M.LANGS)
    if l in TM.LANGS: themes = f'<a href="{rel(me, lang_root(l) + TM.SLUG[l] + "/")}"><b>{TM.T[l]["h1"]}</b></a>' + themes
    title, h1, desc = t["title"].format(**fill), t["h1"].format(**fill), t["desc"].format(**fill)
    lds = [{"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "inLanguage": l, "mainEntityOfPage": BASE + me,
            "image": BASE + "img/airblade.jpg", "datePublished": HUB.UPDATED, "dateModified": HUB.UPDATED,
            "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}, "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}},
           {"@context": "https://schema.org", "@type": "ItemList", "name": h1, "itemListElement": [
            {"@type": "ListItem", "position": p["i"], "item": {"@type": "TouristAttraction", "name": p["n"], "geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lng"]}, "hasMap": p["g"]}} for p in pts]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a, lk in faqs]},
           crumbs_ld(l, [(h1, me)])]
    js = json.dumps(pts, ensure_ascii=False)
    pm = PM.T[l]
    return f"""<!doctype html>
<html lang="{l}"{' dir="rtl"' if l == "he" else ""}><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<meta name="description" content="{desc}"><link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="article"><meta property="og:locale" content="{LOCALE[l]}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/airblade.jpg">
{"".join(ldjson(x) for x in lds)}
<link rel="stylesheet" href="/vendor/leaflet/leaflet.css">
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}
#pmap{{height:480px;border-radius:14px;border:1px solid var(--line)}}
.pmn{{flex:none;width:28px;height:28px;border-radius:50%;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px}} .pmn.ev{{background:#0f7a4f}} .pmn.gas{{background:#c06a00}}
.pmk{{background:none;border:none}} .pmk span{{display:flex;width:24px;height:24px;border-radius:50%;color:#fff;font:700 11px sans-serif;align-items:center;justify-content:center;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}}
.pmleg{{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;margin:8px 0}}
@media(max-width:640px){{.toc{{columns:1}}}}
</style></head><body>
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{bar}</div></div>
<div class="hero">{crumbs(l, me, [(h1, None)])}<h1>{h1}</h1><p class="lead">{t["lead"]}</p><p class="upd"><time datetime="{HUB.UPDATED}">{UPD[l]}: {fdate(l, HUB.UPDATED)}</time></p>
<div class="cta">{hero_btns(l)}</div></div></div></header>
<main class="wrap">
<section><h2>{t["toc"]}</h2><ol class="toc">{toc}</ol></section>
<section><h2>{t["map_h"]}</h2><div id="pmap" role="img" aria-label="{t["map_h"]}"></div>
<div class="pmleg"><span><span class="pmn ev" style="display:inline-flex;width:14px;height:14px"></span> {t["ev"]}</span><span><span class="pmn gas" style="display:inline-flex;width:14px;height:14px"></span> {t["gas"]}</span></div>
<p class="note">{pm["check"]} · ≈ {t["km"]}{(" · " + HUBP.NOTE[l]) if l in HUBP.NOTE else ""}</p></section>
{secs}
<section><h2>{t["faq_h"]}</h2></section>
{faq_html}
<section><h2>{t["themes_h"]}</h2><p class="chips">{themes}</p></section>
<section class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px"><h2>{t["cta_h"]}</h2><p>{t["cta"]}</p><p><a class="btn" href="{rel(me, home_path(l))}">{kw_rent(l)} →</a> <a class="btn alt" href="{rel(me, ev_path(l))}" style="border:1px solid var(--line)">{EV[l]["h1"]} →</a></p></section>
<section>{contact_box(l)}</section>
</main>
<script src="/vendor/leaflet/leaflet.js"></script>
<script>
(function(){{if(!window.L)return;var P={js};
var m=L.map('pmap',{{scrollWheelZoom:false}});L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',{{maxZoom:18,attribution:'&copy; OpenStreetMap'}}).addTo(m);
var b=[];P.forEach(function(p){{var c=p.ev?'#0f7a4f':'#c06a00';var k=L.marker([p.lat,p.lng],{{icon:L.divIcon({{className:'pmk',html:'<span style="background:'+c+'">'+p.i+'</span>',iconSize:[24,24],iconAnchor:[12,12]}})}}).addTo(m);
k.bindPopup('<b>'+p.i+'. '+p.n+'</b><br>{t["hours"]}: '+p.h+'<br>{t["best"]}: '+p.b+'<br><a href='+JSON.stringify(p.g)+' target=_blank rel=noopener>📍 {t["dir"]}</a>');b.push([p.lat,p.lng]);}});
L.marker([{LAT},{LON}],{{icon:L.divIcon({{className:'pmk',html:'<span style="background:#1a1a1a;width:auto;padding:0 8px;border-radius:12px">Van Phu</span>',iconSize:[70,26],iconAnchor:[35,13]}})}}).addTo(m).bindPopup('<b>{pm["shop"]}</b><br><a href="{GMAPS}" target="_blank" rel="noopener">{t["dir"]} →</a>');
m.fitBounds(b,{{padding:[20,20]}});}})();
</script>
""" + foot(l, frm=me)
for l in HUB.LANGS:
    write(hub_path(l), page_hub(l))
# ------------------------------------------------------------------ day-trip hub (self-drive routes, vi + en)
def page_day(l):
    t = DAY.T[l]; me = day_path(l)
    bar = "".join(f'<a href="{rel(me, day_path(x))}" hreflang="{x}" data-l="{x}"{" class=\"on\" aria-current=\"page\"" if x == l else ""}>{LABEL[x]}</a>' for x in DAY.LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + day_path(x)}">\n' for x in DAY.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + day_path("en")}">\n'
    cards = ""
    for M in (RC, RN):
        mt = M.T[l]; name = M.__name__.split(".")[-1]
        stops = " → ".join(mt["s"][x[0]][0] for x in M.SPOTS)
        pdf = rel(me, f"files/{M.PDF}-{l.upper()}.pdf")
        cards += (f'<div class="route"><h3><a href="{rel(me, map_path(M, l))}">{mt["h1"]}</a></h3><div class="meta">{t["km"].format(km=M.TOTAL)}</div>'
                  f'<p><b>{t["stops"]}:</b> {stops}</p><p>{t["verdict"][name]}</p>'
                  f'<p><a class="btn wa" href="{rel(me, map_path(M, l))}">🗺 {t["open"]} →</a> <a class="btn alt" href="{pdf}" download style="border:1px solid var(--line)">⬇ {t["pdf"]}</a></p></div>')
    more = "".join(f'<a href="{hub_link(l, me, k)}">{x} →</a>' for k, x in t["more"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    lds = [{"@context": "https://schema.org", "@type": "Article", "headline": t["h1"], "description": t["desc"], "inLanguage": l, "mainEntityOfPage": BASE + me,
            "image": BASE + "img/airblade.jpg", "datePublished": DAY.UPDATED, "dateModified": DAY.UPDATED,
            "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}, "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}},
           {"@context": "https://schema.org", "@type": "ItemList", "name": t["routes_h"], "itemListElement": [
            {"@type": "ListItem", "position": i, "url": BASE + map_path(M, l), "name": M.T[l]["h1"]} for i, M in enumerate((RC, RN), 1)]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
           crumbs_ld(l, [(t["h1"], me)])]
    return f"""<!doctype html>
<html lang="{l}"><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}"><link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="article"><meta property="og:locale" content="{LOCALE[l]}"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}"><meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/airblade.jpg">
{"".join(ldjson(x) for x in lds)}
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}
</style></head><body>
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{bar}</div></div>
<div class="hero">{crumbs(l, me, [(t["h1"], None)])}<h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><p class="upd"><time datetime="{DAY.UPDATED}">{UPD[l]}: {fdate(l, DAY.UPDATED)}</time></p>
<div class="cta">{hero_btns(l)}</div></div></div></header>
<main class="wrap">
<section><h2>{t["routes_h"]}</h2>{cards}</section>
<section><h2>{t["more_h"]}</h2><p class="chips">{more}</p></section>
<section class="faq"><h2>{t["faq_h"]}</h2>{faq}</section>
<section>{contact_box(l)}{cta_box(l, me)}</section>
</main>
""" + foot(l, frm=me)
for l in DAY.LANGS:
    write(day_path(l), page_day(l))

# ------------------------------------------------------------------ licence pillar page (all languages, owner asked 2026-10-28)
_PMAPS = {"busmap": BU, "nhatrangbusmap": NT, "danangbusmap": DN}
def page_pillar(M, l):
    t = M.T[l]; me = pil_path(M, l); langs = [x for x in M.LANGS if x in M.T]; img = getattr(M, "IMG", "electric-row")
    links = {"{EV}": rel(me, ev_path(l)), "{HOME}": rel(me, home_path(l)), "{DOCS}": rel(me, art_path(l, "lt-documents")),
             "{RULES}": rel(me, art_path(l, "evrules")), "{ROUTES}": rel(me, routes_path(l)), "{LIC}": rel(me, lic_path(l)), "{ARRIVE}": rel(me, arr_path(l))}
    def fill(x):
        for a, b in links.items(): x = x.replace(a, b)
        x = re.sub(r"\{ART:([a-z0-9-]+)\}", lambda m: rel(me, art_path(l, m.group(1))), x)
        return re.sub(r"\{MAP:([a-z]+)\}", lambda m: rel(me, map_path(_PMAPS[m.group(1)], l)), x)
    bar = "".join(f'<a href="{rel(me, pil_path(M, x))}" hreflang="{x}" data-l="{x}"{" class=\"on\" aria-current=\"page\"" if x == l else ""}>{LABEL[x]}</a>' for x in langs)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + pil_path(M, x)}">\n' for x in langs) + f'<link rel="alternate" hreflang="x-default" href="{BASE + pil_path(M, "en")}">\n'
    short = "".join(f"<tr><td>{k}</td><td><b>{v}</b></td></tr>" for k, v in t["short"])
    secs = "".join(f'<section class="prose"><h2>{h}</h2>{fill(b)}</section>' for h, b in t["secs"])
    faq = "".join(f"<details><summary>{q}</summary><p>{fill(a)}</p></details>" for q, a in t["faq"])
    more = "".join(f'<a href="{fill(u)}">{x} →</a>' for u, x in t["more"])
    strip = lambda x: re.sub(r"<[^>]+>", "", x)
    lds = [{"@context": "https://schema.org", "@type": "Article", "headline": t["h1"], "description": t["desc"], "inLanguage": l, "mainEntityOfPage": BASE + me,
            "image": BASE + f"img/{img}.jpg", "datePublished": M.UPDATED, "dateModified": M.UPDATED,
            "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}, "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in t["faq"]]},
           business_ld(l, BASE + me), crumbs_ld(l, [(t["crumb"], me)])]
    return f"""<!doctype html>
<html lang="{l}"{' dir="rtl"' if l == "he" else ""}><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}"><link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="article"><meta property="og:locale" content="{LOCALE[l]}"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}"><meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/{img}.jpg">
{"".join(ldjson(x) for x in lds)}
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}
</style></head><body>
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{bar}</div></div>
<div class="hero">{crumbs(l, me, [(t["crumb"], None)])}<h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><p class="upd"><time datetime="{M.UPDATED}">{UPD[l]}: {fdate(l, M.UPDATED)}</time></p>
<div class="cta">{hero_btns(l)}</div></div></div></header>
<main class="wrap">
<section><h2>{t["short_h"]}</h2><table class="price">{short}</table></section>
<section><img src="{rel(me, f"/img/{img}.jpg")}" alt="{t["h1"]}" loading="lazy" style="width:100%;border-radius:12px"></section>
{secs}
<section class="faq"><h2>{t["faq_h"]}</h2>{faq}</section>
<section><h2>{t["more_h"]}</h2><p class="chips">{more}</p></section>
<section>{contact_box(l)}{cta_box(l, me)}</section>
</main>
""" + foot(l, frm=me)
for _M in (LIC, ARR):
    for l in [x for x in _M.LANGS if x in _M.T]:
        write(pil_path(_M, l), page_pillar(_M, l))

# ------------------------------------------------------------------ tourist map by motorbike route (vi + en)
def page_tourmap(l):
    t = TM.T[l]; me = tm_path(l)
    hub = {s[0]: s for s in HUB.spots(l)}
    amt = AM.T[l]["s"]
    am = {s[0]: (s[0], s[1], s[2], s[3], s[4], s[5], amt[s[0]], None, AM) for s in AM.SPOTS}
    routes = []
    for rid, col, stops in TM.ROUTES:
        sp = [hub[sid] if src == "hub" else am[sid] for src, sid in stops]
        lg = route_legs(sp); tot = sum(lg)
        ev = all(x[4] for x in sp) and tot * TM.ROAD[1] <= TM.EV_MAX
        routes.append((rid, col, sp, tot, ev))
    nm = t["names"]
    ev_list = ", ".join(nm[r[0]][0] for r in routes if r[4])
    far = max(routes, key=lambda r: r[3])
    fill = {"ev_list": ev_list, "far_name": nm[far[0]][0], "far_km": f"{far[3]:.0f}"}
    bar = "".join(f'<a href="{rel(me, tm_path(x))}" hreflang="{x}" data-l="{x}"{" class=\"on\" aria-current=\"page\"" if x == l else ""}>{LABEL[x]}</a>' for x in TM.LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + tm_path(x)}">\n' for x in TM.LANGS) + f'<link rel="alternate" hreflang="x-default" href="{BASE + tm_path("en")}">\n'
    js_routes, cards, n = [], "", 0
    for k, (rid, col, sp, tot, ev) in enumerate(routes, 1):
        name, dur, intro = nm[rid]
        pts, rows = [], ""
        for sid, lat, lng, cid, sev, h, (pn, best, d), _z, M in sp:
            n += 1
            g = gmap(cid, lat, lng); hr = PM.T[l]["h"].get(h, h)
            rows += f'<li><span class="pmn" style="background:{col}">{n}</span><div><b>{pn}</b><br><small>{t["hours"]}: {hr}</small><br>{d}<br><a href="{g}" target="_blank" rel="noopener">📍 {t["dir"]}</a>{vlink(l, cid)}</div></li>'
            pts.append({"i": n, "n": pn, "lat": lat, "lng": lng, "g": g, "h": hr})
        wp = "|".join(f"{p['lat']},{p['lng']}" for p in pts)
        gdir = f"https://www.google.com/maps/dir/?api=1&origin={LAT},{LON}&destination={LAT},{LON}&waypoints={wp}&travelmode=driving".replace("|", "%7C")
        a, b = (round(tot * f) for f in TM.ROAD)
        bike = t["ev_ok"] if ev else t["ev_no"]
        cards += (f'<section id="{rid}" class="route"><h3><span class="dot" style="background:{col}"></span>{name}</h3>'
                  f'<div class="meta">{t["loop"]}: ≈ {tot:.0f} {t["straight"]} · {t["road"].format(a=a, b=b)} · {t["time"]}: {dur}</div>'
                  f'<p>{intro}</p><p><b>{t["bike"]}:</b> {"🔋" if ev else "⛽"} {bike}</p>'
                  f'<ol class="pmlist">{rows}</ol><p><a class="btn alt" href="{_esc(gdir)}" target="_blank" rel="noopener" style="border:1px solid var(--line)">🧭 {t["open_gm"]}</a></p></section>')
        js_routes.append({"id": rid, "c": col, "n": name, "p": pts})
    plans = "".join(f'<li><b>{d}:</b> {x}' + (f' <a href="{hub_link(l, me, lk)}">→</a>' if lk and (not lk.startswith("art:") or lk[4:] in C[l]["articles"]) else "") + "</li>" for d, x, lk in t["plans"])
    avoid = "".join(f"<li>{x}</li>" for x in t["avoid"])
    faqs = [(q, a.format(**fill)) for q, a in t["faq"]]
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    themes = "".join(f'<a href="{rel(me, map_path(M, l))}">{M.T[l]["h1"]}</a>' for M in THEMES if l in M.LANGS)
    more = "".join(f'<a href="{hub_link(l, me, k)}">{x} →</a>' for k, x in t["more"])
    toc = f'<li><a href="#map">{t["map_h"]}</a></li>' + "".join(f'<li><a href="#{r[0]}">{nm[r[0]][0]}</a></li>' for r in routes) + f'<li><a href="#plan">{t["plan_h"]}</a></li><li><a href="#faq">{t["faq_h"]}</a></li>'
    chips = f'<button type="button" class="rbtn on" data-r="">{t["all"]}</button>' + "".join(f'<button type="button" class="rbtn" data-r="{r[0]}"><span class="dot" style="background:{r[1]}"></span>{nm[r[0]][0].split(" · ")[0]}</button>' for r in routes)
    allp = [p for r in js_routes for p in r["p"]]
    lds = [{"@context": "https://schema.org", "@type": "Article", "headline": t["h1"], "description": t["desc"], "inLanguage": l, "mainEntityOfPage": BASE + me,
            "image": BASE + "img/airblade.jpg", "datePublished": TM.UPDATED, "dateModified": TM.UPDATED,
            "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}, "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}},
           {"@context": "https://schema.org", "@type": "ItemList", "name": t["routes_h"], "itemListElement": [
            {"@type": "ListItem", "position": i, "item": {"@type": "TouristTrip", "name": r["n"], "itinerary": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": j, "item": {"@type": "TouristAttraction", "name": p["n"], "geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lng"]}, "hasMap": p["g"]}} for j, p in enumerate(r["p"], 1)]}}}
            for i, r in enumerate(js_routes, 1)]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
           crumbs_ld(l, [(t["h1"], me)])]
    js = json.dumps(js_routes, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{l}"><head><meta charset="utf-8"><script>if(location.protocol==="http:"&&location.hostname==="vanphudalat.com")location.replace("https:"+location.href.slice(5))</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}"><link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="article"><meta property="og:locale" content="{LOCALE[l]}"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}"><meta property="og:url" content="{BASE + me}"><meta property="og:image" content="{BASE}img/airblade.jpg">
{"".join(ldjson(x) for x in lds)}
<link rel="stylesheet" href="/vendor/leaflet/leaflet.css">
<link rel="preload" href="/fonts/bvp-latin-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/bvp-latin-800.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}
#pmap{{height:480px;border-radius:14px;border:1px solid var(--line)}}
.pmlist{{list-style:none;padding:0;display:grid;gap:10px}} .pmlist li{{display:flex;gap:10px;align-items:flex-start;border-bottom:1px solid var(--line);padding-bottom:10px}}
.pmn{{flex:none;width:28px;height:28px;border-radius:50%;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px}}
.pmk{{background:none;border:none}} .pmk span{{display:flex;width:24px;height:24px;border-radius:50%;color:#fff;font:700 11px sans-serif;align-items:center;justify-content:center;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}}
.dot{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px;vertical-align:middle}}
.rbar{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}} .rbtn{{font:inherit;font-size:14px;padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:#fff;cursor:pointer}} .rbtn.on{{background:#1a1a1a;color:#fff;border-color:#1a1a1a}}
.route .meta{{font-size:14px;opacity:.8;margin:4px 0 8px}}
@media(max-width:640px){{.toc{{columns:1}}}}
</style></head><body>
<header><div class="wrap"><div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{bar}</div></div>
<div class="hero">{crumbs(l, me, [(t["h1"], None)])}<h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><p class="upd"><time datetime="{TM.UPDATED}">{UPD[l]}: {fdate(l, TM.UPDATED)}</time></p>
<div class="cta">{hero_btns(l)}</div></div></div></header>
<main class="wrap">
<section><h2>{t["toc"]}</h2><ol class="toc">{toc}</ol></section>
<section id="map"><h2>{t["map_h"]}</h2><div class="rbar">{chips}</div><div id="pmap" role="img" aria-label="{t["map_h"]}"></div>
<p class="note">{t["km_note"]}</p></section>
<section><h2>{t["routes_h"]}</h2></section>
{cards}
<section id="plan" class="prose"><h2>{t["plan_h"]}</h2><ul>{plans}</ul><h3>{t["avoid_h"]}</h3><ul>{avoid}</ul></section>
<section id="faq" class="faq"><h2>{t["faq_h"]}</h2>{faq}</section>
<section><h2>{t["themes_h"]}</h2><p class="chips">{themes}</p></section>
<section><h2>{t["more_h"]}</h2><p class="chips">{more}</p></section>
<section class="note" style="border:1px solid var(--line);border-radius:12px;padding:12px 16px"><h2>{t["cta_h"]}</h2><p>{t["cta"]}</p><p><a class="btn" href="{rel(me, home_path(l))}">{kw_rent(l)} →</a> <a class="btn alt" href="{rel(me, ev_path(l))}" style="border:1px solid var(--line)">{EV[l]["h1"]} →</a></p></section>
<section>{contact_box(l)}</section>
</main>
<script src="/vendor/leaflet/leaflet.js"></script>
<script>
(function(){{if(!window.L)return;var R={js},S=[{LAT},{LON}];
var m=L.map('pmap',{{scrollWheelZoom:false}});L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',{{maxZoom:18,attribution:'&copy; OpenStreetMap'}}).addTo(m);
var G={{}};R.forEach(function(r){{var g=L.featureGroup(),ll=[S];r.p.forEach(function(p){{ll.push([p.lat,p.lng]);L.marker([p.lat,p.lng],{{icon:L.divIcon({{className:'pmk',html:'<span style="background:'+r.c+'">'+p.i+'</span>',iconSize:[24,24],iconAnchor:[12,12]}})}}).bindPopup('<b>'+p.i+'. '+p.n+'</b><br><small>'+r.n+'</small><br>{t["hours"]}: '+p.h+'<br><a href='+JSON.stringify(p.g)+' target=_blank rel=noopener>📍 {t["dir"]}</a>').addTo(g);}});ll.push(S);
L.polyline(ll,{{color:r.c,weight:3,opacity:.6,dashArray:'6 8'}}).addTo(g);g.addTo(m);G[r.id]=g;}});
L.marker(S,{{icon:L.divIcon({{className:'pmk',html:'<span style="background:#1a1a1a;width:auto;padding:0 8px;border-radius:12px">Van Phu</span>',iconSize:[70,26],iconAnchor:[35,13]}})}}).addTo(m).bindPopup('<b>{t["shop"]}</b><br><a href="{GMAPS}" target="_blank" rel="noopener">{t["dir"]} →</a>');
var all=L.featureGroup(Object.keys(G).map(function(k){{return G[k]}}));m.fitBounds(all.getBounds(),{{padding:[20,20]}});
document.querySelectorAll('.rbtn').forEach(function(b){{b.addEventListener('click',function(){{var id=b.getAttribute('data-r');document.querySelectorAll('.rbtn').forEach(function(x){{x.classList.toggle('on',x===b)}});
Object.keys(G).forEach(function(k){{if(!id||k===id)G[k].addTo(m);else m.removeLayer(G[k]);}});m.fitBounds((id?G[id]:all).getBounds(),{{padding:[20,20]}});}});}});
}})();
</script>
""" + foot(l, frm=me)
for l in TM.LANGS:
    write(tm_path(l), page_tourmap(l))
(OUT / "files").mkdir(exist_ok=True)
for l in PM.LANGS:
    write(pm_path(l), page_photomap(l))
for _M in (FE, PG, CH, SF, CL, CF, BB, HT, H4, H3, BU, DN, RN, RC, WF, AM, FM, NC, NT, NM):
    for l in _M.LANGS:
        write(map_path(_M, l), page_photomap(l, _M))

urls = ""
for kind, key in groups:
    alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + path_of(x, kind, key)}"/>\n' for x in langs_of(kind, key))
    alts += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + path_of("en", kind, key)}"/>\n'
    for l in langs_of(kind, key):
        lm = mdate(l, key) if kind == "art" else max([adate(k) for k in arts(l)] + ["2026-10-10"])
        urls += f"  <url>\n    <loc>{BASE + path_of(l, kind, key)}</loc>\n{alts}    <lastmod>{lm}</lastmod>\n  </url>\n"
_pm_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + pm_path(x)}"/>\n' for x in PM.LANGS)
for l in PM.LANGS:
    urls += f"  <url>\n    <loc>{BASE + pm_path(l)}</loc>\n{_pm_alts}    <lastmod>2026-10-14</lastmod>\n  </url>\n"
for _M in (FE, PG, CH, SF, CL, CF, BB, HT, H4, H3, BU, DN, RN, RC, WF, AM, FM, NC, NT, NM):
    _alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + map_path(_M, x)}"/>\n' for x in _M.LANGS)
    for l in _M.LANGS:
        urls += f"  <url>\n    <loc>{BASE + map_path(_M, l)}</loc>\n{_alts}    <lastmod>2026-10-14</lastmod>\n  </url>\n"
_day_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + day_path(x)}"/>\n' for x in DAY.LANGS) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + day_path("en")}"/>\n'
for l in DAY.LANGS:
    urls += f"  <url>\n    <loc>{BASE + day_path(l)}</loc>\n{_day_alts}    <lastmod>{DAY.UPDATED}</lastmod>\n  </url>\n"
_hub_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + hub_path(x)}"/>\n' for x in HUB.LANGS) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + hub_path("en")}"/>\n'
for l in HUB.LANGS:
    urls += f"  <url>\n    <loc>{BASE + hub_path(l)}</loc>\n{_hub_alts}    <lastmod>{HUB.UPDATED}</lastmod>\n  </url>\n"
_tm_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + tm_path(x)}"/>\n' for x in TM.LANGS) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + tm_path("en")}"/>\n'
for l in TM.LANGS:
    urls += f"  <url>\n    <loc>{BASE + tm_path(l)}</loc>\n{_tm_alts}    <lastmod>{TM.UPDATED}</lastmod>\n  </url>\n"
for _M in (LIC, ARR):
    _pl = [x for x in _M.LANGS if x in _M.T]
    _alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + pil_path(_M, x)}"/>\n' for x in _pl) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + pil_path(_M, "en")}"/>\n'
    for l in _pl:
        urls += f"  <url>\n    <loc>{BASE + pil_path(_M, l)}</loc>\n{_alts}    <lastmod>{_M.UPDATED}</lastmod>\n  </url>\n"
_ab_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + about_path(x)}"/>\n' for x in AB.LANGS) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + about_path("en")}"/>\n'
for _l in AB.LANGS:
    urls += f"  <url>\n    <loc>{BASE + about_path(_l)}</loc>\n{_ab_alts}    <lastmod>{AB.UPDATED}</lastmod>\n  </url>\n"
_vl_alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + villa_path(x)}"/>\n' for x in VL.LANGS) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + villa_path("en")}"/>\n'
for _l in VL.LANGS:
    urls += f"  <url>\n    <loc>{BASE + villa_path(_l)}</loc>\n{_vl_alts}    <lastmod>{VL.UPDATED}</lastmod>\n  </url>\n"
for _me in [st_hub_path(), XS_PATH, VS_PATH, halal_path(), tour_path()] + [guide_path(_l, _g) for _l in GD.GUIDES for _g in GD.GUIDES[_l]] + [st_path(_s) for _s in ST.S]:
    urls += f"  <url>\n    <loc>{BASE + _me}</loc>\n    <lastmod>{ST.UPDATED}</lastmod>\n  </url>\n"
# Missing pages (GitHub Pages serves /404.html for any unknown URL): send the visitor to the home page instead of a blank error.
(OUT / "404.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Van Phu Dalat – Motorbike Rental</title><meta name="robots" content="noindex">
<link rel="canonical" href="{BASE}">
<script>location.replace("{BASE}");</script>
<meta http-equiv="refresh" content="0; url={BASE}">
</head><body><p>Page not found. <a href="{BASE}">Go to the Van Phu Dalat home page</a>.</p></body></html>
""", encoding="utf-8")
# Sitemap scope: keep priority languages only (English root + vi, ru, zh, id, ms, th, ko, ja).
# Other-language pages and PDFs stay on the site (linked and reachable) but are left out of the sitemap,
# so Google's crawl budget goes to the pages we want indexed. hreflang alternates are filtered the same way.
SITEMAP_LANGS = {"vi", "ru", "zh", "id", "ms", "th", "ko", "ja"}
_ALL_PREFIX = {"de", "fr", "es", "he", "it", "nl", "km", "lo", "my"}
def _keep_loc(loc):
    path = loc[len(BASE):]
    if path.startswith("files/"):
        return False
    if re.match(r"^(?:(?:de|fr|es|he|it|nl|km|lo|my)/blog/|vi/thue-xe-may-da-lat/duong-)", path):
        return False
    first = path.split("/", 1)[0]
    return not (first in _ALL_PREFIX)
_kept = []
for _blk in urls.split("  <url>\n")[1:]:
    _loc = _blk.split("<loc>", 1)[1].split("</loc>", 1)[0]
    if not _keep_loc(_loc):
        continue
    _blk = "\n".join(_ln for _ln in _blk.split("\n") if not any(f'hreflang="{x}"' in _ln for x in _ALL_PREFIX))
    _kept.append("  <url>\n" + _blk)
urls = "".join(_kept)

# Thin pages kept out of Google's index (still reachable through links):
#  - blog posts in the non-priority languages (de, fr, es, he, it, nl, km, lo, my); English and priority-language blogs stay indexed;
#  - the vi road pages (thue-xe-may-da-lat/duong-*), near-identical templates per street name.
# They are also dropped from the sitemap above via _keep_loc.
import re as _re
_NOINDEX_RE = _re.compile(r"^(?:(?:de|fr|es|he|it|nl|km|lo|my)/blog/|vi/thue-xe-may-da-lat/duong-)")
for _f in OUT.rglob("index.html"):
    _rel = _f.parent.relative_to(OUT).as_posix() + "/"
    if _NOINDEX_RE.match(_rel):
        _t = _f.read_text(encoding="utf-8")
        if 'name="robots" content="noindex"' not in _t:
            _t = _t.replace("<head>", '<head><meta name="robots" content="noindex">', 1)
            _f.write_text(_t, encoding="utf-8")
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n", encoding="utf-8")
LLMS = f"""# Van Phu Dalat Motorbike Rental (Thuê xe máy Đà Lạt Văn Phú)

> Local motorbike and scooter rental in Da Lat (Đà Lạt), Vietnam. Honda Vision 110cc, Honda Air Blade 125cc and electric scooters, all 150,000 VND per day. No cash deposit, free hotel delivery in central Da Lat for rentals of 2+ days.

## Key facts
- Address: 1/15/5 Thông Thiên Học, Xuân Hương – Đà Lạt, Lâm Đồng, Vietnam ({GMAPS})
- Google Maps address of the same shop: Khu Quy Hoạch/L8 Đường Bùi Thị Xuân, Xuân Hương - Đà Lạt, Lâm Đồng 670000 (actual location: 1/15/5 Thông Thiên Học, Xuân Hương - Đà Lạt, Lâm Đồng 670000)
- Price: 150,000 VND/day for every bike, fixed, no hidden fees
- Opening hours: every day 4:30 AM – 9:00 PM
- Rental day: from pickup until 9:00 PM the same day
- Deposit: no cash deposit; the guest leaves a passport or ID card; rental fee paid upfront
- Included: free helmet and phone holder with every bike; gas scooters come with 1 liter of fuel
- Delivery: free to hotels in central Da Lat for rentals of 2 days or more
- Before renting: test ride and a video of the bike's condition, filmed together
- Tripadvisor: {TRIPADVISOR}
- Yandex Maps: {YANDEX_ORG}
- Phone: +84 944 081 101 (main) / +84 834 622 149 (second line)
- Booking: WhatsApp +84 944 081 101 or +84 834 622 149, Zalo 0944 081 101, Telegram @vanphudalat, WeChat vanphudalat
- YouTube channel: {YT}
- Languages on the website: {", ".join(LABEL.values())}

## Pages
- [Home (English)]({BASE}): prices, bikes, FAQ, map
- [Electric scooter rental (2 batteries per scooter, about 50–60 km in total — 25–30 km each; battery swap 20,000 VND)]({BASE + ev_path("en")})
- [Da Lat photo spot map (16 places, opening hours, free PDF)]({BASE + pm_path("en")})
- [Da Lat pagoda map (7 pagodas and Zen monasteries, opening hours, free PDF)]({BASE + map_path(PG, "en")})
- [Da Lat church map (6 churches incl. the Rooster Church and Domaine de Marie, opening hours, free PDF)]({BASE + map_path(CH, "en")})
- [Da Lat wild sunflower (dã quỳ) map — 9 spots, late Oct–Dec, free PDF]({BASE + map_path(SF, "en")})
- [Da Lat cloud hunting & sunrise map — 8 spots, best hours and months, free PDF]({BASE + map_path(CL, "en")})
- [Da Lat cafés with a view — map of 12 popular view cafés, free PDF]({BASE + map_path(CF, "en")})
- [Da Lat BBQ restaurants — map of 9 popular grill spots, free PDF]({BASE + map_path(BB, "en")})
- [Da Lat 5-star hotels — map of 8 hotels and resorts listed as 5-star, free PDF]({BASE + map_path(HT, "en")})
- [Da Lat 4-star hotels — map of 10 popular 4-star hotels and resorts, free PDF]({BASE + map_path(H4, "en")})
- [Da Lat 3-star hotels — map of 8 popular 3-star hotels near the night market, free PDF]({BASE + map_path(H3, "en")})
- [Places to visit in Da Lat by motorbike — every sight from our maps grouped by direction, with distance, hours and electric-scooter suitability]({BASE + "places-to-visit-in-da-lat/"}) (Vietnamese: {BASE + "vi/dia-diem-du-lich-da-lat/"})
- [Da Lat tourist map by motorbike route — 6 loops from the shop with stops in riding order, distances, electric-scooter suitability and 1–4 day plans]({BASE + "da-lat-tourist-map/"}) (Vietnamese: {BASE + "vi/ban-do-du-lich-da-lat/"})
- [Da Lat day trip on your own by motorbike — self-guided versions of the popular 1-day group tours]({BASE + "da-lat-day-trip-by-motorbike/"}) (Vietnamese: {BASE + "vi/da-lat-1-ngay-tu-tuc/"})
- [Self-guided Da Lat day trip by motorbike: new attractions 2026 (Langbiang Land, Mongo Land, Hoang Long Ohayo, strawberry farm) — ordered route, distances, free PDF]({BASE + map_path(RN, "en")})
- [Self-guided Da Lat day trip by motorbike: hot check-in spots (Lac Hu Co Tran, Memory Station, Suoi Binh Yen, Happy Hill) — ordered route, distances, free PDF]({BASE + map_path(RC, "en")})
- [Da Lat waterfalls map — 6 waterfalls open to visitors (Datanla, Prenn, Cam Ly, Lien Khuong, Elephant Falls, Pongour) with hours, reference ticket prices, free PDF]({BASE + map_path(WF, "en")})
- [Self-guided attractions in Da Lat — 29 places from waterfalls and tea hills to pagodas and the night market, opening hours from Google Maps, reference ticket prices and directions]({BASE + map_path(AM, "en")})
- [Da Lat flower gardens — 9 gardens and flower fields with hours, reference ticket prices and directions]({BASE + map_path(FM, "en")})
- [Da Lat night-view cafés — map of 6 cafés overlooking the lit greenhouse valley (Chenh Venh, Chang Vang, Loi Cua Gio, Vi Yeu Ma Den, Lang Vu Thi, Nha May Cay), free PDF]({BASE + map_path(NC, "en")})
- [How to get from Nha Trang to Da Lat — bus & limousine map: Da Lat bus station and the Da Lat offices of FUTA, The Sinh Tourist, Lac Hong, An Phu, HM; free PDF]({BASE + map_path(NT, "en")})
- [Da Lat night market & evening food map — night market, grilled rice paper, hot soy milk, che, chicken hot pot with lemon basil; free PDF]({BASE + map_path(NM, "en")})
- [Da Lat to Saigon bus — map of the Da Lat bus station and 12 bus company offices, free PDF]({BASE + map_path(BU, "en")})
- [Da Lat to Da Nang bus — map of the Da Lat bus station and 6 bus company offices on the Da Nang / Hoi An route, free PDF]({BASE + map_path(DN, "en")})
- [Da Lat Flower Festival 2026 — planned 19–31 Dec 2026: programme, venue map, free PDF]({BASE + map_path(FE, "en")})
- [Do I need a license to rent a motorbike in Vietnam? Gas scooters need a valid motorbike license; electric scooters in the moped class (up to 50 km/h, motor up to 4 kW) need none]({BASE + lic_path("en")}) (Vietnamese: {BASE + lic_path("vi")})
- [Arriving in Da Lat early by night bus — overnight buses from Ho Chi Minh City usually arrive about 4–7 am; where they stop, getting to the centre, picking up a scooter from 4:30 am]({BASE + arr_path("en")}) (Vietnamese: {BASE + arr_path("vi")})
- [Motorbike routes around Da Lat]({BASE + routes_path("en")})
- [Travel blog]({BASE + blog_path("en")})
""" + "".join(f"- [{LABEL[x]} home]({BASE + home_path(x)})\n" for x in LANGS if x != "en")
LLMS += "\n## Quick answers\n" + "".join(f"- **{q}** {a.replace('see the map below', 'https://maps.app.goo.gl/ULvgaZFh4Q1kjTCe6')}\n" for q, a in C["en"]["home"]["faq"])
LLMS += "\n## Rental guides and articles (newest first; Vietnamese version in brackets)\n" + "".join(
    f"- [{C['en']['articles'][k][2]}]({BASE + art_path('en', k)}) ([VI: {C['vi']['articles'][k][2]}]({BASE + art_path('vi', k)}))\n"
    for k in ARTICLES[::-1] if k in C["en"]["articles"] and k in C["vi"]["articles"])
(OUT / "llms.txt").write_text(LLMS, encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
print("pages:", sum(1 for _ in OUT.rglob("index.html")))
