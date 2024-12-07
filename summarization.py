from langchain_community.chat_models.gigachat import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

from config.app_config import GIGACHAT_TOKEN, GIGACHAT_SCOPE, GIGACHAT_MODEL

_giga_chat = GigaChat(
    credentials=GIGACHAT_TOKEN,
    scope=GIGACHAT_SCOPE,
    model=GIGACHAT_MODEL,
    verify_ssl_certs=False,
    streaming=True,
)


def _get_messages(text: str) -> list:
    min_length = int(0.4 * len(text))
    max_length = int(0.6 * len(text))
    return [
        SystemMessage(
            content=f'Суммаризуй следующий текст так, чтобы итоговый результат содержал от {min_length} до {max_length} символов'
        ),
        HumanMessage(
            content=text
        )
    ]


def summarize_text(text: str) -> str:
    messages = _get_messages(text)
    res = _giga_chat.invoke(messages)
    return res.content
