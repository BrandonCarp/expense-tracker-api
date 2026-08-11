from fastapi import FastAPI


def create_app() -> FastAPI:
  app = FastAPI()
  
  @app.get("/")
  def read_root():
    return {"status": "ok"}
  
  @app.get("/health")
  def health():
    return {"status": "healthy"}

  return app


app = create_app()