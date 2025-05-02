from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import IsAdmin
from app.keyboards import RKB, IKB
from app.locales import t
from app.utils import LanguageService

router = Router()


@router.message(CommandStart, IsAdmin())
async def command_start_handling(message: Message, state: FSMContext) -> None:
    await message.delete()

    lang = await LanguageService.set_to_state(state, message.from_user, enable_db_sync=True)

    text1 = t("greet_admin", lang=lang, name=message.from_user.full_name)
    text2 = t("greet_reply", lang=lang)
    await message.answer(text=text1, reply_markup=IKB.admin_menu(lang=lang))
    await message.answer(text=text2, reply_markup=RKB.admin_menu(lang=lang))
