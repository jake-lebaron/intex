from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=14, unique=True)
    stateabbrev = models.CharField(primary_key=True, max_length=2, unique=True)
    population = models.IntegerField(unique=False)
    deaths = models.IntegerField(unique=False)

    class Meta:
        db_table = "pd_statedata"

    def __str__(self):
        return (self.state)

class Drug(models.Model):
    drugid = models.IntegerField(primary_key=True, unique=True)
    drugname = models.CharField(primary_key=False, max_length=30, unique=True)
    isopioid = models.CharField(max_length=5, unique=False)

    class Meta:
        db_table = "pd_drugs"

    def __str__(self):
        return (self.drugname)

class Prescriber(models.Model):
    npi = models.IntegerField(primary_key=True, unique=True)
    fname = models.CharField(max_length=11, unique=False)
    lname = models.CharField(max_length=11, unique=False)
    gender = models.CharField(max_length=1, unique=False)
    state = models.CharField(max_length=2, unique=True)
    credentials = models.CharField(max_length=20, unique=False)
    specialty = models.CharField(max_length=62, unique=False)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField(unique=False)
    abilify = models.IntegerField(unique=False)
    acetaminophencodeine = models.IntegerField(unique=False)
    acyclovir = models.IntegerField(unique=False)
    advairdiskus = models.IntegerField(unique=False)
    aggrenox = models.IntegerField(unique=False)
    alendronatesodium = models.IntegerField(unique=False)
    allopurinol = models.IntegerField(unique=False)
    alprazolam = models.IntegerField(unique=False)
    amiodaronehcl = models.IntegerField(unique=False)
    amitriptylinehcl = models.IntegerField(unique=False)
    amlodipinebesylate = models.IntegerField(unique=False)
    amlodipinebesylatebenazepril = models.IntegerField(unique=False)
    amoxicillin = models.IntegerField(unique=False)
    amoxtrpotassiumclavulanate = models.IntegerField(unique=False)
    amphetaminesaltcombo = models.IntegerField(unique=False)
    atenolol = models.IntegerField(unique=False)
    atorvastatincalcium = models.IntegerField(unique=False)
    avodart = models.IntegerField(unique=False)
    azithromycin = models.IntegerField(unique=False)
    baclofen = models.IntegerField(unique=False)
    bdultrafinepenneedle = models.IntegerField(unique=False)
    benazeprilhcl = models.IntegerField(unique=False)
    benicar = models.IntegerField(unique=False)
    benicarhct = models.IntegerField(unique=False)
    benztropinemesylate = models.IntegerField(unique=False)
    bisoprololhydrochlorothiazide = models.IntegerField(unique=False)
    brimonidinetartrate = models.IntegerField(unique=False)
    bumetanide = models.IntegerField(unique=False)
    bupropionhclsr = models.IntegerField(unique=False)
    bupropionxl = models.IntegerField(unique=False)
    buspironehcl = models.IntegerField(unique=False)
    bystolic = models.IntegerField(unique=False)
    carbamazepine = models.IntegerField(unique=False)
    carbidopalevodopa = models.IntegerField(unique=False)
    carisoprodol = models.IntegerField(unique=False)
    cartiaxt = models.IntegerField(unique=False)
    carvedilol = models.IntegerField(unique=False)
    cefuroxime = models.IntegerField(unique=False)
    celebrex = models.IntegerField(unique=False)
    cephalexin = models.IntegerField(unique=False)
    chlorhexidinegluconate = models.IntegerField(unique=False)
    chlorthalidone = models.IntegerField(unique=False)
    cilostazol = models.IntegerField(unique=False)
    ciprofloxacinhcl = models.IntegerField(unique=False)
    citalopramhbr = models.IntegerField(unique=False)
    clindamycinhcl = models.IntegerField(unique=False)
    clobetasolpropionate = models.IntegerField(unique=False)
    clonazepam = models.IntegerField(unique=False)
    clonidinehcl = models.IntegerField(unique=False)
    clopidogrel = models.IntegerField(unique=False)
    clotrimazolebetamethasone = models.IntegerField(unique=False)
    colcrys = models.IntegerField(unique=False)
    combiventrespimat = models.IntegerField(unique=False)
    crestor = models.IntegerField(unique=False)
    cyclobenzaprinehcl = models.IntegerField(unique=False)
    dexilant = models.IntegerField(unique=False)
    diazepam = models.IntegerField(unique=False)
    diclofenacsodium = models.IntegerField(unique=False)
    dicyclominehcl = models.IntegerField(unique=False)
    digox = models.IntegerField(unique=False)
    digoxin = models.IntegerField(unique=False)
    diltiazem24hrcd = models.IntegerField(unique=False)
    diltiazem24hrer = models.IntegerField(unique=False)
    diltiazemer = models.IntegerField(unique=False)
    diltiazemhcl = models.IntegerField(unique=False)
    diovan = models.IntegerField(unique=False)
    diphenoxylateatropine = models.IntegerField(unique=False)
    divalproexsodium = models.IntegerField(unique=False)
    divalproexsodiumer = models.IntegerField(unique=False)
    donepezilhcl = models.IntegerField(unique=False)
    dorzolamidetimolol = models.IntegerField(unique=False)
    doxazosinmesylate = models.IntegerField(unique=False)
    doxepinhcl = models.IntegerField(unique=False)
    doxycyclinehyclate = models.IntegerField(unique=False)
    duloxetinehcl = models.IntegerField(unique=False)
    enalaprilmaleate = models.IntegerField(unique=False)
    escitalopramoxalate = models.IntegerField(unique=False)
    estradiol = models.IntegerField(unique=False)
    exelon = models.IntegerField(unique=False)
    famotidine = models.IntegerField(unique=False)
    felodipineer = models.IntegerField(unique=False)
    fenofibrate = models.IntegerField(unique=False)
    fentanyl = models.IntegerField(unique=False)
    finasteride = models.IntegerField(unique=False)
    floventhfa = models.IntegerField(unique=False)
    fluconazole = models.IntegerField(unique=False)
    fluoxetinehcl = models.IntegerField(unique=False)
    fluticasonepropionate = models.IntegerField(unique=False)
    furosemide = models.IntegerField(unique=False)
    gabapentin = models.IntegerField(unique=False)
    gemfibrozil = models.IntegerField(unique=False)
    glimepiride = models.IntegerField(unique=False)
    glipizide = models.IntegerField(unique=False)
    glipizideer = models.IntegerField(unique=False)
    glipizidexl = models.IntegerField(unique=False)
    glyburide = models.IntegerField(unique=False)
    haloperidol = models.IntegerField(unique=False)
    humalog = models.IntegerField(unique=False)
    hydralazinehcl = models.IntegerField(unique=False)
    hydrochlorothiazide = models.IntegerField(unique=False)
    hydrocodoneacetaminophen = models.IntegerField(unique=False)
    hydrocortisone = models.IntegerField(unique=False)
    hydromorphonehcl = models.IntegerField(unique=False)
    hydroxyzinehcl = models.IntegerField(unique=False)
    ibandronatesodium = models.IntegerField(unique=False)
    ibuprofen = models.IntegerField(unique=False)
    insulinsyringe = models.IntegerField(unique=False)
    ipratropiumbromide = models.IntegerField(unique=False)
    irbesartan = models.IntegerField(unique=False)
    isosorbidemononitrateer = models.IntegerField(unique=False)
    jantoven = models.IntegerField(unique=False)
    janumet = models.IntegerField(unique=False)
    januvia = models.IntegerField(unique=False)
    ketoconazole = models.IntegerField(unique=False)
    klorcon10 = models.IntegerField(unique=False)
    klorconm10 = models.IntegerField(unique=False)
    klorconm20 = models.IntegerField(unique=False)
    labetalolhcl = models.IntegerField(unique=False)
    lactulose = models.IntegerField(unique=False)
    lamotrigine = models.IntegerField(unique=False)
    lansoprazole = models.IntegerField(unique=False)
    lantus = models.IntegerField(unique=False)
    lantussolostar = models.IntegerField(unique=False)
    latanoprost = models.IntegerField(unique=False)
    levemir = models.IntegerField(unique=False)
    levemirflexpen = models.IntegerField(unique=False)
    levetiracetam = models.IntegerField(unique=False)
    levofloxacin = models.IntegerField(unique=False)
    levothyroxinesodium = models.IntegerField(unique=False)
    lidocaine = models.IntegerField(unique=False)
    lisinopril = models.IntegerField(unique=False)
    lisinoprilhydrochlorothiazide = models.IntegerField(unique=False)
    lithiumcarbonate = models.IntegerField(unique=False)
    lorazepam = models.IntegerField(unique=False)
    losartanhydrochlorothiazide = models.IntegerField(unique=False)
    losartanpotassium = models.IntegerField(unique=False)
    lovastatin = models.IntegerField(unique=False)
    lovaza = models.IntegerField(unique=False)
    lumigan = models.IntegerField(unique=False)
    lyrica = models.IntegerField(unique=False)
    meclizinehcl = models.IntegerField(unique=False)
    meloxicam = models.IntegerField(unique=False)
    metforminhcl = models.IntegerField(unique=False)
    metforminhcler = models.IntegerField(unique=False)
    methadonehcl = models.IntegerField(unique=False)
    methocarbamol = models.IntegerField(unique=False)
    methotrexate = models.IntegerField(unique=False)
    methylprednisolone = models.IntegerField(unique=False)
    metoclopramidehcl = models.IntegerField(unique=False)
    metolazone = models.IntegerField(unique=False)
    metoprololsuccinate = models.IntegerField(unique=False)
    metoprololtartrate = models.IntegerField(unique=False)
    metronidazole = models.IntegerField(unique=False)
    mirtazapine = models.IntegerField(unique=False)
    montelukastsodium = models.IntegerField(unique=False)
    morphinesulfate = models.IntegerField(unique=False)
    morphinesulfateer = models.IntegerField(unique=False)
    mupirocin = models.IntegerField(unique=False)
    nabumetone = models.IntegerField(unique=False)
    namenda = models.IntegerField(unique=False)
    namendaxr = models.IntegerField(unique=False)
    naproxen = models.IntegerField(unique=False)
    nasonex = models.IntegerField(unique=False)
    nexium = models.IntegerField(unique=False)
    niaciner = models.IntegerField(unique=False)
    nifedicalxl = models.IntegerField(unique=False)
    nifedipineer = models.IntegerField(unique=False)
    nitrofurantoinmonomacro = models.IntegerField(unique=False)
    nitrostat = models.IntegerField(unique=False)
    nortriptylinehcl = models.IntegerField(unique=False)
    novolog = models.IntegerField(unique=False)
    novologflexpen = models.IntegerField(unique=False)
    nystatin = models.IntegerField(unique=False)
    olanzapine = models.IntegerField(unique=False)
    omeprazole = models.IntegerField(unique=False)
    ondansetronhcl = models.IntegerField(unique=False)
    ondansetronodt = models.IntegerField(unique=False)
    onglyza = models.IntegerField(unique=False)
    oxcarbazepine = models.IntegerField(unique=False)
    oxybutyninchloride = models.IntegerField(unique=False)
    oxybutyninchlorideer = models.IntegerField(unique=False)
    oxycodoneacetaminophen = models.IntegerField(unique=False)
    oxycodonehcl = models.IntegerField(unique=False)
    oxycontin = models.IntegerField(unique=False)
    pantoprazolesodium = models.IntegerField(unique=False)
    paroxetinehcl = models.IntegerField(unique=False)
    phenobarbital = models.IntegerField(unique=False)
    phenytoinsodiumextended = models.IntegerField(unique=False)
    pioglitazonehcl = models.IntegerField(unique=False)
    polyethyleneglycol3350 = models.IntegerField(unique=False)
    potassiumchloride = models.IntegerField(unique=False)
    pradaxa = models.IntegerField(unique=False)
    pramipexoledihydrochloride = models.IntegerField(unique=False)
    pravastatinsodium = models.IntegerField(unique=False)
    prednisone = models.IntegerField(unique=False)
    premarin = models.IntegerField(unique=False)
    primidone = models.IntegerField(unique=False)
    proairhfa = models.IntegerField(unique=False)
    promethazinehcl = models.IntegerField(unique=False)
    propranololhcl = models.IntegerField(unique=False)
    propranololhcler = models.IntegerField(unique=False)
    quetiapinefumarate = models.IntegerField(unique=False)
    quinaprilhcl = models.IntegerField(unique=False)
    raloxifenehcl = models.IntegerField(unique=False)
    ramipril = models.IntegerField(unique=False)
    ranexa = models.IntegerField(unique=False)
    ranitidinehcl = models.IntegerField(unique=False)
    restasis = models.IntegerField(unique=False)
    risperidone = models.IntegerField(unique=False)
    ropinirolehcl = models.IntegerField(unique=False)
    seroquelxr = models.IntegerField(unique=False)
    sertralinehcl = models.IntegerField(unique=False)
    simvastatin = models.IntegerField(unique=False)
    sotalol = models.IntegerField(unique=False)
    spiriva = models.IntegerField(unique=False)
    spironolactone = models.IntegerField(unique=False)
    sucralfate = models.IntegerField(unique=False)
    sulfamethoxazoletrimethoprim = models.IntegerField(unique=False)
    sumatriptansuccinate = models.IntegerField(unique=False)
    symbicort = models.IntegerField(unique=False)
    synthroid = models.IntegerField(unique=False)
    tamsulosinhcl = models.IntegerField(unique=False)
    temazepam = models.IntegerField(unique=False)
    terazosinhcl = models.IntegerField(unique=False)
    timololmaleate = models.IntegerField(unique=False)
    tizanidinehcl = models.IntegerField(unique=False)
    tolterodinetartrateer = models.IntegerField(unique=False)
    topiramate = models.IntegerField(unique=False)
    toprolxl = models.IntegerField(unique=False)
    torsemide = models.IntegerField(unique=False)
    tramadolhcl = models.IntegerField(unique=False)
    travatanz = models.IntegerField(unique=False)
    trazodonehcl = models.IntegerField(unique=False)
    triamcinoloneacetonide = models.IntegerField(unique=False)
    triamterenehydrochlorothiazid = models.IntegerField(unique=False)
    valacyclovir = models.IntegerField(unique=False)
    valsartan = models.IntegerField(unique=False)
    valsartanhydrochlorothiazide = models.IntegerField(unique=False)
    venlafaxinehcl = models.IntegerField(unique=False)
    venlafaxinehcler = models.IntegerField(unique=False)
    ventolinhfa = models.IntegerField(unique=False)
    verapamiler = models.IntegerField(unique=False)
    vesicare = models.IntegerField(unique=False)
    voltaren = models.IntegerField(unique=False)
    vytorin = models.IntegerField(unique=False)
    warfarinsodium = models.IntegerField(unique=False)
    xarelto = models.IntegerField(unique=False)
    zetia = models.IntegerField(unique=False)
    ziprasidonehcl = models.IntegerField(unique=False)
    zolpidemtartrate = models.IntegerField(unique=False)

    class Meta:
        db_table = "pd_prescriber"

    def __str__(self):
        return (self.fullname)

    @property
    def fullname(self):
        return '%s %s, %s' % (self.fname, self.lname, self.credentials)

class Triple(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    prescriberid = models.IntegerField(unique=False)
    drugname = models.CharField(max_length=30, unique=False)
    qty = models.IntegerField(unique=False)

    class Meta:
        db_table = "pd_triple"

    def __str__(self):
        return (self.tripleList)

    @property
    def tripleList(self):
        return '%s : %s = %i' % (self.prescriberid, self.drugname, self.qty)