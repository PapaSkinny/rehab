import requests

# Вставь сюда токен, который дал BotFather
TOKEN = "8456762281:AAHLGafzE9NCml-gn78F7hrCCkdlEw_zpXQ"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
response = requests.get(url)
print(response.json())