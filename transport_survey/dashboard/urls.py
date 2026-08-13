from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'responses/',
        views.responses,
        name='responses'
    ),

    path(
        'gender-analysis/',
        views.gender_analysis,
        name='gender_analysis'
    ),
    path(
    "transport-analysis/",
    views.transport_analysis,
    name="transport_analysis"
    ),
    path(
    "safety-analysis/",
    views.safety_analysis,
    name="safety_analysis"
    ),
    path(
    "reports/",
    views.reports,
    name="reports"
   ), 
    path(
    "login/",
    views.login_view,
    name="login"
   ),
    path(
    "logout/",
    views.logout_view,
    name="logout"
   ),
    path(
    "reports/pdf/",
    views.generate_report,
    name="generate_report",
   ),
]
