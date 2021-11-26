from django.core.checks.messages import DEBUG
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import redirect
import os
def index(request):
    gender = ""
    if request.method == "POST":
        prod=Person()
        prod.person_firstname = request.POST.get('fname','')
        prod.person_lastname = request.POST.get('lname','')
        prod.person_email = request.POST.get('email','')
        if len(request.FILES) != 0:
            prod.person_img = request.FILES['image']
        if request.POST.get("btnradio1"):
            gender="male"
            prod.person_gender = gender
        if request.POST.get("btnradio2"):
            gender="female"
            prod.person_gender = gender
        if request.POST.get("btnradio3"):
            gender="other"
            prod.person_gender = gender
        prod.person_password = request.POST.get('password','')
        #gender = request.POST.get('gender','')
        prod.person_dob = request.POST.get('dob','')
        prod.save()
        #thank = True
    return render(request, 'index.html')#, {'thank':thank})
        ##messages.success(request,"Thank you for contacting us. Your Query will be resolved soon.")
    #return render(request,'contactus.html')
    #return render(request,'index.html')
    
# Create your views here.
def showorders(request):
    post = Person.objects.all()
    print("post",post)
    return render(request, 'showorders.html',
                  {'post':post})
    #if len(person)>0:
     #   update = OrderUpdate.objects.filter(order_id=orderId)
      #  updates = []
       # for item in update:
        #    updates.append({'text': item.update_desc, 'time': item.timestamp})
         #   response = json.dumps([updates, order[0].items_json], default=str)
          #  return HttpResponse(response)
 #   else:
  #      return HttpResponse(orderId)
    #return render(request, 'showorders.html',{'params':params})
def delete(request, id):
    print('ids',id)
    Person.objects.filter(id=id).delete()
    #if request.method=="POST":
        #print('ids',id)
        # a = request.POST.get('button1','')
        # b = request.POST.get('button2','')
        # if b:
        #     Person.objects.filter(id=id).delete()
    return HttpResponse(request,'This record has been deleted')    
def update(request, id):
    print('ids',id)
    
    if id != 0:
        ab = Person.objects.filter(id=id)
        print(ab)
        return render(request, 'update.html',
                  {'ab':ab})
    if request.method=="POST" & id !=0:
        updated(request,id)
    return HttpResponse(request,'there is an error')
def updated(request,id):
    print("hello",id)
    if request.method=="POST":
        
        prod=Person.objects.get(id=id)
        print(prod.person_img.path)
        if len(request.FILES) != 0:
            if len(prod.person_img)>0:
                os.remove(prod.person_img.path)
                prod.person_img.delete()
                #print(prod.person_img.path)
        prod.person_img = request.FILES['image']    
        print(prod)
        prod.person_firstname = request.POST.get('fname','')
        print("okok",prod.person_firstname)
        prod.person_lastname = request.POST.get('lname','')
        prod.person_email = request.POST.get('email','')
        prod.person_password = request.POST.get('password','')
        #gender = request.POST.get('gender','')
        prod.person_dob = request.POST.get('dob','')
        print(prod.person_img.path)
        prod.save()
    return render(request, 'updated.html')


    