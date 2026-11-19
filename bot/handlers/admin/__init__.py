from aiogram import Router, F

from bot.config import config


ADMIN_IDS = config.admin_ids

router = Router()

router.message.filter(F.from_user.id.in_(ADMIN_IDS))
router.callback_query.filter(F.from_user.id.in_(ADMIN_IDS))

router.include_routers(
    # Some admin routers
)