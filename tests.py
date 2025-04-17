from src.database.db import get_db
from src.repository.contacts import upcoming_birthdays
import asyncio


async def test_1():
    db = next(get_db())
    res = await upcoming_birthdays(days=10, skip=0, limit=10, db=db)
    print(res)
    return res


if __name__ == "__main__":
    # Запуск через event loop
    asyncio.run(test_1())
