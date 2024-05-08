import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.recommender.LocationsLoader import LocationsLoader
from core.recommender.Recommender import Recommender

app = FastAPI(
    title="Egytraveler Recommender",
    description="Egytraveler recommender API",
    version="1.0.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://egytraveler.netlify.app","http://localhost:5173"], # Allows requests from this origin
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "ًWelcome to Egytraveler API !"}


@app.get("/recommend/{location_id}")
async def recommender(location_id: str):
    locations = LocationsLoader()
    recommendations = Recommender(
        locations
    ).run(location_id, 5)

    return {
        "recommendations": recommendations,
    }


if __name__ == '__main__':
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(app, host="0.0.0.0", port=port)
