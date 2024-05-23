
# from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
redis = Redis(host='localhost')
redis_storage = RedisStorage(redis=redis)

# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class IN_GAME(StatesGroup):
    after_start = State()
    in_game = State()        # Состояние в игре

