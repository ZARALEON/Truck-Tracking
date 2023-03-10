import json

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    with open('./files/data.txt', 'r') as f:
        try:
            data_list = f.read().split('\n')
            data = []
            for line in data_list:
                if not line:
                    continue
                line = line.strip()
                dic = {
                    "x": line.split(',')[1],
                    "y": line.split(',')[0]
                }
                data.append(dic)
        except:
            data = []
    return render_template('index.html', data=json.dumps(data))


if __name__ == '__main__':
    app.run()
