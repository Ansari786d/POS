from fastapi import FastAPI


app = FastAPI()

items = []

@app.get("/")
def root():
    return "hello  Ansari"

@app.get("/items/")
def create_item():
    # items.append(item)
    return {"item":"message" "Item created successfully"}