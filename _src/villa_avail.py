"""Villa availability JSON for the villa page check box (owner asked 2026-11-04 / 2026-11-05).

Reads the owners' booking calendars exported from Google Sheets (.xlsx) and writes /avail/<key>.json
with ONLY a status letter per night — no guest names, no prices (owner: "không hiện giá").
  "f" = free, "b" = booked, missing = not open yet (the page says "message us").

Calendars (Google Sheet file id -> layout):
  flute   "LỊCH DALAT FLUTE HOUSE"  18yl2K3Dbse2O31b1eYZ91Vfu3EfRJDTgsNKygRicb_U
          one tab per month (MMYYYY); col A = date, col B = Flute House.
          number (price, e.g. 2300/2600) = free; text (guest name, merged over nights) = booked.
  sonata  "SONATA VILLA ĐÀ LẠT"      1bi6Ork9Y9pG5l9VjXohb7w0nJPGz8xzvPrGxIfvi_64
          tab "<year>" (e.g. 2026); each month is a block of 3 columns Ngày | Thứ | Giá from row 11.
          number in Giá = free; empty Giá cell coloured (green/pink/yellow…) or text = booked.

Usage: python3 _src/villa_avail.py flute=<flute.xlsx> sonata=<sonata.xlsx>   (any subset)
Clip ids that use each key: content/villa.py CAL
"""
import datetime as dt, json, pathlib, re, sys
import openpyxl

ROOT = pathlib.Path(__file__).resolve().parent.parent
LETTER = re.compile(r"[A-Za-zÀ-ỹĐđ]")
WHITE = {None, "00000000", "FFFFFFFF"}


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str):
        m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", v.strip())
        if m:
            y = int(m[3]); y += 2000 if y < 100 else 0
            return dt.date(y, int(m[2]), int(m[1]))
    return None


def merged_map(ws):
    """(row, col) -> top-left cell of its merged range, so a merge counts on every night it covers."""
    out = {}
    for mr in ws.merged_cells.ranges:
        for r in range(mr.min_row, mr.max_row + 1):
            for c in range(mr.min_col, mr.max_col + 1):
                out[(r, c)] = ws.cell(mr.min_row, mr.min_col)
    return out


def fill_rgb(cell):
    try:
        if cell.fill is None or cell.fill.fill_type in (None, "none"):
            return None
        rgb = cell.fill.fgColor.rgb
        return rgb if isinstance(rgb, str) else None
    except Exception:
        return None


def read_flute(xlsx, today):
    wb, out = openpyxl.load_workbook(xlsx), {}
    for ws in wb.worksheets:
        if not re.fullmatch(r"\d{2}/?\d{4}", ws.title.strip()):
            continue
        mm = merged_map(ws)
        for r in range(1, ws.max_row + 1):
            d = as_date(ws.cell(r, 1).value)
            if not d or d < today:
                continue
            cell = mm.get((r, 2), ws.cell(r, 2))
            v = "" if cell.value is None else str(cell.value).strip()
            if v:
                out[d.isoformat()] = "b" if LETTER.search(v) else "f"
    return out


def read_sonata(xlsx, today):
    wb, out = openpyxl.load_workbook(xlsx), {}
    for ws in wb.worksheets:
        if not re.fullmatch(r"\d{4}", ws.title.strip()):
            continue
        mm = merged_map(ws)
        for c in range(1, ws.max_column + 1):
            if str(ws.cell(10, c).value or "").strip().lower() != "ngày":
                continue
            first = as_date(ws.cell(11, c).value)
            if not first:
                continue
            for r in range(11, ws.max_row + 1):
                d = as_date(ws.cell(r, c).value)
                if not d or d < today or d.month != first.month:  # skip the spill-over row of the next month
                    continue
                cell = mm.get((r, c + 2), ws.cell(r, c + 2))
                v = cell.value
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    out[d.isoformat()] = "f"
                elif v is not None and str(v).strip():
                    out[d.isoformat()] = "b" if LETTER.search(str(v)) else "f"
                elif fill_rgb(cell) not in WHITE:
                    out[d.isoformat()] = "b"
    return out


READERS = {"flute": read_flute, "sonata": read_sonata}


def main(args):
    today = dt.date.today()
    (ROOT / "avail").mkdir(exist_ok=True)
    jobs = dict(a.split("=", 1) for a in args) if args and "=" in args[0] else {"flute": args[0]}
    for key, path in jobs.items():
        days = READERS[key](path, today)
        data = {"updated": dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M"),
                "d": dict(sorted(days.items()))}
        p = ROOT / "avail" / f"{key}.json"
        p.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
        print(p.relative_to(ROOT), len(days), "nights", sum(v == "b" for v in days.values()), "booked")


if __name__ == "__main__":
    main(sys.argv[1:])
