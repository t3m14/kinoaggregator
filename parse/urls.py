
from django.urls import path



from . import views



urlpatterns = [

            path('impuls/', views.Impulse.as_view()),
            path('fokus/', views.Fokus.as_view()),
            path('mega/', views.Mega.as_view()),
            path('almaz/', views.Almaz.as_view()),
            ]
