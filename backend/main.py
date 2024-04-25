import uvicorn

from fastapi import FastAPI

# from core.db_manager import lifespan

from core.setings import settings

from api_v1 import router as router_v1


app = FastAPI()

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
