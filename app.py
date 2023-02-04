from flask import Flask
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/cars')
def get_cars():
    result = run_statement("CALL get_all_cars()")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else: 
        return "Sorry, something went wrong."


app.run(debug = True)