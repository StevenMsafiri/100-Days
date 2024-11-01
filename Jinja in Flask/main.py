from flask import Flask, render_template
import random
import datetime as datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year= year)

@app.route('/blog')
def blog():
    blogs_url = "https://api.npoint.io/7fac6ef9ccd680057eec"
    response = requests.get(blogs_url)
    all_blogs = response.json()
    return render_template("blog.html", blogs=all_blogs)

@app.route('/guess/<name>')
def guess(name):
    age_data = requests.get(f"https://api.agify.io?name=" + name)
    age = age_data.json()['age']

    gender_data = requests.get(f"https://api.genderize.io?name=" + name)
    gender = gender_data.json()['gender']

    return render_template("guess.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)

