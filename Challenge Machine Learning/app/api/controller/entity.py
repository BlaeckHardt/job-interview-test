from flask_restx import Resource, Namespace, fields
from flask import request

from app.api.dtos.dto_entity import Dto
from app.api.endpoints.function_entity import procesar_lista

api = Dto.api

api = Namespace('NER', description='NER operations')
dto_model = api.model('NERModel', {
    'data': fields.String(required=True, description='The data field in JSON')
})

@api.route('/NER', methods=['POST'])
class echolist(Resource):
    @api.doc("NER")
    @api.expect(dto_model)
    def post(self):
        json_data = request.get_json()
        oraciones = json_data["oraciones"]
        resultado = procesar_lista(oraciones)

        return {"resultado":resultado}
