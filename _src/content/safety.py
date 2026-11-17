"""Riding-safety block for the motorbike rental home page, per language.
Facts used: helmet included with every bike and required by Vietnamese law; electric scooters not ridden in rain;
emergency numbers 113 police, 114 fire, 115 ambulance; no rental insurance offered by Van Phu Dalat."""
SAFETY = {
 "en": ("Riding safety in Da Lat", [
   ("Wear a helmet.", "Every bike comes with one, and Vietnamese law requires it."),
   ("Electric scooters: not in rain.", "Do not ride electric scooters in the rain. Ask us for a 110cc gas scooter instead."),
   ("Emergency numbers.", "113 police · 114 fire · 115 ambulance."),
   ("Insurance.", "We do not offer rental insurance. Check your own travel insurance before you ride.")]),
 "vi": ("An toàn khi đi xe ở Đà Lạt", [
   ("Đội mũ bảo hiểm.", "Mỗi xe đều có mũ, và luật giao thông Việt Nam bắt buộc đội mũ."),
   ("Xe điện: không chạy khi mưa.", "Không chạy xe điện khi trời mưa. Hãy chọn xe ga 110cc thay thế."),
   ("Số khẩn cấp.", "113 công an · 114 cứu hỏa · 115 cấp cứu."),
   ("Bảo hiểm.", "Văn Phú Đà Lạt không cung cấp bảo hiểm thuê xe. Hãy kiểm tra bảo hiểm du lịch của bạn trước khi đi.")]),
 "ko": ("달랏 안전 운전 안내", [
   ("헬멧 착용.", "모든 차량에 헬멧이 제공되며, 베트남 법규상 착용이 의무입니다."),
   ("전기 스쿠터는 비 오는 날 금지.", "비 오는 날에는 전기 스쿠터를 운행하지 마세요. 대신 110cc 가솔린 스쿠터를 요청하세요."),
   ("긴급 전화.", "경찰 113 · 소방 114 · 구급차 115"),
   ("보험.", "당사는 대여 보험을 제공하지 않습니다. 운전 전 여행자 보험을 확인해 주세요.")]),
 "zh": ("大叻骑行安全提示", [
   ("请戴头盔。", "每辆车都配有头盔，越南法律要求佩戴。"),
   ("电动车雨天不骑。", "雨天请勿骑电动车。可以改租110cc汽油车。"),
   ("紧急电话。", "警察 113 · 消防 114 · 急救 115"),
   ("保险。", "我们不提供租车保险。出发前请确认您自己的旅游保险。")]),
 "ja": ("ダラットでの安全運転", [
   ("ヘルメットを着用。", "全ての車両にヘルメットを用意しています。ベトナムの法律で着用が義務付けられています。"),
   ("雨の日は電動スクーターに乗らない。", "雨の日は電動スクーターの運転をお控えください。110ccのガソリンスクーターに変更できます。"),
   ("緊急連絡先。", "警察 113 · 消防 114 · 救急 115"),
   ("保険。", "レンタル保険は提供していません。走行前にご自身の旅行保険をご確認ください。")]),
 "th": ("ความปลอดภัยในการขับขี่ในดาลัต", [
   ("สวมหมวกกันน็อก.", "ทุกคันมีหมวกให้ และกฎหมายเวียดนามกำหนดให้สวม"),
   ("สกู๊ตเตอร์ไฟฟ้า: ไม่ขับเมื่อฝนตก.", "ไม่ควรขับสกู๊ตเตอร์ไฟฟ้าขณะฝนตก สามารถขอเปลี่ยนเป็นสกู๊ตเตอร์น้ำมัน 110cc ได้"),
   ("เบอร์ฉุกเฉิน.", "ตำรวจ 113 · ดับเพลิง 114 · รถพยาบาล 115"),
   ("ประกันภัย.", "เราไม่มีบริการประกันการเช่ารถ โปรดตรวจสอบประกันการเดินทางของคุณก่อนขับ")]),
 "id": ("Keselamatan berkendara di Da Lat", [
   ("Pakai helm.", "Setiap motor dilengkapi helm, dan hukum Vietnam mewajibkannya."),
   ("Skuter listrik: jangan saat hujan.", "Jangan mengendarai skuter listrik saat hujan. Anda bisa minta skuter bensin 110cc sebagai gantinya."),
   ("Nomor darurat.", "Polisi 113 · Pemadam kebakaran 114 · Ambulans 115"),
   ("Asuransi.", "Kami tidak menyediakan asuransi sewa. Periksa asuransi perjalanan Anda sebelum berkendara.")]),
 "ms": ("Keselamatan menunggang di Da Lat", [
   ("Pakai topi keledar.", "Setiap motosikal disediakan topi keledar, dan undang-undang Vietnam mewajibkannya."),
   ("Skuter elektrik: jangan semasa hujan.", "Jangan menunggang skuter elektrik semasa hujan. Anda boleh minta skuter gas 110cc sebagai gantian."),
   ("Nombor kecemasan.", "Polis 113 · Bomba 114 · Ambulans 115"),
   ("Insurans.", "Kami tidak menawarkan insurans sewaan. Semak insurans perjalanan anda sebelum menunggang.")]),
 "ru": ("Безопасность на дороге в Далате", [
   ("Шлем обязателен.", "Шлем есть на каждом байке, и этого требует вьетнамский закон."),
   ("Электроскутер: не в дождь.", "Не ездите на электроскутере под дождём. Можно взять бензиновый скутер 110cc."),
   ("Экстренные номера.", "Полиция 113 · Пожарные 114 · Скорая помощь 115"),
   ("Страховка.", "Страхование аренды мы не предоставляем. Проверьте свою туристическую страховку перед поездкой.")]),
}

# Standalone safety guide page: one page per priority language.
SAFETY_SLUG = {"en": "riding-safety-da-lat", "vi": "an-toan-khi-di-xe-da-lat", "ko": "dalat-anjeon-undong-annae",
               "zh": "dalat-qixing-anquan", "ja": "dalat-anzen-unten", "th": "khwam-plodphai-dalat",
               "id": "keselamatan-berkendara-dalat", "ms": "keselamatan-menunggang-dalat", "ru": "bezopasnost-dalat"}
SAFETY_PAGE = {
 "en": dict(title="Riding Safety in Da Lat | Van Phu Dalat", desc="Riding safety tips for scooters and motorbikes in Da Lat: helmets, rain, emergency numbers and insurance.", h1="Riding safety in Da Lat", lead="The short rules we give every guest before they ride.", cta="Rent a scooter"),
 "vi": dict(title="An toàn khi đi xe ở Đà Lạt | Văn Phú Đà Lạt", desc="Lưu ý an toàn khi đi xe máy, xe điện ở Đà Lạt: mũ bảo hiểm, trời mưa, số khẩn cấp và bảo hiểm.", h1="An toàn khi đi xe ở Đà Lạt", lead="Những lưu ý ngắn gọn chúng tôi nói với mọi khách trước khi xuất phát.", cta="Thuê xe ngay"),
 "ko": dict(title="달랏 안전 운전 가이드 | 반푸 달랏", desc="달랏에서 스쿠터와 오토바이를 탈 때의 안전 수칙: 헬멧, 비 오는 날, 긴급 전화, 보험.", h1="달랏 안전 운전 안내", lead="모든 고객이 출발 전에 듣는 짧은 안내입니다.", cta="스쿠터 대여하기"),
 "zh": dict(title="大叻骑行安全指南 | Văn Phú Đà Lạt", desc="在大叻骑摩托车或电动车的安全提示：头盔、雨天、紧急电话和保险。", h1="大叻骑行安全提示", lead="每位客人出发前我们都会说明的简单规则。", cta="立即租车"),
 "ja": dict(title="ダラットの安全運転ガイド | Văn Phú Đà Lạt", desc="ダラットでスクーターやバイクに乗る際の安全のポイント：ヘルメット、雨の日、緊急連絡先、保険。", h1="ダラットでの安全運転", lead="出発前に全てのお客様にお伝えしている簡単なルールです。", cta="スクーターを借りる"),
 "th": dict(title="ความปลอดภัยในการขับขี่ในดาลัต | Văn Phú Đà Lạt", desc="เคล็ดลับความปลอดภัยสำหรับการขับสกู๊ตเตอร์หรือมอเตอร์ไซค์ในดาลัต: หมวกกันน็อก ฝนตก เบอร์ฉุกเฉิน และประกัน", h1="ความปลอดภัยในการขับขี่ในดาลัต", lead="กฎสั้นๆ ที่เราแจ้งลูกค้าทุกคนก่อนขับ", cta="เช่าสกู๊ตเตอร์"),
 "id": dict(title="Keselamatan Berkendara di Da Lat | Văn Phú Đà Lạt", desc="Tips keselamatan naik skuter atau motor di Da Lat: helm, hujan, nomor darurat, dan asuransi.", h1="Keselamatan berkendara di Da Lat", lead="Aturan singkat yang kami sampaikan kepada setiap tamu sebelum berkendara.", cta="Sewa skuter"),
 "ms": dict(title="Keselamatan Menunggang di Da Lat | Văn Phú Đà Lạt", desc="Tip keselamatan menunggang skuter atau motosikal di Da Lat: topi keledar, hujan, nombor kecemasan dan insurans.", h1="Keselamatan menunggang di Da Lat", lead="Peraturan ringkas yang kami beritahu kepada setiap tetamu sebelum menunggang.", cta="Sewa skuter"),
 "ru": dict(title="Безопасность на дороге в Далате | Văn Phú Đà Lạt", desc="Советы по безопасности при езде на скутере или мотоцикле в Далате: шлем, дождь, экстренные номера и страховка.", h1="Безопасность на дороге в Далате", lead="Короткие правила, которые мы объясняем каждому гостю перед поездкой.", cta="Арендовать скутер"),
}
