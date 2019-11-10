from flask import Flask, render_template

app = Flask('example_4')


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')


app.run(debug=True)
