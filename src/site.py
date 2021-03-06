"""Creates a simple website for CI/CD demo purposes"""
from flask import Flask, render_template
app = Flask(__name__)
client = app.test_client()


@app.route("/")
def index():
    """Renders site index"""
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0')
