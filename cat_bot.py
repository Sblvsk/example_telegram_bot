import time
from telegram import Bot


from secrets import bot_token, id_chat

chat_id = id_chat
bot = Bot(bot_token)

def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)

def main() -> None:
    send_random_cat()

if __name__ == '__main__':
    for i in range(5):
        main()

