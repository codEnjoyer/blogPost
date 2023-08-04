from fastapi import FastAPI

from auth.router import router as auth_router

app = FastAPI(title="BlogPost")

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
