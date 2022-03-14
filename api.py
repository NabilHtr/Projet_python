from turtle import title
from flask import Flask
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


import pymongo
from flask_mongoengine import MongoEngine


'''
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="Films" 
)

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS test")

cursor.execute("INSERT INTO test(nom, prenom, age, taille) VALUES('Jad', 'Salloum', 20, 195)")

cursor.execute("SELECT * FROM test")

result = cursor.fetchall()

print(result)

db.close()
'''


app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'db': 'Films',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class HelloWorld(Resource):
    def get(self , id):
        
        data = pd.read_csv('Films.csv')  
        data = data.to_dict()
        return {'data': data}, 200

    
    
    def put(self , id):
        
        
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('title', required=True)  # add args
        parser.add_argument('rating', required=True)
        parser.add_argument('ranking', required=True)
        parser.add_argument('director', required=True)  # add args
        parser.add_argument('actors', required=True)
        parser.add_argument('country', required=True)
        parser.add_argument('language', required=True)  # add args
        parser.add_argument('date_sortie', required=True)
        parser.add_argument('production', required=True)
        parser.add_argument('synopsis', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('Films.csv')
        
        if args['title'] in list(data['title']):

            # select our film
            user_data = data[data['title'] == args['title']]

            # update film's rating
            user_data['rating'] = args['rating']
            
            # save back to CSV
            data.to_csv('Films.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['title']}' user not found."
            }, 404

    
    
    
    def delete(self , id):
        return {'delete' : str(id)}

    
    
    
    def post(self , id):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('title', required=True)  # add args
        parser.add_argument('rating', required=True)
        parser.add_argument('ranking', required=True)
        parser.add_argument('director', required=True)  # add args
        parser.add_argument('actors', required=True)
        parser.add_argument('country', required=True)
        parser.add_argument('language', required=True)  # add args
        parser.add_argument('date_sortie', required=True)
        parser.add_argument('production', required=True)
        parser.add_argument('synopsis', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        
        data = pd.read_csv('Films.csv')

        
        #Vérification de l'existence du film dans notre df

        if (args['title'] in data['title']):
            return {
                'message': f"'{args['title']}' already exists."
            }, 401
        else:
            
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'title' : args['title'],
                'rating' : args['rating'],
                'ranking' : args['ranking'],
                'director' : args['director'],
                'actors' : args['actors'],
                'country' : args['country'],
                'language' : args['language'],
                'date_sortie' : args['date_sortie'],
                'production' : args['production'],
                'synopsis' : args['synopsis']
        })



        
        data = data.append(new_data, ignore_index=True)
        
        data.to_csv('Films.csv', index=False)
        
        return {'data': data.to_dict()}, 200  # return data with 200 OK





api.add_resource(HelloWorld , '/<id>')


class User(db.Document):
    name = db.StringField()
    email = db.StringField()



if __name__ == '__main__':
    app.run() 

