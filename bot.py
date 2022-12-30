from pyrogram import Client
import time
from sys import stderr
from loguru import logger
from datetime import datetime

# api_id = 12345
# api_hash = "string"

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

global chat_list
with open('chats.txt', 'r') as f:
    chat_list = f.read().splitlines()

app = Client("my_account")


async def main():
    async with app:
        while True:

            logger.info('Starting bot')
            time_now = datetime.now().strftime("%H")

            if int(time_now) in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:            
                async for message in app.get_chat_history(-754987302, 1):
                    for i in range(len(chat_list)):
                        chat_id = chat_list[i]
                        await app.copy_message(int(chat_id), -754987302, message.id)
                        logger.info(f"Message copied and forwarded to {chat_id}")
                        time.sleep(3)
                logger.success('Cycle finished | sleeping 3h')
                time.sleep(int(10800))
            else:
                logger.error('Not in time')
                time.sleep(1800)
                logger.info('Trying to run again')
            

app.run(main())