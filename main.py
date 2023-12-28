from fastapi import FastAPI
from app.routes import menu as user_routes
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5173" # 또는 http://localhost:5173
    ,"http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():
    return {"message" : "안녕하세요 파이보"}