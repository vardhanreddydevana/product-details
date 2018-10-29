from django.shortcuts import render
from firebase.firebase import FirebaseApplication
# Create your views here.
def showindex(request):
    pno = request.GET.get('update')
    fire = FirebaseApplication('https://merchant-a8a0f.firebaseio.com/', None)
    d1=fire.get('product',pno)
    #print(d1)
    return render(request,'index.html',{'key':d1})
def savedata(request):
    pno=request.POST.get('t1')
    pname = request.POST.get('t2')
    pprice = request.POST.get('t3')
    fire=FirebaseApplication('https://merchant-a8a0f.firebaseio.com/',None)
    fire.put('product',pno,{'name':pname,'price':pprice})
    d1=fire.get('product',None)
    #print(d1)
    return render(request,'index.html',{'data':d1})


def deletedata(request):
    pno=request.POST.get('d1')
    fire=FirebaseApplication('https://merchant-a8a0f.firebaseio.com/',None)
    fire.delete('product',pno)
    return render(request,'index.html')
