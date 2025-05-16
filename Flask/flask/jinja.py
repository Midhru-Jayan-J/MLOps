from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to the home page</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method =='POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method =='POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

@app.route('/success/<score>')
def success(score):
    return "The marks u got is " + score
    


if __name__ == "__main__":
    app.run(debug=True)