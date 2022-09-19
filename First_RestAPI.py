from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

user_list = [{"name": "Ajay", "age": 21}, {"name": "Vijay", "age": 30}]
# user_list[0].update({"name": "Ajay", "age": 29})
# x = dict(user_list[0].items())["age"]
# print(x)
for i in user_list:
    print(i["name"])
@app.route("/", methods=["GET"])
def home():
    data = user_list
    json_data = jsonify(data)
    return  json_data

@app.route("/", methods=["POST"])
def home_post():
    data = request.get_json()
    user_list.append(data)
    return user_list

@app.route("/", methods=["DELETE"])
def home_delete():
    user_list.clear()
    return user_list

@app.route("/<int:age>", methods=["PUT"])
def home_update(age):
    print("here")
    for i in range(len(user_list)):
        if dict(user_list[i].items())["age"] == age:
            user_list[0].update({"name": dict(user_list[i].items())["name"], "age": 90})
    return user_list

app.run()