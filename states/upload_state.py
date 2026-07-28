from aiogram.fsm.state import State, StatesGroup


class UploadState(StatesGroup):
    waiting_for_resume = State()
    waiting_for_jd = State()