from django.shortcuts import render
import json

def index(request):
    """uso request.GET.get para pegar os dados em JSON da API, com retorno no formato
    {
    "query": "24.48.0.1",
    "status": "success",
    "country": "Canada",
    "regionName": "Quebec",
    "city": "Montreal",
    "zip": "H1K",
    "lat": 45.6085,
    "lon": -73.5493
    }   """
    res = request.GET.get('http://ip-api.com/json/24.48.0.1?fields=24825')
    #Veriicar se esse request está sendo armazenado corretamente
    json_string = json.dumps(res)
    local_geo = json.loads(json_string)
    #usando json.dumps e loads para fazer as conversões, pois só o loads retorna um objeto vazio
    #investigar qual o motivo do objeto vazia, se o problema ocorre na conversão ou no request
    return render(request, 'index.html', {'data':local_geo})