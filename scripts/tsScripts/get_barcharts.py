#!/opt/homebrew/bin/python3

# This script uses the access token to get the quote for a symbol.

import json
import os
import requests
import sys

# Include local lib code from the project
local_lib_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
if local_lib_dir not in sys.path:
    sys.path.append(local_lib_dir)
from tslib.setenv import tsSettings

access_token = tsSettings.get_access_token()

#====================================================================================================
def main():
    # Get access_token from the token file
    print(f"access_token is {access_token}")

    url = f"https://api.tradestation.com/v3/marketdata/barcharts/MSFT?interval=1&unit=Daily&barsback=2&startdate=2024-01-05T21:00:00Z"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    print(f"Calling url: {url}, headers: {headers}")
    response = requests.get(url, headers=headers)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")
    out_text = json.dumps(response.json(), indent=4)
    print(f"respnose object: \n{out_text}")


#====================================================================================================
if __name__ == "__main__":
    main()
