# person_rest_api.py: Flask Rest API code

from flask import Flask, request, jsonify
from person import Person, Response

app = Flask(__name__)

person_list = []


@app.route("/")
def welcome():
    return "Welcome to Flask Project of person model with Rest API!"


@app.route('/add', methods=['POST'])
def add_person():
    resp = Response()

    result = [person for person in person_list if person.person_id == request.form.get('id')]
    if result:
        resp.status = False
        resp.message = "Person Already Exists"
    else:
        person_obj = Person(request.form.get('id'), request.form.get('name'), request.form.get('age'))
        person_list.append(person_obj)
        resp.status = True
        resp.message = "Person created successfully"

    return jsonify(resp.__dict__)


@app.route("/<id>/delete", methods=['GET'])
def delete_person(id):
    resp = Response()

    result = [person for person in person_list if person.person_id == id]
    if result:
        person_list.remove(result[0])
        resp.status = True
        resp.message = "Person deleted successfully"
    else:
        resp.status = False
        resp.message = "Person Doesn't Exists"

    return jsonify(resp.__dict__)


@app.route("/<id>/get", methods=['GET'])
def get_person(id):
    person = [obj for obj in person_list if obj.person_id == id]
    if person:
        # There will be single person object if ID matches, hence pick 0th index element
        person = person[0]
        return jsonify(person.__dict__)
    else:
        return person


@app.route('/<id>/getDummy', methods=['GET'])
def get_dummy_person(id):
    person_obj = Person(int(id), "Dummy", 99)
    return jsonify(person_obj.__dict__)


@app.route('/getAll')
def get_all_persons():
    return jsonify([person.__dict__ for person in person_list])
