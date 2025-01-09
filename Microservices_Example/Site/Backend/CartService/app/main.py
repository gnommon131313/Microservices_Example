import asyncio
import uvicorn
from api.main import app
from db import init as db_init


async def server_run():
    config = uvicorn.Config(app, host="127.0.0.1", port=8002, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    db_init.init()
    
    await asyncio.gather(server_run())

if __name__ == "__main__":
    asyncio.run(main())