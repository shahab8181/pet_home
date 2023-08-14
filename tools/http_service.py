from django.http import HttpRequest

def UserIp(request: HttpRequest):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR') 
    if user_ip is not None:
        return user_ip
    else:
        return request.META.get('REMOTE_ADDR')