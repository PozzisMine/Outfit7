from google_play_scraper import developer, app
import json
import time
from datetime import datetime

DEV_ID = "5630538819012062144"
COUNTRY = "us"
LANG = "en"

apps = developer(DEV_ID, lang=LANG, country=COUNTRY)

result = {
    "checked_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    "games": []
}

for item in apps:
    app_id = item["appId"]

    try:
        info = app(app_id, lang=LANG, country=COUNTRY)

        result["games"].append({
            "title": info.get("title"),
            "appId": app_id,
            "updated": info.get("updated"),
            "url": f"https://play.google.com/store/apps/details?id={app_id}"
        })

        time.sleep(1)

    except Exception as e:
        print("Ошибка:", app_id, e)

with open("updates.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Готово: updates.json обновлён")
