"""Indonesian-only page: halal restaurants in Da Lat for Muslim travellers from Indonesia/Malaysia (/id/sewa-motor-dalat/restoran-halal-dalat/).
Places were picked from Google Maps search results (2026-10-27) and kept only when the listing says halal or guests describe halal food.
Ratings and hours are Google Maps values on that date. Văn Phú holds no halal certificate for these restaurants: guests must ask."""

UPDATED = "2026-10-27"
H1 = "Restoran Halal di Dalat (Đà Lạt)"
TITLE = "Restoran Halal di Dalat: Peta Makanan Halal untuk Wisatawan Muslim | Van Phu"
DESC = "Peta restoran halal di Đà Lạt untuk wisatawan Muslim: 5 tempat dengan jam buka, rating Google, arah ke setiap tempat dan tips sebelum makan. Gratis."
LEAD = "Daftar dan peta restoran halal dan makanan halal di Dalat (Đà Lạt) untuk wisatawan Muslim: jam buka, rating Google dan arah ke tiap tempat. Dari tiệm Văn Phú, semua tempat ini bisa dicapai dengan motor."

# name, rating, rating count, lat, lng, Google Maps place_id, hours, what it is, tip
SPOTS = [
    ("Sarah Halal Food", 4.3, 385, 11.9393156, 108.4344752, "ChIJNR7IagATcTERBdYNpK36fEQ", "06:30–22:30 setiap hari",
     "Restoran halal di pusat kota, di jalan utama, sekitar 350 m dari pasar malam. Menu Vietnam halal seperti gỏi cuốn, nasi ayam claypot dan hot pot. Ulasan menyebut staf bisa berbahasa Melayu.",
     "Cocok untuk makan malam setelah dari pasar malam."),
    ("Sagar Indian Cuisine – Halal Food", 4.9, 2827, 11.944323, 108.4348131, "ChIJzZTRb2ITcTERWlGidA6B1Dg", "10:00–22:00 (Selasa 14:30–22:00)",
     "Masakan India halal: biryani, kari, tandoori, samosa dan naan. Rating tertinggi dari antara tempat di daftar ini, dengan lebih dari 2.800 ulasan.",
     "Porsi besar dan cocok untuk makan berdua atau berkelompok."),
    ("Halal Food Dalat Hajah Hawa", 4.4, 220, 11.9382808, 108.439614, "ChIJ6a96xABtcTERFN7c10FhZGc", "07:00–22:00 setiap hari",
     "Hot pot seafood ala Vietnam dan pho daging sapi, dengan ruang makan dua lantai untuk rombongan. Ulasan menyebut ada tempat sholat dan pengunjung bisa mengisi daya ponsel.",
     "Tanyakan tempat sholat saat datang; staf biasanya melayani dalam bahasa Inggris."),
    ("Halal food ISMAEL", 4.3, 110, 11.9408137, 108.418481, "ChIJuXjkyt8TcTERmhAy1h6PfDY", "07:00–20:00 setiap hari",
     "Restoran di Cam Ly dengan bánh mì daging sapi, phở dan nasi goreng, sarapan sampai makan malam. Ulasan menyebut ada ruang sholat untuk Muslim dan parkir motor di depan.",
     "Agak jauh dari pusat, jadi pakai motor atau taksi. Minta cili potong jika suka pedas."),
    ("Halal Restaurant Kampung Melayu", 4.2, 184, 11.9435021, 108.4513805, "ChIJ0yjMS7UTcTERnq3m_tvAhHY", "06:00–21:30 setiap hari",
     "Restoran bergaya Melayu-Malaysia di Yersin, dengan pemilik yang bisa berbahasa Melayu. Ulasan pengunjung terbagi: ada yang puas, ada yang mengeluhkan rasa dan pelayanan.",
     "Baca ulasan terbaru dan coba dulu menu sederhana."),
]

TIPS = [
    "Tanyakan langsung kepada restoran tentang sertifikat halal, bahan dan cara memasak sebelum memesan. Văn Phú tidak memiliki sertifikat halal untuk tempat-tempat ini.",
    "Jika butuh tempat sholat, tanyakan dulu. Ulasan Google menyebut ISMAEL dan Hajah Hawa menyediakannya.",
    "Sarah Halal Food dan Sagar berada di pusat kota dan bisa dijangkau dengan jalan kaki atau motor singkat.",
    "ISMAEL dan Kampung Melayu agak jauh dari pusat, jadi sebaiknya naik motor atau taksi.",
    "Jam buka bisa berubah saat hari raya atau libur. Cek Google Maps sebelum datang.",
]

FAQ = [
    ("Apakah restoran di Đà Lạt ini bersertifikat halal?",
     "Văn Phú tidak memiliki sertifikat halal resmi untuk tempat-tempat ini. Daftar ini dibuat dari Google Maps dan ulasan pengunjung, jadi tanyakan langsung kepada restoran sebelum memesan."),
    ("Restoran halal mana yang paling dekat pusat kota?",
     "Sarah Halal Food dan Sagar Indian Cuisine berada di pusat kota dan sekitar Xuân Hương. ISMAEL dan Kampung Melayu sedikit lebih jauh."),
    ("Bagaimana sampai ke restoran-restoran ini?",
     "Sewa motor di tiệm Văn Phú di 1/15/5 Thông Thiên Học, buka mulai 4:30 pagi. Dari tiệm, semua tempat di daftar ini bisa dicapai dengan motor dalam waktu singkat."),
    ("Apakah ada tempat sholat di dekat restoran?",
     "Ulasan Google menyebut ISMAEL dan Hajah Hawa menyediakan tempat sholat. Tanyakan saat datang karena ini tidak selalu tercantum di Google Maps."),
]

# --- Muslim-traveller insights (added 2026-10-28) ---
PRAYER_H3 = "Tempat Sholat di Dalat (Chỗ Sholat)"
PRAYER = [
    "ISMAEL (Cam Ly): ulasan Google menyebut ada ruang sholat untuk Muslim. Parkir motor tersedia tepat di depan.",
    "Halal Food Dalat Hajah Hawa: ulasan menyebut ada tempat sholat, dan staf membantu pengunjung mengisi daya HP.",
    "Restoran lain di daftar ini: belum ada informasi pasti tentang tempat sholat. Tanyakan dulu saat datang.",
    "Kami belum punya daftar masjid yang sudah diverifikasi di Đà Lạt. Jika butuh tempat sholat saat sedang di kota, tanyakan ke restoran halal terdekat.",
]
FOOD_H3 = "Phở dan Bánh Mì: cara memesan dengan aman"
FOOD_TIPS = [
    "Phở dan bánh mì adalah makanan Vietnam yang paling umum. Nước dùng phở sering dimasak dengan kaldu tulang sapi, jadi tanyakan dulu apakah kaldunya dibuat dari sapi atau ayam halal.",
    "Untuk bánh mì, tanyakan jenis dagingnya (sapi atau ayam) dan apakah ada pâté atau daging babi di dalamnya.",
    "Restoran yang menampilkan label halal atau tertulis halal di Google Maps biasanya tidak menjual daging babi. Tetap konfirmasi langsung sebelum memesan.",
]
CTA_TEXT = ("Di Đà Lạt, naik motor adalah cara paling praktis untuk mencari makan halal. Jalan di pusat kota cukup lebar, dan banyak tempat di daftar ini "
            "terletak dekat jalan utama. Văn Phú menyewakan xe tay ga dan xe điện dengan harga 150.000 VND/hari, tanpa cọc tiền, dan bisa diantar ke hotel "
            "jika sewa dari 2 hari. Ambil motor di tiệm, lalu mampir ke beberapa tempat ini dalam satu hari.")

# --- Indonesian article: motorbike tour for Muslim travellers (added 2026-10-28) ---
TOUR_SLUG = "tur-motor-dalat-muslim/"
TOUR_TITLE = "Tur Motor Dalat untuk Wisatawan Muslim: Rute, Makan Halal & Sholat | Van Phu"
TOUR_H1 = "Tur Motor Dalat untuk Wisatawan Muslim"
TOUR_DESC = "Panduan sehari keliling Dalat dengan motor untuk wisatawan Muslim: rute yang mudah, makan halal di sepanjang jalan, tempat sholat dan tips aman berkendara."
TOUR_LEAD = "Dalat paling enak dijelajahi dengan motor. Berikut rute sehari yang bisa diikuti, sekaligus tempat makan halal dan tempat sholat yang bisa Anda rencanakan di tengah perjalanan."
TOUR_ROUTE = [
    ("Pagi: ambil motor di tiệm Văn Phú", "Tiệm di 1/15/5 Thông Thiên Học buka mulai 4:30 pagi. Cek motor, pakai helm, dan minta petunjuk jalan singkat dari staf."),
    ("Siang: makan di Sarah Halal Food", "Restoran halal di pusat kota, dekat jalan utama dan pasar malam. Staf di sini ada yang bisa berbahasa Melayu menurut ulasan."),
    ("Sore: masuk ke pusat kota dan danau", "Berkeliling di sekitar Hồ Xuân Hương. Jalannya lebar dan datar, cocok untuk pemula."),
    ("Malam: makan di Sagar Indian Cuisine", "Masakan India halal dengan porsi besar. Buka sampai 22:00, kecuali Selasa mulai 14:30."),
]
TOUR_TIPS = [
    "Sebelum jalan di tanjakan, cek rem dan bahan bakar. Motor sudah diberi bensin 1 liter saat diserahkan.",
    "Tempat sholat: ISMAEL dan Hajah Hawa disebut punya ruang sholat di ulasan Google. Panduan lengkap ada di halaman restoran halal.",
    "Pakai jaket. Dalat lebih dingin dari kota pesisir, terutama malam hari.",
]
TOUR_FAQ = [
    ("Berapa sewa motor di Văn Phú?", "150.000 VND per hari untuk setiap motor, tanpa cọc tiền. Kami hanya menahan paspor atau KTP."),
    ("Apakah bisa diantar ke hotel?", "Bisa, gratis untuk sewa 2 hari atau lebih di pusat kota. Untuk sewa 1 hari, ambil di tiệm."),
    ("Apakah Văn Phú menyediakan helm?", "Ya, helm sudah termasuk di setiap sewa."),
]
