from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    return render(request,"Food/index.html",{"item_list":item_list})

######Class Based View
class IndexClassView(ListView):
    model = Item
    template_name = "Food/index.html"
    context_object_name = 'item_list'

def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    return render(request,"Food/detail.html",{"item":item})

class FoodDetail(DetailView):
    model = Item
    template_name = "Food/detail.html"
    
def create_item(request):
    form =ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    return render(request,"Food/form.html",{"form":form})

####Class Based View

class CreateItem(CreateView):
    model = Item
    fields = ["item_name","item_desc","item_price","item_image"]
    template_name = "Food/form.html"

    def form_valid(self,form):
        form.instance.user_name =self.request.user
        return super().form_valid(form) 
        
def update_item(request,id):
    item = Item.objects.get(id=id)
    form =ItemForm(request.POST or None,instance=item)
    #inorder to item be present before update instance=item
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    return render(request,"Food/form.html",{"form":form,"item":item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("Food:index")
    return render(request,"Food/delete.html",{"item":item})

    
