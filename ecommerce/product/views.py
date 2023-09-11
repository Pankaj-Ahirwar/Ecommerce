from django.shortcuts import render
from .models import SoapItem,SurfItem

# Create your views here.

def home(req):
    req.session['cart']={}  #cart is a key #cart ko empty dictionary dena h
    print(dict(req.session))
    return render(req, 'product/index.html')

def soap_page(req):
    if req.method=='POST':
        required=int(req.POST.get("req"))   # single page application nhi banayege , multiple pages rehte h 
        instock=int(req.POST.get("instock"))  # website me
        id=int(req.POST.get("id_product"))   # 1 page se data 2sre page pr jata h to string form me jta h
        print(required)                      # islye int me convert krege
        print(instock)
        print(type(instock))
        if required>instock:
             data=SoapItem.objects.all()
             msg="OUT OF STOCK"
             return render(req, 'product/soap.html',{'data':data, 'msg':msg, 'id':id} )
        
        cat='soap'
        cat_id=cat+str(id)
        cart=req.session.get('cart') #local variable
        print(cart)
        old=cart.get(cat_id) #old name ka variable banaya , get me hum key pass krte h (cat_id)
        if old:              #key cart h , uski value empty dictionary kr di
            cart[cat_id]=required+old #key value pair bana rhe h , jese python me dictionary me banate the
            
        else:
            #cart={}
            cart[cat_id]=required

       # print(cart)

        req.session['cart']=cart  # assign new value
       # cart=req.session.get('cart')
       # print(cart)

   # cart=req.session.get('cart')
   # print(cart)

       
    
    data=SoapItem.objects.all()
    return render(req, 'product/soap.html',{'data':data })
            
def surf(req):
    if req.method=='POST':
        required=int(req.POST.get("req"))
        instock=int(req.POST.get("instock"))
        id=int(req.POST.get("id_product"))
        print(required)
        print(instock)
        print(type(instock))
        if required>instock:
             data=SurfItem.objects.all()
             msg="OUT OF STOCK"
             return render(req, 'product/soap.html',{'data':data, 'msg':msg, 'id':id} )
        

        cat='surf'
        cat_id=cat+str(id)
        cart=req.session.get('cart')
        old=cart.get(cat_id)
       # print(cart)
        if old:              #key cart h , uski value empty dictionary kr di
            cart[cat_id]=required+old #key value pair bana rhe h , jese python me dictionary me banate the
            
        else:
           # cart={}
            cart[cat_id]=required
       # print(cart)

        req.session['cart']=cart
       
    
    data=SurfItem.objects.all()
    return render(req, 'product/soap.html',{'data':data })
           
def cart(req):
    data=req.session.get('cart')
    print(data)
    list_final=[]
    GT=0
    for i,j in data.items():  #{'soap2': 44, 'surf2': 5}
        if "soap" in i :      #"soap22"
            id=int(i[4:])
            d1=SoapItem.objects.get(pk=id)
            price=d1.price
            total=j*price
            lis=[d1,j,total]
            list_final.append(lis)
            GT+=total

        if "surf" in i :      #"soap22"
            id=int(i[4:])
            d1=SurfItem.objects.get(pk=id)
            price=d1.price
            total=j*price
            lis=[d1,j,total]
            list_final.append(lis)
            GT+=total
    return render(req, 'product/mycart.html',{'list_final':list_final,'GT':GT} )

def search(req):
    if req.method=="POST":
        search=req.POST.get('search')
        print(search)
        # data = Woman_item.objects.all()
        # data= Woman_item.objects.filter(Name=search)
        #print(data)
        if search:
            data = SoapItem.objects.filter(name__icontains=search)
            print(data)
            
            data1 = SurfItem.objects.filter(name__icontains=search)
            print(data1)

            if data:
                # print('fdgfhj')
                return render(req,"product/search.html",{'data':data} )
            
            if data1:
                return render(req,"product/search.html",{'data':data1})
            
    return render(req,'product/search.html')