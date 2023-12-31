from fastapi import FastAPI
from starlette.responses import PlainTextResponse

from auth.router import router as auth_router
from publications.router import router as publications_router
from reactions.router import router as reactions_router
from users.router import router as users_router


def _register_routers(*routers) -> None:
    for router in routers:
        app.include_router(router)


app = FastAPI(title="BlogPost")


@app.get("/", tags=["Root"])
async def root():
    return PlainTextResponse(content="Hello World!\n"
                                     "This is a simple blog post application.\n"
                                     "You can find the documentation at /docs")


_register_routers(
    auth_router,
    users_router,
    publications_router,
    reactions_router,
)
