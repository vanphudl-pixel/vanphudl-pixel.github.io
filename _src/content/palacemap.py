"""Da Lat palaces map (dinh thự) — website page, 6 focus languages (owner asked 2026-11-09; new content only in vi/en/zh/ru/ko/id).
Checked 2026-11-09. Coordinates and Google Maps place links from Google Maps, except Dinh 3: its Google listing pin sits ~1.7 km north
of the real palace, so it uses the Wikipedia coordinates (11.9302, 108.4297) and a Google Maps search link instead of the place link.
Status / prices (reference, change often):
- Madame de Dalat: official site madamededalat.vn (mansion 7:30–17:30 daily; mansion + woodblocks 178,000 / child 50,000; 50% off after 16:00). Google Maps lists Sunday closed.
- Dinh 3: ~60,000 adult / 40,000 child (lamdongtours 30/06/2026, hoadalattravel 01/09/2026); Google Maps 7:00–17:30.
- Dinh Tỉnh trưởng: old-Da-Lat memorabilia, no ticket (theleader 2022, mia); Google Maps Mon–Fri 8–11, 14–17; reviews: building sometimes shut.
- Dinh 2: recent Google reviews: closed to casual visitors, run as a guesthouse; lamdongtours 23/06/2026: not reliably open.
- Cung Nam Phương: in the Lâm Đồng Museum grounds, 4 Hùng Vương (baovanhoa 08/04/2026); Google Maps 7:30–11:30, 13:30–17:00.
- Dinh 1: closed 26/04/2024, reopened free 15/06/2026 (SGGP), gate closed on 17/08/2026 (lamdongtours); recent Google reviews: restored, ~50,000 entry / 150,000 with activities. Always "check before going".
No printable PDF yet (PDF = None hides the button)."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid / place_id / "q:<search>", ok on electric scooter, hours ("check" = status changes, ask first)
SPOTS = [
    ("madame",   11.9460096, 108.4258434, "ChIJ84s2rABtcTERcfxQq6Ao1lI", True, "7:30–17:30"),
    ("dinh3",    11.9302000, 108.4297000, "q:Dinh Bảo Đại 3, 1 Triệu Việt Vương, Đà Lạt", True, "7:00–17:30"),
    ("tinhtruong", 11.9456908, 108.4374190, "ChIJp5ez7ygTcTERPlx842OxG44", True, "8:00–11:00, 14:00–17:00"),
    ("dinh2",    11.9356230, 108.4479972, "ChIJq6rq4TwTcTERv-5xL1SCzxg", True, "check"),
    ("namphuong", 11.9399113, 108.4604752, "ChIJ6SkCmRsTcTERbHtqG1PO0Rc", True, "7:30–11:30, 13:30–17:00"),
    ("dinh1",    11.9443357, 108.4697101, "ChIJES1bgwETcTERmuKW99fNdIc", True, "check"),
]
CENTER = _PM.CENTER
SLUG = {"en": "dalat-palaces-map", "vi": "ban-do-cac-dinh-da-lat", "zh": "dalat-palaces-map", "ru": "karta-dvortsov-dalata",
        "ko": "dalat-palaces-map", "id": "peta-istana-dalat"}
PDF = None
GUIDES = {}
LANGS = ["vi", "en", "zh", "ru", "ko", "id"]
UPDATED = "2026-11-09"
NCENTER = 6
SHOP_DY = -30
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]
CHECK = {"vi": "trạng thái hay thay đổi — gọi hỏi trước khi đi", "en": "status changes — check before you go",
         "zh": "开放情况常变——出发前请先确认", "ru": "режим меняется — уточните перед поездкой",
         "ko": "운영 여부가 자주 바뀜 — 가기 전에 확인", "id": "status sering berubah — tanyakan dulu sebelum pergi"}

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["vi"] = _mk("Bản đồ các dinh Đà Lạt: Dinh 1, 2, 3 và các biệt điện (2026) | Văn Phú", "Bản đồ các dinh Đà Lạt",
 "Bản đồ 6 dinh thự Đà Lạt: Dinh 1, Dinh 2, Dinh 3, Dinh Tỉnh trưởng, Cung Nam Phương Hoàng hậu, biệt điện Trần Lệ Xuân — dinh nào đang mở, giờ mở cửa, giá vé tham khảo và chỉ đường.",
 "6 dinh thự nổi tiếng của Đà Lạt, từ Dinh 3 của vua Bảo Đại đến Cung Nam Phương Hoàng hậu và biệt điện Trần Lệ Xuân. Mỗi dinh có ghi rõ đang mở hay không, giờ mở cửa, giá vé tham khảo và nút chỉ đường. Tất cả cách hồ Xuân Hương dưới 4 km, đi xe máy điện được.",
 "Các dinh Đà Lạt (1–6)", "Nên đi lúc nào",
 [("Buổi sáng 8:00–10:00", "ít khách, ánh sáng đẹp để chụp mặt tiền"), ("Ngày thường", "vắng hơn hẳn cuối tuần và dịp lễ"), ("Trời nắng", "đi Dinh 3 và Cung Nam Phương, vườn đẹp và view hồ rõ")],
 "Lưu ý",
 ["Giá vé là giá tham khảo (cập nhật 11/2026), có thể đổi — hỏi lại tại quầy.",
  "Dinh 1 và Dinh 2 hay đóng mở thất thường: Dinh 1 mở lại tháng 6/2026 rồi lại đóng cổng tháng 8/2026; Dinh 2 hiện chủ yếu làm nhà nghỉ. Gọi hỏi trước, đừng xếp làm điểm chính.",
  "Cung Nam Phương nghỉ trưa 11:30–13:30 và phải cởi giày khi vào nhà.",
  "Lộ trình gợi ý nửa ngày: Madame de Dalat → Dinh 3 → Dinh Tỉnh trưởng → Cung Nam Phương (khoảng 8 km).",
  "Vào trong dinh nên ăn mặc lịch sự, không chạm vào đồ trưng bày."],
 [("Madame de Dalat (biệt điện Trần Lệ Xuân)", "Buổi sáng", "Biệt điện xây năm 1958, nay là bảo tàng và khu vườn: chuyện áo dài, mộc bản triều Nguyễn, vườn hồng. Vé dinh + mộc bản 178.000 VND (trẻ em 50.000), giảm 50% sau 16:00 theo website chính thức; Google Maps ghi nghỉ Chủ nhật — hỏi trước."),
  ("Dinh 3 (Dinh Bảo Đại)", "8:00–10:00", "Dinh nghỉ dưỡng của vua Bảo Đại và gia đình, xây 1933–1938 trên đồi thông. Còn phòng làm việc, phòng ngủ, đồ nội thất xưa. Vé tham khảo 60.000 VND (trẻ em 40.000). Dinh được tham quan nhiều nhất."),
  ("Dinh Tỉnh trưởng", "Buổi sáng ngày thường", "Dinh thời Pháp (đầu thế kỷ 20) trên đồi Dinh ngay trung tâm, có không gian trưng bày kỷ vật Đà Lạt xưa, không bán vé. Có lúc chỉ xem được khuôn viên bên ngoài; cuối tuần đóng cửa."),
  ("Dinh 2 (Dinh Toàn quyền Decoux)", "Ngắm bên ngoài", "Dinh của Toàn quyền Đông Dương trên đường Trần Hưng Đạo. Khách gần đây cho biết dinh không mở cho khách vãng lai, đang dùng làm nhà nghỉ — gọi hỏi trước."),
  ("Cung Nam Phương Hoàng hậu", "Buổi sáng", "Dinh Nguyễn Hữu Hào phong cách Art Deco (thập niên 1930), của hồi môn của Hoàng hậu Nam Phương; nằm trong khuôn viên Bảo tàng Lâm Đồng, 4 Hùng Vương. Có 9 lò sưởi, view nhìn xuống thành phố. Vé rẻ, cởi giày khi vào."),
  ("Dinh 1 (Dinh Bảo Đại 1)", "Gọi hỏi trước", "Dinh trên đồi phía đông, từng là nơi làm việc của vua Bảo Đại. Đóng cửa từ 4/2024, mở lại miễn phí 15/6/2026 nhưng đến 17/8/2026 cổng lại đóng. Đánh giá Google gần đây có nói vé 50.000 VND (150.000 kèm trò chơi) — hỏi trước khi đến.")])

T["en"] = _mk("Da Lat Palaces Map: Bao Dai Palaces 1, 2, 3 & More (2026) | Van Phu", "Da Lat Palaces Map",
 "Map of 6 palaces and villas in Da Lat — Bao Dai Palaces 1, 2 and 3, the Governor's Palace, Empress Nam Phuong's Palace and Madame de Dalat — which ones are open, hours, reference ticket prices and directions.",
 "Six historic palaces in Da Lat, from Emperor Bao Dai's Palace 3 to Empress Nam Phuong's Palace and the Madame de Dalat villa — with what is open right now, opening hours, reference ticket prices and one-tap directions. All within 4 km of Xuan Huong Lake, easy on an electric scooter.",
 "Da Lat palaces (1–6)", "When to go",
 [("Morning, 8:00–10:00", "fewer visitors and soft light on the façades"), ("Weekdays", "much quieter than weekends and holidays"), ("Sunny days", "Palace 3 and Nam Phuong's Palace have the best gardens and lake views")],
 "Good to know",
 ["Ticket prices are reference prices (Nov 2026) and change often — check at the gate.",
  "Palaces 1 and 2 open and close without notice: Palace 1 reopened in June 2026, then its gate was closed again in August 2026; Palace 2 is now mostly a guesthouse. Ask first and don't plan your day around them.",
  "Nam Phuong's Palace closes for lunch 11:30–13:30, and shoes come off at the door.",
  "Half-day route: Madame de Dalat → Palace 3 → Governor's Palace → Nam Phuong's Palace (about 8 km).",
  "Dress neatly inside and don't touch the displays."],
 [("Madame de Dalat (Tran Le Xuan villa)", "Morning", "Villa built in 1958, now a museum and garden: the story of the áo dài, Nguyen dynasty woodblocks and a rose garden. Villa + woodblocks 178,000 VND (child 50,000), 50% off after 16:00 per the official site; Google Maps shows Sundays closed — check first."),
  ("Bao Dai Palace 3 (Summer Palace)", "8:00–10:00", "Emperor Bao Dai's family residence, built 1933–1938 on a pine hill, with his office, bedrooms and original furniture. Reference ticket 60,000 VND (child 40,000). The most visited palace."),
  ("Governor's Palace (Dinh Tinh Truong)", "Weekday morning", "French-era residence (early 20th century) on Palace Hill in the centre, with a free exhibition of old Da Lat memorabilia. Sometimes only the grounds are open; closed at weekends."),
  ("Bao Dai Palace 2 (Decoux Palace)", "View from outside", "Residence of the Governor-General of Indochina on Tran Hung Dao Street. Recent visitors say it is closed to casual visitors and runs as a guesthouse — check first."),
  ("Empress Nam Phuong's Palace", "Morning", "Art Deco villa from the 1930s, the Nguyen Huu Hao palace given as Empress Nam Phuong's dowry; in the Lam Dong Museum grounds, 4 Hung Vuong. Nine fireplaces and a view over the city. Cheap ticket; shoes off inside."),
  ("Bao Dai Palace 1", "Check first", "Hilltop palace in the east of town, once Bao Dai's working residence. Closed from April 2024, reopened free on 15 June 2026, but the gate was closed again on 17 August 2026. Recent Google reviews mention 50,000 VND entry (150,000 with activities) — ask before you go.")])

T["zh"] = _mk("大叻宫殿地图：保大一号、二号、三号行宫等6处（2026） | Van Phu", "大叻宫殿地图",
 "大叻6处宫殿与别墅地图——保大一号、二号、三号行宫，省长府，南芳皇后宫，陈丽春别墅（Madame de Dalat）——哪些在开放、开放时间、参考票价和导航。",
 "大叻最有名的6处宫殿，从保大皇帝的三号行宫到南芳皇后宫和陈丽春别墅。每处都写明目前是否开放、开放时间、参考票价，并可一键导航。全部距春香湖4公里以内，骑电动车很方便。",
 "大叻宫殿（1–6）", "什么时候去",
 [("上午 8:00–10:00", "游客少，正面拍照光线好"), ("工作日", "比周末和节假日安静得多"), ("晴天", "三号行宫和南芳皇后宫花园漂亮，湖景清楚")],
 "注意事项",
 ["票价为参考价（2026年11月），经常变动——请以售票处为准。",
  "一号、二号行宫开放情况不稳定：一号行宫2026年6月重新开放，8月又关门；二号行宫现在主要作为旅馆。请先询问，不要当作主要景点。",
  "南芳皇后宫午休 11:30–13:30，进屋要脱鞋。",
  "半日路线：陈丽春别墅 → 三号行宫 → 省长府 → 南芳皇后宫（约8公里）。",
  "参观室内请穿着得体，不要触摸展品。"],
 [("陈丽春别墅（Madame de Dalat）", "上午", "1958年建成的别墅，现为博物馆和花园：奥黛的故事、阮朝木刻版、玫瑰园。官网票价：别墅+木刻版 178,000越南盾（儿童50,000），16:00后半价；谷歌地图显示周日休息——请先确认。"),
  ("保大三号行宫（夏宫）", "8:00–10:00", "保大皇帝一家的住所，1933–1938年建在松林山丘上，保留书房、卧室和老家具。参考票价60,000越南盾（儿童40,000）。游客最多的一处。"),
  ("省长府（Dinh Tỉnh trưởng）", "工作日上午", "法国时期（20世纪初）的府邸，位于市中心的府邸山上，有免费的老大叻纪念品展览。有时只能看外面的院子；周末不开放。"),
  ("保大二号行宫（德古总督府）", "外观参观", "法属印度支那总督的府邸，在陈兴道路。最近的游客说不对散客开放，现作为旅馆经营——请先确认。"),
  ("南芳皇后宫", "上午", "1930年代装饰艺术风格的阮有豪别墅，是南芳皇后的嫁妆；位于林同博物馆园区内（雄王路4号）。有9座壁炉，可俯瞰市区。门票便宜，进屋脱鞋。"),
  ("保大一号行宫", "请先确认", "城东山丘上的宫殿，曾是保大皇帝办公的地方。2024年4月关闭，2026年6月15日免费重新开放，但8月17日大门又关闭。最近的谷歌评价提到门票50,000越南盾（含活动150,000）——出发前请先询问。")])

T["ru"] = _mk("Карта дворцов Далата: дворцы Бао Дая 1, 2, 3 и другие (2026) | Van Phu", "Карта дворцов Далата",
 "Карта 6 дворцов и вилл Далата — дворцы Бао Дая 1, 2 и 3, дворец губернатора, дворец императрицы Нам Фыонг и Madame de Dalat — что открыто, часы работы, ориентировочные цены и маршрут.",
 "Шесть исторических дворцов Далата: от летнего дворца императора Бао Дая до дворца императрицы Нам Фыонг и виллы Madame de Dalat. Для каждого — открыт ли он сейчас, часы работы, ориентировочная цена билета и маршрут в одно касание. Все в пределах 4 км от озера Сюанхыонг, легко доехать на электроскутере.",
 "Дворцы Далата (1–6)", "Когда ехать",
 [("Утро, 8:00–10:00", "меньше людей, мягкий свет на фасадах"), ("Будни", "намного спокойнее, чем выходные и праздники"), ("Солнечный день", "у дворца 3 и дворца Нам Фыонг лучшие сады и виды на озеро")],
 "Полезно знать",
 ["Цены ориентировочные (ноябрь 2026) и часто меняются — уточняйте на кассе.",
  "Дворцы 1 и 2 открываются и закрываются без предупреждения: дворец 1 снова открыли в июне 2026, а в августе 2026 ворота опять закрыли; дворец 2 сейчас в основном работает как гостевой дом. Спросите заранее и не стройте день вокруг них.",
  "Дворец Нам Фыонг закрыт на обед 11:30–13:30, в доме нужно снять обувь.",
  "Маршрут на полдня: Madame de Dalat → дворец 3 → дворец губернатора → дворец Нам Фыонг (около 8 км).",
  "Внутри одевайтесь опрятно и не трогайте экспонаты."],
 [("Madame de Dalat (вилла Чан Ле Суан)", "Утро", "Вилла 1958 года, сейчас музей и сад: история аозай, ксилографии династии Нгуен, розарий. Вилла + ксилографии 178 000 VND (детский 50 000), после 16:00 скидка 50% по данным официального сайта; в Google Maps воскресенье указано выходным — уточните."),
  ("Дворец Бао Дая 3 (летний дворец)", "8:00–10:00", "Резиденция семьи императора Бао Дая, построена в 1933–1938 годах на сосновом холме: кабинет, спальни, старинная мебель. Ориентировочно 60 000 VND (детский 40 000). Самый посещаемый дворец."),
  ("Дворец губернатора (Dinh Tỉnh trưởng)", "Утро в будни", "Особняк французской эпохи (начало XX века) на Дворцовом холме в центре, бесплатная выставка вещей старого Далата. Иногда открыта только территория; в выходные закрыто."),
  ("Дворец Бао Дая 2 (дворец Деку)", "Смотреть снаружи", "Резиденция генерал-губернатора Индокитая на улице Чан Хынг Дао. Недавние гости пишут, что для обычных посетителей он закрыт и работает как гостевой дом — уточните заранее."),
  ("Дворец императрицы Нам Фыонг", "Утро", "Вилла в стиле ар-деко 1930-х годов (дворец Нгуен Хыу Хао), приданое императрицы Нам Фыонг; на территории музея Ламдонга, ул. Хунгвыонг, 4. Девять каминов, вид на город. Билет недорогой, обувь снимают у входа."),
  ("Дворец Бао Дая 1", "Уточните заранее", "Дворец на холме на востоке города, где работал Бао Дай. Закрыт с апреля 2024, бесплатно открыт 15 июня 2026, но 17 августа 2026 ворота снова были закрыты. В свежих отзывах Google — вход 50 000 VND (150 000 с развлечениями). Спросите перед поездкой.")])

T["ko"] = _mk("달랏 궁전 지도: 바오다이 1·2·3궁 등 6곳 (2026) | Van Phu", "달랏 궁전 지도",
 "달랏 궁전·빌라 6곳 지도 — 바오다이 1·2·3궁, 성장 관저, 남프엉 황후궁, 마담 드 달랏 — 지금 열려 있는 곳, 운영 시간, 참고 입장료, 길찾기.",
 "바오다이 황제의 3궁부터 남프엉 황후궁, 마담 드 달랏 빌라까지 달랏의 대표 궁전 6곳. 현재 개방 여부, 운영 시간, 참고 입장료와 원터치 길찾기를 정리했습니다. 모두 쑤언흐엉 호수에서 4km 이내라 전기 스쿠터로 다니기 좋습니다.",
 "달랏 궁전 (1–6)", "언제 가면 좋을까",
 [("오전 8:00–10:00", "사람이 적고 정면 사진 빛이 좋음"), ("평일", "주말·연휴보다 훨씬 한산"), ("맑은 날", "3궁과 남프엉 황후궁은 정원과 호수 전망이 좋음")],
 "알아두세요",
 ["입장료는 참고 가격(2026년 11월)이며 자주 바뀝니다 — 매표소에서 확인하세요.",
  "1궁과 2궁은 예고 없이 열고 닫습니다: 1궁은 2026년 6월 재개방 후 8월에 다시 문을 닫았고, 2궁은 지금 주로 숙소로 운영됩니다. 먼저 확인하고 메인 일정으로 잡지 마세요.",
  "남프엉 황후궁은 점심시간 11:30–13:30 휴관, 실내는 신발을 벗고 들어갑니다.",
  "반나절 코스: 마담 드 달랏 → 3궁 → 성장 관저 → 남프엉 황후궁 (약 8km).",
  "실내에서는 단정한 복장, 전시품은 만지지 마세요."],
 [("마담 드 달랏 (쩐레쑤언 빌라)", "오전", "1958년에 지은 빌라로 지금은 박물관과 정원: 아오자이 이야기, 응우옌 왕조 목판, 장미 정원. 공식 사이트 기준 빌라+목판 178,000동(어린이 50,000), 16시 이후 50% 할인. 구글 지도에는 일요일 휴무로 나와 있어 확인 필요."),
  ("바오다이 3궁 (여름 궁전)", "8:00–10:00", "바오다이 황제 가족의 거처로 1933–1938년 소나무 언덕에 지어졌고, 집무실·침실·옛 가구가 남아 있습니다. 참고 입장료 60,000동(어린이 40,000). 가장 많이 찾는 궁전."),
  ("성장 관저 (Dinh Tỉnh trưởng)", "평일 오전", "시내 중심 언덕 위 프랑스 시대(20세기 초) 관저로, 옛 달랏 물건을 무료로 전시합니다. 가끔 바깥 정원만 볼 수 있고 주말은 휴관."),
  ("바오다이 2궁 (드쿠 총독 관저)", "외관 관람", "쩐흥다오 거리의 인도차이나 총독 관저. 최근 방문객에 따르면 일반 관람객에게 개방하지 않고 숙소로 운영 중 — 먼저 확인하세요."),
  ("남프엉 황후궁", "오전", "1930년대 아르데코 양식의 응우옌흐우하오 저택으로 남프엉 황후의 혼수였습니다. 럼동 박물관 부지 안(훙브엉 4번지). 벽난로 9개와 시내 전망. 입장료 저렴, 실내는 신발을 벗습니다."),
  ("바오다이 1궁", "먼저 확인", "시 동쪽 언덕의 궁전으로 바오다이가 집무하던 곳. 2024년 4월 폐쇄, 2026년 6월 15일 무료 재개방했지만 8월 17일 다시 문이 닫혀 있었습니다. 최근 구글 리뷰에는 입장 50,000동(체험 포함 150,000) — 가기 전에 문의하세요.")])

T["id"] = _mk("Peta Istana Da Lat: Istana Bao Dai 1, 2, 3 dan Lainnya (2026) | Van Phu", "Peta Istana Da Lat",
 "Peta 6 istana dan vila di Da Lat — Istana Bao Dai 1, 2 dan 3, Istana Gubernur, Istana Permaisuri Nam Phuong dan Madame de Dalat — mana yang buka, jam buka, harga tiket acuan dan petunjuk arah.",
 "Enam istana bersejarah di Da Lat, dari Istana 3 milik Kaisar Bao Dai sampai Istana Permaisuri Nam Phuong dan vila Madame de Dalat — lengkap dengan status buka, jam buka, harga tiket acuan dan petunjuk arah sekali ketuk. Semuanya dalam 4 km dari Danau Xuan Huong, mudah dicapai dengan skuter listrik.",
 "Istana di Da Lat (1–6)", "Kapan sebaiknya datang",
 [("Pagi, 8:00–10:00", "lebih sepi dan cahaya bagus untuk foto bagian depan"), ("Hari kerja", "jauh lebih sepi daripada akhir pekan dan hari libur"), ("Hari cerah", "Istana 3 dan Istana Nam Phuong punya taman dan pemandangan danau terbaik")],
 "Perlu diketahui",
 ["Harga tiket adalah harga acuan (Nov 2026) dan sering berubah — cek di loket.",
  "Istana 1 dan 2 buka-tutup tanpa pemberitahuan: Istana 1 dibuka lagi Juni 2026, lalu gerbangnya ditutup lagi Agustus 2026; Istana 2 kini lebih banyak dipakai sebagai penginapan. Tanyakan dulu dan jangan jadikan tujuan utama.",
  "Istana Nam Phuong tutup istirahat siang 11:30–13:30, dan alas kaki dilepas di dalam rumah.",
  "Rute setengah hari: Madame de Dalat → Istana 3 → Istana Gubernur → Istana Nam Phuong (sekitar 8 km).",
  "Berpakaian sopan di dalam dan jangan menyentuh barang pajangan."],
 [("Madame de Dalat (vila Tran Le Xuan)", "Pagi", "Vila tahun 1958, kini museum dan taman: kisah áo dài, cetakan kayu Dinasti Nguyen dan taman mawar. Vila + cetakan kayu 178.000 VND (anak 50.000), diskon 50% setelah pukul 16:00 menurut situs resmi; Google Maps mencantumkan Minggu tutup — tanyakan dulu."),
  ("Istana Bao Dai 3 (Istana Musim Panas)", "8:00–10:00", "Kediaman keluarga Kaisar Bao Dai, dibangun 1933–1938 di bukit pinus, dengan ruang kerja, kamar tidur dan perabot asli. Tiket acuan 60.000 VND (anak 40.000). Istana yang paling banyak dikunjungi."),
  ("Istana Gubernur (Dinh Tinh Truong)", "Pagi hari kerja", "Rumah dinas era Prancis (awal abad ke-20) di Bukit Istana di pusat kota, dengan pameran gratis barang-barang Da Lat tempo dulu. Kadang hanya halamannya yang bisa dikunjungi; tutup akhir pekan."),
  ("Istana Bao Dai 2 (Istana Decoux)", "Lihat dari luar", "Kediaman Gubernur Jenderal Indochina di Jalan Tran Hung Dao. Pengunjung baru-baru ini menyebut istana ini tidak dibuka untuk umum dan dipakai sebagai penginapan — tanyakan dulu."),
  ("Istana Permaisuri Nam Phuong", "Pagi", "Vila Art Deco tahun 1930-an (istana Nguyen Huu Hao), mas kawin Permaisuri Nam Phuong; di area Museum Lam Dong, Jl. Hung Vuong 4. Ada sembilan perapian dan pemandangan kota. Tiket murah; lepas alas kaki di dalam."),
  ("Istana Bao Dai 1", "Tanyakan dulu", "Istana di bukit sisi timur kota, dulu tempat Bao Dai bekerja. Ditutup sejak April 2024, dibuka gratis 15 Juni 2026, tetapi gerbangnya kembali tertutup pada 17 Agustus 2026. Ulasan Google terbaru menyebut tiket masuk 50.000 VND (150.000 dengan aktivitas) — tanyakan sebelum datang.")])

for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    T[_l]["h"] = dict(_PM.T[_l]["h"], check=CHECK[_l])
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_VI = {"madame": "Madame de Dalat biệt điện Trần Lệ Xuân", "dinh3": "Dinh Bảo Đại 3", "tinhtruong": "Dinh Tỉnh trưởng",
       "dinh2": "Dinh 2 Trần Hưng Đạo", "namphuong": "Cung Nam Phương Hoàng hậu", "dinh1": "Dinh 1 Bảo Đại"}
def img_link(sid):
    """Temporary photo link: Google Images search for the Vietnamese place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_VI[sid] + " Đà Lạt")
