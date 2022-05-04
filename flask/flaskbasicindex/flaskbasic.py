from flask import *
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello This is my first Webpage created using Flask Framework"

@app.route('/index')
def ggmg():
    return render_template("index.html")

@app.route('/about')
def goo():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
