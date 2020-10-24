from flask import Flask
import os

# for env.py set up
if os.path.exists("env.py"):
    import env
app = Flask(__name__)


# initialise Users database
@app.route("/")
def hello():
    return "Hello world... again!"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
