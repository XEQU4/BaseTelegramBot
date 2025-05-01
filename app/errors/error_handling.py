from aiogram import Router, exceptions
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from app.logger import logger

router = Router()


@router.error(ExceptionTypeFilter(exceptions.CallbackAnswerException))
async def error_handler1(event: ErrorEvent) -> None:
    logger.error(
        f"\n\tAiogram error: CallbackAnswerException – Exception while answering callback query"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tCallback: {event.update.callback_query}"
        f"\n\tUpdate: {event.update}\n"
    )


@router.error(ExceptionTypeFilter(exceptions.TelegramNotFound))
async def error_handler2(event: ErrorEvent) -> None:
    logger.error(
        f"\n\tAiogram error: TelegramNotFound – Chat/User/Message not found"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tMessage: {event.update.message}"
        f"\n\tUpdate: {event.update}\n"
    )


@router.error(ExceptionTypeFilter(exceptions.TelegramRetryAfter))
async def error_handler3(event: ErrorEvent) -> None:
    logger.warning(
        f"\n\tAiogram warning: TelegramRetryAfter – Too many requests. Retry after "
        f"{str(event.exception).split()[-7]} seconds"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tMessage: {event.update.message}"
        f"\n\tUpdate: {event.update}\n"
    )


@router.error(ExceptionTypeFilter(exceptions.TelegramBadRequest))
async def error_handler4(event: ErrorEvent) -> None:
    logger.exception(
        f"\n\tAiogram error: TelegramBadRequest – Malformed or invalid request"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tMessage: {event.update.message}"
        f"\n\tUpdate: {event.update}\n"
    )


@router.error(ExceptionTypeFilter(exceptions.TelegramUnauthorizedError))
async def error_handler5(event: ErrorEvent) -> None:
    logger.exception(
        f"\n\tAiogram error: TelegramUnauthorizedError – Bot token is invalid or has been revoked"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tUpdate: {event.update}\n"
    )


@router.error(ExceptionTypeFilter(exceptions.TelegramForbiddenError))
async def error_handler6(event: ErrorEvent) -> None:
    logger.exception(
        f"\n\tAiogram error: TelegramForbiddenError – Bot was kicked or is not allowed in chat"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tUpdate: {event.update}\n"
    )


@router.error()
async def error_handler(event: ErrorEvent) -> None:
    logger.exception(
        f"\n\tAiogram error: Unhandled exception"
        f"\n\tevent exception: {event.exception}"
        f"\n\n\tUpdate: {event.update}\n"
    )
