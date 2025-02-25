from fastapi import FastAPI
from backend.app.routes.auth import router as auth_router
from backend.app.routes.users import router as users_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to BrandConnect SaaS!"}