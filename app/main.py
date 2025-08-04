from fastapi import FastAPI
from config.settings import settings

# import versioned routers
from app.v1.endpoints import items as items_v1
from app.v2.endpoints import items as items_v2
from app.endpoints.health import router as health_router

app = FastAPI(title=settings.app_name, debug=settings.debug)

# include common health check
app.include_router(health_router, prefix="")

# include version 1 API
app.include_router(
    items_v1.router,
    prefix=settings.version_v1_prefix,
    tags=["v1"]
)

# include version 2 API
app.include_router(
    items_v2.router,
    prefix=settings.version_v2_prefix,
    tags=["v2"]
)