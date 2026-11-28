"""Guide articles (Vietnamese and English) for Văn Phú. Facts come from the shop's own rules (owner-confirmed, Oct 2026):
price 150,000 VND/day for every bike; no cash deposit (CCCD or passport is held); no rental insurance offered;
helmet included; (owner 2026-11-28: never mention driving licences on the site — guests ask by message);
bike handed over with 1 litre of fuel; electric: about 50–60 km per full charge (varies with road and rider),
battery swap 20,000 VND, max load 130 kg; shop opens 4:30 AM; rental day ends 21:00; delivery to city-centre hotels free for 2+ days.
Anything not listed here is intentionally left out. Rental insurance is not mentioned on purpose: the owner asked not to write about it."""

GUIDES = {
 "vi": [
  {"slug": "giay-to-thue-xe-may-da-lat/",
   "title": "Thuê xe máy Đà Lạt cần giấy tờ gì? Cọc và quy định | Văn Phú",
   "desc": "Thuê xe máy Đà Lạt cần giấy tờ gì: không cọc tiền, chỉ giữ CCCD hoặc hộ chiếu. Giá 150.000 VND/ngày.",
   "h1": "Thuê xe máy Đà Lạt cần giấy tờ gì?",
   "lead": "Trước khi đặt xe, bạn nên biết rõ giấy tờ nào cần mang theo, tiền cọc và những điều Văn Phú không cung cấp. Mọi thông tin dưới đây áp dụng cho tất cả xe tại tiệm.",
   "sections": [
     ("Có phải đặt cọc tiền không?", "<p>Không. Văn Phú <b>không giữ tiền cọc</b>. Chúng tôi chỉ giữ CCCD hoặc hộ chiếu trong thời gian thuê và trả lại khi bạn trả xe.</p>"),
     ("Thanh toán và tính tiền thế nào?", "<ul><li>Giá <b>150.000 VND/ngày</b> cho mọi xe máy, bao gồm xe ga và xe điện.</li><li>Thanh toán khi nhận xe.</li><li>Ngày thuê tính đến <b>21:00</b> cùng ngày. Trả xe sau 21:00 hôm sau sẽ tính thành 2 ngày.</li><li>Xe được giao sẵn 1 lít xăng và có mũ bảo hiểm, giá đỡ điện thoại.</li></ul>"),
     ("Giao xe tận nơi có tốn phí không?", "<p>Không tốn phí khi thuê từ 2 ngày, Văn Phú giao xe miễn phí tới khách sạn hoặc homestay khu trung tâm Đà Lạt. Thuê 1 ngày, bạn ghé tiệm tại 1/15/5 Thông Thiên Học, tiệm mở cửa từ 4:30 sáng.</p>"),
   ],
   "faq": [
     ("Quên mang CCCD thì sao?", "Hãy liên hệ tiệm trước khi đến để được hướng dẫn. Văn Phú giữ CCCD hoặc hộ chiếu trong thời gian thuê để đảm bảo xe được trả lại."),
   ]},
  {"slug": "lai-xe-may-len-da-lat-an-toan/",
   "title": "Lái xe máy lên Đà Lạt: lưu ý an toàn cho người mới | Văn Phú",
   "desc": "Lưu ý an toàn khi lái xe máy ở Đà Lạt: đèo dốc, sương mù buổi sáng, đường trơn sau mưa, áo ấm và cách chạy thử xe trước khi đi.",
   "h1": "Lái xe máy ở Đà Lạt: lưu ý an toàn",
   "lead": "Đà Lạt có nhiều đèo dốc, khúc cua và sương mù buổi sáng. Vài thói quen đơn giản sẽ giúp chuyến đi an toàn và thoải mái hơn.",
   "sections": [
     ("Đi chậm ở đèo và khúc cua", "<p>Đường đèo quanh co, nên giữ tốc độ vừa phải và giữ khoảng cách với xe phía trước. Khi xuống dốc, giảm ga và dùng phanh đều, không để phanh gấp khi đang nghiêng xe.</p>"),
     ("Sương mù buổi sáng và đường trơn", "<p>Sương mù thường xuất hiện sớm, nhất là mùa mưa. Hãy bật đèn, giảm tốc và cẩn thận ở các đoạn đường ướt, vì mặt đường trơn hơn bình thường sau cơn mưa.</p>"),
     ("Mặc đồ ấm", "<p>Đà Lạt lạnh hơn các thành phố dưới đồng bằng, đặc biệt buổi sáng và buổi tối. Hãy mang áo khoác, vì đi xe gió lạnh còn cảm giác rét hơn.</p>"),
     ("Chạy thử xe trước khi đi", "<p>Trước khi nhận xe, hãy chạy thử vài vòng quanh tiệm để quen phanh, ga và đèn. Nếu thấy xe có vấn đề, báo ngay cho nhân viên tại tiệm trước khi rời đi.</p>"),
     ("Không uống rượu bia khi lái", "<p>Không uống rượu bia trước và trong khi lái xe. Đây là điều luật giao thông bắt buộc và cũng là điều quan trọng nhất để giữ an toàn cho bạn và người khác.</p>"),
     ("Khi cần hỗ trợ", "<p>Nếu gặp sự cố trên đường, hãy gọi tiệm theo số <b>0944 081 101</b> để được hướng dẫn.</p>"),
   ],
   "faq": [
     ("Người mới lái xe có nên thuê xe điện không?", "Có thể. Xe điện êm, vặn ga là chạy, phù hợp để đi trong thành phố. Nếu đi nhiều đoạn đèo, bạn nên cân nhắc xe ga 125cc."),
     ("Có nên đi lên đèo khi trời mưa không?", "Nên hạn chế. Đường trơn và sương mù làm việc đi lại nguy hiểm hơn, nên chỉ đi khi thật cần thiết và giảm tốc độ rõ rệt."),
   ]},
  {"slug": "xe-dien-hay-xe-ga-da-lat/",
   "title": "Thuê xe điện hay xe ga ở Đà Lạt? So sánh để chọn đúng xe | Văn Phú",
   "desc": "So sánh xe điện và xe ga khi thuê ở Đà Lạt: quãng đường, sạc pin, tải trọng và nên chọn loại nào cho chuyến đi của bạn.",
   "h1": "Thuê xe điện hay xe ga ở Đà Lạt?",
   "lead": "Xe điện và xe ga đều có ưu và nhược điểm riêng. Bài này giúp bạn chọn đúng loại xe theo nhu cầu, không cần đoán.",
   "sections": [
     ("So sánh nhanh", "<ul><li><b>Quãng đường:</b> xe điện ước tính khoảng 50–60 km mỗi lần sạc đầy, tùy đường đi và cách lái; xe ga chạy được xa hơn trong một lần đổ xăng.</li><li><b>Sạc và đổi pin:</b> xe điện đổi pin tại tiệm với giá 20.000 VND mỗi lần.</li><li><b>Tải trọng:</b> xe điện tải tối đa 130 kg.</li><li><b>Tiếng ồn và độ êm:</b> xe điện êm và ít tiếng ồn hơn.</li></ul>"),
     ("Chọn xe điện khi nào?", "<p>Xe điện phù hợp nếu bạn đi chủ yếu trong thành phố, cà phê, chợ đêm hoặc muốn một chuyến đi yên tĩnh.</p>"),
     ("Chọn xe ga khi nào?", "<p>Xe ga phù hợp nếu bạn định đi xa trong ngày, lên đèo nhiều, hoặc muốn không phải lo về pin. Honda Air Blade 125cc có động cơ lớn hơn Honda Vision 110cc, nên thoải mái hơn trên đường dốc.</p>"),
     ("Lưu ý khi chọn", "<p>Dù chọn loại nào, bạn cũng nên cân nhắc tải trọng và lộ trình. Nếu chưa chắc, hãy nhắn tiệm kèm lịch trình để được tư vấn.</p>"),
   ],
   "faq": [
     ("Xe điện đi được bao xa trong một lần sạc?", "Ước tính khoảng 50–60 km, nhưng quãng đường thực tế phụ thuộc vào đường đi, tải trọng và cách lái. Nếu cần đi xa hơn, bạn có thể đổi pin tại tiệm với giá 20.000 VND mỗi lần."),
     ("Xe ga và xe điện, loại nào rẻ hơn?", "Giá thuê giống nhau: 150.000 VND/ngày cho cả hai. Khác biệt nằm ở quãng đường và cách sạc pin."),
   ]},
 ],
 "en": [
  {"slug": "motorbike-rental-dalat-documents/",
   "title": "Motorbike Rental in Da Lat: Documents, Deposit & Rules | Van Phu",
   "desc": "What you need to rent a motorbike in Da Lat: no cash deposit, we hold your ID or passport. 150,000 VND/day.",
   "h1": "Motorbike rental in Da Lat: what you need",
   "lead": "Before you book, check which documents to bring, how the deposit works and what we don't include. These rules apply to every bike at our shop.",
   "sections": [
     ("Is there a cash deposit?", "<p>No. Van Phu <b>does not take a cash deposit</b>. We only hold your ID card or passport during the rental and return it when you bring the bike back.</p>"),
     ("How does payment and the rental day work?", "<ul><li>Price: <b>150,000 VND per day</b> for every bike, gas or electric.</li><li>Pay when you pick up the bike.</li><li>A rental day runs until <b>21:00</b> on the same day. Returning after 21:00 the next day counts as 2 days.</li><li>Every bike comes with a helmet, a phone holder and 1 litre of fuel.</li></ul>"),
     ("Is hotel delivery free?", "<p>Yes, for rentals of 2 days or more we deliver free to hotels and homestays in central Da Lat. For a 1-day rental, pick up at our shop at 1/15/5 Thong Thien Hoc Street. We open at 4:30 AM.</p>"),
   ],
   "faq": [
     ("What if I forgot my ID?", "Contact the shop before you come for guidance. We hold your ID or passport during the rental to make sure the bike is returned."),
   ]},
  {"slug": "riding-safely-in-da-lat/",
   "title": "Riding a Motorbike in Da Lat: Safety Tips for Beginners | Van Phu",
   "desc": "Safety tips for riding in Da Lat: hill roads, morning fog, wet roads after rain, warm clothing and how to test-ride your bike before you leave.",
   "h1": "Riding in Da Lat: safety tips",
   "lead": "Da Lat has many hills, sharp bends and morning fog. A few simple habits will make your ride safer and more comfortable.",
   "sections": [
     ("Ride slowly on hills and bends", "<p>Hill roads twist a lot, so keep a moderate speed and a safe distance from the vehicle ahead. Going downhill, ease off the throttle and brake smoothly. Avoid braking hard while leaning into a bend.</p>"),
     ("Morning fog and wet roads", "<p>Fog often appears early in the morning, especially in the rainy season. Turn on your lights, slow down, and take extra care on wet roads, which are more slippery after rain.</p>"),
     ("Dress warmly", "<p>Da Lat is cooler than the lowland cities, especially in the morning and evening. Bring a jacket, because the wind on a bike makes it feel colder.</p>"),
     ("Test-ride before you leave", "<p>Before you take the bike, ride a few laps around the shop to get used to the brakes, throttle and lights. If something seems wrong, tell the staff before you leave.</p>"),
     ("Never ride after drinking", "<p>Do not drink alcohol or beer before or while riding. It is required by traffic law and is the most important way to keep yourself and others safe.</p>"),
     ("If you need help", "<p>If something goes wrong on the road, call the shop on <b>0944 081 101</b> for guidance.</p>"),
   ],
   "faq": [
     ("Should a beginner rent an electric scooter?", "It can be a good choice. Electric scooters are quiet and easy to ride, which suits city riding. For many hill roads, consider the 125cc gas scooter instead."),
     ("Should I ride up the hills when it is raining?", "Better not. Wet roads and fog make riding more dangerous, so only ride when necessary and slow down clearly."),
   ]},
  {"slug": "electric-or-gas-scooter-da-lat/",
   "title": "Electric or Gas Scooter in Da Lat? How to Choose | Van Phu",
   "desc": "Compare electric and gas scooters in Da Lat: range per charge, battery swap, load limit and which one suits your trip.",
   "h1": "Electric or gas scooter in Da Lat?",
   "lead": "Electric and gas scooters both have pros and cons. This guide helps you choose the right bike for your plans.",
   "sections": [
     ("Quick comparison", "<ul><li><b>Range:</b> electric scooters are estimated at about 50–60 km per full charge, depending on the road and riding style. Gas scooters go further on one tank.</li><li><b>Charging and battery swap:</b> swap the battery at the shop for 20,000 VND each time.</li><li><b>Load limit:</b> electric scooters carry up to 130 kg.</li><li><b>Noise:</b> electric scooters are quieter and smoother.</li></ul>"),
     ("When to choose electric", "<p>Pick an electric scooter if you mostly ride around town, go to cafés and the night market or want a quiet ride.</p>"),
     ("When to choose gas", "<p>Pick a gas scooter if you plan longer rides in the day, go up many hills, or don't want to think about battery range. The 125cc Honda Air Blade has a larger engine than the 110cc Honda Vision, so it feels more comfortable on climbs.</p>"),
     ("Tip", "<p>Whichever you choose, check your load and your route. If you're not sure, message the shop with your plans and we'll advise you.</p>"),
   ],
   "faq": [
     ("How far can an electric scooter go on one charge?", "About 50–60 km, but the real distance depends on the road, the load and how you ride. If you need more, swap the battery at the shop for 20,000 VND each time."),
     ("Is an electric or gas scooter cheaper?", "Both cost 150,000 VND per day. The differences are range and how you recharge."),
   ]},
 ],
}
