from django.shortcuts import render
from customer.models import Account,Customer
from admin.models import AddProduct, Purchase

# Create your views here.



def add_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(username = username, password = password, type = "admin")
        obj.save()

    return render(request,'add_admin.html')


def add_products(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        brand = request.POST['brand']
        price = request.POST['price']
        image = request.FILES['image']


        obj = AddProduct(model_name = model_name, brand = brand, price = price, image=image)
        obj.save()

    
    return render(request,'add_products.html')




def index_admin(request):
    return render(request,'index_admin.html')




def view_products(request):
    obj = AddProduct.objects.all()

    return render(request,'view_products.html',{'mobiles':obj})



def view_register(request):
    obj = Customer.objects.all()

    return render(request,'view_register.html',{'mobiles':obj})




def view_purchase(request):
    obj = Purchase.objects.all()
    return render(request,'view_purchase.html',{'data':obj})



