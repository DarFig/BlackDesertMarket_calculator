from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola holita vecinito"


app.run(debug=True, port=8080, host='0.0.0.0')
