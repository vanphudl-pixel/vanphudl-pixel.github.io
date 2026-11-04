"""About / Giới thiệu pages (owner asked 2026-11-04, vi + en only) + author box on articles + "meet the owner" block on the home page.
Owner rule for these texts: NO prices — describe Văn Phú Đà Lạt generally as travel services: motorbike rental, homestay and villa booking.
Do not use licence/permit wording here (the site-wide rule is about driving licences; say "registered business" instead)."""

LANGS = ["vi", "en"]
UPDATED = "2026-11-04"
IMG = "ngo-van-phu-van-phu-dalat"
BIZ_CODE = "8317515796-001"

SLUG = {"vi": "vi/gioi-thieu/", "en": "about/"}

T = {
 "vi": {
  "title": "Giới thiệu Văn Phú Đà Lạt – Ngô Văn Phú, dịch vụ du lịch Đà Lạt",
  "desc": "Văn Phú Đà Lạt do Ngô Văn Phú làm chủ, hộ kinh doanh đăng ký từ 23/05/2024: dịch vụ du lịch Đà Lạt gồm thuê xe máy, đặt homestay, villa và tư vấn lịch trình.",
  "crumb": "Giới thiệu",
  "h1": "Xin chào, tôi là Phú",
  "sub": "<b>Ngô Văn Phú</b> – chủ <b>Văn Phú Đà Lạt</b>, dịch vụ du lịch tại Đà Lạt.",
  "alt": "Ngô Văn Phú – chủ Văn Phú Đà Lạt, dịch vụ du lịch Đà Lạt",
  "intro": [
    "Tôi sống và làm việc tại Đà Lạt. Văn Phú Đà Lạt là hộ kinh doanh do tôi đứng tên, <b>đăng ký chính thức từ ngày 23/05/2024</b> (mã số hộ kinh doanh 8317515796-001).",
    "Tôi trực tiếp hỗ trợ và trả lời tin nhắn của khách, không qua trung gian. Khách của tôi đến từ Việt Nam và nhiều nước trên thế giới.",
  ],
  "h_services": "Dịch vụ của Văn Phú",
  "services": [
    ("Thuê xe máy Đà Lạt", "xe tay ga, xe điện và xe số để tự do khám phá thành phố.", "home"),
    ("Đặt homestay, villa", "chỗ ở phù hợp cho cặp đôi, gia đình và nhóm bạn.", None),
    ("Tư vấn lịch trình", "gợi ý cung đường, điểm chụp ảnh, quán ăn và thời điểm đẹp nhất để đi.", "routes"),
  ],
  "h_more": "Không chỉ là dịch vụ",
  "more": "Các bản đồ điểm chụp ảnh, thác nước, quán cà phê, chợ đêm và cẩm nang du lịch trên website này do tôi tổng hợp, để khách khám phá Đà Lạt dễ dàng và an toàn hơn. Tôi cũng chia sẻ video Đà Lạt trên kênh YouTube.",
  "h_contact": "Liên hệ trực tiếp với tôi",
  "addr_lbl": "Địa chỉ",
  "h_reviews": "Đánh giá của khách",
  "author": "Viết bởi Ngô Văn Phú",
  "author_txt": "chủ Văn Phú Đà Lạt, hộ kinh doanh dịch vụ du lịch đăng ký tại Đà Lạt từ 2024: thuê xe máy, đặt homestay, villa.",
  "author_link": "Giới thiệu về tôi",
  "meet": "Gặp Phú, người trực tiếp hỗ trợ bạn",
  "meet_txt": "Dịch vụ du lịch Đà Lạt, hộ kinh doanh đăng ký từ 2024: thuê xe máy, đặt homestay, villa.",
  "meet_link": "Giới thiệu",
  "foot": "Giới thiệu",
 },
 "en": {
  "title": "About Van Phu Dalat – Meet Phu, Local Travel Services in Da Lat",
  "desc": "Van Phu Dalat is run by Ngo Van Phu, an officially registered business since 23 May 2024: local travel services in Da Lat – motorbike rental, homestay and villa booking.",
  "crumb": "About",
  "h1": "Hi, I'm Phu",
  "sub": "<b>Ngô Văn Phú</b> – owner of <b>Van Phu Dalat</b>, local travel services in Da Lat, Vietnam.",
  "alt": "Ngo Van Phu, owner of Van Phu Dalat travel services in Da Lat",
  "intro": [
    "I live and work in Da Lat. Van Phu Dalat is my own business, <b>officially registered since 23 May 2024</b> (business code 8317515796-001).",
    "I look after every guest and answer every message myself – no agents, no middlemen. My guests come from Vietnam and from all over the world.",
  ],
  "h_services": "What we offer",
  "services": [
    ("Motorbike rental in Da Lat", "scooters, electric scooters and manual bikes to explore the city at your own pace.", "home"),
    ("Homestay &amp; villa booking", "places to stay for couples, families and groups of friends.", None),
    ("Local travel advice", "routes, photo spots, food and the best time to visit each place.", "routes"),
  ],
  "h_more": "More than a service",
  "more": "The photo-spot, waterfall, café and night-market maps and the travel guides on this website are put together by me, to help you explore Da Lat easily and safely. I also share Da Lat videos on my YouTube channel.",
  "h_contact": "Contact me directly",
  "addr_lbl": "Address",
  "h_reviews": "Guest reviews",
  "author": "Written by Ngô Văn Phú (Phu)",
  "author_txt": "owner of Van Phu Dalat, a registered local travel business in Da Lat since 2024: motorbike rental, homestay and villa booking.",
  "author_link": "About me",
  "meet": "Meet Phu, the local who looks after you",
  "meet_txt": "Local Da Lat travel services, a registered business since 2024: motorbike rental, homestay and villa booking.",
  "meet_link": "About us",
  "foot": "About",
 },
}

# Owner asked 2026-11-04: also the other main (focus) languages.
LANGS = ["vi", "en", "zh", "ru", "ko", "id"]
SLUG.update({"zh": "zh/about/", "ru": "ru/o-nas/", "ko": "ko/about/", "id": "id/tentang-kami/"})

T["zh"] = {
  "title": "关于 Van Phu 大叻 – 店主 Phu，大叻本地旅游服务",
  "desc": "Van Phu 大叻由店主 Ngô Văn Phú 经营，自2024年5月23日起正式注册：大叻本地旅游服务，包括摩托车租赁、民宿和别墅预订。",
  "crumb": "关于我们",
  "h1": "你好，我是 Phu",
  "sub": "<b>Ngô Văn Phú</b>（Phu）—— <b>Van Phu 大叻</b>店主，大叻本地旅游服务。",
  "alt": "Van Phu 大叻店主 Ngô Văn Phú",
  "intro": [
    "我在大叻生活和工作。Van Phu 大叻是以我名义经营的个体工商户，<b>自2024年5月23日起正式注册</b>（营业登记号 8317515796-001）。",
    "每位客人都由我本人接待，消息也由我亲自回复，没有中介。我的客人来自越南和世界各地。",
  ],
  "h_services": "我们的服务",
  "services": [
    ("大叻摩托车租赁", "踏板车、电动车和手动挡摩托车，按自己的节奏探索大叻。", "home"),
    ("民宿、别墅预订", "适合情侣、家庭和朋友结伴入住。", None),
    ("行程建议", "推荐路线、拍照点、美食，以及每个地方的最佳游览时间。", "routes"),
  ],
  "h_more": "不只是服务",
  "more": "本网站上的拍照点、瀑布、咖啡馆、夜市地图和旅游攻略都由我亲自整理，让你更轻松、更安全地游览大叻。我也在 YouTube 频道分享大叻视频。",
  "h_contact": "直接联系我", "addr_lbl": "地址", "h_reviews": "客人评价",
  "author": "作者：Ngô Văn Phú（Phu）",
  "author_txt": "Van Phu 大叻店主，自2024年起在大叻正式注册的本地旅游服务：摩托车租赁、民宿和别墅预订。",
  "author_link": "关于我",
  "meet": "认识 Phu，亲自为你服务的本地人",
  "meet_txt": "大叻本地旅游服务，自2024年起正式注册：摩托车租赁、民宿和别墅预订。",
  "meet_link": "关于我们",
  "foot": "关于我们",
}

T["ru"] = {
  "title": "О Van Phu Dalat – владелец Фу, туристические услуги в Далате",
  "desc": "Van Phu Dalat – бизнес Нго Ван Фу, официально зарегистрированный с 23 мая 2024 года: туристические услуги в Далате – аренда байков, бронирование хоумстеев и вилл.",
  "crumb": "О нас",
  "h1": "Привет, я Фу",
  "sub": "<b>Нго Ван Фу (Ngô Văn Phú)</b> – владелец <b>Van Phu Dalat</b>, местные туристические услуги в Далате.",
  "alt": "Нго Ван Фу, владелец Van Phu Dalat в Далате",
  "intro": [
    "Я живу и работаю в Далате. Van Phu Dalat – мой собственный бизнес, <b>официально зарегистрированный с 23 мая 2024 года</b> (регистрационный номер 8317515796-001).",
    "Я сам встречаю каждого гостя и отвечаю на каждое сообщение – без агентов и посредников. Ко мне приезжают гости из Вьетнама и со всего мира.",
  ],
  "h_services": "Что мы предлагаем",
  "services": [
    ("Аренда байков в Далате", "скутеры, электроскутеры и байки с механикой, чтобы исследовать город в своём темпе.", "home"),
    ("Бронирование хоумстеев и вилл", "жильё для пар, семей и компаний друзей.", None),
    ("Советы по маршрутам", "маршруты, места для фото, еда и лучшее время для каждой точки.", "routes"),
  ],
  "h_more": "Больше, чем услуга",
  "more": "Карты фотоспотов, водопадов, кафе и ночного рынка, а также путеводители на этом сайте я собираю сам, чтобы вам было проще и безопаснее исследовать Далат. Ещё я делюсь видео о Далате на своём YouTube-канале.",
  "h_contact": "Свяжитесь со мной напрямую", "addr_lbl": "Адрес", "h_reviews": "Отзывы гостей",
  "author": "Автор: Нго Ван Фу (Phu)",
  "author_txt": "владелец Van Phu Dalat, зарегистрированные туристические услуги в Далате с 2024 года: аренда байков, бронирование хоумстеев и вилл.",
  "author_link": "Обо мне",
  "meet": "Знакомьтесь: Фу, местный, который о вас позаботится",
  "meet_txt": "Туристические услуги в Далате, официальный бизнес с 2024 года: аренда байков, бронирование хоумстеев и вилл.",
  "meet_link": "О нас",
  "foot": "О нас",
}

T["ko"] = {
  "title": "Van Phu 달랏 소개 – 사장 Phu, 달랏 현지 여행 서비스",
  "desc": "Van Phu 달랏은 Ngô Văn Phú가 운영하며 2024년 5월 23일부터 정식 등록된 사업자입니다. 달랏 현지 여행 서비스: 오토바이 렌탈, 홈스테이·빌라 예약.",
  "crumb": "소개",
  "h1": "안녕하세요, Phu입니다",
  "sub": "<b>Ngô Văn Phú</b> – <b>Van Phu 달랏</b> 사장, 달랏 현지 여행 서비스.",
  "alt": "Van Phu 달랏 사장 Ngô Văn Phú",
  "intro": [
    "저는 달랏에서 살며 일하고 있습니다. Van Phu 달랏은 제 이름으로 운영하는 사업자로, <b>2024년 5월 23일부터 정식 등록</b>되어 있습니다(사업자 번호 8317515796-001).",
    "모든 손님을 제가 직접 맞이하고 메시지에도 직접 답변합니다. 중개인은 없습니다. 베트남과 세계 여러 나라에서 손님들이 찾아오십니다.",
  ],
  "h_services": "서비스 안내",
  "services": [
    ("달랏 오토바이 렌탈", "스쿠터, 전기 스쿠터, 기어 오토바이로 원하는 속도에 맞춰 달랏을 둘러보세요.", "home"),
    ("홈스테이·빌라 예약", "커플, 가족, 친구 모임에 맞는 숙소.", None),
    ("여행 일정 상담", "코스, 사진 명소, 맛집, 장소별 가장 좋은 방문 시간.", "routes"),
  ],
  "h_more": "서비스 그 이상",
  "more": "이 웹사이트의 사진 명소, 폭포, 카페, 야시장 지도와 여행 가이드는 제가 직접 정리했습니다. 달랏을 더 쉽고 안전하게 여행하실 수 있도록 돕기 위해서입니다. YouTube 채널에서도 달랏 영상을 공유하고 있습니다.",
  "h_contact": "직접 연락하기", "addr_lbl": "주소", "h_reviews": "손님 후기",
  "author": "글쓴이: Ngô Văn Phú (Phu)",
  "author_txt": "Van Phu 달랏 사장, 2024년부터 달랏에 정식 등록된 현지 여행 서비스: 오토바이 렌탈, 홈스테이·빌라 예약.",
  "author_link": "소개 보기",
  "meet": "Phu를 만나보세요, 직접 도와드리는 현지인",
  "meet_txt": "달랏 현지 여행 서비스, 2024년부터 정식 등록 사업자: 오토바이 렌탈, 홈스테이·빌라 예약.",
  "meet_link": "소개",
  "foot": "소개",
}

T["id"] = {
  "title": "Tentang Van Phu Dalat – Kenalan dengan Phu, Layanan Wisata Lokal Da Lat",
  "desc": "Van Phu Dalat dijalankan oleh Ngô Văn Phú, usaha resmi terdaftar sejak 23 Mei 2024: layanan wisata lokal di Da Lat – sewa motor, pemesanan homestay dan vila.",
  "crumb": "Tentang kami",
  "h1": "Halo, saya Phu",
  "sub": "<b>Ngô Văn Phú</b> – pemilik <b>Van Phu Dalat</b>, layanan wisata lokal di Da Lat, Vietnam.",
  "alt": "Ngô Văn Phú, pemilik Van Phu Dalat di Da Lat",
  "intro": [
    "Saya tinggal dan bekerja di Da Lat. Van Phu Dalat adalah usaha milik saya sendiri, <b>terdaftar resmi sejak 23 Mei 2024</b> (nomor usaha 8317515796-001).",
    "Saya sendiri yang melayani setiap tamu dan membalas setiap pesan – tanpa agen, tanpa perantara. Tamu saya datang dari Vietnam dan dari seluruh dunia.",
  ],
  "h_services": "Layanan kami",
  "services": [
    ("Sewa motor di Da Lat", "skuter matic, skuter listrik dan motor bebek untuk menjelajah kota dengan santai.", "home"),
    ("Pemesanan homestay &amp; vila", "tempat menginap untuk pasangan, keluarga dan rombongan teman.", None),
    ("Saran perjalanan lokal", "rute, spot foto, kuliner dan waktu terbaik untuk mengunjungi setiap tempat.", "routes"),
  ],
  "h_more": "Lebih dari sekadar layanan",
  "more": "Peta spot foto, air terjun, kafe, pasar malam dan panduan wisata di situs ini saya susun sendiri, agar Anda bisa menjelajah Da Lat dengan mudah dan aman. Saya juga membagikan video Da Lat di kanal YouTube saya.",
  "h_contact": "Hubungi saya langsung", "addr_lbl": "Alamat", "h_reviews": "Ulasan tamu",
  "author": "Ditulis oleh Ngô Văn Phú (Phu)",
  "author_txt": "pemilik Van Phu Dalat, layanan wisata lokal terdaftar di Da Lat sejak 2024: sewa motor, pemesanan homestay dan vila.",
  "author_link": "Tentang saya",
  "meet": "Kenalan dengan Phu, warga lokal yang melayani Anda",
  "meet_txt": "Layanan wisata lokal Da Lat, usaha terdaftar sejak 2024: sewa motor, pemesanan homestay dan vila.",
  "meet_link": "Tentang kami",
  "foot": "Tentang kami",
}
