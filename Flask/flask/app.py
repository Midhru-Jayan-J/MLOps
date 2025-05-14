from flask import Flask

app=Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to this Flask Webpage"

@app.route("/index")
def Index():
    return "Welcome to the index page"

if __name__ =="__main__":
    app.run(debug=True)