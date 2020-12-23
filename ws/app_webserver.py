
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '%}\xc0\xb5\xc9\xfd\xa8t\xed\x1a&\\\x9e\xfde3\xe4\xb88\xa0:\xb7\xe0\xd9'


@app.route('/')
def index():
    return render_template('index.html')


app.run()
