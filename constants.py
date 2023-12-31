from config import *
import random
from create_bot import bot

TEXT_APPROVE = "✅ Подтвердить"
TEXT_REJECT = "❌ Отказать"
TEXT_BOT_DESCRIPTION = "Через этот бот можно присылать фото и видео для публикации в канале @vputite" + "\n\n" + "Нажмите /start чтобы начать" + "\n" + "Нажмите /help для помощи"
TEXT_BOT_DESCRIPTION_IMG = "info_photo.png"
TEXT_START = "Запустить бота"
TEXT_WELCOME = "Здравствуйте"
TEXT_WELCOME_DESCRIPTION = "На связи с вами для формирования актуальной информации о ситуации в общественном транспорте"
TEXT_SUBMIT_CONFIRMATION = "Ваше сообщение отправлено на рассмотрение"
TEXT_SUBMIT_ERROR = "Ошибка при отправлении сообщения"
TEXT_SUBMIT_RULES = "Пришлите пожалуйста фото или видео c описанием"
TEXT_SUBMIT_RULES_PHOTO = "Пришлите пожалуйста фото c описанием"
TEXT_SUBMIT_RULES_VIDEO = "Пришлите пожалуйста видео c описанием"
TEXT_SUBMIT_RULES_GROUP = "Пришлите пожалуйста ОДИН фото/видео файл с описанием"
TEXT_PHOTO_REQUEST = "Пришлите пожалуйста фотографию"
TEXT_CAPTION_REQUEST = "Пришлите пожалуйста описание"
TEXT_THANKS = "Спасибо за информацию, после одобрения модератором, она будет размещена в канале"
TEXT_USER_REJECT_CONFIRMATION = "К сожалению модераторы отклонили публикацию"
TEXT_USER_APPROVE_CONFIRMATION = "Сообщение отправлено в канал"
TEXT_ADMIN_REJECT_CONFIRMATION = "По ряду причин мы не можем принять его сегодня для публикации в канале. Но очень хотим, чтобы вы оставались с нами - присылайте пожалуйста еще"
TEXT_ADMIN_APPROVE_CONFIRMATION = "Ваше сообщение принято для публикации в канал! Спасибо за наполние его актуальной информацией :)"
TEXT_SUBSCRIBE = "Подписаться на канал"
TEXT_SENDINFO = "Прислать информацию"

TEXT_SUBSCRIBE = "✍️ Подписаться на канал"
TEXT_SENDINFO = "⬆️ Прислать информацию"

TEXT_HELP = "Как отправить новость:"  + "\n\n" + "1️⃣ Нажмите на кнопку 📎 в поле ввода текста, чтобы прикрепить фотографию или видео"  + "\n" + "2️⃣ Добавьте комментарий о ситуации в поле Добавить подпись"  + "\n" + "3️⃣ Отправьте сообщение боту" + "\n\n" + "Формат новости:"  + "\n\n" + "⚠ сообщение должно содержать только одну фотографию или видеофайл с подписью" 

def getValue(v):
        if type(v) == type(list()):
                print("This is a list of {} items!".format(len(v)))
        
                r_idx=random.randint(0, len(v)-1)
                print(r_idx)
                return v[r_idx]

        if isinstance(v, str):
                print("This is a string!")
                return v

        return str(v)
