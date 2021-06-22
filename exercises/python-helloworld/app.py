from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response





@app.route("/")
def hello():
    return "Hello World! I was able to do it. Yes."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
