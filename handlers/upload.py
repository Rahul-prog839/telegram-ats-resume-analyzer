import os
import shutil

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.upload_state import UploadState

router = Router()


@router.message(
    UploadState.waiting_for_resume,
    F.document
)
async def upload_resume(message: Message, state: FSMContext):

    # Create folder for current user
    user_folder = os.path.join(
        "uploads",
        "resumes",
        str(message.from_user.id)
    )

    # Clear old resumes only once at the beginning of a new upload session
    data = await state.get_data()

    if not data.get("session_started"):

        if os.path.exists(user_folder):
            shutil.rmtree(user_folder)

        os.makedirs(user_folder, exist_ok=True)

        await state.update_data(session_started=True)

    else:
        os.makedirs(user_folder, exist_ok=True)

    # Get uploaded file
    file = await message.bot.get_file(
        message.document.file_id
    )

    destination = os.path.join(
        user_folder,
        message.document.file_name
    )

    # Download file
    await message.bot.download_file(
        file.file_path,
        destination
    )

    total = len(os.listdir(user_folder))

    await message.answer(
        f"✅ Resume uploaded successfully.\n\n"
        f"📄 File: {message.document.file_name}\n"
        f"📂 Total resumes uploaded: {total}\n\n"
        f"Upload another resume or type /done."
    )


@router.message(
    Command("done"),
    UploadState.waiting_for_resume
)
async def done_uploading(message: Message, state: FSMContext):

    await state.set_state(
        UploadState.waiting_for_jd
    )

    await message.answer(
        "📄 Great!\n\n"
        "Now upload the Job Description (PDF or DOCX)."
    )


@router.message(
    UploadState.waiting_for_resume
)
async def invalid_resume(message: Message):

    await message.answer(
        "❌ Please upload a resume as a PDF or DOCX file.\n\n"
        "When finished uploading resumes, type /done."
    )