"""Villa Đà Lạt page (owner asked 2026-11-04): embeds the whole TikTok channel @bietthudalat (official TikTok creator embed,
auto-updates when a new clip is posted) + booking by message. Focus languages only.
Owner rules: no prices here, no licence wording; villa booking is by message (Zalo / WhatsApp / Telegram / WeChat), no online payment."""

LANGS = ["vi", "en", "zh", "ru", "ko", "id"]
UPDATED = "2026-11-04"
# TikTok clip links to show one by one (owner adds them). The whole-channel embed was dropped 2026-11-04: TikTok's server
# answered "overload-protect triggered" inside the frame. Single-video embeds are TikTok's stable embed type.
VIDEOS = [
    "https://www.tiktok.com/@bietthudalat/video/7571084141525994759",
    "https://www.tiktok.com/@bietthudalat/video/7505023658906307847",
    "https://www.tiktok.com/@bietthudalat/video/7429951407928691976",
    "https://www.tiktok.com/@bietthudalat/video/7358784531450678545",
    "https://www.tiktok.com/@bietthudalat/video/7343552631505292546",
]  # e.g. "https://www.tiktok.com/@bietthudalat/video/7400000000000000000"
SLUG = {"vi": "vi/villa-da-lat/", "en": "villa-da-lat/", "zh": "zh/villa/", "ru": "ru/villa/", "ko": "ko/villa/", "id": "id/villa/"}

T = {
 "vi": {
  "title": "Villa Đà Lạt – Xem clip thực tế trên TikTok, đặt qua Văn Phú",
  "desc": "Xem clip thực tế các căn villa, homestay Đà Lạt trên kênh TikTok @bietthudalat của Văn Phú Đà Lạt, chọn căn ưng ý rồi nhắn Zalo để đặt.",
  "crumb": "Villa Đà Lạt", "h1": "Villa Đà Lạt – xem clip thực tế",
  "lead": "Các căn villa, homestay Đà Lạt được quay thực tế trên kênh TikTok <b>@bietthudalat</b>. Xem phòng, sân vườn, view rồi nhắn tôi để đặt.",
  "h_how": "Đặt villa thế nào?",
  "how": ["Xem clip bên dưới, chọn căn bạn thích.", "Nhắn tôi tên căn (hoặc gửi link clip), ngày nhận – trả phòng và số khách.",
          "Tôi kiểm tra lịch trống, báo giá và giữ phòng cho bạn."],
  "h_clips": "Clip villa trên TikTok", "fallback": "Không xem được clip? Mở kênh TikTok @bietthudalat →",
  "h_book": "Nhắn để đặt villa", "book_txt": "Gửi tên căn, ngày nhận – trả phòng và số khách. Có thể đặt kèm thuê xe máy giao tận villa.",
  "msg": "Chào Văn Phú, mình muốn đặt villa Đà Lạt. Căn: ... Ngày nhận – trả: ... Số khách: ...",
  "btn": "💬 Nhắn Zalo đặt villa",
  "link_about": "Đặt homestay, villa – xem clip", "foot": "Villa Đà Lạt",
 },
 "en": {
  "title": "Da Lat Villas – Real Video Tours on TikTok, Book with Van Phu",
  "desc": "Watch real video tours of Da Lat villas and homestays on Van Phu Dalat's TikTok channel @bietthudalat, pick one you like and message us to book.",
  "crumb": "Da Lat villas", "h1": "Da Lat villas – real video tours",
  "lead": "Real walk-through clips of Da Lat villas and homestays on our TikTok channel <b>@bietthudalat</b>. See the rooms, gardens and views, then message me to book.",
  "h_how": "How to book a villa",
  "how": ["Watch the clips below and pick the place you like.", "Message me the villa name (or the clip link), your check-in and check-out dates and number of guests.",
          "I check availability, send you the price and hold the villa for you."],
  "h_clips": "Villa clips on TikTok", "fallback": "Clips not loading? Open the TikTok channel @bietthudalat →",
  "h_book": "Message to book a villa", "book_txt": "Send the villa name, dates and number of guests. You can add a scooter delivered to the villa.",
  "msg": "Hi Van Phu, I'd like to book a villa in Da Lat. Villa: ... Dates: ... Guests: ...",
  "btn": "💬 WhatsApp to book",
  "link_about": "Villa booking – watch the clips", "foot": "Da Lat villas",
 },
 "zh": {
  "title": "大叻别墅 – TikTok实拍视频，通过Van Phu预订",
  "desc": "在Van Phu大叻的TikTok频道@bietthudalat观看大叻别墅、民宿实拍视频，选好后发消息预订。",
  "crumb": "大叻别墅", "h1": "大叻别墅 – 实拍视频",
  "lead": "TikTok频道 <b>@bietthudalat</b> 实拍大叻别墅和民宿：房间、花园、景观一目了然，选好后联系我预订。",
  "h_how": "如何预订别墅",
  "how": ["观看下面的视频，选择喜欢的房源。", "发给我房源名称（或视频链接）、入住和退房日期、人数。", "我查询空房、报价并为您保留。"],
  "h_clips": "TikTok别墅视频", "fallback": "视频无法加载？打开TikTok频道 @bietthudalat →",
  "h_book": "发消息预订别墅", "book_txt": "请发送房源名称、日期和人数。也可加订摩托车，送到别墅。",
  "msg": "", "btn": "微信: vanphudalat",
  "link_about": "预订民宿、别墅 – 看视频", "foot": "大叻别墅",
 },
 "ru": {
  "title": "Виллы в Далате – видеообзоры в TikTok, бронирование через Van Phu",
  "desc": "Смотрите реальные видеообзоры вилл и гестхаусов Далата в TikTok-канале @bietthudalat от Van Phu Dalat, выберите подходящую и напишите, чтобы забронировать.",
  "crumb": "Виллы в Далате", "h1": "Виллы в Далате – видеообзоры",
  "lead": "Реальные видеообзоры вилл и гестхаусов Далата в TikTok-канале <b>@bietthudalat</b>: комнаты, сад, вид. Выберите и напишите мне, чтобы забронировать.",
  "h_how": "Как забронировать виллу",
  "how": ["Посмотрите видео ниже и выберите понравившийся вариант.", "Напишите мне название виллы (или ссылку на видео), даты заезда и выезда и количество гостей.",
          "Я проверю свободные даты, сообщу цену и забронирую для вас."],
  "h_clips": "Видео вилл в TikTok", "fallback": "Видео не загружается? Откройте TikTok-канал @bietthudalat →",
  "h_book": "Написать, чтобы забронировать", "book_txt": "Пришлите название виллы, даты и количество гостей. Можно добавить байк с доставкой к вилле.",
  "msg": "", "btn": "💬 Написать в Telegram",
  "link_about": "Бронирование вилл – смотреть видео", "foot": "Виллы в Далате",
 },
 "ko": {
  "title": "달랏 빌라 – TikTok 실제 영상, Van Phu로 예약",
  "desc": "Van Phu Dalat의 TikTok 채널 @bietthudalat에서 달랏 빌라·홈스테이 실제 영상을 보고 마음에 드는 곳을 메시지로 예약하세요.",
  "crumb": "달랏 빌라", "h1": "달랏 빌라 – 실제 영상",
  "lead": "TikTok 채널 <b>@bietthudalat</b>에서 달랏 빌라와 홈스테이를 직접 촬영했습니다. 방, 정원, 전망을 보고 메시지로 예약하세요.",
  "h_how": "빌라 예약 방법",
  "how": ["아래 영상을 보고 마음에 드는 곳을 고르세요.", "빌라 이름(또는 영상 링크), 체크인·체크아웃 날짜, 인원을 보내 주세요.", "빈 날짜를 확인하고 가격을 알려 드린 뒤 예약해 드립니다."],
  "h_clips": "TikTok 빌라 영상", "fallback": "영상이 안 보이나요? TikTok 채널 @bietthudalat 열기 →",
  "h_book": "메시지로 빌라 예약", "book_txt": "빌라 이름, 날짜, 인원을 보내 주세요. 빌라까지 스쿠터 배달도 함께 예약할 수 있습니다.",
  "msg": "Hi Van Phu, I'd like to book a villa in Da Lat. Villa: ... Dates: ... Guests: ...",
  "btn": "💬 WhatsApp으로 예약",
  "link_about": "빌라 예약 – 영상 보기", "foot": "달랏 빌라",
 },
 "id": {
  "title": "Vila di Da Lat – Video Asli di TikTok, Pesan lewat Van Phu",
  "desc": "Tonton video asli vila dan homestay Da Lat di kanal TikTok @bietthudalat milik Van Phu Dalat, pilih yang Anda suka lalu kirim pesan untuk memesan.",
  "crumb": "Vila Da Lat", "h1": "Vila di Da Lat – video asli",
  "lead": "Video asli vila dan homestay Da Lat di kanal TikTok <b>@bietthudalat</b>: kamar, taman dan pemandangan. Pilih lalu kirim pesan ke saya untuk memesan.",
  "h_how": "Cara memesan vila",
  "how": ["Tonton video di bawah dan pilih tempat yang Anda suka.", "Kirim nama vila (atau link video), tanggal check-in dan check-out, serta jumlah tamu.",
          "Saya cek ketersediaan, kirim harga dan menahan vila untuk Anda."],
  "h_clips": "Video vila di TikTok", "fallback": "Video tidak muncul? Buka kanal TikTok @bietthudalat →",
  "h_book": "Kirim pesan untuk memesan", "book_txt": "Kirim nama vila, tanggal dan jumlah tamu. Bisa sekalian sewa skuter yang diantar ke vila.",
  "msg": "Halo Van Phu, saya ingin memesan vila di Da Lat. Vila: ... Tanggal: ... Jumlah tamu: ...",
  "btn": "💬 WhatsApp untuk memesan",
  "link_about": "Pesan vila – tonton video", "foot": "Vila Da Lat",
 },
}

# All clips of @bietthudalat (owner asked 2026-11-04 "lấy hết dữ liệu trên kênh"): read from the channel page on 2026-11-04,
# covers saved in /img/tiktok/<id>.webp. Order = channel order (pinned first). Fields: id, v (views as shown), p (pinned), t (title), c (caption).
import json as _json, pathlib as _pl
CLIPS = _json.loads((_pl.Path(__file__).resolve().parent.parent / "data" / "tiktok.json").read_text(encoding="utf-8"))
UI = {
 "vi": ("Đã ghim", "Xem trên TikTok", "💬 Đặt căn này qua Zalo", "Đóng", "clip"),
 "en": ("Pinned", "Watch on TikTok", "💬 Book this villa on WhatsApp", "Close", "clips"),
 "zh": ("置顶", "在TikTok观看", "微信预订: vanphudalat", "关闭", "个视频"),
 "ru": ("Закреплено", "Смотреть в TikTok", "💬 Забронировать в Telegram", "Закрыть", "видео"),
 "ko": ("고정됨", "TikTok에서 보기", "💬 WhatsApp으로 이 빌라 예약", "닫기", "개 영상"),
 "id": ("Disematkan", "Tonton di TikTok", "💬 Pesan vila ini via WhatsApp", "Tutup", "video"),
}
