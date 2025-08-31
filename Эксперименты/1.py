db = {
        "user_template": {"page": 1, "bookmarks": set()},
        "users": {
            173901673: {
                "name": "Арнольд",
                "age": 45,
                "gender": "undefined_gender",
                "photo_unique_id": "AQADfL8xGyZXcEl4",
                "photo_id": "AgACAgIAAxkBAAIR82OtqD4CMSbFTvitRQNgwhuzf1y1AAJ8vzEbJldwSSpk2bs2OF4_AQADAgADcwADLAQ",
                "education": "no_edu",
                "wish_news": False
            }
        }
    }
print(db)
db["users"].pop(173901673)
print(db)