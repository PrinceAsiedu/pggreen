
import asyncio
from publish import publish
from subscribe import subscribe
import aiopg
from config import config_string

# dsn = "dbname=bimbo user=pygreen password=icugr8xx14 host=localhost"
data_source_name = config_string
async def main():
    async with aiopg.connect(data_source_name) as listenConn:
        async with aiopg.create_pool(data_source_name) as notifyPool:
            listener = subscribe(listenConn, "channel")
            notifier = publish(notifyPool, "channel", [f"message {i}" for i in range(5)])
            await asyncio.gather(listener, notifier)
asyncio.run(main())
