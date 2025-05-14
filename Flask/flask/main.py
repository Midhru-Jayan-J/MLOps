from flask import Flask,render_template  #render_template - used to match the html files in templates section

app=Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to the home page</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)