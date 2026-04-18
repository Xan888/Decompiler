from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    message: str

@app.post("/my-endpoint")
def handle_request(body: RequestBody):
    # Do whatever you need here
    return {"result": "your response here"}
