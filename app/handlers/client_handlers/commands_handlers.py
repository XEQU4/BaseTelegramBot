from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import IsClient
from app.keyboards import RKB
from app.locales import t
from app.utils import LanguageService

router = Router()


@router.message(CommandStart, IsClient())
async def command_start_handling(message: Message, state: FSMContext) -> None:
    await message.delete()

    lang = await LanguageService.set_to_state(state, message.from_user, enable_db_sync=True)

    text = t("greet_client", lang=lang, name=message.from_user.full_name)
    await message.answer(text=text, reply_markup=RKB.client_menu(lang=lang))
