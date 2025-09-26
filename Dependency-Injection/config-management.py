from fastapi import FastAPI, Depends


class Settings:
    def __init__(self):
        self.api_key = "my-secret-api"
        self.debug = True


def get_settings():
    return Settings()


app = FastAPI()


@app.get("/config")
def get_settings(settings: Settings = Depends(get_settings)):
    return {"api_key": settings.api_key}
