import requests
import time

current_time = int(time.time())
two_days_ago = current_time - 172800
tag = 'Python'

url = f'https://api.stackexchange.com//2.3/questions?fromdate={two_days_ago}&todate={current_time}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
response = requests.get(url)
if 199 < response.status_code < 300:
    cnt = 0
    for q in response.json()['items']:
        cnt += 1
        print(f'{cnt}. {q["title"]}')
    print(f'Общее количество вопросов с меткой {tag} - {cnt}')

