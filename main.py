from flask import Flask, render_template

app = Flask(__name__)  #creating a flask instance


@app.route("/")  #helps you to do routing, whenever the home page is called, the below function will be executed.
def home():
    return render_template("index.html")


@app.route("/<name>")  #helps you to do routing, whenever the home page is called, the below function will be executed.
def user(name):
    return render_template("index.html", my_name = name)

@app.route("/info")
def info_page():
    return render_template("info.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")



app.run()