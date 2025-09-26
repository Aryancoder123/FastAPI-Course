import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f"Request: {request.url.path} completed in {duration:.5f} seconds")
        return response


app = FastAPI()

app.add_middleware(TimerMiddleware)


@app.get("/hello")
async def index():
    for i in range(100000):
        pass
    return {"message": "Hello, World!"}
