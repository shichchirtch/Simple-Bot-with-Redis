from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from lexicon import start_greeding, press_cancel
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import default_state
from external_functions import insert_new_user_in_table, reset
from aiogram.fsm.context import FSMContext
from keyboards import  keyboard_after_cancel
from bot_states import IN_GAME

command_router = Router()
@command_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    print(f'user {message.chat.first_name} press start')
    user_name = message.chat.first_name
    user_tg_id = message.from_user.id
    await insert_new_user_in_table(user_tg_id, user_name)
    await state.set_state(IN_GAME.after_start)
    print('\n\nstate.get_state()  =  ', end=" ")
    status = await state.get_state()
    print(status)
    await message.answer(
        f'Привет, <b>{message.chat.first_name}</b> !  \U0001F60A\n {start_greeding}',
                    reply_markup=keyboard_after_cancel)
    print("Process finfshed")


@command_router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command(message: Message, state: FSMContext):
    await message.answer(text=f'Вы вышли из игры\n\n{press_cancel}', reply_markup=keyboard_after_cancel)
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    user_tg_id = message.from_user.id
    await reset(user_tg_id)
    await state.clear()




