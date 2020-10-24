from flask import Flask, render_template, request, redirect, url_for
import os, pymysql, pymongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
 
 
@app.route("/")
def hello():
    return "Hello World ... again!"
 
 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)