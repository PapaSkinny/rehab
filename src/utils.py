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

