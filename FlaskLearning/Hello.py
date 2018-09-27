
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
	return 'hello'+'kppppp'
if __name__ == '__main__':
	 app.run()
	
