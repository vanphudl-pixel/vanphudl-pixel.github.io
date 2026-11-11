"""Da Lat 4-star hotels map — shared data for the website page (/4-star-hotels-map/) and the printable PDF.
Hotels listed as 4-star by at least two travel sources (mia.vn, vietnambooking.com, hotels.com, Oct 2026), with 800+
Google Maps reviews; coordinates and place links (cid) taken from Google Maps on 2026-10-14.
Expanded to 16 on 2026-11-11 from the owner's list (see the block after _inject)."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (reception)
SPOTS = [
    ("colline",    11.9439482, 108.4381016, "17255277842950743451", True,  "24h"),
    ("duparc",     11.9366386, 108.4389673, "8790842944379774753",  True,  "24h"),
    ("muongthanh", 11.9438404, 108.4399551, "1003164070957619988",  True,  "24h"),
    ("golfvalley", 11.9475322, 108.4405789, "8381202117877470580",  True,  "24h"),
    ("kings",      11.9435050, 108.4405111, "14341709312785904334", True,  "24h"),
    ("saphir",     11.9419343, 108.4347183, "3149213615629357863",  True,  "24h"),
    ("sammy",      11.9352354, 108.4326854, "6091233267378616388",  True,  "24h"),
    ("goldient",   11.9284095, 108.4457707, "3109569490500162061",  True,  "24h"),
    ("terracotta", 11.8948927, 108.4380538, "13411763141745868215", False, "24h"),
    ("wonder",     11.8959331, 108.4126064, "9573032481010526535",  False, "24h"),
]
CENTER = _PM.CENTER
SLUG = "4-star-hotels-map"
PDF = "VanPhu-Dalat-4-Star-Hotels-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 8
LEGW = 330
MAPH = 560
H1PT = 22
MAXKM = 7.0
RINGS = (1, 2, 5)
SIDE = {}
JITTER = {"muongthanh": (-10, 6), "kings": (20, 10), "golfvalley": (22, 0), "colline": (-14, 2)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("4-Star Hotels in Da Lat: Map of 10 Popular Hotels | Van Phu", "Da Lat 4-Star Hotels Map",
 "Map of 10 popular 4-star hotels and resorts in Da Lat — eight in the centre near the night market and two by Tuyen Lam Lake — with directions, distances and a free PDF.",
 "Here are 10 hotels and resorts listed as 4-star in Da Lat, each with 800+ Google Maps reviews — eight in the centre, most a short walk from the night market, and two by Tuyen Lam Lake — with one-tap directions.",
 "In town (1–8)", "Good to know",
 [("Delivery", "we bring the scooter to your hotel in the city centre for rentals of 2 days or more"), ("Lake resorts (9–10)", "about 20 minutes from town on hilly roads — an Air Blade 125cc is the better choice"), ("Deposit", "passport or ID card, no cash deposit"), ("Return", "bring the scooter back by 21:00")],
 "Tips",
 ["Ask reception where to park the scooter safely.", "Hotels 1–5 are a short walk from the night market and Xuan Huong Lake.", "Roads around Tuyen Lam Lake are dark at night — ride back before dark.", "Star ratings and prices change — check with the hotel when you book."],
 [("Colline Dalat", "Any time", "Modern hotel right next to the night market and Da Lat Market."),
  ("Du Parc Hotel Dalat", "Any time", "Vintage-style heritage hotel on Tran Phu Street, walking distance to the night market."),
  ("Muong Thanh Holiday Dalat", "Any time", "Period-style hotel with a courtyard garden, near the lake and the market."),
  ("Nesta Valley (Golf Valley) Hotel", "Any time", "Tall hotel on Bui Thi Xuan Street with city views and parking at the back."),
  ("Kings Hotel Dalat", "Any time", "Central hotel on Bui Thi Xuan Street, close to the market."),
  ("Saphir Dalat Hotel", "Any time", "Castle-style classic hotel full of antiques, in the centre."),
  ("Sammy Dalat Hotel", "Any time", "Large hotel on Le Hong Phong Street with hill views."),
  ("Goldient Boutique Hotel", "Any time", "Hue-inspired boutique hotel with a pool, south of the centre."),
  ("Terracotta Hotel & Resort", "Morning", "Large resort by Tuyen Lam Lake with a lakeside path in the pines."),
  ("Dalat Wonder Resort", "Morning", "Resort and villas with Tuyen Lam Lake views.")])
T["vi"] = _mk("Khách sạn 4 sao Đà Lạt: bản đồ 10 khách sạn đông khách | Văn Phú", "Bản đồ khách sạn 4 sao Đà Lạt",
 "Bản đồ 10 khách sạn và resort 4 sao đông khách ở Đà Lạt — 8 nơi ở trung tâm gần chợ đêm và 2 nơi ở hồ Tuyền Lâm — có chỉ đường, khoảng cách và PDF miễn phí.",
 "Đây là 10 khách sạn và resort được xếp hạng 4 sao ở Đà Lạt, nơi nào cũng có trên 800 đánh giá Google Maps — 8 nơi ở trung tâm, phần lớn đi bộ ra chợ đêm, và 2 nơi ở hồ Tuyền Lâm — có nút chỉ đường.",
 "Trong thành phố (1–8)", "Nên biết",
 [("Giao xe", "giao xe tận khách sạn trong trung tâm khi thuê từ 2 ngày"), ("Resort ven hồ (9–10)", "cách phố khoảng 20 phút, đường dốc — nên đi Air Blade 125cc"), ("Đặt cọc", "giữ hộ chiếu hoặc CCCD, không cọc tiền"), ("Trả xe", "trả xe trước 21:00")],
 "Lưu ý",
 ["Hỏi lễ tân chỗ để xe an toàn.", "Khách sạn 1–5 đi bộ vài phút ra chợ đêm và hồ Xuân Hương.", "Đường quanh hồ Tuyền Lâm tối vào ban đêm — nên về trước khi trời tối.", "Hạng sao và giá phòng có thể thay đổi — hỏi khách sạn khi đặt phòng."],
 [("Colline Dalat", "Cả ngày", "Khách sạn hiện đại sát chợ đêm và chợ Đà Lạt."),
  ("Du Parc Hotel Dalat", "Cả ngày", "Khách sạn cổ phong cách xưa trên đường Trần Phú, đi bộ ra chợ đêm."),
  ("Mường Thanh Holiday Đà Lạt", "Cả ngày", "Khách sạn kiến trúc cổ có sân vườn, gần hồ và chợ."),
  ("Nesta Valley (Golf Valley) Hotel", "Cả ngày", "Khách sạn cao tầng trên đường Bùi Thị Xuân, view thành phố, có bãi xe phía sau."),
  ("Kings Hotel Dalat", "Cả ngày", "Khách sạn trung tâm trên đường Bùi Thị Xuân, gần chợ."),
  ("Saphir Đà Lạt Hotel", "Cả ngày", "Khách sạn cổ điển kiểu lâu đài, nhiều đồ cổ, ở trung tâm."),
  ("Sammy Đà Lạt Hotel", "Cả ngày", "Khách sạn lớn trên đường Lê Hồng Phong, view đồi."),
  ("Goldient Boutique Hotel", "Cả ngày", "Khách sạn boutique phong cách Huế, có hồ bơi, phía nam trung tâm."),
  ("Terracotta Hotel & Resort", "Buổi sáng", "Resort rộng bên hồ Tuyền Lâm, có đường dạo ven hồ giữa rừng thông."),
  ("Dalat Wonder Resort", "Buổi sáng", "Resort và biệt thự view hồ Tuyền Lâm.")])
T["ru"] = _mk("Отели 4 звезды в Далате: карта 10 популярных отелей | Van Phu", "Карта отелей 4 звезды Далата",
 "Карта 10 популярных отелей и курортов Далата категории 4 звезды — восемь в центре у ночного рынка и два у озера Туйенлам — с маршрутом, расстоянием и бесплатным PDF.",
 "Здесь 10 отелей и курортов Далата категории 4 звезды, у каждого более 800 отзывов в Google Maps — восемь в центре, большинство в паре минут от ночного рынка, и два у озера Туйенлам — с маршрутом в одно касание.",
 "В городе (1–8)", "Полезно знать",
 [("Доставка", "привезём байк к вашему отелю в центре при аренде от 2 дней"), ("Курорты у озера (9–10)", "около 20 минут от города по холмам — лучше взять Air Blade 125cc"), ("Залог", "паспорт или ID-карта, без денежного залога"), ("Возврат", "верните байк до 21:00")],
 "Советы",
 ["Спросите на ресепшене, где безопасно оставить байк.", "От отелей 1–5 пару минут пешком до ночного рынка и озера Суанхыонг.", "Дороги вокруг озера Туйенлам ночью тёмные — возвращайтесь до темноты.", "Категория и цены меняются — уточняйте в отеле при бронировании."],
 [("Colline Dalat", "В любое время", "Современный отель прямо у ночного рынка и рынка Далата."),
  ("Du Parc Hotel Dalat", "В любое время", "Старинный отель в винтажном стиле на улице Чанфу, пешком до ночного рынка."),
  ("Muong Thanh Holiday Dalat", "В любое время", "Отель в старинном стиле с садом во дворе, рядом с озером и рынком."),
  ("Nesta Valley (Golf Valley) Hotel", "В любое время", "Высокий отель на улице Буйтхисуан с видом на город и парковкой сзади."),
  ("Kings Hotel Dalat", "В любое время", "Отель в центре на улице Буйтхисуан, рядом с рынком."),
  ("Saphir Dalat Hotel", "В любое время", "Классический отель в стиле замка с антиквариатом, в центре."),
  ("Sammy Dalat Hotel", "В любое время", "Большой отель на улице Лехонгфонг с видом на холмы."),
  ("Goldient Boutique Hotel", "В любое время", "Бутик-отель в стиле Хюэ с бассейном, к югу от центра."),
  ("Terracotta Hotel & Resort", "Утром", "Большой курорт у озера Туйенлам с тропой вдоль берега в сосновом лесу."),
  ("Dalat Wonder Resort", "Утром", "Курорт и виллы с видом на озеро Туйенлам.")])
T["zh"] = _mk("大叻四星级酒店：10 家热门酒店地图 | Van Phu", "大叻四星级酒店地图",
 "大叻 10 家热门四星级酒店与度假村地图——8 家在市中心夜市附近，2 家在宣林湖——附导航、距离和免费 PDF。",
 "这里是大叻 10 家四星级酒店与度假村，每家在 Google 地图上都有 800 条以上评价——8 家在市中心，大多步行即到夜市，2 家在宣林湖——一键导航。",
 "市区（1–8）", "须知",
 [("送车", "租 2 天及以上，可把车送到市中心酒店"), ("湖边度假村（9–10）", "距市区约 20 分钟，坡路多——建议骑 Air Blade 125cc"), ("押金", "押护照或身份证，不收现金押金"), ("还车", "21:00 前还车")],
 "提示",
 ["向前台询问安全的停车位置。", "1–5 号酒店步行几分钟即到夜市和春香湖。", "宣林湖周边道路夜间很暗——请在天黑前返回。", "星级和房价可能变化——订房时请向酒店确认。"],
 [("Colline Dalat", "全天", "紧邻夜市和大叻市场的现代酒店。"),
  ("Du Parc Hotel Dalat", "全天", "陈富路上的复古风老牌酒店，步行可到夜市。"),
  ("Muong Thanh Holiday Dalat", "全天", "带庭院花园的古典风格酒店，靠近湖和市场。"),
  ("Nesta Valley (Golf Valley) Hotel", "全天", "裴氏春路上的高层酒店，可看城市景观，后面有停车场。"),
  ("Kings Hotel Dalat", "全天", "裴氏春路上的市中心酒店，靠近市场。"),
  ("Saphir Dalat Hotel", "全天", "城堡风格的古典酒店，满是古董，位于市中心。"),
  ("Sammy Dalat Hotel", "全天", "黎鸿峰路上的大型酒店，可看山景。"),
  ("Goldient Boutique Hotel", "全天", "顺化风格精品酒店，有泳池，位于市中心南边。"),
  ("Terracotta Hotel & Resort", "上午", "宣林湖畔的大型度假村，松林中有湖边步道。"),
  ("Dalat Wonder Resort", "上午", "可看宣林湖景的度假村和别墅。")])
T["ko"] = _mk("달랏 4성급 호텔: 인기 호텔 10곳 지도 | Van Phu", "달랏 4성급 호텔 지도",
 "달랏의 인기 4성급 호텔·리조트 10곳 지도 — 야시장 근처 시내 8곳과 뚜엔럼 호수 2곳 — 길찾기, 거리, 무료 PDF.",
 "달랏의 4성급 호텔·리조트 10곳으로, 모두 구글 지도 리뷰가 800개 이상입니다. 시내 8곳은 대부분 야시장까지 걸어갈 수 있고, 2곳은 뚜엔럼 호수에 있습니다 — 원터치 길찾기.",
 "시내 (1–8)", "알아두세요",
 [("배달", "2일 이상 대여 시 시내 중심 호텔로 오토바이를 가져다 드립니다"), ("호수 리조트 (9–10)", "시내에서 약 20분, 언덕길 — Air Blade 125cc 추천"), ("보증", "여권 또는 신분증, 현금 보증금 없음"), ("반납", "21:00까지 반납")],
 "팁",
 ["오토바이를 안전하게 세울 곳을 리셉션에 물어보세요.", "1–5번 호텔은 야시장과 쑤언흐엉 호수까지 걸어서 몇 분입니다.", "뚜엔럼 호수 주변 도로는 밤에 어둡습니다 — 해 지기 전에 돌아오세요.", "등급과 요금은 바뀔 수 있으니 예약 시 호텔에 확인하세요."],
 [("Colline Dalat", "언제든", "야시장과 달랏 시장 바로 옆의 모던한 호텔."),
  ("Du Parc Hotel Dalat", "언제든", "쩐푸 거리의 빈티지풍 헤리티지 호텔, 야시장까지 도보."),
  ("Muong Thanh Holiday Dalat", "언제든", "안뜰 정원이 있는 클래식 스타일 호텔, 호수와 시장 근처."),
  ("Nesta Valley (Golf Valley) Hotel", "언제든", "부이티쑤언 거리의 고층 호텔, 시내 전망, 뒤편 주차장."),
  ("Kings Hotel Dalat", "언제든", "부이티쑤언 거리의 시내 호텔, 시장 근처."),
  ("Saphir Dalat Hotel", "언제든", "골동품이 가득한 성 같은 클래식 호텔, 시내 중심."),
  ("Sammy Dalat Hotel", "언제든", "레홍퐁 거리의 대형 호텔, 언덕 전망."),
  ("Goldient Boutique Hotel", "언제든", "후에 스타일 부티크 호텔, 수영장 있음, 시내 남쪽."),
  ("Terracotta Hotel & Resort", "오전", "뚜엔럼 호숫가의 넓은 리조트, 소나무 숲 호숫가 산책로."),
  ("Dalat Wonder Resort", "오전", "뚜엔럼 호수 전망의 리조트와 빌라.")])
T["ja"] = _mk("ダラットの4つ星ホテル：人気ホテル10軒の地図 | Van Phu", "ダラット4つ星ホテルマップ",
 "ダラットの人気4つ星ホテル・リゾート10軒の地図。ナイトマーケット近くの中心部に8軒、トゥエンラム湖に2軒。ルート案内・距離・無料PDF付き。",
 "ダラットの4つ星ホテル・リゾート10軒で、どこもGoogleマップの口コミが800件以上。中心部の8軒はほとんどナイトマーケットまで歩いて行け、2軒はトゥエンラム湖にあります。ワンタップでルート案内。",
 "市内（1–8）", "知っておきたいこと",
 [("配達", "2日以上のレンタルなら市中心部のホテルまでバイクをお届け"), ("湖のリゾート（9–10）", "市内から約20分、坂道が多い — Air Blade 125ccがおすすめ"), ("デポジット", "パスポートまたはIDカード、現金デポジットなし"), ("返却", "21:00までに返却")],
 "ヒント",
 ["バイクを安全に停められる場所をフロントで聞きましょう。", "1–5のホテルはナイトマーケットとスアンフーン湖まで徒歩数分。", "トゥエンラム湖周辺の道は夜は暗いので、暗くなる前に戻りましょう。", "星の等級や料金は変わることがあります — 予約時にホテルへ確認を。"],
 [("Colline Dalat", "いつでも", "ナイトマーケットとダラット市場のすぐ隣のモダンなホテル。"),
  ("Du Parc Hotel Dalat", "いつでも", "チャンフー通りのヴィンテージ調ヘリテージホテル、ナイトマーケットまで徒歩圏。"),
  ("Muong Thanh Holiday Dalat", "いつでも", "中庭の庭園があるクラシックなホテル、湖と市場の近く。"),
  ("Nesta Valley (Golf Valley) Hotel", "いつでも", "ブイティスアン通りの高層ホテル、街の眺め、裏に駐車場あり。"),
  ("Kings Hotel Dalat", "いつでも", "ブイティスアン通りの中心部のホテル、市場の近く。"),
  ("Saphir Dalat Hotel", "いつでも", "アンティークに囲まれたお城風のクラシックホテル、中心部。"),
  ("Sammy Dalat Hotel", "いつでも", "レホンフォン通りの大型ホテル、丘の眺め。"),
  ("Goldient Boutique Hotel", "いつでも", "フエ風のブティックホテル、プールあり、中心部の南。"),
  ("Terracotta Hotel & Resort", "午前", "トゥエンラム湖畔の広いリゾート、松林の湖畔遊歩道。"),
  ("Dalat Wonder Resort", "午前", "トゥエンラム湖を望むリゾートとヴィラ。")])
T["th"] = _mk("โรงแรม 4 ดาวในดาลัด: แผนที่โรงแรมยอดนิยม 10 แห่ง | Van Phu", "แผนที่โรงแรม 4 ดาวดาลัด",
 "แผนที่โรงแรมและรีสอร์ต 4 ดาวยอดนิยม 10 แห่งในดาลัด ในตัวเมืองใกล้ไนท์มาร์เก็ต 8 แห่ง และที่ทะเลสาบเตวียนเลิม 2 แห่ง พร้อมเส้นทาง ระยะทาง และ PDF ฟรี",
 "นี่คือโรงแรมและรีสอร์ต 4 ดาว 10 แห่งในดาลัด ทุกแห่งมีรีวิวบน Google Maps มากกว่า 800 รีวิว ในตัวเมือง 8 แห่ง ส่วนใหญ่เดินไปไนท์มาร์เก็ตได้ และอีก 2 แห่งที่ทะเลสาบเตวียนเลิม กดนำทางได้ทันที",
 "ในเมือง (1–8)", "ควรรู้",
 [("ส่งรถ", "เช่าตั้งแต่ 2 วัน ส่งรถถึงโรงแรมในตัวเมือง"), ("รีสอร์ตริมทะเลสาบ (9–10)", "ห่างเมืองราว 20 นาที ทางขึ้นลงเขา — แนะนำ Air Blade 125cc"), ("มัดจำ", "ฝากพาสปอร์ตหรือบัตรประชาชน ไม่มีมัดจำเงินสด"), ("คืนรถ", "คืนรถก่อน 21:00")],
 "เคล็ดลับ",
 ["ถามแผนกต้อนรับว่าจอดรถตรงไหนปลอดภัย", "โรงแรม 1–5 เดินไม่กี่นาทีถึงไนท์มาร์เก็ตและทะเลสาบซวนเฮือง", "ถนนรอบทะเลสาบเตวียนเลิมมืดตอนกลางคืน ควรกลับก่อนมืด", "ระดับดาวและราคาอาจเปลี่ยน — สอบถามโรงแรมตอนจอง"],
 [("Colline Dalat", "ทั้งวัน", "โรงแรมทันสมัยติดไนท์มาร์เก็ตและตลาดดาลัด"),
  ("Du Parc Hotel Dalat", "ทั้งวัน", "โรงแรมเก่าแก่สไตล์วินเทจบนถนนเจิ่นฟู เดินไปไนท์มาร์เก็ตได้"),
  ("Muong Thanh Holiday Dalat", "ทั้งวัน", "โรงแรมสไตล์คลาสสิกมีสวนกลางลาน ใกล้ทะเลสาบและตลาด"),
  ("Nesta Valley (Golf Valley) Hotel", "ทั้งวัน", "โรงแรมสูงบนถนนบุ่ยถิซวน วิวเมือง มีที่จอดรถด้านหลัง"),
  ("Kings Hotel Dalat", "ทั้งวัน", "โรงแรมใจกลางเมืองบนถนนบุ่ยถิซวน ใกล้ตลาด"),
  ("Saphir Dalat Hotel", "ทั้งวัน", "โรงแรมคลาสสิกสไตล์ปราสาท เต็มไปด้วยของเก่า ใจกลางเมือง"),
  ("Sammy Dalat Hotel", "ทั้งวัน", "โรงแรมใหญ่บนถนนเลห่งฟอง วิวเนินเขา"),
  ("Goldient Boutique Hotel", "ทั้งวัน", "โรงแรมบูทีคสไตล์เว้ มีสระว่ายน้ำ ทางใต้ของตัวเมือง"),
  ("Terracotta Hotel & Resort", "ช่วงเช้า", "รีสอร์ตกว้างริมทะเลสาบเตวียนเลิม มีทางเดินริมน้ำในป่าสน"),
  ("Dalat Wonder Resort", "ช่วงเช้า", "รีสอร์ตและวิลล่าวิวทะเลสาบเตวียนเลิม")])
T["id"] = _mk("Hotel Bintang 4 di Da Lat: Peta 10 Hotel Populer | Van Phu", "Peta Hotel Bintang 4 Da Lat",
 "Peta 10 hotel dan resor bintang 4 populer di Da Lat — delapan di pusat dekat pasar malam dan dua di Danau Tuyen Lam — dengan petunjuk arah, jarak, dan PDF gratis.",
 "Inilah 10 hotel dan resor bintang 4 di Da Lat, masing-masing dengan lebih dari 800 ulasan Google Maps — delapan di pusat, kebanyakan dekat jalan kaki ke pasar malam, dan dua di Danau Tuyen Lam — dengan petunjuk arah sekali ketuk.",
 "Di kota (1–8)", "Perlu diketahui",
 [("Antar motor", "kami antar motor ke hotel Anda di pusat kota untuk sewa 2 hari atau lebih"), ("Resor danau (9–10)", "sekitar 20 menit dari kota, jalan berbukit — lebih baik pakai Air Blade 125cc"), ("Jaminan", "paspor atau kartu identitas, tanpa deposit uang"), ("Pengembalian", "kembalikan motor sebelum 21:00")],
 "Tips",
 ["Tanyakan resepsionis tempat parkir motor yang aman.", "Hotel 1–5 hanya beberapa menit jalan kaki ke pasar malam dan Danau Xuan Huong.", "Jalan di sekitar Danau Tuyen Lam gelap di malam hari — kembalilah sebelum gelap.", "Peringkat bintang dan harga bisa berubah — tanyakan hotel saat memesan."],
 [("Colline Dalat", "Kapan saja", "Hotel modern tepat di sebelah pasar malam dan Pasar Da Lat."),
  ("Du Parc Hotel Dalat", "Kapan saja", "Hotel bersejarah bergaya vintage di Jalan Tran Phu, jalan kaki ke pasar malam."),
  ("Muong Thanh Holiday Dalat", "Kapan saja", "Hotel bergaya klasik dengan taman di halaman, dekat danau dan pasar."),
  ("Nesta Valley (Golf Valley) Hotel", "Kapan saja", "Hotel tinggi di Jalan Bui Thi Xuan dengan pemandangan kota dan parkir di belakang."),
  ("Kings Hotel Dalat", "Kapan saja", "Hotel di pusat kota di Jalan Bui Thi Xuan, dekat pasar."),
  ("Saphir Dalat Hotel", "Kapan saja", "Hotel klasik bergaya kastil penuh barang antik, di pusat kota."),
  ("Sammy Dalat Hotel", "Kapan saja", "Hotel besar di Jalan Le Hong Phong dengan pemandangan bukit."),
  ("Goldient Boutique Hotel", "Kapan saja", "Hotel butik bergaya Hue dengan kolam renang, di selatan pusat kota."),
  ("Terracotta Hotel & Resort", "Pagi", "Resor luas di tepi Danau Tuyen Lam dengan jalur tepi danau di hutan pinus."),
  ("Dalat Wonder Resort", "Pagi", "Resor dan vila dengan pemandangan Danau Tuyen Lam.")])
T["ms"] = _mk("Hotel 4 Bintang di Da Lat: Peta 10 Hotel Popular | Van Phu", "Peta Hotel 4 Bintang Da Lat",
 "Peta 10 hotel dan resort 4 bintang popular di Da Lat — lapan di pusat bandar dekat pasar malam dan dua di Tasik Tuyen Lam — dengan arah, jarak dan PDF percuma.",
 "Inilah 10 hotel dan resort 4 bintang di Da Lat, setiap satu dengan lebih 800 ulasan Google Maps — lapan di pusat bandar, kebanyakannya dekat berjalan kaki ke pasar malam, dan dua di Tasik Tuyen Lam — dengan arah satu ketikan.",
 "Dalam bandar (1–8)", "Perlu tahu",
 [("Hantar motosikal", "kami hantar motosikal ke hotel anda di pusat bandar untuk sewa 2 hari atau lebih"), ("Resort tasik (9–10)", "kira-kira 20 minit dari bandar, jalan berbukit — lebih baik naik Air Blade 125cc"), ("Cagaran", "pasport atau kad pengenalan, tiada deposit wang"), ("Pulangkan", "pulangkan motosikal sebelum 21:00")],
 "Tip",
 ["Tanya kaunter penyambut tetamu tempat letak motosikal yang selamat.", "Hotel 1–5 hanya beberapa minit berjalan kaki ke pasar malam dan Tasik Xuan Huong.", "Jalan di sekitar Tasik Tuyen Lam gelap pada waktu malam — pulang sebelum gelap.", "Penarafan bintang dan harga boleh berubah — semak dengan hotel semasa menempah."],
 [("Colline Dalat", "Bila-bila masa", "Hotel moden betul-betul di sebelah pasar malam dan Pasar Da Lat."),
  ("Du Parc Hotel Dalat", "Bila-bila masa", "Hotel warisan gaya vintaj di Jalan Tran Phu, berjalan kaki ke pasar malam."),
  ("Muong Thanh Holiday Dalat", "Bila-bila masa", "Hotel gaya klasik dengan taman laman dalam, dekat tasik dan pasar."),
  ("Nesta Valley (Golf Valley) Hotel", "Bila-bila masa", "Hotel tinggi di Jalan Bui Thi Xuan dengan pemandangan bandar dan tempat letak kereta di belakang."),
  ("Kings Hotel Dalat", "Bila-bila masa", "Hotel di pusat bandar di Jalan Bui Thi Xuan, dekat pasar."),
  ("Saphir Dalat Hotel", "Bila-bila masa", "Hotel klasik gaya istana lama penuh barang antik, di pusat bandar."),
  ("Sammy Dalat Hotel", "Bila-bila masa", "Hotel besar di Jalan Le Hong Phong dengan pemandangan bukit."),
  ("Goldient Boutique Hotel", "Bila-bila masa", "Hotel butik gaya Hue dengan kolam renang, di selatan pusat bandar."),
  ("Terracotta Hotel & Resort", "Pagi", "Resort luas di tepi Tasik Tuyen Lam dengan laluan tepi tasik di hutan pain."),
  ("Dalat Wonder Resort", "Pagi", "Resort dan vila dengan pemandangan Tasik Tuyen Lam.")])
T["de"] = _mk("4-Sterne-Hotels in Da Lat: Karte mit 10 beliebten Hotels | Van Phu", "Karte der 4-Sterne-Hotels in Da Lat",
 "Karte von 10 beliebten 4-Sterne-Hotels und Resorts in Da Lat — acht im Zentrum nahe dem Nachtmarkt, zwei am Tuyen-Lam-See — mit Route, Entfernung und kostenlosem PDF.",
 "Hier sind 10 Hotels und Resorts mit 4 Sternen in Da Lat, jedes mit über 800 Google-Maps-Bewertungen — acht im Zentrum, die meisten zu Fuß vom Nachtmarkt, zwei am Tuyen-Lam-See — mit Route per Fingertipp.",
 "In der Stadt (1–8)", "Gut zu wissen",
 [("Lieferung", "ab 2 Miettagen bringen wir den Roller zu Ihrem Hotel im Zentrum"), ("Seeresorts (9–10)", "etwa 20 Minuten von der Stadt, hügelige Straßen — besser mit der Air Blade 125cc"), ("Kaution", "Reisepass oder Ausweis, keine Geldkaution"), ("Rückgabe", "Roller bis 21:00 zurückbringen")],
 "Tipps",
 ["Fragen Sie an der Rezeption nach einem sicheren Parkplatz für den Roller.", "Von den Hotels 1–5 sind es nur wenige Gehminuten zum Nachtmarkt und zum Xuan-Huong-See.", "Die Straßen um den Tuyen-Lam-See sind nachts dunkel — vor Einbruch der Dunkelheit zurückfahren.", "Sterne und Preise können sich ändern — bei der Buchung beim Hotel nachfragen."],
 [("Colline Dalat", "Jederzeit", "Modernes Hotel direkt neben dem Nachtmarkt und dem Markt von Da Lat."),
  ("Du Parc Hotel Dalat", "Jederzeit", "Traditionshotel im Vintage-Stil an der Tran-Phu-Straße, zu Fuß zum Nachtmarkt."),
  ("Muong Thanh Holiday Dalat", "Jederzeit", "Hotel im klassischen Stil mit Innenhofgarten, nahe See und Markt."),
  ("Nesta Valley (Golf Valley) Hotel", "Jederzeit", "Hohes Hotel an der Bui-Thi-Xuan-Straße mit Stadtblick und Parkplatz hinten."),
  ("Kings Hotel Dalat", "Jederzeit", "Zentrales Hotel an der Bui-Thi-Xuan-Straße, nahe dem Markt."),
  ("Saphir Dalat Hotel", "Jederzeit", "Klassisches Hotel im Schlossstil voller Antiquitäten, im Zentrum."),
  ("Sammy Dalat Hotel", "Jederzeit", "Großes Hotel an der Le-Hong-Phong-Straße mit Blick auf die Hügel."),
  ("Goldient Boutique Hotel", "Jederzeit", "Boutiquehotel im Hue-Stil mit Pool, südlich des Zentrums."),
  ("Terracotta Hotel & Resort", "Morgens", "Großes Resort am Tuyen-Lam-See mit Uferweg im Kiefernwald."),
  ("Dalat Wonder Resort", "Morgens", "Resort und Villen mit Blick auf den Tuyen-Lam-See.")])
T["fr"] = _mk("Hôtels 4 étoiles à Da Lat : carte de 10 hôtels populaires | Van Phu", "Carte des hôtels 4 étoiles de Da Lat",
 "Carte de 10 hôtels et resorts 4 étoiles populaires à Da Lat — huit au centre près du marché de nuit et deux au lac Tuyen Lam — avec itinéraire, distances et PDF gratuit.",
 "Voici 10 hôtels et resorts classés 4 étoiles à Da Lat, chacun avec plus de 800 avis Google Maps — huit au centre, la plupart à pied du marché de nuit, et deux au lac Tuyen Lam — avec itinéraire en un clic.",
 "En ville (1–8)", "Bon à savoir",
 [("Livraison", "nous livrons le scooter à votre hôtel du centre-ville pour 2 jours de location ou plus"), ("Resorts du lac (9–10)", "à environ 20 minutes de la ville, routes vallonnées — mieux en Air Blade 125cc"), ("Caution", "passeport ou carte d'identité, pas de caution en argent"), ("Retour", "rendez le scooter avant 21 h")],
 "Conseils",
 ["Demandez à la réception où garer le scooter en sécurité.", "Les hôtels 1–5 sont à quelques minutes à pied du marché de nuit et du lac Xuan Huong.", "Les routes autour du lac Tuyen Lam sont sombres la nuit — rentrez avant la tombée de la nuit.", "Les étoiles et les prix peuvent changer — vérifiez auprès de l'hôtel à la réservation."],
 [("Colline Dalat", "À tout moment", "Hôtel moderne juste à côté du marché de nuit et du marché de Da Lat."),
  ("Du Parc Hotel Dalat", "À tout moment", "Hôtel historique au style rétro rue Tran Phu, à pied du marché de nuit."),
  ("Muong Thanh Holiday Dalat", "À tout moment", "Hôtel de style classique avec jardin intérieur, près du lac et du marché."),
  ("Nesta Valley (Golf Valley) Hotel", "À tout moment", "Hôtel en hauteur rue Bui Thi Xuan, vue sur la ville, parking à l'arrière."),
  ("Kings Hotel Dalat", "À tout moment", "Hôtel central rue Bui Thi Xuan, près du marché."),
  ("Saphir Dalat Hotel", "À tout moment", "Hôtel classique façon château, rempli d'antiquités, au centre."),
  ("Sammy Dalat Hotel", "À tout moment", "Grand hôtel rue Le Hong Phong avec vue sur les collines."),
  ("Goldient Boutique Hotel", "À tout moment", "Hôtel boutique inspiré de Hué, avec piscine, au sud du centre."),
  ("Terracotta Hotel & Resort", "Matin", "Grand resort au bord du lac Tuyen Lam, sentier au bord de l'eau dans les pins."),
  ("Dalat Wonder Resort", "Matin", "Resort et villas avec vue sur le lac Tuyen Lam.")])
T["es"] = _mk("Hoteles de 4 estrellas en Da Lat: mapa de 10 hoteles populares | Van Phu", "Mapa de hoteles 4 estrellas de Da Lat",
 "Mapa de 10 hoteles y resorts de 4 estrellas populares en Da Lat — ocho en el centro cerca del mercado nocturno y dos en el lago Tuyen Lam — con cómo llegar, distancias y PDF gratis.",
 "Aquí tienes 10 hoteles y resorts de 4 estrellas en Da Lat, cada uno con más de 800 reseñas en Google Maps — ocho en el centro, la mayoría a pie del mercado nocturno, y dos en el lago Tuyen Lam — con ruta en un toque.",
 "En la ciudad (1–8)", "Bueno saber",
 [("Entrega", "llevamos la moto a tu hotel del centro en alquileres de 2 días o más"), ("Resorts del lago (9–10)", "a unos 20 minutos de la ciudad, carreteras con cuestas — mejor en Air Blade 125cc"), ("Garantía", "pasaporte o documento de identidad, sin depósito en efectivo"), ("Devolución", "devuelve la moto antes de las 21:00")],
 "Consejos",
 ["Pregunta en recepción dónde aparcar la moto con seguridad.", "Los hoteles 1–5 están a pocos minutos a pie del mercado nocturno y del lago Xuan Huong.", "Las carreteras alrededor del lago Tuyen Lam están oscuras de noche — vuelve antes de que anochezca.", "Las estrellas y los precios pueden cambiar — confírmalo con el hotel al reservar."],
 [("Colline Dalat", "Cualquier hora", "Hotel moderno justo al lado del mercado nocturno y del mercado de Da Lat."),
  ("Du Parc Hotel Dalat", "Cualquier hora", "Hotel histórico de estilo vintage en la calle Tran Phu, a pie del mercado nocturno."),
  ("Muong Thanh Holiday Dalat", "Cualquier hora", "Hotel de estilo clásico con jardín interior, cerca del lago y del mercado."),
  ("Nesta Valley (Golf Valley) Hotel", "Cualquier hora", "Hotel alto en la calle Bui Thi Xuan con vistas a la ciudad y aparcamiento detrás."),
  ("Kings Hotel Dalat", "Cualquier hora", "Hotel céntrico en la calle Bui Thi Xuan, cerca del mercado."),
  ("Saphir Dalat Hotel", "Cualquier hora", "Hotel clásico estilo castillo lleno de antigüedades, en el centro."),
  ("Sammy Dalat Hotel", "Cualquier hora", "Gran hotel en la calle Le Hong Phong con vistas a las colinas."),
  ("Goldient Boutique Hotel", "Cualquier hora", "Hotel boutique inspirado en Hue, con piscina, al sur del centro."),
  ("Terracotta Hotel & Resort", "Mañana", "Gran resort junto al lago Tuyen Lam con sendero a la orilla entre pinos."),
  ("Dalat Wonder Resort", "Mañana", "Resort y villas con vistas al lago Tuyen Lam.")])
T["he"] = _mk("מלונות 4 כוכבים בדלאט: מפה של 10 מלונות פופולריים | Van Phu", "מפת מלונות 4 כוכבים בדלאט",
 "מפה של 10 מלונות ואתרי נופש פופולריים בדירוג 4 כוכבים בדלאט — שמונה במרכז ליד שוק הלילה ושניים באגם טויין לאם — עם ניווט, מרחקים ו-PDF בחינם.",
 "הנה 10 מלונות ואתרי נופש בדירוג 4 כוכבים בדלאט, לכל אחד יותר מ-800 ביקורות ב-Google Maps — שמונה במרכז, רובם במרחק הליכה משוק הלילה, ושניים באגם טויין לאם — עם ניווט בלחיצה אחת.",
 "בעיר (1–8)", "כדאי לדעת",
 [("משלוח", "בהשכרה של יומיים ומעלה נביא את הקטנוע למלון שלכם במרכז העיר"), ("אתרי נופש באגם (9–10)", "כ-20 דקות מהעיר, דרכים הרריות — עדיף Air Blade 125cc"), ("ערבון", "דרכון או תעודת זהות, בלי פיקדון כספי"), ("החזרה", "מחזירים את הקטנוע עד 21:00")],
 "טיפים",
 ["שאלו בקבלה איפה לחנות את הקטנוע בבטחה.", "ממלונות 1–5 הולכים כמה דקות לשוק הלילה ולאגם שואן הואנג.", "הדרכים סביב אגם טויין לאם חשוכות בלילה — חזרו לפני החשכה.", "דירוג הכוכבים והמחירים משתנים — בדקו מול המלון בהזמנה."],
 [("Colline Dalat", "בכל שעה", "מלון מודרני ממש ליד שוק הלילה והשוק של דלאט."),
  ("Du Parc Hotel Dalat", "בכל שעה", "מלון היסטורי בסגנון וינטג' ברחוב טראן פו, במרחק הליכה משוק הלילה."),
  ("Muong Thanh Holiday Dalat", "בכל שעה", "מלון בסגנון קלאסי עם גינה בחצר, ליד האגם והשוק."),
  ("Nesta Valley (Golf Valley) Hotel", "בכל שעה", "מלון גבוה ברחוב בוי טי שואן עם נוף לעיר וחניה מאחור."),
  ("Kings Hotel Dalat", "בכל שעה", "מלון במרכז ברחוב בוי טי שואן, ליד השוק."),
  ("Saphir Dalat Hotel", "בכל שעה", "מלון קלאסי בסגנון טירה מלא עתיקות, במרכז."),
  ("Sammy Dalat Hotel", "בכל שעה", "מלון גדול ברחוב לה הונג פונג עם נוף לגבעות."),
  ("Goldient Boutique Hotel", "בכל שעה", "מלון בוטיק בהשראת הואה עם בריכה, דרומית למרכז."),
  ("Terracotta Hotel & Resort", "בוקר", "אתר נופש גדול על שפת אגם טויין לאם עם שביל לאורך המים ביער האורנים."),
  ("Dalat Wonder Resort", "בוקר", "אתר נופש ווילות עם נוף לאגם טויין לאם.")])

from content._langs import inject as _inject
_inject(T, __name__)

# ===== 2026-11-11: owner sent a list of 20 four-star hotels/resorts (hotels_4star_dalat.json). Each was checked on Google Maps
# the same day; coordinates, place links, phones and addresses below come from Google Maps (several list coordinates were off by
# up to 3 km). Added: TTC Premium, TTC Ngoc Lan, Sandals Flora, Mi Amor, La Fleur, Saigon Dalat. Left out: MerPerle, Ana Mandara,
# Ladalat, Swiss-Belresort and Edensee (already on the 5-star map) and Grand Mercure Dalat (listed by Google as Grand Mercure,
# Accor's upscale brand — not added until its star class is confirmed). The PDF still shows the first 10, so it is hidden.
_OLD = {x[0]: x for x in SPOTS}
SPOTS = [
    _OLD["colline"],
    ("ttcpremium",  11.9418548, 108.4376529, "ChIJfd3dES8TcTERFIYekwScKx0", True, "24h"),
    ("sandalsflora", 11.9427646, 108.4371617, "ChIJU-QHpVATcTERq0vfxJfXi10", True, "24h"),
    ("ngoclan",     11.9407891, 108.4365157, "ChIJiX7FwvoTcTERRgfRUcD6gZc", True, "24h"),
    _OLD["muongthanh"], _OLD["kings"], _OLD["saphir"],
    _OLD["golfvalley"],
    ("miamor",      11.9473981, 108.4390647, "ChIJ2WVBAAATcTER59yO0cxWKWs", True, "24h"),
    _OLD["duparc"],
    ("lafleur",     11.9367744, 108.4396131, "ChIJocRfy2QTcTERziPwIj0YnCw", True, "24h"),
    _OLD["sammy"],
    ("saigon",      11.9392169, 108.4294193, "ChIJkbmJYC0TcTER7CH3wvDJ2Z8", True, "24h"),
    _OLD["goldient"],
    _OLD["terracotta"], _OLD["wonder"],
]
N = len(SPOTS); NC = N - 2
PDF = None
PHONE = {"colline": "+84 263 3665 588", "ttcpremium": "+84 263 3826 042", "sandalsflora": "+84 263 3558 816", "ngoclan": "+84 263 3838 838",
         "muongthanh": "+84 263 3578 888", "kings": "+84 263 3551 551", "saphir": "+84 862 340 468", "golfvalley": "+84 263 3697 666",
         "miamor": "+84 878 511 106", "duparc": "+84 263 3825 777", "lafleur": "+84 263 3791 999", "sammy": "+84 263 3545 454",
         "saigon": "+84 263 3556 789", "goldient": "+84 263 3662 222", "terracotta": "+84 263 3883 838", "wonder": "+84 263 3800 099"}
ADDR = {"colline": "10 Phan Bội Châu", "ttcpremium": "4 Nguyễn Thị Minh Khai", "sandalsflora": "18 Nguyễn Thị Minh Khai",
        "ngoclan": "42 Nguyễn Chí Thanh", "muongthanh": "42 Phan Bội Châu", "kings": "10 Bùi Thị Xuân", "saphir": "22–24 Phan Như Thạch",
        "golfvalley": "94 Bùi Thị Xuân", "miamor": "106 Lý Tự Trọng", "duparc": "15 Trần Phú", "lafleur": "05–07B Trần Phú",
        "sammy": "1 Lê Hồng Phong", "saigon": "180 Ba Tháng Hai", "goldient": "26 Tô Hiến Thành",
        "terracotta": "Khu 7.9, KDL hồ Tuyền Lâm", "wonder": "19 Hoa Hồng, KDL hồ Tuyền Lâm"}
AREA = {**{k: "market" for k in ("colline", "ttcpremium", "sandalsflora", "ngoclan", "muongthanh", "kings", "saphir")},
        **{k: "btx" for k in ("golfvalley", "miamor", "duparc", "lafleur")}, **{k: "out" for k in ("sammy", "saigon", "goldient")},
        **{k: "lake" for k in ("terracotta", "wonder")}}
_AL = {  # all, market, Bui Thi Xuan – Tran Phu, outside the centre, Tuyen Lam Lake, "to Van Phu"
 "vi": ("Tất cả", "Trung tâm chợ Đà Lạt", "Bùi Thị Xuân – Trần Phú", "Ngoài trung tâm", "Hồ Tuyền Lâm", "đến Văn Phú"),
 "en": ("All", "Da Lat Market centre", "Bui Thi Xuan – Tran Phu", "Outside the centre", "Tuyen Lam Lake", "to Van Phu"),
 "ru": ("Все", "Центр у рынка Далата", "Буйтхисуан – Чан Фу", "За центром", "Озеро Туйенлам", "до Van Phu"),
 "zh": ("全部", "大叻市场中心", "裴氏春 – 陈富路", "市中心外", "宣林湖", "到 Van Phu"),
 "ko": ("전체", "달랏 시장 중심", "부이티쑤언 – 쩐푸", "시내 외곽", "뚜옌럼 호수", "Van Phu까지"),
 "ja": ("すべて", "ダラット市場周辺", "ブイティスアン – チャンフー", "中心部の外", "トゥエンラム湖", "Van Phuまで"),
 "th": ("ทั้งหมด", "ใจกลางตลาดดาลัด", "บุ่ยถิซวน – เจิ่นฟู", "นอกตัวเมือง", "ทะเลสาบเตวียนเลิม", "ถึง Van Phu"),
 "id": ("Semua", "Pusat Pasar Da Lat", "Bui Thi Xuan – Tran Phu", "Luar pusat kota", "Danau Tuyen Lam", "ke Van Phu"),
 "ms": ("Semua", "Pusat Pasar Da Lat", "Bui Thi Xuan – Tran Phu", "Luar pusat bandar", "Tasik Tuyen Lam", "ke Van Phu"),
 "de": ("Alle", "Zentrum am Markt", "Bui Thi Xuan – Tran Phu", "Außerhalb des Zentrums", "Tuyen-Lam-See", "bis Van Phu"),
 "fr": ("Tous", "Centre – marché de Da Lat", "Bui Thi Xuan – Tran Phu", "Hors du centre", "Lac Tuyen Lam", "jusqu'à Van Phu"),
 "es": ("Todos", "Centro – mercado de Da Lat", "Bui Thi Xuan – Tran Phu", "Fuera del centro", "Lago Tuyen Lam", "hasta Van Phu"),
 "he": ("הכול", "מרכז השוק של דלאט", "בואי טי שואן – טראן פו", "מחוץ למרכז", "אגם טויין לאם", "עד Van Phu"),
 "it": ("Tutti", "Centro – mercato di Da Lat", "Bui Thi Xuan – Tran Phu", "Fuori dal centro", "Lago Tuyen Lam", "fino a Van Phu"),
 "nl": ("Alle", "Centrum bij de markt", "Bui Thi Xuan – Tran Phu", "Buiten het centrum", "Tuyen Lam-meer", "tot Van Phu"),
 "km": ("ទាំងអស់", "ផ្សារដាឡាត់", "Bùi Thị Xuân – Trần Phú", "ក្រៅទីក្រុង", "បឹង Tuyền Lâm", "ដល់ Van Phu"),
 "lo": ("ທັງໝົດ", "ຕະຫຼາດດາລາດ", "Bùi Thị Xuân – Trần Phú", "ນອກເມືອງ", "ທະເລສາບ Tuyền Lâm", "ຫາ Van Phu"),
 "my": ("အားလုံး", "ဒါလတ်ဈေး", "Bùi Thị Xuân – Trần Phú", "မြို့ပြင်", "Tuyền Lâm ကန်", "Van Phu သို့"),
}
def areas(l):
    a = _AL.get(l, _AL["en"])
    return [("", a[0]), ("market", a[1]), ("btx", a[2]), ("out", a[3]), ("lake", a[4])]
def toshop(l): return _AL.get(l, _AL["en"])[5]

_NEW = ["ttcpremium", "sandalsflora", "ngoclan", "miamor", "lafleur", "saigon"]
_NAME = {"ttcpremium": "TTC Hotel Premium – Dalat", "sandalsflora": "Sandals Flora Hotel", "ngoclan": "TTC Hotel – Ngọc Lan",
         "miamor": "Mi Amor Dalat by DD Hospitality", "lafleur": "La Fleur Premium Central Apartment", "saigon": "Saigon Dalat Hotel"}
_D = {
 "en": ["Large hotel at the entrance to the night market, on Nguyen Thi Minh Khai Street.",
        "Hotel on Nguyen Thi Minh Khai Street, right by the night market.",
        "Hotel on Nguyen Chi Thanh Street above the market, a short walk to the lake.",
        "Boutique hotel with a garden café on Ly Tu Trong Street, walking distance to the lake.",
        "Apartment hotel on Tran Phu Street; apartments have their own kitchen.",
        "Hotel on 3 Thang 2 Street with a pool and sauna, west of the market."],
 "vi": ["Khách sạn lớn ngay lối vào chợ đêm, trên đường Nguyễn Thị Minh Khai.",
        "Khách sạn trên đường Nguyễn Thị Minh Khai, sát chợ đêm.",
        "Khách sạn trên đường Nguyễn Chí Thanh phía trên chợ, đi bộ ra hồ.",
        "Khách sạn boutique có quán cà phê sân vườn trên đường Lý Tự Trọng, đi bộ ra hồ.",
        "Căn hộ khách sạn trên đường Trần Phú, căn hộ có bếp riêng.",
        "Khách sạn trên đường 3 Tháng 2 có hồ bơi và xông hơi, phía tây chợ."],
 "zh": ["夜市入口处的大型酒店，位于阮氏明开路。",
        "阮氏明开路上的酒店，紧挨夜市。",
        "市场上方阮志清路上的酒店，步行可到湖边。",
        "李自重路上带花园咖啡馆的精品酒店，步行可到湖边。",
        "陈富路上的公寓式酒店，公寓带独立厨房。",
        "3月2日路上有泳池和桑拿的酒店，在市场西边。"],
 "ru": ["Большой отель у входа на ночной рынок, улица Нгуен Тхи Минь Кхай.",
        "Отель на улице Нгуен Тхи Минь Кхай, прямо у ночного рынка.",
        "Отель на улице Нгуен Тьи Тхань над рынком, пешком до озера.",
        "Бутик-отель с кафе в саду на улице Ли Ты Чонг, пешком до озера.",
        "Апарт-отель на улице Чан Фу, в апартаментах есть кухня.",
        "Отель на улице 3 Тханг 2 с бассейном и сауной, западнее рынка."],
 "ko": ["응우옌티민카이 거리, 야시장 입구의 큰 호텔.",
        "야시장 바로 옆 응우옌티민카이 거리의 호텔.",
        "시장 위쪽 응우옌치타인 거리의 호텔, 호수까지 걸어서 가능.",
        "리뜨쫑 거리의 정원 카페가 있는 부티크 호텔, 호수까지 걸어서 가능.",
        "쩐푸 거리의 레지던스 호텔, 객실에 주방이 있음.",
        "시장 서쪽 3탕2 거리의 수영장·사우나가 있는 호텔."],
 "id": ["Hotel besar di pintu masuk pasar malam, Jalan Nguyen Thi Minh Khai.",
        "Hotel di Jalan Nguyen Thi Minh Khai, tepat di samping pasar malam.",
        "Hotel di Jalan Nguyen Chi Thanh di atas pasar, jalan kaki ke danau.",
        "Hotel butik dengan kafe taman di Jalan Ly Tu Trong, jalan kaki ke danau.",
        "Hotel apartemen di Jalan Tran Phu; apartemen punya dapur sendiri.",
        "Hotel di Jalan 3 Thang 2 dengan kolam renang dan sauna, di barat pasar."],
}
_TPL = {"ja": "{s}通りのホテル。", "th": "โรงแรมบนถนน {s}", "ms": "Hotel di Jalan {s}.", "de": "Hotel an der Straße {s}.",
        "fr": "Hôtel rue {s}.", "es": "Hotel en la calle {s}.", "he": "מלון ברחוב {s}.", "it": "Hotel in via {s}.",
        "nl": "Hotel aan de {s}-straat.", "km": "សណ្ឋាគារនៅផ្លូវ {s}", "lo": "ໂຮງແຮມຢູ່ຖະໜົນ {s}", "my": "{s} လမ်းရှိ ဟိုတယ်"}
def _street(sid): return ADDR[sid].split(" ", 1)[1]
_DEL = {"vi": "Văn Phú hỗ trợ giao xe máy miễn phí tận sảnh các khách sạn 4 sao tại trung tâm Đà Lạt khi thuê từ 2 ngày.",
        "en": "Van Phu delivers your scooter free of charge to the lobby of 4-star hotels in central Da Lat for rentals of 2 days or more.",
        "zh": "租车 2 天以上，Van Phu 免费把摩托车送到大叻市中心四星级酒店大堂。",
        "ru": "При аренде от 2 дней Van Phu бесплатно доставит байк к лобби 4-звёздочных отелей в центре Далата.",
        "ko": "2일 이상 렌탈하시면 Van Phu가 달랏 시내 4성급 호텔 로비까지 무료로 오토바이를 배달해 드립니다.",
        "id": "Van Phu mengantar motor gratis sampai lobi hotel bintang 4 di pusat Da Lat untuk sewa 2 hari atau lebih."}
_LEAD = {
 "vi": f"{N} khách sạn và resort 4 sao đông khách ở Đà Lạt: {NC} nơi ở trung tâm, phần lớn đi bộ ra chợ đêm, và 2 resort ven hồ Tuyền Lâm — có số điện thoại, khoảng cách tới tiệm Văn Phú và nút chỉ đường. " + _DEL["vi"],
 "en": f"{N} popular 4-star hotels and resorts in Da Lat: {NC} in town, most a short walk from the night market, and 2 by Tuyen Lam Lake — with phone numbers, distance to our shop and one-tap directions. " + _DEL["en"],
 "zh": f"大叻 {N} 家热门四星级酒店和度假村：{NC} 家在市区，大多步行可到夜市，2 家在宣林湖边——附电话、到 Van Phu 店的距离和一键导航。" + _DEL["zh"],
 "ru": f"{N} популярных отелей и курортов 4 звезды в Далате: {NC} в городе, большинство в паре минут от ночного рынка, и 2 у озера Туйенлам — с телефонами, расстоянием до нашей мастерской и маршрутом в одно касание. " + _DEL["ru"],
 "ko": f"달랏의 인기 4성급 호텔·리조트 {N}곳: 시내 {NC}곳(대부분 야시장까지 도보)과 뚜옌럼 호숫가 2곳 — 전화번호, Van Phu 가게까지 거리, 원터치 길찾기 포함. " + _DEL["ko"],
 "id": f"{N} hotel dan resor bintang 4 populer di Da Lat: {NC} di kota, sebagian besar dekat pasar malam, dan 2 di Danau Tuyen Lam — lengkap dengan nomor telepon, jarak ke toko kami dan petunjuk arah sekali ketuk. " + _DEL["id"],
 "ja": f"ダラットの人気4つ星ホテル・リゾート{N}軒：市内{NC}軒とトゥエンラム湖畔2軒。電話番号、Van Phuまでの距離、ワンタップのルート案内付き。",
 "th": f"โรงแรมและรีสอร์ต 4 ดาวยอดนิยม {N} แห่งในดาลัด: ในเมือง {NC} แห่ง และริมทะเลสาบเตวียนเลิม 2 แห่ง พร้อมเบอร์โทร ระยะทางถึงร้าน Van Phu และปุ่มนำทาง",
 "ms": f"{N} hotel dan resort 4 bintang yang popular di Da Lat: {NC} di bandar dan 2 di Tasik Tuyen Lam — dengan nombor telefon, jarak ke kedai kami dan arah satu ketikan.",
 "de": f"{N} beliebte 4-Sterne-Hotels und Resorts in Da Lat: {NC} in der Stadt und 2 am Tuyen-Lam-See — mit Telefonnummer, Entfernung zu unserem Laden und Route per Fingertipp.",
 "fr": f"{N} hôtels et resorts 4 étoiles populaires à Da Lat : {NC} en ville et 2 au lac Tuyen Lam — avec téléphone, distance jusqu'à notre boutique et itinéraire en un clic.",
 "es": f"{N} hoteles y resorts populares de 4 estrellas en Da Lat: {NC} en la ciudad y 2 junto al lago Tuyen Lam — con teléfono, distancia a nuestra tienda y ruta en un toque.",
 "he": f"{N} מלונות ואתרי נופש פופולריים בדירוג 4 כוכבים בדלאט: {NC} בעיר ו-2 ליד אגם טויין לאם — עם מספרי טלפון, מרחק לחנות שלנו וניווט בלחיצה אחת.",
 "it": f"{N} hotel e resort 4 stelle molto richiesti a Da Lat: {NC} in città e 2 sul lago Tuyen Lam — con telefono, distanza dal nostro negozio e indicazioni con un tocco.",
 "nl": f"{N} populaire 4-sterrenhotels en resorts in Da Lat: {NC} in de stad en 2 aan het Tuyen Lam-meer — met telefoonnummer, afstand tot onze winkel en route met één tik.",
}
_TITLE = {"en": f"4-Star Hotels in Da Lat: Map of {N} Hotels & Resorts | Van Phu",
          "vi": f"Khách sạn 4 sao Đà Lạt: bản đồ {N} khách sạn và resort, có số điện thoại | Văn Phú",
          "zh": f"大叻四星级酒店：{N} 家酒店和度假村地图（附电话） | Van Phu",
          "ru": f"Отели 4 звезды в Далате: карта {N} отелей и курортов | Van Phu",
          "ko": f"달랏 4성급 호텔: 호텔·리조트 {N}곳 지도 | Van Phu",
          "id": f"Hotel Bintang 4 di Da Lat: Peta {N} Hotel & Resor | Van Phu"}
_DESC = {"en": f"Map of {N} popular 4-star hotels and resorts in Da Lat — in town near the night market and by Tuyen Lam Lake — with phone numbers, distance to Van Phu and directions.",
         "vi": f"Bản đồ {N} khách sạn và resort 4 sao Đà Lạt — trung tâm chợ đêm và ven hồ Tuyền Lâm — có số điện thoại, khoảng cách tới Văn Phú và chỉ đường.",
         "zh": f"大叻 {N} 家四星级酒店和度假村地图——夜市一带和宣林湖边——附电话、到 Van Phu 的距离和导航。",
         "ru": f"Карта {N} отелей и курортов 4 звезды в Далате — у ночного рынка и у озера Туйенлам — с телефонами, расстоянием до Van Phu и маршрутом.",
         "ko": f"달랏 4성급 호텔·리조트 {N}곳 지도 — 야시장 주변과 뚜옌럼 호숫가 — 전화번호, Van Phu까지 거리, 길찾기.",
         "id": f"Peta {N} hotel dan resor bintang 4 di Da Lat — dekat pasar malam dan di Danau Tuyen Lam — dengan nomor telepon, jarak ke Van Phu dan petunjuk arah."}
import re as _re
for _l in LANGS:
    t = T[_l]; anytime = t["s"]["colline"][1]
    for i, sid in enumerate(_NEW):
        t["s"][sid] = (_NAME[sid], anytime, _D[_l][i] if _l in _D else _TPL[_l].format(s=_street(sid)))
    t["title"] = _TITLE.get(_l) or _re.sub(r"(?<!\d)10(?!\d)", str(N), t["title"])
    t["desc"] = _DESC.get(_l) or _re.sub(r"(?<!\d)8(?!\d)", str(NC), _re.sub(r"(?<!\d)10(?!\d)", str(N), t["desc"]))
    if _l in _LEAD:
        t["lead"] = _LEAD[_l]
    else:  # km, lo, my: drop the "800+ reviews each" clause and update counts
        ld = t["lead"]
        for cut in ["នីមួយៗមានមតិលើស 800 នៅលើ Google Maps ", "ແຕ່ລະແຫ່ງມີຣີວິວຫຼາຍກວ່າ 800 ໃນ Google Maps ", "၊ တစ်ခုစီတွင် Google Maps သုံးသပ်ချက် 800 ကျော် ရှိသည်"]:
            ld = ld.replace(cut, "")
        assert "800" not in ld, _l
        t["lead"] = _re.sub(r"(?<!\d)8(?!\d)", str(NC), _re.sub(r"(?<!\d)10(?!\d)", str(N), ld))
    t["center"] = t["center"].replace("1–8", f"1–{NC}")
    t["season"] = [(a.replace("9–10", f"{NC + 1}–{N}"), b) for a, b in t["season"]]
    t["tips"] = [x.replace("1–5", "1–7") for x in t["tips"]]
    assert f"1–{NC}" in t["center"] and any(f"{NC + 1}–{N}" in a for a, _ in t["season"]), _l
for _l in LANGS:  # no PDF while it is hidden; reuse the new lead as description where no description was written
    if _l in _LEAD and _l not in _DESC:
        T[_l]["desc"] = _LEAD[_l]
    T[_l]["desc"] = T[_l]["desc"].replace(" និង PDF ឥតគិតថ្លៃ", "").replace(" ແລະ PDF ຟຣີ", "").replace("၊ အကွာအဝေးနှင့် PDF အခမဲ့", "နှင့် အကွာအဝေး")
    assert "PDF" not in T[_l]["desc"] + T[_l]["title"] + T[_l]["lead"], _l
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"colline": "Colline Hotel", "duparc": "Du Parc Hotel", "muongthanh": "Mường Thanh Holiday", "golfvalley": "Nesta Valley Golf Valley Hotel",
      "kings": "Kings Hotel", "saphir": "Saphir Hotel", "sammy": "Sammy Hotel", "goldient": "Goldient Boutique Hotel",
      "terracotta": "Terracotta Hotel Resort", "wonder": "Dalat Wonder Resort"}
_Q.update(_NAME)
def img_link(sid):
    """Temporary photo link: Google Images search for the hotel name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
