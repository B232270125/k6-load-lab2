import time
from flask import Flask

app = Flask(__name__)

@app.route('/fast')
def fast():
    return 'ok'

@app.route('/slow')
def slow():
    time.sleep(0.1)
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000, threaded=True)
