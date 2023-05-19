# {e0a8f641eec576db55848eb85593028a}
# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import aiohttp

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_weather(request: Request):
    # Location and API Key
    location = "New York"
    api_key = "e0a8f641eec576db55848eb85593028a"

    # API URL
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    print(url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)

    # Extract weather information from the response
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    weather_description = data["current"]["condition"]["text"]

    # Render the HTML template with weather data
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "temperature": temperature, "humidity": humidity, "description": weather_description},
    )
