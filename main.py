from fastapi import FastAPI


app = FastAPI()

items = []

@app.get("/")
def root():
    return "Welcome To Pos Solution API"

@app.get("/sale")
async def sale():
    return {"item": "message" "sale created successfully"}

@app.get("/supplier")
def supplier(item:str):
    return  {"item":"message" "supplier created successfully"}

@app.get("/product")
def product(item:str):
    return  {"item":"message" "product created successfully"}
@app.get("/purchase")
def purchase(item:str):
    return  {"item":"message" "purchase created successfully"}      


@app.get("/stock")
def stock(item:str):
    return  {"item":"message" "stock created successfully"}      

@app.get("/report")
def report(item:str):
    return  {"item":"message" "report created successfully"}  

@app.get("/hrm")
def hrm(item:str):
    return  {"item":"message" "hrm created successfully"}