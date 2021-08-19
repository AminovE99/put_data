import json

import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/data/{account_number}/{phone_number}/{name}")
async def get_data(account_number, phone_number, name):
    with open('data.csv', 'a', newline='') as f:
        data = {'account_number': account_number, 'phone_number': phone_number, 'name': name}
        f.write(f'{json.dumps(data)}\n')
    return 'ok'


if __name__ == "__main__":
    uvicorn.run("manage:app", host="0.0.0.0", port=8080, log_level="info")
