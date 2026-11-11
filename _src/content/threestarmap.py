"""Da Lat 3-star hotels map — shared data for the website page (/3-star-hotels-map/) and the printable PDF.
First 8 hotels: listed as 3-star by at least two travel sources (mia.vn, vietnambooking.com, agotourist.com, tourdalattravel.com,
Oct 2026), with 250+ Google Maps reviews; coordinates and place links (cid) taken from Google Maps on 2026-10-14.
Expanded to 23 on 2026-11-11 from the owner's list (see the block after _inject)."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (reception)
SPOTS = [
    ("ngocphat",   11.9376231, 108.4439463, "10108612022680929948", True, "24h"),
    ("iris",       11.9410146, 108.4336734, "17595584161299827193", True, "24h"),
    ("dulys",      11.9407917, 108.4346003, "2788549472951622892",  True, "24h"),
    ("roydala",    11.9406411, 108.4355364, "12718554076507123743", True, "24h"),
    ("marguerite", 11.9412421, 108.4364376, "15508391104840311404", True, "24h"),
    ("maivang",    11.9420054, 108.4316465, "5025561373797321540",  True, "24h"),
    ("kyhoa",      11.9683652, 108.4438086, "15643657310000291558", True, "24h"),
    ("decharme",   11.9325602, 108.4645702, "12454287519585639178", True, "24h"),
]
CENTER = _PM.CENTER
SLUG = "3-star-hotels-map"
PDF = "VanPhu-Dalat-3-Star-Hotels-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 8
LEGW = 280
MAPH = 560
H1PT = 22
MAXKM = 4.0
RINGS = (1, 2, 3)
SIDE = {}
JITTER = {"maivang": (-14, -16), "iris": (-22, 12), "dulys": (-4, 26), "roydala": (18, 20), "marguerite": (20, -10), "kyhoa": (34, 8)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("3-Star Hotels in Da Lat: Map of 8 Popular Hotels | Van Phu", "Da Lat 3-Star Hotels Map",
 "Map of 8 popular 3-star hotels in Da Lat — most a short walk from the night market and Xuan Huong Lake — with directions, distances and a free PDF.",
 "Here are 8 hotels listed as 3-star in Da Lat, each with 250+ Google Maps reviews — six in the centre near the night market and two quieter ones a short ride out — with one-tap directions.",
 "In town (1–8)", "Good to know",
 [("Delivery", "we bring the scooter to your hotel in the city centre for rentals of 2 days or more"), ("Centre (1–6)", "all within walking distance of the night market and Xuan Huong Lake"), ("Deposit", "passport or ID card, no cash deposit"), ("Return", "bring the scooter back by 21:00")],
 "Tips",
 ["Ask reception where to park the scooter safely.", "Many 3-star hotels have no air-conditioning — Da Lat is cool, but ask for a fan if needed.", "Rooms on the street side can be noisy — ask for a higher floor.", "Star ratings and prices change — check with the hotel when you book."],
 [("Ngoc Phat Dalat Hotel", "Any time", "Hotel across from Lam Vien Square, some rooms with lake views."),
  ("Iris Dalat Hotel", "Any time", "Hotel on Phan Nhu Thach Street, a short walk from the night market."),
  ("Hotel Du Lys", "Any time", "Hotel on Nam Ky Khoi Nghia Street, minutes from the market and restaurants."),
  ("Hotel Roy Dala", "Any time", "Hotel with a marble lobby and large rooms, walking distance to the market and lake."),
  ("Marguerite Hotel", "Any time", "Spacious rooms on Nguyen Chi Thanh Street, across from the night market."),
  ("Mai Vang Hotel", "Any time", "Simple hotel on Hai Thuong Street, about 5 minutes to the night market."),
  ("Ky Hoa Garden Villages Hotel", "Any time", "French-style villas with gardens, north of the centre."),
  ("Dalat De Charme Village", "Sunset", "Themed rooms and a terraced garden, east of the centre.")])
T["vi"] = _mk("Khách sạn 3 sao Đà Lạt: bản đồ 8 khách sạn đông khách | Văn Phú", "Bản đồ khách sạn 3 sao Đà Lạt",
 "Bản đồ 8 khách sạn 3 sao đông khách ở Đà Lạt — phần lớn đi bộ ra chợ đêm và hồ Xuân Hương — có chỉ đường, khoảng cách và PDF miễn phí.",
 "Đây là 8 khách sạn được xếp hạng 3 sao ở Đà Lạt, nơi nào cũng có trên 250 đánh giá Google Maps — 6 nơi ở trung tâm gần chợ đêm và 2 nơi yên tĩnh hơn, đi xe một đoạn ngắn — có nút chỉ đường.",
 "Trong thành phố (1–8)", "Nên biết",
 [("Giao xe", "giao xe tận khách sạn trong trung tâm khi thuê từ 2 ngày"), ("Trung tâm (1–6)", "đều đi bộ được ra chợ đêm và hồ Xuân Hương"), ("Đặt cọc", "giữ hộ chiếu hoặc CCCD, không cọc tiền"), ("Trả xe", "trả xe trước 21:00")],
 "Lưu ý",
 ["Hỏi lễ tân chỗ để xe an toàn.", "Nhiều khách sạn 3 sao không có máy lạnh — Đà Lạt mát, cần thì xin thêm quạt.", "Phòng mặt đường có thể ồn — nên xin tầng cao.", "Hạng sao và giá phòng có thể thay đổi — hỏi khách sạn khi đặt phòng."],
 [("Khách sạn Ngọc Phát", "Cả ngày", "Khách sạn đối diện quảng trường Lâm Viên, có phòng view hồ."),
  ("Iris Dalat Hotel", "Cả ngày", "Khách sạn trên đường Phan Như Thạch, đi bộ vài phút ra chợ đêm."),
  ("Hotel Du Lys", "Cả ngày", "Khách sạn trên đường Nam Kỳ Khởi Nghĩa, gần chợ và quán ăn."),
  ("Hotel Roy Dala", "Cả ngày", "Sảnh lát đá cẩm thạch, phòng rộng, đi bộ ra chợ và hồ."),
  ("Khách sạn Marguerite", "Cả ngày", "Phòng rộng trên đường Nguyễn Chí Thanh, đối diện chợ đêm."),
  ("Khách sạn Mai Vàng", "Cả ngày", "Khách sạn đơn giản trên đường Hải Thượng, khoảng 5 phút ra chợ đêm."),
  ("Kỳ Hòa Garden Villages", "Cả ngày", "Biệt thự kiểu Pháp có sân vườn, phía bắc trung tâm."),
  ("Dalat De Charme Village", "Hoàng hôn", "Phòng thiết kế theo chủ đề, vườn bậc thang, phía đông trung tâm.")])
T["ru"] = _mk("Отели 3 звезды в Далате: карта 8 популярных отелей | Van Phu", "Карта отелей 3 звезды Далата",
 "Карта 8 популярных отелей Далата категории 3 звезды — большинство в нескольких минутах от ночного рынка и озера Суанхыонг — с маршрутом, расстоянием и бесплатным PDF.",
 "Здесь 8 отелей Далата категории 3 звезды, у каждого более 250 отзывов в Google Maps — шесть в центре у ночного рынка и два потише, недалеко от центра — с маршрутом в одно касание.",
 "В городе (1–8)", "Полезно знать",
 [("Доставка", "привезём байк к вашему отелю в центре при аренде от 2 дней"), ("Центр (1–6)", "все в пешей доступности от ночного рынка и озера Суанхыонг"), ("Залог", "паспорт или ID-карта, без денежного залога"), ("Возврат", "верните байк до 21:00")],
 "Советы",
 ["Спросите на ресепшене, где безопасно оставить байк.", "Во многих отелях 3 звезды нет кондиционера — в Далате прохладно, при необходимости попросите вентилятор.", "Номера с окнами на улицу бывают шумными — просите этаж повыше.", "Категория и цены меняются — уточняйте в отеле при бронировании."],
 [("Ngoc Phat Dalat Hotel", "В любое время", "Отель напротив площади Ламвьен, в части номеров вид на озеро."),
  ("Iris Dalat Hotel", "В любое время", "Отель на улице Фаннятхать, пара минут пешком до ночного рынка."),
  ("Hotel Du Lys", "В любое время", "Отель на улице Намкикхоингиа, рядом с рынком и кафе."),
  ("Hotel Roy Dala", "В любое время", "Мраморное лобби и большие номера, пешком до рынка и озера."),
  ("Marguerite Hotel", "В любое время", "Просторные номера на улице Нгуенчитхань, напротив ночного рынка."),
  ("Mai Vang Hotel", "В любое время", "Простой отель на улице Хайтхыонг, около 5 минут до ночного рынка."),
  ("Ky Hoa Garden Villages Hotel", "В любое время", "Виллы во французском стиле с садами, к северу от центра."),
  ("Dalat De Charme Village", "Закат", "Тематические номера и сад на террасах, к востоку от центра.")])
T["zh"] = _mk("大叻三星级酒店：8 家热门酒店地图 | Van Phu", "大叻三星级酒店地图",
 "大叻 8 家热门三星级酒店地图——大多步行即到夜市和春香湖——附导航、距离和免费 PDF。",
 "这里是大叻 8 家三星级酒店，每家在 Google 地图上都有 250 条以上评价——6 家在市中心夜市附近，2 家稍远一点、更安静——一键导航。",
 "市区（1–8）", "须知",
 [("送车", "租 2 天及以上，可把车送到市中心酒店"), ("市中心（1–6）", "步行即可到夜市和春香湖"), ("押金", "押护照或身份证，不收现金押金"), ("还车", "21:00 前还车")],
 "提示",
 ["向前台询问安全的停车位置。", "很多三星级酒店没有空调——大叻天气凉爽，需要时可以要风扇。", "临街房间可能较吵——可要求高楼层。", "星级和房价可能变化——订房时请向酒店确认。"],
 [("Ngoc Phat Dalat Hotel", "全天", "林园广场对面的酒店，部分房间可看湖景。"),
  ("Iris Dalat Hotel", "全天", "范如石路上的酒店，步行几分钟到夜市。"),
  ("Hotel Du Lys", "全天", "南圻起义路上的酒店，靠近市场和餐馆。"),
  ("Hotel Roy Dala", "全天", "大理石大堂、房间宽敞，步行可到市场和湖边。"),
  ("Marguerite Hotel", "全天", "阮志清路上的宽敞客房，就在夜市对面。"),
  ("Mai Vang Hotel", "全天", "海上路上的简单酒店，到夜市约 5 分钟。"),
  ("Ky Hoa Garden Villages Hotel", "全天", "带花园的法式别墅，位于市中心北边。"),
  ("Dalat De Charme Village", "日落", "主题客房和梯田花园，位于市中心东边。")])
T["ko"] = _mk("달랏 3성급 호텔: 인기 호텔 8곳 지도 | Van Phu", "달랏 3성급 호텔 지도",
 "달랏의 인기 3성급 호텔 8곳 지도 — 대부분 야시장과 쑤언흐엉 호수까지 걸어갈 수 있는 곳 — 길찾기, 거리, 무료 PDF.",
 "달랏의 3성급 호텔 8곳으로, 모두 구글 지도 리뷰가 250개 이상입니다. 6곳은 야시장 근처 시내, 2곳은 조금 떨어진 조용한 곳 — 원터치 길찾기.",
 "시내 (1–8)", "알아두세요",
 [("배달", "2일 이상 대여 시 시내 중심 호텔로 오토바이를 가져다 드립니다"), ("시내 중심 (1–6)", "모두 야시장과 쑤언흐엉 호수까지 걸어갈 수 있습니다"), ("보증", "여권 또는 신분증, 현금 보증금 없음"), ("반납", "21:00까지 반납")],
 "팁",
 ["오토바이를 안전하게 세울 곳을 리셉션에 물어보세요.", "3성급 호텔은 에어컨이 없는 곳이 많아요 — 달랏은 시원하지만 필요하면 선풍기를 요청하세요.", "길가 쪽 방은 시끄러울 수 있으니 높은 층을 요청하세요.", "등급과 요금은 바뀔 수 있으니 예약 시 호텔에 확인하세요."],
 [("Ngoc Phat Dalat Hotel", "언제든", "럼비엔 광장 맞은편 호텔, 일부 객실 호수 전망."),
  ("Iris Dalat Hotel", "언제든", "판뉴탁 거리의 호텔, 야시장까지 걸어서 몇 분."),
  ("Hotel Du Lys", "언제든", "남끼커이응이아 거리의 호텔, 시장과 식당 근처."),
  ("Hotel Roy Dala", "언제든", "대리석 로비와 넓은 객실, 시장과 호수까지 도보."),
  ("Marguerite Hotel", "언제든", "응우옌찌타인 거리의 넓은 객실, 야시장 맞은편."),
  ("Mai Vang Hotel", "언제든", "하이트엉 거리의 소박한 호텔, 야시장까지 약 5분."),
  ("Ky Hoa Garden Villages Hotel", "언제든", "정원이 있는 프랑스풍 빌라, 시내 북쪽."),
  ("Dalat De Charme Village", "해 질 녘", "테마 객실과 계단식 정원, 시내 동쪽.")])
T["ja"] = _mk("ダラットの3つ星ホテル：人気ホテル8軒の地図 | Van Phu", "ダラット3つ星ホテルマップ",
 "ダラットの人気3つ星ホテル8軒の地図。ほとんどがナイトマーケットやスアンフーン湖まで徒歩圏。ルート案内・距離・無料PDF付き。",
 "ダラットの3つ星ホテル8軒で、どこもGoogleマップの口コミが250件以上。6軒はナイトマーケット近くの中心部、2軒は少し離れた静かな場所です。ワンタップでルート案内。",
 "市内（1–8）", "知っておきたいこと",
 [("配達", "2日以上のレンタルなら市中心部のホテルまでバイクをお届け"), ("中心部（1–6）", "どこもナイトマーケットとスアンフーン湖まで徒歩圏"), ("デポジット", "パスポートまたはIDカード、現金デポジットなし"), ("返却", "21:00までに返却")],
 "ヒント",
 ["バイクを安全に停められる場所をフロントで聞きましょう。", "3つ星ホテルはエアコンがないことも多いです — ダラットは涼しいですが、必要なら扇風機を頼みましょう。", "通り側の部屋はうるさいことがあるので、高層階を頼みましょう。", "星の等級や料金は変わることがあります — 予約時にホテルへ確認を。"],
 [("Ngoc Phat Dalat Hotel", "いつでも", "ラムヴィエン広場の向かいのホテル、湖が見える部屋も。"),
  ("Iris Dalat Hotel", "いつでも", "ファンニュータック通りのホテル、ナイトマーケットまで徒歩数分。"),
  ("Hotel Du Lys", "いつでも", "ナムキーコイギア通りのホテル、市場や食堂の近く。"),
  ("Hotel Roy Dala", "いつでも", "大理石のロビーと広い客室、市場と湖まで徒歩圏。"),
  ("Marguerite Hotel", "いつでも", "グエンチータン通りの広い客室、ナイトマーケットの向かい。"),
  ("Mai Vang Hotel", "いつでも", "ハイトゥオン通りのシンプルなホテル、ナイトマーケットまで約5分。"),
  ("Ky Hoa Garden Villages Hotel", "いつでも", "庭のあるフランス風ヴィラ、中心部の北。"),
  ("Dalat De Charme Village", "夕暮れ", "テーマ別の客室と段々の庭園、中心部の東。")])
T["th"] = _mk("โรงแรม 3 ดาวในดาลัด: แผนที่โรงแรมยอดนิยม 8 แห่ง | Van Phu", "แผนที่โรงแรม 3 ดาวดาลัด",
 "แผนที่โรงแรม 3 ดาวยอดนิยม 8 แห่งในดาลัด ส่วนใหญ่เดินไปไนท์มาร์เก็ตและทะเลสาบซวนเฮืองได้ พร้อมเส้นทาง ระยะทาง และ PDF ฟรี",
 "นี่คือโรงแรม 3 ดาว 8 แห่งในดาลัด ทุกแห่งมีรีวิวบน Google Maps มากกว่า 250 รีวิว ในใจกลางเมืองใกล้ไนท์มาร์เก็ต 6 แห่ง และอีก 2 แห่งที่เงียบกว่า ขี่รถไม่ไกล กดนำทางได้ทันที",
 "ในเมือง (1–8)", "ควรรู้",
 [("ส่งรถ", "เช่าตั้งแต่ 2 วัน ส่งรถถึงโรงแรมในตัวเมือง"), ("ใจกลางเมือง (1–6)", "ทุกแห่งเดินไปไนท์มาร์เก็ตและทะเลสาบซวนเฮืองได้"), ("มัดจำ", "ฝากพาสปอร์ตหรือบัตรประชาชน ไม่มีมัดจำเงินสด"), ("คืนรถ", "คืนรถก่อน 21:00")],
 "เคล็ดลับ",
 ["ถามแผนกต้อนรับว่าจอดรถตรงไหนปลอดภัย", "โรงแรม 3 ดาวหลายแห่งไม่มีแอร์ — ดาลัดอากาศเย็น แต่ขอพัดลมได้ถ้าต้องการ", "ห้องติดถนนอาจเสียงดัง — ขอชั้นสูง", "ระดับดาวและราคาอาจเปลี่ยน — สอบถามโรงแรมตอนจอง"],
 [("Ngoc Phat Dalat Hotel", "ทั้งวัน", "โรงแรมตรงข้ามจัตุรัสลัมเวียน บางห้องเห็นวิวทะเลสาบ"),
  ("Iris Dalat Hotel", "ทั้งวัน", "โรงแรมบนถนนฟานนูทัค เดินไม่กี่นาทีถึงไนท์มาร์เก็ต"),
  ("Hotel Du Lys", "ทั้งวัน", "โรงแรมบนถนนนามกีคอยเงีย ใกล้ตลาดและร้านอาหาร"),
  ("Hotel Roy Dala", "ทั้งวัน", "ล็อบบี้หินอ่อน ห้องกว้าง เดินไปตลาดและทะเลสาบได้"),
  ("Marguerite Hotel", "ทั้งวัน", "ห้องกว้างบนถนนเหงียนชีทาน ตรงข้ามไนท์มาร์เก็ต"),
  ("Mai Vang Hotel", "ทั้งวัน", "โรงแรมเรียบง่ายบนถนนไห่เทือง ราว 5 นาทีถึงไนท์มาร์เก็ต"),
  ("Ky Hoa Garden Villages Hotel", "ทั้งวัน", "วิลล่าสไตล์ฝรั่งเศสมีสวน ทางเหนือของตัวเมือง"),
  ("Dalat De Charme Village", "พระอาทิตย์ตก", "ห้องพักตามธีมและสวนขั้นบันได ทางตะวันออกของตัวเมือง")])
T["id"] = _mk("Hotel Bintang 3 di Da Lat: Peta 8 Hotel Populer | Van Phu", "Peta Hotel Bintang 3 Da Lat",
 "Peta 8 hotel bintang 3 populer di Da Lat — kebanyakan dekat jalan kaki ke pasar malam dan Danau Xuan Huong — dengan petunjuk arah, jarak, dan PDF gratis.",
 "Inilah 8 hotel bintang 3 di Da Lat, masing-masing dengan lebih dari 250 ulasan Google Maps — enam di pusat dekat pasar malam dan dua yang lebih tenang tak jauh dari pusat — dengan petunjuk arah sekali ketuk.",
 "Di kota (1–8)", "Perlu diketahui",
 [("Antar motor", "kami antar motor ke hotel Anda di pusat kota untuk sewa 2 hari atau lebih"), ("Pusat kota (1–6)", "semuanya dekat jalan kaki ke pasar malam dan Danau Xuan Huong"), ("Jaminan", "paspor atau kartu identitas, tanpa deposit uang"), ("Pengembalian", "kembalikan motor sebelum 21:00")],
 "Tips",
 ["Tanyakan resepsionis tempat parkir motor yang aman.", "Banyak hotel bintang 3 tanpa AC — Da Lat sejuk, tapi mintalah kipas jika perlu.", "Kamar menghadap jalan bisa bising — mintalah lantai atas.", "Peringkat bintang dan harga bisa berubah — tanyakan hotel saat memesan."],
 [("Ngoc Phat Dalat Hotel", "Kapan saja", "Hotel di seberang Lapangan Lam Vien, sebagian kamar menghadap danau."),
  ("Iris Dalat Hotel", "Kapan saja", "Hotel di Jalan Phan Nhu Thach, beberapa menit jalan kaki ke pasar malam."),
  ("Hotel Du Lys", "Kapan saja", "Hotel di Jalan Nam Ky Khoi Nghia, dekat pasar dan tempat makan."),
  ("Hotel Roy Dala", "Kapan saja", "Lobi marmer dan kamar luas, jalan kaki ke pasar dan danau."),
  ("Marguerite Hotel", "Kapan saja", "Kamar luas di Jalan Nguyen Chi Thanh, di seberang pasar malam."),
  ("Mai Vang Hotel", "Kapan saja", "Hotel sederhana di Jalan Hai Thuong, sekitar 5 menit ke pasar malam."),
  ("Ky Hoa Garden Villages Hotel", "Kapan saja", "Vila bergaya Prancis dengan taman, di utara pusat kota."),
  ("Dalat De Charme Village", "Matahari terbenam", "Kamar bertema dan taman berteras, di timur pusat kota.")])
T["ms"] = _mk("Hotel 3 Bintang di Da Lat: Peta 8 Hotel Popular | Van Phu", "Peta Hotel 3 Bintang Da Lat",
 "Peta 8 hotel 3 bintang popular di Da Lat — kebanyakannya dekat berjalan kaki ke pasar malam dan Tasik Xuan Huong — dengan arah, jarak dan PDF percuma.",
 "Inilah 8 hotel 3 bintang di Da Lat, setiap satu dengan lebih 250 ulasan Google Maps — enam di pusat bandar dekat pasar malam dan dua yang lebih tenang tidak jauh dari pusat — dengan arah satu ketikan.",
 "Dalam bandar (1–8)", "Perlu tahu",
 [("Hantar motosikal", "kami hantar motosikal ke hotel anda di pusat bandar untuk sewa 2 hari atau lebih"), ("Pusat bandar (1–6)", "semuanya dekat berjalan kaki ke pasar malam dan Tasik Xuan Huong"), ("Cagaran", "pasport atau kad pengenalan, tiada deposit wang"), ("Pulangkan", "pulangkan motosikal sebelum 21:00")],
 "Tip",
 ["Tanya kaunter penyambut tetamu tempat letak motosikal yang selamat.", "Banyak hotel 3 bintang tiada penghawa dingin — Da Lat sejuk, tetapi minta kipas jika perlu.", "Bilik menghadap jalan boleh bising — minta tingkat atas.", "Penarafan bintang dan harga boleh berubah — semak dengan hotel semasa menempah."],
 [("Ngoc Phat Dalat Hotel", "Bila-bila masa", "Hotel bertentangan Dataran Lam Vien, sesetengah bilik menghadap tasik."),
  ("Iris Dalat Hotel", "Bila-bila masa", "Hotel di Jalan Phan Nhu Thach, beberapa minit berjalan kaki ke pasar malam."),
  ("Hotel Du Lys", "Bila-bila masa", "Hotel di Jalan Nam Ky Khoi Nghia, dekat pasar dan kedai makan."),
  ("Hotel Roy Dala", "Bila-bila masa", "Lobi marmar dan bilik luas, berjalan kaki ke pasar dan tasik."),
  ("Marguerite Hotel", "Bila-bila masa", "Bilik luas di Jalan Nguyen Chi Thanh, bertentangan pasar malam."),
  ("Mai Vang Hotel", "Bila-bila masa", "Hotel ringkas di Jalan Hai Thuong, kira-kira 5 minit ke pasar malam."),
  ("Ky Hoa Garden Villages Hotel", "Bila-bila masa", "Vila gaya Perancis dengan taman, di utara pusat bandar."),
  ("Dalat De Charme Village", "Matahari terbenam", "Bilik bertema dan taman bertingkat, di timur pusat bandar.")])
T["de"] = _mk("3-Sterne-Hotels in Da Lat: Karte mit 8 beliebten Hotels | Van Phu", "Karte der 3-Sterne-Hotels in Da Lat",
 "Karte von 8 beliebten 3-Sterne-Hotels in Da Lat — die meisten zu Fuß vom Nachtmarkt und vom Xuan-Huong-See — mit Route, Entfernung und kostenlosem PDF.",
 "Hier sind 8 Hotels mit 3 Sternen in Da Lat, jedes mit über 250 Google-Maps-Bewertungen — sechs im Zentrum nahe dem Nachtmarkt und zwei ruhigere etwas außerhalb — mit Route per Fingertipp.",
 "In der Stadt (1–8)", "Gut zu wissen",
 [("Lieferung", "ab 2 Miettagen bringen wir den Roller zu Ihrem Hotel im Zentrum"), ("Zentrum (1–6)", "alle zu Fuß vom Nachtmarkt und vom Xuan-Huong-See erreichbar"), ("Kaution", "Reisepass oder Ausweis, keine Geldkaution"), ("Rückgabe", "Roller bis 21:00 zurückbringen")],
 "Tipps",
 ["Fragen Sie an der Rezeption nach einem sicheren Parkplatz für den Roller.", "Viele 3-Sterne-Hotels haben keine Klimaanlage — Da Lat ist kühl, bei Bedarf nach einem Ventilator fragen.", "Zimmer zur Straße können laut sein — nach einem höheren Stockwerk fragen.", "Sterne und Preise können sich ändern — bei der Buchung beim Hotel nachfragen."],
 [("Ngoc Phat Dalat Hotel", "Jederzeit", "Hotel gegenüber dem Lam-Vien-Platz, manche Zimmer mit Seeblick."),
  ("Iris Dalat Hotel", "Jederzeit", "Hotel an der Phan-Nhu-Thach-Straße, wenige Gehminuten zum Nachtmarkt."),
  ("Hotel Du Lys", "Jederzeit", "Hotel an der Nam-Ky-Khoi-Nghia-Straße, nahe Markt und Restaurants."),
  ("Hotel Roy Dala", "Jederzeit", "Marmorlobby und große Zimmer, zu Fuß zum Markt und zum See."),
  ("Marguerite Hotel", "Jederzeit", "Geräumige Zimmer an der Nguyen-Chi-Thanh-Straße, gegenüber dem Nachtmarkt."),
  ("Mai Vang Hotel", "Jederzeit", "Einfaches Hotel an der Hai-Thuong-Straße, etwa 5 Minuten zum Nachtmarkt."),
  ("Ky Hoa Garden Villages Hotel", "Jederzeit", "Villen im französischen Stil mit Gärten, nördlich des Zentrums."),
  ("Dalat De Charme Village", "Sonnenuntergang", "Themenzimmer und Terrassengarten, östlich des Zentrums.")])
T["fr"] = _mk("Hôtels 3 étoiles à Da Lat : carte de 8 hôtels populaires | Van Phu", "Carte des hôtels 3 étoiles de Da Lat",
 "Carte de 8 hôtels 3 étoiles populaires à Da Lat — la plupart à pied du marché de nuit et du lac Xuan Huong — avec itinéraire, distances et PDF gratuit.",
 "Voici 8 hôtels classés 3 étoiles à Da Lat, chacun avec plus de 250 avis Google Maps — six au centre près du marché de nuit et deux plus calmes un peu à l'écart — avec itinéraire en un clic.",
 "En ville (1–8)", "Bon à savoir",
 [("Livraison", "nous livrons le scooter à votre hôtel du centre-ville pour 2 jours de location ou plus"), ("Centre (1–6)", "tous à pied du marché de nuit et du lac Xuan Huong"), ("Caution", "passeport ou carte d'identité, pas de caution en argent"), ("Retour", "rendez le scooter avant 21 h")],
 "Conseils",
 ["Demandez à la réception où garer le scooter en sécurité.", "Beaucoup d'hôtels 3 étoiles n'ont pas de climatisation — Da Lat est frais, demandez un ventilateur si besoin.", "Les chambres côté rue peuvent être bruyantes — demandez un étage élevé.", "Les étoiles et les prix peuvent changer — vérifiez auprès de l'hôtel à la réservation."],
 [("Ngoc Phat Dalat Hotel", "À tout moment", "Hôtel face à la place Lam Vien, certaines chambres avec vue sur le lac."),
  ("Iris Dalat Hotel", "À tout moment", "Hôtel rue Phan Nhu Thach, à quelques minutes à pied du marché de nuit."),
  ("Hotel Du Lys", "À tout moment", "Hôtel rue Nam Ky Khoi Nghia, près du marché et des restaurants."),
  ("Hotel Roy Dala", "À tout moment", "Hall en marbre et grandes chambres, à pied du marché et du lac."),
  ("Marguerite Hotel", "À tout moment", "Chambres spacieuses rue Nguyen Chi Thanh, face au marché de nuit."),
  ("Mai Vang Hotel", "À tout moment", "Hôtel simple rue Hai Thuong, à environ 5 minutes du marché de nuit."),
  ("Ky Hoa Garden Villages Hotel", "À tout moment", "Villas de style français avec jardins, au nord du centre."),
  ("Dalat De Charme Village", "Coucher du soleil", "Chambres à thème et jardin en terrasses, à l'est du centre.")])
T["es"] = _mk("Hoteles de 3 estrellas en Da Lat: mapa de 8 hoteles populares | Van Phu", "Mapa de hoteles 3 estrellas de Da Lat",
 "Mapa de 8 hoteles de 3 estrellas populares en Da Lat — la mayoría a pie del mercado nocturno y del lago Xuan Huong — con cómo llegar, distancias y PDF gratis.",
 "Aquí tienes 8 hoteles de 3 estrellas en Da Lat, cada uno con más de 250 reseñas en Google Maps — seis en el centro cerca del mercado nocturno y dos más tranquilos a poca distancia — con ruta en un toque.",
 "En la ciudad (1–8)", "Bueno saber",
 [("Entrega", "llevamos la moto a tu hotel del centro en alquileres de 2 días o más"), ("Centro (1–6)", "todos a pie del mercado nocturno y del lago Xuan Huong"), ("Garantía", "pasaporte o documento de identidad, sin depósito en efectivo"), ("Devolución", "devuelve la moto antes de las 21:00")],
 "Consejos",
 ["Pregunta en recepción dónde aparcar la moto con seguridad.", "Muchos hoteles de 3 estrellas no tienen aire acondicionado — Da Lat es fresco, pide un ventilador si lo necesitas.", "Las habitaciones a la calle pueden ser ruidosas — pide un piso alto.", "Las estrellas y los precios pueden cambiar — confírmalo con el hotel al reservar."],
 [("Ngoc Phat Dalat Hotel", "Cualquier hora", "Hotel frente a la plaza Lam Vien, algunas habitaciones con vista al lago."),
  ("Iris Dalat Hotel", "Cualquier hora", "Hotel en la calle Phan Nhu Thach, a pocos minutos a pie del mercado nocturno."),
  ("Hotel Du Lys", "Cualquier hora", "Hotel en la calle Nam Ky Khoi Nghia, cerca del mercado y de restaurantes."),
  ("Hotel Roy Dala", "Cualquier hora", "Vestíbulo de mármol y habitaciones grandes, a pie del mercado y del lago."),
  ("Marguerite Hotel", "Cualquier hora", "Habitaciones amplias en la calle Nguyen Chi Thanh, frente al mercado nocturno."),
  ("Mai Vang Hotel", "Cualquier hora", "Hotel sencillo en la calle Hai Thuong, a unos 5 minutos del mercado nocturno."),
  ("Ky Hoa Garden Villages Hotel", "Cualquier hora", "Villas de estilo francés con jardines, al norte del centro."),
  ("Dalat De Charme Village", "Atardecer", "Habitaciones temáticas y jardín en terrazas, al este del centro.")])
T["he"] = _mk("מלונות 3 כוכבים בדלאט: מפה של 8 מלונות פופולריים | Van Phu", "מפת מלונות 3 כוכבים בדלאט",
 "מפה של 8 מלונות פופולריים בדירוג 3 כוכבים בדלאט — רובם במרחק הליכה משוק הלילה ומאגם שואן הואנג — עם ניווט, מרחקים ו-PDF בחינם.",
 "הנה 8 מלונות בדירוג 3 כוכבים בדלאט, לכל אחד יותר מ-250 ביקורות ב-Google Maps — שישה במרכז ליד שוק הלילה ושניים שקטים יותר במרחק נסיעה קצרה — עם ניווט בלחיצה אחת.",
 "בעיר (1–8)", "כדאי לדעת",
 [("משלוח", "בהשכרה של יומיים ומעלה נביא את הקטנוע למלון שלכם במרכז העיר"), ("מרכז (1–6)", "כולם במרחק הליכה משוק הלילה ומאגם שואן הואנג"), ("ערבון", "דרכון או תעודת זהות, בלי פיקדון כספי"), ("החזרה", "מחזירים את הקטנוע עד 21:00")],
 "טיפים",
 ["שאלו בקבלה איפה לחנות את הקטנוע בבטחה.", "בהרבה מלונות 3 כוכבים אין מזגן — בדלאט קריר, אבל אפשר לבקש מאוורר.", "חדרים לכיוון הרחוב עלולים להיות רועשים — בקשו קומה גבוהה.", "דירוג הכוכבים והמחירים משתנים — בדקו מול המלון בהזמנה."],
 [("Ngoc Phat Dalat Hotel", "בכל שעה", "מלון מול כיכר לאם וייאן, בחלק מהחדרים נוף לאגם."),
  ("Iris Dalat Hotel", "בכל שעה", "מלון ברחוב פאן נו טאך, כמה דקות הליכה משוק הלילה."),
  ("Hotel Du Lys", "בכל שעה", "מלון ברחוב נאם קי חוי נגיה, ליד השוק והמסעדות."),
  ("Hotel Roy Dala", "בכל שעה", "לובי שיש וחדרים גדולים, במרחק הליכה מהשוק והאגם."),
  ("Marguerite Hotel", "בכל שעה", "חדרים מרווחים ברחוב נגוין צ'י טאן, מול שוק הלילה."),
  ("Mai Vang Hotel", "בכל שעה", "מלון פשוט ברחוב האי טואנג, כ-5 דקות משוק הלילה."),
  ("Ky Hoa Garden Villages Hotel", "בכל שעה", "וילות בסגנון צרפתי עם גינות, צפונית למרכז."),
  ("Dalat De Charme Village", "שקיעה", "חדרים בעיצוב נושאי וגינה מדורגת, מזרחית למרכז.")])

from content._langs import inject as _inject
_inject(T, __name__)

# ===== 2026-11-11: owner sent a list of 22 central hotels (hotels_3star_dalat.json). Each was checked on Google Maps the same day:
# coordinates, place links, phone numbers and addresses below come from Google Maps (the list's own coordinates were off by
# 100 m – 1 km, so its "distance to Van Phu" was not used; distances are computed). Left out: Nesta Valley (4-star, already on
# the 4-star map) and three hotels not found on Google Maps (Thanh Do, Nature Hotel Nam Ky Khoi Nghia, Kim Oanh Orchids).
# Descriptions only state facts from the address and Google Maps listing. Star class is as listed by the owner / travel sites.
# The printable PDF still shows the first 8 hotels, so the PDF button is hidden until the PDF is redrawn.
_OLD = {x[0]: x for x in SPOTS}
SPOTS = [
    ("lerecit",    11.9474226, 108.4400863, "ChIJI87FgBETcTERDEKKi09-W0U", True, "24h"),
    ("marigold",   11.9459600, 108.4395578, "ChIJt5-t5MYTcTERh0ODVE4qMT4", True, "24h"),
    ("dreamlux",   11.9461778, 108.4402173, "ChIJpYdulE8TcTERZ8Kl4Lh0mcI", True, "24h"),
    ("naturepbc",  11.9446966, 108.4380153, "ChIJ0bHRAQATcTERy2rTNU2ywHs", True, "24h"),
    ("sandals",    11.9439546, 108.4337711, "ChIJaWcKe6QTcTERdQyqM8N-xxc", True, "24h"),
    ("westernhill", 11.9456162, 108.4346376, "ChIJufFRaikTcTERXx_YV-0i7ws", True, "24h"),
    ("minhnguyen", 11.9455570, 108.4343117, "ChIJa33VyC8TcTERUE7NGoChaCg", True, "24h"),
    _OLD["dulys"], _OLD["roydala"], _OLD["iris"], _OLD["marguerite"], _OLD["maivang"],
    ("tuongvy",    11.9411115, 108.4335289, "ChIJcbZBsMYTcTER5IVTlEIm9a0", True, "24h"),
    ("tulip",      11.9412800, 108.4341530, "ChIJ71IbPZcTcTER_zwsLgp_Xyk", True, "24h"),
    ("bombo",      11.9418662, 108.4350328, "ChIJn_gGnKITcTERzU3HfQ2S2XI", True, "24h"),
    ("wisteria",   11.9384054, 108.4387095, "ChIJtZQBsC8TcTERZn6K2alzklQ", True, "24h"),
    ("plaza",      11.9385305, 108.4380433, "ChIJJT9I7y8TcTER6xZ6NIvBiow", True, "24h"),
    _OLD["ngocphat"],
    ("dview",      11.9358619, 108.4374510, "ChIJP1hnMwATcTERFIYLK_uBRrU", True, "24h"),
    ("lutan",      11.9351245, 108.4417162, "ChIJPe-AVzoTcTERxzQ_ip02ObU", True, "6:00–23:00"),
    ("naturelt",   11.9322043, 108.4422776, "ChIJka-fb88TcTERAPGGsuuQ-xA", True, "24h"),
    _OLD["kyhoa"], _OLD["decharme"],
]
N = len(SPOTS); NC = N - 2
PDF = None
PHONE = {"lerecit": "+84 263 3638 668", "marigold": "+84 263 3956 666", "dreamlux": "+84 263 3588 880", "naturepbc": "+84 816 525 626",
         "sandals": "+84 912 541 616", "westernhill": "+84 263 3565 888", "minhnguyen": "+84 263 3668 891", "dulys": "+84 263 3838 163",
         "roydala": "+84 263 3636 677", "iris": "+84 263 3593 456", "marguerite": "+84 263 3822 758", "maivang": "+84 263 3511 162",
         "tuongvy": "+84 909 605 563", "tulip": "+84 263 7302 468", "bombo": "+84 978 497 809", "wisteria": "+84 263 3697 968",
         "plaza": "+84 263 6252 999", "ngocphat": "+84 263 3683 979", "dview": "+84 865 467 079", "lutan": "+84 937 530 909",
         "naturelt": "+84 816 525 626", "kyhoa": "+84 263 3555 215", "decharme": "+84 263 6506 999"}
ADDR = {"lerecit": "117 Bùi Thị Xuân", "marigold": "83 Bùi Thị Xuân", "dreamlux": "72 Bùi Thị Xuân", "naturepbc": "77/4 Phan Bội Châu",
        "sandals": "83 Phan Đình Phùng", "westernhill": "135–145 Phan Đình Phùng", "minhnguyen": "145/1 Phan Đình Phùng",
        "dulys": "14 Nam Kỳ Khởi Nghĩa", "roydala": "10A Nam Kỳ Khởi Nghĩa", "iris": "20 Phan Như Thạch", "marguerite": "30–32 Nguyễn Chí Thanh",
        "maivang": "A1–A2 Hải Thượng", "tuongvy": "46 Phan Như Thạch", "tulip": "53–55 Phan Như Thạch", "bombo": "20 Phan Như Thạch",
        "wisteria": "5–6 Lê Đại Hành", "plaza": "19 Lê Đại Hành", "ngocphat": "10 Hồ Tùng Mậu", "dview": "15D Trần Phú",
        "lutan": "2/25 Trần Hưng Đạo", "naturelt": "52 Lương Thế Vinh", "kyhoa": "211–217 Phù Đổng Thiên Vương", "decharme": "94 Hoàng Hoa Thám"}
AREA = {**{k: "btx" for k in ("lerecit", "marigold", "dreamlux", "naturepbc")}, **{k: "pdp" for k in ("sandals", "westernhill", "minhnguyen")},
        **{k: "market" for k in ("dulys", "roydala", "iris", "marguerite", "maivang", "tuongvy", "tulip", "bombo")},
        **{k: "lake" for k in ("wisteria", "plaza", "ngocphat", "dview", "lutan", "naturelt")}, **{k: "out" for k in ("kyhoa", "decharme")}}
_AL = {  # all, night market area, Le Dai Hanh – lake, outside the centre, "to Van Phu"
 "vi": ("Tất cả", "Chợ đêm – Nam Kỳ Khởi Nghĩa", "Lê Đại Hành – hồ Xuân Hương", "Ngoài trung tâm", "đến Văn Phú"),
 "en": ("All", "Night market – Nam Ky Khoi Nghia", "Le Dai Hanh – the lake", "Outside the centre", "to Van Phu"),
 "ru": ("Все", "Ночной рынок – Намки Хойнгиа", "Ле Дай Хань – озеро", "За центром", "до Van Phu"),
 "zh": ("全部", "夜市 – 南圻起义路", "黎大行路 – 春香湖", "市中心外", "到 Van Phu"),
 "ko": ("전체", "야시장 – 남끼커이응이아", "레다이한 – 호수", "시내 외곽", "Van Phu까지"),
 "ja": ("すべて", "ナイトマーケット周辺", "レダイハイン通り・湖", "中心部の外", "Van Phuまで"),
 "th": ("ทั้งหมด", "ไนท์มาร์เก็ต", "ถนนเลได่หั่ญ – ทะเลสาบ", "นอกตัวเมือง", "ถึง Van Phu"),
 "id": ("Semua", "Pasar malam – Nam Ky Khoi Nghia", "Le Dai Hanh – danau", "Luar pusat kota", "ke Van Phu"),
 "ms": ("Semua", "Pasar malam – Nam Ky Khoi Nghia", "Le Dai Hanh – tasik", "Luar pusat bandar", "ke Van Phu"),
 "de": ("Alle", "Nachtmarkt – Nam Ky Khoi Nghia", "Le Dai Hanh – See", "Außerhalb des Zentrums", "bis Van Phu"),
 "fr": ("Tous", "Marché de nuit – Nam Ky Khoi Nghia", "Le Dai Hanh – le lac", "Hors du centre", "jusqu'à Van Phu"),
 "es": ("Todos", "Mercado nocturno – Nam Ky Khoi Nghia", "Le Dai Hanh – el lago", "Fuera del centro", "hasta Van Phu"),
 "he": ("הכול", "שוק הלילה – נאם קי קוי נגיה", "לה דאי האן – האגם", "מחוץ למרכז", "עד Van Phu"),
 "it": ("Tutti", "Mercato notturno – Nam Ky Khoi Nghia", "Le Dai Hanh – il lago", "Fuori dal centro", "fino a Van Phu"),
 "nl": ("Alle", "Avondmarkt – Nam Ky Khoi Nghia", "Le Dai Hanh – het meer", "Buiten het centrum", "tot Van Phu"),
 "km": ("ទាំងអស់", "ផ្សាររាត្រី", "Lê Đại Hành – បឹង", "ក្រៅទីក្រុង", "ដល់ Van Phu"),
 "lo": ("ທັງໝົດ", "ຕະຫຼາດກາງຄືນ", "Lê Đại Hành – ໜອງ", "ນອກເມືອງ", "ຫາ Van Phu"),
 "my": ("အားလုံး", "ညဈေး", "Lê Đại Hành – ကန်", "မြို့ပြင်", "Van Phu သို့"),
}
def areas(l):
    a = _AL.get(l, _AL["en"])
    return [("", a[0]), ("btx", "Bùi Thị Xuân"), ("pdp", "Phan Đình Phùng"), ("market", a[1]), ("lake", a[2]), ("out", a[3])]
def toshop(l): return _AL.get(l, _AL["en"])[4]

_NEW = ["lerecit", "marigold", "dreamlux", "naturepbc", "sandals", "westernhill", "minhnguyen", "tuongvy", "tulip", "bombo",
        "wisteria", "plaza", "dview", "lutan", "naturelt"]
_NAME = {"lerecit": "Le Récit Boutique Hôtel de Dalat", "marigold": "Marigold Hotel Dalat", "dreamlux": "Dream Luxury Hotel",
         "naturepbc": "Nature Hotel – Phan Bội Châu", "sandals": "Sandals Camellia Hotel", "westernhill": "The Western Hill Hotel",
         "minhnguyen": "Minh Nguyên 145 Hotel", "tuongvy": "Tường Vy Dalat Central", "tulip": "Tulip City View Hotel",
         "bombo": "Bom Bo Dalat Hotel", "wisteria": "Wisteria Hotel", "plaza": "Dalat Plaza Hotel", "dview": "D View Hotel",
         "lutan": "Lữ Tấn Hotel", "naturelt": "Nature Hotel – Lương Thế Vinh"}
_D = {
 "en": ["Boutique hotel on Bui Thi Xuan Street, walking distance to cafés and restaurants.",
        "Large hotel on Bui Thi Xuan Street with 24-hour reception, close to the centre.",
        "Hotel on Bui Thi Xuan Street with parking, a short walk to the night market.",
        "Small hotel in an alley off Phan Boi Chau Street, close to Da Lat Market.",
        "Hotel on Phan Dinh Phung Street, a busy street full of local eateries.",
        "Hotel with a restaurant on Phan Dinh Phung Street, in the middle of a food area.",
        "Small hotel in an alley off Phan Dinh Phung Street, quiet but close to food streets.",
        "Budget hotel on Phan Nhu Thach Street, a few minutes' walk to Da Lat Market.",
        "Hotel on Phan Nhu Thach Street with 24-hour reception, near the night market.",
        "Hotel on a quieter stretch of Phan Nhu Thach Street, 5–10 minutes' walk to the night market.",
        "Small hotel on Le Dai Hanh Street, close to the lake and the night market.",
        "Hotel on Le Dai Hanh Street across from a park, under 10 minutes' walk to the night market.",
        "Small hotel in an alley off Tran Phu Street, about 5 minutes' walk to the lake.",
        "Quiet hotel with a garden in an alley off Tran Hung Dao Street.",
        "Hotel on Luong The Vinh Street, south of the centre and quieter than the market area."],
 "vi": ["Khách sạn boutique trên đường Bùi Thị Xuân, đi bộ ra quán cà phê và quán ăn.",
        "Khách sạn lớn trên đường Bùi Thị Xuân, lễ tân 24/24, gần trung tâm.",
        "Khách sạn trên đường Bùi Thị Xuân, có chỗ để xe, đi bộ ra chợ đêm.",
        "Khách sạn nhỏ trong hẻm Phan Bội Châu, gần chợ Đà Lạt.",
        "Khách sạn trên đường Phan Đình Phùng, con phố nhiều quán ăn địa phương.",
        "Khách sạn có nhà hàng trên đường Phan Đình Phùng, ngay khu ăn uống.",
        "Khách sạn nhỏ trong hẻm Phan Đình Phùng, yên tĩnh nhưng gần phố ăn uống.",
        "Khách sạn bình dân trên đường Phan Như Thạch, đi bộ vài phút ra chợ Đà Lạt.",
        "Khách sạn trên đường Phan Như Thạch, lễ tân 24/24, gần chợ đêm.",
        "Khách sạn trên đoạn yên tĩnh của đường Phan Như Thạch, đi bộ 5–10 phút ra chợ đêm.",
        "Khách sạn nhỏ trên đường Lê Đại Hành, gần hồ và chợ đêm.",
        "Khách sạn trên đường Lê Đại Hành, đối diện công viên, đi bộ chưa đến 10 phút ra chợ đêm.",
        "Khách sạn nhỏ trong hẻm Trần Phú, đi bộ khoảng 5 phút ra hồ.",
        "Khách sạn yên tĩnh có sân vườn trong hẻm Trần Hưng Đạo.",
        "Khách sạn trên đường Lương Thế Vinh, phía nam trung tâm, yên tĩnh hơn khu chợ."],
 "zh": ["裴氏春路上的精品酒店，步行可到咖啡馆和餐厅。",
        "裴氏春路上的大型酒店，24小时前台，靠近市中心。",
        "裴氏春路上的酒店，有停车位，步行可到夜市。",
        "潘佩珠路小巷里的小酒店，靠近大叻市场。",
        "潘庭逢路上的酒店，这条街有很多本地小吃店。",
        "潘庭逢路上带餐厅的酒店，就在美食区中间。",
        "潘庭逢路小巷里的小酒店，安静又靠近美食街。",
        "潘如石路上的经济型酒店，步行几分钟到大叻市场。",
        "潘如石路上的酒店，24小时前台，靠近夜市。",
        "位于潘如石路较安静路段的酒店，步行5–10分钟到夜市。",
        "黎大行路上的小酒店，靠近春香湖和夜市。",
        "黎大行路上的酒店，对面是公园，步行不到10分钟到夜市。",
        "陈富路小巷里的小酒店，步行约5分钟到湖边。",
        "陈兴道路小巷里带花园的安静酒店。",
        "梁世荣路上的酒店，在市中心南边，比市场一带安静。"],
 "ru": ["Бутик-отель на улице Буйтхисуан, кафе и рестораны в пешей доступности.",
        "Большой отель на улице Буйтхисуан, круглосуточная стойка, рядом с центром.",
        "Отель на улице Буйтхисуан с парковкой, пешком до ночного рынка.",
        "Небольшой отель в переулке улицы Фан Бой Тяу, рядом с рынком Далата.",
        "Отель на улице Фан Динь Фунг, где много местных кафе.",
        "Отель с рестораном на улице Фан Динь Фунг, в самой гастрономической зоне.",
        "Небольшой отель в переулке улицы Фан Динь Фунг: тихо, но рядом улицы с едой.",
        "Недорогой отель на улице Фан Ньы Тхать, несколько минут пешком до рынка Далата.",
        "Отель на улице Фан Ньы Тхать, круглосуточная стойка, рядом ночной рынок.",
        "Отель на тихом участке улицы Фан Ньы Тхать, 5–10 минут пешком до ночного рынка.",
        "Небольшой отель на улице Ле Дай Хань, рядом озеро и ночной рынок.",
        "Отель на улице Ле Дай Хань напротив парка, меньше 10 минут пешком до ночного рынка.",
        "Небольшой отель в переулке улицы Чан Фу, около 5 минут пешком до озера.",
        "Тихий отель с садом в переулке улицы Чан Хынг Дао.",
        "Отель на улице Лыонг Тхе Винь, южнее центра и тише района рынка."],
 "ko": ["부이티쑤언 거리의 부티크 호텔, 카페와 식당까지 걸어서 가능.",
        "부이티쑤언 거리의 큰 호텔, 24시간 프런트, 시내 가까움.",
        "부이티쑤언 거리의 호텔, 주차 가능, 야시장까지 걸어서 가능.",
        "판보이쩌우 거리 골목 안의 작은 호텔, 달랏 시장 가까움.",
        "현지 식당이 많은 판딘풍 거리의 호텔.",
        "판딘풍 거리 먹거리 구역 한가운데의 레스토랑이 있는 호텔.",
        "판딘풍 거리 골목 안의 작은 호텔, 조용하지만 먹자골목 가까움.",
        "판뉴탁 거리의 저렴한 호텔, 달랏 시장까지 걸어서 몇 분.",
        "판뉴탁 거리의 호텔, 24시간 프런트, 야시장 가까움.",
        "판뉴탁 거리의 조용한 구간에 있는 호텔, 야시장까지 걸어서 5–10분.",
        "레다이한 거리의 작은 호텔, 호수와 야시장 가까움.",
        "공원 맞은편 레다이한 거리의 호텔, 야시장까지 걸어서 10분 이내.",
        "쩐푸 거리 골목 안의 작은 호텔, 호수까지 걸어서 약 5분.",
        "쩐흥다오 거리 골목 안의 정원이 있는 조용한 호텔.",
        "르엉테빈 거리의 호텔, 시내 남쪽으로 시장 주변보다 조용함."],
 "id": ["Hotel butik di Jalan Bui Thi Xuan, jalan kaki ke kafe dan restoran.",
        "Hotel besar di Jalan Bui Thi Xuan, resepsionis 24 jam, dekat pusat kota.",
        "Hotel di Jalan Bui Thi Xuan dengan tempat parkir, jalan kaki ke pasar malam.",
        "Hotel kecil di gang Jalan Phan Boi Chau, dekat Pasar Da Lat.",
        "Hotel di Jalan Phan Dinh Phung, jalan yang penuh warung makan lokal.",
        "Hotel dengan restoran di Jalan Phan Dinh Phung, di tengah kawasan kuliner.",
        "Hotel kecil di gang Jalan Phan Dinh Phung, tenang tapi dekat jalan kuliner.",
        "Hotel hemat di Jalan Phan Nhu Thach, beberapa menit jalan kaki ke Pasar Da Lat.",
        "Hotel di Jalan Phan Nhu Thach, resepsionis 24 jam, dekat pasar malam.",
        "Hotel di bagian Jalan Phan Nhu Thach yang lebih tenang, 5–10 menit jalan kaki ke pasar malam.",
        "Hotel kecil di Jalan Le Dai Hanh, dekat danau dan pasar malam.",
        "Hotel di Jalan Le Dai Hanh di seberang taman, kurang dari 10 menit jalan kaki ke pasar malam.",
        "Hotel kecil di gang Jalan Tran Phu, sekitar 5 menit jalan kaki ke danau.",
        "Hotel tenang dengan taman di gang Jalan Tran Hung Dao.",
        "Hotel di Jalan Luong The Vinh, di selatan pusat kota dan lebih tenang dari area pasar."],
}
_TPL = {  # short automatic description for languages outside the 6 focus languages: street from the Google Maps address
 "ja": "{s}通りのホテル。", "th": "โรงแรมบนถนน {s}", "ms": "Hotel di Jalan {s}.", "de": "Hotel an der Straße {s}.",
 "fr": "Hôtel rue {s}.", "es": "Hotel en la calle {s}.", "he": "מלון ברחוב {s}.", "it": "Hotel in via {s}.",
 "nl": "Hotel aan de {s}-straat.", "km": "សណ្ឋាគារនៅផ្លូវ {s}", "lo": "ໂຮງແຮມຢູ່ຖະໜົນ {s}", "my": "{s} လမ်းရှိ ဟိုတယ်",
}
def _street(sid):
    a = ADDR[sid]; return a.split(" ", 1)[1] if a[0].isdigit() or a[:2] == "A1" else a
_LEAD = {
 "en": f"{N} popular 3-star and mid-range hotels in Da Lat, grouped by street — Bui Thi Xuan, Phan Dinh Phung, the night market and Le Dai Hanh by the lake — with phone numbers, distance to our shop and one-tap directions. Tap a pin to call the hotel or get directions.",
 "vi": f"{N} khách sạn 3 sao và tầm trung đông khách ở Đà Lạt, chia theo khu — Bùi Thị Xuân, Phan Đình Phùng, chợ đêm và Lê Đại Hành cạnh hồ — có số điện thoại, khoảng cách tới tiệm Văn Phú và nút chỉ đường. Bấm vào ghim để gọi khách sạn hoặc chỉ đường.",
 "zh": f"大叻 {N} 家热门三星级及中档酒店，按街区分组——裴氏春路、潘庭逢路、夜市一带和湖边的黎大行路——附电话、到 Van Phu 店的距离和一键导航。点地图上的图钉可直接打电话或导航。",
 "ru": f"{N} популярных отелей 3 звезды и среднего класса в Далате, по районам — Буйтхисуан, Фан Динь Фунг, ночной рынок и Ле Дай Хань у озера — с телефонами, расстоянием до нашей мастерской и маршрутом в одно касание. Нажмите на метку, чтобы позвонить в отель или построить маршрут.",
 "ko": f"달랏의 인기 3성급·중급 호텔 {N}곳을 거리별로 정리했습니다 — 부이티쑤언, 판딘풍, 야시장 주변, 호숫가 레다이한. 전화번호, Van Phu 가게까지 거리, 원터치 길찾기 포함. 지도의 핀을 누르면 바로 전화하거나 길찾기를 할 수 있습니다.",
 "id": f"{N} hotel bintang 3 dan kelas menengah populer di Da Lat, dikelompokkan per jalan — Bui Thi Xuan, Phan Dinh Phung, pasar malam dan Le Dai Hanh di tepi danau — lengkap dengan nomor telepon, jarak ke toko kami dan petunjuk arah sekali ketuk. Ketuk pin untuk menelepon hotel atau membuka rute.",
 "ja": f"ダラットの人気3つ星・中級ホテル{N}軒を通りごとにまとめました。電話番号、Van Phuまでの距離、ワンタップのルート案内付き。",
 "th": f"โรงแรม 3 ดาวและระดับกลางยอดนิยม {N} แห่งในดาลัด แบ่งตามถนน พร้อมเบอร์โทร ระยะทางถึงร้าน Van Phu และปุ่มนำทาง",
 "ms": f"{N} hotel 3 bintang dan pertengahan yang popular di Da Lat, mengikut jalan — dengan nombor telefon, jarak ke kedai kami dan arah satu ketikan.",
 "de": f"{N} beliebte 3-Sterne- und Mittelklassehotels in Da Lat, nach Straßen geordnet — mit Telefonnummer, Entfernung zu unserem Laden und Route per Fingertipp.",
 "fr": f"{N} hôtels 3 étoiles et de gamme moyenne populaires à Da Lat, classés par rue — avec téléphone, distance jusqu'à notre boutique et itinéraire en un clic.",
 "es": f"{N} hoteles populares de 3 estrellas y gama media en Da Lat, agrupados por calle — con teléfono, distancia a nuestra tienda y ruta en un toque.",
 "he": f"{N} מלונות פופולריים בדירוג 3 כוכבים ובטווח הביניים בדלאט, לפי רחובות — עם מספרי טלפון, מרחק לחנות שלנו וניווט בלחיצה אחת.",
 "it": f"{N} hotel 3 stelle e di fascia media molto richiesti a Da Lat, divisi per via — con telefono, distanza dal nostro negozio e indicazioni con un tocco.",
 "nl": f"{N} populaire 3-sterren- en middenklassehotels in Da Lat, per straat — met telefoonnummer, afstand tot onze winkel en route met één tik.",
}
_TITLE = {
 "en": f"3-Star Hotels in Da Lat: Map of {N} Hotels by Street | Van Phu",
 "vi": f"Khách sạn 3 sao Đà Lạt: bản đồ {N} khách sạn theo khu, có số điện thoại | Văn Phú",
 "zh": f"大叻三星级酒店：{N} 家酒店地图（按街区，附电话） | Van Phu",
 "ru": f"Отели 3 звезды в Далате: карта {N} отелей по районам | Van Phu",
 "ko": f"달랏 3성급 호텔: 거리별 호텔 {N}곳 지도 | Van Phu",
 "id": f"Hotel Bintang 3 di Da Lat: Peta {N} Hotel per Jalan | Van Phu",
}
_DESC = {
 "en": f"Map of {N} popular 3-star hotels in Da Lat by street (Bui Thi Xuan, Phan Dinh Phung, night market, Le Dai Hanh) with phone numbers, distance to Van Phu and directions.",
 "vi": f"Bản đồ {N} khách sạn 3 sao Đà Lạt theo khu (Bùi Thị Xuân, Phan Đình Phùng, chợ đêm, Lê Đại Hành): số điện thoại, khoảng cách tới Văn Phú và chỉ đường.",
 "zh": f"大叻 {N} 家三星级酒店地图，按街区分组（裴氏春、潘庭逢、夜市、黎大行），附电话、到 Van Phu 的距离和导航。",
 "ru": f"Карта {N} отелей 3 звезды в Далате по районам (Буйтхисуан, Фан Динь Фунг, ночной рынок, Ле Дай Хань): телефоны, расстояние до Van Phu и маршрут.",
 "ko": f"달랏 3성급 호텔 {N}곳 지도(부이티쑤언, 판딘풍, 야시장, 레다이한): 전화번호, Van Phu까지 거리, 길찾기.",
 "id": f"Peta {N} hotel bintang 3 di Da Lat per jalan (Bui Thi Xuan, Phan Dinh Phung, pasar malam, Le Dai Hanh): nomor telepon, jarak ke Van Phu dan petunjuk arah.",
}
import re as _re
for _l in LANGS:
    t = T[_l]; anytime = t["s"]["ngocphat"][1]
    for i, sid in enumerate(_NEW):
        d = _D[_l][i] if _l in _D else _TPL[_l].format(s=_street(sid))
        t["s"][sid] = (_NAME[sid], anytime, d)
    t["title"] = _TITLE.get(_l) or _re.sub(r"(?<!\d)8(?!\d)", str(N), t["title"])
    t["desc"] = _DESC.get(_l) or _re.sub(r"(?<!\d)8(?!\d)", str(N), t["desc"])
    if _l in _LEAD:
        t["lead"] = _LEAD[_l]
    else:  # km, lo, my: drop the "250+ reviews each" clause (no longer true) and update counts
        ld = t["lead"]
        for cut in ["នីមួយៗមានមតិលើស 250 នៅលើ Google Maps ", "ແຕ່ລະແຫ່ງມີຣີວິວຫຼາຍກວ່າ 250 ໃນ Google Maps ", "၊ တစ်ခုစီတွင် Google Maps သုံးသပ်ချက် 250 ကျော် ရှိသည်"]:
            ld = ld.replace(cut, "")
        assert "250" not in ld, _l
        t["lead"] = _re.sub(r"(?<!\d)6(?!\d)", str(NC), _re.sub(r"(?<!\d)8(?!\d)", str(N), ld))
    t["center"] = t["center"].replace("1–8", f"1–{N}")
    t["season"] = [(a.replace("1–6", f"1–{NC}"), b) for a, b in t["season"]]
    assert f"1–{N}" in t["center"] and any(f"1–{NC}" in a for a, _ in t["season"]), _l
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"ngocphat": "Khách sạn Ngọc Phát", "iris": "Iris Dalat Hotel", "dulys": "Hotel Du Lys", "roydala": "Hotel Roy Dala",
      "marguerite": "Marguerite Hotel", "maivang": "Khách sạn Mai Vàng", "kyhoa": "Khách sạn Kỳ Hòa Garden Villages",
      "decharme": "Dalat De Charme Village"}
_Q.update(_NAME)
def img_link(sid):
    """Temporary photo link: Google Images search for the hotel name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
