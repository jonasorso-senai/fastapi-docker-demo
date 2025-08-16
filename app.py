from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá turma, este é meu primeiro container com FastAPI!"}

@app.get("/jonas")
def read_jonas():
    return {"message": "Olá turma, esse é o endpoint do jonas!"}
