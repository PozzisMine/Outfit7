from google_play_scraper import app
import json
import time
from datetime import datetime, timezone

COUNTRY = "us"
LANG = "en"

APP_IDS = [
    "com.outfit7.talkingtom",
    "com.outfit7.talkingben",
    "com.outfit7.talkingtom2free",
    "com.outfit7.talkingpierrefree",
    "com.outfit7.talkingnewsfree",
    "com.outfit7.talkinggingerfree",
    "com.outfit7.talkingangelafree",
    "com.outfit7.gingersbirthdayfree",
    "com.outfit7.mytalkingtomfree",
    "com.outfit7.mytalkingangelafree",
    "com.outfit7.talkingtomgoldrun",
    "com.outfit7.mytalkinghank",
    "com.outfit7.mytalkingtom2",
    "com.outfit7.herodash",
    "com.outfit7.mytalkingtomfriends",
    "com.outfit7.mytalkingangela2",
    "com.outfit7.talkingtomtimerush",
    "com.outfit7.ttfworld",
    "com.outfit7.mytalkingtomfriends2"
]

result = {
    "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "games": []
}

for app_id in APP_IDS:
    try:
        info = app(app_id, lang=LANG, country=COUNTRY)

        ts = info.get("updated")
        readable = "Не найдено"

        if ts:
            readable = datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        result["games"].append({
            "title": info.get("title"),
            "appId": app_id,
            "icon": info.get("icon"),
            "updated": ts,
            "updated_readable": readable,
            "url": f"https://play.google.com/store/apps/details?id={app_id}"
        })

        print("OK:", app_id)
        time.sleep(1)

    except Exception as e:
        print("Ошибка:", app_id, e)

with open("updates.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Готово")
