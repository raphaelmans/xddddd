from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from midterm.forms import CustomerForm

from midterm.models import DVD, Customer, Rent

# Create your views here.


class IndexView(View):
    def get(self, request):

        dvds = DVD.objects.all()

        customers = Customer.objects.all()

        context = {
            'customers': customers,
            'dvds': dvds
        }

        return render(request, 'index.html', context)

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
 
            name = request.POST.get("name")
            address = request.POST.get("address")
            birthdate = request.POST.get("birthdate")
            mobile_number = request.POST.get("mobile_number")

            dvd_id = request.POST.get("dvd_id")

            customerObject = Customer(
                name=name,
                address=address,
                birthdate=birthdate,
                mobile_number=mobile_number
            )

            dvdObj = DVD.objects.get(dvd_id=dvd_id)

            rentObj = Rent(customer=customerObject, dvd=dvdObj)

            customerObject.save()
            rentObj.save()
            return redirect('midterm:index_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')
