"""NOT BUILT since 2026-11-28 (owner: no licence content anywhere on the site; guests ask by message). Old URLs redirect to the rental home.
The electric fleet is VinFast Feliz II, so the old 'no licence for electric' claim below is WRONG — never reuse it.
Licence pillar page — 'Do I need a licence to rent a motorbike in Vietnam?' (owner asked 2026-10-28, all languages).
The ONLY place (with guides.py) where licence wording is allowed; check.py scans this file for every other rule.
Owner-confirmed facts (2026-10-28):
- Electric scooters are mopeds (xe gắn máy): top speed up to 50 km/h, motor up to 4 kW -> no licence needed (Law 36/2024/QH15).
- Gas scooters (Honda Vision 110cc, Honda Air Blade 125cc) need a motorbike licence valid under Vietnamese law (A1 covers up to 125cc).
- Owner's choice: do NOT go into international-permit details; say only "a licence valid under Vietnamese law".
- Minimum age for a moped under Law 36/2024: 16.
Placeholders in html/faq: {EV} electric page, {HOME} rental home, {DOCS} documents article, {RULES} EV rules article, {ROUTES} routes page.
Never: price in title/desc (owner rule 2026-10-16), weight limit (kept off this page), any range wording other than the approved one."""
LANGS = ["en", "vi", "ru", "zh", "ko", "ja", "th", "id", "ms", "de", "fr", "es", "he", "it", "nl", "km", "lo", "my"]
EN_SLUG = "do-i-need-a-license-to-rent-a-motorbike-in-vietnam"
SLUG = {l: EN_SLUG for l in LANGS}
SLUG["vi"] = "thue-xe-may-co-can-bang-lai"
SLUG["ru"] = "nuzhny-li-prava-chtoby-arendovat-bayk-vo-vetname"
UPDATED = "2026-10-28"
T = {}

T["en"] = {
 "title": "Do I Need a License to Rent a Motorbike in Vietnam? | Van Phu",
 "desc": "Gas scooters in Vietnam need a valid motorbike license. Electric scooters in the moped class (up to 50 km/h) don't. What this means when you rent in Da Lat.",
 "h1": "Do I Need a License to Rent a Motorbike in Vietnam?",
 "crumb": "Motorbike license in Vietnam",
 "lead": "Short answer: <b>for a gas scooter, yes</b> — you need a motorbike license that is valid under Vietnamese law. <b>For an electric scooter in the moped class, no</b> — our electric scooters (top speed up to 50 km/h) can be ridden without a license. Here is what that means when you rent in Da Lat.",
 "short_h": "Quick answer",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (gas)", "License needed — a motorbike license valid in Vietnam (category A1 or higher)"),
  ("Electric scooter (moped: up to 50 km/h, motor up to 4 kW)", "No license needed"),
  ("Minimum age for an electric moped", "16 years"),
  ("Helmet", "Required for rider and passenger — included free"),
  ("What we keep at the shop", "Your passport or ID card — no cash deposit"),
 ],
 "secs": [
  ("Why electric scooters don't need a license", "<p>Vietnam's Road Traffic Order and Safety Law 2024 (No. 36/2024/QH15, in force since 1 January 2025) requires a driving license for every motor vehicle <b>except mopeds</b>. A moped (<i>xe gắn máy</i>) is a two-wheeler with a top design speed of up to 50 km/h; for electric models the motor is up to 4 kW.</p><p>Our electric scooters are in this moped class, so you can ride them in Vietnam without a license. Everything else still applies: wear your helmet, no alcohol or beer when riding, and strictly follow Vietnamese traffic law.</p>"),
  ("Gas scooters need a valid license", "<p>The Honda Vision 110cc and Honda Air Blade 125cc are motorcycles above 50cc. To ride them you need a motorbike license that is valid under Vietnamese law — category A1 covers bikes up to 125cc.</p><p>If you are visiting from abroad, check before your trip whether your license is valid in Vietnam. Not sure? The electric scooter is the simple choice: same price, no license.</p>"),
  ("No license? What an electric scooter can do in Da Lat", "<ul><li><b>Good for:</b> the city centre, Xuan Huong Lake, cafés, the night market and nearby sights.</li><li><b>Battery:</b> one battery lasts about 25–30 km, and each scooter comes with 2 batteries — about 50–60 km in total. We swap in a full battery at the shop for 20,000 VND.</li><li><b>Avoid:</b> long, steep climbs such as Prenn Pass, Mimosa Pass and the road up Lang Biang. For those, riders with a valid license take the Air Blade 125cc.</li></ul><p>Please read our short <a href=\"{RULES}\">electric scooter rental rules</a> before pick-up.</p>"),
  ("What you need to rent at Van Phu", "<ul><li><b>Foreign guests:</b> your original passport. <b>Vietnamese guests:</b> your CCCD.</li><li>No cash deposit. 150,000 VND per day for every bike, fixed.</li><li>A short test ride and a video of the bike's condition that we film together.</li><li>Helmet and phone holder included; we open every day from 4:30 am.</li></ul><p>More details: <a href=\"{DOCS}\">what you need to rent a motorbike in Da Lat</a>.</p>"),
 ],
 "faq_h": "Frequently asked questions",
 "faq": [
  ("Do I need a license for an electric scooter in Vietnam?", "Not for an electric moped — one with a top speed of up to 50 km/h and a motor of up to 4 kW. Our electric scooters are in this class, so no license is needed. You must be at least 16."),
  ("Can I rent a gas scooter in Da Lat without a license?", "Vietnamese law requires a valid motorbike license for gas scooters such as the Honda Vision and Air Blade, so at Van Phu we rent them only to riders with a valid license. Without one, take an electric scooter."),
  ("Is my license from home valid in Vietnam?", "Only a license that is valid under Vietnamese law counts. The rules depend on the country that issued it, so check before you travel. If you are not sure, rent an electric scooter."),
  ("Is an electric scooter enough to explore Da Lat?", "For the city and nearby sights, yes. One battery lasts about 25–30 km, each scooter comes with 2 batteries (about 50–60 km in total), and a battery swap at the shop costs 20,000 VND. For long, steep passes a 125cc gas scooter is better."),
  ("Does the electric scooter cost less?", "No — every bike is 150,000 VND per day, with a helmet and phone holder included."),
 ],
 "more_h": "Read next",
 "more": [("{EV}", "Electric scooter rental in Da Lat"), ("{DOCS}", "What you need to rent a motorbike in Da Lat"), ("{RULES}", "Electric scooter rental rules"), ("{HOME}", "Da Lat motorbike rental — bikes and prices")],
}

T["vi"] = {
 "title": "Thuê xe máy có cần bằng lái không? Xe điện, xe ga 2026 | Văn Phú",
 "desc": "Thuê xe máy ở Việt Nam có cần bằng lái không: xe ga cần bằng hợp lệ (A1 trở lên), xe máy điện loại xe gắn máy (tối đa 50 km/h) không cần. Áp dụng khi thuê ở Đà Lạt.",
 "h1": "Thuê xe máy có cần bằng lái không?",
 "crumb": "Thuê xe máy có cần bằng lái",
 "lead": "Trả lời ngắn: <b>xe ga thì cần</b> bằng lái xe máy hợp lệ theo luật Việt Nam. <b>Xe máy điện loại xe gắn máy thì không cần</b> — xe điện của Văn Phú (tốc độ tối đa đến 50 km/h) đi được mà không cần bằng. Dưới đây là chi tiết khi bạn thuê xe ở Đà Lạt.",
 "short_h": "Trả lời nhanh",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (xe ga)", "Cần bằng lái xe máy hợp lệ (hạng A1 trở lên)"),
  ("Xe máy điện (xe gắn máy: tối đa 50 km/h, động cơ đến 4 kW)", "Không cần bằng lái"),
  ("Tuổi tối thiểu đi xe gắn máy điện", "Đủ 16 tuổi"),
  ("Mũ bảo hiểm", "Bắt buộc cho người lái và người ngồi sau — tiệm tặng kèm"),
  ("Tiệm giữ gì khi thuê", "CCCD hoặc hộ chiếu — không cọc tiền"),
 ],
 "secs": [
  ("Vì sao xe máy điện không cần bằng lái?", "<p>Luật Trật tự, an toàn giao thông đường bộ 2024 (Luật số 36/2024/QH15, hiệu lực từ 01/01/2025) yêu cầu người lái xe phải có giấy phép lái xe phù hợp, <b>trừ người lái xe gắn máy</b>. Xe gắn máy là xe hai bánh có vận tốc thiết kế tối đa không quá 50 km/h; với xe điện, công suất động cơ không quá 4 kW.</p><p>Xe điện của Văn Phú thuộc loại xe gắn máy, nên bạn đi được mà không cần bằng lái. Các quy định khác vẫn giữ nguyên: đội mũ bảo hiểm, không uống rượu bia khi lái xe và chấp hành nghiêm luật giao thông.</p>"),
  ("Xe ga cần bằng lái hợp lệ", "<p>Honda Vision 110cc và Honda Air Blade 125cc là xe mô tô trên 50cc. Để chạy các xe này, bạn cần bằng lái xe máy hợp lệ theo luật Việt Nam — hạng A1 dùng cho xe đến 125cc.</p><p>Chưa có bằng hoặc để quên bằng ở nhà? Xe máy điện là lựa chọn đơn giản: cùng giá, không cần bằng.</p>"),
  ("Không có bằng: xe điện đi được những đâu ở Đà Lạt?", "<ul><li><b>Phù hợp:</b> trung tâm, hồ Xuân Hương, quán cà phê, chợ đêm và các điểm gần thành phố.</li><li><b>Pin:</b> mỗi pin đi khoảng 25–30 km, mỗi xe có 2 pin — tổng khoảng 50–60 km. Đổi pin đầy tại tiệm 20.000 VND mỗi lần.</li><li><b>Nên tránh:</b> đèo dài, dốc như đèo Prenn, đèo Mimosa và đường lên Lang Biang. Nếu có bằng, bạn nên chọn Air Blade 125cc cho các cung này.</li></ul><p>Đọc nhanh <a href=\"{RULES}\">quy định thuê xe máy điện</a> trước khi nhận xe.</p>"),
  ("Thuê xe ở Văn Phú cần gì?", "<ul><li><b>Khách Việt Nam:</b> CCCD. <b>Khách nước ngoài:</b> hộ chiếu bản gốc.</li><li>Không cọc tiền. Giá cố định 150.000 VND/ngày cho mọi xe.</li><li>Chạy thử và cùng quay video tình trạng xe trước khi nhận.</li><li>Kèm mũ bảo hiểm và giá đỡ điện thoại; tiệm mở cửa từ 4:30 sáng mỗi ngày.</li></ul><p>Xem thêm: <a href=\"{DOCS}\">thuê xe máy Đà Lạt cần giấy tờ gì</a>.</p>"),
 ],
 "faq_h": "Câu hỏi thường gặp",
 "faq": [
  ("Xe máy điện có cần bằng lái không?", "Xe máy điện loại xe gắn máy (tốc độ tối đa đến 50 km/h, động cơ đến 4 kW) không cần bằng lái. Xe điện của Văn Phú thuộc loại này. Người lái phải đủ 16 tuổi."),
  ("Không có bằng có thuê xe ga ở Đà Lạt được không?", "Luật Việt Nam yêu cầu bằng lái hợp lệ khi chạy xe ga như Honda Vision, Air Blade, nên Văn Phú chỉ cho thuê xe ga khi bạn có bằng hợp lệ. Chưa có bằng thì thuê xe máy điện."),
  ("Đi xe ga 125cc cần bằng hạng gì?", "Hạng A1 dùng cho xe mô tô hai bánh đến 125cc, nên đủ cho Honda Vision 110cc và Air Blade 125cc."),
  ("Xe điện có đủ đi chơi Đà Lạt không?", "Đi trong thành phố và các điểm gần thì đủ. Mỗi pin khoảng 25–30 km, mỗi xe có 2 pin (tổng khoảng 50–60 km), đổi pin tại tiệm 20.000 VND. Đèo dài, dốc thì nên đi xe ga 125cc."),
  ("Thuê xe điện có rẻ hơn xe ga không?", "Không. Mọi xe đều 150.000 VND/ngày, kèm mũ bảo hiểm và giá đỡ điện thoại."),
 ],
 "more_h": "Đọc thêm",
 "more": [("{EV}", "Thuê xe máy điện Đà Lạt"), ("{DOCS}", "Thuê xe máy Đà Lạt cần giấy tờ gì"), ("{RULES}", "Quy định thuê xe máy điện"), ("{HOME}", "Thuê xe máy Đà Lạt — loại xe và giá")],
}

T["ru"] = {
 "title": "Нужны ли права, чтобы арендовать байк во Вьетнаме? | Van Phu",
 "desc": "Для бензинового скутера во Вьетнаме нужны права, действующие по вьетнамскому закону. Для электроскутера-мопеда (до 50 км/ч) права не нужны. Что это значит в Далате.",
 "h1": "Нужны ли права, чтобы арендовать байк во Вьетнаме?",
 "crumb": "Права на байк во Вьетнаме",
 "lead": "Коротко: <b>для бензинового скутера — да</b>, нужны мотоправа, действующие по вьетнамскому закону. <b>Для электроскутера класса «мопед» — нет</b>: наши электроскутеры (максимальная скорость до 50 км/ч) можно водить без прав. Ниже — что это значит при аренде в Далате.",
 "short_h": "Быстрый ответ",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (бензин)", "Нужны мотоправа, действующие во Вьетнаме (категория A1 или выше)"),
  ("Электроскутер (мопед: до 50 км/ч, мотор до 4 кВт)", "Права не нужны"),
  ("Минимальный возраст для электромопеда", "16 лет"),
  ("Шлем", "Обязателен для водителя и пассажира — выдаём бесплатно"),
  ("Что остаётся в прокате", "Паспорт или ID-карта — без денежного залога"),
 ],
 "secs": [
  ("Почему для электроскутера не нужны права", "<p>Закон Вьетнама о порядке и безопасности дорожного движения 2024 года (№ 36/2024/QH15, действует с 1 января 2025) требует водительское удостоверение для всех транспортных средств, <b>кроме мопедов</b>. Мопед (<i>xe gắn máy</i>) — это двухколёсный транспорт с конструктивной скоростью до 50 км/ч; у электрических моделей мощность мотора до 4 кВт.</p><p>Наши электроскутеры относятся к этому классу, поэтому ездить на них во Вьетнаме можно без прав. Всё остальное остаётся: шлем обязателен, никакого алкоголя за рулём, строго соблюдайте ПДД Вьетнама.</p>"),
  ("Для бензинового скутера нужны действующие права", "<p>Honda Vision 110cc и Honda Air Blade 125cc — это мотоциклы объёмом больше 50 куб. см. Для них нужны мотоправа, действующие по вьетнамскому закону; категория A1 охватывает мотоциклы до 125 куб. см.</p><p>Если вы приезжаете из другой страны, заранее проверьте, действуют ли ваши права во Вьетнаме. Не уверены — берите электроскутер: та же цена и права не нужны.</p>"),
  ("Без прав: где можно ездить на электроскутере в Далате", "<ul><li><b>Подходит для:</b> центра, озера Суанхыонг, кафе, ночного рынка и мест рядом с городом.</li><li><b>Батарея:</b> одной батареи хватает примерно на 25–30 км, у каждого скутера 2 батареи — всего около 50–60 км. Полную батарею поменяем в прокате за 20 000 VND.</li><li><b>Лучше избегать:</b> длинных крутых подъёмов — перевал Прен, перевал Мимоза, дорога на Лангбиан. Там с действующими правами лучше взять Air Blade 125cc.</li></ul><p>Перед выдачей прочитайте короткие <a href=\"{RULES}\">правила аренды электроскутера</a>.</p>"),
  ("Что нужно для аренды в Van Phu", "<ul><li><b>Иностранным гостям:</b> оригинал паспорта. <b>Гостям из Вьетнама:</b> CCCD.</li><li>Без денежного залога. 150 000 VND в сутки за любой байк, цена фиксированная.</li><li>Короткая тестовая поездка и общее видео состояния байка.</li><li>Шлем и держатель для телефона в комплекте; открываемся каждый день в 4:30 утра.</li></ul><p>Подробнее: <a href=\"{DOCS}\">что нужно для аренды байка в Далате</a>.</p>"),
 ],
 "faq_h": "Частые вопросы",
 "faq": [
  ("Нужны ли права на электроскутер во Вьетнаме?", "Для электромопеда — с максимальной скоростью до 50 км/ч и мотором до 4 кВт — права не нужны. Наши электроскутеры именно такие. Водителю должно быть не меньше 16 лет."),
  ("Можно ли взять бензиновый скутер в Далате без прав?", "Вьетнамский закон требует действующие права для бензиновых скутеров вроде Honda Vision и Air Blade, поэтому в Van Phu мы выдаём их только водителям с действующими правами. Без прав берите электроскутер."),
  ("Действуют ли мои права из дома во Вьетнаме?", "Считаются только права, действующие по вьетнамскому закону. Правила зависят от страны, которая выдала права, поэтому проверьте это до поездки. Если не уверены — арендуйте электроскутер."),
  ("Хватит ли электроскутера, чтобы посмотреть Далат?", "Для города и мест рядом — да. Одной батареи хватает примерно на 25–30 км, у каждого скутера 2 батареи (всего около 50–60 км), замена батареи в прокате — 20 000 VND. Для длинных крутых перевалов лучше бензиновый 125cc."),
  ("Электроскутер дешевле?", "Нет — любой байк стоит 150 000 VND в сутки, шлем и держатель для телефона включены."),
 ],
 "more_h": "Читайте также",
 "more": [("{EV}", "Аренда электроскутера в Далате"), ("{DOCS}", "Что нужно для аренды байка в Далате"), ("{RULES}", "Правила аренды электроскутера"), ("{HOME}", "Аренда байка в Далате — байки и цены")],
}

T["zh"] = {
 "title": "在越南租摩托车需要驾照吗？汽油车与电动车 | Van Phu",
 "desc": "在越南骑汽油踏板车需要越南法律认可的有效摩托车驾照；属于轻便摩托车（最高时速50公里以内）的电动车不需要驾照。在大叻租车时的具体说明。",
 "h1": "在越南租摩托车需要驾照吗？",
 "crumb": "越南骑摩托车的驾照要求",
 "lead": "简单回答：<b>汽油踏板车需要</b>越南法律认可的有效摩托车驾照；<b>属于轻便摩托车的电动车不需要</b>——我们的电动车最高时速在50公里以内，无需驾照即可骑行。下面说明在大叻租车时这意味着什么。",
 "short_h": "快速回答",
 "short": [
  ("Honda Vision 110cc、Honda Air Blade 125cc（汽油车）", "需要在越南有效的摩托车驾照（A1类或以上）"),
  ("电动车（轻便摩托车：最高时速50公里以内，电机不超过4千瓦）", "不需要驾照"),
  ("骑电动轻便摩托车的最低年龄", "16岁"),
  ("头盔", "驾驶人和乘客必须佩戴——免费提供"),
  ("租车时店里保管什么", "护照或身份证——不收现金押金"),
 ],
 "secs": [
  ("为什么电动车不需要驾照", "<p>越南《道路交通秩序与安全法》（2024年第36/2024/QH15号，2025年1月1日起施行）规定，驾驶机动车必须持有相应驾照，<b>但轻便摩托车除外</b>。轻便摩托车（<i>xe gắn máy</i>）指设计最高时速不超过50公里的两轮车；电动车型的电机功率不超过4千瓦。</p><p>我们的电动车属于这一类，所以在越南骑行不需要驾照。其他规定照常适用：必须戴头盔，骑车不喝酒、不喝啤酒，严格遵守越南交通法规。</p>"),
  ("汽油踏板车需要有效驾照", "<p>Honda Vision 110cc 和 Honda Air Blade 125cc 是排量超过50cc的摩托车，骑行需要越南法律认可的有效摩托车驾照，A1类适用于125cc以内的摩托车。</p><p>如果您从国外来旅行，请在出发前确认您的驾照在越南是否有效。不确定的话，选电动车最简单：价格一样，也不需要驾照。</p>"),
  ("没有驾照：电动车在大叻能去哪里", "<ul><li><b>适合：</b>市中心、春香湖、咖啡馆、夜市和城市附近的景点。</li><li><b>电池：</b>一块电池大约可骑25–30公里，每辆车配2块电池，合计约50–60公里。可到店更换满电电池，每次20,000 VND。</li><li><b>尽量避开：</b>长而陡的坡道，如Prenn山口、Mimosa山口和上朗璧安山的路。持有效驾照的骑手跑这些路线建议选Air Blade 125cc。</li></ul><p>取车前请先看看简短的<a href=\"{RULES}\">电动车租赁规则</a>。</p>"),
  ("在Van Phu租车需要什么", "<ul><li><b>外国游客：</b>护照原件。<b>越南客人：</b>CCCD身份证。</li><li>不收现金押金。所有车型每天固定150,000 VND。</li><li>取车前短暂试骑，并一起拍摄车况视频。</li><li>附送头盔和手机支架；每天凌晨4:30开门。</li></ul><p>详情请看：<a href=\"{DOCS}\">在大叻租摩托车需要什么</a>。</p>"),
 ],
 "faq_h": "常见问题",
 "faq": [
  ("在越南骑电动车需要驾照吗？", "属于轻便摩托车的电动车（最高时速50公里以内、电机不超过4千瓦）不需要驾照。我们的电动车属于这一类。骑行者须年满16岁。"),
  ("在大叻没有驾照可以租汽油踏板车吗？", "越南法律规定骑Honda Vision、Air Blade等汽油踏板车须持有效驾照，所以Van Phu只把汽油车租给持有效驾照的骑手。没有驾照请选电动车。"),
  ("我在本国的驾照在越南有效吗？", "只有越南法律认可的有效驾照才算数。具体规定取决于签发驾照的国家，请在出行前确认。不确定的话，租电动车即可。"),
  ("骑电动车够游览大叻吗？", "市区和附近景点完全够用。一块电池约25–30公里，每辆车配2块电池（合计约50–60公里），到店换电池20,000 VND。长而陡的山口建议骑125cc汽油车。"),
  ("电动车更便宜吗？", "不是——所有车型都是每天150,000 VND，含头盔和手机支架。"),
 ],
 "more_h": "延伸阅读",
 "more": [("{EV}", "大叻电动车租赁"), ("{DOCS}", "在大叻租摩托车需要什么"), ("{RULES}", "电动车租赁规则"), ("{HOME}", "大叻摩托车租赁——车型与价格")],
}

T["ko"] = {
 "title": "베트남에서 오토바이 렌트, 면허가 필요할까? | Van Phu",
 "desc": "베트남에서 가솔린 스쿠터는 베트남 법상 유효한 오토바이 면허가 필요하고, 모페드 등급(최고 50 km/h) 전기 스쿠터는 면허가 필요 없습니다. 달랏에서 렌트할 때의 의미를 정리했습니다.",
 "h1": "베트남에서 오토바이 렌트, 면허가 필요할까?",
 "crumb": "베트남 오토바이 면허",
 "lead": "짧게 답하면: <b>가솔린 스쿠터는 필요합니다</b> — 베트남 법상 유효한 오토바이 면허가 있어야 합니다. <b>모페드 등급 전기 스쿠터는 필요 없습니다</b> — 저희 전기 스쿠터(최고 속도 50 km/h 이하)는 면허 없이 탈 수 있습니다. 달랏에서 렌트할 때 무엇을 뜻하는지 알려 드릴게요.",
 "short_h": "빠른 답변",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (가솔린)", "면허 필요 — 베트남에서 유효한 오토바이 면허(A1 등급 이상)"),
  ("전기 스쿠터 (모페드: 최고 50 km/h, 모터 4 kW 이하)", "면허 불필요"),
  ("전기 모페드 최소 연령", "16세"),
  ("헬멧", "운전자와 동승자 모두 의무 — 무료 제공"),
  ("가게에 맡기는 것", "여권 또는 신분증 — 현금 보증금 없음"),
 ],
 "secs": [
  ("전기 스쿠터에 면허가 필요 없는 이유", "<p>베트남 도로교통질서·안전법 2024(제36/2024/QH15호, 2025년 1월 1일 시행)은 모든 차량 운전에 면허를 요구하지만 <b>모페드는 예외</b>입니다. 모페드(<i>xe gắn máy</i>)는 설계 최고 속도가 50 km/h 이하인 이륜차이며, 전기 모델은 모터 출력이 4 kW 이하입니다.</p><p>저희 전기 스쿠터는 이 모페드 등급이라 베트남에서 면허 없이 탈 수 있습니다. 나머지 규칙은 그대로입니다: 헬멧 착용, 음주 운전 금지, 베트남 교통법 철저히 준수.</p>"),
  ("가솔린 스쿠터는 유효한 면허가 필요합니다", "<p>Honda Vision 110cc와 Honda Air Blade 125cc는 50cc를 넘는 오토바이입니다. 타려면 베트남 법상 유효한 오토바이 면허가 필요하며, A1 등급이 125cc 이하를 포함합니다.</p><p>해외에서 오신다면 여행 전에 본인 면허가 베트남에서 유효한지 꼭 확인하세요. 잘 모르겠다면 전기 스쿠터가 간단합니다: 가격은 같고 면허는 필요 없습니다.</p>"),
  ("면허가 없다면: 달랏에서 전기 스쿠터로 갈 수 있는 곳", "<ul><li><b>추천:</b> 시내 중심, 쑤언흐엉 호수, 카페, 야시장, 시내 근교 명소.</li><li><b>배터리:</b> 배터리 1개로 약 25–30 km, 스쿠터마다 배터리 2개 — 합계 약 50–60 km. 가게에서 완충 배터리로 교체 시 20,000 VND.</li><li><b>피하세요:</b> 프렌 고개, 미모사 고개, 랑비앙 오르막처럼 길고 가파른 오르막. 유효한 면허가 있다면 이런 코스는 Air Blade 125cc를 추천합니다.</li></ul><p>픽업 전에 짧은 <a href=\"{RULES}\">전기 스쿠터 렌트 규칙</a>을 읽어 주세요.</p>"),
  ("Van Phu에서 렌트할 때 필요한 것", "<ul><li><b>외국인 손님:</b> 여권 원본. <b>베트남 손님:</b> CCCD.</li><li>현금 보증금 없음. 모든 바이크 하루 150,000 VND 고정.</li><li>짧은 시승과 함께 찍는 바이크 상태 영상.</li><li>헬멧과 휴대폰 거치대 포함; 매일 새벽 4:30에 문을 엽니다.</li></ul><p>자세히 보기: <a href=\"{DOCS}\">달랏 오토바이 렌트에 필요한 것</a>.</p>"),
 ],
 "faq_h": "자주 묻는 질문",
 "faq": [
  ("베트남에서 전기 스쿠터도 면허가 필요한가요?", "최고 속도 50 km/h 이하, 모터 4 kW 이하인 전기 모페드는 면허가 필요 없습니다. 저희 전기 스쿠터가 이 등급입니다. 만 16세 이상이어야 합니다."),
  ("면허 없이 달랏에서 가솔린 스쿠터를 빌릴 수 있나요?", "베트남 법은 Honda Vision, Air Blade 같은 가솔린 스쿠터에 유효한 면허를 요구하므로, Van Phu는 유효한 면허가 있는 분께만 가솔린 스쿠터를 빌려 드립니다. 면허가 없다면 전기 스쿠터를 선택하세요."),
  ("한국 면허가 베트남에서 유효한가요?", "베트남 법상 유효한 면허만 인정됩니다. 규정은 면허를 발급한 나라에 따라 다르니 여행 전에 확인하세요. 확실하지 않다면 전기 스쿠터를 빌리시면 됩니다."),
  ("전기 스쿠터로 달랏 여행이 충분한가요?", "시내와 근교라면 충분합니다. 배터리 1개로 약 25–30 km, 스쿠터마다 배터리 2개(합계 약 50–60 km), 가게에서 배터리 교체는 20,000 VND입니다. 길고 가파른 고개는 125cc 가솔린 스쿠터가 낫습니다."),
  ("전기 스쿠터가 더 저렴한가요?", "아니요 — 모든 바이크가 하루 150,000 VND이며 헬멧과 휴대폰 거치대가 포함됩니다."),
 ],
 "more_h": "함께 읽기",
 "more": [("{EV}", "달랏 전기 스쿠터 렌트"), ("{DOCS}", "달랏 오토바이 렌트에 필요한 것"), ("{RULES}", "전기 스쿠터 렌트 규칙"), ("{HOME}", "달랏 오토바이 렌트 — 바이크와 가격")],
}

T["ja"] = {
 "title": "ベトナムでバイクを借りるのに免許は必要？ガソリン車と電動 | Van Phu",
 "desc": "ベトナムでガソリンスクーターに乗るにはベトナムの法律で有効なバイク免許が必要。モペッド区分（最高時速50km以下）の電動スクーターは免許不要。ダラットでレンタルする場合を解説。",
 "h1": "ベトナムでバイクを借りるのに免許は必要？",
 "crumb": "ベトナムのバイク免許",
 "lead": "結論から言うと、<b>ガソリンスクーターは必要</b>です。ベトナムの法律で有効なバイク免許が要ります。<b>モペッド区分の電動スクーターは不要</b>です。当店の電動スクーター（最高時速50km以下）は免許なしで乗れます。ダラットでレンタルするときのポイントをまとめました。",
 "short_h": "すぐ分かる答え",
 "short": [
  ("Honda Vision 110cc・Honda Air Blade 125cc（ガソリン）", "免許が必要 — ベトナムで有効なバイク免許（A1区分以上）"),
  ("電動スクーター（モペッド：最高時速50km以下、モーター4kW以下）", "免許不要"),
  ("電動モペッドに乗れる年齢", "16歳以上"),
  ("ヘルメット", "運転者・同乗者ともに着用義務 — 無料で貸し出し"),
  ("お店で預かるもの", "パスポートまたはIDカード — 現金のデポジットなし"),
 ],
 "secs": [
  ("電動スクーターに免許が要らない理由", "<p>ベトナムの道路交通秩序・安全法2024（第36/2024/QH15号、2025年1月1日施行）は、車両の運転に免許を求めていますが、<b>モペッドは例外</b>です。モペッド（<i>xe gắn máy</i>）は設計上の最高速度が時速50km以下の二輪車で、電動モデルはモーター出力4kW以下です。</p><p>当店の電動スクーターはこのモペッド区分なので、ベトナムでは免許なしで運転できます。そのほかのルールは同じです。ヘルメットを着用し、飲酒運転はせず、ベトナムの交通法規を必ず守ってください。</p>"),
  ("ガソリンスクーターには有効な免許が必要", "<p>Honda Vision 110ccとHonda Air Blade 125ccは50ccを超えるバイクです。運転にはベトナムの法律で有効なバイク免許が必要で、A1区分が125ccまでをカバーします。</p><p>海外から旅行される方は、出発前にご自身の免許がベトナムで有効か確認してください。分からない場合は電動スクーターが手軽です。料金は同じで、免許も要りません。</p>"),
  ("免許がない場合：ダラットで電動スクーターで行ける場所", "<ul><li><b>向いている場所：</b>市内中心部、スアンフーン湖、カフェ、ナイトマーケット、市内近郊の観光地。</li><li><b>バッテリー：</b>バッテリー1個で約25〜30km、各スクーターに2個付き — 合計約50〜60km。お店で満充電のバッテリーに交換すると1回20,000 VND。</li><li><b>避けたい道：</b>プレン峠、ミモザ峠、ランビアン山への上り道など長く急な坂。有効な免許をお持ちの方はAir Blade 125ccがおすすめです。</li></ul><p>受け取り前に、短い<a href=\"{RULES}\">電動スクーターのレンタルルール</a>をお読みください。</p>"),
  ("Van Phuでレンタルするときに必要なもの", "<ul><li><b>外国人のお客様：</b>パスポートの原本。<b>ベトナムのお客様：</b>CCCD。</li><li>現金のデポジットなし。全車種1日150,000 VNDの固定料金。</li><li>短い試乗と、車両の状態を一緒に撮る動画。</li><li>ヘルメットとスマホホルダー付き。毎日朝4:30から営業。</li></ul><p>詳しくは：<a href=\"{DOCS}\">ダラットでバイクを借りるのに必要なもの</a>。</p>"),
 ],
 "faq_h": "よくある質問",
 "faq": [
  ("ベトナムで電動スクーターに免許は必要ですか？", "最高時速50km以下・モーター4kW以下の電動モペッドなら免許は不要です。当店の電動スクーターはこの区分です。16歳以上の方が対象です。"),
  ("免許なしでダラットでガソリンスクーターを借りられますか？", "ベトナムの法律ではHonda VisionやAir Bladeなどのガソリンスクーターに有効な免許が必要なため、Van Phuでは有効な免許をお持ちの方にのみお貸ししています。免許がない場合は電動スクーターをお選びください。"),
  ("日本の免許はベトナムで有効ですか？", "ベトナムの法律で有効な免許のみが認められます。条件は免許を発行した国によって異なるため、出発前にご確認ください。不安な場合は電動スクーターを借りるのがおすすめです。"),
  ("電動スクーターでダラット観光は足りますか？", "市内と近郊なら十分です。バッテリー1個で約25〜30km、各スクーターに2個付き（合計約50〜60km）、お店でのバッテリー交換は20,000 VNDです。長く急な峠は125ccのガソリンスクーターが向いています。"),
  ("電動スクーターのほうが安いですか？", "いいえ。全車種1日150,000 VNDで、ヘルメットとスマホホルダーが含まれます。"),
 ],
 "more_h": "あわせて読みたい",
 "more": [("{EV}", "ダラットの電動スクーターレンタル"), ("{DOCS}", "ダラットでバイクを借りるのに必要なもの"), ("{RULES}", "電動スクーターのレンタルルール"), ("{HOME}", "ダラットのバイクレンタル — 車種と料金")],
}

T["th"] = {
 "title": "เช่ามอเตอร์ไซค์ในเวียดนามต้องมีใบขับขี่ไหม? | Van Phu",
 "desc": "ขี่สกู๊ตเตอร์น้ำมันในเวียดนามต้องมีใบขับขี่มอเตอร์ไซค์ที่ใช้ได้ตามกฎหมายเวียดนาม ส่วนสกู๊ตเตอร์ไฟฟ้าประเภทโมเปด (ไม่เกิน 50 กม./ชม.) ไม่ต้องใช้ใบขับขี่ สรุปสำหรับการเช่าที่ดาลัด",
 "h1": "เช่ามอเตอร์ไซค์ในเวียดนามต้องมีใบขับขี่ไหม?",
 "crumb": "ใบขับขี่มอเตอร์ไซค์ในเวียดนาม",
 "lead": "ตอบสั้น ๆ: <b>สกู๊ตเตอร์น้ำมัน ต้องมี</b> ใบขับขี่มอเตอร์ไซค์ที่ใช้ได้ตามกฎหมายเวียดนาม <b>สกู๊ตเตอร์ไฟฟ้าประเภทโมเปด ไม่ต้องมี</b> — สกู๊ตเตอร์ไฟฟ้าของเรา (ความเร็วสูงสุดไม่เกิน 50 กม./ชม.) ขี่ได้โดยไม่ต้องใช้ใบขับขี่ มาดูว่าเรื่องนี้หมายถึงอะไรเมื่อเช่ารถที่ดาลัด",
 "short_h": "คำตอบแบบเร็ว",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (น้ำมัน)", "ต้องมีใบขับขี่มอเตอร์ไซค์ที่ใช้ได้ในเวียดนาม (ประเภท A1 ขึ้นไป)"),
  ("สกู๊ตเตอร์ไฟฟ้า (โมเปด: ไม่เกิน 50 กม./ชม., มอเตอร์ไม่เกิน 4 kW)", "ไม่ต้องใช้ใบขับขี่"),
  ("อายุขั้นต่ำสำหรับโมเปดไฟฟ้า", "16 ปี"),
  ("หมวกกันน็อก", "บังคับทั้งคนขี่และคนซ้อน — ให้ฟรี"),
  ("สิ่งที่ร้านเก็บไว้", "พาสปอร์ตหรือบัตรประชาชน — ไม่มีมัดจำเงินสด"),
 ],
 "secs": [
  ("ทำไมสกู๊ตเตอร์ไฟฟ้าไม่ต้องใช้ใบขับขี่", "<p>กฎหมายว่าด้วยระเบียบและความปลอดภัยการจราจรทางถนนของเวียดนาม ปี 2024 (เลขที่ 36/2024/QH15 มีผลตั้งแต่ 1 มกราคม 2025) กำหนดให้ผู้ขับขี่ยานพาหนะต้องมีใบขับขี่ <b>ยกเว้นผู้ขับขี่โมเปด</b> โมเปด (<i>xe gắn máy</i>) คือรถสองล้อที่ออกแบบให้มีความเร็วสูงสุดไม่เกิน 50 กม./ชม. สำหรับรุ่นไฟฟ้า มอเตอร์ต้องไม่เกิน 4 kW</p><p>สกู๊ตเตอร์ไฟฟ้าของเราอยู่ในประเภทโมเปดนี้ จึงขี่ในเวียดนามได้โดยไม่ต้องใช้ใบขับขี่ กฎอื่นยังเหมือนเดิม: สวมหมวกกันน็อก ห้ามดื่มแอลกอฮอล์หรือเบียร์ขณะขี่ และปฏิบัติตามกฎจราจรเวียดนามอย่างเคร่งครัด</p>"),
  ("สกู๊ตเตอร์น้ำมันต้องมีใบขับขี่ที่ใช้ได้", "<p>Honda Vision 110cc และ Honda Air Blade 125cc เป็นมอเตอร์ไซค์ที่เกิน 50cc ต้องมีใบขับขี่มอเตอร์ไซค์ที่ใช้ได้ตามกฎหมายเวียดนาม โดยประเภท A1 ครอบคลุมรถไม่เกิน 125cc</p><p>ถ้ามาจากต่างประเทศ ควรเช็กก่อนเดินทางว่าใบขับขี่ของคุณใช้ได้ในเวียดนามหรือไม่ ถ้าไม่แน่ใจ เลือกสกู๊ตเตอร์ไฟฟ้าง่ายที่สุด: ราคาเท่ากันและไม่ต้องใช้ใบขับขี่</p>"),
  ("ไม่มีใบขับขี่: สกู๊ตเตอร์ไฟฟ้าไปไหนได้บ้างในดาลัด", "<ul><li><b>เหมาะกับ:</b> ใจกลางเมือง ทะเลสาบซวนเฮือง คาเฟ่ ตลาดกลางคืน และที่เที่ยวใกล้เมือง</li><li><b>แบตเตอรี่:</b> แบตก้อนเดียววิ่งได้ประมาณ 25–30 กม. สกู๊ตเตอร์แต่ละคันมีแบต 2 ก้อน — รวมประมาณ 50–60 กม. เปลี่ยนแบตเต็มที่ร้าน 20,000 VND ต่อครั้ง</li><li><b>ควรเลี่ยง:</b> ทางขึ้นเขาชันและยาว เช่น ช่องเขาเปรน ช่องเขามิโมซา และทางขึ้นลางเบียง ถ้ามีใบขับขี่ที่ใช้ได้ เส้นทางเหล่านี้แนะนำ Air Blade 125cc</li><li>เวียดนามขับรถชิดขวา (ไทยขับชิดซ้าย) ช่วงแรกขี่ช้า ๆ ก่อนจนคุ้นเคย</li></ul><p>อ่าน<a href=\"{RULES}\">กฎการเช่าสกู๊ตเตอร์ไฟฟ้า</a>สั้น ๆ ก่อนรับรถ</p>"),
  ("เช่ารถที่ Van Phu ต้องใช้อะไรบ้าง", "<ul><li><b>ลูกค้าต่างชาติ:</b> พาสปอร์ตตัวจริง <b>ลูกค้าชาวเวียดนาม:</b> CCCD</li><li>ไม่มีมัดจำเงินสด ทุกคัน 150,000 VND ต่อวัน ราคาคงที่</li><li>ลองขี่สั้น ๆ และถ่ายวิดีโอสภาพรถด้วยกันก่อนรับรถ</li><li>มีหมวกกันน็อกและที่ยึดโทรศัพท์ให้ ร้านเปิดทุกวันตั้งแต่ตี 4:30</li></ul><p>รายละเอียดเพิ่มเติม: <a href=\"{DOCS}\">เช่ามอเตอร์ไซค์ที่ดาลัดต้องใช้อะไร</a></p>"),
 ],
 "faq_h": "คำถามที่พบบ่อย",
 "faq": [
  ("ขี่สกู๊ตเตอร์ไฟฟ้าในเวียดนามต้องมีใบขับขี่ไหม?", "โมเปดไฟฟ้าที่ความเร็วสูงสุดไม่เกิน 50 กม./ชม. และมอเตอร์ไม่เกิน 4 kW ไม่ต้องใช้ใบขับขี่ สกู๊ตเตอร์ไฟฟ้าของเราอยู่ในประเภทนี้ ผู้ขี่ต้องอายุ 16 ปีขึ้นไป"),
  ("ไม่มีใบขับขี่ เช่าสกู๊ตเตอร์น้ำมันที่ดาลัดได้ไหม?", "กฎหมายเวียดนามกำหนดให้ต้องมีใบขับขี่ที่ใช้ได้สำหรับสกู๊ตเตอร์น้ำมันอย่าง Honda Vision และ Air Blade ที่ Van Phu เราจึงให้เช่าเฉพาะผู้ที่มีใบขับขี่ที่ใช้ได้ ถ้าไม่มี เลือกสกู๊ตเตอร์ไฟฟ้าแทน"),
  ("ใบขับขี่ไทยใช้ในเวียดนามได้ไหม?", "นับเฉพาะใบขับขี่ที่ใช้ได้ตามกฎหมายเวียดนาม เงื่อนไขขึ้นกับประเทศที่ออกใบขับขี่ จึงควรเช็กก่อนเดินทาง ถ้าไม่แน่ใจ เช่าสกู๊ตเตอร์ไฟฟ้าได้เลย"),
  ("สกู๊ตเตอร์ไฟฟ้าพอสำหรับเที่ยวดาลัดไหม?", "ในเมืองและที่เที่ยวใกล้ ๆ พอแน่นอน แบตก้อนเดียวประมาณ 25–30 กม. แต่ละคันมีแบต 2 ก้อน (รวมประมาณ 50–60 กม.) เปลี่ยนแบตที่ร้าน 20,000 VND ส่วนช่องเขายาวและชัน สกู๊ตเตอร์น้ำมัน 125cc เหมาะกว่า"),
  ("สกู๊ตเตอร์ไฟฟ้าถูกกว่าไหม?", "ไม่ — ทุกคัน 150,000 VND ต่อวัน รวมหมวกกันน็อกและที่ยึดโทรศัพท์"),
 ],
 "more_h": "อ่านต่อ",
 "more": [("{EV}", "เช่าสกู๊ตเตอร์ไฟฟ้าที่ดาลัด"), ("{DOCS}", "เช่ามอเตอร์ไซค์ที่ดาลัดต้องใช้อะไร"), ("{RULES}", "กฎการเช่าสกู๊ตเตอร์ไฟฟ้า"), ("{HOME}", "เช่ามอเตอร์ไซค์ดาลัด — รุ่นรถและราคา")],
}

T["id"] = {
 "title": "Perlu SIM untuk Sewa Motor di Vietnam? | Van Phu",
 "desc": "Motor matic bensin di Vietnam butuh SIM motor yang berlaku menurut hukum Vietnam. Skuter listrik kelas moped (maks. 50 km/jam) tidak perlu SIM. Penjelasannya untuk sewa di Da Lat.",
 "h1": "Perlu SIM untuk Sewa Motor di Vietnam?",
 "crumb": "SIM motor di Vietnam",
 "lead": "Jawaban singkat: <b>motor matic bensin perlu</b> SIM motor yang berlaku menurut hukum Vietnam. <b>Skuter listrik kelas moped tidak perlu</b> — skuter listrik kami (kecepatan maksimal hingga 50 km/jam) boleh dikendarai tanpa SIM. Berikut artinya saat kamu sewa motor di Da Lat.",
 "short_h": "Jawaban cepat",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (bensin)", "Perlu SIM motor yang berlaku di Vietnam (kategori A1 ke atas)"),
  ("Skuter listrik (moped: maks. 50 km/jam, motor hingga 4 kW)", "Tidak perlu SIM"),
  ("Usia minimal untuk moped listrik", "16 tahun"),
  ("Helm", "Wajib untuk pengendara dan penumpang — gratis dari kami"),
  ("Yang kami simpan di toko", "Paspor atau KTP — tanpa deposit uang tunai"),
 ],
 "secs": [
  ("Kenapa skuter listrik tidak perlu SIM", "<p>Undang-Undang Ketertiban dan Keselamatan Lalu Lintas Jalan Vietnam tahun 2024 (No. 36/2024/QH15, berlaku sejak 1 Januari 2025) mewajibkan SIM untuk semua kendaraan bermotor, <b>kecuali moped</b>. Moped (<i>xe gắn máy</i>) adalah kendaraan roda dua dengan kecepatan rancangan maksimal 50 km/jam; untuk model listrik, motornya maksimal 4 kW.</p><p>Skuter listrik kami termasuk kelas moped ini, jadi boleh dikendarai di Vietnam tanpa SIM. Aturan lain tetap berlaku: pakai helm, jangan minum alkohol atau bir saat berkendara, dan patuhi hukum lalu lintas Vietnam dengan ketat.</p>"),
  ("Motor bensin perlu SIM yang berlaku", "<p>Honda Vision 110cc dan Honda Air Blade 125cc adalah sepeda motor di atas 50cc. Untuk mengendarainya kamu perlu SIM motor yang berlaku menurut hukum Vietnam — kategori A1 mencakup motor hingga 125cc.</p><p>Kalau datang dari luar negeri, cek sebelum berangkat apakah SIM kamu berlaku di Vietnam. Belum yakin? Skuter listrik pilihan paling mudah: harganya sama dan tidak perlu SIM.</p>"),
  ("Tanpa SIM: skuter listrik bisa ke mana di Da Lat", "<ul><li><b>Cocok untuk:</b> pusat kota, Danau Xuan Huong, kafe, pasar malam, dan tempat wisata dekat kota.</li><li><b>Baterai:</b> satu baterai cukup untuk sekitar 25–30 km, tiap skuter dapat 2 baterai — total sekitar 50–60 km. Tukar baterai penuh di toko 20.000 VND sekali tukar.</li><li><b>Hindari:</b> tanjakan panjang dan curam seperti Prenn Pass, Mimosa Pass dan jalan naik ke Lang Biang. Kalau punya SIM yang berlaku, pakai Air Blade 125cc untuk rute ini.</li><li>Di Vietnam kendaraan berjalan di sisi kanan (di Indonesia di kiri) — pelan-pelan dulu sampai terbiasa.</li></ul><p>Baca singkat <a href=\"{RULES}\">aturan sewa skuter listrik</a> sebelum ambil motor.</p>"),
  ("Yang perlu dibawa untuk sewa di Van Phu", "<ul><li><b>Tamu asing:</b> paspor asli. <b>Tamu Vietnam:</b> CCCD.</li><li>Tanpa deposit uang tunai. Semua motor 150.000 VND per hari, harga tetap.</li><li>Coba jalan sebentar dan rekam video kondisi motor bersama-sama.</li><li>Helm dan holder HP sudah termasuk; toko buka setiap hari mulai pukul 4.30 pagi.</li></ul><p>Selengkapnya: <a href=\"{DOCS}\">apa saja yang dibutuhkan untuk sewa motor di Da Lat</a>.</p>"),
 ],
 "faq_h": "Pertanyaan yang sering diajukan",
 "faq": [
  ("Apakah skuter listrik di Vietnam perlu SIM?", "Moped listrik dengan kecepatan maksimal hingga 50 km/jam dan motor hingga 4 kW tidak perlu SIM. Skuter listrik kami termasuk kelas ini. Pengendara minimal berusia 16 tahun."),
  ("Bisa sewa motor bensin di Da Lat tanpa SIM?", "Hukum Vietnam mewajibkan SIM yang berlaku untuk motor bensin seperti Honda Vision dan Air Blade, jadi di Van Phu kami hanya menyewakannya kepada pengendara dengan SIM yang berlaku. Tanpa SIM, pilih skuter listrik."),
  ("Apakah SIM Indonesia berlaku di Vietnam?", "Hanya SIM yang berlaku menurut hukum Vietnam yang diterima. Aturannya tergantung negara penerbit SIM, jadi cek sebelum berangkat. Kalau tidak yakin, sewa skuter listrik saja."),
  ("Apakah skuter listrik cukup untuk keliling Da Lat?", "Untuk kota dan tempat wisata terdekat, cukup. Satu baterai sekitar 25–30 km, tiap skuter dapat 2 baterai (total sekitar 50–60 km), tukar baterai di toko 20.000 VND. Untuk tanjakan panjang dan curam, motor bensin 125cc lebih cocok."),
  ("Apakah skuter listrik lebih murah?", "Tidak — semua motor 150.000 VND per hari, sudah termasuk helm dan holder HP."),
 ],
 "more_h": "Baca juga",
 "more": [("{EV}", "Sewa skuter listrik di Da Lat"), ("{DOCS}", "Yang dibutuhkan untuk sewa motor di Da Lat"), ("{RULES}", "Aturan sewa skuter listrik"), ("{HOME}", "Sewa motor Da Lat — motor dan harga")],
}

T["ms"] = {
 "title": "Perlukah Lesen untuk Sewa Motosikal di Vietnam? | Van Phu",
 "desc": "Skuter petrol di Vietnam memerlukan lesen motosikal yang sah mengikut undang-undang Vietnam. Skuter elektrik kelas moped (maks. 50 km/j) tidak memerlukan lesen. Maksudnya bila sewa di Da Lat.",
 "h1": "Perlukah Lesen untuk Sewa Motosikal di Vietnam?",
 "crumb": "Lesen motosikal di Vietnam",
 "lead": "Jawapan ringkas: <b>skuter petrol, perlu</b> lesen motosikal yang sah mengikut undang-undang Vietnam. <b>Skuter elektrik kelas moped, tidak perlu</b> — skuter elektrik kami (kelajuan maksimum hingga 50 km/j) boleh ditunggang tanpa lesen. Ini maksudnya apabila anda menyewa di Da Lat.",
 "short_h": "Jawapan pantas",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (petrol)", "Perlu lesen motosikal yang sah di Vietnam (kategori A1 ke atas)"),
  ("Skuter elektrik (moped: maks. 50 km/j, motor hingga 4 kW)", "Tidak perlu lesen"),
  ("Umur minimum untuk moped elektrik", "16 tahun"),
  ("Topi keledar", "Wajib untuk penunggang dan pembonceng — percuma"),
  ("Apa yang kami simpan di kedai", "Pasport atau kad pengenalan — tiada deposit tunai"),
 ],
 "secs": [
  ("Kenapa skuter elektrik tidak perlu lesen", "<p>Undang-undang Ketenteraman dan Keselamatan Lalu Lintas Jalan Raya Vietnam 2024 (No. 36/2024/QH15, berkuat kuasa sejak 1 Januari 2025) mewajibkan lesen memandu untuk semua kenderaan bermotor, <b>kecuali moped</b>. Moped (<i>xe gắn máy</i>) ialah kenderaan dua roda dengan kelajuan reka bentuk maksimum 50 km/j; bagi model elektrik, motornya tidak melebihi 4 kW.</p><p>Skuter elektrik kami tergolong dalam kelas moped ini, jadi anda boleh menunggangnya di Vietnam tanpa lesen. Peraturan lain kekal: pakai topi keledar, jangan minum alkohol atau bir semasa menunggang, dan patuhi undang-undang lalu lintas Vietnam dengan ketat.</p>"),
  ("Skuter petrol perlu lesen yang sah", "<p>Honda Vision 110cc dan Honda Air Blade 125cc ialah motosikal melebihi 50cc. Untuk menunggangnya anda perlu lesen motosikal yang sah mengikut undang-undang Vietnam — kategori A1 meliputi motosikal hingga 125cc.</p><p>Jika anda datang dari luar negara, semak sebelum perjalanan sama ada lesen anda sah di Vietnam. Tidak pasti? Skuter elektrik pilihan paling mudah: harga sama dan tidak perlu lesen.</p>"),
  ("Tiada lesen: ke mana skuter elektrik boleh pergi di Da Lat", "<ul><li><b>Sesuai untuk:</b> pusat bandar, Tasik Xuan Huong, kafe, pasar malam dan tempat menarik berhampiran bandar.</li><li><b>Bateri:</b> satu bateri tahan kira-kira 25–30 km, setiap skuter ada 2 bateri — jumlah kira-kira 50–60 km. Tukar bateri penuh di kedai 20,000 VND setiap kali.</li><li><b>Elakkan:</b> pendakian panjang dan curam seperti Prenn Pass, Mimosa Pass dan jalan naik ke Lang Biang. Jika ada lesen yang sah, pilih Air Blade 125cc untuk laluan ini.</li><li>Vietnam memandu di sebelah kanan jalan (Malaysia di kiri) — tunggang perlahan dahulu sehingga biasa.</li></ul><p>Baca ringkas <a href=\"{RULES}\">peraturan sewa skuter elektrik</a> sebelum ambil skuter.</p>"),
  ("Apa yang diperlukan untuk sewa di Van Phu", "<ul><li><b>Tetamu asing:</b> pasport asal. <b>Tetamu Vietnam:</b> CCCD.</li><li>Tiada deposit tunai. Semua motosikal 150,000 VND sehari, harga tetap.</li><li>Cubaan tunggang sebentar dan video keadaan motosikal yang kita rakam bersama.</li><li>Topi keledar dan pemegang telefon disertakan; kedai dibuka setiap hari dari 4:30 pagi.</li></ul><p>Butiran lanjut: <a href=\"{DOCS}\">apa yang diperlukan untuk sewa motosikal di Da Lat</a>.</p>"),
 ],
 "faq_h": "Soalan lazim",
 "faq": [
  ("Adakah skuter elektrik di Vietnam perlu lesen?", "Moped elektrik dengan kelajuan maksimum hingga 50 km/j dan motor hingga 4 kW tidak perlu lesen. Skuter elektrik kami tergolong dalam kelas ini. Penunggang mesti berumur sekurang-kurangnya 16 tahun."),
  ("Bolehkah saya sewa skuter petrol di Da Lat tanpa lesen?", "Undang-undang Vietnam mewajibkan lesen yang sah untuk skuter petrol seperti Honda Vision dan Air Blade, jadi di Van Phu kami hanya menyewakannya kepada penunggang yang ada lesen sah. Tanpa lesen, pilih skuter elektrik."),
  ("Adakah lesen Malaysia sah di Vietnam?", "Hanya lesen yang sah mengikut undang-undang Vietnam diterima. Syaratnya bergantung pada negara yang mengeluarkan lesen, jadi semak sebelum perjalanan. Jika tidak pasti, sewa skuter elektrik."),
  ("Cukupkah skuter elektrik untuk meneroka Da Lat?", "Untuk bandar dan tempat berhampiran, cukup. Satu bateri kira-kira 25–30 km, setiap skuter ada 2 bateri (jumlah kira-kira 50–60 km), tukar bateri di kedai 20,000 VND. Untuk laluan bukit yang panjang dan curam, skuter petrol 125cc lebih sesuai."),
  ("Adakah skuter elektrik lebih murah?", "Tidak — semua motosikal 150,000 VND sehari, termasuk topi keledar dan pemegang telefon."),
 ],
 "more_h": "Baca juga",
 "more": [("{EV}", "Sewa skuter elektrik di Da Lat"), ("{DOCS}", "Apa yang diperlukan untuk sewa motosikal di Da Lat"), ("{RULES}", "Peraturan sewa skuter elektrik"), ("{HOME}", "Sewa motosikal Da Lat — motosikal dan harga")],
}

T["de"] = {
 "title": "Führerschein nötig für einen Roller in Vietnam? | Van Phu",
 "desc": "Für Benzinroller brauchst du in Vietnam einen nach vietnamesischem Recht gültigen Motorradführerschein. Für E-Roller der Mopedklasse (bis 50 km/h) nicht. Was das in Da Lat heißt.",
 "h1": "Brauche ich einen Führerschein, um in Vietnam einen Roller zu mieten?",
 "crumb": "Führerschein in Vietnam",
 "lead": "Kurz gesagt: <b>für einen Benzinroller ja</b> — du brauchst einen Motorradführerschein, der nach vietnamesischem Recht gültig ist. <b>Für einen E-Roller der Mopedklasse nein</b> — unsere E-Roller (Höchstgeschwindigkeit bis 50 km/h) darfst du ohne Führerschein fahren. Hier liest du, was das bei der Miete in Da Lat bedeutet.",
 "short_h": "Die schnelle Antwort",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (Benzin)", "Führerschein nötig — ein in Vietnam gültiger Motorradführerschein (Klasse A1 oder höher)"),
  ("E-Roller (Moped: bis 50 km/h, Motor bis 4 kW)", "Kein Führerschein nötig"),
  ("Mindestalter für ein E-Moped", "16 Jahre"),
  ("Helm", "Pflicht für Fahrer und Beifahrer — gibt es kostenlos dazu"),
  ("Was wir im Laden behalten", "Deinen Reisepass oder Personalausweis — keine Barkaution"),
 ],
 "secs": [
  ("Warum du für den E-Roller keinen Führerschein brauchst", "<p>Vietnams Gesetz über Ordnung und Sicherheit im Straßenverkehr von 2024 (Nr. 36/2024/QH15, gültig seit 1. Januar 2025) verlangt für alle Kraftfahrzeuge einen Führerschein — <b>außer für Mopeds</b>. Ein Moped (<i>xe gắn máy</i>) ist ein Zweirad mit einer bauartbedingten Höchstgeschwindigkeit bis 50 km/h; bei Elektromodellen hat der Motor höchstens 4 kW.</p><p>Unsere E-Roller gehören zu dieser Mopedklasse, du darfst sie in Vietnam also ohne Führerschein fahren. Alles andere gilt weiter: Helm tragen, kein Alkohol oder Bier beim Fahren und die vietnamesischen Verkehrsregeln strikt einhalten.</p>"),
  ("Benzinroller brauchen einen gültigen Führerschein", "<p>Die Honda Vision 110cc und die Honda Air Blade 125cc sind Motorräder über 50 cm³. Dafür brauchst du einen Motorradführerschein, der nach vietnamesischem Recht gültig ist — Klasse A1 deckt Maschinen bis 125 cm³ ab.</p><p>Kommst du aus dem Ausland, prüfe vor der Reise, ob dein Führerschein in Vietnam gilt. Unsicher? Dann ist der E-Roller die einfache Wahl: gleicher Preis, kein Führerschein.</p>"),
  ("Ohne Führerschein: wohin du mit dem E-Roller in Da Lat kommst", "<ul><li><b>Ideal für:</b> das Zentrum, den Xuan-Huong-See, Cafés, den Nachtmarkt und Sehenswürdigkeiten nahe der Stadt.</li><li><b>Akku:</b> Ein Akku reicht für etwa 25–30 km, jeder Roller hat 2 Akkus — zusammen etwa 50–60 km. Im Laden tauschen wir für 20.000 VND gegen einen vollen Akku.</li><li><b>Besser meiden:</b> lange, steile Anstiege wie den Prenn-Pass, den Mimosa-Pass und die Straße hinauf zum Lang Biang. Mit gültigem Führerschein nimmst du dafür die Air Blade 125cc.</li></ul><p>Lies vor der Abholung kurz unsere <a href=\"{RULES}\">Regeln für die E-Roller-Miete</a>.</p>"),
  ("Was du für die Miete bei Van Phu brauchst", "<ul><li><b>Ausländische Gäste:</b> deinen Original-Reisepass. <b>Vietnamesische Gäste:</b> CCCD.</li><li>Keine Barkaution. 150.000 VND pro Tag für jedes Bike, fester Preis.</li><li>Eine kurze Probefahrt und ein gemeinsames Video vom Zustand des Bikes.</li><li>Helm und Handyhalter inklusive; wir öffnen jeden Tag um 4:30 Uhr.</li></ul><p>Mehr dazu: <a href=\"{DOCS}\">was du zum Rollermieten in Da Lat brauchst</a>.</p>"),
 ],
 "faq_h": "Häufige Fragen",
 "faq": [
  ("Brauche ich in Vietnam einen Führerschein für einen E-Roller?", "Für ein E-Moped mit Höchstgeschwindigkeit bis 50 km/h und Motor bis 4 kW nicht. Unsere E-Roller gehören zu dieser Klasse. Du musst mindestens 16 Jahre alt sein."),
  ("Kann ich in Da Lat ohne Führerschein einen Benzinroller mieten?", "Das vietnamesische Recht verlangt für Benzinroller wie die Honda Vision und die Air Blade einen gültigen Führerschein. Bei Van Phu vermieten wir sie deshalb nur an Fahrer mit gültigem Führerschein. Ohne Führerschein nimmst du den E-Roller."),
  ("Gilt mein deutscher Führerschein in Vietnam?", "Es zählt nur ein Führerschein, der nach vietnamesischem Recht gültig ist. Die Regeln hängen vom Ausstellungsland ab, prüfe das also vor der Reise. Bist du unsicher, miete einen E-Roller."),
  ("Reicht ein E-Roller, um Da Lat zu erkunden?", "Für die Stadt und die nahen Sehenswürdigkeiten ja. Ein Akku reicht für etwa 25–30 km, jeder Roller hat 2 Akkus (zusammen etwa 50–60 km), der Akkutausch im Laden kostet 20.000 VND. Für lange, steile Pässe ist ein 125cc-Benzinroller besser."),
  ("Ist der E-Roller günstiger?", "Nein — jedes Bike kostet 150.000 VND pro Tag, Helm und Handyhalter inklusive."),
 ],
 "more_h": "Weiterlesen",
 "more": [("{EV}", "E-Roller mieten in Da Lat"), ("{DOCS}", "Was du zum Rollermieten in Da Lat brauchst"), ("{RULES}", "Regeln für die E-Roller-Miete"), ("{HOME}", "Roller mieten in Da Lat — Bikes und Preise")],
}

T["fr"] = {
 "title": "Faut-il un permis pour louer un scooter au Vietnam ? | Van Phu",
 "desc": "Au Vietnam, un scooter essence exige un permis moto valable selon la loi vietnamienne. Un scooter électrique de catégorie cyclomoteur (jusqu'à 50 km/h) n'en demande pas. Ce que cela veut dire à Da Lat.",
 "h1": "Faut-il un permis pour louer un scooter au Vietnam ?",
 "crumb": "Permis moto au Vietnam",
 "lead": "En bref : <b>pour un scooter essence, oui</b> — il vous faut un permis moto valable selon la loi vietnamienne. <b>Pour un scooter électrique de catégorie cyclomoteur, non</b> — nos scooters électriques (vitesse maximale jusqu'à 50 km/h) se conduisent sans permis. Voici ce que cela signifie quand vous louez à Da Lat.",
 "short_h": "La réponse rapide",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (essence)", "Permis requis — un permis moto valable au Vietnam (catégorie A1 ou supérieure)"),
  ("Scooter électrique (cyclomoteur : jusqu'à 50 km/h, moteur jusqu'à 4 kW)", "Aucun permis requis"),
  ("Âge minimum pour un cyclomoteur électrique", "16 ans"),
  ("Casque", "Obligatoire pour le conducteur et le passager — fourni gratuitement"),
  ("Ce que nous gardons à la boutique", "Votre passeport ou carte d'identité — pas de caution en espèces"),
 ],
 "secs": [
  ("Pourquoi le scooter électrique se conduit sans permis", "<p>La loi vietnamienne de 2024 sur l'ordre et la sécurité de la circulation routière (n° 36/2024/QH15, en vigueur depuis le 1er janvier 2025) impose un permis pour tous les véhicules à moteur, <b>sauf les cyclomoteurs</b>. Un cyclomoteur (<i>xe gắn máy</i>) est un deux-roues dont la vitesse maximale par construction ne dépasse pas 50 km/h ; pour les modèles électriques, le moteur fait au plus 4 kW.</p><p>Nos scooters électriques entrent dans cette catégorie : vous pouvez donc les conduire au Vietnam sans permis. Le reste ne change pas : casque obligatoire, pas d'alcool ni de bière au guidon, et respect strict du code de la route vietnamien.</p>"),
  ("Les scooters essence demandent un permis valable", "<p>Le Honda Vision 110cc et le Honda Air Blade 125cc sont des motos de plus de 50 cm³. Pour les conduire, il faut un permis moto valable selon la loi vietnamienne — la catégorie A1 couvre les machines jusqu'à 125 cm³.</p><p>Si vous venez de l'étranger, vérifiez avant le départ que votre permis est valable au Vietnam. Un doute ? Le scooter électrique est le choix le plus simple : même prix, sans permis.</p>"),
  ("Sans permis : où aller en scooter électrique à Da Lat", "<ul><li><b>Idéal pour :</b> le centre-ville, le lac Xuan Huong, les cafés, le marché de nuit et les sites proches de la ville.</li><li><b>Batterie :</b> une batterie tient environ 25–30 km et chaque scooter en a 2 — soit environ 50–60 km au total. Échange contre une batterie pleine à la boutique : 20 000 VND.</li><li><b>À éviter :</b> les longues montées raides comme le col de Prenn, le col de Mimosa et la route du Lang Biang. Avec un permis valable, prenez plutôt l'Air Blade 125cc.</li></ul><p>Lisez nos courtes <a href=\"{RULES}\">règles de location du scooter électrique</a> avant de le récupérer.</p>"),
  ("Ce qu'il vous faut pour louer chez Van Phu", "<ul><li><b>Clients étrangers :</b> votre passeport original. <b>Clients vietnamiens :</b> la CCCD.</li><li>Pas de caution en espèces. 150 000 VND par jour pour chaque deux-roues, prix fixe.</li><li>Un court essai et une vidéo de l'état du scooter que nous filmons ensemble.</li><li>Casque et support de téléphone inclus ; ouvert tous les jours dès 4 h 30.</li></ul><p>En savoir plus : <a href=\"{DOCS}\">ce qu'il faut pour louer un scooter à Da Lat</a>.</p>"),
 ],
 "faq_h": "Questions fréquentes",
 "faq": [
  ("Faut-il un permis pour un scooter électrique au Vietnam ?", "Pas pour un cyclomoteur électrique dont la vitesse maximale ne dépasse pas 50 km/h et dont le moteur fait au plus 4 kW. Nos scooters électriques sont dans cette catégorie. Il faut avoir au moins 16 ans."),
  ("Puis-je louer un scooter essence à Da Lat sans permis ?", "La loi vietnamienne exige un permis valable pour les scooters essence comme le Honda Vision et l'Air Blade ; chez Van Phu, nous les louons donc uniquement aux conducteurs titulaires d'un permis valable. Sans permis, prenez un scooter électrique."),
  ("Mon permis français est-il valable au Vietnam ?", "Seul compte un permis valable selon la loi vietnamienne. Les règles dépendent du pays qui l'a délivré : vérifiez avant de partir. En cas de doute, louez un scooter électrique."),
  ("Un scooter électrique suffit-il pour visiter Da Lat ?", "Pour la ville et les environs proches, oui. Une batterie tient environ 25–30 km, chaque scooter en a 2 (environ 50–60 km au total), et l'échange à la boutique coûte 20 000 VND. Pour les longs cols raides, un scooter essence 125cc convient mieux."),
  ("Le scooter électrique est-il moins cher ?", "Non — chaque deux-roues coûte 150 000 VND par jour, casque et support de téléphone compris."),
 ],
 "more_h": "À lire aussi",
 "more": [("{EV}", "Location de scooter électrique à Da Lat"), ("{DOCS}", "Ce qu'il faut pour louer un scooter à Da Lat"), ("{RULES}", "Règles de location du scooter électrique"), ("{HOME}", "Location de scooter à Da Lat — modèles et prix")],
}

T["es"] = {
 "title": "¿Necesito licencia para alquilar una moto en Vietnam? | Van Phu",
 "desc": "En Vietnam, un scooter de gasolina exige una licencia de moto válida según la ley vietnamita. Un scooter eléctrico de clase ciclomotor (hasta 50 km/h) no. Qué significa al alquilar en Da Lat.",
 "h1": "¿Necesito licencia para alquilar una moto en Vietnam?",
 "crumb": "Licencia de moto en Vietnam",
 "lead": "Respuesta corta: <b>para un scooter de gasolina, sí</b> — necesitas una licencia de moto válida según la ley vietnamita. <b>Para un scooter eléctrico de clase ciclomotor, no</b> — nuestros scooters eléctricos (velocidad máxima de hasta 50 km/h) se conducen sin licencia. Esto es lo que significa cuando alquilas en Da Lat.",
 "short_h": "Respuesta rápida",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (gasolina)", "Licencia necesaria — una licencia de moto válida en Vietnam (categoría A1 o superior)"),
  ("Scooter eléctrico (ciclomotor: hasta 50 km/h, motor de hasta 4 kW)", "No necesita licencia"),
  ("Edad mínima para un ciclomotor eléctrico", "16 años"),
  ("Casco", "Obligatorio para conductor y pasajero — incluido gratis"),
  ("Lo que guardamos en la tienda", "Tu pasaporte o documento de identidad — sin depósito en efectivo"),
 ],
 "secs": [
  ("Por qué el scooter eléctrico no necesita licencia", "<p>La Ley de Orden y Seguridad del Tráfico Vial de Vietnam de 2024 (n.º 36/2024/QH15, vigente desde el 1 de enero de 2025) exige licencia para todos los vehículos a motor, <b>excepto los ciclomotores</b>. Un ciclomotor (<i>xe gắn máy</i>) es un vehículo de dos ruedas con velocidad máxima de diseño de hasta 50 km/h; en los modelos eléctricos, el motor es de hasta 4 kW.</p><p>Nuestros scooters eléctricos son de esta clase, así que puedes conducirlos en Vietnam sin licencia. Lo demás sigue igual: casco siempre, nada de alcohol ni cerveza al conducir y respeta estrictamente las normas de tráfico vietnamitas.</p>"),
  ("Los scooters de gasolina requieren licencia válida", "<p>La Honda Vision 110cc y la Honda Air Blade 125cc son motos de más de 50 cc. Para conducirlas necesitas una licencia de moto válida según la ley vietnamita; la categoría A1 cubre motos de hasta 125 cc.</p><p>Si vienes del extranjero, comprueba antes del viaje si tu licencia es válida en Vietnam. ¿No estás seguro? El scooter eléctrico es la opción sencilla: mismo precio y sin licencia.</p>"),
  ("Sin licencia: adónde llegas en scooter eléctrico en Da Lat", "<ul><li><b>Ideal para:</b> el centro, el lago Xuan Huong, cafeterías, el mercado nocturno y lugares cercanos a la ciudad.</li><li><b>Batería:</b> una batería dura unos 25–30 km y cada scooter lleva 2 — en total unos 50–60 km. En la tienda la cambiamos por una llena por 20.000 VND.</li><li><b>Mejor evitar:</b> subidas largas y empinadas como el paso de Prenn, el paso de Mimosa y la carretera al Lang Biang. Con licencia válida, para esas rutas elige la Air Blade 125cc.</li></ul><p>Lee nuestras breves <a href=\"{RULES}\">normas de alquiler del scooter eléctrico</a> antes de recogerlo.</p>"),
  ("Qué necesitas para alquilar en Van Phu", "<ul><li><b>Clientes extranjeros:</b> tu pasaporte original. <b>Clientes vietnamitas:</b> la CCCD.</li><li>Sin depósito en efectivo. 150.000 VND al día por cualquier moto, precio fijo.</li><li>Una breve prueba y un vídeo del estado de la moto que grabamos juntos.</li><li>Casco y soporte para el móvil incluidos; abrimos todos los días desde las 4:30.</li></ul><p>Más detalles: <a href=\"{DOCS}\">qué necesitas para alquilar una moto en Da Lat</a>.</p>"),
 ],
 "faq_h": "Preguntas frecuentes",
 "faq": [
  ("¿Necesito licencia para un scooter eléctrico en Vietnam?", "No para un ciclomotor eléctrico con velocidad máxima de hasta 50 km/h y motor de hasta 4 kW. Nuestros scooters eléctricos son de esta clase. Debes tener al menos 16 años."),
  ("¿Puedo alquilar un scooter de gasolina en Da Lat sin licencia?", "La ley vietnamita exige licencia válida para scooters de gasolina como la Honda Vision y la Air Blade, por eso en Van Phu solo los alquilamos a conductores con licencia válida. Sin licencia, elige un scooter eléctrico."),
  ("¿Mi licencia de mi país vale en Vietnam?", "Solo cuenta una licencia válida según la ley vietnamita. Las normas dependen del país que la expidió, así que compruébalo antes de viajar. Si no estás seguro, alquila un scooter eléctrico."),
  ("¿Basta un scooter eléctrico para recorrer Da Lat?", "Para la ciudad y los alrededores cercanos, sí. Una batería dura unos 25–30 km, cada scooter lleva 2 (unos 50–60 km en total) y el cambio en la tienda cuesta 20.000 VND. Para pasos de montaña largos y empinados es mejor un scooter de gasolina de 125 cc."),
  ("¿El scooter eléctrico es más barato?", "No — todas las motos cuestan 150.000 VND al día, con casco y soporte para el móvil incluidos."),
 ],
 "more_h": "Sigue leyendo",
 "more": [("{EV}", "Alquiler de scooter eléctrico en Da Lat"), ("{DOCS}", "Qué necesitas para alquilar una moto en Da Lat"), ("{RULES}", "Normas de alquiler del scooter eléctrico"), ("{HOME}", "Alquiler de motos en Da Lat — modelos y precios")],
}

T["he"] = {
 "title": "האם צריך רישיון כדי לשכור קטנוע בווייטנאם? | Van Phu",
 "desc": "בווייטנאם, לקטנוע בנזין צריך רישיון אופנוע בתוקף לפי החוק הווייטנאמי. לקטנוע חשמלי מסוג טוסטוס (עד 50 קמ\"ש) לא צריך. מה זה אומר כשאתם שוכרים בדאלאט.",
 "h1": "האם צריך רישיון כדי לשכור קטנוע בווייטנאם?",
 "crumb": "רישיון אופנוע בווייטנאם",
 "lead": "בקצרה: <b>לקטנוע בנזין — כן</b>, צריך רישיון אופנוע בתוקף לפי החוק הווייטנאמי. <b>לקטנוע חשמלי מסוג טוסטוס — לא</b>: את הקטנועים החשמליים שלנו (מהירות מרבית עד 50 קמ\"ש) אפשר לרכוב בלי רישיון. הנה מה זה אומר כשאתם שוכרים בדאלאט.",
 "short_h": "תשובה מהירה",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (בנזין)", "צריך רישיון — רישיון אופנוע בתוקף בווייטנאם (דרגה A1 ומעלה)"),
  ("קטנוע חשמלי (טוסטוס: עד 50 קמ\"ש, מנוע עד 4 קילוואט)", "לא צריך רישיון"),
  ("גיל מינימלי לטוסטוס חשמלי", "16"),
  ("קסדה", "חובה לרוכב ולנוסע — מקבלים אצלנו בחינם"),
  ("מה נשאר אצלנו בחנות", "הדרכון או תעודת הזהות — בלי פיקדון במזומן"),
 ],
 "secs": [
  ("למה לקטנוע חשמלי לא צריך רישיון", "<p>חוק הסדר והבטיחות בתעבורה של וייטנאם משנת 2024 (מס' <bdi dir=\"ltr\">36/2024/QH15</bdi>, בתוקף מ־1 בינואר 2025) מחייב רישיון לכל רכב מנועי, <b>חוץ מטוסטוסים</b>. טוסטוס (<i>xe gắn máy</i>) הוא דו־גלגלי שמהירותו המרבית לפי התכנון היא עד 50 קמ\"ש; בדגמים חשמליים המנוע הוא עד 4 קילוואט.</p><p>הקטנועים החשמליים שלנו שייכים לסוג הזה, ולכן אפשר לרכוב עליהם בווייטנאם בלי רישיון. כל השאר לא משתנה: חובשים קסדה, לא שותים אלכוהול או בירה כשרוכבים, ומקפידים על חוקי התנועה של וייטנאם.</p>"),
  ("לקטנוע בנזין צריך רישיון בתוקף", "<p>Honda Vision 110cc ו־Honda Air Blade 125cc הם אופנועים מעל 50 סמ\"ק. כדי לרכוב עליהם צריך רישיון אופנוע בתוקף לפי החוק הווייטנאמי — דרגה A1 מכסה עד 125 סמ\"ק.</p><p>אם אתם מגיעים מחו\"ל, בדקו לפני הטיסה אם הרישיון שלכם תקף בווייטנאם. לא בטוחים? הקטנוע החשמלי הוא הבחירה הפשוטה: אותו מחיר, בלי רישיון.</p>"),
  ("בלי רישיון: לאן מגיעים עם קטנוע חשמלי בדאלאט", "<ul><li><b>מתאים ל:</b> מרכז העיר, אגם שואן הואנג, בתי קפה, השוק הלילי ואתרים קרובים לעיר.</li><li><b>סוללה:</b> סוללה אחת מספיקה לכ־25–30 ק\"מ, ולכל קטנוע יש 2 סוללות — בסך הכול כ־50–60 ק\"מ. בחנות מחליפים לסוללה מלאה ב־20,000 VND.</li><li><b>עדיף להימנע:</b> מעליות ארוכות ותלולות כמו מעבר פרן, מעבר מימוזה והדרך למעלה ללאנג ביאנג. עם רישיון בתוקף, קחו למסלולים האלה את ה־Air Blade 125cc.</li></ul><p>קראו לפני האיסוף את <a href=\"{RULES}\">כללי ההשכרה של הקטנוע החשמלי</a> — הם קצרים.</p>"),
  ("מה צריך כדי לשכור אצל Van Phu", "<ul><li><b>אורחים מחו\"ל:</b> הדרכון המקורי. <b>אורחים וייטנאמים:</b> CCCD.</li><li>בלי פיקדון במזומן. 150,000 VND ליום לכל כלי, מחיר קבוע.</li><li>נסיעת מבחן קצרה וסרטון של מצב הכלי שמצלמים יחד.</li><li>קסדה ומחזיק לטלפון כלולים; פתוחים כל יום מ־4:30 בבוקר.</li></ul><p>עוד פרטים: <a href=\"{DOCS}\">מה צריך כדי לשכור קטנוע בדאלאט</a>.</p>"),
 ],
 "faq_h": "שאלות נפוצות",
 "faq": [
  ("צריך רישיון לקטנוע חשמלי בווייטנאם?", "לא לטוסטוס חשמלי שמהירותו המרבית עד 50 קמ\"ש והמנוע שלו עד 4 קילוואט. הקטנועים החשמליים שלנו מהסוג הזה. צריך להיות בני 16 לפחות."),
  ("אפשר לשכור קטנוע בנזין בדאלאט בלי רישיון?", "החוק הווייטנאמי מחייב רישיון בתוקף לקטנועי בנזין כמו Honda Vision ו־Air Blade, ולכן ב־Van Phu אנחנו משכירים אותם רק לרוכבים עם רישיון בתוקף. בלי רישיון — קחו קטנוע חשמלי."),
  ("הרישיון הישראלי שלי תקף בווייטנאם?", "נחשב רק רישיון שתקף לפי החוק הווייטנאמי. הכללים תלויים במדינה שהנפיקה את הרישיון, אז בדקו לפני הנסיעה. לא בטוחים? שכרו קטנוע חשמלי."),
  ("קטנוע חשמלי מספיק כדי לטייל בדאלאט?", "לעיר ולאתרים הקרובים — כן. סוללה אחת כ־25–30 ק\"מ, לכל קטנוע 2 סוללות (בסך הכול כ־50–60 ק\"מ), והחלפת סוללה בחנות עולה 20,000 VND. למעברי הרים ארוכים ותלולים עדיף קטנוע בנזין 125cc."),
  ("הקטנוע החשמלי זול יותר?", "לא — כל כלי עולה 150,000 VND ליום, כולל קסדה ומחזיק לטלפון."),
 ],
 "more_h": "עוד לקריאה",
 "more": [("{EV}", "השכרת קטנוע חשמלי בדאלאט"), ("{DOCS}", "מה צריך כדי לשכור קטנוע בדאלאט"), ("{RULES}", "כללי ההשכרה של הקטנוע החשמלי"), ("{HOME}", "השכרת קטנועים בדאלאט — כלים ומחירים")],
}

T["it"] = {
 "title": "Serve la patente per noleggiare uno scooter in Vietnam? | Van Phu",
 "desc": "In Vietnam per uno scooter a benzina serve una patente moto valida per la legge vietnamita. Per uno scooter elettrico di classe ciclomotore (fino a 50 km/h) no. Cosa significa a Da Lat.",
 "h1": "Serve la patente per noleggiare uno scooter in Vietnam?",
 "crumb": "Patente moto in Vietnam",
 "lead": "In breve: <b>per uno scooter a benzina sì</b> — serve una patente moto valida secondo la legge vietnamita. <b>Per uno scooter elettrico di classe ciclomotore no</b> — i nostri scooter elettrici (velocità massima fino a 50 km/h) si guidano senza patente. Ecco cosa significa quando noleggi a Da Lat.",
 "short_h": "Risposta rapida",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (benzina)", "Patente necessaria — una patente moto valida in Vietnam (categoria A1 o superiore)"),
  ("Scooter elettrico (ciclomotore: fino a 50 km/h, motore fino a 4 kW)", "Nessuna patente necessaria"),
  ("Età minima per un ciclomotore elettrico", "16 anni"),
  ("Casco", "Obbligatorio per guidatore e passeggero — incluso gratis"),
  ("Cosa teniamo in negozio", "Il passaporto o la carta d'identità — nessun deposito in contanti"),
 ],
 "secs": [
  ("Perché lo scooter elettrico non richiede la patente", "<p>La legge vietnamita del 2024 sull'ordine e la sicurezza della circolazione stradale (n. 36/2024/QH15, in vigore dal 1° gennaio 2025) richiede la patente per tutti i veicoli a motore, <b>tranne i ciclomotori</b>. Un ciclomotore (<i>xe gắn máy</i>) è un veicolo a due ruote con velocità massima di progetto fino a 50 km/h; nei modelli elettrici il motore è al massimo di 4 kW.</p><p>I nostri scooter elettrici rientrano in questa classe, quindi puoi guidarli in Vietnam senza patente. Il resto non cambia: casco sempre, niente alcol né birra alla guida e rispetto rigoroso del codice della strada vietnamita.</p>"),
  ("Gli scooter a benzina richiedono una patente valida", "<p>La Honda Vision 110cc e la Honda Air Blade 125cc sono moto sopra i 50 cc. Per guidarle serve una patente moto valida secondo la legge vietnamita: la categoria A1 copre moto fino a 125 cc.</p><p>Se arrivi dall'estero, verifica prima del viaggio che la tua patente sia valida in Vietnam. Non sei sicuro? Lo scooter elettrico è la scelta semplice: stesso prezzo, niente patente.</p>"),
  ("Senza patente: dove arrivi con lo scooter elettrico a Da Lat", "<ul><li><b>Ideale per:</b> il centro, il lago Xuan Huong, i caffè, il mercato notturno e i luoghi vicini alla città.</li><li><b>Batteria:</b> una batteria dura circa 25–30 km e ogni scooter ne ha 2 — in totale circa 50–60 km. In negozio la cambiamo con una carica per 20.000 VND.</li><li><b>Meglio evitare:</b> salite lunghe e ripide come il passo Prenn, il passo Mimosa e la strada per il Lang Biang. Con una patente valida, per queste strade scegli l'Air Blade 125cc.</li></ul><p>Leggi le brevi <a href=\"{RULES}\">regole di noleggio dello scooter elettrico</a> prima del ritiro.</p>"),
  ("Cosa ti serve per noleggiare da Van Phu", "<ul><li><b>Ospiti stranieri:</b> il passaporto originale. <b>Ospiti vietnamiti:</b> la CCCD.</li><li>Nessun deposito in contanti. 150.000 VND al giorno per ogni mezzo, prezzo fisso.</li><li>Un breve giro di prova e un video dello stato del mezzo che giriamo insieme.</li><li>Casco e porta telefono inclusi; apriamo ogni giorno alle 4:30.</li></ul><p>Più dettagli: <a href=\"{DOCS}\">cosa serve per noleggiare uno scooter a Da Lat</a>.</p>"),
 ],
 "faq_h": "Domande frequenti",
 "faq": [
  ("Serve la patente per uno scooter elettrico in Vietnam?", "Non per un ciclomotore elettrico con velocità massima fino a 50 km/h e motore fino a 4 kW. I nostri scooter elettrici sono di questa classe. Devi avere almeno 16 anni."),
  ("Posso noleggiare uno scooter a benzina a Da Lat senza patente?", "La legge vietnamita richiede una patente valida per gli scooter a benzina come la Honda Vision e l'Air Blade, quindi da Van Phu li noleggiamo solo a chi ha una patente valida. Senza patente, scegli lo scooter elettrico."),
  ("La mia patente italiana è valida in Vietnam?", "Conta solo una patente valida secondo la legge vietnamita. Le regole dipendono dal paese che l'ha rilasciata, quindi controlla prima di partire. Se non sei sicuro, noleggia uno scooter elettrico."),
  ("Basta uno scooter elettrico per girare Da Lat?", "Per la città e i dintorni vicini sì. Una batteria dura circa 25–30 km, ogni scooter ne ha 2 (in totale circa 50–60 km) e il cambio in negozio costa 20.000 VND. Per i passi lunghi e ripidi è meglio uno scooter a benzina 125cc."),
  ("Lo scooter elettrico costa meno?", "No — ogni mezzo costa 150.000 VND al giorno, con casco e porta telefono inclusi."),
 ],
 "more_h": "Leggi anche",
 "more": [("{EV}", "Noleggio scooter elettrico a Da Lat"), ("{DOCS}", "Cosa serve per noleggiare uno scooter a Da Lat"), ("{RULES}", "Regole di noleggio dello scooter elettrico"), ("{HOME}", "Noleggio scooter a Da Lat — mezzi e prezzi")],
}

T["nl"] = {
 "title": "Rijbewijs nodig om een scooter te huren in Vietnam? | Van Phu",
 "desc": "In Vietnam heb je voor een benzinescooter een motorrijbewijs nodig dat geldig is volgens de Vietnamese wet. Voor een elektrische bromfietsscooter (tot 50 km/u) niet. Wat dat betekent in Da Lat.",
 "h1": "Heb je een rijbewijs nodig om een scooter te huren in Vietnam?",
 "crumb": "Rijbewijs in Vietnam",
 "lead": "Kort antwoord: <b>voor een benzinescooter wel</b> — je hebt een motorrijbewijs nodig dat geldig is volgens de Vietnamese wet. <b>Voor een elektrische scooter in de bromfietsklasse niet</b> — onze elektrische scooters (topsnelheid tot 50 km/u) mag je zonder rijbewijs rijden. Dit betekent het als je huurt in Da Lat.",
 "short_h": "Snel antwoord",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (benzine)", "Rijbewijs nodig — een in Vietnam geldig motorrijbewijs (categorie A1 of hoger)"),
  ("Elektrische scooter (bromfiets: tot 50 km/u, motor tot 4 kW)", "Geen rijbewijs nodig"),
  ("Minimumleeftijd voor een elektrische bromfiets", "16 jaar"),
  ("Helm", "Verplicht voor bestuurder en passagier — gratis inbegrepen"),
  ("Wat wij in de winkel bewaren", "Je paspoort of ID-kaart — geen borg in contanten"),
 ],
 "secs": [
  ("Waarom je voor een elektrische scooter geen rijbewijs nodig hebt", "<p>De Vietnamese wet op orde en veiligheid in het wegverkeer van 2024 (nr. 36/2024/QH15, van kracht sinds 1 januari 2025) vereist een rijbewijs voor alle motorvoertuigen, <b>behalve bromfietsen</b>. Een bromfiets (<i>xe gắn máy</i>) is een tweewieler met een ontwerpsnelheid van maximaal 50 km/u; bij elektrische modellen is de motor maximaal 4 kW.</p><p>Onze elektrische scooters vallen in deze klasse, dus je mag ze in Vietnam zonder rijbewijs rijden. De rest blijft gelden: helm op, geen alcohol of bier tijdens het rijden en houd je strikt aan de Vietnamese verkeersregels.</p>"),
  ("Benzinescooters vragen een geldig rijbewijs", "<p>De Honda Vision 110cc en de Honda Air Blade 125cc zijn motoren boven de 50 cc. Daarvoor heb je een motorrijbewijs nodig dat geldig is volgens de Vietnamese wet — categorie A1 dekt motoren tot 125 cc.</p><p>Kom je uit het buitenland, check dan vóór je reis of je rijbewijs in Vietnam geldig is. Twijfel je? De elektrische scooter is de makkelijke keuze: zelfde prijs, geen rijbewijs.</p>"),
  ("Zonder rijbewijs: waar je komt met een elektrische scooter in Da Lat", "<ul><li><b>Ideaal voor:</b> het centrum, het Xuan Huong-meer, cafés, de nachtmarkt en bezienswaardigheden vlak bij de stad.</li><li><b>Accu:</b> één accu gaat ongeveer 25–30 km mee en elke scooter heeft er 2 — samen ongeveer 50–60 km. In de winkel wisselen we hem voor een volle accu voor 20.000 VND.</li><li><b>Liever vermijden:</b> lange, steile klimmen zoals de Prenn-pas, de Mimosa-pas en de weg omhoog naar Lang Biang. Met een geldig rijbewijs neem je daarvoor de Air Blade 125cc.</li></ul><p>Lees vóór het ophalen even onze korte <a href=\"{RULES}\">huurregels voor de elektrische scooter</a>.</p>"),
  ("Wat je nodig hebt om te huren bij Van Phu", "<ul><li><b>Buitenlandse gasten:</b> je originele paspoort. <b>Vietnamese gasten:</b> je CCCD.</li><li>Geen borg in contanten. 150.000 VND per dag voor elke scooter, vaste prijs.</li><li>Een korte proefrit en een video van de staat van de scooter die we samen maken.</li><li>Helm en telefoonhouder inbegrepen; we zijn elke dag open vanaf 4.30 uur.</li></ul><p>Meer info: <a href=\"{DOCS}\">wat je nodig hebt om een scooter te huren in Da Lat</a>.</p>"),
 ],
 "faq_h": "Veelgestelde vragen",
 "faq": [
  ("Heb je in Vietnam een rijbewijs nodig voor een elektrische scooter?", "Niet voor een elektrische bromfiets met een topsnelheid tot 50 km/u en een motor tot 4 kW. Onze elektrische scooters vallen in deze klasse. Je moet minstens 16 jaar zijn."),
  ("Kan ik in Da Lat zonder rijbewijs een benzinescooter huren?", "De Vietnamese wet vereist een geldig rijbewijs voor benzinescooters zoals de Honda Vision en de Air Blade, dus bij Van Phu verhuren we die alleen aan rijders met een geldig rijbewijs. Zonder rijbewijs neem je de elektrische scooter."),
  ("Is mijn Nederlandse of Belgische rijbewijs geldig in Vietnam?", "Alleen een rijbewijs dat geldig is volgens de Vietnamese wet telt. De regels hangen af van het land dat het heeft uitgegeven, dus check het vóór je reis. Twijfel je, huur dan een elektrische scooter."),
  ("Is een elektrische scooter genoeg om Da Lat te ontdekken?", "Voor de stad en de directe omgeving wel. Eén accu gaat ongeveer 25–30 km mee, elke scooter heeft er 2 (samen ongeveer 50–60 km) en een accuwissel in de winkel kost 20.000 VND. Voor lange, steile passen is een 125cc-benzinescooter beter."),
  ("Is de elektrische scooter goedkoper?", "Nee — elke scooter kost 150.000 VND per dag, inclusief helm en telefoonhouder."),
 ],
 "more_h": "Lees ook",
 "more": [("{EV}", "Elektrische scooter huren in Da Lat"), ("{DOCS}", "Wat je nodig hebt om een scooter te huren in Da Lat"), ("{RULES}", "Huurregels voor de elektrische scooter"), ("{HOME}", "Scooter huren in Da Lat — modellen en prijzen")],
}

T["km"] = {
 "title": "តើត្រូវការប័ណ្ណបើកបរ ដើម្បីជួលម៉ូតូនៅវៀតណាមទេ? | Van Phu",
 "desc": "នៅវៀតណាម ម៉ូតូសាំងត្រូវការប័ណ្ណបើកបរម៉ូតូដែលមានសុពលភាពតាមច្បាប់វៀតណាម។ ម៉ូតូអគ្គិសនីប្រភេទម៉ូប៉ិត (ល្បឿនមិនលើស 50 គ.ម/ម៉ោង) មិនត្រូវការទេ។ ការពន្យល់សម្រាប់ការជួលនៅដាឡាត់។",
 "h1": "តើត្រូវការប័ណ្ណបើកបរ ដើម្បីជួលម៉ូតូនៅវៀតណាមទេ?",
 "crumb": "ប័ណ្ណបើកបរម៉ូតូនៅវៀតណាម",
 "lead": "ចម្លើយខ្លី៖ <b>ម៉ូតូសាំង ត្រូវការ</b> ប័ណ្ណបើកបរម៉ូតូដែលមានសុពលភាពតាមច្បាប់វៀតណាម។ <b>ម៉ូតូអគ្គិសនីប្រភេទម៉ូប៉ិត មិនត្រូវការទេ</b> — ម៉ូតូអគ្គិសនីរបស់យើង (ល្បឿនអតិបរមាមិនលើស 50 គ.ម/ម៉ោង) អាចជិះបានដោយគ្មានប័ណ្ណបើកបរ។ ខាងក្រោមនេះជាអត្ថន័យនៅពេលអ្នកជួលនៅដាឡាត់។",
 "short_h": "ចម្លើយរហ័ស",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (សាំង)", "ត្រូវការប័ណ្ណបើកបរម៉ូតូដែលមានសុពលភាពនៅវៀតណាម (ប្រភេទ A1 ឡើងទៅ)"),
  ("ម៉ូតូអគ្គិសនី (ម៉ូប៉ិត៖ មិនលើស 50 គ.ម/ម៉ោង ម៉ូទ័រមិនលើស 4 kW)", "មិនត្រូវការប័ណ្ណបើកបរ"),
  ("អាយុអប្បបរមាសម្រាប់ម៉ូប៉ិតអគ្គិសនី", "16 ឆ្នាំ"),
  ("មួកសុវត្ថិភាព", "ចាំបាច់សម្រាប់អ្នកបើក និងអ្នកជិះពីក្រោយ — ផ្តល់ជូនដោយឥតគិតថ្លៃ"),
  ("អ្វីដែលហាងរក្សាទុក", "លិខិតឆ្លងដែន ឬអត្តសញ្ញាណប័ណ្ណ — គ្មានប្រាក់កក់"),
 ],
 "secs": [
  ("ហេតុអ្វីម៉ូតូអគ្គិសនីមិនត្រូវការប័ណ្ណបើកបរ", "<p>ច្បាប់ស្តីពីសណ្តាប់ធ្នាប់ និងសុវត្ថិភាពចរាចរណ៍ផ្លូវគោករបស់វៀតណាម ឆ្នាំ 2024 (លេខ 36/2024/QH15 ចូលជាធរមានចាប់ពីថ្ងៃទី 1 ខែមករា ឆ្នាំ 2025) តម្រូវឱ្យមានប័ណ្ណបើកបរសម្រាប់យានយន្តទាំងអស់ <b>លើកលែងតែម៉ូប៉ិត</b>។ ម៉ូប៉ិត (<i>xe gắn máy</i>) គឺជាយានពីរកង់ដែលមានល្បឿនអតិបរមាតាមការរចនាមិនលើស 50 គ.ម/ម៉ោង ហើយសម្រាប់ម៉ូដែលអគ្គិសនី ម៉ូទ័រមិនលើស 4 kW។</p><p>ម៉ូតូអគ្គិសនីរបស់យើងស្ថិតក្នុងប្រភេទនេះ ដូច្នេះអ្នកអាចជិះនៅវៀតណាមដោយគ្មានប័ណ្ណបើកបរ។ ច្បាប់ផ្សេងទៀតនៅដដែល៖ ពាក់មួកសុវត្ថិភាព មិនផឹកស្រា ឬបៀរពេលជិះ និងគោរពច្បាប់ចរាចរណ៍វៀតណាមយ៉ាងម៉ឺងម៉ាត់។</p>"),
  ("ម៉ូតូសាំងត្រូវការប័ណ្ណបើកបរដែលមានសុពលភាព", "<p>Honda Vision 110cc និង Honda Air Blade 125cc គឺជាម៉ូតូលើស 50cc។ ដើម្បីជិះ អ្នកត្រូវការប័ណ្ណបើកបរម៉ូតូដែលមានសុពលភាពតាមច្បាប់វៀតណាម — ប្រភេទ A1 គ្របដណ្តប់ម៉ូតូរហូតដល់ 125cc។</p><p>បើអ្នកមកពីបរទេស សូមពិនិត្យមុនពេលធ្វើដំណើរថា ប័ណ្ណបើកបររបស់អ្នកមានសុពលភាពនៅវៀតណាមឬទេ។ មិនប្រាកដ? ម៉ូតូអគ្គិសនីជាជម្រើសងាយស្រួល៖ តម្លៃដូចគ្នា ហើយមិនត្រូវការប័ណ្ណបើកបរ។</p>"),
  ("គ្មានប័ណ្ណបើកបរ៖ ម៉ូតូអគ្គិសនីទៅកន្លែងណាបានខ្លះនៅដាឡាត់", "<ul><li><b>សមស្របសម្រាប់៖</b> កណ្តាលទីក្រុង បឹងសួនហឿង ហាងកាហ្វេ ផ្សាររាត្រី និងកន្លែងទេសចរណ៍ជិតទីក្រុង។</li><li><b>ថ្ម៖</b> ថ្មមួយដុំជិះបានប្រហែល 25–30 គ.ម ម៉ូតូនីមួយៗមានថ្ម 2 ដុំ — សរុបប្រហែល 50–60 គ.ម។ ប្តូរថ្មពេញនៅហាង 20,000 VND ក្នុងមួយដង។</li><li><b>គួរជៀសវាង៖</b> ផ្លូវឡើងភ្នំវែង និងចោត ដូចជា ច្រកភ្នំ Prenn ច្រកភ្នំ Mimosa និងផ្លូវឡើងភ្នំ Lang Biang។ បើមានប័ណ្ណបើកបរដែលមានសុពលភាព សូមជ្រើស Air Blade 125cc។</li></ul><p>សូមអាន<a href=\"{RULES}\">ច្បាប់ជួលម៉ូតូអគ្គិសនី</a>ខ្លីៗ មុនពេលទទួលម៉ូតូ។</p>"),
  ("អ្វីដែលត្រូវការដើម្បីជួលនៅ Van Phu", "<ul><li><b>ភ្ញៀវបរទេស៖</b> លិខិតឆ្លងដែនច្បាប់ដើម។ <b>ភ្ញៀវវៀតណាម៖</b> CCCD។</li><li>គ្មានប្រាក់កក់។ ម៉ូតូគ្រប់ប្រភេទ 150,000 VND ក្នុងមួយថ្ងៃ តម្លៃថេរ។</li><li>សាកល្បងជិះខ្លី និងថតវីដេអូស្ថានភាពម៉ូតូជាមួយគ្នា។</li><li>មានមួកសុវត្ថិភាព និងជើងទម្រទូរស័ព្ទ ហាងបើករាល់ថ្ងៃចាប់ពីម៉ោង 4:30 ព្រឹក។</li></ul><p>ព័ត៌មានបន្ថែម៖ <a href=\"{DOCS}\">អ្វីដែលត្រូវការដើម្បីជួលម៉ូតូនៅដាឡាត់</a>។</p>"),
 ],
 "faq_h": "សំណួរដែលសួរញឹកញាប់",
 "faq": [
  ("ម៉ូតូអគ្គិសនីនៅវៀតណាមត្រូវការប័ណ្ណបើកបរទេ?", "ម៉ូប៉ិតអគ្គិសនីដែលមានល្បឿនអតិបរមាមិនលើស 50 គ.ម/ម៉ោង និងម៉ូទ័រមិនលើស 4 kW មិនត្រូវការប័ណ្ណបើកបរទេ។ ម៉ូតូអគ្គិសនីរបស់យើងស្ថិតក្នុងប្រភេទនេះ។ អ្នកជិះត្រូវមានអាយុយ៉ាងតិច 16 ឆ្នាំ។"),
  ("តើអាចជួលម៉ូតូសាំងនៅដាឡាត់ដោយគ្មានប័ណ្ណបើកបរបានទេ?", "ច្បាប់វៀតណាមតម្រូវឱ្យមានប័ណ្ណបើកបរដែលមានសុពលភាពសម្រាប់ម៉ូតូសាំងដូចជា Honda Vision និង Air Blade ដូច្នេះ Van Phu ជួលម៉ូតូសាំងតែដល់អ្នកដែលមានប័ណ្ណបើកបរដែលមានសុពលភាពប៉ុណ្ណោះ។ បើគ្មាន សូមជ្រើសម៉ូតូអគ្គិសនី។"),
  ("តើប័ណ្ណបើកបររបស់ខ្ញុំមានសុពលភាពនៅវៀតណាមទេ?", "មានតែប័ណ្ណបើកបរដែលមានសុពលភាពតាមច្បាប់វៀតណាមប៉ុណ្ណោះដែលត្រូវបានទទួលស្គាល់។ លក្ខខណ្ឌអាស្រ័យលើប្រទេសដែលចេញប័ណ្ណ ដូច្នេះសូមពិនិត្យមុនពេលធ្វើដំណើរ។ បើមិនប្រាកដ សូមជួលម៉ូតូអគ្គិសនី។"),
  ("ម៉ូតូអគ្គិសនីគ្រប់គ្រាន់សម្រាប់ដើរលេងដាឡាត់ទេ?", "សម្រាប់ទីក្រុង និងកន្លែងជិតៗ គឺគ្រប់គ្រាន់។ ថ្មមួយដុំប្រហែល 25–30 គ.ម ម៉ូតូនីមួយៗមានថ្ម 2 ដុំ (សរុបប្រហែល 50–60 គ.ម) ហើយប្តូរថ្មនៅហាង 20,000 VND។ សម្រាប់ច្រកភ្នំវែង និងចោត ម៉ូតូសាំង 125cc សមស្របជាង។"),
  ("ម៉ូតូអគ្គិសនីថោកជាងទេ?", "ទេ — ម៉ូតូគ្រប់ប្រភេទ 150,000 VND ក្នុងមួយថ្ងៃ រួមទាំងមួកសុវត្ថិភាព និងជើងទម្រទូរស័ព្ទ។"),
 ],
 "more_h": "អានបន្ថែម",
 "more": [("{EV}", "ជួលម៉ូតូអគ្គិសនីនៅដាឡាត់"), ("{DOCS}", "អ្វីដែលត្រូវការដើម្បីជួលម៉ូតូនៅដាឡាត់"), ("{RULES}", "ច្បាប់ជួលម៉ូតូអគ្គិសនី"), ("{HOME}", "ជួលម៉ូតូនៅដាឡាត់ — ប្រភេទម៉ូតូ និងតម្លៃ")],
}

T["lo"] = {
 "title": "ເຊົ່າລົດຈັກຢູ່ຫວຽດນາມ ຕ້ອງມີໃບຂັບຂີ່ບໍ? | Van Phu",
 "desc": "ຢູ່ຫວຽດນາມ ລົດຈັກນ້ຳມັນຕ້ອງມີໃບຂັບຂີ່ລົດຈັກທີ່ຖືກຕ້ອງຕາມກົດໝາຍຫວຽດນາມ. ລົດໄຟຟ້າປະເພດໂມເປັດ (ບໍ່ເກີນ 50 ກມ/ຊມ) ບໍ່ຕ້ອງມີ. ອະທິບາຍສຳລັບການເຊົ່າຢູ່ດາລາດ.",
 "h1": "ເຊົ່າລົດຈັກຢູ່ຫວຽດນາມ ຕ້ອງມີໃບຂັບຂີ່ບໍ?",
 "crumb": "ໃບຂັບຂີ່ລົດຈັກຢູ່ຫວຽດນາມ",
 "lead": "ຕອບສັ້ນໆ: <b>ລົດຈັກນ້ຳມັນ ຕ້ອງມີ</b> ໃບຂັບຂີ່ລົດຈັກທີ່ຖືກຕ້ອງຕາມກົດໝາຍຫວຽດນາມ. <b>ລົດໄຟຟ້າປະເພດໂມເປັດ ບໍ່ຕ້ອງມີ</b> — ລົດໄຟຟ້າຂອງພວກເຮົາ (ຄວາມໄວສູງສຸດບໍ່ເກີນ 50 ກມ/ຊມ) ຂີ່ໄດ້ໂດຍບໍ່ຕ້ອງມີໃບຂັບຂີ່. ນີ້ແມ່ນຄວາມໝາຍເມື່ອທ່ານເຊົ່າລົດຢູ່ດາລາດ.",
 "short_h": "ຄຳຕອບດ່ວນ",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (ນ້ຳມັນ)", "ຕ້ອງມີໃບຂັບຂີ່ລົດຈັກທີ່ຖືກຕ້ອງໃນຫວຽດນາມ (ປະເພດ A1 ຂຶ້ນໄປ)"),
  ("ລົດໄຟຟ້າ (ໂມເປັດ: ບໍ່ເກີນ 50 ກມ/ຊມ, ມໍເຕີບໍ່ເກີນ 4 kW)", "ບໍ່ຕ້ອງມີໃບຂັບຂີ່"),
  ("ອາຍຸຕ່ຳສຸດສຳລັບໂມເປັດໄຟຟ້າ", "16 ປີ"),
  ("ໝວກກັນກະທົບ", "ບັງຄັບທັງຄົນຂີ່ ແລະ ຄົນຊ້ອນ — ໃຫ້ຟຣີ"),
  ("ສິ່ງທີ່ຮ້ານເກັບໄວ້", "ໜັງສືຜ່ານແດນ ຫຼື ບັດປະຈຳຕົວ — ບໍ່ມີເງິນມັດຈຳ"),
 ],
 "secs": [
  ("ເປັນຫຍັງລົດໄຟຟ້າບໍ່ຕ້ອງມີໃບຂັບຂີ່", "<p>ກົດໝາຍວ່າດ້ວຍຄວາມເປັນລະບຽບ ແລະ ຄວາມປອດໄພການຈະລາຈອນທາງບົກຂອງຫວຽດນາມ ປີ 2024 (ເລກທີ 36/2024/QH15, ມີຜົນແຕ່ວັນທີ 1 ມັງກອນ 2025) ກຳນົດໃຫ້ຜູ້ຂັບຂີ່ພາຫະນະຕ້ອງມີໃບຂັບຂີ່ <b>ຍົກເວັ້ນໂມເປັດ</b>. ໂມເປັດ (<i>xe gắn máy</i>) ແມ່ນລົດສອງລໍ້ທີ່ອອກແບບໃຫ້ມີຄວາມໄວສູງສຸດບໍ່ເກີນ 50 ກມ/ຊມ; ສຳລັບລຸ້ນໄຟຟ້າ ມໍເຕີບໍ່ເກີນ 4 kW.</p><p>ລົດໄຟຟ້າຂອງພວກເຮົາຢູ່ໃນປະເພດນີ້ ສະນັ້ນທ່ານຂີ່ໄດ້ຢູ່ຫວຽດນາມໂດຍບໍ່ຕ້ອງມີໃບຂັບຂີ່. ກົດອື່ນໆຍັງຄືເກົ່າ: ໃສ່ໝວກກັນກະທົບ, ບໍ່ດື່ມເຫຼົ້າ ຫຼື ເບຍຂະນະຂີ່ ແລະ ປະຕິບັດຕາມກົດຈະລາຈອນຫວຽດນາມຢ່າງເຂັ້ມງວດ.</p>"),
  ("ລົດຈັກນ້ຳມັນຕ້ອງມີໃບຂັບຂີ່ທີ່ຖືກຕ້ອງ", "<p>Honda Vision 110cc ແລະ Honda Air Blade 125cc ແມ່ນລົດຈັກເກີນ 50cc. ເພື່ອຂີ່ ທ່ານຕ້ອງມີໃບຂັບຂີ່ລົດຈັກທີ່ຖືກຕ້ອງຕາມກົດໝາຍຫວຽດນາມ — ປະເພດ A1 ໃຊ້ໄດ້ກັບລົດເຖິງ 125cc.</p><p>ຖ້າທ່ານມາຈາກຕ່າງປະເທດ ກະລຸນາກວດກ່ອນເດີນທາງວ່າໃບຂັບຂີ່ຂອງທ່ານໃຊ້ໄດ້ຢູ່ຫວຽດນາມບໍ. ບໍ່ແນ່ໃຈ? ລົດໄຟຟ້າແມ່ນທາງເລືອກທີ່ງ່າຍ: ລາຄາເທົ່າກັນ ແລະ ບໍ່ຕ້ອງມີໃບຂັບຂີ່.</p>"),
  ("ບໍ່ມີໃບຂັບຂີ່: ລົດໄຟຟ້າໄປໃສໄດ້ແດ່ຢູ່ດາລາດ", "<ul><li><b>ເໝາະກັບ:</b> ໃຈກາງເມືອງ, ທະເລສາບຊວນເຮືອງ, ຮ້ານກາເຟ, ຕະຫຼາດກາງຄືນ ແລະ ສະຖານທີ່ທ່ອງທ່ຽວໃກ້ເມືອງ.</li><li><b>ແບັດເຕີຣີ:</b> ແບັດກ້ອນດຽວຂີ່ໄດ້ປະມານ 25–30 ກມ, ລົດແຕ່ລະຄັນມີແບັດ 2 ກ້ອນ — ລວມປະມານ 50–60 ກມ. ປ່ຽນແບັດເຕັມທີ່ຮ້ານ 20,000 VND ຕໍ່ຄັ້ງ.</li><li><b>ຄວນຫຼີກລ່ຽງ:</b> ທາງຂຶ້ນພູຍາວ ແລະ ຊັນ ເຊັ່ນ ຊ່ອງພູ Prenn, ຊ່ອງພູ Mimosa ແລະ ທາງຂຶ້ນ Lang Biang. ຖ້າມີໃບຂັບຂີ່ທີ່ຖືກຕ້ອງ ໃຫ້ເລືອກ Air Blade 125cc.</li></ul><p>ອ່ານ<a href=\"{RULES}\">ກົດການເຊົ່າລົດໄຟຟ້າ</a>ສັ້ນໆ ກ່ອນຮັບລົດ.</p>"),
  ("ສິ່ງທີ່ຕ້ອງການເພື່ອເຊົ່າທີ່ Van Phu", "<ul><li><b>ແຂກຕ່າງປະເທດ:</b> ໜັງສືຜ່ານແດນສະບັບແທ້. <b>ແຂກຫວຽດນາມ:</b> CCCD.</li><li>ບໍ່ມີເງິນມັດຈຳ. ລົດທຸກຄັນ 150,000 VND ຕໍ່ມື້ ລາຄາຄົງທີ່.</li><li>ທົດລອງຂີ່ສັ້ນໆ ແລະ ຖ່າຍວິດີໂອສະພາບລົດນຳກັນ.</li><li>ມີໝວກກັນກະທົບ ແລະ ທີ່ຈັບໂທລະສັບ; ຮ້ານເປີດທຸກມື້ແຕ່ 4:30 ໂມງເຊົ້າ.</li></ul><p>ລາຍລະອຽດເພີ່ມເຕີມ: <a href=\"{DOCS}\">ສິ່ງທີ່ຕ້ອງການເພື່ອເຊົ່າລົດຈັກຢູ່ດາລາດ</a>.</p>"),
 ],
 "faq_h": "ຄຳຖາມທີ່ພົບເລື້ອຍ",
 "faq": [
  ("ລົດໄຟຟ້າຢູ່ຫວຽດນາມ ຕ້ອງມີໃບຂັບຂີ່ບໍ?", "ໂມເປັດໄຟຟ້າທີ່ມີຄວາມໄວສູງສຸດບໍ່ເກີນ 50 ກມ/ຊມ ແລະ ມໍເຕີບໍ່ເກີນ 4 kW ບໍ່ຕ້ອງມີໃບຂັບຂີ່. ລົດໄຟຟ້າຂອງພວກເຮົາຢູ່ໃນປະເພດນີ້. ຜູ້ຂີ່ຕ້ອງມີອາຍຸ 16 ປີຂຶ້ນໄປ."),
  ("ບໍ່ມີໃບຂັບຂີ່ ເຊົ່າລົດຈັກນ້ຳມັນຢູ່ດາລາດໄດ້ບໍ?", "ກົດໝາຍຫວຽດນາມກຳນົດໃຫ້ຕ້ອງມີໃບຂັບຂີ່ທີ່ຖືກຕ້ອງສຳລັບລົດຈັກນ້ຳມັນ ເຊັ່ນ Honda Vision ແລະ Air Blade ສະນັ້ນ Van Phu ໃຫ້ເຊົ່າສະເພາະຜູ້ທີ່ມີໃບຂັບຂີ່ທີ່ຖືກຕ້ອງ. ຖ້າບໍ່ມີ ໃຫ້ເລືອກລົດໄຟຟ້າ."),
  ("ໃບຂັບຂີ່ລາວໃຊ້ໄດ້ຢູ່ຫວຽດນາມບໍ?", "ຮັບສະເພາະໃບຂັບຂີ່ທີ່ຖືກຕ້ອງຕາມກົດໝາຍຫວຽດນາມ. ເງື່ອນໄຂຂຶ້ນກັບປະເທດທີ່ອອກໃບຂັບຂີ່ ສະນັ້ນກະລຸນາກວດກ່ອນເດີນທາງ. ຖ້າບໍ່ແນ່ໃຈ ໃຫ້ເຊົ່າລົດໄຟຟ້າ."),
  ("ລົດໄຟຟ້າພຽງພໍສຳລັບທ່ຽວດາລາດບໍ?", "ໃນເມືອງ ແລະ ບ່ອນໃກ້ໆ ພຽງພໍ. ແບັດກ້ອນດຽວປະມານ 25–30 ກມ, ລົດແຕ່ລະຄັນມີແບັດ 2 ກ້ອນ (ລວມປະມານ 50–60 ກມ), ປ່ຽນແບັດທີ່ຮ້ານ 20,000 VND. ສຳລັບຊ່ອງພູຍາວ ແລະ ຊັນ ລົດຈັກນ້ຳມັນ 125cc ເໝາະກວ່າ."),
  ("ລົດໄຟຟ້າຖືກກວ່າບໍ?", "ບໍ່ — ລົດທຸກຄັນ 150,000 VND ຕໍ່ມື້ ລວມໝວກກັນກະທົບ ແລະ ທີ່ຈັບໂທລະສັບ."),
 ],
 "more_h": "ອ່ານຕໍ່",
 "more": [("{EV}", "ເຊົ່າລົດໄຟຟ້າຢູ່ດາລາດ"), ("{DOCS}", "ສິ່ງທີ່ຕ້ອງການເພື່ອເຊົ່າລົດຈັກຢູ່ດາລາດ"), ("{RULES}", "ກົດການເຊົ່າລົດໄຟຟ້າ"), ("{HOME}", "ເຊົ່າລົດຈັກຢູ່ດາລາດ — ລົດ ແລະ ລາຄາ")],
}

T["my"] = {
 "title": "ဗီယက်နမ်မှာ ဆိုင်ကယ်ငှားဖို့ လိုင်စင်လိုသလား? | Van Phu",
 "desc": "ဗီယက်နမ်မှာ ဓာတ်ဆီစကူတာစီးရန် ဗီယက်နမ်ဥပဒေအရ တရားဝင်သော ဆိုင်ကယ်လိုင်စင် လိုအပ်သည်။ မိုပက်အမျိုးအစား လျှပ်စစ်စကူတာ (အမြန်နှုန်း 50 km/h အထိ) မလိုပါ။ ဒါလတ်မှာ ငှားရာတွင် အဓိပ္ပာယ်။",
 "h1": "ဗီယက်နမ်မှာ ဆိုင်ကယ်ငှားဖို့ လိုင်စင်လိုသလား?",
 "crumb": "ဗီယက်နမ် ဆိုင်ကယ်လိုင်စင်",
 "lead": "အတိုချုပ်အဖြေ — <b>ဓာတ်ဆီစကူတာအတွက် လိုပါသည်</b>၊ ဗီယက်နမ်ဥပဒေအရ တရားဝင်သော ဆိုင်ကယ်လိုင်စင် ရှိရမည်။ <b>မိုပက်အမျိုးအစား လျှပ်စစ်စကူတာအတွက် မလိုပါ</b> — ကျွန်ုပ်တို့၏ လျှပ်စစ်စကူတာများ (အမြင့်ဆုံးအမြန်နှုန်း 50 km/h အထိ) ကို လိုင်စင်မပါဘဲ စီးနိုင်ပါသည်။ ဒါလတ်မှာ ငှားသည့်အခါ ဘာကိုဆိုလိုသလဲ ဆက်ဖတ်ပါ။",
 "short_h": "အမြန်အဖြေ",
 "short": [
  ("Honda Vision 110cc, Honda Air Blade 125cc (ဓာတ်ဆီ)", "လိုင်စင်လိုသည် — ဗီယက်နမ်တွင် တရားဝင်သော ဆိုင်ကယ်လိုင်စင် (A1 အဆင့် သို့မဟုတ် အထက်)"),
  ("လျှပ်စစ်စကူတာ (မိုပက်: 50 km/h အထိ၊ မော်တာ 4 kW အထိ)", "လိုင်စင်မလို"),
  ("လျှပ်စစ်မိုပက် စီးရန် အနည်းဆုံးအသက်", "16 နှစ်"),
  ("ဦးထုပ်", "စီးသူနှင့် နောက်ထိုင်သူ နှစ်ဦးလုံး မဖြစ်မနေ ဆောင်းရမည် — အခမဲ့ ပေးသည်"),
  ("ဆိုင်တွင် ထားခဲ့ရမည့်အရာ", "နိုင်ငံကူးလက်မှတ် သို့မဟုတ် မှတ်ပုံတင် — ငွေသားအာမခံ မလို"),
 ],
 "secs": [
  ("လျှပ်စစ်စကူတာအတွက် လိုင်စင် ဘာကြောင့်မလိုသလဲ", "<p>ဗီယက်နမ်၏ ၂၀၂၄ ခုနှစ် လမ်းစည်းကမ်းနှင့် ယာဉ်အန္တရာယ်ကင်းရေး ဥပဒေ (အမှတ် 36/2024/QH15၊ ၂၀၂၅ ဇန်နဝါရီ ၁ ရက်မှစ၍ အာဏာတည်) သည် မော်တော်ယာဉ်အားလုံးအတွက် လိုင်စင် လိုအပ်သည်ဟု သတ်မှတ်ထားသော်လည်း <b>မိုပက်များကို ချွင်းချက်ပေးထားသည်</b>။ မိုပက် (<i>xe gắn máy</i>) ဆိုသည်မှာ ဒီဇိုင်းအရ အမြင့်ဆုံးအမြန်နှုန်း 50 km/h အထိသာရှိသော ဘီးနှစ်ဘီးယာဉ်ဖြစ်ပြီး လျှပ်စစ်မော်ဒယ်များတွင် မော်တာ 4 kW အထိသာ ရှိသည်။</p><p>ကျွန်ုပ်တို့၏ လျှပ်စစ်စကူတာများသည် ဤအမျိုးအစားဖြစ်သောကြောင့် ဗီယက်နမ်တွင် လိုင်စင်မပါဘဲ စီးနိုင်သည်။ အခြားစည်းကမ်းများ မပြောင်းပါ — ဦးထုပ်ဆောင်းပါ၊ စီးနေစဉ် အရက် သို့မဟုတ် ဘီယာ မသောက်ပါနှင့်၊ ဗီယက်နမ် ယာဉ်စည်းကမ်းကို တင်းကျပ်စွာ လိုက်နာပါ။</p>"),
  ("ဓာတ်ဆီစကူတာအတွက် တရားဝင်လိုင်စင် လိုအပ်သည်", "<p>Honda Vision 110cc နှင့် Honda Air Blade 125cc တို့သည် 50cc ထက်ကြီးသော ဆိုင်ကယ်များ ဖြစ်သည်။ စီးရန် ဗီယက်နမ်ဥပဒေအရ တရားဝင်သော ဆိုင်ကယ်လိုင်စင် လိုအပ်ပြီး A1 အဆင့်သည် 125cc အထိ ပါဝင်သည်။</p><p>နိုင်ငံခြားမှ လာမည်ဆိုလျှင် ခရီးမထွက်မီ သင့်လိုင်စင် ဗီယက်နမ်တွင် တရားဝင်မဝင် စစ်ဆေးပါ။ မသေချာပါက လျှပ်စစ်စကူတာကို ရွေးပါ — ဈေးနှုန်းတူပြီး လိုင်စင်မလိုပါ။</p>"),
  ("လိုင်စင်မရှိလျှင် — ဒါလတ်တွင် လျှပ်စစ်စကူတာဖြင့် ဘယ်နေရာတွေ သွားနိုင်သလဲ", "<ul><li><b>သင့်တော်သည်:</b> မြို့လယ်၊ ဆွမ်ဟွောင်ကန်၊ ကော်ဖီဆိုင်များ၊ ညဈေးနှင့် မြို့အနီးရှိ နေရာများ။</li><li><b>ဘက်ထရီ:</b> ဘက်ထရီတစ်လုံးဖြင့် 25–30 km ခန့် စီးနိုင်ပြီး စကူတာတစ်စီးလျှင် ဘက်ထရီ ၂ လုံးပါသည် — စုစုပေါင်း 50–60 km ခန့်။ ဆိုင်တွင် ဘက်ထရီအပြည့်နှင့် လဲလှယ်ခ တစ်ကြိမ်လျှင် 20,000 VND။</li><li><b>ရှောင်သင့်သည်:</b> Prenn တောင်ကြား၊ Mimosa တောင်ကြားနှင့် Lang Biang တက်လမ်းကဲ့သို့ ရှည်လျားပြီး မတ်စောက်သော တက်လမ်းများ။ တရားဝင်လိုင်စင်ရှိပါက ဤလမ်းများအတွက် Air Blade 125cc ကို ရွေးပါ။</li></ul><p>စကူတာမယူမီ <a href=\"{RULES}\">လျှပ်စစ်စကူတာ ငှားရမ်းခြင်း စည်းကမ်းများ</a> ကို ဖတ်ပါ။</p>"),
  ("Van Phu တွင် ငှားရန် လိုအပ်သည်များ", "<ul><li><b>နိုင်ငံခြားဧည့်သည်:</b> နိုင်ငံကူးလက်မှတ် မူရင်း။ <b>ဗီယက်နမ်ဧည့်သည်:</b> CCCD။</li><li>ငွေသားအာမခံ မလို။ ဆိုင်ကယ်တိုင်း တစ်ရက် 150,000 VND၊ ဈေးနှုန်းပုံသေ။</li><li>ခဏ စမ်းစီးပြီး ဆိုင်ကယ်အခြေအနေကို အတူ ဗီဒီယိုရိုက်သည်။</li><li>ဦးထုပ်နှင့် ဖုန်းကိုင်တိုင် ပါဝင်သည်၊ နေ့တိုင်း မနက် 4:30 မှ ဖွင့်သည်။</li></ul><p>အသေးစိတ်: <a href=\"{DOCS}\">ဒါလတ်တွင် ဆိုင်ကယ်ငှားရန် လိုအပ်သည်များ</a>။</p>"),
 ],
 "faq_h": "မေးလေ့ရှိသော မေးခွန်းများ",
 "faq": [
  ("ဗီယက်နမ်တွင် လျှပ်စစ်စကူတာအတွက် လိုင်စင်လိုသလား?", "အမြင့်ဆုံးအမြန်နှုန်း 50 km/h အထိနှင့် မော်တာ 4 kW အထိရှိသော လျှပ်စစ်မိုပက်အတွက် လိုင်စင်မလိုပါ။ ကျွန်ုပ်တို့၏ လျှပ်စစ်စကူတာများသည် ဤအမျိုးအစားဖြစ်သည်။ စီးသူသည် အနည်းဆုံး ၁၆ နှစ် ရှိရမည်။"),
  ("လိုင်စင်မပါဘဲ ဒါလတ်တွင် ဓာတ်ဆီစကူတာ ငှားနိုင်သလား?", "ဗီယက်နမ်ဥပဒေသည် Honda Vision နှင့် Air Blade ကဲ့သို့ ဓာတ်ဆီစကူတာများအတွက် တရားဝင်လိုင်စင် လိုအပ်သောကြောင့် Van Phu သည် တရားဝင်လိုင်စင်ရှိသူများကိုသာ ငှားပေးသည်။ လိုင်စင်မရှိပါက လျှပ်စစ်စကူတာကို ရွေးပါ။"),
  ("ကျွန်ုပ်၏ လိုင်စင် ဗီယက်နမ်တွင် တရားဝင်သလား?", "ဗီယက်နမ်ဥပဒေအရ တရားဝင်သော လိုင်စင်ကိုသာ လက်ခံသည်။ စည်းကမ်းများသည် လိုင်စင်ထုတ်ပေးသည့် နိုင်ငံပေါ် မူတည်သောကြောင့် ခရီးမထွက်မီ စစ်ဆေးပါ။ မသေချာပါက လျှပ်စစ်စကူတာ ငှားပါ။"),
  ("ဒါလတ်ကို လည်ပတ်ရန် လျှပ်စစ်စကူတာ လုံလောက်သလား?", "မြို့ထဲနှင့် အနီးရှိနေရာများအတွက် လုံလောက်သည်။ ဘက်ထရီတစ်လုံး 25–30 km ခန့်၊ စကူတာတစ်စီးလျှင် ဘက်ထရီ ၂ လုံး (စုစုပေါင်း 50–60 km ခန့်) ပါပြီး ဆိုင်တွင် ဘက်ထရီလဲခ 20,000 VND ဖြစ်သည်။ ရှည်လျားမတ်စောက်သော တောင်ကြားများအတွက် 125cc ဓာတ်ဆီစကူတာ ပိုကောင်းသည်။"),
  ("လျှပ်စစ်စကူတာ ပိုသက်သာသလား?", "မဟုတ်ပါ — ဆိုင်ကယ်တိုင်း တစ်ရက် 150,000 VND ဖြစ်ပြီး ဦးထုပ်နှင့် ဖုန်းကိုင်တိုင် ပါဝင်သည်။"),
 ],
 "more_h": "ဆက်ဖတ်ရန်",
 "more": [("{EV}", "ဒါလတ် လျှပ်စစ်စကူတာ ငှားရမ်းခြင်း"), ("{DOCS}", "ဒါလတ်တွင် ဆိုင်ကယ်ငှားရန် လိုအပ်သည်များ"), ("{RULES}", "လျှပ်စစ်စကူတာ ငှားရမ်းခြင်း စည်းကမ်းများ"), ("{HOME}", "ဒါလတ် ဆိုင်ကယ်ငှား — ဆိုင်ကယ်များနှင့် ဈေးနှုန်း")],
}

# Hebrew typography: use gershayim (״) instead of ASCII quotes inside words, so meta attributes stay valid
def _gersh(x):
    if isinstance(x, str): return x.replace('מ"ש', 'מ״ש').replace('ק"מ', 'ק״מ').replace('מ"ק', 'מ״ק').replace('ו"ל', 'ו״ל')
    if isinstance(x, list): return [_gersh(i) for i in x]
    if isinstance(x, tuple): return tuple(_gersh(i) for i in x)
    if isinstance(x, dict): return {k: _gersh(v) for k, v in x.items()}
    return x
T["he"] = _gersh(T["he"])
assert set(T) == set(LANGS), set(LANGS) ^ set(T)
