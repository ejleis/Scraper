from fastapi import FastAPI, HTTPException, Query
from bs4 import BeautifulSoup
from pydantic import BaseModel

import requests
import uvicorn

app = FastAPI(title="Simple Scraper API")

class ScrapeRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Scraper!"}


@app.post("/scrape")
def scrape(request: ScrapeRequest):
    """
    Scrape the provided URL from the JSON payload and return all <h2> text elements.
    """
    try:
        response = requests.get(request.url)
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch URL: {request.url}"
            )
        soup = BeautifulSoup(response.text, "html.parser")
        h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
        return {"url": request.url, "h2": h2_tags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)