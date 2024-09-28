from flask import Flask, render_template
import yaml

app = Flask(__name__)

global content
with open('src/content.yaml', 'r') as file:
    resume_content = yaml.safe_load(file)

@app.route('/')
def index():
    return render_template('index.html', resume=resume_content)

@app.route('/resume')
def resume():
    return render_template('resume.html', resume=resume_content)

@app.route('/projects')
def projects():
    return render_template('projects.html', resume=resume_content)

if __name__ == '__main__':
    app.run(debug=True)
