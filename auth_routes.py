from fastapi import APIRouter

auth_routes = APIRouter(
    prefix="/auth"
)

@auth_routes.get("/signup")
async def signup():
    return {"message": "Sign Up"}