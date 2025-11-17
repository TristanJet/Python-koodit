from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/prime_number/<int:n>")
def isPrime(n):
    if n < 0: return obj(n, False)
    for i in range(2, n):
        if n % i == 0:
            return obj(n, False)

    return obj(n, True)

def obj(n, prime) -> dict:
    return {
        "Number": n,
        "isPrime": prime,
    }
