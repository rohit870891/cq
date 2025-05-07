from decouple import config

try:
    APP_ID = config("APP_ID", default=20718334, cast=int)
    API_HASH = config("API_HASH", default="4e81464b29d79c58d0ad8a0c55ece4a5")
    BOT_TOKEN = config("BOT_TOKEN", default="8065030679:AAE-Vvvejh6maceHLBamYQPOYIyC-sMUM2w")
    DEV = config("DEV", default=7328629001, cast=int)
    OWNER = config("OWNER", default="7328629001")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config("THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg")
except Exception as e:
    print("Environment vars Missing")
    print("Something went wrong")
    print(str(e))
    exit()