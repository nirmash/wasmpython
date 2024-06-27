from spin_sdk.http import IncomingHandler, Request, Response, send

class IncomingHandler(IncomingHandler):
    def handle_request(self, request: Request) -> Response:

        # Make a request to the app service
        response = send(Request("GET", "http://comp1.spin.internal", {}, None))
        #print the response
        print(response.body)
        
        return Response(
            200,
            {"content-type": "text/plain"},
            bytes("Hello from app!", "utf-8")
        )
