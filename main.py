from fastapi import FastAPI
from order_routes import orders_router
from auth_routes import auth_routes
app = FastAPI()
app.include_router(orders_router)
app.include_router(auth_routes)

@app.get("/")
async def root():
    return {"message": "Bosh Sahifa"}

