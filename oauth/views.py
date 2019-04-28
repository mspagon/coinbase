from django.http import HttpResponse

from cb import CoinbaseOAuth

def loginView(request):
    c = CoinbaseOAuth
    return HttpResponse('LOGIN TO COINBASE SPAGON')