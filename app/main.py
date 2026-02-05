from fastapi import FastAPI
import routes
import uvicorn

app = FastAPI()

app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)