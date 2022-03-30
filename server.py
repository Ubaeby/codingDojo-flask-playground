from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Try typing /play!"

@app.route("/play")
def boxes():
    return render_template("options.html", times=3,color="lightblue")

@app.route('/play/<int:times>')
def box_number(times):
    return render_template("options.html", times=times)

@app.route('/play/<int:times>/<string:color>')
def box_number_colors(times, color):
    return render_template('options.html', times=times, color=color)

if __name__=="__main__":
    app.run(debug=True)