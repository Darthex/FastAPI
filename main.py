from fastapi import FastAPI
from mangum import Mangum
from routers import title, content, recommendation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(recommendation.router)
app.include_router(title.router)
app.include_router(content.router)
