from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

recipes = [{"id": 1, "name": "Dosa", "description": "This is recipe for masala dosa"},
           {"id": 2, "name": "chapati", "description": "Recipe for Chapati" },
           {"id": 3, "name": "Rice", "description": "Recipe for Rice" }]


@app.route("/recipes", methods=["GET"])
def recipes_all():
    return jsonify(recipes)


@app.route("/recipes/<int:id>", methods=["GET"])
def recipe_get_id(id):
    print(id)
    for recipe in recipes:
        if recipe["id"] == id:
            return jsonify(recipe)
    else:
        return ("Recipe not Found")


@app.route("/recipes/<int:id>", methods=["DELETE"])
def recipe_delete_id(id):
    for i in recipes:
        if i["id"] == id:
            recipes.remove(i)
    return jsonify(recipes)


@app.route("/recipes/<int:id>", methods=["PUT"])
def recipe_put_id(id):
    data = request.get_json()
    for i in recipes:
        if i["id"] == id:
            i["description"] = data["description"]
    return recipes


@app.route("/recipes", methods=["POST"])
def recipe_post():
    post_data = request.get_json()
    recipes.append(post_data)
    return recipes

app.run()