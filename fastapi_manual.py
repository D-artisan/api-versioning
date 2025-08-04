from fastapi import FastAPI, APIRouter

app = FastAPI(title="Manual Versioning API")

# Version 1 router
v1_router = APIRouter(prefix="/api/v1")

@v1_router.get("/greet")
def greet_v1():
    return {"message": "Hello from v1"}

# Version 2 router
v2_router = APIRouter(prefix="/api/v2")

@v2_router.get("/greet")
def greet_v2():
    return {"message": "Hi from v2"}

app.include_router(v1_router)
app.include_router(v2_router)
