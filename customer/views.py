
from django.shortcuts import render, redirect
from customer.models import Customer,Account
from admin.models import AddProduct, Purchase

# Create your views here.



def register_customers(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        pincode = request.POST['pincode']
        username = request.POST['username']
        password = request.POST['password']


        obj = Customer( name=name, email=email, contact=contact, address=address, pincode=pincode)
        obj.save()
        account = Account( username = username, password = password, type = 'customer', user_id = obj.id )
        account.save()
    return render(request,'register_customers.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username = username, password = password)
            request.session['userid'] = user.id
            if(user.type == 'customer'):
                return redirect('user:after_login')
            elif(user.type == 'admin'):
                return redirect('admin:index_admin')
        except:
            return render(request, 'login.html',{'message':'username or password is incorrect'})

    return render(request,'login.html')



def index(request):
    return render(request,'index.html')


def after_login(request):
    # object = AddProduct.objects.get(id = id)
    print(object)
    
    obj = AddProduct.objects.all()
    return render(request,'after_login.html',{'mobiles': obj})

    



def purchase(request, idd):
    obj = AddProduct.objects.get(id = idd)
    print(obj)
    ss = request.session['userid']
    o = Account.objects.get(id = ss)
    ob = Purchase(product_id = obj.id, customer_id  = o.user.id )
    ob.save()

    return redirect('user:after_login')