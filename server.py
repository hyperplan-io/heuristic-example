from flask import Flask, request, jsonify
from algorithm import Algorithm

app = Flask(__name__)
algorithm = Algorithm()

@app.route("/", methods = ["POST"])
def predict():
    json_data = request.json
    text = json_data['content']
    return jsonify(algorithm.predict(text))

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
