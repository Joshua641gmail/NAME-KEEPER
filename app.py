from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    # Read stored data to display it
    try:
        with open('storage.txt', 'r') as f:
            data = f.read()
    except FileNotFoundError:
        data = "No data yet."
    return render_template('index.html', saved_data=data)

# Route to handle form submission (Storage capability)
@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.form.get('data')
    # Save data to a file
    with open('storage.txt', 'a') as f:
        f.write(user_data + '\n')
    return 'Data Saved! <a href="/">Go Back</a>'

if __name__ == '__main__':
    app.run(debug=True)
