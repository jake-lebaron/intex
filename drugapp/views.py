from django.shortcuts import render
from django.http import HttpResponse

from drugapp.models import Drug, Prescriber, State
 
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
   data = Drug.objects.all()

   context = {
      "key" : data,
   }

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

   elif (drugname == '') & (isopioid == '') :
      return render(request, 'drugapp/searchDrug.html', context)

   sQuery += ' ORDER BY drugid, drugname, isopioid'

   print(sQuery)
   data = Drug.objects.raw(sQuery)

   context = {
      "key" : data
   }
   return render(request, 'drugapp/searchDrug.html', context)

def lookupPrescPageView(request) :
   print("Now looking at presc page")
   fname = request.GET['fname'].upper()
   lname = request.GET['lname'].upper()
   credentials = request.GET['credentials'].upper().replace(" ", "")
   state = request.GET['state']
   specialty = request.GET['specialty']

   # print("this is inside the isopiod variable" + "'" + isopioid + "'")
   sQuery = 'SELECT npi, fname, lname, credentials, stateabbrev, specialty FROM pd_prescriber, pd_statedata WHERE pd_prescriber.state = pd_statedata.stateabbrev'

   if fname != '' :
      sQuery += " AND first_name = '" + fname + "'"
      
   if lname != '' :
      sQuery += " AND last_name = '" + lname + "'"

   if credentials != '' :
      sQuery += " AND credentials = '" + credentials + "'"      

   if state != '' :
      sQuery += " AND stateabbrev = '" + state + "'"     

   if specialty != '' :
      sQuery += " AND specialty = '" + specialty + "'"       

   sQuery += ' ORDER BY npi, fname, lname, credentials, stateabbrev, specialty'

   print(sQuery)
   data = Prescriber.objects.raw(sQuery)

   context = {
      "key" : data,
   }   
   return render(request, 'drugapp/searchPresc.html', context)

def searchPrePageView(request) :
   sQuery = "WITH CTE AS (SELECT npi, specialty, ROW_NUMBER() OVER (PARTITION BY specialty ORDER BY npi DESC) AS RowNumber FROM pd_prescriber) SELECT npi, specialty FROM CTE WHERE RowNumber = 1"
   #Professor Hilton, this was brought to you by late night Jake LeBaron and his random stroke of mad genuis. Consider this his TA application.
   specs = Prescriber.objects.raw(sQuery)

   state = State.objects.all()

   context = {
      "state" : state,
      "our_specialties" : specs
   }   

   return render(request, 'drugapp/searchPre.html', context) 