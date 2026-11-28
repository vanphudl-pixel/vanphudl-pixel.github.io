"""'Arriving in Da Lat early by night bus' pillar page (owner asked 2026-10-28, all languages) — the "before the trip" cluster.
Hub of the cluster: links to the getting article, lt-early, cloudhunt, caudat, the 3 bus maps and the licence page; those pages link back here.
Facts used (sources checked 2026-10-28):
- HCMC -> Da Lat about 300 km, sleeper bus about 6-8 h; overnight buses usually arrive about 4:00-7:00 (varies by company, traffic, weather).
- Nha Trang -> Da Lat about 135-140 km, about 3.5-4 h, departures in the daytime.
- Da Lat intercity bus station: 1 Tô Hiến Thành, open 24 h; many companies drop at their own office instead.
- Bus station -> shop about 3 km straight line (Futa office about 1.3 km). Night temperatures about 10-15 °C (site weather article).
Owner rules kept: shop opens 4:30, rental day until 21:00, free delivery only to central hotels for 2+ days (never promise bus-station
delivery: "message us"), no price in title/desc, VND, approved EV range wording, gas scooters need a licence -> link {LIC}.
No fares, no timetables, no company recommendations.
Placeholders: {EV} {HOME} {ROUTES} {LIC} {ART:key} {MAP:module}."""
LANGS = ["en", "vi", "ru", "zh", "ko", "ja", "th", "id", "ms", "de", "fr", "es", "he", "it", "nl", "km", "lo", "my"]
EN_SLUG = "arriving-in-da-lat-early-by-night-bus"
SLUG = {l: EN_SLUG for l in LANGS}
SLUG["vi"] = "xe-dem-den-da-lat-sang-som"
SLUG["ru"] = "nochnoy-avtobus-v-dalat-rano-utrom"
UPDATED = "2026-10-28"
IMG = "van-phu-shop-early-pickup-air-blade"
ICON = "🚌"
FROM = {"getting", "lt-early", "lt-caudat-early", "cloudhunt", "lt-procedure"}  # articles that link here
MAPS_FROM = {"busmap", "nhatrangbusmap", "danangbusmap"}  # map pages that link here
T = {}

T["en"] = {
 "title": "Night Bus to Da Lat Arriving at 4–5 am: What to Do | Van Phu",
 "desc": "Overnight buses from Ho Chi Minh City reach Da Lat around 4–7 am. Where they stop, how to get to the centre, and picking up a scooter from 4:30 am.",
 "h1": "Arriving in Da Lat Early by Night Bus: What to Do",
 "crumb": "Arriving in Da Lat early",
 "lead": "The overnight sleeper bus from Ho Chi Minh City usually reaches Da Lat between about <b>4:00 and 7:00 am</b> — before most of the city wakes up. Our rental shop opens at <b>4:30 am every day</b>, so you can be on a scooter soon after you step off the bus. Here is how that first morning works.",
 "short_h": "At a glance",
 "short": [
  ("Ho Chi Minh City → Da Lat", "About 300 km; sleeper bus about 6–8 hours; overnight buses usually arrive about 4:00–7:00"),
  ("Nha Trang → Da Lat", "About 135–140 km; about 3.5–4 hours; buses run in the daytime"),
  ("Where buses stop", "Da Lat intercity bus station (1 Tô Hiến Thành, open 24 hours) or the bus company's own office"),
  ("Bus station → our shop", "About 3 km in a straight line, a little more by road — taxi or Grab"),
  ("Our shop", "1/15/5 Thông Thiên Học — opens 4:30 am every day"),
  ("Early-morning temperature", "Often about 10–15 °C — keep a jacket out of your bag"),
 ],
 "secs": [
  ("Night bus from Ho Chi Minh City: when you arrive", "<p>Sleeper buses leave Ho Chi Minh City in the evening and cover about 300 km in roughly 6–8 hours. The exact arrival depends on the company, traffic and the weather on the mountain road, but most overnight buses pull into Da Lat somewhere between about 4:00 and 7:00 am.</p><p>When you book, ask where the bus stops in Da Lat: the intercity bus station on Tô Hiến Thành, the company's own office in town, or — with some limousine vans — your hotel. You can see the bus station and the main company offices on our <a href=\"{MAP:busmap}\">Da Lat – Saigon bus map</a>. Coming from Da Nang or Hoi An? See the <a href=\"{MAP:danangbusmap}\">Da Lat – Da Nang bus map</a>.</p>"),
  ("From Nha Trang: a daytime bus", "<p>Nha Trang is closer — about 135–140 km over a scenic mountain pass, roughly 3.5–4 hours — and buses run during the day, so you usually arrive in Da Lat by late morning or afternoon. The offices of the main companies are on our <a href=\"{MAP:nhatrangbusmap}\">Nha Trang – Da Lat bus map</a>, and the route options are in <a href=\"{ART:getting}\">how to get to Da Lat</a>.</p><p>One thing to know: a rental day runs from pick-up until 21:00. If you arrive at 16:00, picking up the scooter straight away still counts as a full day. Many guests check in, rest, and pick up the next morning from 4:30. Renting for 2 days or more? We deliver free to hotels in central Da Lat.</p>"),
  ("From the bus to a scooter, step by step", "<ol><li><b>The evening before:</b> message us on WhatsApp (+84 944 081 101 or +84 834 622 149), Telegram (@vanphudalat), WeChat (vanphudalat) or Zalo with your bus company, your rough arrival time and the bike you want.</li><li><b>Get off the bus</b> and take a taxi or Grab to 1/15/5 Thông Thiên Học. Ride-hailing can be slow to find before dawn; taxis usually wait at the bus station.</li><li><b>Paperwork takes a few minutes:</b> your passport (no cash deposit) and 150,000 VND per day for any bike.</li><li><b>Short test ride</b>, and we film the bike's condition together.</li><li><b>Ride off.</b> A rental day runs until 21:00, so a scooter picked up at 4:30 is yours for the whole day.</li></ol>"),
  ("Your first hours: sunrise, or rest first?", "<ul><li><b>Slept well on the bus?</b> Da Lat's best light is right now. Head for <a href=\"{ART:cloudhunt}\">cloud hunting</a> or the <a href=\"{ART:caudat}\">Cau Dat tea hills at sunrise</a> — take the Honda Air Blade 125cc for those hills.</li><li><b>Slept badly?</b> Don't start on misty, wet hill roads while you're tired. Have a hot coffee and breakfast first, and ride once you feel awake.</li><li><b>Big suitcase?</b> Don't ride with it. Drop it at your hotel first — many hotels hold luggage before check-in — or rent for 2+ days and we bring the bike to your central hotel for free.</li><li>Wear your helmet, no alcohol or beer when riding, and strictly follow Vietnamese traffic law.</li></ul><p>More reasons to start early: <a href=\"{ART:lt-early}\">early motorbike rental in Da Lat</a>.</p>"),
 ],
 "faq_h": "Frequently asked questions",
 "faq": [
  ("What time does the night bus from Ho Chi Minh City arrive in Da Lat?", "Usually between about 4:00 and 7:00 am. It depends on the company, traffic and the weather on the mountain road, so ask the company for its estimate when you book."),
  ("Where does the bus drop me in Da Lat?", "Either at the Da Lat intercity bus station on Tô Hiến Thành (open 24 hours) or at the bus company's own office in town. Some limousine vans drop at hotels. Ask when you book."),
  ("Can I rent a scooter at 4:30 am?", "Yes. Our shop opens at 4:30 am every day. Message us the evening before with your arrival time and bike, and it will be ready when you come."),
  ("Can you bring the bike to the bus station?", "Free delivery is for hotels in central Da Lat on rentals of 2 days or more. For anything else, message us with your plan and we'll tell you what's possible."),
  ("I arrive from Nha Trang in the afternoon. Should I rent today or tomorrow?", "A rental day runs until 21:00, so a late-afternoon pick-up still counts as a full day. If you only need the bike from the next morning, pick it up from 4:30 — or rent for 2+ days and get free delivery to your central hotel."),
 ],
 "more_h": "Plan the rest of your trip",
 "more": [("{ART:getting}", "How to get to Da Lat"), ("{MAP:busmap}", "Da Lat – Saigon bus map"), ("{MAP:nhatrangbusmap}", "Nha Trang – Da Lat bus map"), ("{ART:lt-early}", "Early motorbike rental (4:30 am)"), ("{HOME}", "Da Lat motorbike rental — bikes and prices")],
}

T["vi"] = {
 "title": "Xe đêm Sài Gòn – Đà Lạt mấy giờ tới? Đến sớm làm gì | Văn Phú",
 "desc": "Xe giường nằm đêm từ Sài Gòn thường tới Đà Lạt khoảng 4–7 giờ sáng. Xe dừng ở đâu, về trung tâm thế nào và thuê xe máy từ 4:30 sáng ở Văn Phú.",
 "h1": "Đi xe đêm đến Đà Lạt sáng sớm: nên làm gì?",
 "crumb": "Xe đêm đến Đà Lạt sáng sớm",
 "lead": "Xe giường nằm đêm từ Sài Gòn thường tới Đà Lạt khoảng <b>4–7 giờ sáng</b>, khi thành phố còn chưa thức dậy. Tiệm Văn Phú mở cửa <b>từ 4:30 sáng mỗi ngày</b>, nên xuống xe một lúc là bạn đã có xe máy để đi. Dưới đây là cách sắp xếp buổi sáng đầu tiên.",
 "short_h": "Tóm tắt nhanh",
 "short": [
  ("Sài Gòn → Đà Lạt", "Khoảng 300 km; xe giường nằm khoảng 6–8 tiếng; xe đêm thường tới khoảng 4–7 giờ sáng"),
  ("Nha Trang → Đà Lạt", "Khoảng 135–140 km; khoảng 3,5–4 tiếng; xe chạy ban ngày"),
  ("Xe dừng ở đâu", "Bến xe liên tỉnh Đà Lạt (1 Tô Hiến Thành, mở 24 giờ) hoặc văn phòng riêng của nhà xe"),
  ("Bến xe → tiệm Văn Phú", "Khoảng 3 km đường chim bay, đường thực tế xa hơn một chút — đi taxi hoặc Grab"),
  ("Tiệm Văn Phú", "1/15/5 Thông Thiên Học — mở cửa 4:30 sáng mỗi ngày"),
  ("Nhiệt độ sáng sớm", "Thường khoảng 10–15 °C — để sẵn áo khoác ngoài balo"),
 ],
 "secs": [
  ("Xe đêm từ Sài Gòn: mấy giờ tới Đà Lạt?", "<p>Xe giường nằm xuất phát từ Sài Gòn buổi tối, chạy khoảng 300 km trong 6–8 tiếng. Giờ tới thực tế tùy nhà xe, tình trạng đường và thời tiết trên đèo, nhưng phần lớn xe đêm vào Đà Lạt trong khoảng 4–7 giờ sáng.</p><p>Khi đặt vé, hãy hỏi xe trả khách ở đâu: bến xe liên tỉnh trên đường Tô Hiến Thành, văn phòng riêng của nhà xe trong thành phố, hay — với một số xe limousine — trả tận khách sạn. Bến xe và văn phòng các nhà xe chính có trên <a href=\"{MAP:busmap}\">bản đồ xe Đà Lạt – Sài Gòn</a>. Đi từ Đà Nẵng, Hội An thì xem <a href=\"{MAP:danangbusmap}\">bản đồ xe Đà Lạt – Đà Nẵng</a>.</p>"),
  ("Từ Nha Trang: xe chạy ban ngày", "<p>Nha Trang gần hơn — khoảng 135–140 km qua đèo, chừng 3,5–4 tiếng — và xe chạy ban ngày, nên thường bạn tới Đà Lạt vào cuối buổi sáng hoặc buổi chiều. Văn phòng các nhà xe chính có trên <a href=\"{MAP:nhatrangbusmap}\">bản đồ xe Nha Trang – Đà Lạt</a>, còn các cách đi có trong bài <a href=\"{ART:getting}\">cách đi đến Đà Lạt</a>.</p><p>Cần biết: một ngày thuê tính từ lúc nhận xe đến 21:00. Nếu tới lúc 16:00 mà lấy xe ngay thì vẫn tính trọn một ngày. Nhiều khách nhận phòng, nghỉ ngơi rồi sáng hôm sau lấy xe từ 4:30. Thuê từ 2 ngày, tiệm giao xe miễn phí tới khách sạn ở trung tâm.</p>"),
  ("Từ lúc xuống xe đến lúc có xe máy", "<ol><li><b>Tối hôm trước:</b> nhắn Zalo 0944 081 101 hoặc WhatsApp (+84 944 081 101, +84 834 622 149) báo nhà xe, giờ dự kiến tới và loại xe bạn muốn.</li><li><b>Xuống xe</b> rồi đi taxi hoặc Grab tới 1/15/5 Thông Thiên Học. Trước lúc trời sáng, gọi Grab có thể lâu; taxi thường đợi sẵn ở bến xe.</li><li><b>Thủ tục vài phút:</b> để lại CCCD hoặc hộ chiếu (không cọc tiền), giá 150.000 VND/ngày cho mọi xe.</li><li><b>Chạy thử</b> và cùng quay video tình trạng xe.</li><li><b>Lên đường.</b> Ngày thuê tính đến 21:00, nên xe lấy lúc 4:30 là của bạn cả ngày.</li></ol>"),
  ("Mấy giờ đầu tiên: săn mây hay nghỉ trước?", "<ul><li><b>Ngủ được trên xe?</b> Đây là lúc Đà Lạt đẹp nhất. Đi <a href=\"{ART:cloudhunt}\">săn mây</a> hoặc <a href=\"{ART:caudat}\">ngắm bình minh đồi chè Cầu Đất</a> — nên chọn Honda Air Blade 125cc cho các cung dốc này.</li><li><b>Ngủ không ngon?</b> Đừng chạy đường đèo có sương, ướt khi đang mệt. Uống cà phê nóng, ăn sáng trước, tỉnh táo rồi hãy đi.</li><li><b>Mang vali lớn?</b> Đừng chở vali trên xe máy. Gửi ở khách sạn trước — nhiều khách sạn giữ hành lý trước giờ nhận phòng — hoặc thuê từ 2 ngày để tiệm giao xe miễn phí tới khách sạn trung tâm.</li><li>Đội mũ bảo hiểm, không uống rượu bia khi lái xe và chấp hành nghiêm luật giao thông.</li></ul><p>Thêm lý do để đi sớm: <a href=\"{ART:lt-early}\">thuê xe máy Đà Lạt mở cửa sớm</a>.</p>"),
 ],
 "faq_h": "Câu hỏi thường gặp",
 "faq": [
  ("Xe giường nằm đêm Sài Gòn – Đà Lạt mấy giờ tới?", "Thường khoảng 4–7 giờ sáng, tùy nhà xe, tình trạng đường và thời tiết trên đèo. Hãy hỏi nhà xe giờ tới dự kiến khi đặt vé."),
  ("Xe trả khách ở đâu tại Đà Lạt?", "Ở bến xe liên tỉnh Đà Lạt trên đường Tô Hiến Thành (mở 24 giờ) hoặc văn phòng riêng của nhà xe trong thành phố. Một số xe limousine trả tận khách sạn. Nên hỏi khi đặt vé."),
  ("4:30 sáng có thuê được xe máy không?", "Được. Tiệm mở cửa 4:30 sáng mỗi ngày. Nhắn trước tối hôm trước giờ tới và loại xe, tiệm sẽ chuẩn bị sẵn."),
  ("Tiệm có giao xe ra bến xe không?", "Giao miễn phí áp dụng cho khách sạn ở trung tâm Đà Lạt khi thuê từ 2 ngày. Trường hợp khác, bạn nhắn kế hoạch để tiệm báo có làm được không."),
  ("Tới từ Nha Trang lúc chiều, nên lấy xe luôn hay sáng mai?", "Ngày thuê tính đến 21:00, nên lấy xe chiều muộn vẫn tính trọn một ngày. Nếu chỉ cần xe từ sáng hôm sau, hãy lấy từ 4:30 — hoặc thuê từ 2 ngày để được giao xe miễn phí tới khách sạn trung tâm."),
 ],
 "more_h": "Lên kế hoạch tiếp",
 "more": [("{ART:getting}", "Cách đi đến Đà Lạt"), ("{MAP:busmap}", "Bản đồ xe Đà Lạt – Sài Gòn"), ("{MAP:nhatrangbusmap}", "Bản đồ xe Nha Trang – Đà Lạt"), ("{ART:lt-early}", "Thuê xe máy mở cửa sớm 4:30"), ("{HOME}", "Thuê xe máy Đà Lạt — loại xe và giá")],
}

T["ru"] = {
 "title": "Ночной автобус в Далат: что делать в 4–5 утра | Van Phu",
 "desc": "Ночные автобусы из Хошимина приходят в Далат примерно в 4–7 утра. Где они останавливаются, как добраться до центра и как взять байк с 4:30.",
 "h1": "Приехали в Далат ночным автобусом рано утром: что делать",
 "crumb": "Ранний приезд в Далат",
 "lead": "Ночной спальный автобус из Хошимина обычно приходит в Далат примерно <b>в 4:00–7:00 утра</b>, когда город ещё спит. Наш прокат открывается <b>в 4:30 каждый день</b>, так что вскоре после автобуса вы уже можете ехать на байке. Вот как устроено это первое утро.",
 "short_h": "Коротко",
 "short": [
  ("Хошимин → Далат", "Около 300 км; спальный автобус примерно 6–8 часов; ночные рейсы обычно приходят около 4:00–7:00"),
  ("Нячанг → Далат", "Около 135–140 км; примерно 3,5–4 часа; автобусы ходят днём"),
  ("Где останавливаются автобусы", "Междугородний автовокзал Далата (1 Tô Hiến Thành, круглосуточно) или собственный офис перевозчика"),
  ("Автовокзал → наш прокат", "Около 3 км по прямой, по дороге чуть больше — такси или Grab"),
  ("Наш прокат", "1/15/5 Thông Thiên Học — открыто с 4:30 каждый день"),
  ("Температура ранним утром", "Часто около 10–15 °C — держите куртку под рукой"),
 ],
 "secs": [
  ("Ночной автобус из Хошимина: когда вы приедете", "<p>Спальные автобусы выезжают из Хошимина вечером и проходят около 300 км примерно за 6–8 часов. Точное время зависит от перевозчика, пробок и погоды на горной дороге, но большинство ночных рейсов приходит в Далат примерно между 4:00 и 7:00.</p><p>При покупке билета спросите, где автобус останавливается в Далате: на междугороднем автовокзале на Tô Hiến Thành, у собственного офиса компании в городе или — у некоторых лимузин-вэнов — прямо у отеля. Автовокзал и офисы основных компаний есть на нашей <a href=\"{MAP:busmap}\">карте автобусов Далат – Сайгон</a>. Едете из Дананга или Хойана? Смотрите <a href=\"{MAP:danangbusmap}\">карту автобусов Далат – Дананг</a>.</p>"),
  ("Из Нячанга: дневной автобус", "<p>Нячанг ближе — около 135–140 км через живописный перевал, примерно 3,5–4 часа, — и автобусы ходят днём, так что в Далат вы обычно приезжаете к концу утра или днём. Офисы основных компаний — на <a href=\"{MAP:nhatrangbusmap}\">карте автобусов Нячанг – Далат</a>, а варианты дороги — в статье <a href=\"{ART:getting}\">как добраться до Далата</a>.</p><p>Важно: сутки аренды длятся с момента выдачи до 21:00. Если вы приехали в 16:00 и сразу берёте байк, это всё равно полные сутки. Многие гости заселяются, отдыхают и забирают байк на следующее утро с 4:30. Берёте на 2 дня и больше? Бесплатно привезём байк в отель в центре Далата.</p>"),
  ("От автобуса до байка — по шагам", "<ol><li><b>Вечером накануне</b> напишите нам в WhatsApp (+84 944 081 101 или +84 834 622 149), Telegram (@vanphudalat) или WeChat (vanphudalat): компания, примерное время прибытия и какой байк нужен.</li><li><b>Выйдя из автобуса,</b> возьмите такси или Grab до 1/15/5 Thông Thiên Học. До рассвета Grab бывает трудно поймать; такси обычно стоят у автовокзала.</li><li><b>Оформление — несколько минут:</b> паспорт (без денежного залога) и 150 000 VND в сутки за любой байк.</li><li><b>Короткая тестовая поездка</b> и общее видео состояния байка.</li><li><b>В путь.</b> Сутки аренды длятся до 21:00, так что байк, взятый в 4:30, ваш на весь день.</li></ol>"),
  ("Первые часы: рассвет или сначала отдых?", "<ul><li><b>Выспались в автобусе?</b> Лучший свет в Далате — именно сейчас. Езжайте на <a href=\"{ART:cloudhunt}\">«охоту за облаками»</a> или на <a href=\"{ART:caudat}\">рассвет на чайных холмах Каудат</a> — для этих подъёмов берите Honda Air Blade 125cc.</li><li><b>Спали плохо?</b> Не выезжайте уставшим на мокрые горные дороги в тумане. Сначала горячий кофе и завтрак, а потом за руль.</li><li><b>Большой чемодан?</b> Не везите его на байке. Сначала оставьте его в отеле — многие отели хранят багаж до заселения — или возьмите байк на 2+ дня, и мы бесплатно привезём его в ваш отель в центре.</li><li>Шлем обязателен, никакого алкоголя за рулём, строго соблюдайте ПДД Вьетнама.</li></ul><p>Ещё причины выехать пораньше: <a href=\"{ART:lt-early}\">ранняя аренда байка в Далате</a>.</p>"),
 ],
 "faq_h": "Частые вопросы",
 "faq": [
  ("Во сколько ночной автобус из Хошимина приходит в Далат?", "Обычно примерно между 4:00 и 7:00 утра. Это зависит от перевозчика, пробок и погоды на горной дороге, поэтому уточните ориентировочное время при покупке билета."),
  ("Где автобус высаживает в Далате?", "На междугороднем автовокзале на Tô Hiến Thành (работает круглосуточно) или у собственного офиса компании в городе. Некоторые лимузин-вэны высаживают у отелей. Спросите при бронировании."),
  ("Можно взять байк в 4:30 утра?", "Да. Наш прокат открывается в 4:30 каждый день. Напишите накануне вечером время прибытия и нужный байк — он будет готов к вашему приходу."),
  ("Можете привезти байк на автовокзал?", "Бесплатная доставка — в отели в центре Далата при аренде от 2 дней. В остальных случаях напишите нам свой план, и мы скажем, что получится."),
  ("Приезжаю из Нячанга днём. Брать байк сегодня или завтра?", "Сутки аренды длятся до 21:00, поэтому выдача ближе к вечеру всё равно считается полными сутками. Если байк нужен только со следующего утра, забирайте его с 4:30 — или берите на 2+ дня с бесплатной доставкой в отель в центре."),
 ],
 "more_h": "Планируйте дальше",
 "more": [("{ART:getting}", "Как добраться до Далата"), ("{MAP:busmap}", "Карта автобусов Далат – Сайгон"), ("{MAP:nhatrangbusmap}", "Карта автобусов Нячанг – Далат"), ("{ART:lt-early}", "Ранняя аренда байка (с 4:30)"), ("{HOME}", "Аренда байка в Далате — байки и цены")],
}

T["zh"] = {
 "title": "坐夜班车凌晨到大叻怎么办？胡志明市—大叻几点到 | Van Phu",
 "desc": "从胡志明市出发的夜班卧铺车一般在凌晨4–7点左右到大叻。车停在哪里、怎么去市中心，以及凌晨4:30起取摩托车。",
 "h1": "坐夜班车凌晨到大叻，该怎么安排？",
 "crumb": "凌晨抵达大叻",
 "lead": "从胡志明市出发的夜班卧铺车，通常在<b>凌晨4:00–7:00左右</b>到达大叻，那时城市还没醒。我们的租车店<b>每天凌晨4:30开门</b>，下车后不久就能骑上摩托车出发。下面说说第一个早晨怎么安排。",
 "short_h": "一览",
 "short": [
  ("胡志明市 → 大叻", "约300公里；卧铺车约6–8小时；夜班车通常约4:00–7:00到达"),
  ("芽庄 → 大叻", "约135–140公里；约3.5–4小时；白天发车"),
  ("下车地点", "大叻省际客运站（1 Tô Hiến Thành，24小时开放）或客运公司自己的办事处"),
  ("客运站 → 我们的店", "直线约3公里，实际路程稍远——打车或Grab"),
  ("我们的店", "1/15/5 Thông Thiên Học——每天凌晨4:30开门"),
  ("清晨气温", "常在10–15 °C左右——外套放在随手能拿的地方"),
 ],
 "secs": [
  ("胡志明市夜班车：几点到大叻", "<p>卧铺车傍晚或夜里从胡志明市出发，约300公里，行驶约6–8小时。具体到达时间取决于客运公司、路况和山路天气，但大多数夜班车在凌晨4:00到7:00之间进入大叻。</p><p>订票时请问清楚在大叻的下车点：Tô Hiến Thành路上的省际客运站、公司在市内的办事处，或者部分豪华商务车会送到酒店。客运站和主要公司的办事处都标在我们的<a href=\"{MAP:busmap}\">大叻—西贡巴士地图</a>上。从岘港或会安过来？请看<a href=\"{MAP:danangbusmap}\">大叻—岘港巴士地图</a>。</p>"),
  ("从芽庄出发：白天的班车", "<p>芽庄更近——约135–140公里，翻越一段风景很美的山口，约3.5–4小时——而且班车白天发车，通常在上午晚些时候或下午到达大叻。主要公司的办事处见<a href=\"{MAP:nhatrangbusmap}\">芽庄—大叻巴士地图</a>，交通方式见<a href=\"{ART:getting}\">如何前往大叻</a>。</p><p>需要注意：租车一天是从取车时起算到当天21:00。如果16:00到达就马上取车，也按整天计算。很多客人先入住休息，第二天早上4:30以后再来取车。租2天及以上，我们免费把车送到大叻市中心的酒店。</p>"),
  ("从下车到骑上摩托车", "<ol><li><b>前一天晚上：</b>通过微信（vanphudalat）、WhatsApp（+84 944 081 101 或 +84 834 622 149）或 Telegram（@vanphudalat）告诉我们客运公司、大概到达时间和想要的车型。</li><li><b>下车后</b>打车或用Grab到 1/15/5 Thông Thiên Học。天亮前Grab可能不好叫；客运站通常有出租车等候。</li><li><b>手续几分钟：</b>护照（不收现金押金），所有车型每天150,000 VND。</li><li><b>短暂试骑</b>，一起拍摄车况视频。</li><li><b>出发。</b>租车一天到21:00为止，所以凌晨4:30取的车一整天都归你用。</li></ol>"),
  ("最初几个小时：去看日出，还是先休息？", "<ul><li><b>在车上睡得好？</b>大叻最美的光线就在现在。去<a href=\"{ART:cloudhunt}\">追云海</a>或<a href=\"{ART:caudat}\">看Cau Dat茶山日出</a>——这些坡路建议选Honda Air Blade 125cc。</li><li><b>没睡好？</b>别在疲劳时骑上有雾、湿滑的山路。先喝杯热咖啡、吃早餐，清醒了再出发。</li><li><b>带大行李箱？</b>不要用摩托车载。先放到酒店——很多酒店可以在入住前寄存行李——或者租2天以上，我们免费把车送到你在市中心的酒店。</li><li>戴好头盔，骑车不喝酒、不喝啤酒，严格遵守越南交通法规。</li></ul><p>早出发的更多理由：<a href=\"{ART:lt-early}\">大叻早开门的摩托车租赁</a>。</p>"),
 ],
 "faq_h": "常见问题",
 "faq": [
  ("胡志明市到大叻的夜班车几点到？", "通常在凌晨4:00到7:00左右，取决于客运公司、路况和山路天气，订票时请向客运公司确认预计到达时间。"),
  ("在大叻下车地点在哪里？", "在Tô Hiến Thành路上的大叻省际客运站（24小时开放），或客运公司在市内的办事处。部分豪华商务车会送到酒店。订票时问清楚即可。"),
  ("凌晨4:30能租到摩托车吗？", "可以。我们每天凌晨4:30开门。前一天晚上告诉我们到达时间和车型，到店时车就准备好了。"),
  ("能把车送到客运站吗？", "免费送车适用于租2天及以上、送到大叻市中心的酒店。其他情况请把行程发给我们，我们告诉你能否安排。"),
  ("下午从芽庄到，今天取车还是明天？", "租车一天到21:00为止，所以傍晚取车也按整天计算。如果第二天早上才用车，就4:30以后来取——或者租2天以上，享受免费送车到市中心酒店。"),
 ],
 "more_h": "继续规划行程",
 "more": [("{ART:getting}", "如何前往大叻"), ("{MAP:busmap}", "大叻—西贡巴士地图"), ("{MAP:nhatrangbusmap}", "芽庄—大叻巴士地图"), ("{ART:lt-early}", "凌晨4:30开门租车"), ("{HOME}", "大叻摩托车租赁——车型与价格")],
}

T["ko"] = {
 "title": "야간버스로 새벽 달랏 도착, 4~5시에 뭘 할까? | Van Phu",
 "desc": "호찌민에서 출발한 야간 슬리핑버스는 보통 새벽 4~7시쯤 달랏에 도착합니다. 하차 장소, 시내 이동 방법, 새벽 4시 30분부터 스쿠터 픽업까지 정리했습니다.",
 "h1": "야간버스로 새벽에 달랏 도착했다면: 이렇게 하세요",
 "crumb": "새벽 달랏 도착",
 "lead": "호찌민발 야간 슬리핑버스는 보통 <b>새벽 4시~7시쯤</b> 달랏에 도착합니다. 도시가 아직 잠든 시간이죠. 저희 렌트 가게는 <b>매일 새벽 4시 30분</b>에 문을 열어서, 버스에서 내린 뒤 금방 스쿠터를 탈 수 있습니다. 첫 아침을 이렇게 보내세요.",
 "short_h": "한눈에 보기",
 "short": [
  ("호찌민 → 달랏", "약 300 km; 슬리핑버스 약 6~8시간; 야간버스는 보통 4:00~7:00 도착"),
  ("나트랑 → 달랏", "약 135~140 km; 약 3.5~4시간; 낮에 운행"),
  ("하차 장소", "달랏 시외버스터미널(1 Tô Hiến Thành, 24시간) 또는 버스 회사 자체 사무실"),
  ("터미널 → 저희 가게", "직선 약 3 km, 실제 도로는 조금 더 — 택시 또는 Grab"),
  ("저희 가게", "1/15/5 Thông Thiên Học — 매일 새벽 4:30 오픈"),
  ("새벽 기온", "보통 10~15 °C 정도 — 겉옷은 꺼내 두세요"),
 ],
 "secs": [
  ("호찌민 야간버스: 언제 도착할까", "<p>슬리핑버스는 저녁에 호찌민을 출발해 약 300 km를 6~8시간 정도 달립니다. 도착 시간은 버스 회사, 교통, 산길 날씨에 따라 다르지만 대부분 새벽 4시에서 7시 사이에 달랏에 들어옵니다.</p><p>예약할 때 달랏 어디에서 내리는지 꼭 물어보세요. Tô Hiến Thành 거리의 시외버스터미널, 시내에 있는 회사 사무실, 또는 일부 리무진 밴은 호텔 앞에 내려 줍니다. 터미널과 주요 회사 사무실은 <a href=\"{MAP:busmap}\">달랏–사이공 버스 지도</a>에서 볼 수 있어요. 다낭이나 호이안에서 오신다면 <a href=\"{MAP:danangbusmap}\">달랏–다낭 버스 지도</a>를 보세요.</p>"),
  ("나트랑에서: 낮 버스", "<p>나트랑은 더 가깝습니다. 경치 좋은 고개를 넘어 약 135~140 km, 3.5~4시간 정도이고 버스가 낮에 다녀서 보통 늦은 오전이나 오후에 달랏에 도착합니다. 주요 회사 사무실은 <a href=\"{MAP:nhatrangbusmap}\">나트랑–달랏 버스 지도</a>에, 이동 방법은 <a href=\"{ART:getting}\">달랏 가는 방법</a>에 정리해 두었습니다.</p><p>알아 두세요: 렌트 하루는 픽업 시각부터 그날 21:00까지입니다. 16시에 도착해서 바로 빌려도 하루로 계산돼요. 많은 손님이 체크인하고 쉰 다음, 다음 날 새벽 4시 30분부터 픽업합니다. 2일 이상 렌트하면 달랏 시내 호텔로 무료 배달해 드립니다.</p>"),
  ("버스에서 내려 스쿠터를 타기까지", "<ol><li><b>전날 저녁:</b> WhatsApp(+84 944 081 101 또는 +84 834 622 149), Telegram(@vanphudalat), WeChat(vanphudalat)으로 버스 회사, 대략적인 도착 시간, 원하는 바이크를 알려 주세요.</li><li><b>버스에서 내리면</b> 택시나 Grab으로 1/15/5 Thông Thiên Học까지 오세요. 해 뜨기 전에는 Grab 잡기가 어려울 수 있고, 택시는 보통 터미널에서 대기합니다.</li><li><b>수속은 몇 분:</b> 여권(현금 보증금 없음)과 모든 바이크 하루 150,000 VND.</li><li><b>짧은 시승</b>과 함께 바이크 상태 영상 촬영.</li><li><b>출발.</b> 렌트 하루는 21:00까지라서 4:30에 빌린 바이크는 하루 종일 쓸 수 있어요.</li></ol>"),
  ("첫 몇 시간: 일출 먼저, 아니면 휴식 먼저?", "<ul><li><b>버스에서 잘 잤다면?</b> 달랏의 가장 좋은 빛은 바로 지금입니다. <a href=\"{ART:cloudhunt}\">구름 사냥</a>이나 <a href=\"{ART:caudat}\">꺼우닷 차밭 일출</a>로 가 보세요. 이런 오르막에는 Honda Air Blade 125cc를 추천합니다.</li><li><b>잠을 설쳤다면?</b> 피곤한 상태로 안개 낀 젖은 산길을 달리지 마세요. 뜨거운 커피와 아침을 먼저 드시고, 정신이 들면 출발하세요.</li><li><b>큰 캐리어가 있다면?</b> 스쿠터에 싣지 마세요. 먼저 호텔에 맡기거나(체크인 전 짐 보관을 해 주는 호텔이 많아요), 2일 이상 렌트해서 시내 호텔로 무료 배달을 받으세요.</li><li>헬멧 착용, 음주 운전 금지, 베트남 교통법을 꼭 지켜 주세요.</li></ul><p>일찍 출발할 이유가 더 있어요: <a href=\"{ART:lt-early}\">달랏 새벽 오토바이 렌트</a>.</p>"),
 ],
 "faq_h": "자주 묻는 질문",
 "faq": [
  ("호찌민발 야간버스는 달랏에 몇 시에 도착하나요?", "보통 새벽 4시~7시쯤입니다. 버스 회사, 교통, 산길 날씨에 따라 달라지니 예약할 때 예상 도착 시간을 물어보세요."),
  ("달랏에서는 어디에서 내리나요?", "Tô Hiến Thành 거리의 달랏 시외버스터미널(24시간) 또는 시내의 버스 회사 사무실입니다. 일부 리무진 밴은 호텔 앞에 내려 줍니다. 예약할 때 확인하세요."),
  ("새벽 4시 30분에 스쿠터를 빌릴 수 있나요?", "네. 저희 가게는 매일 새벽 4시 30분에 엽니다. 전날 저녁에 도착 시간과 바이크를 알려 주시면 준비해 두겠습니다."),
  ("버스터미널로 바이크를 가져다줄 수 있나요?", "무료 배달은 2일 이상 렌트 시 달랏 시내 호텔에 한합니다. 그 밖의 경우는 일정을 보내 주시면 가능한지 알려 드릴게요."),
  ("나트랑에서 오후에 도착해요. 오늘 빌릴까요, 내일 빌릴까요?", "렌트 하루는 21:00까지라서 늦은 오후에 픽업해도 하루로 계산됩니다. 다음 날 아침부터만 필요하다면 4시 30분부터 픽업하시거나, 2일 이상 렌트해 시내 호텔 무료 배달을 받으세요."),
 ],
 "more_h": "다음 일정 계획하기",
 "more": [("{ART:getting}", "달랏 가는 방법"), ("{MAP:busmap}", "달랏–사이공 버스 지도"), ("{MAP:nhatrangbusmap}", "나트랑–달랏 버스 지도"), ("{ART:lt-early}", "새벽 4:30 오토바이 렌트"), ("{HOME}", "달랏 오토바이 렌트 — 바이크와 가격")],
}

T["ja"] = {
 "title": "夜行バスで早朝ダラット着、朝4〜5時にどうする？ | Van Phu",
 "desc": "ホーチミン発の夜行寝台バスは、だいたい朝4〜7時ごろダラットに着きます。降車場所、中心部への行き方、朝4:30からのスクーター受け取りを解説。",
 "h1": "夜行バスで早朝ダラットに着いたら：何をする？",
 "crumb": "早朝のダラット到着",
 "lead": "ホーチミン発の夜行寝台バスは、だいたい<b>朝4:00〜7:00ごろ</b>ダラットに着きます。街がまだ眠っている時間です。当店は<b>毎日朝4:30から営業</b>しているので、バスを降りてまもなくスクーターで出発できます。最初の朝の過ごし方をまとめました。",
 "short_h": "ひと目で分かるポイント",
 "short": [
  ("ホーチミン → ダラット", "約300km。寝台バスで約6〜8時間。夜行便はたいてい4:00〜7:00ごろ到着"),
  ("ニャチャン → ダラット", "約135〜140km。約3.5〜4時間。日中の運行"),
  ("バスの降車場所", "ダラット長距離バスターミナル（1 Tô Hiến Thành、24時間）またはバス会社の自社オフィス"),
  ("バスターミナル → 当店", "直線で約3km、道路ではもう少し — タクシーかGrab"),
  ("当店", "1/15/5 Thông Thiên Học — 毎日朝4:30から営業"),
  ("早朝の気温", "10〜15°Cくらいのことが多い — 上着はすぐ出せる所に"),
 ],
 "secs": [
  ("ホーチミンからの夜行バス：何時に着く？", "<p>寝台バスは夕方から夜にホーチミンを出発し、約300kmを6〜8時間ほどで走ります。到着時刻はバス会社、交通状況、山道の天気によって変わりますが、多くの夜行便は朝4:00〜7:00ごろダラットに入ります。</p><p>予約のときに、ダラットのどこで降りるのか確認しましょう。Tô Hiến Thành通りの長距離バスターミナル、市内にある会社のオフィス、または一部のリムジンバンならホテルまで送ってくれます。ターミナルと主なバス会社のオフィスは<a href=\"{MAP:busmap}\">ダラット〜サイゴン バスマップ</a>で見られます。ダナンやホイアンから来る方は<a href=\"{MAP:danangbusmap}\">ダラット〜ダナン バスマップ</a>をどうぞ。</p>"),
  ("ニャチャンから：日中のバス", "<p>ニャチャンはもっと近く、景色のよい峠を越えて約135〜140km、3.5〜4時間ほど。バスは日中に走るので、たいてい午前遅くか午後にダラットに着きます。主な会社のオフィスは<a href=\"{MAP:nhatrangbusmap}\">ニャチャン〜ダラット バスマップ</a>に、行き方は<a href=\"{ART:getting}\">ダラットへの行き方</a>にまとめています。</p><p>知っておきたいこと：レンタルの1日は受け取りからその日の21:00までです。16時に着いてすぐ借りても1日分になります。多くのお客様はチェックインして休み、翌朝4:30以降に受け取りに来ます。2日以上のレンタルなら、ダラット中心部のホテルまで無料でお届けします。</p>"),
  ("バスを降りてからスクーターに乗るまで", "<ol><li><b>前日の夜：</b>WhatsApp（+84 944 081 101 または +84 834 622 149）、Telegram（@vanphudalat）、WeChat（vanphudalat）で、バス会社、到着予定時刻、希望の車種を教えてください。</li><li><b>バスを降りたら</b>タクシーかGrabで 1/15/5 Thông Thiên Học へ。夜明け前はGrabがつかまりにくいことがあり、タクシーはたいていターミナルで待っています。</li><li><b>手続きは数分：</b>パスポート（現金のデポジットなし）と、全車種1日150,000 VND。</li><li><b>短い試乗</b>と、車両の状態を一緒に撮る動画。</li><li><b>出発。</b>レンタルの1日は21:00までなので、4:30に借りたスクーターは丸一日使えます。</li></ol>"),
  ("最初の数時間：日の出か、まず休むか？", "<ul><li><b>バスでよく眠れた？</b>ダラットのいちばん美しい光は今です。<a href=\"{ART:cloudhunt}\">雲海ハンティング</a>や<a href=\"{ART:caudat}\">カウダット茶畑の日の出</a>へ。坂が多いのでHonda Air Blade 125ccがおすすめです。</li><li><b>よく眠れなかった？</b>疲れたまま霧の出た濡れた山道を走らないでください。温かいコーヒーと朝ごはんで目を覚ましてから出発しましょう。</li><li><b>大きなスーツケースがある？</b>スクーターには載せないでください。まずホテルに預けるか（チェックイン前でも荷物を預かってくれるホテルは多いです）、2日以上借りて中心部のホテルまで無料でお届けを。</li><li>ヘルメットを着用し、飲酒運転はせず、ベトナムの交通法規を必ず守ってください。</li></ul><p>早く出かけたい理由はほかにも：<a href=\"{ART:lt-early}\">ダラットの早朝バイクレンタル</a>。</p>"),
 ],
 "faq_h": "よくある質問",
 "faq": [
  ("ホーチミン発の夜行バスは何時にダラットに着きますか？", "だいたい朝4:00〜7:00ごろです。バス会社、交通状況、山道の天気によって変わるので、予約時に到着予定を確認してください。"),
  ("ダラットではどこで降ろしてもらえますか？", "Tô Hiến Thành通りのダラット長距離バスターミナル（24時間）か、市内のバス会社のオフィスです。一部のリムジンバンはホテルまで送ってくれます。予約時に確認しましょう。"),
  ("朝4:30にスクーターを借りられますか？", "はい。当店は毎日朝4:30に開きます。前日の夜に到着時刻と車種を教えていただければ、準備しておきます。"),
  ("バスターミナルまでバイクを届けてもらえますか？", "無料配達は2日以上のレンタルで、ダラット中心部のホテルが対象です。それ以外は予定を送っていただければ、対応できるかお知らせします。"),
  ("ニャチャンから午後に着きます。今日借りる？明日借りる？", "レンタルの1日は21:00までなので、夕方に受け取っても1日分です。翌朝から使うなら4:30以降に受け取るか、2日以上借りて中心部のホテルへの無料配達をご利用ください。"),
 ],
 "more_h": "旅の計画を続けよう",
 "more": [("{ART:getting}", "ダラットへの行き方"), ("{MAP:busmap}", "ダラット〜サイゴン バスマップ"), ("{MAP:nhatrangbusmap}", "ニャチャン〜ダラット バスマップ"), ("{ART:lt-early}", "朝4:30からのバイクレンタル"), ("{HOME}", "ダラットのバイクレンタル — 車種と料金")],
}

T["th"] = {
 "title": "นั่งรถทัวร์กลางคืนถึงดาลัดตี 4–5 ทำอะไรดี? | Van Phu",
 "desc": "รถบัสนอนกลางคืนจากโฮจิมินห์มักถึงดาลัดราวตี 4–7 โมงเช้า จอดที่ไหน เข้าเมืองยังไง และรับสกู๊ตเตอร์ได้ตั้งแต่ตี 4:30",
 "h1": "นั่งรถทัวร์กลางคืนถึงดาลัดตอนเช้ามืด: ควรทำอะไร",
 "crumb": "ถึงดาลัดตอนเช้ามืด",
 "lead": "รถบัสนอนกลางคืนจากโฮจิมินห์มักถึงดาลัดราว<b>ตี 4 ถึง 7 โมงเช้า</b> ตอนที่เมืองยังไม่ตื่น ร้านเช่ารถของเราเปิด<b>ตั้งแต่ตี 4:30 ทุกวัน</b> ลงรถไม่นานคุณก็ขี่สกู๊ตเตอร์ออกเที่ยวได้เลย มาดูวิธีจัดการเช้าวันแรกกัน",
 "short_h": "สรุปสั้น ๆ",
 "short": [
  ("โฮจิมินห์ → ดาลัด", "ประมาณ 300 กม.; รถบัสนอนประมาณ 6–8 ชั่วโมง; รอบกลางคืนมักถึงราว 4:00–7:00"),
  ("ญาจาง → ดาลัด", "ประมาณ 135–140 กม.; ประมาณ 3.5–4 ชั่วโมง; รถวิ่งตอนกลางวัน"),
  ("รถจอดที่ไหน", "สถานีขนส่งระหว่างจังหวัดดาลัด (1 Tô Hiến Thành เปิด 24 ชั่วโมง) หรือสำนักงานของบริษัทรถเอง"),
  ("สถานีขนส่ง → ร้านเรา", "ประมาณ 3 กม. แบบเส้นตรง ทางจริงไกลกว่านิดหน่อย — แท็กซี่หรือ Grab"),
  ("ร้านของเรา", "1/15/5 Thông Thiên Học — เปิดตี 4:30 ทุกวัน"),
  ("อุณหภูมิตอนเช้ามืด", "มักราว 10–15 °C — เอาเสื้อกันหนาวไว้ใกล้มือ"),
 ],
 "secs": [
  ("รถกลางคืนจากโฮจิมินห์: ถึงกี่โมง", "<p>รถบัสนอนออกจากโฮจิมินห์ช่วงเย็นถึงค่ำ วิ่งประมาณ 300 กม. ใช้เวลาราว 6–8 ชั่วโมง เวลาถึงจริงขึ้นกับบริษัทรถ สภาพการจราจร และอากาศบนถนนภูเขา แต่รถกลางคืนส่วนใหญ่เข้าดาลัดช่วงตี 4 ถึง 7 โมงเช้า</p><p>ตอนจองตั๋ว ถามให้ชัดว่ารถจอดที่ไหนในดาลัด: สถานีขนส่งบนถนน Tô Hiến Thành สำนักงานของบริษัทในเมือง หรือรถตู้ลีมูซีนบางเจ้าส่งถึงโรงแรม ดูสถานีขนส่งและสำนักงานบริษัทหลักได้บน<a href=\"{MAP:busmap}\">แผนที่รถบัสดาลัด – ไซ่ง่อน</a> มาจากดานังหรือฮอยอัน? ดู<a href=\"{MAP:danangbusmap}\">แผนที่รถบัสดาลัด – ดานัง</a></p>"),
  ("จากญาจาง: รถรอบกลางวัน", "<p>ญาจางใกล้กว่า — ประมาณ 135–140 กม. ข้ามช่องเขาวิวสวย ราว 3.5–4 ชั่วโมง — และรถวิ่งตอนกลางวัน จึงมักถึงดาลัดช่วงสายหรือบ่าย สำนักงานบริษัทหลักอยู่บน<a href=\"{MAP:nhatrangbusmap}\">แผนที่รถบัสญาจาง – ดาลัด</a> และวิธีเดินทางอยู่ในบทความ<a href=\"{ART:getting}\">วิธีเดินทางไปดาลัด</a></p><p>ควรรู้: การเช่า 1 วันนับจากเวลารับรถถึง 21:00 ของวันนั้น ถ้าถึง 16:00 แล้วรับรถทันทีก็ยังนับเป็น 1 วันเต็ม ลูกค้าหลายคนเช็กอิน พักผ่อน แล้วมารับรถเช้าวันถัดไปตั้งแต่ตี 4:30 เช่า 2 วันขึ้นไป เราส่งรถฟรีถึงโรงแรมในตัวเมืองดาลัด</p>"),
  ("จากลงรถทัวร์ถึงได้ขี่สกู๊ตเตอร์", "<ol><li><b>เย็นวันก่อน:</b> ทักเราทาง WhatsApp (+84 944 081 101 หรือ +84 834 622 149), Telegram (@vanphudalat) หรือ WeChat (vanphudalat) บอกบริษัทรถ เวลาถึงโดยประมาณ และรุ่นรถที่ต้องการ</li><li><b>ลงรถแล้ว</b> นั่งแท็กซี่หรือ Grab มาที่ 1/15/5 Thông Thiên Học ก่อนฟ้าสางเรียก Grab อาจยาก ส่วนแท็กซี่มักจอดรออยู่ที่สถานีขนส่ง</li><li><b>เอกสารไม่กี่นาที:</b> พาสปอร์ต (ไม่มีมัดจำเงินสด) และทุกคัน 150,000 VND ต่อวัน</li><li><b>ลองขี่สั้น ๆ</b> และถ่ายวิดีโอสภาพรถด้วยกัน</li><li><b>ออกเดินทาง</b> การเช่า 1 วันถึง 21:00 รถที่รับตอนตี 4:30 จึงใช้ได้ทั้งวัน</li></ol><p>จำไว้ว่าเวียดนามขับรถชิดขวา</p>"),
  ("ชั่วโมงแรก: ไปดูพระอาทิตย์ขึ้น หรือพักก่อน?", "<ul><li><b>หลับสบายบนรถ?</b> แสงที่สวยที่สุดของดาลัดคือตอนนี้ ไป<a href=\"{ART:cloudhunt}\">ล่าทะเลหมอก</a>หรือ<a href=\"{ART:caudat}\">ดูพระอาทิตย์ขึ้นที่ไร่ชาเกาดัต</a> — ทางขึ้นเขาแบบนี้แนะนำ Honda Air Blade 125cc</li><li><b>นอนไม่ค่อยหลับ?</b> อย่าเพิ่งขี่ถนนภูเขาที่มีหมอกและเปียกตอนเหนื่อย ดื่มกาแฟร้อน กินอาหารเช้าก่อน สดชื่นแล้วค่อยไป</li><li><b>มีกระเป๋าเดินทางใบใหญ่?</b> อย่าบรรทุกบนสกู๊ตเตอร์ ฝากไว้ที่โรงแรมก่อน — หลายโรงแรมรับฝากกระเป๋าก่อนเช็กอิน — หรือเช่า 2 วันขึ้นไปแล้วให้เราส่งรถฟรีถึงโรงแรมในเมือง</li><li>สวมหมวกกันน็อก ห้ามดื่มแอลกอฮอล์หรือเบียร์ขณะขี่ และปฏิบัติตามกฎจราจรเวียดนามอย่างเคร่งครัด</li></ul><p>เหตุผลที่ควรออกแต่เช้าเพิ่มเติม: <a href=\"{ART:lt-early}\">เช่ามอเตอร์ไซค์ดาลัดร้านเปิดเช้า</a></p>"),
 ],
 "faq_h": "คำถามที่พบบ่อย",
 "faq": [
  ("รถทัวร์กลางคืนจากโฮจิมินห์ถึงดาลัดกี่โมง?", "ปกติราวตี 4 ถึง 7 โมงเช้า ขึ้นกับบริษัทรถ การจราจร และอากาศบนถนนภูเขา ถามเวลาถึงโดยประมาณจากบริษัทตอนจองตั๋ว"),
  ("รถจอดส่งที่ไหนในดาลัด?", "ที่สถานีขนส่งระหว่างจังหวัดดาลัดบนถนน Tô Hiến Thành (เปิด 24 ชั่วโมง) หรือสำนักงานของบริษัทรถในเมือง รถตู้ลีมูซีนบางเจ้าส่งถึงโรงแรม ถามตอนจองได้เลย"),
  ("เช่าสกู๊ตเตอร์ตอนตี 4:30 ได้ไหม?", "ได้ ร้านเราเปิดตี 4:30 ทุกวัน บอกเวลาถึงและรุ่นรถไว้ตั้งแต่เย็นวันก่อน รถจะพร้อมเมื่อคุณมาถึง"),
  ("ส่งรถไปที่สถานีขนส่งได้ไหม?", "ส่งรถฟรีสำหรับโรงแรมในตัวเมืองดาลัดเมื่อเช่า 2 วันขึ้นไป กรณีอื่นส่งแผนเดินทางมา แล้วเราจะบอกว่าทำได้หรือไม่"),
  ("ถึงจากญาจางตอนบ่าย รับรถวันนี้หรือพรุ่งนี้ดี?", "การเช่า 1 วันถึง 21:00 รับรถตอนบ่ายแก่ก็นับเป็นวันเต็ม ถ้าต้องใช้รถตั้งแต่เช้าวันถัดไป ให้มารับตั้งแต่ตี 4:30 — หรือเช่า 2 วันขึ้นไปเพื่อรับบริการส่งรถฟรีถึงโรงแรมในเมือง"),
 ],
 "more_h": "วางแผนเที่ยวต่อ",
 "more": [("{ART:getting}", "วิธีเดินทางไปดาลัด"), ("{MAP:busmap}", "แผนที่รถบัสดาลัด – ไซ่ง่อน"), ("{MAP:nhatrangbusmap}", "แผนที่รถบัสญาจาง – ดาลัด"), ("{ART:lt-early}", "เช่ารถร้านเปิดตี 4:30"), ("{HOME}", "เช่ามอเตอร์ไซค์ดาลัด — รุ่นรถและราคา")],
}

T["id"] = {
 "title": "Tiba di Da Lat Subuh Naik Bus Malam: Ngapain Jam 4–5? | Van Phu",
 "desc": "Bus malam dari Ho Chi Minh City biasanya tiba di Da Lat sekitar jam 4–7 pagi. Turun di mana, cara ke pusat kota, dan ambil skuter mulai jam 4.30.",
 "h1": "Tiba di Da Lat Subuh Naik Bus Malam: Apa yang Harus Dilakukan",
 "crumb": "Tiba di Da Lat subuh",
 "lead": "Bus tidur malam dari Ho Chi Minh City biasanya tiba di Da Lat sekitar <b>jam 4.00–7.00 pagi</b>, saat kota belum bangun. Toko sewa kami buka <b>mulai jam 4.30 setiap hari</b>, jadi tak lama setelah turun dari bus kamu sudah bisa naik skuter. Begini cara mengatur pagi pertamamu.",
 "short_h": "Sekilas",
 "short": [
  ("Ho Chi Minh City → Da Lat", "Sekitar 300 km; bus tidur sekitar 6–8 jam; bus malam biasanya tiba sekitar 04.00–07.00"),
  ("Nha Trang → Da Lat", "Sekitar 135–140 km; sekitar 3,5–4 jam; bus berangkat siang hari"),
  ("Tempat bus berhenti", "Terminal bus antarkota Da Lat (1 Tô Hiến Thành, buka 24 jam) atau kantor perusahaan bus sendiri"),
  ("Terminal → toko kami", "Sekitar 3 km garis lurus, lewat jalan sedikit lebih jauh — taksi atau Grab"),
  ("Toko kami", "1/15/5 Thông Thiên Học — buka jam 4.30 setiap hari"),
  ("Suhu subuh", "Sering sekitar 10–15 °C — taruh jaket di tempat yang mudah diambil"),
 ],
 "secs": [
  ("Bus malam dari Ho Chi Minh City: jam berapa sampai", "<p>Bus tidur berangkat dari Ho Chi Minh City sore atau malam hari dan menempuh sekitar 300 km dalam 6–8 jam. Jam tiba sebenarnya tergantung perusahaan, lalu lintas dan cuaca di jalan pegunungan, tapi kebanyakan bus malam masuk Da Lat antara sekitar jam 4.00 dan 7.00.</p><p>Saat pesan tiket, tanyakan di mana bus berhenti di Da Lat: terminal antarkota di Jalan Tô Hiến Thành, kantor perusahaan di kota, atau — untuk beberapa van limosin — langsung di hotel. Terminal dan kantor perusahaan utama ada di <a href=\"{MAP:busmap}\">peta bus Da Lat – Saigon</a> kami. Datang dari Da Nang atau Hoi An? Lihat <a href=\"{MAP:danangbusmap}\">peta bus Da Lat – Da Nang</a>.</p>"),
  ("Dari Nha Trang: bus siang hari", "<p>Nha Trang lebih dekat — sekitar 135–140 km lewat jalur pegunungan yang indah, kira-kira 3,5–4 jam — dan busnya jalan siang hari, jadi biasanya kamu tiba di Da Lat menjelang siang atau sore. Kantor perusahaan utama ada di <a href=\"{MAP:nhatrangbusmap}\">peta bus Nha Trang – Da Lat</a>, dan pilihan perjalanan ada di artikel <a href=\"{ART:getting}\">cara ke Da Lat</a>.</p><p>Perlu diketahui: satu hari sewa dihitung dari saat ambil motor sampai jam 21.00. Kalau tiba jam 16.00 lalu langsung ambil motor, tetap dihitung satu hari penuh. Banyak tamu check-in dan istirahat dulu, lalu ambil motor besok paginya mulai jam 4.30. Sewa 2 hari atau lebih? Motor kami antar gratis ke hotel di pusat Da Lat.</p>"),
  ("Dari turun bus sampai naik skuter", "<ol><li><b>Malam sebelumnya:</b> kirim pesan WhatsApp (+84 944 081 101 atau +84 834 622 149) atau Telegram (@vanphudalat): nama perusahaan bus, perkiraan jam tiba dan motor yang kamu mau.</li><li><b>Setelah turun bus,</b> naik taksi atau Grab ke 1/15/5 Thông Thiên Học. Sebelum subuh Grab kadang susah didapat; taksi biasanya menunggu di terminal.</li><li><b>Urusan administrasi beberapa menit:</b> paspor (tanpa deposit uang tunai) dan 150.000 VND per hari untuk semua motor.</li><li><b>Coba jalan sebentar</b> dan rekam video kondisi motor bersama-sama.</li><li><b>Berangkat.</b> Satu hari sewa sampai jam 21.00, jadi motor yang diambil jam 4.30 bisa dipakai seharian.</li></ol><p>Ingat, di Vietnam kendaraan berjalan di sisi kanan.</p>"),
  ("Jam-jam pertama: lihat sunrise atau istirahat dulu?", "<ul><li><b>Tidur nyenyak di bus?</b> Cahaya terbaik Da Lat ada sekarang. Pergilah <a href=\"{ART:cloudhunt}\">berburu awan</a> atau ke <a href=\"{ART:caudat}\">kebun teh Cau Dat saat matahari terbit</a> — untuk tanjakan ini pakai Honda Air Blade 125cc.</li><li><b>Kurang tidur?</b> Jangan langsung lewat jalan gunung yang berkabut dan basah saat masih lelah. Minum kopi panas dan sarapan dulu, berangkat setelah segar.</li><li><b>Bawa koper besar?</b> Jangan dibawa naik skuter. Titipkan dulu di hotel — banyak hotel mau menyimpan barang sebelum check-in — atau sewa 2+ hari dan kami antar motor gratis ke hotelmu di pusat kota.</li><li>Pakai helm, jangan minum alkohol atau bir saat berkendara, dan patuhi hukum lalu lintas Vietnam dengan ketat.</li></ul><p>Alasan lain untuk berangkat pagi: <a href=\"{ART:lt-early}\">sewa motor di Da Lat yang buka pagi</a>.</p>"),
 ],
 "faq_h": "Pertanyaan yang sering diajukan",
 "faq": [
  ("Jam berapa bus malam dari Ho Chi Minh City tiba di Da Lat?", "Biasanya sekitar jam 4.00 sampai 7.00 pagi, tergantung perusahaan, lalu lintas dan cuaca di jalan pegunungan. Tanyakan perkiraan jam tiba saat pesan tiket."),
  ("Di mana bus menurunkan penumpang di Da Lat?", "Di terminal bus antarkota Da Lat di Jalan Tô Hiến Thành (buka 24 jam) atau di kantor perusahaan bus di kota. Beberapa van limosin mengantar sampai hotel. Tanyakan saat pesan."),
  ("Bisa sewa skuter jam 4.30 pagi?", "Bisa. Toko kami buka jam 4.30 setiap hari. Kabari kami malam sebelumnya jam tiba dan motor yang dimau, motornya akan siap saat kamu datang."),
  ("Bisa antar motor ke terminal bus?", "Antar gratis berlaku untuk hotel di pusat Da Lat dengan sewa 2 hari atau lebih. Untuk yang lain, kirim rencanamu dan kami kabari apa yang bisa."),
  ("Saya tiba dari Nha Trang sore hari. Ambil motor hari ini atau besok?", "Satu hari sewa sampai jam 21.00, jadi ambil motor sore hari tetap dihitung satu hari penuh. Kalau motornya baru dipakai besok pagi, ambil mulai jam 4.30 — atau sewa 2+ hari dan dapat antar gratis ke hotel di pusat kota."),
 ],
 "more_h": "Rencanakan perjalananmu",
 "more": [("{ART:getting}", "Cara ke Da Lat"), ("{MAP:busmap}", "Peta bus Da Lat – Saigon"), ("{MAP:nhatrangbusmap}", "Peta bus Nha Trang – Da Lat"), ("{ART:lt-early}", "Sewa motor buka jam 4.30"), ("{HOME}", "Sewa motor Da Lat — motor dan harga")],
}

T["ms"] = {
 "title": "Tiba di Da Lat Awal Pagi dengan Bas Malam: Apa Nak Buat? | Van Phu",
 "desc": "Bas malam dari Ho Chi Minh City biasanya tiba di Da Lat kira-kira jam 4–7 pagi. Di mana bas berhenti, cara ke pusat bandar dan ambil skuter dari jam 4:30 pagi.",
 "h1": "Tiba di Da Lat Awal Pagi dengan Bas Malam: Apa Perlu Dibuat",
 "crumb": "Tiba di Da Lat awal pagi",
 "lead": "Bas tidur malam dari Ho Chi Minh City biasanya tiba di Da Lat kira-kira <b>jam 4:00–7:00 pagi</b>, ketika bandar masih tidur. Kedai sewa kami dibuka <b>dari jam 4:30 pagi setiap hari</b>, jadi tidak lama selepas turun bas anda sudah boleh menunggang skuter. Begini cara mengatur pagi pertama anda.",
 "short_h": "Ringkasan",
 "short": [
  ("Ho Chi Minh City → Da Lat", "Kira-kira 300 km; bas tidur kira-kira 6–8 jam; bas malam biasanya tiba kira-kira 4:00–7:00"),
  ("Nha Trang → Da Lat", "Kira-kira 135–140 km; kira-kira 3.5–4 jam; bas bergerak pada siang hari"),
  ("Tempat bas berhenti", "Stesen bas antara bandar Da Lat (1 Tô Hiến Thành, dibuka 24 jam) atau pejabat syarikat bas sendiri"),
  ("Stesen bas → kedai kami", "Kira-kira 3 km garis lurus, ikut jalan sedikit lebih jauh — teksi atau Grab"),
  ("Kedai kami", "1/15/5 Thông Thiên Học — dibuka 4:30 pagi setiap hari"),
  ("Suhu awal pagi", "Selalunya kira-kira 10–15 °C — letak jaket di tempat mudah dicapai"),
 ],
 "secs": [
  ("Bas malam dari Ho Chi Minh City: pukul berapa sampai", "<p>Bas tidur bertolak dari Ho Chi Minh City pada waktu petang atau malam dan menempuh kira-kira 300 km dalam 6–8 jam. Waktu tiba sebenar bergantung pada syarikat, trafik dan cuaca di jalan pergunungan, tetapi kebanyakan bas malam masuk ke Da Lat antara kira-kira jam 4:00 dan 7:00 pagi.</p><p>Semasa menempah, tanya di mana bas berhenti di Da Lat: stesen bas antara bandar di Jalan Tô Hiến Thành, pejabat syarikat di bandar, atau — bagi sesetengah van limosin — terus di hotel. Stesen bas dan pejabat syarikat utama ada pada <a href=\"{MAP:busmap}\">peta bas Da Lat – Saigon</a> kami. Datang dari Da Nang atau Hoi An? Lihat <a href=\"{MAP:danangbusmap}\">peta bas Da Lat – Da Nang</a>.</p>"),
  ("Dari Nha Trang: bas siang hari", "<p>Nha Trang lebih dekat — kira-kira 135–140 km melalui laluan gunung yang cantik, lebih kurang 3.5–4 jam — dan bas bergerak pada siang hari, jadi biasanya anda tiba di Da Lat lewat pagi atau petang. Pejabat syarikat utama ada pada <a href=\"{MAP:nhatrangbusmap}\">peta bas Nha Trang – Da Lat</a>, dan pilihan perjalanan dalam artikel <a href=\"{ART:getting}\">cara ke Da Lat</a>.</p><p>Perlu tahu: satu hari sewa dikira dari masa ambil motosikal hingga jam 21:00. Jika tiba jam 16:00 dan terus ambil motosikal, ia tetap dikira satu hari penuh. Ramai tetamu daftar masuk dan berehat dahulu, kemudian ambil motosikal keesokan pagi dari jam 4:30. Sewa 2 hari atau lebih? Kami hantar percuma ke hotel di pusat bandar Da Lat.</p>"),
  ("Dari turun bas hingga menunggang skuter", "<ol><li><b>Malam sebelumnya:</b> mesej kami di WhatsApp (+84 944 081 101 atau +84 834 622 149) atau Telegram (@vanphudalat): syarikat bas, anggaran waktu tiba dan motosikal yang anda mahu.</li><li><b>Selepas turun bas,</b> naik teksi atau Grab ke 1/15/5 Thông Thiên Học. Sebelum subuh Grab kadang-kadang sukar didapati; teksi biasanya menunggu di stesen bas.</li><li><b>Urusan beberapa minit:</b> pasport (tiada deposit tunai) dan 150,000 VND sehari untuk semua motosikal.</li><li><b>Cubaan tunggang sebentar</b> dan video keadaan motosikal yang kita rakam bersama.</li><li><b>Mula perjalanan.</b> Satu hari sewa hingga jam 21:00, jadi motosikal yang diambil jam 4:30 boleh digunakan sepanjang hari.</li></ol><p>Ingat, Vietnam memandu di sebelah kanan jalan.</p>"),
  ("Jam-jam pertama: lihat matahari terbit atau rehat dahulu?", "<ul><li><b>Tidur lena dalam bas?</b> Cahaya terindah Da Lat ialah sekarang. Pergi <a href=\"{ART:cloudhunt}\">memburu awan</a> atau ke <a href=\"{ART:caudat}\">ladang teh Cau Dat waktu matahari terbit</a> — untuk bukit ini pilih Honda Air Blade 125cc.</li><li><b>Kurang tidur?</b> Jangan terus menunggang di jalan gunung yang berkabus dan basah ketika letih. Minum kopi panas dan sarapan dahulu, kemudian bertolak bila sudah segar.</li><li><b>Bawa beg besar?</b> Jangan bawa atas skuter. Tinggalkan di hotel dahulu — banyak hotel boleh simpan beg sebelum daftar masuk — atau sewa 2+ hari dan kami hantar motosikal percuma ke hotel anda di pusat bandar.</li><li>Pakai topi keledar, jangan minum alkohol atau bir semasa menunggang, dan patuhi undang-undang lalu lintas Vietnam dengan ketat.</li></ul><p>Sebab lain untuk keluar awal: <a href=\"{ART:lt-early}\">sewa motosikal di Da Lat yang dibuka awal pagi</a>.</p>"),
 ],
 "faq_h": "Soalan lazim",
 "faq": [
  ("Pukul berapa bas malam dari Ho Chi Minh City tiba di Da Lat?", "Biasanya kira-kira jam 4:00 hingga 7:00 pagi, bergantung pada syarikat, trafik dan cuaca di jalan pergunungan. Tanya anggaran waktu tiba semasa menempah."),
  ("Di mana bas menurunkan penumpang di Da Lat?", "Di stesen bas antara bandar Da Lat di Jalan Tô Hiến Thành (dibuka 24 jam) atau di pejabat syarikat bas di bandar. Sesetengah van limosin menghantar ke hotel. Tanya semasa menempah."),
  ("Boleh sewa skuter jam 4:30 pagi?", "Boleh. Kedai kami dibuka jam 4:30 pagi setiap hari. Beritahu kami malam sebelumnya waktu tiba dan motosikal yang dimahukan, dan ia akan sedia bila anda sampai."),
  ("Boleh hantar motosikal ke stesen bas?", "Penghantaran percuma untuk hotel di pusat bandar Da Lat bagi sewaan 2 hari atau lebih. Untuk lain-lain, hantar rancangan anda dan kami beritahu apa yang boleh dibuat."),
  ("Saya tiba dari Nha Trang waktu petang. Ambil motosikal hari ini atau esok?", "Satu hari sewa hingga jam 21:00, jadi ambil lewat petang tetap dikira satu hari penuh. Jika hanya perlu dari pagi esok, ambil dari jam 4:30 — atau sewa 2+ hari untuk penghantaran percuma ke hotel di pusat bandar."),
 ],
 "more_h": "Rancang perjalanan seterusnya",
 "more": [("{ART:getting}", "Cara ke Da Lat"), ("{MAP:busmap}", "Peta bas Da Lat – Saigon"), ("{MAP:nhatrangbusmap}", "Peta bas Nha Trang – Da Lat"), ("{ART:lt-early}", "Sewa motosikal dibuka 4:30 pagi"), ("{HOME}", "Sewa motosikal Da Lat — motosikal dan harga")],
}

T["de"] = {
 "title": "Mit dem Nachtbus früh in Da Lat: Was tun um 4–5 Uhr? | Van Phu",
 "desc": "Nachtbusse aus Ho-Chi-Minh-Stadt erreichen Da Lat meist gegen 4–7 Uhr. Wo sie halten, wie du ins Zentrum kommst und wie du ab 4:30 Uhr einen Roller abholst.",
 "h1": "Mit dem Nachtbus früh in Da Lat angekommen: Was tun?",
 "crumb": "Früh in Da Lat ankommen",
 "lead": "Der Nacht-Schlafbus aus Ho-Chi-Minh-Stadt kommt meist zwischen etwa <b>4 und 7 Uhr morgens</b> in Da Lat an — bevor die Stadt aufwacht. Unser Verleih öffnet <b>jeden Tag um 4:30 Uhr</b>, du kannst also kurz nach dem Aussteigen auf dem Roller sitzen. So läuft der erste Morgen.",
 "short_h": "Auf einen Blick",
 "short": [
  ("Ho-Chi-Minh-Stadt → Da Lat", "Etwa 300 km; Schlafbus etwa 6–8 Stunden; Nachtbusse kommen meist gegen 4:00–7:00 an"),
  ("Nha Trang → Da Lat", "Etwa 135–140 km; etwa 3,5–4 Stunden; Busse fahren tagsüber"),
  ("Wo die Busse halten", "Überlandbusbahnhof Da Lat (1 Tô Hiến Thành, rund um die Uhr geöffnet) oder das eigene Büro der Busgesellschaft"),
  ("Busbahnhof → unser Laden", "Etwa 3 km Luftlinie, auf der Straße etwas mehr — Taxi oder Grab"),
  ("Unser Laden", "1/15/5 Thông Thiên Học — öffnet jeden Tag um 4:30 Uhr"),
  ("Temperatur am frühen Morgen", "Oft etwa 10–15 °C — die Jacke griffbereit halten"),
 ],
 "secs": [
  ("Nachtbus aus Ho-Chi-Minh-Stadt: wann du ankommst", "<p>Schlafbusse starten abends in Ho-Chi-Minh-Stadt und brauchen für die rund 300 km etwa 6–8 Stunden. Die genaue Ankunft hängt von der Gesellschaft, vom Verkehr und vom Wetter auf der Bergstraße ab, aber die meisten Nachtbusse erreichen Da Lat zwischen etwa 4 und 7 Uhr.</p><p>Frag beim Buchen, wo der Bus in Da Lat hält: am Überlandbusbahnhof an der Tô Hiến Thành, am eigenen Büro der Gesellschaft in der Stadt oder — bei manchen Limousinen-Vans — direkt am Hotel. Busbahnhof und die wichtigsten Büros findest du auf unserer <a href=\"{MAP:busmap}\">Buskarte Da Lat – Saigon</a>. Kommst du aus Da Nang oder Hoi An? Dann schau auf die <a href=\"{MAP:danangbusmap}\">Buskarte Da Lat – Da Nang</a>.</p>"),
  ("Aus Nha Trang: ein Tagbus", "<p>Nha Trang liegt näher — etwa 135–140 km über einen schönen Bergpass, rund 3,5–4 Stunden — und die Busse fahren tagsüber, du kommst also meist am späten Vormittag oder Nachmittag an. Die Büros der wichtigsten Gesellschaften stehen auf der <a href=\"{MAP:nhatrangbusmap}\">Buskarte Nha Trang – Da Lat</a>, die Anreisemöglichkeiten im Artikel <a href=\"{ART:getting}\">wie du nach Da Lat kommst</a>.</p><p>Gut zu wissen: Ein Miettag läuft von der Abholung bis 21:00 Uhr. Kommst du um 16 Uhr an und holst den Roller sofort, zählt das trotzdem als voller Tag. Viele Gäste checken ein, ruhen sich aus und holen den Roller am nächsten Morgen ab 4:30 Uhr. Mietest du 2 Tage oder länger, bringen wir den Roller kostenlos zu deinem Hotel im Zentrum.</p>"),
  ("Vom Bus auf den Roller — Schritt für Schritt", "<ol><li><b>Am Abend vorher:</b> schreib uns per WhatsApp (+84 944 081 101 oder +84 834 622 149) oder Telegram (@vanphudalat) die Busgesellschaft, deine ungefähre Ankunftszeit und das gewünschte Bike.</li><li><b>Nach dem Aussteigen</b> nimm ein Taxi oder Grab zur 1/15/5 Thông Thiên Học. Vor Sonnenaufgang ist Grab oft schwer zu bekommen; Taxis warten meist am Busbahnhof.</li><li><b>Formalitäten in wenigen Minuten:</b> dein Reisepass (keine Barkaution) und 150.000 VND pro Tag für jedes Bike.</li><li><b>Kurze Probefahrt</b> und ein gemeinsames Video vom Zustand des Bikes.</li><li><b>Los geht's.</b> Ein Miettag läuft bis 21:00 Uhr, ein um 4:30 Uhr abgeholter Roller gehört dir also den ganzen Tag.</li></ol>"),
  ("Die ersten Stunden: Sonnenaufgang oder erst ausruhen?", "<ul><li><b>Im Bus gut geschlafen?</b> Jetzt ist das schönste Licht in Da Lat. Fahr zur <a href=\"{ART:cloudhunt}\">Wolkenjagd</a> oder zum <a href=\"{ART:caudat}\">Sonnenaufgang über den Teehügeln von Cau Dat</a> — für diese Steigungen nimm die Honda Air Blade 125cc.</li><li><b>Schlecht geschlafen?</b> Fahr nicht müde auf nassen, nebligen Bergstraßen los. Erst heißer Kaffee und Frühstück, dann aufs Bike, wenn du wach bist.</li><li><b>Großer Koffer?</b> Nicht auf dem Roller transportieren. Erst im Hotel abgeben — viele Hotels bewahren Gepäck vor dem Check-in auf — oder 2+ Tage mieten, dann bringen wir den Roller kostenlos zu deinem Hotel im Zentrum.</li><li>Helm tragen, kein Alkohol oder Bier beim Fahren und die vietnamesischen Verkehrsregeln strikt einhalten.</li></ul><p>Noch mehr Gründe für einen frühen Start: <a href=\"{ART:lt-early}\">Roller früh am Morgen mieten in Da Lat</a>.</p>"),
 ],
 "faq_h": "Häufige Fragen",
 "faq": [
  ("Wann kommt der Nachtbus aus Ho-Chi-Minh-Stadt in Da Lat an?", "Meist zwischen etwa 4 und 7 Uhr morgens. Das hängt von der Gesellschaft, vom Verkehr und vom Wetter auf der Bergstraße ab — frag beim Buchen nach der geschätzten Ankunft."),
  ("Wo lässt mich der Bus in Da Lat raus?", "Am Überlandbusbahnhof Da Lat an der Tô Hiến Thành (rund um die Uhr geöffnet) oder am eigenen Büro der Gesellschaft in der Stadt. Manche Limousinen-Vans fahren bis zum Hotel. Frag beim Buchen."),
  ("Kann ich um 4:30 Uhr einen Roller mieten?", "Ja. Unser Laden öffnet jeden Tag um 4:30 Uhr. Schreib uns am Vorabend deine Ankunftszeit und das Bike, dann steht es bereit."),
  ("Bringt ihr den Roller zum Busbahnhof?", "Die kostenlose Lieferung gilt für Hotels im Zentrum von Da Lat bei Mieten ab 2 Tagen. Für alles andere schick uns deinen Plan, und wir sagen dir, was möglich ist."),
  ("Ich komme nachmittags aus Nha Trang. Heute oder morgen abholen?", "Ein Miettag läuft bis 21:00 Uhr, eine Abholung am späten Nachmittag zählt also als voller Tag. Brauchst du den Roller erst ab dem nächsten Morgen, hol ihn ab 4:30 Uhr — oder miete 2+ Tage mit kostenloser Lieferung ins Hotel im Zentrum."),
 ],
 "more_h": "Plane weiter",
 "more": [("{ART:getting}", "Wie du nach Da Lat kommst"), ("{MAP:busmap}", "Buskarte Da Lat – Saigon"), ("{MAP:nhatrangbusmap}", "Buskarte Nha Trang – Da Lat"), ("{ART:lt-early}", "Roller mieten ab 4:30 Uhr"), ("{HOME}", "Roller mieten in Da Lat — Bikes und Preise")],
}

T["fr"] = {
 "title": "Arriver tôt à Da Lat en bus de nuit : que faire à 4–5 h ? | Van Phu",
 "desc": "Les bus de nuit depuis Hô Chi Minh-Ville arrivent à Da Lat vers 4–7 h. Où ils s'arrêtent, comment rejoindre le centre et récupérer un scooter dès 4 h 30.",
 "h1": "Arrivé tôt à Da Lat en bus de nuit : que faire ?",
 "crumb": "Arriver tôt à Da Lat",
 "lead": "Le bus-couchettes de nuit depuis Hô Chi Minh-Ville arrive généralement à Da Lat entre <b>4 h et 7 h du matin</b>, avant que la ville se réveille. Notre boutique de location ouvre <b>tous les jours à 4 h 30</b> : vous pouvez donc être sur un scooter peu après être descendu du bus. Voici comment s'organise cette première matinée.",
 "short_h": "En bref",
 "short": [
  ("Hô Chi Minh-Ville → Da Lat", "Environ 300 km ; bus-couchettes environ 6–8 heures ; les bus de nuit arrivent en général vers 4 h–7 h"),
  ("Nha Trang → Da Lat", "Environ 135–140 km ; environ 3 h 30–4 h ; bus en journée"),
  ("Où s'arrêtent les bus", "Gare routière interprovinciale de Da Lat (1 Tô Hiến Thành, ouverte 24 h/24) ou bureau de la compagnie"),
  ("Gare routière → notre boutique", "Environ 3 km à vol d'oiseau, un peu plus par la route — taxi ou Grab"),
  ("Notre boutique", "1/15/5 Thông Thiên Học — ouverte tous les jours dès 4 h 30"),
  ("Température au petit matin", "Souvent autour de 10–15 °C — gardez une veste à portée de main"),
 ],
 "secs": [
  ("Bus de nuit depuis Hô Chi Minh-Ville : à quelle heure arrive-t-on ?", "<p>Les bus-couchettes partent de Hô Chi Minh-Ville en soirée et parcourent environ 300 km en 6 à 8 heures. L'heure exacte dépend de la compagnie, de la circulation et de la météo sur la route de montagne, mais la plupart des bus de nuit arrivent à Da Lat entre 4 h et 7 h environ.</p><p>Au moment de réserver, demandez où le bus s'arrête à Da Lat : à la gare routière interprovinciale de la rue Tô Hiến Thành, au bureau de la compagnie en ville ou, pour certains vans limousine, directement à l'hôtel. La gare et les bureaux des principales compagnies figurent sur notre <a href=\"{MAP:busmap}\">carte des bus Da Lat – Saïgon</a>. Vous venez de Da Nang ou Hoi An ? Voyez la <a href=\"{MAP:danangbusmap}\">carte des bus Da Lat – Da Nang</a>.</p>"),
  ("Depuis Nha Trang : un bus de jour", "<p>Nha Trang est plus proche — environ 135–140 km par un beau col de montagne, soit 3 h 30 à 4 h — et les bus roulent de jour : vous arrivez en général à Da Lat en fin de matinée ou dans l'après-midi. Les bureaux des principales compagnies sont sur la <a href=\"{MAP:nhatrangbusmap}\">carte des bus Nha Trang – Da Lat</a>, et les options de trajet dans <a href=\"{ART:getting}\">comment aller à Da Lat</a>.</p><p>Bon à savoir : une journée de location va de la prise en main jusqu'à 21 h. Si vous arrivez à 16 h et prenez le scooter tout de suite, cela compte quand même pour une journée entière. Beaucoup de clients s'installent à l'hôtel, se reposent et récupèrent le scooter le lendemain dès 4 h 30. Location de 2 jours ou plus ? Nous livrons gratuitement votre hôtel dans le centre de Da Lat.</p>"),
  ("Du bus au scooter, étape par étape", "<ol><li><b>La veille au soir :</b> écrivez-nous sur WhatsApp (+84 944 081 101 ou +84 834 622 149) ou Telegram (@vanphudalat) avec votre compagnie, votre heure d'arrivée approximative et le deux-roues souhaité.</li><li><b>En descendant du bus,</b> prenez un taxi ou un Grab jusqu'au 1/15/5 Thông Thiên Học. Avant l'aube, Grab peut être long à trouver ; des taxis attendent en général à la gare routière.</li><li><b>Formalités en quelques minutes :</b> votre passeport (pas de caution en espèces) et 150 000 VND par jour pour n'importe quel deux-roues.</li><li><b>Un court essai</b> et une vidéo de l'état du scooter que nous filmons ensemble.</li><li><b>C'est parti.</b> Une journée de location dure jusqu'à 21 h : un scooter pris à 4 h 30 est à vous toute la journée.</li></ol>"),
  ("Les premières heures : lever du soleil ou repos d'abord ?", "<ul><li><b>Bien dormi dans le bus ?</b> La plus belle lumière de Da Lat, c'est maintenant. Partez pour la <a href=\"{ART:cloudhunt}\">chasse aux nuages</a> ou le <a href=\"{ART:caudat}\">lever du soleil sur les collines de thé de Cau Dat</a> — pour ces côtes, prenez le Honda Air Blade 125cc.</li><li><b>Mal dormi ?</b> Ne partez pas fatigué sur des routes de montagne mouillées et brumeuses. Un café chaud et un petit-déjeuner d'abord, puis en route une fois bien réveillé.</li><li><b>Grosse valise ?</b> Ne la transportez pas en scooter. Déposez-la d'abord à l'hôtel — beaucoup gardent les bagages avant l'enregistrement — ou louez 2 jours ou plus et nous apportons le scooter gratuitement à votre hôtel du centre.</li><li>Casque obligatoire, pas d'alcool ni de bière au guidon, et respect strict du code de la route vietnamien.</li></ul><p>D'autres raisons de partir tôt : <a href=\"{ART:lt-early}\">location de scooter tôt le matin à Da Lat</a>.</p>"),
 ],
 "faq_h": "Questions fréquentes",
 "faq": [
  ("À quelle heure le bus de nuit de Hô Chi Minh-Ville arrive-t-il à Da Lat ?", "En général entre 4 h et 7 h du matin environ. Cela dépend de la compagnie, de la circulation et de la météo sur la route de montagne ; demandez l'heure estimée en réservant."),
  ("Où le bus me dépose-t-il à Da Lat ?", "À la gare routière interprovinciale de Da Lat, rue Tô Hiến Thành (ouverte 24 h/24), ou au bureau de la compagnie en ville. Certains vans limousine déposent à l'hôtel. Renseignez-vous en réservant."),
  ("Peut-on louer un scooter à 4 h 30 ?", "Oui. Notre boutique ouvre tous les jours à 4 h 30. Envoyez-nous la veille votre heure d'arrivée et le deux-roues souhaité : il sera prêt à votre arrivée."),
  ("Pouvez-vous livrer le scooter à la gare routière ?", "La livraison gratuite concerne les hôtels du centre de Da Lat pour les locations de 2 jours ou plus. Pour le reste, envoyez-nous votre programme et nous vous dirons ce qui est possible."),
  ("J'arrive de Nha Trang l'après-midi. Je loue aujourd'hui ou demain ?", "Une journée de location dure jusqu'à 21 h : une prise en fin d'après-midi compte donc pour une journée entière. Si vous n'avez besoin du scooter qu'à partir du lendemain matin, récupérez-le dès 4 h 30 — ou louez 2 jours ou plus avec livraison gratuite à votre hôtel du centre."),
 ],
 "more_h": "Préparez la suite",
 "more": [("{ART:getting}", "Comment aller à Da Lat"), ("{MAP:busmap}", "Carte des bus Da Lat – Saïgon"), ("{MAP:nhatrangbusmap}", "Carte des bus Nha Trang – Da Lat"), ("{ART:lt-early}", "Location dès 4 h 30"), ("{HOME}", "Location de scooter à Da Lat — modèles et prix")],
}

T["es"] = {
 "title": "Bus nocturno a Da Lat: ¿qué hacer si llegas a las 4–5? | Van Phu",
 "desc": "Los buses nocturnos desde Ciudad Ho Chi Minh llegan a Da Lat hacia las 4–7 de la mañana. Dónde paran, cómo llegar al centro y recoger un scooter desde las 4:30.",
 "h1": "Llegaste temprano a Da Lat en bus nocturno: ¿qué hacer?",
 "crumb": "Llegar temprano a Da Lat",
 "lead": "El bus cama nocturno desde Ciudad Ho Chi Minh suele llegar a Da Lat entre las <b>4:00 y las 7:00 de la mañana</b>, antes de que la ciudad despierte. Nuestra tienda de alquiler abre <b>todos los días a las 4:30</b>, así que puedes estar en un scooter poco después de bajar del bus. Así funciona esa primera mañana.",
 "short_h": "De un vistazo",
 "short": [
  ("Ciudad Ho Chi Minh → Da Lat", "Unos 300 km; bus cama unas 6–8 horas; los nocturnos suelen llegar hacia las 4:00–7:00"),
  ("Nha Trang → Da Lat", "Unos 135–140 km; unas 3,5–4 horas; buses de día"),
  ("Dónde paran los buses", "Estación de buses interprovincial de Da Lat (1 Tô Hiến Thành, abierta 24 h) o la oficina propia de la compañía"),
  ("Estación → nuestra tienda", "Unos 3 km en línea recta, algo más por carretera — taxi o Grab"),
  ("Nuestra tienda", "1/15/5 Thông Thiên Học — abre todos los días a las 4:30"),
  ("Temperatura de madrugada", "A menudo unos 10–15 °C — ten la chaqueta a mano"),
 ],
 "secs": [
  ("Bus nocturno desde Ciudad Ho Chi Minh: a qué hora llegas", "<p>Los buses cama salen de Ciudad Ho Chi Minh por la tarde-noche y recorren unos 300 km en unas 6–8 horas. La hora exacta depende de la compañía, del tráfico y del tiempo en la carretera de montaña, pero la mayoría de los nocturnos entra en Da Lat entre las 4:00 y las 7:00 aproximadamente.</p><p>Al reservar, pregunta dónde para el bus en Da Lat: en la estación interprovincial de la calle Tô Hiến Thành, en la oficina de la compañía en la ciudad o, con algunas furgonetas limusina, en tu hotel. La estación y las oficinas de las principales compañías están en nuestro <a href=\"{MAP:busmap}\">mapa de buses Da Lat – Saigón</a>. ¿Vienes de Da Nang o Hoi An? Mira el <a href=\"{MAP:danangbusmap}\">mapa de buses Da Lat – Da Nang</a>.</p>"),
  ("Desde Nha Trang: un bus de día", "<p>Nha Trang está más cerca — unos 135–140 km por un bonito paso de montaña, unas 3,5–4 horas — y los buses van de día, así que normalmente llegas a Da Lat a media mañana o por la tarde. Las oficinas de las principales compañías están en el <a href=\"{MAP:nhatrangbusmap}\">mapa de buses Nha Trang – Da Lat</a>, y las opciones de viaje en <a href=\"{ART:getting}\">cómo llegar a Da Lat</a>.</p><p>Ten en cuenta: un día de alquiler va desde la recogida hasta las 21:00. Si llegas a las 16:00 y recoges el scooter enseguida, cuenta igualmente como un día completo. Muchos clientes hacen el check-in, descansan y lo recogen a la mañana siguiente desde las 4:30. ¿Alquilas 2 días o más? Te lo llevamos gratis al hotel en el centro de Da Lat.</p>"),
  ("Del bus al scooter, paso a paso", "<ol><li><b>La noche anterior:</b> escríbenos por WhatsApp (+84 944 081 101 o +84 834 622 149) o Telegram (@vanphudalat) con tu compañía de bus, la hora aproximada de llegada y la moto que quieres.</li><li><b>Al bajar del bus,</b> toma un taxi o un Grab hasta 1/15/5 Thông Thiên Học. Antes del amanecer puede costar encontrar Grab; los taxis suelen esperar en la estación.</li><li><b>Trámites en pocos minutos:</b> tu pasaporte (sin depósito en efectivo) y 150.000 VND al día por cualquier moto.</li><li><b>Una breve prueba</b> y un vídeo del estado de la moto que grabamos juntos.</li><li><b>¡En marcha!</b> Un día de alquiler dura hasta las 21:00, así que un scooter recogido a las 4:30 es tuyo todo el día.</li></ol>"),
  ("Las primeras horas: ¿amanecer o descanso primero?", "<ul><li><b>¿Dormiste bien en el bus?</b> La mejor luz de Da Lat es ahora. Ve a la <a href=\"{ART:cloudhunt}\">caza de nubes</a> o al <a href=\"{ART:caudat}\">amanecer en las colinas de té de Cau Dat</a> — para esas subidas elige la Honda Air Blade 125cc.</li><li><b>¿Dormiste mal?</b> No salgas cansado por carreteras de montaña mojadas y con niebla. Primero un café caliente y desayuno, y luego a rodar cuando estés despierto.</li><li><b>¿Maleta grande?</b> No la lleves en el scooter. Déjala antes en el hotel — muchos guardan el equipaje antes del check-in — o alquila 2 días o más y te llevamos la moto gratis a tu hotel del centro.</li><li>Casco siempre, nada de alcohol ni cerveza al conducir y respeta estrictamente las normas de tráfico vietnamitas.</li></ul><p>Más razones para salir temprano: <a href=\"{ART:lt-early}\">alquiler de moto temprano en Da Lat</a>.</p>"),
 ],
 "faq_h": "Preguntas frecuentes",
 "faq": [
  ("¿A qué hora llega a Da Lat el bus nocturno desde Ciudad Ho Chi Minh?", "Normalmente entre las 4:00 y las 7:00 de la mañana. Depende de la compañía, del tráfico y del tiempo en la carretera de montaña; pregunta la hora estimada al reservar."),
  ("¿Dónde me deja el bus en Da Lat?", "En la estación de buses interprovincial de Da Lat, en la calle Tô Hiến Thành (abierta 24 horas), o en la oficina de la compañía en la ciudad. Algunas furgonetas limusina dejan en el hotel. Pregunta al reservar."),
  ("¿Puedo alquilar un scooter a las 4:30?", "Sí. Nuestra tienda abre todos los días a las 4:30. Escríbenos la noche anterior con tu hora de llegada y la moto, y estará lista cuando llegues."),
  ("¿Podéis llevar la moto a la estación de buses?", "La entrega gratuita es para hoteles del centro de Da Lat en alquileres de 2 días o más. Para lo demás, mándanos tu plan y te decimos qué es posible."),
  ("Llego de Nha Trang por la tarde. ¿Alquilo hoy o mañana?", "Un día de alquiler dura hasta las 21:00, así que recoger a última hora de la tarde cuenta como un día completo. Si solo necesitas la moto desde la mañana siguiente, recógela desde las 4:30 — o alquila 2 días o más con entrega gratis a tu hotel del centro."),
 ],
 "more_h": "Sigue planeando",
 "more": [("{ART:getting}", "Cómo llegar a Da Lat"), ("{MAP:busmap}", "Mapa de buses Da Lat – Saigón"), ("{MAP:nhatrangbusmap}", "Mapa de buses Nha Trang – Da Lat"), ("{ART:lt-early}", "Alquiler de motos desde las 4:30"), ("{HOME}", "Alquiler de motos en Da Lat — modelos y precios")],
}

T["he"] = {
 "title": "מגיעים לדאלאט מוקדם באוטובוס לילה: מה עושים ב־4–5 בבוקר? | Van Phu",
 "desc": "אוטובוסי הלילה מהו צ׳י מין סיטי מגיעים לדאלאט בדרך כלל בסביבות 4–7 בבוקר. איפה הם עוצרים, איך מגיעים למרכז ואיך אוספים קטנוע כבר מ־4:30.",
 "h1": "הגעתם לדאלאט מוקדם באוטובוס לילה: מה עושים?",
 "crumb": "הגעה מוקדמת לדאלאט",
 "lead": "אוטובוס השינה של הלילה מהו צ׳י מין סיטי מגיע לדאלאט בדרך כלל בין <b>4:00 ל־7:00 בבוקר</b>, לפני שהעיר מתעוררת. החנות שלנו נפתחת <b>כל יום ב־4:30</b>, כך שזמן קצר אחרי שירדתם מהאוטובוס אתם כבר על קטנוע. ככה נראה הבוקר הראשון.",
 "short_h": "בקצרה",
 "short": [
  ("הו צ׳י מין סיטי ← דאלאט", "כ־300 ק״מ; אוטובוס שינה כ־6–8 שעות; אוטובוסי לילה מגיעים בדרך כלל בסביבות 4:00–7:00"),
  ("נה טראנג ← דאלאט", "כ־135–140 ק״מ; כ־3.5–4 שעות; אוטובוסים בשעות היום"),
  ("איפה האוטובוסים עוצרים", "בתחנה המרכזית הבין־עירונית של דאלאט (<bdi dir=\"ltr\">1 Tô Hiến Thành</bdi>, פתוחה 24 שעות) או במשרד של חברת האוטובוסים"),
  ("מהתחנה לחנות שלנו", "כ־3 ק״מ בקו אווירי, קצת יותר בכביש — מונית או Grab"),
  ("החנות שלנו", "<bdi dir=\"ltr\">1/15/5 Thông Thiên Học</bdi> — פתוחה כל יום מ־4:30"),
  ("טמפרטורה בשעות הבוקר המוקדמות", "לרוב כ־10–15 מעלות — שמרו מעיל בהישג יד"),
 ],
 "secs": [
  ("אוטובוס לילה מהו צ׳י מין סיטי: מתי מגיעים", "<p>אוטובוסי השינה יוצאים מהו צ׳י מין סיטי בערב ועוברים כ־300 ק״מ בכ־6–8 שעות. שעת ההגעה המדויקת תלויה בחברה, בתנועה ובמזג האוויר בכביש ההררי, אבל רוב אוטובוסי הלילה נכנסים לדאלאט בערך בין 4:00 ל־7:00.</p><p>כשאתם מזמינים, שאלו איפה האוטובוס עוצר בדאלאט: בתחנה הבין־עירונית ברחוב <bdi dir=\"ltr\">Tô Hiến Thành</bdi>, במשרד של החברה בעיר, או — בחלק מוואני הלימוזינה — ממש ליד המלון. התחנה ומשרדי החברות העיקריות מופיעים ב<a href=\"{MAP:busmap}\">מפת האוטובוסים דאלאט – סייגון</a> שלנו. מגיעים מדה נאנג או מהוי אן? ראו את <a href=\"{MAP:danangbusmap}\">מפת האוטובוסים דאלאט – דה נאנג</a>.</p>"),
  ("מנה טראנג: אוטובוס של יום", "<p>נה טראנג קרובה יותר — כ־135–140 ק״מ דרך מעבר הרים יפה, בערך 3.5–4 שעות — והאוטובוסים נוסעים ביום, כך שבדרך כלל מגיעים לדאלאט בסוף הבוקר או אחר הצהריים. משרדי החברות העיקריות מופיעים ב<a href=\"{MAP:nhatrangbusmap}\">מפת האוטובוסים נה טראנג – דאלאט</a>, ודרכי ההגעה במאמר <a href=\"{ART:getting}\">איך מגיעים לדאלאט</a>.</p><p>כדאי לדעת: יום השכרה נמשך מרגע האיסוף ועד 21:00. אם הגעתם ב־16:00 ולקחתם קטנוע מיד, זה עדיין נחשב יום שלם. הרבה אורחים עושים צ׳ק־אין, נחים ואוספים את הקטנוע למחרת בבוקר מ־4:30. שוכרים ליומיים או יותר? נביא את הקטנוע בחינם למלון שלכם במרכז דאלאט.</p>"),
  ("מהאוטובוס לקטנוע, צעד אחר צעד", "<ol><li><b>בערב שלפני:</b> כתבו לנו בוואטסאפ (<bdi dir=\"ltr\">+84 944 081 101</bdi> או <bdi dir=\"ltr\">+84 834 622 149</bdi>) או בטלגרם (<bdi dir=\"ltr\">@vanphudalat</bdi>) את חברת האוטובוסים, שעת ההגעה המשוערת ואיזה קטנוע אתם רוצים.</li><li><b>אחרי שירדתם מהאוטובוס,</b> קחו מונית או Grab אל <bdi dir=\"ltr\">1/15/5 Thông Thiên Học</bdi>. לפני הזריחה קשה לפעמים למצוא Grab; מוניות בדרך כלל מחכות בתחנה.</li><li><b>הסידורים לוקחים כמה דקות:</b> הדרכון (בלי פיקדון במזומן) ו־150,000 VND ליום לכל כלי.</li><li><b>נסיעת מבחן קצרה</b> וסרטון של מצב הכלי שמצלמים יחד.</li><li><b>יוצאים לדרך.</b> יום השכרה נמשך עד 21:00, כך שקטנוע שנאסף ב־4:30 שלכם לכל היום.</li></ol>"),
  ("השעות הראשונות: זריחה או קודם מנוחה?", "<ul><li><b>ישנתם טוב באוטובוס?</b> האור הכי יפה של דאלאט הוא עכשיו. צאו ל<a href=\"{ART:cloudhunt}\">ציד עננים</a> או ל<a href=\"{ART:caudat}\">זריחה בגבעות התה של קאו דאט</a> — לעליות האלה קחו את ה־Honda Air Blade 125cc.</li><li><b>ישנתם רע?</b> אל תצאו עייפים לכבישי הרים רטובים וערפיליים. קודם קפה חם וארוחת בוקר, ורק כשאתם ערניים — לדרך.</li><li><b>מזוודה גדולה?</b> אל תסחבו אותה על הקטנוע. השאירו אותה קודם במלון — הרבה מלונות שומרים מזוודות לפני הצ׳ק־אין — או שכרו ליומיים ומעלה ונביא את הקטנוע בחינם למלון שלכם במרכז.</li><li>חובשים קסדה, לא שותים אלכוהול או בירה כשרוכבים, ומקפידים על חוקי התנועה של וייטנאם.</li></ul><p>עוד סיבות לצאת מוקדם: <a href=\"{ART:lt-early}\">השכרת קטנוע מוקדמת בדאלאט</a>.</p>"),
 ],
 "faq_h": "שאלות נפוצות",
 "faq": [
  ("באיזו שעה אוטובוס הלילה מהו צ׳י מין סיטי מגיע לדאלאט?", "בדרך כלל בערך בין 4:00 ל־7:00 בבוקר. זה תלוי בחברה, בתנועה ובמזג האוויר בכביש ההררי, אז שאלו על שעת ההגעה המשוערת כשאתם מזמינים."),
  ("איפה האוטובוס מוריד אותי בדאלאט?", "בתחנה הבין־עירונית של דאלאט ברחוב Tô Hiến Thành (פתוחה 24 שעות) או במשרד של החברה בעיר. חלק מוואני הלימוזינה מורידים ליד המלון. שאלו כשאתם מזמינים."),
  ("אפשר לשכור קטנוע ב־4:30 בבוקר?", "כן. החנות שלנו נפתחת כל יום ב־4:30. כתבו לנו בערב שלפני את שעת ההגעה ואיזה קטנוע אתם רוצים, והוא יחכה לכם מוכן."),
  ("אתם יכולים להביא את הקטנוע לתחנת האוטובוסים?", "משלוח חינם הוא למלונות במרכז דאלאט בהשכרה של יומיים ומעלה. לכל דבר אחר שלחו לנו את התוכנית ונגיד לכם מה אפשר."),
  ("אני מגיע מנה טראנג אחר הצהריים. לשכור היום או מחר?", "יום השכרה נמשך עד 21:00, כך שאיסוף בשעות אחר הצהריים המאוחרות נחשב יום שלם. אם צריך את הקטנוע רק מהבוקר שלמחרת, אספו אותו מ־4:30 — או שכרו ליומיים ומעלה עם משלוח חינם למלון במרכז."),
 ],
 "more_h": "ממשיכים לתכנן",
 "more": [("{ART:getting}", "איך מגיעים לדאלאט"), ("{MAP:busmap}", "מפת האוטובוסים דאלאט – סייגון"), ("{MAP:nhatrangbusmap}", "מפת האוטובוסים נה טראנג – דאלאט"), ("{ART:lt-early}", "השכרה מוקדמת מ־4:30"), ("{HOME}", "השכרת קטנועים בדאלאט — כלים ומחירים")],
}

T["it"] = {
 "title": "Bus notturno per Da Lat: cosa fare se arrivi alle 4–5 | Van Phu",
 "desc": "I bus notturni da Ho Chi Minh City arrivano a Da Lat verso le 4–7 del mattino. Dove fermano, come raggiungere il centro e ritirare uno scooter dalle 4:30.",
 "h1": "Arrivato presto a Da Lat col bus notturno: cosa fare?",
 "crumb": "Arrivare presto a Da Lat",
 "lead": "Il bus notturno con cuccette da Ho Chi Minh City arriva di solito a Da Lat tra le <b>4:00 e le 7:00 del mattino</b>, prima che la città si svegli. Il nostro negozio apre <b>ogni giorno alle 4:30</b>, quindi poco dopo essere sceso dal bus puoi già essere in sella a uno scooter. Ecco come funziona quella prima mattina.",
 "short_h": "In breve",
 "short": [
  ("Ho Chi Minh City → Da Lat", "Circa 300 km; bus con cuccette circa 6–8 ore; i notturni arrivano di solito verso le 4:00–7:00"),
  ("Nha Trang → Da Lat", "Circa 135–140 km; circa 3,5–4 ore; bus di giorno"),
  ("Dove fermano i bus", "Stazione degli autobus interprovinciale di Da Lat (1 Tô Hiến Thành, aperta 24 ore) o l'ufficio della compagnia"),
  ("Stazione → il nostro negozio", "Circa 3 km in linea d'aria, un po' di più su strada — taxi o Grab"),
  ("Il nostro negozio", "1/15/5 Thông Thiên Học — aperto ogni giorno dalle 4:30"),
  ("Temperatura all'alba", "Spesso circa 10–15 °C — tieni la giacca a portata di mano"),
 ],
 "secs": [
  ("Bus notturno da Ho Chi Minh City: quando arrivi", "<p>I bus con cuccette partono da Ho Chi Minh City in serata e percorrono circa 300 km in 6–8 ore. L'orario preciso dipende dalla compagnia, dal traffico e dal meteo sulla strada di montagna, ma la maggior parte dei notturni arriva a Da Lat tra le 4:00 e le 7:00 circa.</p><p>Quando prenoti, chiedi dove ferma il bus a Da Lat: alla stazione interprovinciale in via Tô Hiến Thành, all'ufficio della compagnia in città o, con alcuni van limousine, direttamente all'hotel. La stazione e gli uffici delle compagnie principali sono sulla nostra <a href=\"{MAP:busmap}\">mappa dei bus Da Lat – Saigon</a>. Arrivi da Da Nang o Hoi An? Guarda la <a href=\"{MAP:danangbusmap}\">mappa dei bus Da Lat – Da Nang</a>.</p>"),
  ("Da Nha Trang: un bus di giorno", "<p>Nha Trang è più vicina — circa 135–140 km lungo un bel passo di montagna, più o meno 3,5–4 ore — e i bus viaggiano di giorno, quindi di solito arrivi a Da Lat in tarda mattinata o nel pomeriggio. Gli uffici delle compagnie principali sono sulla <a href=\"{MAP:nhatrangbusmap}\">mappa dei bus Nha Trang – Da Lat</a>, e le opzioni di viaggio in <a href=\"{ART:getting}\">come arrivare a Da Lat</a>.</p><p>Da sapere: un giorno di noleggio va dal ritiro fino alle 21:00. Se arrivi alle 16:00 e ritiri subito lo scooter, conta comunque come un giorno intero. Molti ospiti fanno il check-in, riposano e ritirano lo scooter la mattina dopo dalle 4:30. Noleggi per 2 giorni o più? Te lo portiamo gratis all'hotel nel centro di Da Lat.</p>"),
  ("Dal bus allo scooter, passo dopo passo", "<ol><li><b>La sera prima:</b> scrivici su WhatsApp (+84 944 081 101 o +84 834 622 149) o Telegram (@vanphudalat) con la compagnia del bus, l'orario di arrivo approssimativo e il mezzo che vuoi.</li><li><b>Sceso dal bus,</b> prendi un taxi o un Grab fino a 1/15/5 Thông Thiên Học. Prima dell'alba Grab può essere difficile da trovare; i taxi di solito aspettano alla stazione.</li><li><b>Pratiche in pochi minuti:</b> il passaporto (nessun deposito in contanti) e 150.000 VND al giorno per qualsiasi mezzo.</li><li><b>Un breve giro di prova</b> e un video dello stato del mezzo che giriamo insieme.</li><li><b>Si parte.</b> Un giorno di noleggio dura fino alle 21:00, quindi uno scooter ritirato alle 4:30 è tuo per tutta la giornata.</li></ol>"),
  ("Le prime ore: alba o prima riposo?", "<ul><li><b>Hai dormito bene in bus?</b> La luce più bella di Da Lat è adesso. Vai a <a href=\"{ART:cloudhunt}\">caccia di nuvole</a> o all'<a href=\"{ART:caudat}\">alba sulle colline del tè di Cau Dat</a> — per queste salite scegli la Honda Air Blade 125cc.</li><li><b>Hai dormito male?</b> Non partire stanco su strade di montagna bagnate e nebbiose. Prima un caffè caldo e la colazione, poi in sella quando sei ben sveglio.</li><li><b>Valigia grande?</b> Non portarla sullo scooter. Lasciala prima in hotel — molti tengono i bagagli prima del check-in — oppure noleggia per 2+ giorni e ti portiamo lo scooter gratis all'hotel in centro.</li><li>Casco sempre, niente alcol né birra alla guida e rispetto rigoroso del codice della strada vietnamita.</li></ul><p>Altri motivi per partire presto: <a href=\"{ART:lt-early}\">noleggio scooter all'alba a Da Lat</a>.</p>"),
 ],
 "faq_h": "Domande frequenti",
 "faq": [
  ("A che ora arriva a Da Lat il bus notturno da Ho Chi Minh City?", "Di solito tra le 4:00 e le 7:00 del mattino circa. Dipende dalla compagnia, dal traffico e dal meteo sulla strada di montagna: chiedi l'orario stimato quando prenoti."),
  ("Dove mi lascia il bus a Da Lat?", "Alla stazione degli autobus interprovinciale di Da Lat in via Tô Hiến Thành (aperta 24 ore) o all'ufficio della compagnia in città. Alcuni van limousine lasciano in hotel. Chiedi quando prenoti."),
  ("Posso noleggiare uno scooter alle 4:30?", "Sì. Il nostro negozio apre ogni giorno alle 4:30. Scrivici la sera prima con l'orario di arrivo e il mezzo, e sarà pronto quando arrivi."),
  ("Potete portare lo scooter alla stazione dei bus?", "La consegna gratuita è per gli hotel nel centro di Da Lat con noleggi di 2 giorni o più. Per il resto, mandaci il tuo programma e ti diciamo cosa è possibile."),
  ("Arrivo da Nha Trang nel pomeriggio. Noleggio oggi o domani?", "Un giorno di noleggio dura fino alle 21:00, quindi un ritiro nel tardo pomeriggio conta come un giorno intero. Se ti serve lo scooter solo dalla mattina dopo, ritiralo dalle 4:30 — oppure noleggia per 2+ giorni con consegna gratuita all'hotel in centro."),
 ],
 "more_h": "Continua a pianificare",
 "more": [("{ART:getting}", "Come arrivare a Da Lat"), ("{MAP:busmap}", "Mappa dei bus Da Lat – Saigon"), ("{MAP:nhatrangbusmap}", "Mappa dei bus Nha Trang – Da Lat"), ("{ART:lt-early}", "Noleggio dalle 4:30"), ("{HOME}", "Noleggio scooter a Da Lat — mezzi e prezzi")],
}

T["nl"] = {
 "title": "Vroeg in Da Lat met de nachtbus: wat doe je om 4–5 uur? | Van Phu",
 "desc": "Nachtbussen uit Ho Chi Minhstad komen meestal rond 4–7 uur in Da Lat aan. Waar ze stoppen, hoe je in het centrum komt en een scooter ophaalt vanaf 4.30 uur.",
 "h1": "Vroeg in Da Lat aangekomen met de nachtbus: wat nu?",
 "crumb": "Vroeg aankomen in Da Lat",
 "lead": "De nachtelijke slaapbus uit Ho Chi Minhstad komt meestal tussen ongeveer <b>4.00 en 7.00 uur 's ochtends</b> in Da Lat aan, voordat de stad wakker is. Onze verhuurwinkel gaat <b>elke dag om 4.30 uur</b> open, dus kort nadat je uit de bus stapt zit je al op een scooter. Zo verloopt die eerste ochtend.",
 "short_h": "In het kort",
 "short": [
  ("Ho Chi Minhstad → Da Lat", "Ongeveer 300 km; slaapbus ongeveer 6–8 uur; nachtbussen komen meestal rond 4.00–7.00 uur aan"),
  ("Nha Trang → Da Lat", "Ongeveer 135–140 km; ongeveer 3,5–4 uur; bussen rijden overdag"),
  ("Waar de bussen stoppen", "Het interprovinciale busstation van Da Lat (1 Tô Hiến Thành, 24 uur open) of het eigen kantoor van de busmaatschappij"),
  ("Busstation → onze winkel", "Ongeveer 3 km hemelsbreed, over de weg iets meer — taxi of Grab"),
  ("Onze winkel", "1/15/5 Thông Thiên Học — elke dag open vanaf 4.30 uur"),
  ("Temperatuur in de vroege ochtend", "Vaak ongeveer 10–15 °C — houd je jas binnen handbereik"),
 ],
 "secs": [
  ("Nachtbus uit Ho Chi Minhstad: wanneer je aankomt", "<p>Slaapbussen vertrekken 's avonds uit Ho Chi Minhstad en doen over ongeveer 300 km zo'n 6–8 uur. De precieze aankomsttijd hangt af van de maatschappij, het verkeer en het weer op de bergweg, maar de meeste nachtbussen rijden Da Lat binnen tussen ongeveer 4.00 en 7.00 uur.</p><p>Vraag bij het boeken waar de bus in Da Lat stopt: op het interprovinciale busstation aan de Tô Hiến Thành, bij het kantoor van de maatschappij in de stad of — bij sommige limousinebusjes — gewoon bij je hotel. Het station en de kantoren van de grote maatschappijen staan op onze <a href=\"{MAP:busmap}\">buskaart Da Lat – Saigon</a>. Kom je uit Da Nang of Hoi An? Bekijk dan de <a href=\"{MAP:danangbusmap}\">buskaart Da Lat – Da Nang</a>.</p>"),
  ("Vanuit Nha Trang: een dagbus", "<p>Nha Trang ligt dichterbij — ongeveer 135–140 km over een mooie bergpas, zo'n 3,5–4 uur — en de bussen rijden overdag, dus je komt meestal laat in de ochtend of 's middags in Da Lat aan. De kantoren van de grote maatschappijen staan op de <a href=\"{MAP:nhatrangbusmap}\">buskaart Nha Trang – Da Lat</a>, de reisopties in <a href=\"{ART:getting}\">hoe je in Da Lat komt</a>.</p><p>Goed om te weten: een huurdag loopt van het ophalen tot 21.00 uur. Kom je om 16.00 uur aan en haal je de scooter meteen op, dan telt dat toch als een hele dag. Veel gasten checken in, rusten uit en halen de scooter de volgende ochtend vanaf 4.30 uur op. Huur je 2 dagen of langer? Dan brengen we de scooter gratis naar je hotel in het centrum van Da Lat.</p>"),
  ("Van de bus op de scooter, stap voor stap", "<ol><li><b>De avond ervoor:</b> stuur ons via WhatsApp (+84 944 081 101 of +84 834 622 149) of Telegram (@vanphudalat) je busmaatschappij, je geschatte aankomsttijd en de scooter die je wilt.</li><li><b>Uit de bus</b> neem je een taxi of Grab naar 1/15/5 Thông Thiên Học. Vóór zonsopgang is Grab soms lastig te vinden; taxi's wachten meestal bij het busstation.</li><li><b>Papierwerk in een paar minuten:</b> je paspoort (geen borg in contanten) en 150.000 VND per dag voor elke scooter.</li><li><b>Een korte proefrit</b> en een video van de staat van de scooter die we samen maken.</li><li><b>Op pad.</b> Een huurdag loopt tot 21.00 uur, dus een scooter die je om 4.30 uur ophaalt, is de hele dag van jou.</li></ol>"),
  ("De eerste uren: zonsopgang of eerst rusten?", "<ul><li><b>Goed geslapen in de bus?</b> Het mooiste licht van Da Lat is nu. Ga <a href=\"{ART:cloudhunt}\">wolken jagen</a> of naar de <a href=\"{ART:caudat}\">zonsopgang boven de theeheuvels van Cau Dat</a> — neem voor die hellingen de Honda Air Blade 125cc.</li><li><b>Slecht geslapen?</b> Ga niet moe de natte, mistige bergwegen op. Eerst een hete koffie en ontbijt, en pas rijden als je wakker bent.</li><li><b>Grote koffer?</b> Neem die niet mee op de scooter. Laat hem eerst bij je hotel — veel hotels bewaren bagage vóór het inchecken — of huur 2+ dagen en we brengen de scooter gratis naar je hotel in het centrum.</li><li>Helm op, geen alcohol of bier tijdens het rijden en houd je strikt aan de Vietnamese verkeersregels.</li></ul><p>Nog meer redenen om vroeg te beginnen: <a href=\"{ART:lt-early}\">vroeg in de ochtend een scooter huren in Da Lat</a>.</p>"),
 ],
 "faq_h": "Veelgestelde vragen",
 "faq": [
  ("Hoe laat komt de nachtbus uit Ho Chi Minhstad in Da Lat aan?", "Meestal tussen ongeveer 4.00 en 7.00 uur 's ochtends. Dat hangt af van de maatschappij, het verkeer en het weer op de bergweg; vraag bij het boeken naar de geschatte aankomsttijd."),
  ("Waar zet de bus me af in Da Lat?", "Op het interprovinciale busstation van Da Lat aan de Tô Hiến Thành (24 uur open) of bij het kantoor van de maatschappij in de stad. Sommige limousinebusjes zetten je af bij je hotel. Vraag het bij het boeken."),
  ("Kan ik om 4.30 uur een scooter huren?", "Ja. Onze winkel gaat elke dag om 4.30 uur open. Stuur ons de avond ervoor je aankomsttijd en de scooter, dan staat hij klaar als je komt."),
  ("Kunnen jullie de scooter naar het busstation brengen?", "Gratis bezorging geldt voor hotels in het centrum van Da Lat bij huur van 2 dagen of langer. Voor de rest: stuur ons je plan en we laten weten wat mogelijk is."),
  ("Ik kom 's middags aan uit Nha Trang. Vandaag of morgen huren?", "Een huurdag loopt tot 21.00 uur, dus ophalen aan het eind van de middag telt als een hele dag. Heb je de scooter pas vanaf de volgende ochtend nodig, haal hem dan vanaf 4.30 uur op — of huur 2+ dagen met gratis bezorging naar je hotel in het centrum."),
 ],
 "more_h": "Plan verder",
 "more": [("{ART:getting}", "Hoe je in Da Lat komt"), ("{MAP:busmap}", "Buskaart Da Lat – Saigon"), ("{MAP:nhatrangbusmap}", "Buskaart Nha Trang – Da Lat"), ("{ART:lt-early}", "Scooter huren vanaf 4.30 uur"), ("{HOME}", "Scooter huren in Da Lat — modellen en prijzen")],
}

T["km"] = {
 "title": "មកដល់ដាឡាត់ព្រឹកព្រលឹមដោយឡានយប់៖ ម៉ោង 4–5 ធ្វើអ្វី? | Van Phu",
 "desc": "ឡានក្រុងយប់ពីទីក្រុងហូជីមិញ ជាធម្មតាមកដល់ដាឡាត់ប្រហែលម៉ោង 4–7 ព្រឹក។ ចុះនៅឯណា ទៅកណ្តាលក្រុងដោយរបៀបណា និងយកម៉ូតូបានចាប់ពីម៉ោង 4:30។",
 "h1": "មកដល់ដាឡាត់ព្រឹកព្រលឹមដោយឡានយប់៖ គួរធ្វើអ្វី?",
 "crumb": "មកដល់ដាឡាត់ព្រឹកព្រលឹម",
 "lead": "ឡានក្រុងគេងពេលយប់ពីទីក្រុងហូជីមិញ ជាធម្មតាមកដល់ដាឡាត់ប្រហែល <b>ម៉ោង 4:00 ដល់ 7:00 ព្រឹក</b> មុនពេលទីក្រុងភ្ញាក់។ ហាងជួលម៉ូតូរបស់យើងបើក <b>រាល់ថ្ងៃចាប់ពីម៉ោង 4:30 ព្រឹក</b> ដូច្នេះចុះពីឡានមិនយូរប៉ុន្មាន អ្នកអាចជិះម៉ូតូចេញដំណើរបានហើយ។ នេះជារបៀបរៀបចំព្រឹកដំបូង។",
 "short_h": "សង្ខេប",
 "short": [
  ("ហូជីមិញ → ដាឡាត់", "ប្រហែល 300 គ.ម; ឡានគេងប្រហែល 6–8 ម៉ោង; ឡានយប់ជាធម្មតាមកដល់ប្រហែល 4:00–7:00"),
  ("ញ៉ាត្រាង → ដាឡាត់", "ប្រហែល 135–140 គ.ម; ប្រហែល 3.5–4 ម៉ោង; ឡានរត់ពេលថ្ងៃ"),
  ("ឡានឈប់នៅឯណា", "ចំណតឡានអន្តរខេត្តដាឡាត់ (1 Tô Hiến Thành បើក 24 ម៉ោង) ឬការិយាល័យផ្ទាល់របស់ក្រុមហ៊ុនឡាន"),
  ("ចំណតឡាន → ហាងរបស់យើង", "ប្រហែល 3 គ.ម តាមបន្ទាត់ត្រង់ តាមផ្លូវឆ្ងាយជាងបន្តិច — តាក់ស៊ី ឬ Grab"),
  ("ហាងរបស់យើង", "1/15/5 Thông Thiên Học — បើករាល់ថ្ងៃចាប់ពីម៉ោង 4:30 ព្រឹក"),
  ("សីតុណ្ហភាពព្រឹកព្រលឹម", "ច្រើនតែប្រហែល 10–15 °C — ទុកអាវរងារនៅជិតដៃ"),
 ],
 "secs": [
  ("ឡានយប់ពីហូជីមិញ៖ មកដល់ម៉ោងប៉ុន្មាន", "<p>ឡានគេងចេញពីទីក្រុងហូជីមិញពេលល្ងាច ហើយធ្វើដំណើរប្រហែល 300 គ.ម ក្នុងរយៈពេលប្រហែល 6–8 ម៉ោង។ ម៉ោងមកដល់ពិតប្រាកដអាស្រ័យលើក្រុមហ៊ុន ចរាចរណ៍ និងអាកាសធាតុលើផ្លូវភ្នំ ប៉ុន្តែឡានយប់ភាគច្រើនចូលដល់ដាឡាត់ចន្លោះប្រហែលម៉ោង 4:00 ដល់ 7:00 ព្រឹក។</p><p>ពេលកក់សំបុត្រ សូមសួរថាឡានឈប់នៅឯណាក្នុងដាឡាត់៖ ចំណតឡានអន្តរខេត្តនៅផ្លូវ Tô Hiến Thành ការិយាល័យក្រុមហ៊ុនក្នុងក្រុង ឬ — សម្រាប់ឡានលីមូស៊ីនខ្លះ — ដល់សណ្ឋាគារ។ ចំណតឡាន និងការិយាល័យក្រុមហ៊ុនធំៗមាននៅលើ<a href=\"{MAP:busmap}\">ផែនទីឡានក្រុងដាឡាត់ – សៃហ្គន</a>របស់យើង។ មកពីដាណាំង ឬហូយអាន? សូមមើល<a href=\"{MAP:danangbusmap}\">ផែនទីឡានក្រុងដាឡាត់ – ដាណាំង</a>។</p>"),
  ("ពីញ៉ាត្រាង៖ ឡានពេលថ្ងៃ", "<p>ញ៉ាត្រាងនៅជិតជាង — ប្រហែល 135–140 គ.ម កាត់ច្រកភ្នំដ៏ស្រស់ស្អាត ប្រហែល 3.5–4 ម៉ោង — ហើយឡានរត់ពេលថ្ងៃ ដូច្នេះជាធម្មតាអ្នកមកដល់ដាឡាត់ពេលថ្ងៃត្រង់ ឬរសៀល។ ការិយាល័យក្រុមហ៊ុនធំៗមាននៅលើ<a href=\"{MAP:nhatrangbusmap}\">ផែនទីឡានក្រុងញ៉ាត្រាង – ដាឡាត់</a> ហើយជម្រើសធ្វើដំណើរមាននៅក្នុងអត្ថបទ<a href=\"{ART:getting}\">របៀបទៅដាឡាត់</a>។</p><p>គួរដឹង៖ ការជួលមួយថ្ងៃគិតពីពេលយកម៉ូតូរហូតដល់ម៉ោង 21:00។ បើមកដល់ម៉ោង 16:00 ហើយយកម៉ូតូភ្លាម ក៏នៅតែគិតមួយថ្ងៃពេញ។ ភ្ញៀវជាច្រើនចូលសណ្ឋាគារ សម្រាក ហើយមកយកម៉ូតូនៅព្រឹកបន្ទាប់ចាប់ពីម៉ោង 4:30។ ជួល 2 ថ្ងៃឡើងទៅ? យើងដឹកម៉ូតូទៅសណ្ឋាគារនៅកណ្តាលក្រុងដាឡាត់ដោយឥតគិតថ្លៃ។</p>"),
  ("ពីចុះឡានរហូតដល់ជិះម៉ូតូ", "<ol><li><b>ល្ងាចមុន៖</b> ផ្ញើសារមកយើងតាម WhatsApp (+84 944 081 101 ឬ +84 834 622 149) ឬ Telegram (@vanphudalat) ប្រាប់ឈ្មោះក្រុមហ៊ុនឡាន ម៉ោងមកដល់ប្រហាក់ប្រហែល និងប្រភេទម៉ូតូដែលអ្នកចង់បាន។</li><li><b>ចុះពីឡានរួច</b> ជិះតាក់ស៊ី ឬ Grab មកកាន់ 1/15/5 Thông Thiên Học។ មុនភ្លឺ ហៅ Grab អាចពិបាក ឯតាក់ស៊ីជាធម្មតារង់ចាំនៅចំណតឡាន។</li><li><b>នីតិវិធីប៉ុន្មាននាទី៖</b> លិខិតឆ្លងដែន (គ្មានប្រាក់កក់) និង 150,000 VND ក្នុងមួយថ្ងៃសម្រាប់ម៉ូតូគ្រប់ប្រភេទ។</li><li><b>សាកល្បងជិះខ្លី</b> និងថតវីដេអូស្ថានភាពម៉ូតូជាមួយគ្នា។</li><li><b>ចេញដំណើរ។</b> ការជួលមួយថ្ងៃរហូតដល់ម៉ោង 21:00 ដូច្នេះម៉ូតូដែលយកម៉ោង 4:30 អាចប្រើបានពេញមួយថ្ងៃ។</li></ol>"),
  ("ម៉ោងដំបូង៖ ទៅមើលថ្ងៃរះ ឬសម្រាកសិន?", "<ul><li><b>គេងលក់ស្រួលលើឡាន?</b> ពន្លឺដ៏ស្អាតបំផុតរបស់ដាឡាត់គឺពេលនេះ។ ទៅ<a href=\"{ART:cloudhunt}\">តាមរកសមុទ្រពពក</a> ឬ<a href=\"{ART:caudat}\">មើលថ្ងៃរះនៅចម្ការតែ Cau Dat</a> — សម្រាប់ផ្លូវឡើងចោតទាំងនេះ សូមជ្រើស Honda Air Blade 125cc។</li><li><b>គេងមិនលក់?</b> កុំជិះលើផ្លូវភ្នំដែលមានអ័ព្ទ និងសើម ពេលកំពុងហត់។ ផឹកកាហ្វេក្តៅ ញ៉ាំអាហារពេលព្រឹកសិន ភ្ញាក់ស្រឡះហើយសឹមចេញ។</li><li><b>មានវ៉ាលីធំ?</b> កុំដឹកលើម៉ូតូ។ ផ្ញើទុកនៅសណ្ឋាគារសិន — សណ្ឋាគារជាច្រើនរក្សាឥវ៉ាន់មុនពេលចូលបន្ទប់ — ឬជួល 2 ថ្ងៃឡើងទៅ ហើយយើងដឹកម៉ូតូទៅសណ្ឋាគារកណ្តាលក្រុងដោយឥតគិតថ្លៃ។</li><li>ពាក់មួកសុវត្ថិភាព មិនផឹកស្រា ឬបៀរពេលជិះ និងគោរពច្បាប់ចរាចរណ៍វៀតណាមយ៉ាងម៉ឺងម៉ាត់។</li></ul><p>ហេតុផលបន្ថែមដើម្បីចេញដំណើរពីព្រឹក៖ <a href=\"{ART:lt-early}\">ជួលម៉ូតូនៅដាឡាត់ពីព្រឹកព្រលឹម</a>។</p>"),
 ],
 "faq_h": "សំណួរដែលសួរញឹកញាប់",
 "faq": [
  ("ឡានយប់ពីហូជីមិញមកដល់ដាឡាត់ម៉ោងប៉ុន្មាន?", "ជាធម្មតាប្រហែលម៉ោង 4:00 ដល់ 7:00 ព្រឹក អាស្រ័យលើក្រុមហ៊ុន ចរាចរណ៍ និងអាកាសធាតុលើផ្លូវភ្នំ។ សូមសួរក្រុមហ៊ុនពីម៉ោងមកដល់ប្រហាក់ប្រហែលពេលកក់សំបុត្រ។"),
  ("ឡានទម្លាក់ខ្ញុំនៅឯណាក្នុងដាឡាត់?", "នៅចំណតឡានអន្តរខេត្តដាឡាត់ ផ្លូវ Tô Hiến Thành (បើក 24 ម៉ោង) ឬការិយាល័យក្រុមហ៊ុនក្នុងក្រុង។ ឡានលីមូស៊ីនខ្លះទម្លាក់ដល់សណ្ឋាគារ។ សូមសួរពេលកក់។"),
  ("អាចជួលម៉ូតូម៉ោង 4:30 ព្រឹកបានទេ?", "បាន។ ហាងរបស់យើងបើករាល់ថ្ងៃម៉ោង 4:30 ព្រឹក។ ប្រាប់យើងពីល្ងាចមុនពីម៉ោងមកដល់ និងប្រភេទម៉ូតូ ម៉ូតូនឹងរៀបចំរួចពេលអ្នកមកដល់។"),
  ("អាចដឹកម៉ូតូទៅចំណតឡានបានទេ?", "ការដឹកឥតគិតថ្លៃសម្រាប់សណ្ឋាគារនៅកណ្តាលក្រុងដាឡាត់ ពេលជួល 2 ថ្ងៃឡើងទៅ។ ករណីផ្សេង សូមផ្ញើផែនការរបស់អ្នកមក យើងនឹងប្រាប់ថាអាចធ្វើបានឬអត់។"),
  ("ខ្ញុំមកពីញ៉ាត្រាងពេលរសៀល។ គួរជួលថ្ងៃនេះ ឬថ្ងៃស្អែក?", "ការជួលមួយថ្ងៃរហូតដល់ម៉ោង 21:00 ដូច្នេះយកពេលរសៀលល្ងាចក៏នៅតែគិតមួយថ្ងៃពេញ។ បើត្រូវការម៉ូតូតែពីព្រឹកស្អែក សូមមកយកចាប់ពីម៉ោង 4:30 — ឬជួល 2 ថ្ងៃឡើងទៅ ដើម្បីទទួលការដឹកឥតគិតថ្លៃទៅសណ្ឋាគារកណ្តាលក្រុង។"),
 ],
 "more_h": "រៀបចំផែនការបន្ត",
 "more": [("{ART:getting}", "របៀបទៅដាឡាត់"), ("{MAP:busmap}", "ផែនទីឡានក្រុងដាឡាត់ – សៃហ្គន"), ("{MAP:nhatrangbusmap}", "ផែនទីឡានក្រុងញ៉ាត្រាង – ដាឡាត់"), ("{ART:lt-early}", "ជួលម៉ូតូចាប់ពីម៉ោង 4:30"), ("{HOME}", "ជួលម៉ូតូនៅដាឡាត់ — ប្រភេទម៉ូតូ និងតម្លៃ")],
}

T["lo"] = {
 "title": "ຮອດດາລາດແຕ່ເຊົ້າມືດດ້ວຍລົດເມກາງຄືນ: 4–5 ໂມງເຮັດຫຍັງ? | Van Phu",
 "desc": "ລົດເມນອນກາງຄືນຈາກນະຄອນໂຮ່ຈີມິນ ສ່ວນຫຼາຍຮອດດາລາດປະມານ 4–7 ໂມງເຊົ້າ. ຈອດຢູ່ໃສ, ເຂົ້າເມືອງແນວໃດ ແລະ ຮັບລົດຈັກໄດ້ແຕ່ 4:30.",
 "h1": "ຮອດດາລາດແຕ່ເຊົ້າມືດດ້ວຍລົດເມກາງຄືນ: ຄວນເຮັດຫຍັງ?",
 "crumb": "ຮອດດາລາດແຕ່ເຊົ້າມືດ",
 "lead": "ລົດເມນອນກາງຄືນຈາກນະຄອນໂຮ່ຈີມິນ ສ່ວນຫຼາຍຮອດດາລາດປະມານ <b>4:00 ຫາ 7:00 ໂມງເຊົ້າ</b> ຕອນທີ່ເມືອງຍັງບໍ່ຕື່ນ. ຮ້ານເຊົ່າລົດຂອງພວກເຮົາເປີດ <b>ທຸກມື້ແຕ່ 4:30 ໂມງເຊົ້າ</b> ລົງລົດບໍ່ດົນທ່ານກໍຂີ່ລົດຈັກອອກທ່ຽວໄດ້ເລີຍ. ນີ້ແມ່ນວິທີຈັດການເຊົ້າມື້ທຳອິດ.",
 "short_h": "ສະຫຼຸບສັ້ນໆ",
 "short": [
  ("ໂຮ່ຈີມິນ → ດາລາດ", "ປະມານ 300 ກມ; ລົດເມນອນປະມານ 6–8 ຊົ່ວໂມງ; ລົດກາງຄືນສ່ວນຫຼາຍຮອດປະມານ 4:00–7:00"),
  ("ຍາຈາງ → ດາລາດ", "ປະມານ 135–140 ກມ; ປະມານ 3.5–4 ຊົ່ວໂມງ; ລົດແລ່ນຕອນກາງເວັນ"),
  ("ລົດຈອດຢູ່ໃສ", "ສະຖານີລົດເມລະຫວ່າງແຂວງດາລາດ (1 Tô Hiến Thành ເປີດ 24 ຊົ່ວໂມງ) ຫຼື ຫ້ອງການຂອງບໍລິສັດລົດເອງ"),
  ("ສະຖານີ → ຮ້ານພວກເຮົາ", "ປະມານ 3 ກມ ເປັນເສັ້ນຊື່, ທາງຈິງໄກກວ່າໜ້ອຍໜຶ່ງ — ແທັກຊີ ຫຼື Grab"),
  ("ຮ້ານຂອງພວກເຮົາ", "1/15/5 Thông Thiên Học — ເປີດທຸກມື້ແຕ່ 4:30 ໂມງເຊົ້າ"),
  ("ອຸນຫະພູມຕອນເຊົ້າມືດ", "ສ່ວນຫຼາຍປະມານ 10–15 °C — ເອົາເສື້ອກັນໜາວໄວ້ໃກ້ມື"),
 ],
 "secs": [
  ("ລົດກາງຄືນຈາກໂຮ່ຈີມິນ: ຮອດຈັກໂມງ", "<p>ລົດເມນອນອອກຈາກນະຄອນໂຮ່ຈີມິນຕອນແລງ ແລ່ນປະມານ 300 ກມ ໃຊ້ເວລາປະມານ 6–8 ຊົ່ວໂມງ. ເວລາຮອດຈິງຂຶ້ນກັບບໍລິສັດ, ການຈະລາຈອນ ແລະ ອາກາດເທິງທາງພູ ແຕ່ລົດກາງຄືນສ່ວນຫຼາຍເຂົ້າດາລາດລະຫວ່າງປະມານ 4:00 ຫາ 7:00 ໂມງເຊົ້າ.</p><p>ຕອນຈອງປີ້ ໃຫ້ຖາມວ່າລົດຈອດຢູ່ໃສໃນດາລາດ: ສະຖານີລົດເມລະຫວ່າງແຂວງເທິງຖະໜົນ Tô Hiến Thành, ຫ້ອງການບໍລິສັດໃນເມືອງ ຫຼື — ລົດຕູ້ລີມູຊີນບາງເຈົ້າ — ສົ່ງຮອດໂຮງແຮມ. ສະຖານີ ແລະ ຫ້ອງການບໍລິສັດຫຼັກມີຢູ່ໃນ<a href=\"{MAP:busmap}\">ແຜນທີ່ລົດເມດາລາດ – ໄຊ່ງ່ອນ</a>ຂອງພວກເຮົາ. ມາຈາກດານັງ ຫຼື ຮອຍອານ? ເບິ່ງ<a href=\"{MAP:danangbusmap}\">ແຜນທີ່ລົດເມດາລາດ – ດານັງ</a>.</p>"),
  ("ຈາກຍາຈາງ: ລົດຮອບກາງເວັນ", "<p>ຍາຈາງໃກ້ກວ່າ — ປະມານ 135–140 ກມ ຂ້າມຊ່ອງພູວິວງາມ ປະມານ 3.5–4 ຊົ່ວໂມງ — ແລະ ລົດແລ່ນຕອນກາງເວັນ ສະນັ້ນສ່ວນຫຼາຍທ່ານຈະຮອດດາລາດຕອນສວາຍ ຫຼື ຕອນບ່າຍ. ຫ້ອງການບໍລິສັດຫຼັກມີຢູ່ໃນ<a href=\"{MAP:nhatrangbusmap}\">ແຜນທີ່ລົດເມຍາຈາງ – ດາລາດ</a> ແລະ ວິທີເດີນທາງຢູ່ໃນບົດຄວາມ<a href=\"{ART:getting}\">ວິທີໄປດາລາດ</a>.</p><p>ຄວນຮູ້: ການເຊົ່າ 1 ມື້ນັບແຕ່ເວລາຮັບລົດຈົນຮອດ 21:00. ຖ້າຮອດ 16:00 ແລ້ວຮັບລົດເລີຍ ກໍຍັງນັບເປັນ 1 ມື້ເຕັມ. ແຂກຫຼາຍຄົນເຊັກອິນ ພັກຜ່ອນ ແລ້ວມາຮັບລົດເຊົ້າມື້ຕໍ່ໄປແຕ່ 4:30. ເຊົ່າ 2 ມື້ຂຶ້ນໄປ? ພວກເຮົາສົ່ງລົດຟຣີຮອດໂຮງແຮມໃນໃຈກາງເມືອງດາລາດ.</p>"),
  ("ແຕ່ລົງລົດເມຈົນໄດ້ຂີ່ລົດຈັກ", "<ol><li><b>ແລງມື້ກ່ອນ:</b> ສົ່ງຂໍ້ຄວາມຫາພວກເຮົາທາງ WhatsApp (+84 944 081 101 ຫຼື +84 834 622 149) ຫຼື Telegram (@vanphudalat) ບອກບໍລິສັດລົດ, ເວລາຮອດໂດຍປະມານ ແລະ ລົດທີ່ຕ້ອງການ.</li><li><b>ລົງລົດແລ້ວ</b> ຂີ່ແທັກຊີ ຫຼື Grab ມາທີ່ 1/15/5 Thông Thiên Học. ກ່ອນແຈ້ງ ເອີ້ນ Grab ອາດຍາກ ສ່ວນແທັກຊີມັກລໍຖ້າຢູ່ສະຖານີ.</li><li><b>ເອກະສານບໍ່ເທົ່າໃດນາທີ:</b> ໜັງສືຜ່ານແດນ (ບໍ່ມີເງິນມັດຈຳ) ແລະ ລົດທຸກຄັນ 150,000 VND ຕໍ່ມື້.</li><li><b>ທົດລອງຂີ່ສັ້ນໆ</b> ແລະ ຖ່າຍວິດີໂອສະພາບລົດນຳກັນ.</li><li><b>ອອກເດີນທາງ.</b> ການເຊົ່າ 1 ມື້ຮອດ 21:00 ລົດທີ່ຮັບຕອນ 4:30 ຈຶ່ງໃຊ້ໄດ້ໝົດມື້.</li></ol>"),
  ("ຊົ່ວໂມງທຳອິດ: ໄປເບິ່ງຕາເວັນຂຶ້ນ ຫຼື ພັກກ່ອນ?", "<ul><li><b>ນອນຫຼັບດີເທິງລົດ?</b> ແສງທີ່ງາມທີ່ສຸດຂອງດາລາດແມ່ນຕອນນີ້. ໄປ<a href=\"{ART:cloudhunt}\">ລ່າທະເລໝອກ</a> ຫຼື <a href=\"{ART:caudat}\">ເບິ່ງຕາເວັນຂຶ້ນທີ່ສວນຊາ Cau Dat</a> — ທາງຂຶ້ນພູແບບນີ້ແນະນຳ Honda Air Blade 125cc.</li><li><b>ນອນບໍ່ຄ່ອຍຫຼັບ?</b> ຢ່າຂີ່ທາງພູທີ່ມີໝອກ ແລະ ປຽກຕອນເມື່ອຍ. ດື່ມກາເຟຮ້ອນ ກິນເຂົ້າເຊົ້າກ່ອນ ສົດຊື່ນແລ້ວຈຶ່ງໄປ.</li><li><b>ມີກະເປົ໋າໃຫຍ່?</b> ຢ່າບັນທຸກເທິງລົດຈັກ. ຝາກໄວ້ໂຮງແຮມກ່ອນ — ໂຮງແຮມຫຼາຍແຫ່ງຮັບຝາກເຄື່ອງກ່ອນເຊັກອິນ — ຫຼື ເຊົ່າ 2 ມື້ຂຶ້ນໄປ ແລ້ວພວກເຮົາສົ່ງລົດຟຣີຮອດໂຮງແຮມໃນເມືອງ.</li><li>ໃສ່ໝວກກັນກະທົບ, ບໍ່ດື່ມເຫຼົ້າ ຫຼື ເບຍຂະນະຂີ່ ແລະ ປະຕິບັດຕາມກົດຈະລາຈອນຫວຽດນາມຢ່າງເຂັ້ມງວດ.</li></ul><p>ເຫດຜົນເພີ່ມເຕີມທີ່ຄວນອອກແຕ່ເຊົ້າ: <a href=\"{ART:lt-early}\">ເຊົ່າລົດຈັກຢູ່ດາລາດແຕ່ເຊົ້າມືດ</a>.</p>"),
 ],
 "faq_h": "ຄຳຖາມທີ່ພົບເລື້ອຍ",
 "faq": [
  ("ລົດກາງຄືນຈາກໂຮ່ຈີມິນຮອດດາລາດຈັກໂມງ?", "ສ່ວນຫຼາຍປະມານ 4:00 ຫາ 7:00 ໂມງເຊົ້າ ຂຶ້ນກັບບໍລິສັດ, ການຈະລາຈອນ ແລະ ອາກາດເທິງທາງພູ. ຖາມເວລາຮອດໂດຍປະມານຕອນຈອງປີ້."),
  ("ລົດສົ່ງຢູ່ໃສໃນດາລາດ?", "ຢູ່ສະຖານີລົດເມລະຫວ່າງແຂວງດາລາດ ຖະໜົນ Tô Hiến Thành (ເປີດ 24 ຊົ່ວໂມງ) ຫຼື ຫ້ອງການບໍລິສັດໃນເມືອງ. ລົດຕູ້ລີມູຊີນບາງເຈົ້າສົ່ງຮອດໂຮງແຮມ. ຖາມຕອນຈອງ."),
  ("ເຊົ່າລົດຈັກຕອນ 4:30 ໂມງເຊົ້າໄດ້ບໍ?", "ໄດ້. ຮ້ານພວກເຮົາເປີດທຸກມື້ 4:30 ໂມງເຊົ້າ. ບອກເວລາຮອດ ແລະ ລົດທີ່ຕ້ອງການໄວ້ແຕ່ແລງມື້ກ່ອນ ລົດຈະພ້ອມເມື່ອທ່ານມາຮອດ."),
  ("ສົ່ງລົດໄປສະຖານີລົດເມໄດ້ບໍ?", "ສົ່ງຟຣີສຳລັບໂຮງແຮມໃນໃຈກາງເມືອງດາລາດ ເມື່ອເຊົ່າ 2 ມື້ຂຶ້ນໄປ. ກໍລະນີອື່ນ ສົ່ງແຜນເດີນທາງມາ ພວກເຮົາຈະບອກວ່າເຮັດໄດ້ບໍ."),
  ("ຮອດຈາກຍາຈາງຕອນບ່າຍ ຮັບລົດມື້ນີ້ ຫຼື ມື້ອື່ນດີ?", "ການເຊົ່າ 1 ມື້ຮອດ 21:00 ຮັບລົດຕອນບ່າຍແກ່ກໍນັບເປັນມື້ເຕັມ. ຖ້າຕ້ອງການລົດແຕ່ເຊົ້າມື້ຕໍ່ໄປ ໃຫ້ມາຮັບແຕ່ 4:30 — ຫຼື ເຊົ່າ 2 ມື້ຂຶ້ນໄປ ເພື່ອໄດ້ສົ່ງລົດຟຣີຮອດໂຮງແຮມໃນເມືອງ."),
 ],
 "more_h": "ວາງແຜນຕໍ່",
 "more": [("{ART:getting}", "ວິທີໄປດາລາດ"), ("{MAP:busmap}", "ແຜນທີ່ລົດເມດາລາດ – ໄຊ່ງ່ອນ"), ("{MAP:nhatrangbusmap}", "ແຜນທີ່ລົດເມຍາຈາງ – ດາລາດ"), ("{ART:lt-early}", "ເຊົ່າລົດແຕ່ 4:30"), ("{HOME}", "ເຊົ່າລົດຈັກຢູ່ດາລາດ — ລົດ ແລະ ລາຄາ")],
}

T["my"] = {
 "title": "ညဘတ်စ်ဖြင့် ဒါလတ်ကို မနက်စောစော ရောက်လျှင် ဘာလုပ်မလဲ? | Van Phu",
 "desc": "ဟိုချီမင်းမြို့မှ ညဘက် အိပ်ယာပါဘတ်စ်ကားများသည် ဒါလတ်သို့ မနက် 4–7 နာရီခန့်တွင် ရောက်လေ့ရှိသည်။ ဘယ်မှာရပ်သလဲ၊ မြို့လယ်သို့ ဘယ်လိုသွားမလဲ၊ မနက် 4:30 မှ စကူတာယူနိုင်ပုံ။",
 "h1": "ညဘတ်စ်ဖြင့် ဒါလတ်ကို မနက်စောစော ရောက်လျှင် — ဘာလုပ်ရမလဲ",
 "crumb": "ဒါလတ်ကို မနက်စောစော ရောက်ခြင်း",
 "lead": "ဟိုချီမင်းမြို့မှ ညဘက် အိပ်ယာပါဘတ်စ်ကားသည် ဒါလတ်သို့ <b>မနက် 4:00 မှ 7:00 ခန့်</b>တွင် ရောက်လေ့ရှိပြီး မြို့က မနိုးသေးချိန် ဖြစ်သည်။ ကျွန်ုပ်တို့၏ ငှားရမ်းဆိုင်သည် <b>နေ့တိုင်း မနက် 4:30 မှ</b> ဖွင့်သောကြောင့် ကားပေါ်မှဆင်းပြီး မကြာမီ စကူတာဖြင့် ထွက်နိုင်သည်။ ပထမဆုံး မနက်ကို ဤသို့ စီစဉ်ပါ။",
 "short_h": "အကျဉ်းချုပ်",
 "short": [
  ("ဟိုချီမင်း → ဒါလတ်", "300 km ခန့်; အိပ်ယာပါဘတ်စ် 6–8 နာရီခန့်; ညဘတ်စ်များ များသောအားဖြင့် 4:00–7:00 ခန့် ရောက်"),
  ("ညာချန် → ဒါလတ်", "135–140 km ခန့်; 3.5–4 နာရီခန့်; နေ့ဘက်တွင် ပြေးဆွဲ"),
  ("ကားရပ်သည့်နေရာ", "ဒါလတ် ပြည်နယ်ပြေး ဘတ်စ်ကားဂိတ် (1 Tô Hiến Thành၊ 24 နာရီဖွင့်) သို့မဟုတ် ကားကုမ္ပဏီ၏ ကိုယ်ပိုင်ရုံး"),
  ("ကားဂိတ် → ကျွန်ုပ်တို့ဆိုင်", "မျဉ်းဖြောင့် 3 km ခန့်၊ လမ်းအတိုင်း နည်းနည်းပိုဝေး — တက္ကစီ သို့မဟုတ် Grab"),
  ("ကျွန်ုပ်တို့ဆိုင်", "1/15/5 Thông Thiên Học — နေ့တိုင်း မနက် 4:30 မှ ဖွင့်"),
  ("မနက်စောစော အပူချိန်", "10–15 °C ခန့် ဖြစ်လေ့ရှိ — အနွေးထည်ကို လက်လှမ်းမီရာတွင် ထားပါ"),
 ],
 "secs": [
  ("ဟိုချီမင်းမှ ညဘတ်စ် — ဘယ်အချိန် ရောက်မလဲ", "<p>အိပ်ယာပါဘတ်စ်ကားများသည် ဟိုချီမင်းမြို့မှ ညနေပိုင်းတွင် ထွက်ပြီး 300 km ခန့်ကို 6–8 နာရီခန့် မောင်းသည်။ ရောက်ချိန်အတိအကျသည် ကုမ္ပဏီ၊ ယာဉ်ကြောနှင့် တောင်လမ်းပေါ်ရှိ ရာသီဥတုပေါ် မူတည်သော်လည်း ညဘတ်စ်အများစုသည် မနက် 4:00 မှ 7:00 ခန့်အတွင်း ဒါလတ်သို့ ဝင်လာသည်။</p><p>လက်မှတ်ဝယ်သည့်အခါ ဒါလတ်တွင် ဘယ်မှာ ရပ်မလဲ မေးပါ — Tô Hiến Thành လမ်းရှိ ပြည်နယ်ပြေး ဘတ်စ်ကားဂိတ်၊ မြို့ထဲရှိ ကုမ္ပဏီရုံး၊ သို့မဟုတ် လီမိုဇင်းဗင်အချို့ဆိုလျှင် ဟိုတယ်အထိ။ ကားဂိတ်နှင့် အဓိက ကုမ္ပဏီရုံးများကို ကျွန်ုပ်တို့၏ <a href=\"{MAP:busmap}\">ဒါလတ် – ဆိုင်ဂုံ ဘတ်စ်ကားမြေပုံ</a> တွင် ကြည့်နိုင်သည်။ ဒါနန် သို့မဟုတ် ဟွိုင်အန်မှ လာမည်လား? <a href=\"{MAP:danangbusmap}\">ဒါလတ် – ဒါနန် ဘတ်စ်ကားမြေပုံ</a> ကို ကြည့်ပါ။</p>"),
  ("ညာချန်မှ — နေ့ဘက်ဘတ်စ်", "<p>ညာချန်က ပိုနီးသည် — လှပသော တောင်ကြားကို ဖြတ်၍ 135–140 km ခန့်၊ 3.5–4 နာရီခန့် — ကားများ နေ့ဘက်တွင် ပြေးသောကြောင့် ဒါလတ်ကို နေ့လယ်ပိုင်း သို့မဟုတ် နေ့ခင်းဘက်တွင် ရောက်လေ့ရှိသည်။ အဓိက ကုမ္ပဏီရုံးများကို <a href=\"{MAP:nhatrangbusmap}\">ညာချန် – ဒါလတ် ဘတ်စ်ကားမြေပုံ</a> တွင်၊ ခရီးသွားနည်းများကို <a href=\"{ART:getting}\">ဒါလတ်သို့ သွားနည်း</a> ဆောင်းပါးတွင် ကြည့်ပါ။</p><p>သိထားရန် — ငှားရမ်းမှု တစ်ရက်ကို ယူသည့်အချိန်မှ ည 21:00 အထိ တွက်သည်။ 16:00 တွင် ရောက်ပြီး ချက်ချင်းယူလျှင်လည်း တစ်ရက်ပြည့် တွက်သည်။ ဧည့်သည်အများအပြားသည် ဟိုတယ်ဝင်ပြီး အနားယူကာ နောက်တစ်နေ့ မနက် 4:30 မှ လာယူကြသည်။ 2 ရက်နှင့်အထက် ငှားမလား? ဒါလတ်မြို့လယ်ရှိ ဟိုတယ်အထိ အခမဲ့ ပို့ပေးပါသည်။</p>"),
  ("ဘတ်စ်ကားမှဆင်းပြီး စကူတာစီးသည်အထိ", "<ol><li><b>မနေ့ညနေ:</b> WhatsApp (+84 944 081 101 သို့မဟုတ် +84 834 622 149) သို့မဟုတ် Telegram (@vanphudalat) ဖြင့် ကားကုမ္ပဏီ၊ ခန့်မှန်းရောက်ချိန်နှင့် လိုချင်သော ဆိုင်ကယ်ကို ပြောပါ။</li><li><b>ကားပေါ်မှ ဆင်းပြီးနောက်</b> တက္ကစီ သို့မဟုတ် Grab ဖြင့် 1/15/5 Thông Thiên Học သို့ လာပါ။ မိုးမလင်းမီ Grab ခေါ်ရခက်နိုင်ပြီး တက္ကစီများကမူ ကားဂိတ်တွင် စောင့်နေလေ့ရှိသည်။</li><li><b>စာရွက်စာတမ်း မိနစ်အနည်းငယ်:</b> နိုင်ငံကူးလက်မှတ် (ငွေသားအာမခံ မလို) နှင့် ဆိုင်ကယ်တိုင်း တစ်ရက် 150,000 VND။</li><li><b>ခဏ စမ်းစီးပြီး</b> ဆိုင်ကယ်အခြေအနေကို အတူ ဗီဒီယိုရိုက်သည်။</li><li><b>ထွက်ခွာပါ။</b> ငှားရမ်းမှု တစ်ရက်သည် 21:00 အထိ ဖြစ်သောကြောင့် 4:30 တွင် ယူသော စကူတာကို တစ်နေကုန် သုံးနိုင်သည်။</li></ol>"),
  ("ပထမ နာရီအနည်းငယ် — နေထွက်ကြည့်မလား၊ အရင် အနားယူမလား?", "<ul><li><b>ကားပေါ်မှာ ကောင်းကောင်းအိပ်ရသလား?</b> ဒါလတ်၏ အလှဆုံးအလင်းရောင်က အခုပါ။ <a href=\"{ART:cloudhunt}\">တိမ်ပင်လယ်ရှာ</a> သွားပါ သို့မဟုတ် <a href=\"{ART:caudat}\">Cau Dat လက်ဖက်ခြံတွင် နေထွက်ကြည့်</a>ပါ — ဤတောင်တက်လမ်းများအတွက် Honda Air Blade 125cc ကို ရွေးပါ။</li><li><b>အိပ်မပျော်ခဲ့ဘူးလား?</b> ပင်ပန်းနေစဉ် မြူဆိုင်းပြီး စိုစွတ်သော တောင်လမ်းပေါ် မစီးပါနှင့်။ ကော်ဖီပူပူနှင့် မနက်စာ အရင်စားပြီး လန်းဆန်းမှ ထွက်ပါ။</li><li><b>ခရီးဆောင်သေတ္တာကြီး ပါလား?</b> စကူတာပေါ်တွင် မတင်ပါနှင့်။ ဟိုတယ်တွင် အရင်အပ်ထားပါ — ဟိုတယ်များစွာက ဝင်ချိန်မတိုင်မီ ပစ္စည်းအပ်လက်ခံသည် — သို့မဟုတ် 2 ရက်နှင့်အထက် ငှားလျှင် မြို့လယ်ဟိုတယ်အထိ အခမဲ့ ပို့ပေးမည်။</li><li>ဦးထုပ်ဆောင်းပါ၊ စီးနေစဉ် အရက် သို့မဟုတ် ဘီယာ မသောက်ပါနှင့်၊ ဗီယက်နမ် ယာဉ်စည်းကမ်းကို တင်းကျပ်စွာ လိုက်နာပါ။</li></ul><p>စောစောထွက်ရန် နောက်ထပ် အကြောင်းများ: <a href=\"{ART:lt-early}\">ဒါလတ်တွင် မနက်စောစော ဆိုင်ကယ်ငှားခြင်း</a>။</p>"),
 ],
 "faq_h": "မေးလေ့ရှိသော မေးခွန်းများ",
 "faq": [
  ("ဟိုချီမင်းမှ ညဘတ်စ်သည် ဒါလတ်ကို ဘယ်အချိန် ရောက်သလဲ?", "များသောအားဖြင့် မနက် 4:00 မှ 7:00 ခန့်ဖြစ်ပြီး ကုမ္ပဏီ၊ ယာဉ်ကြောနှင့် တောင်လမ်းပေါ်ရှိ ရာသီဥတုပေါ် မူတည်သည်။ လက်မှတ်ဝယ်သည့်အခါ ခန့်မှန်းရောက်ချိန်ကို မေးပါ။"),
  ("ဒါလတ်တွင် ကားက ဘယ်မှာ ချပေးသလဲ?", "Tô Hiến Thành လမ်းရှိ ဒါလတ် ပြည်နယ်ပြေး ဘတ်စ်ကားဂိတ် (24 နာရီဖွင့်) သို့မဟုတ် မြို့ထဲရှိ ကုမ္ပဏီရုံး။ လီမိုဇင်းဗင်အချို့က ဟိုတယ်အထိ ပို့သည်။ လက်မှတ်ဝယ်သည့်အခါ မေးပါ။"),
  ("မနက် 4:30 တွင် စကူတာ ငှားနိုင်သလား?", "ငှားနိုင်ပါသည်။ ကျွန်ုပ်တို့ဆိုင်သည် နေ့တိုင်း မနက် 4:30 တွင် ဖွင့်သည်။ မနေ့ညနေကတည်းက ရောက်ချိန်နှင့် ဆိုင်ကယ်ကို ပြောထားလျှင် သင်ရောက်ချိန်တွင် အသင့်ဖြစ်နေမည်။"),
  ("ဘတ်စ်ကားဂိတ်အထိ ဆိုင်ကယ် ပို့ပေးနိုင်သလား?", "အခမဲ့ပို့ဆောင်မှုသည် 2 ရက်နှင့်အထက် ငှားလျှင် ဒါလတ်မြို့လယ်ရှိ ဟိုတယ်များအတွက်သာ ဖြစ်သည်။ အခြားကိစ္စများအတွက် သင့်အစီအစဉ်ကို ပို့ပါ၊ ဘာလုပ်ပေးနိုင်သလဲ ပြောပါမည်။"),
  ("ညာချန်မှ နေ့ခင်းဘက် ရောက်မည်။ ယနေ့ ငှားမလား၊ မနက်ဖြန် ငှားမလား?", "ငှားရမ်းမှု တစ်ရက်သည် 21:00 အထိ ဖြစ်သောကြောင့် ညနေစောင်းတွင် ယူလည်း တစ်ရက်ပြည့် တွက်သည်။ နောက်တစ်နေ့ မနက်မှသာ လိုလျှင် 4:30 မှ လာယူပါ — သို့မဟုတ် 2 ရက်နှင့်အထက် ငှားပြီး မြို့လယ်ဟိုတယ်အထိ အခမဲ့ ပို့ဆောင်မှု ရယူပါ။"),
 ],
 "more_h": "ဆက်လက် စီစဉ်ရန်",
 "more": [("{ART:getting}", "ဒါလတ်သို့ သွားနည်း"), ("{MAP:busmap}", "ဒါလတ် – ဆိုင်ဂုံ ဘတ်စ်ကားမြေပုံ"), ("{MAP:nhatrangbusmap}", "ညာချန် – ဒါလတ် ဘတ်စ်ကားမြေပုံ"), ("{ART:lt-early}", "မနက် 4:30 မှ ဆိုင်ကယ်ငှား"), ("{HOME}", "ဒါလတ် ဆိုင်ကယ်ငှား — ဆိုင်ကယ်များနှင့် ဈေးနှုန်း")],
}

assert set(T) == set(LANGS), set(LANGS) ^ set(T)
