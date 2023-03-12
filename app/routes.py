from flask import Flask

app = Flask(__name__)


@app.get("/")
def about_me():
    me = {
        "first_name": "Scott",
        "last_name": "Stevens",
        "hobbies": "Flying drones",
        "active": True    
    }

    return me
