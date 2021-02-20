from flask import Flask, request,redirect, url_for, render_template, send_file
import json
import random
import datetime
import hashlib
from flask_cors import CORS

host_ip=input("Enter ip: ")
current="0"



def md5_hash(data):
  x=hashlib.md5(str(data).encode())
  x=x.hexdigest()
  return x




#temp 97 99

def empl():
	temp = random.randrange(96,100,1)
	sugar=random.randrange(100,210,1)
	if sugar>140:
		sugar=random.randrange(100,210,1)
	
	oxygen=random.randrange(95,100,1)
	if oxygen<96:
		oxygen=random.randrange(95,100,1)
	
	beat=random.randrange(75,130,1)
	
	breath=random.randrange(18,32,1)
	
	return [temp,sugar,oxygen ,beat,breath]





def all():
	global previous
	global current
	data=[]
	for i in range(10):
		data.append(empl())
	time=datetime.datetime.now()
	previous=current
	current=md5_hash(str(data)+str(time))
	msg={
	"data":data,
	"time":str(time),
	"previous_hash":previous,
	"current_hash":current
	}
	return msg



def one():
	global previous
	global current
	data=empl()
	time=datetime.datetime.now()
	previous=current
	current=md5_hash(str(data)+str(time))
	msg={
	"data":data,
	"time":str(time),
	"previous_hash":previous,
	"current_hash":current
	}
	return msg

	

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/a')
def homea():
 return render_template('employees.html')


@app.route('/employee/<sorc>')
def employee(sorc):
 if(sorc=="all"):
 	return json.dumps(all())
 else:
    return json.dumps(one())
 
@app.route('/get_image/<sorc>')
def get_image(sorc):
    filename = sorc+'.png'
    return send_file(filename,mimetype='image/png')
 
 
 

if __name__ == '__main__': 
 #app.run(debug = True)
 app.run(host = host_ip, port='5000')
