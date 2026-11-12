"""Short Q&A shown at the end of articles (with FAQPage markup). Answers only restate facts already in the article or on
the rental pages — no new prices, hours or claims. Languages: vi + en for now; FAQ[l][article key] = [(question, answer)].
UPDATED[l][key] = date the article (with its FAQ) was last changed, shown as 'Updated' and used as dateModified."""
FAQ = {
"vi": {
 "weather": [
  ("Đà Lạt mùa nào đẹp nhất?", "Mùa khô từ tháng 12 đến tháng 4 nắng ráo và ổn định nhất, hợp chạy xe đi xa. Tháng 1–2 có mai anh đào nở hồng cả thành phố."),
  ("Mùa mưa Đà Lạt từ tháng mấy?", "Khoảng tháng 5 đến tháng 11. Mưa thường vào nửa sau của ngày, có thể lớn nhưng nhanh tạnh — nên đi xa vào buổi sáng."),
  ("Đi Đà Lạt nên mang theo gì?", "Áo khoác hoặc áo gió cho buổi tối và khi chạy xe, áo mưa, giày kín cho đồi dốc và thác, kem chống nắng."),
 ],
 "getting": [
  ("Từ Nha Trang đi Đà Lạt mất bao lâu?", "Khoảng 135–140 km qua đèo, mất chừng 3,5–4 giờ bằng xe khách hoặc xe limousine."),
  ("Từ Sài Gòn đi Đà Lạt bằng gì?", "Xe giường nằm đêm khoảng 6–8 giờ, hoặc máy bay khoảng 1 giờ tới sân bay Liên Khương, rồi khoảng 30 km vào trung tâm."),
  ("Tới Đà Lạt có cần ra tiệm lấy xe không?", "Không bắt buộc: thuê từ 2 ngày, Văn Phú giao xe miễn phí tới khách sạn ở trung tâm. Chỉ cần nhắn trước ngày tới và tên khách sạn."),
 ],
 "days3": [
  ("Đà Lạt 3 ngày nên đi những đâu?", "Ngày 1 trung tâm (hồ Xuân Hương, Crazy House, ga Đà Lạt, chợ đêm); ngày 2 thác Datanla, cáp treo Trúc Lâm, hồ Tuyền Lâm; ngày 3 bình minh đồi chè Cầu Đất và chùa Linh Phước."),
  ("Ngày nào nên thuê Air Blade?", "Ngày thứ ba đi Cầu Đất nhiều dốc dài — Honda Air Blade 125cc chạy chắc hơn. Ngày 1 trong trung tâm thì xe nào cũng được, kể cả xe máy điện."),
  ("Mùa mưa có đi theo lịch này được không?", "Được, nhưng nên dồn chặng xa vào buổi sáng vì mưa thường đến buổi chiều."),
 ],
 "food": [
  ("Đà Lạt có món gì ngon nên thử?", "Bánh tráng nướng, bánh căn, nem nướng, lẩu gà lá é, sữa đậu nành nóng, kem bơ, dâu tây và trà atiso."),
  ("Ăn bánh tráng nướng ở đâu?", "Buổi tối ở chợ đêm và các con hẻm quanh trung tâm — đây là lúc đồ ăn đường phố nhộn nhịp nhất."),
  ("Ăn ở chỗ đông khách du lịch cần lưu ý gì?", "Hỏi giá trước khi gọi món, và mang áo khoác vì buổi tối Đà Lạt lạnh."),
 ],
 "riding": [
  ("Chạy xe máy ở Đà Lạt cần lưu ý gì nhất?", "Luôn đội mũ bảo hiểm, không uống rượu bia khi lái, đi bên phải và tuân thủ luật giao thông Việt Nam."),
  ("Xuống đèo dốc dài nên phanh thế nào?", "Phanh nhẹ cả hai phanh, không bóp phanh liên tục, và không vượt ở khúc cua."),
  ("Gặp mưa hoặc sương mù thì sao?", "Giảm tốc, bật đèn và đi sát bên phải; mưa lớn thì vào quán cà phê chờ tạnh, tránh chạy đường núi khi trời tối."),
 ],
 "wildsunflower": [
  ("Hoa dã quỳ Đà Lạt nở vào tháng mấy?", "Thường từ cuối tháng 10 đến tháng 12, rộ nhất khoảng giữa tháng 11; thời điểm thay đổi theo mưa mỗi năm."),
  ("Ngắm dã quỳ ở đâu gần Đà Lạt?", "Đường xuống hồ Tuyền Lâm, Trại Mát và chùa Linh Phước, hướng Langbiang – Lạc Dương, và cung đường đi đồi chè Cầu Đất."),
  ("Chụp ảnh dã quỳ cần lưu ý gì?", "Đẹp nhất sáng sớm và chiều muộn; dừng xe hẳn vào lề, không đứng ở khúc cua, không giẫm vườn và không hái hoa."),
 ],
 "waterfalls": [
  ("Thác nào gần trung tâm Đà Lạt nhất?", "Thác Datanla, cách trung tâm khoảng 5–7 km về phía Nam, chạy xe chừng 15 phút."),
  ("Đi thác Datanla và Prenn trong một buổi được không?", "Được — hai thác nằm trên cùng một tuyến đường, rất hợp đi chung một buổi sáng."),
  ("Mùa nào thác nhiều nước nhất?", "Mùa mưa, khoảng tháng 5 đến tháng 10–11: thác lớn nhất nhưng nước đục và đường trơn. Mùa khô nước trong hơn, đường khô."),
 ],
 "evrules": [
  ("Thuê xe máy điện cần cọc không?", "Không cọc tiền mặt — bạn để lại hộ chiếu hoặc CCCD bản gốc và nhận lại khi trả xe đúng tình trạng."),
  ("Pin xe máy điện đi được bao xa?", "Một pin đi khoảng 25–30 km (mỗi xe có 2 pin, tổng khoảng 50–60 km). Cần thêm thì mang xe về tiệm đổi pin đầy, 20.000 VND."),
  ("Xe máy điện chở được mấy người?", "Tối đa 2 người, tổng cân nặng dưới 130 kg."),
  ("Trả xe muộn sau 21:00 thì sao?", "Trả sau 21:00 tính thêm một ngày. Muốn gia hạn, hãy nhắn trước cho tiệm."),
 ],
 "caudat": [
  ("Đồi chè Cầu Đất cách Đà Lạt bao xa?", "Khoảng 20–25 km từ trung tâm, chạy xe máy chừng 40–60 phút, lâu hơn khi trời tối."),
  ("Mấy giờ nên xuất phát ngắm bình minh?", "Khoảng 4:30–4:45 từ trung tâm để tới kịp lúc trời hửng sáng, trước khi mặt trời lên."),
  ("Đi Cầu Đất bằng xe máy điện được không?", "Không nên: đi về khoảng 50 km nhiều dốc dài. Xe có 2 pin (khoảng 50–60 km) nhưng công suất thấp, leo dốc chậm và hao pin nhanh. Honda Air Blade 125cc là lựa chọn thoải mái nhất."),
 ],
 "domainedemarie": [
  ("Nhà thờ Domaine de Marie mở cửa mấy giờ?", "Thường 7:30–11:30 và 13:30–17:30 hằng ngày (Google Maps, tháng 10/2026); đóng cửa tham quan trong giờ lễ."),
  ("Vào nhà thờ Domaine de Marie có mất vé không?", "Không, vào cửa miễn phí."),
  ("Đi xe máy điện tới Domaine de Marie được không?", "Được — cách chợ Đà Lạt khoảng 1 km, đoạn cuối lên dốc nhẹ."),
 ],
 "price": [
  ("Thuê xe máy Đà Lạt bao nhiêu tiền một ngày?", "Tại Văn Phú mọi xe — Honda Vision, Air Blade 125cc và xe máy điện — đều 150.000 VND/ngày, giá cố định."),
  ("Có phải đặt cọc tiền mặt không?", "Không. Bạn để lại hộ chiếu hoặc CCCD trong thời gian thuê; tiền thuê trả trước khi nhận xe."),
  ("Giá thuê đã gồm những gì?", "Mũ bảo hiểm, giá đỡ điện thoại, 1 lít xăng cho xe xăng, và giao xe miễn phí tới khách sạn trung tâm khi thuê từ 2 ngày."),
 ],
 "evgas": [
  ("Nên thuê xe máy điện hay xe xăng ở Đà Lạt?", "Đi trong thành phố và quanh gần: xe máy điện êm, dễ đi. Đi đèo, đồi chè Cầu Đất, Langbiang hay các thác xa: chọn xe xăng, tốt nhất là Honda Air Blade 125cc."),
  ("Xe máy điện và xe xăng giá có khác nhau không?", "Không — cả hai đều 150.000 VND/ngày, cùng mũ bảo hiểm và giá đỡ điện thoại miễn phí."),
  ("Xe máy điện đi được bao xa?", "Một pin khoảng 25–30 km (mỗi xe có 2 pin, tổng khoảng 50–60 km); đổi pin tại tiệm 20.000 VND."),
 ],
},
"en": {
 "weather": [
  ("When is the best time to visit Da Lat?", "The dry season, December to April, is the sunniest and most stable — ideal for long rides. In January and February the cherry trees turn the city pink."),
  ("When is the rainy season in Da Lat?", "Roughly May to November. Rain usually falls in the second half of the day, heavy but short — ride the long stretches in the morning."),
  ("What should I pack for Da Lat?", "A jacket or windbreaker for evenings and rides, a raincoat, closed shoes for hills and waterfalls, and sunscreen."),
 ],
 "getting": [
  ("How long is the trip from Nha Trang to Da Lat?", "About 135–140 km over a mountain pass, roughly 3.5–4 hours by bus or limousine van."),
  ("How do I get from Ho Chi Minh City to Da Lat?", "An overnight sleeper bus takes about 6–8 hours, or fly about an hour to Lien Khuong Airport, then about 30 km to the centre."),
  ("Do I have to come to the shop to pick up the bike?", "No: for rentals of 2 days or more we deliver the bike free to hotels in central Da Lat. Just send your arrival date and hotel name."),
 ],
 "days3": [
  ("What should I see in Da Lat in 3 days?", "Day 1 the centre (Xuan Huong Lake, Crazy House, the railway station, the night market); day 2 Datanla Waterfall, the Truc Lam cable car and Tuyen Lam Lake; day 3 sunrise at the Cau Dat tea hills and Linh Phuoc Pagoda."),
  ("Which day needs the Air Blade?", "Day 3 to Cau Dat has long climbs — the Honda Air Blade 125cc is more confident. Any bike works for day 1 in the centre, including an electric scooter."),
  ("Does this plan work in the rainy season?", "Yes, but do the long rides in the morning, because rain usually comes in the afternoon."),
 ],
 "food": [
  ("What food should I try in Da Lat?", "Bánh tráng nướng, bánh căn, nem nướng, lẩu gà lá é, hot soy milk, avocado ice cream, strawberries and artichoke tea."),
  ("Where can I eat bánh tráng nướng?", "In the evening at the night market and in the lanes around the centre — the best time for street food."),
  ("Any tips for eating in touristy spots?", "Check prices before ordering, and bring a jacket — Da Lat evenings are cool."),
 ],
 "riding": [
  ("What are the key rules for riding in Vietnam?", "Always wear a helmet, no alcohol when riding, keep to the right and follow Vietnamese traffic law."),
  ("How should I brake on long descents?", "Brake gently with both brakes, don't hold them on constantly, and never overtake on bends."),
  ("What if it rains or gets foggy?", "Slow down, turn on your lights and keep right; in a downpour wait in a café, and avoid mountain roads after dark."),
 ],
 "wildsunflower": [
  ("When do wild sunflowers bloom in Da Lat?", "Usually late October to December, fullest around mid-November; the timing shifts a little each year with the rain."),
  ("Where can I see wild sunflowers near Da Lat?", "On the road to Tuyen Lam Lake, around Trai Mat and Linh Phuoc Pagoda, towards Lang Biang and Lac Duong, and on the road to the Cau Dat tea hills."),
  ("Any photo tips?", "Shoot early morning or late afternoon; pull fully off the road, never stop on a bend, don't trample farms and don't pick the flowers."),
 ],
 "waterfalls": [
  ("Which waterfall is closest to central Da Lat?", "Datanla, about 5–7 km south of the centre — roughly a 15-minute ride."),
  ("Can I see Datanla and Prenn in one morning?", "Yes — both are on the same road, so they fit easily into one morning."),
  ("When do the falls have the most water?", "In the rainy season, roughly May to October–November: biggest flow, but brown water and slippery paths. In the dry season the water is clearer and the roads are dry."),
 ],
 "evrules": [
  ("Is there a deposit for an electric scooter?", "No cash deposit — you leave your original passport or ID card and get it back when you return the scooter in the same condition."),
  ("How far does one battery go?", "About 25–30 km (each bike comes with 2 batteries, about 50–60 km in total). Need more? Bring the scooter to our shop for a full battery, 20,000 VND."),
  ("How many people can ride an electric scooter?", "Maximum 2 people, with a combined weight under 130 kg."),
  ("What if I return the scooter after 21:00?", "Returning after 21:00 counts as one extra day. To extend, message us first."),
 ],
 "caudat": [
  ("How far are the Cau Dat tea hills from Da Lat?", "About 20–25 km from the centre, roughly 40–60 minutes by scooter, a little longer in the dark."),
  ("What time should I leave for sunrise?", "Around 4:30–4:45 from the centre, to arrive in the soft light before the sun comes up."),
  ("Can I ride there on an electric scooter?", "Not recommended: the round trip is about 50 km with long climbs. The scooter has 2 batteries (about 50–60 km), but its low power makes climbs slow and drains the batteries fast. The Honda Air Blade 125cc is the most comfortable choice."),
 ],
 "domainedemarie": [
  ("What are Domaine de Marie's opening hours?", "Usually 7:30–11:30 and 13:30–17:30 every day (Google Maps, October 2026); closed to sightseeing during Mass."),
  ("Is Domaine de Marie free to enter?", "Yes, entry is free."),
  ("Can I ride there on an electric scooter?", "Yes — it's about 1 km from Da Lat Market, with a gentle climb at the end."),
 ],
 "price": [
  ("How much is motorbike rental in Da Lat per day?", "At Van Phu every bike — Honda Vision, Air Blade 125cc and electric scooters — costs 150,000 VND per day, a fixed price."),
  ("Do I need to leave a cash deposit?", "No. You leave your passport or ID card during the rental; the rental fee is paid upfront."),
  ("What is included in the price?", "A helmet, a phone holder, 1 liter of fuel for gas scooters, and free delivery to central hotels for rentals of 2 days or more."),
 ],
 "evgas": [
  ("Should I rent an electric or a gas scooter in Da Lat?", "For the city and short trips, an electric scooter is quiet and easy. For passes, the Cau Dat tea hills, Lang Biang or far waterfalls, take a gas scooter — best the Honda Air Blade 125cc."),
  ("Is there a price difference?", "No — both cost 150,000 VND per day, with a helmet included and phone holder."),
  ("How far does an electric scooter go?", "About 25–30 km (each bike comes with 2 batteries, about 50–60 km in total) per battery; a battery swap at our shop costs 20,000 VND."),
 ],
},
}
H = {"vi": "Câu hỏi thường gặp", "en": "Frequently asked questions"}
from content import artfaq_tr1 as _t1, artfaq_tr2 as _t2, artfaq_tr3 as _t3, artfaq_tr4 as _t4
for _m in (_t1, _t2, _t3, _t4):
    FAQ.update(_m.FAQ); H.update(_m.H)
for _l in FAQ:
    assert list(FAQ[_l]) == list(FAQ["en"]), _l
UPDATED = {l: {k: "2026-10-15" for k in FAQ[l]} for l in FAQ}

# 2026-10-16: owner's real photos added to these articles (content/photos.py)
for _l in ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he", "it", "nl", "km", "lo", "my"]:
    for _k in ["weather", "getting", "days3", "food", "riding", "wildsunflower", "waterfalls", "evrules", "caudat", "cloudhunt", "lt-nodeposit"]:
        UPDATED.setdefault(_l, {})[_k] = "2026-10-16"
