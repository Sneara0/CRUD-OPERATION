from django.shortcuts import render


from django.shortcuts import render
from django.shortcuts import render, redirect  
from homepage.forms import homepageForm  
from homepage.models import homepage 
 
def emp(request):  
    if request.method == "POST":  
        form = homepageForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = homepageForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
   homepage = homepage.objects.all()  
   return render(request,"show.html",{'homepage':homepage})  
def edit(request, id):  
    homepage = homepage.objects.get(id=id)  
    return render(request,'edit.html', {'homepage':homepage})  
def update(request, id):  
    homepage = homepage.objects.get(id=id)  
    form = homepageForm(request.POST, instance = homepage)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'homepage': homepage})  
def destroy(request, id):  
    homepage = homepage.objects.get(id=id)  
    homepage.delete()  
    return redirect("/show")

