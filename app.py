#! /usr/bin/env python3
import json
from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': '400 Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': '404 Not Found'}), 404)


with open('companies.json', 'r') as file:
	companies_list = json.load(file)

companies_by_id = {}
companies_by_name = {}
for company in companies_list:
	companies_by_id[company['index']] = company['company']
	companies_by_name[company['company']] = company['index']

with open('people.json', 'r') as file:
	people_list = json.load(file)


@app.route('/hivery/api/v1.0/company/<string:company_name>', methods=['GET'])
def get_employees(company_name):
	if company_name.upper() not in companies_by_name:
		abort(400)
	company_id = companies_by_name[company_name.upper()]
	employees = []
	for person in people_list:
		if person['company_id'] == company_id:
			employees.append(person)
	return jsonify(employees)


@app.route('/hivery/api/v1.0/people/<int:id1>/<int:id2>', methods=['GET'])
def get_friends(id1, id2):
	lim = len(people_list)
	if id1 not in range(lim) or id2 not in range(lim):
		abort(400)
	p1 = people_list[id1]
	p2 = people_list[id2]
	keys = ['name', 'age', 'address', 'phone']
	person_1 = {key: p1[key] for key in keys}
	person_2 = {key: p2[key] for key in keys}
	friends_1 = [friend['index'] for friend in p1['friends']]
	friends_2 = [friend['index'] for friend in p2['friends']]
	common_friends = list(set(friends_1).intersection(friends_2))
	common_friends_selected = []
	for i in common_friends:
		friend = people_list[i]
		if friend['eyeColor'] == 'brown' and not friend['has_died']:
			common_friends_selected.append(i)
	return jsonify({'person_1': person_1,
	                'person_2': person_2,
	                'common_friends': common_friends_selected})


fruits = {'banana', 'apple', 'cucumber', 'strawberry', 'orange'}
vegetables = {'carrot', 'beetroot', 'celery'}


@app.route('/hivery/api/v1.0/people/<int:person_id>', methods=['GET'])
def get_food(person_id):
	person = people_list[person_id]
	user = dict()
	user['username'] = person['name']
	user['age'] = person['age']
	user['fruits'] = [item for item in person['favouriteFood'] if item in fruits]
	user['vegetables'] = [item for item in person['favouriteFood'] if item in vegetables]
	return jsonify(user)


if __name__ == '__main__':
	app.run(debug=True)
