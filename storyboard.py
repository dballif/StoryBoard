from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("form.html")

@app.route('/submit-starter-form', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       return "Your name is "+first_name + last_name
    return render_template("form.html")

app.run()