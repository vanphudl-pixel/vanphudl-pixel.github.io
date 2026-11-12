"""Da Lat 5-star hotels and resorts map — shared data for the website page (/5-star-hotels-map/) and the printable PDF.
Hotels listed as 5-star by at least two Vietnamese travel sources (huongtientourist.com, tourdalattravel.com, Oct 2026);
coordinates and place links (cid) taken from Google Maps on 2026-10-14. Shared labels are reused from the photo-spot map."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (reception)
SPOTS = [
    ("dalatpalace", 11.9376173, 108.4403766, "13632160291114083599", True,  "24h"),
    ("merperle",    11.9411183, 108.4583036, "2925261577989617457",  True,  "24h"),
    ("imperial",    11.9501990, 108.4682005, "5363271250171583556",  True,  "24h"),
    ("anamandara",  11.9440390, 108.4236000, "7753107310771550007",  True,  "24h"),
    ("ladalat",     11.9775949, 108.4510083, "16255844529555003648", True,  "24h"),
    ("swissbel",    11.8824243, 108.4518585, "16734836393639663936", False, "24h"),
    ("edensee",     11.8868268, 108.4235015, "1812293315912519369",  False, "24h"),
    ("teaprenn",    11.8727353, 108.4684633, "13641964310801899366", False, "24h"),
]
CENTER = _PM.CENTER
SLUG = "5-star-hotels-map"
PDF = "VanPhu-Dalat-5-Star-Hotels-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 5
LEGW = 330
MAPH = 560
H1PT = 22
MAXKM = 9.0
RINGS = (2, 5, 8)
SIDE = {}
JITTER = {"swissbel": (0, -26), "teaprenn": (6, 8)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("5-Star Hotels in Da Lat: Map of 8 Hotels & Resorts | Van Phu", "Da Lat 5-Star Hotels Map",
 "Map of 8 hotels and resorts listed as 5-star in Da Lat — from the 1922 Dalat Palace to the Tuyen Lam Lake resorts — with directions, distances and a free PDF.",
 "Staying in style? Here are 8 hotels and resorts listed as 5-star in Da Lat — five in town and three by Tuyen Lam Lake and Prenn Pass — with one-tap directions and how far each is by scooter.",
 "In town (1–5)", "Good to know",
 [("Delivery", "we bring the scooter to your hotel in the city centre for rentals of 2 days or more"), ("Lake resorts (6–8)", "20–30 minutes from town on hilly roads — an Air Blade 125cc is the better choice"), ("Deposit", "passport or ID card, no cash deposit"), ("Return", "bring the scooter back by 21:00")],
 "Tips",
 ["Ask reception where to park the scooter safely.", "Roads around Tuyen Lam Lake are dark at night — ride back before dark.", "Some lake resorts run a shuttle to town; a scooter lets you explore in between.", "Star ratings and prices change — check with the hotel when you book."],
 [("Dalat Palace Heritage Hotel", "Afternoon", "Grand French-era hotel from 1922 above Xuan Huong Lake."),
  ("MerPerle Dalat Hotel", "Any time", "Palace-style hotel on Hung Vuong Street with a heated indoor pool."),
  ("Best Western Premier Imperial Dalat", "Any time", "Newest 5-star in town, opened in 2025 on Hung Vuong Street."),
  ("Ana Mandara Villas Dalat", "Morning", "Restored French colonial villas on a quiet pine hillside."),
  ("Ladalat Hotel", "Any time", "Large hotel on Mai Anh Dao Street, near the Valley of Love."),
  ("Swiss-Belresort Tuyen Lam", "Morning", "Hillside resort next to a golf course with mountain views."),
  ("Dalat Edensee Lake Resort & Spa", "Morning", "Lakeside resort in the pine forest of Tuyen Lam Lake."),
  ("Tea Resort Prenn", "Daytime", "Large resort at the foot of Prenn Pass, beside Prenn Waterfall.")])
T["vi"] = _mk("Khách sạn 5 sao Đà Lạt: bản đồ 8 khách sạn và resort | Văn Phú", "Bản đồ khách sạn 5 sao Đà Lạt",
 "Bản đồ 8 khách sạn và resort được xếp hạng 5 sao ở Đà Lạt — từ Dalat Palace xây năm 1922 đến các resort hồ Tuyền Lâm — có chỉ đường, khoảng cách và PDF miễn phí.",
 "Đây là 8 khách sạn và resort được xếp hạng 5 sao ở Đà Lạt — 5 nơi trong thành phố và 3 nơi ở hồ Tuyền Lâm, đèo Prenn — có nút chỉ đường và khoảng cách đi xe máy.",
 "Trong thành phố (1–5)", "Nên biết",
 [("Giao xe", "giao xe tận khách sạn trong trung tâm khi thuê từ 2 ngày"), ("Resort ven hồ (6–8)", "cách phố 20–30 phút, đường dốc — nên đi Air Blade 125cc"), ("Đặt cọc", "giữ hộ chiếu hoặc CCCD, không cọc tiền"), ("Trả xe", "trả xe trước 21:00")],
 "Lưu ý",
 ["Hỏi lễ tân chỗ để xe an toàn.", "Đường quanh hồ Tuyền Lâm tối vào ban đêm — nên về trước khi trời tối.", "Một số resort ven hồ có xe đưa đón vào phố; có xe máy thì đi chơi chủ động hơn.", "Hạng sao và giá phòng có thể thay đổi — hỏi khách sạn khi đặt phòng."],
 [("Dalat Palace Heritage Hotel", "Buổi chiều", "Khách sạn cổ thời Pháp xây năm 1922, nhìn ra hồ Xuân Hương."),
  ("MerPerle Dalat Hotel", "Cả ngày", "Khách sạn kiểu cung điện trên đường Hùng Vương, có hồ bơi nước ấm trong nhà."),
  ("Best Western Premier Imperial Dalat", "Cả ngày", "Khách sạn 5 sao mới nhất, khai trương năm 2025 trên đường Hùng Vương."),
  ("Ana Mandara Villas Dalat", "Buổi sáng", "Quần thể biệt thự Pháp cổ được phục dựng trên đồi thông yên tĩnh."),
  ("Ladalat Hotel", "Cả ngày", "Khách sạn lớn trên đường Mai Anh Đào, gần Thung lũng Tình yêu."),
  ("Swiss-Belresort Tuyền Lâm", "Buổi sáng", "Resort trên đồi cạnh sân golf, view núi."),
  ("Dalat Edensee Lake Resort & Spa", "Buổi sáng", "Resort ven hồ giữa rừng thông Tuyền Lâm."),
  ("Tea Resort Prenn", "Ban ngày", "Resort rộng dưới chân đèo Prenn, cạnh thác Prenn.")])
T["ru"] = _mk("Отели 5 звёзд в Далате: карта 8 отелей и курортов | Van Phu", "Карта отелей 5 звёзд Далата",
 "Карта 8 отелей и курортов Далата категории 5 звёзд — от Dalat Palace 1922 года до курортов на озере Туйенлам — с маршрутом, расстоянием и бесплатным PDF.",
 "Здесь 8 отелей и курортов Далата категории 5 звёзд — пять в городе и три у озера Туйенлам и перевала Пренн — с маршрутом в одно касание и расстоянием на байке.",
 "В городе (1–5)", "Полезно знать",
 [("Доставка", "привезём байк к вашему отелю в центре при аренде от 2 дней"), ("Курорты у озера (6–8)", "20–30 минут от города по холмам — лучше взять Air Blade 125cc"), ("Залог", "паспорт или ID-карта, без денежного залога"), ("Возврат", "верните байк до 21:00")],
 "Советы",
 ["Спросите на ресепшене, где безопасно оставить байк.", "Дороги вокруг озера Туйенлам ночью тёмные — возвращайтесь до темноты.", "У некоторых курортов есть шаттл в город; на байке можно ездить куда угодно между рейсами.", "Категория и цены меняются — уточняйте в отеле при бронировании."],
 [("Dalat Palace Heritage Hotel", "Днём", "Старинный отель французской эпохи 1922 года над озером Суанхыонг."),
  ("MerPerle Dalat Hotel", "В любое время", "Отель в дворцовом стиле на улице Хунгвыонг с крытым подогреваемым бассейном."),
  ("Best Western Premier Imperial Dalat", "В любое время", "Самый новый 5-звёздочный отель, открыт в 2025 году на улице Хунгвыонг."),
  ("Ana Mandara Villas Dalat", "Утром", "Отреставрированные французские виллы на тихом сосновом холме."),
  ("Ladalat Hotel", "В любое время", "Большой отель на улице Майаньдао, рядом с Долиной любви."),
  ("Swiss-Belresort Tuyen Lam", "Утром", "Курорт на холме рядом с гольф-полем, вид на горы."),
  ("Dalat Edensee Lake Resort & Spa", "Утром", "Курорт на берегу озера Туйенлам в сосновом лесу."),
  ("Tea Resort Prenn", "Днём", "Большой курорт у подножия перевала Пренн, рядом с водопадом Пренн.")])
T["zh"] = _mk("大叻五星级酒店：8 家酒店与度假村地图 | Van Phu", "大叻五星级酒店地图",
 "大叻 8 家五星级酒店与度假村地图——从 1922 年的大叻皇宫酒店到宣林湖度假村——附导航、距离和免费 PDF。",
 "这里是大叻 8 家五星级酒店与度假村：市区 5 家，宣林湖和 Prenn 山口 3 家，一键导航，并标出骑摩托车的距离。",
 "市区（1–5）", "须知",
 [("送车", "租 2 天及以上，可把车送到市中心酒店"), ("湖边度假村（6–8）", "距市区 20–30 分钟，坡路多——建议骑 Air Blade 125cc"), ("押金", "押护照或身份证，不收现金押金"), ("还车", "21:00 前还车")],
 "提示",
 ["向前台询问安全的停车位置。", "宣林湖周边道路夜间很暗——请在天黑前返回。", "部分湖边度假村有进城班车；有摩托车出行更自由。", "星级和房价可能变化——订房时请向酒店确认。"],
 [("Dalat Palace Heritage Hotel", "下午", "1922 年的法式古典酒店，俯瞰春香湖。"),
  ("MerPerle Dalat Hotel", "全天", "雄王路上的宫殿风格酒店，有室内恒温泳池。"),
  ("Best Western Premier Imperial Dalat", "全天", "最新的五星级酒店，2025 年在雄王路开业。"),
  ("Ana Mandara Villas Dalat", "上午", "修复的法式殖民别墅群，位于安静的松林山坡。"),
  ("Ladalat Hotel", "全天", "梅英桃路上的大型酒店，靠近爱情谷。"),
  ("Swiss-Belresort Tuyen Lam", "上午", "山坡上的度假村，紧邻高尔夫球场，可看山景。"),
  ("Dalat Edensee Lake Resort & Spa", "上午", "宣林湖畔松林中的度假村。"),
  ("Tea Resort Prenn", "白天", "Prenn 山口脚下的大型度假村，紧邻 Prenn 瀑布。")])
T["ko"] = _mk("달랏 5성급 호텔: 호텔·리조트 8곳 지도 | Van Phu", "달랏 5성급 호텔 지도",
 "달랏의 5성급 호텔·리조트 8곳 지도 — 1922년 달랏 팰리스부터 뚜엔럼 호수 리조트까지 — 길찾기, 거리, 무료 PDF.",
 "달랏의 5성급 호텔·리조트 8곳입니다. 시내 5곳, 뚜엔럼 호수와 쁘렌 고개 3곳 — 원터치 길찾기와 오토바이 거리를 함께 표시했습니다.",
 "시내 (1–5)", "알아두세요",
 [("배달", "2일 이상 대여 시 시내 중심 호텔로 오토바이를 가져다 드립니다"), ("호수 리조트 (6–8)", "시내에서 20–30분, 언덕길 — Air Blade 125cc 추천"), ("보증", "여권 또는 신분증, 현금 보증금 없음"), ("반납", "21:00까지 반납")],
 "팁",
 ["오토바이를 안전하게 세울 곳을 리셉션에 물어보세요.", "뚜엔럼 호수 주변 도로는 밤에 어둡습니다 — 해 지기 전에 돌아오세요.", "일부 호수 리조트는 시내 셔틀이 있지만, 오토바이가 있으면 더 자유롭게 다닐 수 있어요.", "등급과 요금은 바뀔 수 있으니 예약 시 호텔에 확인하세요."],
 [("Dalat Palace Heritage Hotel", "오후", "쑤언흐엉 호수를 내려다보는 1922년 프랑스 시대 호텔."),
  ("MerPerle Dalat Hotel", "언제든", "훙브엉 거리의 궁전 스타일 호텔, 실내 온수 수영장."),
  ("Best Western Premier Imperial Dalat", "언제든", "2025년 훙브엉 거리에 문을 연 가장 새로운 5성급 호텔."),
  ("Ana Mandara Villas Dalat", "오전", "조용한 소나무 언덕의 복원된 프랑스 식민지풍 빌라."),
  ("Ladalat Hotel", "언제든", "마이아인다오 거리의 대형 호텔, 사랑의 계곡 근처."),
  ("Swiss-Belresort Tuyen Lam", "오전", "골프장 옆 언덕 위 리조트, 산 전망."),
  ("Dalat Edensee Lake Resort & Spa", "오전", "뚜엔럼 호수 소나무 숲 속 호숫가 리조트."),
  ("Tea Resort Prenn", "낮", "쁘렌 고개 아래, 쁘렌 폭포 옆의 넓은 리조트.")])
T["ja"] = _mk("ダラットの5つ星ホテル：ホテル・リゾート8軒の地図 | Van Phu", "ダラット5つ星ホテルマップ",
 "ダラットの5つ星ホテル・リゾート8軒の地図。1922年創業のダラット・パレスからトゥエンラム湖のリゾートまで、ルート案内・距離・無料PDF付き。",
 "ダラットの5つ星ホテル・リゾート8軒です。市内に5軒、トゥエンラム湖とプレン峠に3軒。ワンタップでルート案内、バイクでの距離も表示しています。",
 "市内（1–5）", "知っておきたいこと",
 [("配達", "2日以上のレンタルなら市中心部のホテルまでバイクをお届け"), ("湖のリゾート（6–8）", "市内から20–30分、坂道が多い — Air Blade 125ccがおすすめ"), ("デポジット", "パスポートまたはIDカード、現金デポジットなし"), ("返却", "21:00までに返却")],
 "ヒント",
 ["バイクを安全に停められる場所をフロントで聞きましょう。", "トゥエンラム湖周辺の道は夜は暗いので、暗くなる前に戻りましょう。", "湖のリゾートには市内行きシャトルもありますが、バイクがあれば自由に動けます。", "星の等級や料金は変わることがあります — 予約時にホテルへ確認を。"],
 [("Dalat Palace Heritage Hotel", "午後", "スアンフーン湖を見下ろす1922年のフランス時代のホテル。"),
  ("MerPerle Dalat Hotel", "いつでも", "フンヴオン通りの宮殿風ホテル、屋内温水プールあり。"),
  ("Best Western Premier Imperial Dalat", "いつでも", "2025年にフンヴオン通りに開業した最新の5つ星ホテル。"),
  ("Ana Mandara Villas Dalat", "午前", "静かな松の丘に建つ、修復されたフランス植民地時代のヴィラ。"),
  ("Ladalat Hotel", "いつでも", "マイアンダオ通りの大型ホテル、愛の谷の近く。"),
  ("Swiss-Belresort Tuyen Lam", "午前", "ゴルフ場に隣接する丘の上のリゾート、山の眺め。"),
  ("Dalat Edensee Lake Resort & Spa", "午前", "トゥエンラム湖の松林に囲まれた湖畔リゾート。"),
  ("Tea Resort Prenn", "日中", "プレン峠のふもと、プレンの滝のそばにある広いリゾート。")])
T["th"] = _mk("โรงแรม 5 ดาวในดาลัด: แผนที่โรงแรมและรีสอร์ต 8 แห่ง | Van Phu", "แผนที่โรงแรม 5 ดาวดาลัด",
 "แผนที่โรงแรมและรีสอร์ต 5 ดาว 8 แห่งในดาลัด ตั้งแต่ Dalat Palace ปี 1922 ถึงรีสอร์ตริมทะเลสาบเตวียนเลิม พร้อมเส้นทาง ระยะทาง และ PDF ฟรี",
 "นี่คือโรงแรมและรีสอร์ต 5 ดาว 8 แห่งในดาลัด ในเมือง 5 แห่ง และที่ทะเลสาบเตวียนเลิมกับช่องเขาเปรนอีก 3 แห่ง กดนำทางได้ทันที พร้อมระยะทางขี่มอเตอร์ไซค์",
 "ในเมือง (1–5)", "ควรรู้",
 [("ส่งรถ", "เช่าตั้งแต่ 2 วัน ส่งรถถึงโรงแรมในตัวเมือง"), ("รีสอร์ตริมทะเลสาบ (6–8)", "ห่างเมือง 20–30 นาที ทางขึ้นลงเขา — แนะนำ Air Blade 125cc"), ("มัดจำ", "ฝากพาสปอร์ตหรือบัตรประชาชน ไม่มีมัดจำเงินสด"), ("คืนรถ", "คืนรถก่อน 21:00")],
 "เคล็ดลับ",
 ["ถามแผนกต้อนรับว่าจอดรถตรงไหนปลอดภัย", "ถนนรอบทะเลสาบเตวียนเลิมมืดตอนกลางคืน ควรกลับก่อนมืด", "รีสอร์ตริมทะเลสาบบางแห่งมีรถรับส่งเข้าเมือง แต่มีมอเตอร์ไซค์ไปเที่ยวได้อิสระกว่า", "ระดับดาวและราคาอาจเปลี่ยน — สอบถามโรงแรมตอนจอง"],
 [("Dalat Palace Heritage Hotel", "ช่วงบ่าย", "โรงแรมยุคฝรั่งเศสปี 1922 มองเห็นทะเลสาบซวนเฮือง"),
  ("MerPerle Dalat Hotel", "ทั้งวัน", "โรงแรมสไตล์พระราชวังบนถนนหุ่งเวือง มีสระว่ายน้ำอุ่นในร่ม"),
  ("Best Western Premier Imperial Dalat", "ทั้งวัน", "โรงแรม 5 ดาวใหม่ล่าสุด เปิดปี 2025 บนถนนหุ่งเวือง"),
  ("Ana Mandara Villas Dalat", "ช่วงเช้า", "วิลล่าฝรั่งเศสเก่าที่บูรณะแล้ว บนเนินสนเงียบสงบ"),
  ("Ladalat Hotel", "ทั้งวัน", "โรงแรมใหญ่บนถนนไมอันด่าว ใกล้หุบเขาแห่งความรัก"),
  ("Swiss-Belresort Tuyen Lam", "ช่วงเช้า", "รีสอร์ตบนเนินเขาติดสนามกอล์ฟ วิวภูเขา"),
  ("Dalat Edensee Lake Resort & Spa", "ช่วงเช้า", "รีสอร์ตริมทะเลสาบเตวียนเลิมกลางป่าสน"),
  ("Tea Resort Prenn", "กลางวัน", "รีสอร์ตกว้างที่เชิงช่องเขาเปรน ข้างน้ำตกเปรน")])
T["id"] = _mk("Hotel Bintang 5 di Da Lat: Peta 8 Hotel & Resor | Van Phu", "Peta Hotel Bintang 5 Da Lat",
 "Peta 8 hotel dan resor bintang 5 di Da Lat — dari Dalat Palace tahun 1922 hingga resor di Danau Tuyen Lam — dengan petunjuk arah, jarak, dan PDF gratis.",
 "Inilah 8 hotel dan resor bintang 5 di Da Lat — lima di kota dan tiga di Danau Tuyen Lam dan Celah Prenn — dengan petunjuk arah sekali ketuk dan jarak naik motor.",
 "Di kota (1–5)", "Perlu diketahui",
 [("Antar motor", "kami antar motor ke hotel Anda di pusat kota untuk sewa 2 hari atau lebih"), ("Resor danau (6–8)", "20–30 menit dari kota, jalan berbukit — lebih baik pakai Air Blade 125cc"), ("Jaminan", "paspor atau kartu identitas, tanpa deposit uang"), ("Pengembalian", "kembalikan motor sebelum 21:00")],
 "Tips",
 ["Tanyakan resepsionis tempat parkir motor yang aman.", "Jalan di sekitar Danau Tuyen Lam gelap di malam hari — kembalilah sebelum gelap.", "Beberapa resor danau punya shuttle ke kota; dengan motor Anda lebih bebas menjelajah.", "Peringkat bintang dan harga bisa berubah — tanyakan hotel saat memesan."],
 [("Dalat Palace Heritage Hotel", "Sore", "Hotel era Prancis tahun 1922 di atas Danau Xuan Huong."),
  ("MerPerle Dalat Hotel", "Kapan saja", "Hotel bergaya istana di Jalan Hung Vuong dengan kolam renang air hangat dalam ruangan."),
  ("Best Western Premier Imperial Dalat", "Kapan saja", "Hotel bintang 5 terbaru, dibuka tahun 2025 di Jalan Hung Vuong."),
  ("Ana Mandara Villas Dalat", "Pagi", "Vila kolonial Prancis yang dipugar di bukit pinus yang tenang."),
  ("Ladalat Hotel", "Kapan saja", "Hotel besar di Jalan Mai Anh Dao, dekat Lembah Cinta."),
  ("Swiss-Belresort Tuyen Lam", "Pagi", "Resor di bukit di samping lapangan golf, pemandangan gunung."),
  ("Dalat Edensee Lake Resort & Spa", "Pagi", "Resor tepi danau di hutan pinus Danau Tuyen Lam."),
  ("Tea Resort Prenn", "Siang", "Resor luas di kaki Celah Prenn, di samping Air Terjun Prenn.")])
T["ms"] = _mk("Hotel 5 Bintang di Da Lat: Peta 8 Hotel & Resort | Van Phu", "Peta Hotel 5 Bintang Da Lat",
 "Peta 8 hotel dan resort 5 bintang di Da Lat — dari Dalat Palace tahun 1922 hingga resort di Tasik Tuyen Lam — dengan arah, jarak dan PDF percuma.",
 "Inilah 8 hotel dan resort 5 bintang di Da Lat — lima di bandar dan tiga di Tasik Tuyen Lam dan Laluan Prenn — dengan arah satu ketikan dan jarak menunggang motosikal.",
 "Dalam bandar (1–5)", "Perlu tahu",
 [("Hantar motosikal", "kami hantar motosikal ke hotel anda di pusat bandar untuk sewa 2 hari atau lebih"), ("Resort tasik (6–8)", "20–30 minit dari bandar, jalan berbukit — lebih baik naik Air Blade 125cc"), ("Cagaran", "pasport atau kad pengenalan, tiada deposit wang"), ("Pulangkan", "pulangkan motosikal sebelum 21:00")],
 "Tip",
 ["Tanya kaunter penyambut tetamu tempat letak motosikal yang selamat.", "Jalan di sekitar Tasik Tuyen Lam gelap pada waktu malam — pulang sebelum gelap.", "Sesetengah resort tasik ada shuttle ke bandar; dengan motosikal anda lebih bebas meneroka.", "Penarafan bintang dan harga boleh berubah — semak dengan hotel semasa menempah."],
 [("Dalat Palace Heritage Hotel", "Petang", "Hotel era Perancis tahun 1922 di atas Tasik Xuan Huong."),
  ("MerPerle Dalat Hotel", "Bila-bila masa", "Hotel gaya istana di Jalan Hung Vuong dengan kolam renang air suam dalam bangunan."),
  ("Best Western Premier Imperial Dalat", "Bila-bila masa", "Hotel 5 bintang terbaharu, dibuka pada 2025 di Jalan Hung Vuong."),
  ("Ana Mandara Villas Dalat", "Pagi", "Vila kolonial Perancis yang dipulihkan di bukit pain yang tenang."),
  ("Ladalat Hotel", "Bila-bila masa", "Hotel besar di Jalan Mai Anh Dao, berhampiran Lembah Cinta."),
  ("Swiss-Belresort Tuyen Lam", "Pagi", "Resort di bukit bersebelahan padang golf, pemandangan gunung."),
  ("Dalat Edensee Lake Resort & Spa", "Pagi", "Resort tepi tasik di hutan pain Tasik Tuyen Lam."),
  ("Tea Resort Prenn", "Siang", "Resort luas di kaki Laluan Prenn, di sebelah Air Terjun Prenn.")])
T["de"] = _mk("5-Sterne-Hotels in Da Lat: Karte mit 8 Hotels & Resorts | Van Phu", "Karte der 5-Sterne-Hotels in Da Lat",
 "Karte von 8 als 5 Sterne eingestuften Hotels und Resorts in Da Lat — vom Dalat Palace von 1922 bis zu den Resorts am Tuyen-Lam-See — mit Route, Entfernung und kostenlosem PDF.",
 "Hier sind 8 Hotels und Resorts mit 5 Sternen in Da Lat — fünf in der Stadt, drei am Tuyen-Lam-See und am Prenn-Pass — mit Route per Fingertipp und Entfernung mit dem Roller.",
 "In der Stadt (1–5)", "Gut zu wissen",
 [("Lieferung", "ab 2 Miettagen bringen wir den Roller zu Ihrem Hotel im Zentrum"), ("Seeresorts (6–8)", "20–30 Minuten von der Stadt, hügelige Straßen — besser mit der Air Blade 125cc"), ("Kaution", "Reisepass oder Ausweis, keine Geldkaution"), ("Rückgabe", "Roller bis 21:00 zurückbringen")],
 "Tipps",
 ["Fragen Sie an der Rezeption nach einem sicheren Parkplatz für den Roller.", "Die Straßen um den Tuyen-Lam-See sind nachts dunkel — vor Einbruch der Dunkelheit zurückfahren.", "Manche Seeresorts haben einen Shuttle in die Stadt; mit dem Roller sind Sie flexibler.", "Sterne und Preise können sich ändern — bei der Buchung beim Hotel nachfragen."],
 [("Dalat Palace Heritage Hotel", "Nachmittag", "Prachtvolles Hotel aus der französischen Zeit (1922) über dem Xuan-Huong-See."),
  ("MerPerle Dalat Hotel", "Jederzeit", "Hotel im Palaststil an der Hung-Vuong-Straße mit beheiztem Hallenbad."),
  ("Best Western Premier Imperial Dalat", "Jederzeit", "Neuestes 5-Sterne-Hotel der Stadt, 2025 an der Hung-Vuong-Straße eröffnet."),
  ("Ana Mandara Villas Dalat", "Morgens", "Restaurierte französische Kolonialvillen auf einem ruhigen Kiefernhügel."),
  ("Ladalat Hotel", "Jederzeit", "Großes Hotel an der Mai-Anh-Dao-Straße, nahe dem Tal der Liebe."),
  ("Swiss-Belresort Tuyen Lam", "Morgens", "Resort am Hang neben einem Golfplatz mit Bergblick."),
  ("Dalat Edensee Lake Resort & Spa", "Morgens", "Resort am Ufer des Tuyen-Lam-Sees im Kiefernwald."),
  ("Tea Resort Prenn", "Tagsüber", "Großes Resort am Fuß des Prenn-Passes, neben dem Prenn-Wasserfall.")])
T["fr"] = _mk("Hôtels 5 étoiles à Da Lat : carte de 8 hôtels et resorts | Van Phu", "Carte des hôtels 5 étoiles de Da Lat",
 "Carte de 8 hôtels et resorts classés 5 étoiles à Da Lat — du Dalat Palace de 1922 aux resorts du lac Tuyen Lam — avec itinéraire, distances et PDF gratuit.",
 "Voici 8 hôtels et resorts classés 5 étoiles à Da Lat — cinq en ville et trois au lac Tuyen Lam et au col de Prenn — avec itinéraire en un clic et distance en scooter.",
 "En ville (1–5)", "Bon à savoir",
 [("Livraison", "nous livrons le scooter à votre hôtel du centre-ville pour 2 jours de location ou plus"), ("Resorts du lac (6–8)", "à 20–30 minutes de la ville, routes vallonnées — mieux en Air Blade 125cc"), ("Caution", "passeport ou carte d'identité, pas de caution en argent"), ("Retour", "rendez le scooter avant 21 h")],
 "Conseils",
 ["Demandez à la réception où garer le scooter en sécurité.", "Les routes autour du lac Tuyen Lam sont sombres la nuit — rentrez avant la tombée de la nuit.", "Certains resorts du lac ont une navette vers la ville ; en scooter, vous êtes plus libre.", "Les étoiles et les prix peuvent changer — vérifiez auprès de l'hôtel à la réservation."],
 [("Dalat Palace Heritage Hotel", "Après-midi", "Grand hôtel de l'époque française (1922) dominant le lac Xuan Huong."),
  ("MerPerle Dalat Hotel", "À tout moment", "Hôtel de style palais rue Hung Vuong, avec piscine intérieure chauffée."),
  ("Best Western Premier Imperial Dalat", "À tout moment", "Le plus récent 5 étoiles de la ville, ouvert en 2025 rue Hung Vuong."),
  ("Ana Mandara Villas Dalat", "Matin", "Villas coloniales françaises restaurées sur une colline de pins paisible."),
  ("Ladalat Hotel", "À tout moment", "Grand hôtel rue Mai Anh Dao, près de la Vallée de l'Amour."),
  ("Swiss-Belresort Tuyen Lam", "Matin", "Resort à flanc de colline à côté d'un golf, vue sur les montagnes."),
  ("Dalat Edensee Lake Resort & Spa", "Matin", "Resort au bord du lac Tuyen Lam, dans la forêt de pins."),
  ("Tea Resort Prenn", "Journée", "Grand resort au pied du col de Prenn, à côté de la cascade de Prenn.")])
T["es"] = _mk("Hoteles de 5 estrellas en Da Lat: mapa de 8 hoteles y resorts | Van Phu", "Mapa de hoteles 5 estrellas de Da Lat",
 "Mapa de 8 hoteles y resorts de 5 estrellas en Da Lat — del Dalat Palace de 1922 a los resorts del lago Tuyen Lam — con cómo llegar, distancias y PDF gratis.",
 "Aquí tienes 8 hoteles y resorts de 5 estrellas en Da Lat — cinco en la ciudad y tres en el lago Tuyen Lam y el paso de Prenn — con ruta en un toque y la distancia en moto.",
 "En la ciudad (1–5)", "Bueno saber",
 [("Entrega", "llevamos la moto a tu hotel del centro en alquileres de 2 días o más"), ("Resorts del lago (6–8)", "a 20–30 minutos de la ciudad, carreteras con cuestas — mejor en Air Blade 125cc"), ("Garantía", "pasaporte o documento de identidad, sin depósito en efectivo"), ("Devolución", "devuelve la moto antes de las 21:00")],
 "Consejos",
 ["Pregunta en recepción dónde aparcar la moto con seguridad.", "Las carreteras alrededor del lago Tuyen Lam están oscuras de noche — vuelve antes de que anochezca.", "Algunos resorts del lago tienen traslado al centro; con moto tienes más libertad.", "Las estrellas y los precios pueden cambiar — confírmalo con el hotel al reservar."],
 [("Dalat Palace Heritage Hotel", "Tarde", "Gran hotel de la época francesa (1922) sobre el lago Xuan Huong."),
  ("MerPerle Dalat Hotel", "Cualquier hora", "Hotel estilo palacio en la calle Hung Vuong, con piscina cubierta climatizada."),
  ("Best Western Premier Imperial Dalat", "Cualquier hora", "El 5 estrellas más nuevo de la ciudad, abierto en 2025 en la calle Hung Vuong."),
  ("Ana Mandara Villas Dalat", "Mañana", "Villas coloniales francesas restauradas en una tranquila colina de pinos."),
  ("Ladalat Hotel", "Cualquier hora", "Gran hotel en la calle Mai Anh Dao, cerca del Valle del Amor."),
  ("Swiss-Belresort Tuyen Lam", "Mañana", "Resort en la ladera junto a un campo de golf, con vistas a las montañas."),
  ("Dalat Edensee Lake Resort & Spa", "Mañana", "Resort a orillas del lago Tuyen Lam, en el bosque de pinos."),
  ("Tea Resort Prenn", "Durante el día", "Gran resort al pie del paso de Prenn, junto a la cascada de Prenn.")])
T["he"] = _mk("מלונות 5 כוכבים בדלאט: מפה של 8 מלונות ואתרי נופש | Van Phu", "מפת מלונות 5 כוכבים בדלאט",
 "מפה של 8 מלונות ואתרי נופש בדירוג 5 כוכבים בדלאט — מ-Dalat Palace משנת 1922 ועד אתרי הנופש באגם טויין לאם — עם ניווט, מרחקים ו-PDF בחינם.",
 "הנה 8 מלונות ואתרי נופש בדירוג 5 כוכבים בדלאט — חמישה בעיר ושלושה באגם טויין לאם ובמעבר פרן — עם ניווט בלחיצה אחת ומרחק בקטנוע.",
 "בעיר (1–5)", "כדאי לדעת",
 [("משלוח", "בהשכרה של יומיים ומעלה נביא את הקטנוע למלון שלכם במרכז העיר"), ("אתרי נופש באגם (6–8)", "20–30 דקות מהעיר, דרכים הרריות — עדיף Air Blade 125cc"), ("ערבון", "דרכון או תעודת זהות, בלי פיקדון כספי"), ("החזרה", "מחזירים את הקטנוע עד 21:00")],
 "טיפים",
 ["שאלו בקבלה איפה לחנות את הקטנוע בבטחה.", "הדרכים סביב אגם טויין לאם חשוכות בלילה — חזרו לפני החשכה.", "לחלק מאתרי הנופש באגם יש הסעה לעיר; עם קטנוע אתם חופשיים יותר.", "דירוג הכוכבים והמחירים משתנים — בדקו מול המלון בהזמנה."],
 [("Dalat Palace Heritage Hotel", "אחר הצהריים", "מלון מפואר מהתקופה הצרפתית (1922) מעל אגם שואן הואנג."),
  ("MerPerle Dalat Hotel", "בכל שעה", "מלון בסגנון ארמון ברחוב הונג וואנג, עם בריכה מקורה מחוממת."),
  ("Best Western Premier Imperial Dalat", "בכל שעה", "מלון 5 הכוכבים החדש ביותר בעיר, נפתח ב-2025 ברחוב הונג וואנג."),
  ("Ana Mandara Villas Dalat", "בוקר", "וילות קולוניאליות צרפתיות משוחזרות על גבעת אורנים שקטה."),
  ("Ladalat Hotel", "בכל שעה", "מלון גדול ברחוב מאי אן דאו, ליד עמק האהבה."),
  ("Swiss-Belresort Tuyen Lam", "בוקר", "אתר נופש על צלע גבעה ליד מגרש גולף, עם נוף להרים."),
  ("Dalat Edensee Lake Resort & Spa", "בוקר", "אתר נופש על שפת אגם טויין לאם ביער האורנים."),
  ("Tea Resort Prenn", "במשך היום", "אתר נופש גדול למרגלות מעבר פרן, ליד מפל פרן.")])

from content._langs import inject as _inject
_inject(T, __name__)

# ===== 2026-11-12: owner sent a list of 9 five-star hotels/resorts (hotels_5star_dalat.json), checked on Google Maps the same day.
# Added: Golden Sun, Grand Mercure Dalat (owner confirms 5-star), Binh An Village. Kept Swiss-Belresort and Tea Resort Prenn
# (already on the page, not in the list). Coordinates, phones and addresses from Google Maps (the list's Binh An point was ~1 km off).
# The PDF still shows the first 8, so it is hidden until redrawn.
_OLD = {x[0]: x for x in SPOTS}
SPOTS = [
    _OLD["dalatpalace"],
    ("goldensun",    11.9379193, 108.4465365, "ChIJG9-FB78TcTERTO7DU33kHvE", True, "24h"),
    _OLD["merperle"],
    ("grandmercure", 11.9451708, 108.4594399, "ChIJP6Esk3sTcTERx5XZn19lUx0", True, "24h"),
    _OLD["imperial"], _OLD["anamandara"], _OLD["ladalat"],
    _OLD["swissbel"], _OLD["edensee"],
    ("binhan",       11.8877595, 108.4176396, "ChIJRZmEBEZrcTERIkUn7yHrWQA", False, "24h"),
    _OLD["teaprenn"],
]
N = len(SPOTS); NT = 7
PDF = None
PHONE = {"dalatpalace": "+84 263 3825 444", "goldensun": "+84 263 3939 939", "merperle": "+84 263 3553 789", "grandmercure": "+84 263 3810 826",
         "imperial": "+84 263 3626 626", "anamandara": "+84 263 3555 888", "ladalat": "+84 965 118 118", "swissbel": "+84 263 3800 800",
         "edensee": "+84 263 3831 515", "binhan": "+84 263 3800 999", "teaprenn": "+84 944 391 616"}
ADDR = {"dalatpalace": "2 Trần Phú", "goldensun": "1 Bà Huyện Thanh Quan", "merperle": "1 Hùng Vương", "grandmercure": "03 Nguyễn Du",
        "imperial": "57–59 Hùng Vương", "anamandara": "2 Lê Lai", "ladalat": "106A Mai Anh Đào", "swissbel": "Số 7 & 8, KDL hồ Tuyền Lâm",
        "edensee": "Khu VII.2, KDL hồ Tuyền Lâm", "binhan": "KDL hồ Tuyền Lâm", "teaprenn": "Chân đèo Prenn"}
AREA = {**{k: "center" for k in ("dalatpalace", "goldensun", "merperle", "grandmercure", "imperial")},
        **{k: "nature" for k in ("anamandara", "ladalat", "swissbel", "edensee", "binhan", "teaprenn")}}
_AL = {  # all, centre & Hung Vuong, Tuyen Lam Lake & pine hills, "to Van Phu"
 "vi": ("Tất cả", "Trung tâm & Hùng Vương", "Hồ Tuyền Lâm & Đồi thông", "đến Văn Phú"),
 "en": ("All", "Centre & Hung Vuong", "Tuyen Lam Lake & pine hills", "to Van Phu"),
 "ru": ("Все", "Центр и Хунгвыонг", "Озеро Туйенлам и сосновые холмы", "до Van Phu"),
 "zh": ("全部", "市中心和雄王路", "宣林湖和松林山丘", "到 Van Phu"),
 "ko": ("전체", "시내 & 훙브엉", "뚜옌럼 호수 & 소나무 언덕", "Van Phu까지"),
 "ja": ("すべて", "中心部・フンヴオン通り", "トゥエンラム湖・松林の丘", "Van Phuまで"),
 "th": ("ทั้งหมด", "ใจกลางเมือง & หุ่งเวือง", "ทะเลสาบเตวียนเลิม & เนินสน", "ถึง Van Phu"),
 "id": ("Semua", "Pusat kota & Hung Vuong", "Danau Tuyen Lam & bukit pinus", "ke Van Phu"),
 "ms": ("Semua", "Pusat bandar & Hung Vuong", "Tasik Tuyen Lam & bukit pain", "ke Van Phu"),
 "de": ("Alle", "Zentrum & Hung Vuong", "Tuyen-Lam-See & Kiefernhügel", "bis Van Phu"),
 "fr": ("Tous", "Centre & Hung Vuong", "Lac Tuyen Lam & collines de pins", "jusqu'à Van Phu"),
 "es": ("Todos", "Centro y Hung Vuong", "Lago Tuyen Lam y colinas de pinos", "hasta Van Phu"),
 "he": ("הכול", "מרכז והונג וואנג", "אגם טויין לאם וגבעות האורנים", "עד Van Phu"),
 "it": ("Tutti", "Centro e Hung Vuong", "Lago Tuyen Lam e colline di pini", "fino a Van Phu"),
 "nl": ("Alle", "Centrum & Hung Vuong", "Tuyen Lam-meer & dennenheuvels", "tot Van Phu"),
 "km": ("ទាំងអស់", "ទីក្រុង & Hùng Vương", "បឹង Tuyền Lâm & ភ្នំស្រល់", "ដល់ Van Phu"),
 "lo": ("ທັງໝົດ", "ໃຈກາງເມືອງ & Hùng Vương", "ທະເລສາບ Tuyền Lâm & ພູແປກ", "ຫາ Van Phu"),
 "my": ("အားလုံး", "မြို့လယ် & Hùng Vương", "Tuyền Lâm ကန် & ထင်းရှူးတောင်", "Van Phu သို့"),
}
def areas(l):
    a = _AL.get(l, _AL["en"]); return [("", a[0]), ("center", a[1]), ("nature", a[2])]
def toshop(l): return _AL.get(l, _AL["en"])[3]

_NEW = ["goldensun", "grandmercure", "binhan"]
_NAME = {"goldensun": "Golden Sun Hotel – Dalat", "grandmercure": "Grand Mercure Dalat", "binhan": "Binh An Village Dalat Resort"}
_D = {
 "en": ["Hotel by Lam Vien Square and Xuan Huong Lake, with a spa, indoor pool and rooftop bar.",
        "Hotel with French-style buildings and large flower gardens on Nguyen Du Street, near Da Lat Railway Station.",
        "Small resort of vintage-style houses and gardens above Tuyen Lam Lake, about 9 km from the centre."],
 "vi": ["Khách sạn cạnh quảng trường Lâm Viên và hồ Xuân Hương, có spa, hồ bơi trong nhà và bar sân thượng.",
        "Khách sạn phong cách Pháp, vườn hoa rộng trên đường Nguyễn Du, gần ga Đà Lạt.",
        "Resort nhỏ gồm những ngôi nhà kiểu xưa và vườn hoa trên đồi bên hồ Tuyền Lâm, cách trung tâm khoảng 9 km."],
 "zh": ["靠近林园广场和春香湖的酒店，有水疗、室内泳池和屋顶酒吧。",
        "阮攸路上法式建筑、大花园的酒店，靠近大叻火车站。",
        "宣林湖畔山坡上的小型度假村，复古小屋和花园，距市中心约 9 公里。"],
 "ru": ["Отель у площади Ламвьен и озера Суанхыонг: спа, крытый бассейн и бар на крыше.",
        "Отель во французском стиле с большими цветочными садами на улице Нгуен Зу, рядом с вокзалом Далата.",
        "Небольшой курорт из домиков в старинном стиле с садами над озером Туйенлам, около 9 км от центра."],
 "ko": ["럼비엔 광장과 쑤언흐엉 호수 옆 호텔, 스파·실내 수영장·루프톱 바가 있음.",
        "응우옌주 거리의 프랑스풍 건물과 넓은 꽃정원이 있는 호텔, 달랏 기차역 근처.",
        "뚜옌럼 호수 위 언덕의 옛날풍 집과 정원으로 된 작은 리조트, 시내에서 약 9km."],
 "id": ["Hotel di dekat Lapangan Lam Vien dan Danau Xuan Huong, dengan spa, kolam renang dalam ruangan dan bar atap.",
        "Hotel bergaya Prancis dengan taman bunga luas di Jalan Nguyen Du, dekat Stasiun Kereta Da Lat.",
        "Resor kecil berisi rumah bergaya klasik dan taman di atas Danau Tuyen Lam, sekitar 9 km dari pusat kota."],
}
_TPL = {"ja": "{s}のホテル。", "th": "โรงแรมที่ {s}", "ms": "Hotel di {s}.", "de": "Hotel an der {s}.", "fr": "Hôtel {s}.",
        "es": "Hotel en {s}.", "he": "מלון ב-{s}.", "it": "Hotel in {s}.", "nl": "Hotel aan {s}.", "km": "សណ្ឋាគារនៅ {s}",
        "lo": "ໂຮງແຮມຢູ່ {s}", "my": "{s} ရှိ ဟိုတယ်"}
_PLACE = {"goldensun": "Bà Huyện Thanh Quan", "grandmercure": "Nguyễn Du", "binhan": "Tuyền Lâm"}
_DEL = {"vi": "Khách lưu trú tại các khách sạn 5 sao trung tâm Đà Lạt (Dalat Palace, MerPerle, Golden Sun, Grand Mercure...) được Văn Phú hỗ trợ giao xe máy tận nơi miễn phí khi thuê từ 2 ngày.",
        "en": "Staying at a 5-star hotel in central Da Lat (Dalat Palace, MerPerle, Golden Sun, Grand Mercure…)? Van Phu delivers your scooter to the hotel for free on rentals of 2 days or more.",
        "zh": "入住大叻市中心五星级酒店（大叻皇宫、MerPerle、Golden Sun、Grand Mercure 等）的客人，租车 2 天以上，Van Phu 免费送车到酒店。",
        "ru": "Живёте в 5-звёздочном отеле в центре Далата (Dalat Palace, MerPerle, Golden Sun, Grand Mercure…)? При аренде от 2 дней Van Phu бесплатно доставит байк к отелю.",
        "ko": "달랏 시내 5성급 호텔(Dalat Palace, MerPerle, Golden Sun, Grand Mercure 등)에 묵으신다면, 2일 이상 렌탈 시 Van Phu가 호텔까지 무료로 오토바이를 배달해 드립니다.",
        "id": "Menginap di hotel bintang 5 di pusat Da Lat (Dalat Palace, MerPerle, Golden Sun, Grand Mercure…)? Van Phu mengantar motor gratis ke hotel untuk sewa 2 hari atau lebih."}
_LEAD = {
 "vi": f"{N} khách sạn và resort 5 sao ở Đà Lạt: {NT} nơi trong thành phố và {N - NT} resort ven hồ Tuyền Lâm, đèo Prenn — có số điện thoại, khoảng cách tới tiệm Văn Phú và nút chỉ đường. " + _DEL["vi"],
 "en": f"{N} hotels and resorts listed as 5-star in Da Lat: {NT} in town and {N - NT} by Tuyen Lam Lake and Prenn Pass — with phone numbers, distance to our shop and one-tap directions. " + _DEL["en"],
 "zh": f"大叻 {N} 家五星级酒店和度假村：市区 {NT} 家，宣林湖和普连山口 {N - NT} 家——附电话、到 Van Phu 店的距离和一键导航。" + _DEL["zh"],
 "ru": f"{N} отелей и курортов 5 звёзд в Далате: {NT} в городе и {N - NT} у озера Туйенлам и перевала Пренн — с телефонами, расстоянием до нашей мастерской и маршрутом в одно касание. " + _DEL["ru"],
 "ko": f"달랏의 5성급 호텔·리조트 {N}곳: 시내 {NT}곳과 뚜옌럼 호수·쁘렌 고개 {N - NT}곳 — 전화번호, Van Phu 가게까지 거리, 원터치 길찾기 포함. " + _DEL["ko"],
 "id": f"{N} hotel dan resor bintang 5 di Da Lat: {NT} di kota dan {N - NT} di Danau Tuyen Lam dan Celah Prenn — lengkap dengan nomor telepon, jarak ke toko kami dan petunjuk arah sekali ketuk. " + _DEL["id"],
 "ja": f"ダラットの5つ星ホテル・リゾート{N}軒：市内{NT}軒とトゥエンラム湖・プレン峠{N - NT}軒。電話番号、Van Phuまでの距離、ワンタップのルート案内付き。",
 "th": f"โรงแรมและรีสอร์ต 5 ดาว {N} แห่งในดาลัด: ในเมือง {NT} แห่ง และริมทะเลสาบเตวียนเลิมกับช่องเขาเปรน {N - NT} แห่ง พร้อมเบอร์โทร ระยะทางถึงร้าน Van Phu และปุ่มนำทาง",
 "ms": f"{N} hotel dan resort 5 bintang di Da Lat: {NT} di bandar dan {N - NT} di Tasik Tuyen Lam dan Laluan Prenn — dengan nombor telefon, jarak ke kedai kami dan arah satu ketikan.",
 "de": f"{N} Hotels und Resorts mit 5 Sternen in Da Lat: {NT} in der Stadt und {N - NT} am Tuyen-Lam-See und am Prenn-Pass — mit Telefonnummer, Entfernung zu unserem Laden und Route per Fingertipp.",
 "fr": f"{N} hôtels et resorts 5 étoiles à Da Lat : {NT} en ville et {N - NT} au lac Tuyen Lam et au col de Prenn — avec téléphone, distance jusqu'à notre boutique et itinéraire en un clic.",
 "es": f"{N} hoteles y resorts de 5 estrellas en Da Lat: {NT} en la ciudad y {N - NT} junto al lago Tuyen Lam y el paso de Prenn — con teléfono, distancia a nuestra tienda y ruta en un toque.",
 "he": f"{N} מלונות ואתרי נופש בדירוג 5 כוכבים בדלאט: {NT} בעיר ו-{N - NT} ליד אגם טויין לאם ומעבר פרן — עם מספרי טלפון, מרחק לחנות שלנו וניווט בלחיצה אחת.",
 "it": f"{N} hotel e resort 5 stelle a Da Lat: {NT} in città e {N - NT} sul lago Tuyen Lam e al passo di Prenn — con telefono, distanza dal nostro negozio e indicazioni con un tocco.",
 "nl": f"{N} hotels en resorts met 5 sterren in Da Lat: {NT} in de stad en {N - NT} aan het Tuyen Lam-meer en de Prenn-pas — met telefoonnummer, afstand tot onze winkel en route met één tik.",
}
_TITLE = {"en": f"5-Star Hotels in Da Lat: Map of {N} Hotels & Resorts | Van Phu",
          "vi": f"Khách sạn 5 sao Đà Lạt: bản đồ {N} khách sạn và resort, có số điện thoại | Văn Phú",
          "zh": f"大叻五星级酒店：{N} 家酒店与度假村地图（附电话） | Van Phu",
          "ru": f"Отели 5 звёзд в Далате: карта {N} отелей и курортов | Van Phu",
          "ko": f"달랏 5성급 호텔: 호텔·리조트 {N}곳 지도 | Van Phu",
          "id": f"Hotel Bintang 5 di Da Lat: Peta {N} Hotel & Resor | Van Phu"}
_DESC = {"en": f"Map of {N} 5-star hotels and resorts in Da Lat — in town by Xuan Huong Lake and Hung Vuong, and by Tuyen Lam Lake — with phone numbers, distance to Van Phu and directions.",
         "vi": f"Bản đồ {N} khách sạn và resort 5 sao Đà Lạt — trung tâm hồ Xuân Hương, Hùng Vương và ven hồ Tuyền Lâm — có số điện thoại, khoảng cách tới Văn Phú và chỉ đường.",
         "zh": f"大叻 {N} 家五星级酒店和度假村地图——春香湖、雄王路一带和宣林湖边——附电话、到 Van Phu 的距离和导航。",
         "ru": f"Карта {N} отелей и курортов 5 звёзд в Далате — у озера Суанхыонг, на Хунгвыонг и у озера Туйенлам — с телефонами, расстоянием до Van Phu и маршрутом.",
         "ko": f"달랏 5성급 호텔·리조트 {N}곳 지도 — 쑤언흐엉 호수·훙브엉 거리와 뚜옌럼 호숫가 — 전화번호, Van Phu까지 거리, 길찾기.",
         "id": f"Peta {N} hotel dan resor bintang 5 di Da Lat — dekat Danau Xuan Huong, Jalan Hung Vuong dan Danau Tuyen Lam — dengan nomor telepon, jarak ke Van Phu dan petunjuk arah."}
_KLM = {"km": [("5 ក្នុងទីក្រុង", f"{NT} ក្នុងទីក្រុង"), ("3 នៅបឹង", f"{N - NT} នៅបឹង")],
        "lo": [("5 ແຫ່ງໃນເມືອງ", f"{NT} ແຫ່ງໃນເມືອງ"), ("3 ແຫ່ງຢູ່ທະເລສາບ", f"{N - NT} ແຫ່ງຢູ່ທະເລສາບ")],
        "my": [("မြို့တွင်း 5 ခု", f"မြို့တွင်း {NT} ခု"), ("Prenn ချိုင့်ဝှမ်းရှိ 3 ခု", f"Prenn ချိုင့်ဝှမ်းရှိ {N - NT} ခု")]}
import re as _re
for _l in LANGS:
    t = T[_l]; anytime = t["s"]["dalatpalace"][1]
    for i, sid in enumerate(_NEW):
        t["s"][sid] = (_NAME[sid], anytime, _D[_l][i] if _l in _D else _TPL[_l].format(s=_PLACE[sid]))
    t["title"] = _TITLE.get(_l) or _re.sub(r"(?<!\d)8(?!\d)", str(N), t["title"])
    if _l in _LEAD:
        t["lead"] = _LEAD[_l]
        t["desc"] = _DESC.get(_l, _LEAD[_l])
    else:
        ld = _re.sub(r"(?<!\d)8(?!\d)", str(N), t["lead"])
        for a, b in _KLM[_l]:
            assert a in ld, (_l, a); ld = ld.replace(a, b)
        t["lead"] = ld
        t["desc"] = (_re.sub(r"(?<!\d)8(?!\d)", str(N), t["desc"]).replace(" និង PDF ឥតគិតថ្លៃ", "").replace(" ແລະ PDF ຟຣີ", "")
                     .replace("၊ အကွာအဝေးနှင့် PDF အခမဲ့", "နှင့် အကွာအဝေး"))
    t["center"] = t["center"].replace("1–5", f"1–{NT}")
    t["season"] = [(a.replace("6–8", f"{NT + 1}–{N}"), b) for a, b in t["season"]]
    assert f"1–{NT}" in t["center"] and any(f"{NT + 1}–{N}" in a for a, _ in t["season"]), _l
    assert "PDF" not in t["desc"] + t["title"] + t["lead"], _l
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"dalatpalace": "Dalat Palace Heritage Hotel", "merperle": "MerPerle Dalat Hotel", "imperial": "Best Western Premier Imperial Dalat",
      "anamandara": "Ana Mandara Villas Dalat", "ladalat": "Ladalat Hotel", "swissbel": "Swiss-Belresort Tuyen Lam",
      "edensee": "Dalat Edensee Lake Resort", "teaprenn": "Tea Resort Prenn"}
_Q.update(_NAME)
def img_link(sid):
    """Temporary photo link: Google Images search for the hotel name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
