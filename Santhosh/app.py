

from flask import Flask


app=Flask(__name__)


@app.route("/hello/<name>")
def home(name=None):
    return "Good Morning"+name



if __name__=="__main__":
    app.run(host="localhost")