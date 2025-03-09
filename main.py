from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("база очищена")
    await create_tables()
    print("база готова")
    yield
    print("выключение")


app = FastAPI()
app.include_router(tasks_router)


