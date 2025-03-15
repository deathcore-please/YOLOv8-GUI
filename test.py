from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/test/")
async def test_endpoint(name: str = Form(...)):
    return {"name": name}
