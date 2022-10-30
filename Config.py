import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13782543"))
    API_HASH = os.environ.get("API_HASH", "883e3fce7c3d9d8cfc28c9b9ff51a859")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2043236988:AAEz3kAAvlGtjMrAnB7rln8FkTI-ZsL8i6Y")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKwBu73r4gQmGFo6KAFu3ZV740WoFMuE-bDQFlfFiTcWvTddWi4xfpK3BrrG1Xg2hba5tROw3lOhcamyDAd9xMhE4axz7pjxZmY5lz6q9LWqS9TJ3UKWx-jE_bfTb86d1CGSUBfNV5istrIeArwLMorgwlyAkB13ietd9OPumB6FoKO11c4-V8qb2jR-LjAQH7oO_K3WrpobVx6iT-KqNKy9LbzrxpRJKD_2gxvD0cqpirQXO7v_jcqoeWqClNjgblyOZ44b31Y-9NyWHCBqt6AGFq89voOn9IuveR8UToF74ouk2YDQL7hJqA0Q7ZVhHLb3i9ZsUPId6OLjABzyihDsm6E=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "True")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", "True")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "iiniirobot")
    SUPPORT = os.environ.get("SUPPORT", "evzesda") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "evzesda") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/c042e6fe69dd87ac7160b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1807928922")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "False") # Change it to "True"
