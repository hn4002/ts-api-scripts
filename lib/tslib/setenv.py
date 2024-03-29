import json
import os

#=====================================================================================
class TsSettings(object):

    # ====================================================================================================
    def __init__(self):
        self.TS_API_KEY = "DUMMYADFAFDAFJLKJLDF"
        self.TS_API_SECRET = "DUMMYSDJFADSJADKLJADJKLJDFJJLKDAKLJADLKASFD"
        self.TS_REFRESH_TOKEN = "DUMMYFADJADFJKDFJADFJJKFAHJKAF"
        self.TS_TOKEN_PATH = "/usr/local/ts/token.json"

        self.TS_ACCOUNT_ID = "1234567890"

    # ====================================================================================================
    def get_access_token(self):
        access_token = None
        with open(self.TS_TOKEN_PATH, 'r') as f:
            token_data = json.load(f)
            access_token = token_data["access_token"]
        return access_token

tsSettings = TsSettings()


