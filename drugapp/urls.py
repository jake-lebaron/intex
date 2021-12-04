from django.urls import path
from .views import addPageView, dashboardPageView, detailsDrugPageView, editPageView, indexPageView, lookupDrugPageView
from .views import managePageView, aboutPageView, analysesPageView, detailsPrePageView, searchDrugPageView, searchPrePageView
 
urlpatterns = [
   path("about/", aboutPageView, name="about"),
   path("add/", addPageView, name="add"),
   path("analyses/", analysesPageView, name="analyses"),
   path("dashboard/", dashboardPageView, name="dashboard"),
   path("drugdetails/", detailsDrugPageView, name="drugdetails"),
   path("predetails/", detailsPrePageView, name="predetails"),
   path("edit/", editPageView, name="edit"),
   path("manage/", managePageView, name="manage"),
   path("searchdrug/", searchDrugPageView, name="drugsearch"),
   path("searchpre/", searchPrePageView, name="presearch"),
   path("lookupdrug/", lookupDrugPageView, name="lookupdrug"),
   path("", indexPageView, name="index"),
]
