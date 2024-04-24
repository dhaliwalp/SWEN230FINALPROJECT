from flask import Flask, render_template
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Dockerized Flask App!'

@app.route("/scores")
def get_scores():
    url = "https://www.espn.com/soccer/scoreboard"
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    match_scores = []
    for match in soup.find_all("div", class_="match-score"):
        team_names = [team.text for team in match.find_all("span", class_="short-name")]
        score = match.find("span", class_="score").text
        match_scores.append({"teams": team_names, "score": score})

    return render_template("scores.html", match_scores=match_scores)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)