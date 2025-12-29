import requests
import uuid
from langchain_core.tools import tool
import urllib.parse
import random

import os
from dotenv import load_dotenv
load_dotenv()

# @tool("generate_image")
# def generate_image_tool(prompt: str):
#     """
#     Генерирует изображение бесплатно через Pollinations AI.
#     """
#     try:
#         # 1. Кодируем промпт
#         encoded_prompt = urllib.parse.quote(prompt)
        
#         # 2. Добавляем random seed, чтобы избежать кэширования и таймаутов
#         seed = random.randint(1, 99999)
        
#         # URL (убрали turbo, вернули flux, добавили seed)
#         # Если flux падает, можно попробовать модель 'midjourney' (она там тоже есть как алиас)
#         image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=turbo&width=1024&height=768&seed={seed}&nologo=true"
        
#         # 3. ВАЖНО: Добавляем заголовки, чтобы не получать 524/403
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#         }
        
#         # 4. Скачиваем с таймаутом (чтобы не висело вечно)
#         response = requests.get(image_url, headers=headers, timeout=30)
        
#         if response.status_code == 200:
#             filename = f"generated_image_{uuid.uuid4().hex[:6]}.jpg"
#             with open(filename, 'wb') as f:
#                 f.write(response.content)
#             return f"Изображение успешно сгенерировано и сохранено как: {filename}"
#         else:
#             return f"Ошибка сервиса генерации (Code {response.status_code}). Попробуйте позже."
            
#     except requests.exceptions.Timeout:
#         return "Ошибка: Сервис генерации долго не отвечает (Timeout)."
#     except Exception as e:
#         return f"Ошибка при генерации: {e}"
    
# Если ключа нет, инструмент вернет понятную ошибку
HF_KEY = os.getenv("HUGGINGFACE_API_KEY")

@tool("generate_image")
def generate_image_tool(prompt: str):
    """
    Генерирует изображение по текстовому описанию с помощью Stable Diffusion XL.
    Вход: Подробное описание картинки на английском языке.
    Выход: Имя сохраненного файла картинки.
    """
    # ^^^ ВОТ ЭТОГО ОПИСАНИЯ НЕ ХВАТАЛО ^^^

    if not HF_KEY:
        return "Ошибка: Не найден HUGGINGFACE_API_KEY в файле .env"

    # Используем модель Stable Diffusion XL (бесплатная через API)
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {HF_KEY}"}

    try:
        # Отправляем запрос
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        # Проверяем статус
        if response.status_code != 200:
            return f"Ошибка API HuggingFace: {response.text}"

        # Сохраняем файл
        filename = f"generated_image_{uuid.uuid4().hex[:6]}.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)
            
        return f"Изображение успешно сгенерировано и сохранено как: {filename}"

    except Exception as e:
        return f"Критическая ошибка генерации: {e}"