import asyncio

from app.container import CONTAINER

adapter = CONTAINER.game_adapter()


asyncio.run(adapter.get("3fa85f64-5717-4562-b3fc-2c963f66afa6"))
