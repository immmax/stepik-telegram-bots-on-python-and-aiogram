import requests
import time
import json

from config.config import *

offset: int = -2
counter: int = 0
chat_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:

    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(json.dumps(updates, indent=4))

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            cat_link = cat_response.json()[0]['url']
            if cat_response.status_code == 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(20.63)
    counter += 1
