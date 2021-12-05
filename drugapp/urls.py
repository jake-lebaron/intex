from django.urls import path
from .views import addPageView, dashboardPageView, detailsDrugPageView, indexPageView, lookupDrugPageView, lookupPrescPageView
from .views import managePageView, aboutPageView, analysesPageView, detailsPrePageView, searchDrugPageView, searchPrePageView, updatePrescriberPageView
from .views import deletePrescriberPageView, addPrescriberPageView, editPageView
#  
urlpatterns = [
   path("about/", aboutPageView, name="about"),
   path("add/", addPageView, name="add"),
   path("analyses/", analysesPageView, name="analyses"),
   path("dashboard/", dashboardPageView, name="dashboard"),
   path("drugdetails/<int:drugid>/", detailsDrugPageView, name="drugdetails"),
   path("predetails/<int:npi>/", detailsPrePageView, name="predetails"),
   path("edit/<int:npi>", editPageView, name="edit"),
   path("manage/", managePageView, name="manage"),
   path("searchdrug/", searchDrugPageView, name="drugsearch"),
   path("searchpre/", searchPrePageView, name="presearch"),
   path("lookupdrug/", lookupDrugPageView, name="lookupdrug"),
   path("lookuppresc/", lookupPrescPageView, name="lookuppresc"),
   path("updatePrescriber/", updatePrescriberPageView, name="updatePresc"),
   path("deletePrescriber/<int:npi>/", deletePrescriberPageView, name="deletePresc"),
   path("addPresc/", addPrescriberPageView, name="addPresc"),
   path("", indexPageView, name="index"),
]
