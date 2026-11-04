"""Topic clusters for internal linking: an article's "Read also" box shows its published cluster siblings first
(newest first), then the newest other articles. Add every new article key to the right cluster."""
CLUSTERS = {
    # Group 1 — no cash deposit & quick paperwork
    "procedure": ["lt-nodeposit", "lt-procedure", "lt-documents", "lt-booking", "lt-checklist", "lt-reliable", "lt-first-time", "lt-foreigners"],
    # Group 2 — early opening / cloud hunting / sunrise
    "early": ["cloudhunt", "caudat", "lt-early", "lt-caudat-early", "langbiang", "pinkgrass", "november"],
    # Group 3 — electric scooters
    "ev": ["evrules", "lt-ev-foreigners", "lt-ev-experience", "lt-ev-city", "lt-ev-price", "lt-ev-battery", "lt-ev-couples",
           "lt-ev-beginners", "lt-ev-cafes", "lt-ev-night", "lt-ev-rain", "lt-ev-vs-grab", "lt-ev-eco", "lt-ev-parking",
           "lt-ev-halfday", "lt-ev-checklist", "lt-ev-families", "lt-ev-faq",
           "lt-ev-lake", "lt-ev-market", "lt-ev-hills", "lt-ev-weekend", "lt-ev-homestay", "lt-ev-morning", "lt-ev-safety",
           "lt-ev-flowers", "lt-ev-luggage", "lt-ev-cold"],
    # Group 4 — delivery & location
    "location": ["getaround", "where-to-stay", "selfguided", "lt-busstation", "lt-delivery", "lt-center", "nightmarket", "thingstodo", "oneday", "kids"],
    # bikes & trip length
    "bikes": ["lt-automatic", "lt-2days", "days2", "lt-airblade", "lt-vision", "lt-two", "lt-multiday", "lt-backpacker", "budget", "lt-rainy", "rainyday", "riding", "passes"],
}
GROUP = {k: g for g, ks in CLUSTERS.items() for k in ks}
