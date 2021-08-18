import json

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi import Request

app = FastAPI()


@app.post("/data")
async def get_data(request: Request):
    with open('data.csv', 'a', newline='') as f:
        data = await request.json()
        f.write(f'{json.dumps(data)}\n')
    return await request.json()


if __name__ == "__main__":
    uvicorn.run("manage:app", host="0.0.0.0", port=8080, log_level="info")
