
from django.http import HttpResponse
def home_page(request):
    print("home page requested")
    return HttpResponse("<h1>This is for APIS web, Welcome to my page, Thank you!</h1>")