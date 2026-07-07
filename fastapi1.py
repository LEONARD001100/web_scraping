from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI"
    }
    
@app.get("/about")
def about():
	return {
		"about" : "i am a uvin"
		}
