from django.shortcuts import render,redirect
from .models import *

from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import ClientForm,MapForm
from django.http import HttpResponse
import geocoder
import folium

# Create your views here.
def DashboardView(request):

    context = {}
    return render(request, 'issuerAccounts/dashboardissueraccounts.html', context)



def IssuerClientListView(request):
    datt = Client.objects.all()

    context = {'datas':datt}
    return render(request,'issuerAccounts/issuerClientList.html', context)

class IssuerRegisterClientView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'issuerAccounts/issuerRegisterClient.html'

    def get_success_url(self):
        return reverse('issuerClientList_url')

def IssuerEditClientView(request,pk):
    datta = Client.objects.get(id=pk)
    clientform = ClientForm(instance=datta)

    if request.method == 'POST':
        clientform = ClientForm(request.POST,instance=datta)
        if clientform.is_valid():
            clientform.save()

            return redirect('issuerClientList_url')

        else:
            return redirect('issuerEditClient_url')
    context = {'form':clientform}
    return render(request,'issuerAccounts/issuerEditClient.html', context)

def ContractListView(request):
    data = InsuranceContract.objects.all()

    context = {'contract':data}
    return render(request,'issuerAccounts/contractlist.html', context)

class AssignContractView(CreateView):
    model = InsuranceContract
    fields = '__all__'
    template_name = 'issuerAccounts/assigncontract.html'

    def get_success_url(self):
        return reverse('contractlist_url')



def AccountantPaymentRecordView(request):
    data = Payment.objects.all()

    context = {'data':data}
    return render(request,'issuerAccounts/accountantPaymentRecord.html', context)

class AddContractPaymentView(CreateView):
    model = Payment
    fields = ['contract','user','start_date','end_date']
    template_name = 'issuerAccounts/AddContractPayment.html'

    def get_success_url(self):
        return reverse('accountantPaymentRecord_url')

def MapView(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_url')
    else:
        form = MapForm()
        

    address = Map.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    if lat == None or lng == None:
        address.delete()
        return HttpResponse("Invalid input data.")

    mapobject = folium.Map(location=[19,-12], zoom_start=2)
    folium.Marker([lat,lng], tooltip='click for more', popup=country).add_to(mapobject)

    #get html representation 
    map = mapobject._repr_html_()


    context = {'mp':map, 'form':form}        
    return render(request,'issuerAccounts/map.html', context)




