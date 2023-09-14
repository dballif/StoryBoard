from flask import Flask, request, render_template
import sys
import html
sys.path.insert(0, 'tools/')
from tools import generateFrames



app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("form.html")

@app.route('/submit-starter-form', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        #Get Project Title
        project_title = html.escape(request.form.get("title"))
        #Get Project Description
        project_description = html.escape(request.form.get("description"))
        #Get Type
        storyboard_type = html.escape(request.form.get("storyboard-type"))
        #Get Full Description - Contains all the frames separated by +
        frame_descriptions = html.escape(request.form.get("storyboard-frames"))
        #Use this function to actually generate pics and return array of files
        picArray = generateFrames(project_title,frame_descriptions, storyboard_type)
    return render_template("received.html", titleContent=project_title, descriptionContent=project_description, links=picArray)

app.run()