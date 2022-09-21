from django.urls import path
from.views import home, administrador, funcionario, PanelControl, login

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('administrador/', administrador, name="administrador"),
    path('PanelControl/', PanelControl, name="PanelControl"),
    path('funcionario/', funcionario, name="funcionario")

]