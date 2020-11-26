from django.urls import path


from .views import (
    CustomerSignUp,
    PersonnelSignUp,
    SignUpChoices,
    AdminSignUp
)

app_name = 'accounts'
urlpatterns = [
    path('signup/', CustomerSignUp.as_view(), name = "customer_signup"),
    path('signup/', PersonnelSignUp.as_view(), name = "personnel_signup"),
    path('signup/', AdminSignUp.as_view(), name = "admin_signup"),
    path('signup-options/', SignUpChoices.as_view(), name = "sign_up_option"),
]
