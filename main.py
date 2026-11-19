import sys
import logging
import asyncio

from bot.loader import bot, dp
from bot.config import config

from bot.database.models import init_db
from bot.handlers import router as root_router


log_level = logging.DEBUG if config.debug else logging.INFO


async def main():
    logging.info("Bot has been started")

    await init_db()
    dp.include_router(root_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        stream=sys.stdout
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot has been stopped")