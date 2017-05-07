from flask import Flask, Response
from decimal import *
import time

getcontext().prec = 10

app = Flask(__name__)

def getPI():
	while True:
		time.sleep(10)
		f = open('PI_SAVE', 'r')
		savedPI = f.read()
		f.close()
		yield str(savedPI + '\n')
			
@app.route('/')
def sse_request():
	return Response(
		getPI(), 
		mimetype = 'text/event-stream')


if __name__ == '__main__':
	app.run(debug=True, host = 'localhost', port= 5000)
