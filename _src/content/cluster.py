"""Topic clusters for internal linking: an article's "Read also" box shows its published cluster siblings first
(newest first), then the newest other articles. Add every new article key to the right cluster."""
CLUSTERS = {
    # Group 1 — no cash deposit & quick paperwork
    "procedure": ["lt-nodeposit", "lt-procedure", "lt-sameday", "lt-documents", "lt-booking", "lt-checklist", "lt-reliable", "lt-first-time", "lt-foreigners", "lt-return", "lt-breakdown", "lt-included", "lt-navigation", "lt-solo-female", "lt-nightride", "lt-language", "lt-damage", "lt-helmet", "lt-shop-directions", "lt-backpack-storage"],
    # Group 2 — early opening / cloud hunting / sunrise
    "early": ["cloudhunt", "caudat", "lt-early", "lt-caudat-early", "langbiang", "pinkgrass", "november", "sunrise-sunset", "danhia", "december", "hikes"],
    # Group 3 — electric scooters
    "ev": ["evrules", "lt-ev-foreigners", "lt-ev-experience", "lt-ev-city", "lt-ev-price", "lt-ev-battery", "lt-ev-couples",
           "lt-ev-beginners", "lt-ev-cafes", "lt-ev-night", "lt-ev-rain", "lt-ev-vs-grab", "lt-ev-eco", "lt-ev-parking",
           "lt-ev-halfday", "lt-ev-checklist", "lt-ev-families", "lt-ev-faq",
           "lt-ev-lake", "lt-ev-market", "lt-ev-hills", "lt-ev-weekend", "lt-ev-homestay", "lt-ev-morning", "lt-ev-safety",
           "lt-ev-flowers", "lt-ev-luggage", "lt-ev-cold", "lt-ev-1day", "lt-ev-week", "lt-ev-booking", "lt-ev-delivery", "lt-ev-food-tour", "lt-ev-display", "lt-ev-group", "lt-ev-villas", "lt-ev-pagodas", "lt-ev-nomads", "lt-ev-students", "lt-ev-churches", "lt-ev-station", "lt-ev-palaces", "lt-ev-viewpoints", "lt-ev-lowbattery"],
    # Group 4 — delivery & location
    "location": ["getaround", "from-id-my", "where-to-stay", "selfguided", "lt-busstation", "lt-delivery", "lt-center", "nightmarket", "thingstodo", "oneday", "kids", "station", "phrases", "parking-fuel", "pagodas", "solo", "vegetarian", "souvenirs", "lt-photoshoot", "dalatmarket", "breakfast", "lt-airport", "coffeefarms", "history", "couples", "villages", "evenings", "slowtravel", "crazyhouse", "lakes", "museum", "phototips"],
    # bikes & trip length
    "bikes": ["lt-automatic", "lt-2days", "days2", "lt-airblade", "lt-vision", "lt-two", "lt-multiday", "lt-backpacker", "budget", "lt-rainy", "rainyday", "riding", "passes", "lt-groups", "lt-waterfalls-rent", "lt-weekend", "lt-weather-check", "lt-sunset-ride", "lt-tuyenlam-rent", "packing", "lt-langbiang-rent", "lt-short-ride", "lt-dankia-rent"],
}
GROUP = {k: g for g, ks in CLUSTERS.items() for k in ks}
