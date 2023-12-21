from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	data = {
			  "userId": 1,
			  "id": 1,
			  "title": "delectus aut autem",
			  "completed": False
			}
	return jsonify(data), 201

if __name__ == '__main__':
	app.run()