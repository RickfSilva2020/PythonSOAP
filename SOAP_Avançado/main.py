from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.model.primitive import String
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Configuração do logging para ver os detalhes da requisição
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)  # Isso permitirá solicitações CORS para todas as rotas

class Calculadora(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def adicionar(ctx, num1, num2):
        logging.info(f"adicionar called with: num1={num1}, num2={num2}")
        result = num1 + num2
        logging.info(f"Result: {result}")
        return result

    @rpc(Float, Float, _returns=Float)
    def subtrair(ctx, num1, num2):
        logging.info(f"subtrair called with: num1={num1}, num2={num2}")
        return num1 - num2

    @rpc(Float, Float, _returns=Float)
    def multiplicar(ctx, num1, num2):
        logging.info(f"multiplicar called with: num1={num1}, num2={num2}")
        return num1 * num2

    @rpc(Float, Float, _returns=String)
    def dividir(ctx, num1, num2):
        logging.info(f"dividir called with: num1={num1}, num2={num2}")
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return str(num1 / num2)

def add_cors_headers(environ, start_response):
    def custom_start_response(status, headers, exc_info=None):
        headers.append(('Access-Control-Allow-Origin', '*'))
        headers.append(('Access-Control-Allow-Methods', 'POST, GET, OPTIONS'))
        headers.append(('Access-Control-Allow-Headers', 'Content-Type'))
        return start_response(status, headers, exc_info)

    return custom_start_response

if __name__ == '__main__':
    soap_app = Application([Calculadora],
                           tns='calculadora.soap',
                           in_protocol=Soap11(validator='lxml'),
                           out_protocol=Soap11())

    wsgi_app = WsgiApplication(soap_app)

    def application_with_cors(environ, start_response):
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            start_response('200 OK', [
                ('Access-Control-Allow-Origin', '*'),
                ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS'),
                ('Access-Control-Allow-Headers', 'Content-Type'),
            ])
            return []
        return wsgi_app(environ, add_cors_headers(environ, start_response))

    server = make_server('0.0.0.0', 8000, application_with_cors)

    logging.info("Serviço SOAP iniciado em http://127.0.0.1:8000/")
    logging.info("WSDL disponível em http://127.0.0.1:8000/?wsdl")

    server.serve_forever()
