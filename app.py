from flask import Flask

PORT = 8080

app = Flask(__name__)

@app.route("/")
def root():
  return "Hello world"


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)