
from django.urls import path



from . import views



urlpatterns = [

            path('impuls/', views.MyOwnView.as_view()),

            ]
