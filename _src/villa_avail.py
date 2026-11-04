"""Villa availability JSON for the villa page check box (owner asked 2026-11-04).

Reads the owner's booking calendar exported from Google Sheets (.xlsx, sheet "LỊCH DALAT FLUTE HOUSE",
one tab per month named MMYYYY / "MM/YYYY"; col A = date, col B = Flute House) and writes
/avail/<key>.json with ONLY a status letter per night — no guest names, no prices (owner: "không hiện giá").
  cell with letters (guest name, merged over several nights) = booked  -> "b"
  cell with only numbers (the price, e.g. 2300/2600)          = free    -> "f"
  empty cell / no row                                         = ask     -> (left out)

Usage: python3 _src/villa_avail.py <calendar.xlsx>
"""
import datetime as dt, json, pathlib, re, sys
import openpyxl

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOUSES = {"flute": 2}  # key -> column (B). Clip ids that use each key: content/villa.py CAL
LETTER = re.compile(r"[A-Za-zÀ-ỹĐđ]")


def read(xlsx):
    wb = openpyxl.load_workbook(xlsx)
    today = dt.date.today()
    out = {k: {} for k in HOUSES}
    for ws in wb.worksheets:
        if not re.fullmatch(r"\d{2}/?\d{4}", ws.title.strip()):
            continue
        for key, col in HOUSES.items():
            vals = {}
            for r in range(1, ws.max_row + 1):
                vals[r] = ws.cell(r, col).value
            for mr in ws.merged_cells.ranges:  # guest name merged over several nights
                if mr.min_col <= col <= mr.max_col:
                    top = ws.cell(mr.min_row, mr.min_col).value
                    for r in range(mr.min_row, mr.max_row + 1):
                        vals[r] = top
            for r in range(1, ws.max_row + 1):
                d = ws.cell(r, 1).value
                if isinstance(d, dt.datetime):
                    d = d.date()
                elif isinstance(d, str):
                    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", d.strip())
                    if not m:
                        continue
                    y = int(m[3]); y += 2000 if y < 100 else 0
                    d = dt.date(y, int(m[2]), int(m[1]))
                if not isinstance(d, dt.date) or d < today:
                    continue
                v = "" if vals[r] is None else str(vals[r]).strip()
                if not v:
                    continue
                out[key][d.isoformat()] = "b" if LETTER.search(v) else "f"
    return out


def main(xlsx):
    (ROOT / "avail").mkdir(exist_ok=True)
    for key, days in read(xlsx).items():
        data = {"updated": dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M"),
                "d": dict(sorted(days.items()))}
        p = ROOT / "avail" / f"{key}.json"
        p.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
        print(p.relative_to(ROOT), len(days), "nights",
              sum(v == "b" for v in days.values()), "booked")


if __name__ == "__main__":
    main(sys.argv[1])
