from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"
    #return render_template("index.html") # "Hello, World!"

@app.route("/user/<name>")
def greet_user(name):
    return "<h2>Hello, %s!" % name

@app.route("/user")
def bad_req():
    return "<h1>Bad Request</h1", 400

if __name__=="__main__":
    app.run(debug=True)

