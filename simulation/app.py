from flask import Flask, jsonify, Response, make_response, request
from flask_restplus import Api, Resource, fields
import json
import requests

app = Flask(__name__)
api = Api(app)

def getdecision(M,t,m,d):
	headers = {
		
		'content-type':'application/json',
		'Authorization':'ApiKey % APIKEY %'
	}

	data = '{"Mensualite":"'+m+'","taux":"'+t+'","Montant":"'+M+'","Duree":"'+d+'"}'
	response = requests.post( "https://decision-composer.ibm.com/rest/public/v1/execution/5d08e102e51fd900163a33ff/execute/v7", 
								headers=headers,
								data=data)

	#print(response)
	datastore=response.json()

	return datastore["Decision_1"]

data_in = api.model('simulation', {'Mensualite' : fields.String('0'),'taux':fields.String('0'),'Montant':fields.String('0'),'Duree':fields.String('0')})



@api.route('/simulation',methods=['POST','GET'])
class Simulation(Resource):
    #def get(self):
     #   return languages

    @api.expect(data_in)
    def post(self):
        #languages.append(api.payload)
        M=api.payload['Montant']
        t=api.payload['taux']
        m=api.payload['Mensualite']
        d=api.payload['Duree']

        result =  getdecision(M,t,m,d)
        print(result)

        return {'result' : result}, 201 
    def get(self):
    	return 200



if __name__ == '__main__':
    app.run(debug=True)