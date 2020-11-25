from fastapi import FastAPI
from server.routes.training import router as TrainingRouter
from server.routes.predict import router as PredictRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WILLAC UMU REST API")

app.include_router(TrainingRouter, tags=["Training"], prefix="/training")
app.include_router(PredictRouter, tags=["Predict"], prefix="/predict")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Willac Umu Api is running"}



