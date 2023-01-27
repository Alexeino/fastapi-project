from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    
    return {'data':{
        'name':'Manish',
        'age':24
    }}
    
@app.get("/about")
def about():
    return {'data':'about page'}