from bot_base import session_marker, User
from random import randint
from sqlalchemy import select


async def insert_new_user_in_table(user_tg_id:int, name:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        print('query =', query)
        needed_data = query.scalar()
        print('needed_data = ', needed_data)
        if not needed_data:
            new_us = User(id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()

async def get_secret_number(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        needed_data = query.scalar()
        needed_data.secret_number = randint(6, 100)
        await session.commit()


async def update_table(user_tg_id:int, us_number:int):
    """Функция обновляет таблицу users"""
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        n = query.scalar()
        n.attempts -= 1 # декремент попыток
        data_in = n.steps
        if us_number not in n.steps:
            print('\n\nn,steps =  ', n.steps)
            n.steps = data_in + [us_number]
            print('n-steps =  ', n.steps, '\n\n')
            await session.commit()
            return None
        else:
            await session.commit()
            return "Do not repeat your numbers !"


async def check_attempts_lost_number(user_tg_id):
    '''Функция проверяет количество оставшихся попыток'''
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        needed_data = query.scalar()
        print('\n\n\nneeded_data.attempts', needed_data.attempts)
        if needed_data.attempts == 1:
            return True
        return False

async def reset(user_tg_id):
    async with session_marker() as session:
        print("\n\nWork RESET Function")
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        n = query.scalar()
        n.attempts = 5
        n.steps = []
        n.secret_number = 0
        await session.commit()











