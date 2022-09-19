from decouple import config

HOST = config('HOST')
#PORT = config('PORT')
ENDPOINT = config('ENDPOINT')

API_URL = f'{HOST}{ENDPOINT}'