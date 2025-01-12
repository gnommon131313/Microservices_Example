import uvicorn

from db import init as db_init


def main() -> None:
    db_init.init()
    uvicorn.run("api.main:app", host="127.0.0.1", port=8002)

if __name__ == "__main__":
    main()