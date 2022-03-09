from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView, name='dashboardissueraccounts_url'),

    path('issuerClientList/', views.IssuerClientListView, name='issuerClientList_url'),
    path('issuerRegisterClient/', views.IssuerRegisterClientView.as_view(), name='issuerRegisterClient_url'),
    path('issuerEditClient/<str:pk>', views.IssuerEditClientView, name='issuerEditClient_url'),
    path('contractlist/', views.ContractListView, name='contractlist_url'),
    path('assigncontract/',views.AssignContractView.as_view(),name='assigncontract_url'),

    path('accountantPaymentRecord/', views.AccountantPaymentRecordView, name='accountantPaymentRecord_url'),
    path('AddContractPayment/', views.AddContractPaymentView.as_view(), name='AddContractPayment_url'),
    path('map/',views.MapView, name='map_url'),
    
]