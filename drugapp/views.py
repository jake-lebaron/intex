from django.shortcuts import render
from django.http import HttpResponse

from drugapp.models import Drug, Prescriber
 
# Create your views here.
def indexPageView(request) :
   return render(request, 'drugapp/index.html')


def searchPrePageView(request) :
   return render(request, 'travelpages/displayStudents.html')

def addPageView(request) :
   return render(request, 'drugapp/add.html')

def aboutPageView(request) :
   return render(request, 'drugapp/about.html')

def analysesPageView(request) :
   return render(request, 'drugapp/analyses.html')

def dashboardPageView(request) :
   return render(request, 'drugapp/dashboard.html')

def detailsDrugPageView(request) :
   data = Drug.objects.all()

   context = {
        "key" : data,
   }

   return render(request, 'drugapp/detailsDrug.html', context)

def detailsPrePageView(request) :
   data = Prescriber.objects.all()

   context = {
        "key" : data,
   }

   return render(request, 'drugapp/detailsPre.html', context)

def editPageView(request) :
   return render(request, 'drugapp/edit.html')

def managePageView(request) :
   return render(request, 'drugapp/manage.html')

def searchDrugPageView(request) :
   data = Drug.objects.all()

   context = {
        "key" : data,
   }

   return render(request, 'drugapp/searchDrug.html', context)

def lookupDrugPageView(request) :
   print("Now looking at drug page")
   drugname = request.GET['drugname'].upper()
   isopioid = None
   try :
      isopioid = request.GET['isopioid']
   except :
      isopioid = ""

   print("this is inside the isopiod variable" + "'" + isopioid + "'")
   sQuery = 'SELECT drugid, drugname, isopioid FROM pd_drugs WHERE'

   if (drugname != '') & (isopioid != '') :
      sQuery += " drugname LIKE '%%" + drugname + "%%'" + " AND isopioid = '" + isopioid + "'" 
   
   elif (drugname != '') & (isopioid == '') :
      sQuery += " drugname LIKE '%%" + drugname + "%%'"

   elif (drugname == '') & (isopioid != '') :
      sQuery += " isopioid = '" + isopioid + "'" 

   sQuery += ' ORDER BY drugid, drugname, isopioid'

   print(sQuery)
   data = Drug.objects.raw(sQuery)

   context = {
      "key" : data
   }
   return render(request, 'drugapp/searchDrug.html', context)

def searchPrePageView(request) :
   return render(request, 'drugapp/searchPre.html') 