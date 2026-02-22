from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow any website to call your API
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],  # Fixed: list of separate strings
    allow_headers=["*"],
    expose_headers=["*"],         # allow client to see all response headers (not strictly needed here)
)

@app.get("/api/version")
async def get_version(request: Request, response: Response):
    # Read incoming header (check)
    user_email = '22f1000821@ds.study.iitm.ac.in'

    # Echo it back in response header if present
    if user_email:
        response.headers["X-User-Email"] = user_email

    return {"version": "0.16.3"}
