from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():   
    return"Hola buenas tarde mi nombre es rusel quieres saber de aves "  
@app.get("/aves/{num}")
def aves (num):
    return num
