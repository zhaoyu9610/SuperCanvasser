class CORS_Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
#        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Origin'] = 'http://localhost:4200'
        response['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
        response['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
        response["Access-Control-Allow-Credentials"] = "true"
        return response
