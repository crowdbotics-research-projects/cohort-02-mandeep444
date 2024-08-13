from fastapi import FastAPI
from router import users, subscription, magazines, plans
from db import initialize_database

app = FastAPI()

initialize_database()


app.include_router(users.router)
app.include_router(subscription.router)
app.include_router(magazines.router)
app.include_router(plans.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
