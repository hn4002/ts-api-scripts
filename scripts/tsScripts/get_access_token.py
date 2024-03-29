#!/opt/homebrew/bin/python3

# This script uses the refresh token to get the access token.
# It reads the refresh token from the config.
# The access token is saved in the specified file.

import json
import os
import requests
import sys

# Include local lib code from the project
local_lib_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
if local_lib_dir not in sys.path:
    sys.path.append(local_lib_dir)
from tslib.setenv import tsSettings

client_id = tsSettings.TS_API_KEY
client_secret = tsSettings.TS_API_SECRET
refresh_token = tsSettings.TS_REFRESH_TOKEN
token_path = tsSettings.TS_TOKEN_PATH

#====================================================================================================
def main():
    print(f"refresh_token is {refresh_token}")

    print(f"App Info:\n    client_id={client_id}\n    client_secret={client_secret}")
    print(f"token_path is {token_path}")

    url = "https://signin.tradestation.com/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
    }

    response = requests.post(url, headers=headers, data=data)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    # Print headers
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")

    # Remove token file
    if os.path.exists(token_path):
        os.remove(token_path)

    # Save result in the token file
    out_text = json.dumps(response.json(), indent=4)
    print(f"respnose object: \n{out_text}")
    with open(token_path, 'w') as f:
        f.write(out_text)
    print(f"Token data written to {token_path}")

#====================================================================================================
if __name__ == "__main__":
    main()


