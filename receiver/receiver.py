from fastapi import FastAPI

api = FastAPI()

@api.get("/")
async def root():
    print("Received something")