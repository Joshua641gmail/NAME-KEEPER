from tkinter.font import names

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    # Read stored data to display it
    try:
        with open('storage.txt', 'r') as f:
            names = f.read().strip().split('\n') if f.read().strip() else []
    except FileNotFoundError:
        names = []
    return render_template('index.html', names=names)

# Route to handle form submission (Storage capability)
@app.route('/save', methods=['POST'])
def save():
    user_data = request.form.get('user_content')
    if user_data:
        with open('storage.txt', 'a') as f:
            f.write(user_data + '\n')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
