from django.shortcuts import render, redirect
from . import stockapi
from .models import DailyPrice
from django.db import IntegrityError
api_key = 'SMRUPFC8PX39RTRT' #API Key



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

#Rest API
from rest_framework import generics
from .serializers import DailyPriceSerializer
from .models import DailyPrice

class symbolData(generics.ListAPIView):
    queryset = DailyPrice.objects.all() #Gett All objects
    serializer_class = DailyPriceSerializer #add serializer

    def get_queryset(self, *args, **kwargs): #Get Symbol from url
        try: #Check if we have the latest prices saved on our db or not
            price = stockapi.get_price_list_daily(self.kwargs.get('symbol'), api_key) #Get last 100 prices for symbol
            if price: #If symbol Valied
                for i in price:
                    try:
                        DailyPrice.objects.get(symbol=self.kwargs.get('symbol'), date=i[0]) #Check whether we have the last date in our db as the last date in the fresh data from api
                    except: #If we don't have refreshed data add them to our db
                        new = DailyPrice(symbol=self.kwargs.get('symbol'), date=i[0], open=i[2], high=i[4], low=i[1], close=i[3])
                        new.save() #Save
        except: #If the symbol is wrong pass and print blank list
            pass
        res = self.queryset.filter(symbol=self.kwargs.get('symbol')) #Get all stock price for particular symbol
        return res #return data to api