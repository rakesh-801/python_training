from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shared_content = ""

@app.route("/")
def home():
    return redirect(url_for("updatefortoday"))

@app.route("/updatefortoday", methods=["GET", "POST"])
def updatefortoday():
    global shared_content
    if request.method == "POST":
        shared_content = request.form.get("content", "")
        return redirect(url_for("updatefortoday"))
    
    return render_template("updatefortoday.html", content=shared_content)

@app.route("/share", methods=["GET"])
def share():
    global shared_content
    return render_template("share.html", content=shared_content)

@app.route("/clearnotepadtxt", methods=["GET"])
def clearnotepadtxt():
    global shared_content
    shared_content = ""
    return redirect(url_for("updatefortoday"))

if __name__ == "__main__":
    app.run(debug=True)