import os
from fastapi import FastAPI, Depends, HTTPException, Request, Response, Form
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="Hello welcome")

DATABASE_URL = "sqlite:///people.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LoginRequest(BaseModel):
    username: str
    password: str

def check_password(username: str, password: str) -> bool:
    return username == 'ganesh' and password == 'hero'

def auth_required(session: dict):
    if 'username' not in session:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if check_password(username, password):
        request.session['username'] = username
        return JSONResponse(content={"message": "Login success"})
    return RedirectResponse(url="/login", status_code=303)

@app.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return JSONResponse(content={"message": "Logged out"})

@app.get("/")
async def hello(request: Request):
    auth_required(request.session)
    return Response(content="<html><head><title>Give env</title></head><body><h2>Hello</h2></body></html>", media_type="text/html")

def get_age(db, name: str):
    sql = text("SELECT age FROM people WHERE name = :name")
    result = db.execute(sql, {"name": name}).fetchone()
    return result[0] if result else None

@app.get("/helloj")
@app.get("/helloj/{name}/")
@app.get("/helloj/{name}/{format}")
async def helloj(request: Request, name: str = "ABC", format: str = "json", db=Depends(get_db)):
    name = request.query_params.get("name", name)
    format = request.query_params.get("format", format)
    age = get_age(db, name.lower())
    
    if format == "json":
        if age is not None:
            return JSONResponse(content={"name": name, "age": age})
        return JSONResponse(content={"name": name, "details": "Not found"}, status_code=404)
    
    elif format == "xml":
        xml_response = f"""<?xml version="1.0"?>
                        <data><name>{name}</name>
                        <age>{age}</age></data>"""
        return Response(content=xml_response, media_type="application/xml")
    
    return JSONResponse(content={"error": "Format not recognized"}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
