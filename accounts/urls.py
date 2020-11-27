from django.urls import path


from .views import (
    CustomerSignUp,
    PersonnelSignUp,
    SignUpChoices,
    AdminSignUp,

    view_customer_account_list,
    delete_customer_account,
    update_customer_account,
    view_personnel_account_list,
    delete_personnel_account,
    update_personnel_account,
    view_admin_account_list,
    delete_admin_account,
    update_admin_account


)

app_name = 'accounts'

urlpatterns = [
    path('signup-as-customer/', CustomerSignUp.as_view(), name = "customer_signup"),
    path('signup-as-personel/', PersonnelSignUp.as_view(), name = "personnel_signup"),
    path('signup-as-admin/', AdminSignUp.as_view(), name = "admin_signup"),
    path('signup-options/', SignUpChoices.as_view(), name = "sign_up_option"),


    path('customer-accounts-list/', view_customer_account_list, name = "customer_account"),
    path('delete-customer-accounts/<int:pk>/', delete_customer_account, name = "delete_customer_account"),
    path('update-customer-accounts/<int:pk>/', update_customer_account, name = "update_customer_account"),

    path('personnel-accounts-list/', view_personnel_account_list, name = "personnel_account"),
    path('delete-personnel-accounts/<int:pk>/', delete_personnel_account, name = "delete_personnel_account"),
    path('update-personnel-accounts/<int:pk>/', update_personnel_account, name = "update_personnel_account"),

    path('admin-accounts-list/', view_admin_account_list, name = "admin_account"),
    path('delete-admin-accounts/<int:pk>/', delete_admin_account, name = "delete_admin_account"),
    path('update-admin-accounts/<int:pk>/', update_admin_account, name = "update_admin_account"),
]
