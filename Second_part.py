from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json('candidates.json')


@app.route('/')
def index():
    return render_template("index.html", candidates=data)


@app.route('/candidate/<int:uid>')
def page_index(uid):
    candidate = get_candidates(uid)
    return render_template("profile.html", candidate=candidate)


@app.route('/search/<name>')
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))


@app.route('/skills/<skill>')
def get_skills(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template("skills.html", candidates=candidates, candidates_len=len(candidates), skill=skill)


app.run()
