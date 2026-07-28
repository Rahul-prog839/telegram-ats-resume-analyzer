from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.upload_state import UploadState

router = Router()


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):

    await state.set_state(UploadState.waiting_for_resume)

    await message.answer(
        "👋 Welcome to Resume ATS Analyzer Bot!\n\n"
        "📄 Upload one or more resumes (PDF/DOCX).\n\n"
        "When you finish uploading resumes, type /done."
    )