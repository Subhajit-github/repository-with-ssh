from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

recipes = [{"id": 1, "name": "Dosa", "description": "This is recipe for masala dosa"},
           {"id": 2, "name": "chapati", "description": "Recipe for Chapati"},
           {"id": 3, "name": "Rice", "description": "Recipe for Rice"}]


class AllRecipes(Resource):
    def get(self):
        return jsonify(recipes)

    def post(self):
        post_data = request.get_json()
        recipes.append(post_data)
        return jsonify(recipes)


class OneRecipe(Resource):
    def get(self, recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                return jsonify(recipe)
        else:
            return jsonify("message: ID not found")

    def put(self, recipe_id):
        data = request.get_json()
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                recipe["description"] = data["description"]
        return jsonify(recipes)

    def delete(self, recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                recipes.remove(recipe)
        return jsonify(recipes)


api.add_resource(AllRecipes, "/recipes")
api.add_resource(OneRecipe, "/recipes/<int:recipe_id>")
app.run()