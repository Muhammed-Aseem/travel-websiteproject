from django.http import HttpResponse
from django.shortcuts import render
from.models import Place,Team
def demo(request):
   obj=Place.objects.all()
   team = Team.objects.all()
   return  render(request,"index.html",{'result':obj,'team':team})


   #def addition(request):
  #x = int(request.GET["num1"])
   #y = int(request.GET["num2"])
   #add = x+y
   #sub = x-y
   #mul = x*y
   #div  = x/y

   #return render(request,"about.html",{'obj1':add,'obj2':sub,'obj3':mul,'obj4':div})



#def attent(request):
   return HttpResponse('hrllo')

#def Home(request):
   return HttpResponse("WELCOME")

#def welcome(request):
   return render(request,"welcome.html")
