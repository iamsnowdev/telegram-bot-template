from aiogram import Router

from bot.handlers.admin import router as admin_router
from bot.handlers.user import router as user_router


router = Router()
router.include_routers(
    admin_router,
    user_router
)