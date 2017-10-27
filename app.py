from flask import Flask

app = Flask(__name__)

# basic route and corresponding request handler
@app.route("/")


def main():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug = True)
