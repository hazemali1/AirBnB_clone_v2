#!/usr/bin/python3
from flask import Flask
"""
flask
"""


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
	"""
	hbnb
	"""
	return "Hello HBNB!"
if __name__ == '__main__':
	"""
	main
	"""
	app.run(host='0.0.0.0', port=5000)
