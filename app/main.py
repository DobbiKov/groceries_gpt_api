from fastapi import FastAPI
from app.routes import items

app = FastAPI(
        title="Groceries GPT",
        version="0.1.0"
        )
app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
