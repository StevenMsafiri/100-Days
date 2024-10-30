import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1 style='text-align:center; color:purple'>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='450px' height='450px' style=''> ")

@app.route('/result/<int:number>')
def user_guess(number):
    answer = random.randint(1, 9)
    if number == answer:
        return (f"<h1 style='color:green'> You guessed correctly {number}! </h1>"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='450px' height='450px>")

    elif number > answer:
        return (f"<h1 style='color:purple'> Too high, Try again! </h1>"
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='450px' height='450px>")

    else:
        return (f"<h1 style='color:red'> Too low, Try again! </h1>"
         f"<img src='media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='450px' height='450px>")

if __name__ == '__main__':
    app.run(debug=True)