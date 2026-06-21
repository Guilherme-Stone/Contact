from fastapi import FastAPI
from contextlib import asynccontextmanager
from Database.database import db
from Routes.routes import router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await db.init_db()
    yield app

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
