from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import IsClient
from app.keyboards import RKB
from app.locales import t

router = Router()


@router.message(CommandStart, IsClient())
async def command_start_handling(message: Message, state: FSMContext) -> None:
    await message.delete()

    user = message.from_user

    lang_code = getattr(user, "language_code", "en")
    supported_langs = {"en", "ru"}
    lang = lang_code if lang_code in supported_langs else "en"

    await state.update_data(lang=lang)

    text = t("greet_client", lang=lang, name=message.from_user.full_name)
    await message.answer(text=text, reply_markup=RKB.client_menu(lang=lang))
