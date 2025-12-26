import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* 1. Убираем лишние отступы сверху */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* 2. Прячем меню "Deploy" и футер Streamlit (для вида "Продадакшн") */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
                
        /* 3. Стилизуем кнопки (делаем их более округлыми и неоновыми при наведении) */
        .stButton button {
            border-radius: 12px;
            font-weight: bold;
            border: 1px solid #00ADB5;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #00ADB5;
            color: white;
            box-shadow: 0 0 10px #00ADB5;
        }

        /* 4. Улучшаем вид сообщений чата */
        .stChatMessage {
            background-color: #1E212B;
            border-radius: 15px;
            padding: 10px;
            border: 1px solid #333;
            margin-bottom: 10px;
        }
        /* Аватарки */
        .stChatMessage .stChatMessageAvatar {
            background-color: #00ADB5;
        }

        /* 5. Поле ввода чата - фиксируем внизу красиво */
        .stChatInput textarea {
            border-radius: 15px;
            border: 1px solid #444;
        }
        
        /* 6. Сайдбар */
        [data-testid="stSidebar"] {
            border-right: 1px solid #333;
        }
        
        /* 7. Заголовки */
        h1, h2, h3 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)