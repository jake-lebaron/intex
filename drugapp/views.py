from django.shortcuts import render
from django.http import HttpResponse

from drugapp.models import Drug, Prescriber, State
 
# Create your views here.
def indexPageView(request) :
   return render(request, 'drugapp/index.html')

def searchPrePageView(request) :
   return render(request, 'travelpages/displayStudents.html')

def addPageView(request) :
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
   return render(request, 'drugapp/add.html', context)

def aboutPageView(request) :
   return render(request, 'drugapp/about.html')

def analysesPageView(request) :
   return render(request, 'drugapp/analyses.html')

def dashboardPageView(request) :
   return render(request, 'drugapp/dashboard.html')

def detailsDrugPageView(request, drugid) :
   jakeQuery2 = "SELECT d.drugid, p.npi, CONCAT(p.fname, ' ', p.lname) as PrescriberName FROM pd_triple t INNER JOIN pd_drugs d ON t.DrugName = d.DrugName INNER JOIN pd_prescriber p ON t.PrescriberID = p.NPI WHERE d.drugid = '" + str(drugid) + "' GROUP BY PrescriberName, d.drugid, p.npi ORDER BY drugid DESC LIMIT 10"
   data = Drug.objects.get(drugid = drugid)
   presc = Prescriber.objects.raw(jakeQuery2)

   context = {
      "record" : data,
      "top10" : presc
   }  
   return render(request, 'drugapp/detailsDrug.html', context)

def detailsPrePageView(request, npi) :
   jakeQuery3 = "select npi, d.drugid, d.drugname, qty, CONCAT(p.fname, ' ', p.lname) as PrescriberName from pd_triple t inner join pd_prescriber p on t.prescriberid = p.npi inner join pd_drugs d on d.drugname = t.drugname where p.npi = '" + str(npi)+ "' group by t.id, drugid, qty, npi, d.drugname"

   data = Prescriber.objects.get(npi=npi)
   drug = Drug.objects.raw(jakeQuery3)

   print(jakeQuery3)
   context = {
        "record" : data,
        "totaldrug" : drug
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
   allQuery = "SELECT * FROM pd_prescriber ORDER BY fname, lname, specialty"
   data = Prescriber.objects.raw(allQuery)

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

# # These views are for deleting and adding prescribers-------------------------------------------

def deletePrescriberPageView(request, npi) :
   data = Prescriber.objects.get(npi = npi)

   data.delete()
   
   return managePageView(request)
   
def addPrescriberPageView (request) :
   if request.method == 'POST':
      prescriber = Prescriber()

      prescriber.npi = request.POST['npi']
      prescriber.fname = request.POST['fname'].title()
      prescriber.lname = request.POST['lname'].title()
      prescriber.gender = request.POST['gender']
      prescriber.state = request.POST['state']
      prescriber.credentials = request.POST['credentials'].upper().replace(" ", "")
      prescriber.specialty = request.POST['specialty']
      prescriber.isopioidprescriber = request.POST['isopioidprescriber']
      prescriber.totalprescriptions = request.POST['totalprescriptions']
      prescriber.abilify = 0
      prescriber.acetaminophencodeine = 0
      prescriber.acyclovir = 0
      prescriber.advairdiskus = 0
      prescriber.aggrenox = 0
      prescriber.alendronatesodium = 0
      prescriber.allopurinol = 0
      prescriber.alprazolam = 0
      prescriber.amiodaronehcl = 0
      prescriber.amitriptylinehcl = 0
      prescriber.amlodipinebesylate = 0
      prescriber.amlodipinebesylatebenazepril = 0
      prescriber.amoxicillin = 0
      prescriber.amoxtrpotassiumclavulanate = 0
      prescriber.amphetaminesaltcombo = 0
      prescriber.atenolol = 0
      prescriber.atorvastatincalcium = 0
      prescriber.avodart = 0
      prescriber.azithromycin = 0
      prescriber.baclofen = 0
      prescriber.bdultrafinepenneedle = 0
      prescriber.benazeprilhcl = 0
      prescriber.benicar = 0
      prescriber.benicarhct = 0
      prescriber.benztropinemesylate = 0
      prescriber.bisoprololhydrochlorothiazide = 0
      prescriber.brimonidinetartrate = 0
      prescriber.bumetanide = 0
      prescriber.bupropionhclsr = 0
      prescriber.bupropionxl = 0
      prescriber.buspironehcl = 0
      prescriber.bystolic = 0
      prescriber.carbamazepine = 0
      prescriber.carbidopalevodopa = 0
      prescriber.carisoprodol = 0
      prescriber.cartiaxt = 0
      prescriber.carvedilol = 0
      prescriber.cefuroxime = 0
      prescriber.celebrex = 0
      prescriber.cephalexin = 0
      prescriber.chlorhexidinegluconate = 0
      prescriber.chlorthalidone = 0
      prescriber.cilostazol = 0
      prescriber.ciprofloxacinhcl = 0
      prescriber.citalopramhbr = 0
      prescriber.clindamycinhcl = 0
      prescriber.clobetasolpropionate = 0
      prescriber.clonazepam = 0
      prescriber.clonidinehcl = 0
      prescriber.clopidogrel = 0
      prescriber.clotrimazolebetamethasone = 0
      prescriber.colcrys = 0
      prescriber.combiventrespimat = 0
      prescriber.crestor = 0
      prescriber.cyclobenzaprinehcl = 0
      prescriber.dexilant = 0
      prescriber.diazepam = 0
      prescriber.diclofenacsodium = 0
      prescriber.dicyclominehcl = 0
      prescriber.digox = 0
      prescriber.digoxin = 0
      prescriber.diltiazem24hrcd = 0
      prescriber.diltiazem24hrer = 0
      prescriber.diltiazemer = 0
      prescriber.diltiazemhcl = 0
      prescriber.diovan = 0
      prescriber.diphenoxylateatropine = 0
      prescriber.divalproexsodium = 0
      prescriber.divalproexsodiumer = 0
      prescriber.donepezilhcl = 0
      prescriber.dorzolamidetimolol = 0
      prescriber.doxazosinmesylate = 0
      prescriber.doxepinhcl = 0
      prescriber.doxycyclinehyclate = 0
      prescriber.duloxetinehcl = 0
      prescriber.enalaprilmaleate = 0
      prescriber.escitalopramoxalate = 0
      prescriber.estradiol = 0
      prescriber.exelon = 0
      prescriber.famotidine = 0
      prescriber.felodipineer = 0
      prescriber.fenofibrate = 0
      prescriber.fentanyl = 0
      prescriber.finasteride = 0
      prescriber.floventhfa = 0
      prescriber.fluconazole = 0
      prescriber.fluoxetinehcl = 0
      prescriber.fluticasonepropionate = 0
      prescriber.furosemide = 0
      prescriber.gabapentin = 0
      prescriber.gemfibrozil = 0
      prescriber.glimepiride = 0
      prescriber.glipizide = 0
      prescriber.glipizideer = 0
      prescriber.glipizidexl = 0
      prescriber.glyburide = 0
      prescriber.haloperidol = 0
      prescriber.humalog = 0
      prescriber.hydralazinehcl = 0
      prescriber.hydrochlorothiazide = 0
      prescriber.hydrocodoneacetaminophen = 0
      prescriber.hydrocortisone = 0
      prescriber.hydromorphonehcl = 0
      prescriber.hydroxyzinehcl = 0
      prescriber.ibandronatesodium = 0
      prescriber.ibuprofen = 0
      prescriber.insulinsyringe = 0
      prescriber.ipratropiumbromide = 0
      prescriber.irbesartan = 0
      prescriber.isosorbidemononitrateer = 0
      prescriber.jantoven = 0
      prescriber.janumet = 0
      prescriber.januvia = 0
      prescriber.ketoconazole = 0
      prescriber.klorcon10 = 0
      prescriber.klorconm10 = 0
      prescriber.klorconm20 = 0
      prescriber.labetalolhcl = 0
      prescriber.lactulose = 0
      prescriber.lamotrigine = 0
      prescriber.lansoprazole = 0
      prescriber.lantus = 0
      prescriber.lantussolostar = 0
      prescriber.latanoprost = 0
      prescriber.levemir = 0
      prescriber.levemirflexpen = 0
      prescriber.levetiracetam = 0
      prescriber.levofloxacin = 0
      prescriber.levothyroxinesodium = 0
      prescriber.lidocaine = 0
      prescriber.lisinopril = 0
      prescriber.lisinoprilhydrochlorothiazide = 0
      prescriber.lithiumcarbonate = 0
      prescriber.lorazepam = 0
      prescriber.losartanhydrochlorothiazide = 0
      prescriber.losartanpotassium = 0
      prescriber.lovastatin = 0
      prescriber.lovaza = 0
      prescriber.lumigan = 0
      prescriber.lyrica = 0
      prescriber.meclizinehcl = 0
      prescriber.meloxicam = 0
      prescriber.metforminhcl = 0
      prescriber.metforminhcler = 0
      prescriber.methadonehcl = 0
      prescriber.methocarbamol = 0
      prescriber.methotrexate = 0
      prescriber.methylprednisolone = 0
      prescriber.metoclopramidehcl = 0
      prescriber.metolazone = 0
      prescriber.metoprololsuccinate = 0
      prescriber.metoprololtartrate = 0
      prescriber.metronidazole = 0
      prescriber.mirtazapine = 0
      prescriber.montelukastsodium = 0
      prescriber.morphinesulfate = 0
      prescriber.morphinesulfateer = 0
      prescriber.mupirocin = 0
      prescriber.nabumetone = 0
      prescriber.namenda = 0
      prescriber.namendaxr = 0
      prescriber.naproxen = 0
      prescriber.nasonex = 0
      prescriber.nexium = 0
      prescriber.niaciner = 0
      prescriber.nifedicalxl = 0
      prescriber.nifedipineer = 0
      prescriber.nitrofurantoinmonomacro = 0
      prescriber.nitrostat = 0
      prescriber.nortriptylinehcl = 0
      prescriber.novolog = 0
      prescriber.novologflexpen = 0
      prescriber.nystatin = 0
      prescriber.olanzapine = 0
      prescriber.omeprazole = 0
      prescriber.ondansetronhcl = 0
      prescriber.ondansetronodt = 0
      prescriber.onglyza = 0
      prescriber.oxcarbazepine = 0
      prescriber.oxybutyninchloride = 0
      prescriber.oxybutyninchlorideer = 0
      prescriber.oxycodoneacetaminophen = 0
      prescriber.oxycodonehcl = 0
      prescriber.oxycontin = 0
      prescriber.pantoprazolesodium = 0
      prescriber.paroxetinehcl = 0
      prescriber.phenobarbital = 0
      prescriber.phenytoinsodiumextended = 0
      prescriber.pioglitazonehcl = 0
      prescriber.polyethyleneglycol3350 = 0
      prescriber.potassiumchloride = 0
      prescriber.pradaxa = 0
      prescriber.pramipexoledihydrochloride = 0
      prescriber.pravastatinsodium = 0
      prescriber.prednisone = 0
      prescriber.premarin = 0
      prescriber.primidone = 0
      prescriber.proairhfa = 0
      prescriber.promethazinehcl = 0
      prescriber.propranololhcl = 0
      prescriber.propranololhcler = 0
      prescriber.quetiapinefumarate = 0
      prescriber.quinaprilhcl = 0
      prescriber.raloxifenehcl = 0
      prescriber.ramipril = 0
      prescriber.ranexa = 0
      prescriber.ranitidinehcl = 0
      prescriber.restasis = 0
      prescriber.risperidone = 0
      prescriber.ropinirolehcl = 0
      prescriber.seroquelxr = 0
      prescriber.sertralinehcl = 0
      prescriber.simvastatin = 0
      prescriber.sotalol = 0
      prescriber.spiriva = 0
      prescriber.spironolactone = 0
      prescriber.sucralfate = 0
      prescriber.sulfamethoxazoletrimethoprim = 0
      prescriber.sumatriptansuccinate = 0
      prescriber.symbicort = 0
      prescriber.synthroid = 0
      prescriber.tamsulosinhcl = 0
      prescriber.temazepam = 0
      prescriber.terazosinhcl = 0
      prescriber.timololmaleate = 0
      prescriber.tizanidinehcl = 0
      prescriber.tolterodinetartrateer = 0
      prescriber.topiramate = 0
      prescriber.toprolxl = 0
      prescriber.torsemide = 0
      prescriber.tramadolhcl = 0
      prescriber.travatanz = 0
      prescriber.trazodonehcl = 0
      prescriber.triamcinoloneacetonide = 0
      prescriber.triamterenehydrochlorothiazid = 0
      prescriber.valacyclovir = 0
      prescriber.valsartan = 0
      prescriber.valsartanhydrochlorothiazide = 0
      prescriber.venlafaxinehcl = 0
      prescriber.venlafaxinehcler = 0
      prescriber.ventolinhfa = 0
      prescriber.verapamiler = 0
      prescriber.vesicare = 0
      prescriber.voltaren = 0
      prescriber.vytorin = 0
      prescriber.warfarinsodium = 0
      prescriber.xarelto = 0
      prescriber.zetia = 0
      prescriber.ziprasidonehcl = 0
      prescriber.zolpidemtartrate = 0

      prescriber.save()

      return managePageView(request)
   else : 
      return render(request, 'drugapp/manage.html')