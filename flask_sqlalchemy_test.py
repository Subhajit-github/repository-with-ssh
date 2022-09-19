from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from http import HTTPStatus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/moviedb'
db = SQLAlchemy(app)
api = Api(app)

movielist = []

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    genre = db.Column(db.String(80), nullable = False)

    @staticmethod
    def add_movie(title, year, genre):
        new_movie = Movie(title= title, year=year, genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    @staticmethod
    def get_movie():
        return Movie.query.all()

    @staticmethod
    def update_movie(id, title, year, genre):
        result = Movie.query.filter_by(id = id).first()
        print(result)
        if result:
            result.title = title
            result.year = year
            result.genre = genre
        db.session.commit()
        return result

    @staticmethod
    def get_movie_by_id(id):
        return Movie.query.filter_by(id = id).first()

    @staticmethod
    def delete_movie_by_id(id):
        data = Movie.query.filter_by(id = id).delete()
        db.session.commit()
        return data



class AllMovies(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        Movie.add_movie(title=data["title"], year=data["year"], genre=data["genre"])
        return  " "


    def get(self):
        data = Movie.get_movie()
        print(data)
        for mov in data:
            tempdata = {"title": mov.title, "year": mov.year, "genre": mov.genre}
            movielist.append(tempdata)
        return jsonify(movielist)



class OneMovie(Resource):
    def get(self, id):
        data = Movie.get_movie_by_id(id)
        if data:
            print(data)
            tempdata = jsonify({"title": data.title, "year": data.year, "genre": data.genre}, {'status': HTTPStatus.OK} )
            return tempdata
        else:
            return {"message": "No Data Returned", "status": HTTPStatus.NOT_FOUND}


    def put(self, id):
        data = request.get_json()
        # print(data)
        res = Movie.update_movie(id, data["title"], data["year"],data["genre"])
        if res:
            return jsonify({"message": "Record got updated", "status": HTTPStatus.OK})
        else:
            return jsonify({"message": "No Data updated", "status": HTTPStatus.NOT_FOUND})


    def delete(self, id):
        data = Movie.delete_movie_by_id(id)
        if data == 1:
            return jsonify({"message": "Record got deleted", "status": HTTPStatus.OK})
        else:
            return jsonify({"message": "No Data Returned", "status": HTTPStatus.NOT_FOUND})

        # data = Movie.get_movie()
        # for i in range(len(data)):
        #     if i == id:
        #         tempdata = jsonify({"title": data[i-1].title, "year": data[i-1].year, "genre": data[i-1].genre})
        #         print(tempdata)
        #         return tempdata
        #         break


api.add_resource(AllMovies, "/movies")
api.add_resource(OneMovie, "/movies/<int:id>")
app.run()