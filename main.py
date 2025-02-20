from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The purpose of our lives is to be happy.",
    "Get busy living or get busy dying.",
    "You have within you right now, everything you need to deal with whatever the world can throw at you."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/quotes')
def show_quotes():
    return render_template('quotes.html', quotes=quotes)

@app.route('/add_quote', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        new_quote = request.form['quote']
        if new_quote:
            quotes.append(new_quote)
            flash('Quote added successfully!', 'success')
            return redirect(url_for('show_quotes'))
        else:
            flash('Please enter a quote.', 'error')
    return render_template('add_quote.html')

@app.route('/delete_quote/<int:index>')
def delete_quote(index):
    if 0 <= index < len(quotes):
        quotes.pop(index)
        flash('Quote deleted successfully!', 'success')
    else:
        flash('Invalid quote index.', 'error')
    return redirect(url_for('show_quotes'))

if __name__ == '__main__':
    app.run(debug=True)
