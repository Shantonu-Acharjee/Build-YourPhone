from flask import Flask, render_template, request
import json
import pandas as pd



f = open('static/MobileMenu.json', 'r')
df = pd.read_csv('static/s.csv')
data = json.load(f)




app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    model = request.form.get('model')
    return render_template('index.html', df = df, model = model)





if __name__ == "__main__":
    app.run(threaded=False, debug= True, ) #host= '10.0.0.174'