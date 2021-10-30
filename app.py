from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return f"hello {name}"


@app.route('/f/<celsius>')
def greet(celsius=0):
    fahrenheit = convert_fahrenheit_to_celsius(float(celsius))
    return f"Celsius: {celsius} Fahrenheit: {fahrenheit}"


def convert_fahrenheit_to_celsius(celsius):
    """Convert fahrenheit to celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
