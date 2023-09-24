from flask import Flask, request, jsonify
import numpy as np
import pickle
import pickle4
import sklearn

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    a1 = request.form.get('a')
    a2 = request.form.get('b')
    a3 = request.form.get('c')
    a4 = request.form.get('d')
    a5 = request.form.get('e')
    a6 = request.form.get('f')
    a7 = request.form.get('g')
    a8 = request.form.get('h')
    a9 = request.form.get('i')
    a10 = request.form.get('j')
    a11 = request.form.get('k')
    a12 = request.form.get('l')
    a13 = request.form.get('m')

    input_query = np.array([[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11), int(a12),int(a13)]])

    result = model.predict(np.array(input_query))[0]
    if result == 0:
        return jsonify({"body type": 0})
    elif(result == 1):
        return jsonify({"body type": 1})
    else:
        return jsonify({"body type": 2})


if __name__ == '__main__':
    app.run(debug=True)
