from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print("midd:"+request.GET.get('a'))