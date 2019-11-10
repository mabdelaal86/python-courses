from flask import Flask

app = Flask('example_2')


@app.route('/')
@app.route("/index")
def index():
    return "Hello, Welcome in Resala Foundation."


@app.route("/home")
def home():
    return """
    <html>
        <head><title>home</title></head>
        <body><h1>Welcome in Resala</h1></body>
    </html>
    """


@app.route("/home2")
def home2():
    res = """
    <html>
        <head><title>home 2</title></head>
        <body>
    """

    for i in range(1, 7):
        res += f"<h{i}>Resala my second home</h{i}>"
    
    res += """
    </body>
    </html>
    """
    return res


app.run()
