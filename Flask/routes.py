from flask import Flask, render_template
app = Flask(__name__)


@app.route('/calculator')
def gotoCalculator():
    return render_template("calculator.html")

@app.route('/faq')
def gotoFaq():
    return render_template("faq.html")

@app.route('/about')
def gotoAbout():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True)
