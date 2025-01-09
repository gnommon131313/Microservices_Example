import asyncio
import uvicorn
from api import app


async def server_run():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(server_run())

if __name__ == "__main__":
    asyncio.run(main())