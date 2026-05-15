from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Your routes...

# This should be at the bottom of main.py
if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 10000))
    )

# models.Base.metadata.create_all(bind=engine)


origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"Message": "Hello World successfully deployed from CI/CD pipeline!"}




