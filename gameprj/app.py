from flask import Flask, render_template, request
import random

app = Flask(__name__)

# store a random number when the app starts
secret_number = random.randint(1, 20)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess_game():
    message = ""
    if request.method == 'POST':
        try:
            user_guess = int(request.form['guess'])
            global secret_number

            if user_guess < secret_number:
                message = "Too low! Try again."
            elif user_guess > secret_number:
                message = "Too high! Try again."
            else:
                message = "🎉 Correct! You guessed the number!"
                secret_number = random.randint(1, 20)  # reset for next round
        except ValueError:
            message = "Please enter a valid number!"

    return render_template('guess.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
