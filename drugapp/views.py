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

def editPageView(request, npi) :
   jakeQuery = "WITH CTE AS (SELECT npi, specialty, ROW_NUMBER() OVER (PARTITION BY specialty ORDER BY npi DESC) AS RowNumber FROM pd_prescriber) SELECT npi, specialty FROM CTE WHERE RowNumber = 1"
   #@Professor Hilton, this was brought to you by late night Jake LeBaron and his wizardry and stroke of mad genuis. Consider this his TA application.
   data = Prescriber.objects.get(npi = npi)
   specs = Prescriber.objects.raw(jakeQuery)
   state = State.objects.all()
   
   context = {
      "record" : data,
      "state" : state,
      "our_specialties" : specs
   }  
   
   return render(request, 'drugapp/edit.html', context)

def managePageView(request) :
   data = Prescriber.objects.all()

   context = {
        "key" : data,
   }
   return render(request, 'drugapp/manage.html', context)

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
   fname = request.GET['fname'].title()
   lname = request.GET['lname'].title()
   credentials = request.GET['credentials'].upper().replace(" ", "")
   state = request.GET['state']
   specialty = request.GET['specialty']
   gender = None
   try :
      gender = request.GET['gender']
   except :
      gender = ""

   isopioidpresc = None
   try :
      isopioidpresc = request.GET['isopioidpresc']
   except :
      isopioidpresc = ""

   sQuery = 'SELECT npi, fname, lname, credentials, IsOpioidPrescriber, gender, stateabbrev, specialty FROM pd_prescriber, pd_statedata WHERE pd_prescriber.state = pd_statedata.stateabbrev'

   # print("this is inside sQuery: " + sQuery)
   if fname != '' :
      sQuery += " AND fname = '" + fname + "'"

   if isopioidpresc != '' :
      sQuery += " AND IsOpioidPrescriber = '" + isopioidpresc + "'"
      
   if lname != '' :
      sQuery += " AND lname = '" + lname + "'"

   if credentials != '' :
      sQuery += " AND credentials = '" + credentials + "'"      

   if state != '' :
      sQuery += " AND stateabbrev = '" + state + "'"     

   if gender != '' :
      sQuery += " AND gender = '" + gender + "'"  

   if specialty != '' :
      sQuery += " AND specialty = '" + specialty + "'"       

   sQuery += ' ORDER BY npi, fname, lname, credentials, IsOpioidPrescriber, gender, stateabbrev, specialty'

   print(sQuery)
   jakeQuery = "WITH CTE AS (SELECT npi, specialty, ROW_NUMBER() OVER (PARTITION BY specialty ORDER BY npi DESC) AS RowNumber FROM pd_prescriber) SELECT npi, specialty FROM CTE WHERE RowNumber = 1"
   #@Professor Hilton, this was brought to you by late night Jake LeBaron and his wizardry and stroke of mad genuis. Consider this his TA application.
   specs = Prescriber.objects.raw(jakeQuery)
   data = Prescriber.objects.raw(sQuery)
   state = State.objects.all()

   context = {
      "key" : data,
      "state" : state,
      "our_specialties" : specs
   }   
   return render(request, 'drugapp/searchPre.html', context)

def searchPrePageView(request) :
   sQuery = "WITH CTE AS (SELECT npi, specialty, ROW_NUMBER() OVER (PARTITION BY specialty ORDER BY npi DESC) AS RowNumber FROM pd_prescriber) SELECT npi, specialty FROM CTE WHERE RowNumber = 1"
   #@Professor Hilton, this was brought to you by late night Jake LeBaron and his wizardry and stroke of mad genuis. Consider this his TA application.
   specs = Prescriber.objects.raw(sQuery)

   state = State.objects.all()
   all = Prescriber.objects.all()

   context = {
      "state" : state,
      "our_specialties" : specs,
      "key" : all
   }   

   return render(request, 'drugapp/searchPre.html', context)


# These views are for first, rendering the edit prescriber page, -----------------------------------
# and second, submitting the form on that page


def updatePrescriberPageView(request) :
    if request.method == 'POST' :
        npi = request.POST['npi']

        prescriber = Prescriber.objects.get(npi=npi)

        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        prescriber.state = request.POST['state']
        prescriber.credentials = request.POST['credentials']
        prescriber.specialty = request.POST['specialty']
        prescriber.isopioidprescriber = request.POST['isopioidprescriber']
        prescriber.totalprescriptions = request.POST['totalprescriptions']

        prescriber.save()

    return managePageView(request)


import ctypes  # An included library with Python install.   


# These views are for deleting and adding prescribers-------------------------------------------

def deletePrescriberPageView(request, npi) :

   data = Prescriber.objects.get(id = npi)
   data.delete()
   ctypes.windll.user32.MessageBoxW(0, "you sher bruh?", "Your title", 1)
   return managePageView(request)
   pass
   
def addPrescriberPageView (request) :
   pass