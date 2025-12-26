import os
import uuid
import base64
import requests
import streamlit as st
from langchain_gigachat.chat_models import GigaChat
from dotenv import load_dotenv

load_dotenv()

# Основные настройки
AUTH_KEY = os.getenv("GIGACHAT_CREDENTIALS")
BASE_URL = "https://gigachat.devices.sberbank.ru/api/v1"

def get_llm():
    """Возвращает объект GigaChat для LangChain."""
    if not AUTH_KEY:
        st.error("GigaChat Credentials не найдены!")
        st.stop()

    return GigaChat(
        credentials=AUTH_KEY,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
        temperature=0.1, # Для креатива лучше повыше
    )

def get_access_token():
    """
    Получает временный токен доступа (Bearer) для прямых запросов.
    Нужен, чтобы скачать картинку.
    """
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Bearer {AUTH_KEY}'
    }
    try:
        response = requests.post(url, headers=headers, data={'scope': 'GIGACHAT_API_PERS'}, verify=False)
        return response.json()['access_token']
    except Exception as e:
        print(f"Ошибка получения токена: {e}")
        return None

def download_image(file_id: str):
    """
    Скачивает картинку по ID из GigaChat и сохраняет её локально.
    Возвращает имя файла.
    """
    token = get_access_token()
    if not token:
        print("ОШИБКА: Нет токена доступа!")
        return None

    url = f"{BASE_URL}/files/{file_id}/content"
    headers = {
        'Accept': 'application/jpg',
        'Authorization': f'Bearer {token}'
    }
    
    try:
        response = requests.get(url, headers=headers, verify=False, stream=True)
        filename = f"generated_image_{uuid.uuid4().hex[:6]}.jpg"
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return filename
    except Exception as e:
        print(f"Ошибка скачивания: {e}")
        return None