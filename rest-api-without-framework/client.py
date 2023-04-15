import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def create_resources():
	new_std={
	'name':'Dhoni',
	'rollno':105,
	'marks':9
	}
	resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
	print(resp.status_code)
	print(resp.json())


def get_resource(id=None):
	data={}
	if id is not None:
		data={'id':id}
	resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(resp.status_code)
	print(resp.json())

def update_resource(id):
	new_data={
	'id':id,
	'marks':30
	}
	resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
	print(resp.status_code)
	print(resp.json())

def delete_resource(id):
	data={
	'id':id,
	'marks':30
	}
	resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(resp.status_code)
	print(resp.json())

# get_resourse(2)
# create_resource()
# update_resource(1)
delete_resource(1)




