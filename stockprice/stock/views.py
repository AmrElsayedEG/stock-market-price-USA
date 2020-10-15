from django.shortcuts import render
from . import stockapi
# Create your views here.
from django.http import HttpResponse
api_key = 'SMRUPFC8PX39RTRT'
def home(request):
    s_l = stockapi.get_symbol() #Get all symbols list
    wrong_sym = False #Default Value to know if the user searched for wrong symbol
    if request.GET: #If we have search request
        symbol = request.GET.get("symbol","") #Get value from GET
        try: #Try to get the prices for that symbol
            price = stockapi.get_price_list_daily(symbol,api_key)
            price.reverse() #Revese so we can view chart from older to newer data
        except: #If the symbol is wrong
            wrong_sym = True #Wrong Symbol and show pop-up
            price = None
    else:
        price = None
        symbol = None
    context = {
        's_l': s_l,
        'price':price,
        'symbol':symbol,
        'lenstock':len(s_l),
        'wrong_sym':wrong_sym
    }
    return render(request,'index.html',context)