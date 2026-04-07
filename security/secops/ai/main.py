from fastapi import FastAPI
import requests
import os
import redis

app = FastAPI()

OLLAMA_API = os.getenv("OLLAMA_API")
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379)

@app.post("/analyze")
async def analyze(alert: dict):
    prompt = f"""
    Analyze this security alert and classify severity:

    {alert}
    """

    response = requests.post(
        f"{OLLAMA_API}/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    r.publish("alerts_enriched", result["response"])

    return {"analysis": result["response"]}