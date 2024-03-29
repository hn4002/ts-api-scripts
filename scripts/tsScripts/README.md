The scripts in this directory are for the initial testing of the TS API (in that sequence):

# get_access_token.py

This script uses the refresh token to get the access token.
It reads the refresh token from from the config.
The access token is saved in the specified file.

# get_accounts.py

This script uses the access token to get the list of accounts.

# get_barcharts.py

This script uses the access token to get the historical bar data for a symbol.

# get_quotes.py

This script uses the access token to get the quotes for multiple symbols.
