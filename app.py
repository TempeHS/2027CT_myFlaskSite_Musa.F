from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/fast-and-reliable")
def fast_and_reliable():
    return render_template("fast.html")


@app.route("/easy")
def easy():
    return render_template("easy.html")


@app.route("/sketch")
def sketch():
    return render_template("sketch.html")


@app.route("/colour")
def colour():
    return render_template("colour.html")


@app.route("/anatomy")
def anatomy():
    return render_template("anatomy.html")


@app.route("/about me")
def about_me():
    return render_template("about me.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("sign up.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
