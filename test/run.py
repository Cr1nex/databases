import json
from flask import Flask, jsonify
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['world']
countries1 = db.countries1

app = Flask(__name__)

@app.route('/world/api/v1.0/countries/<code>', methods=['GET'])
def countryByCode(code):
    return jsonify(countries1.find_one({"_id": code}))

@app.route('/world/api/v1.0/countries', methods=['GET'])
def countries():
    return jsonify(countries1.find({}))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
