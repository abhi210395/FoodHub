from django.urls import path
from .import views

#namespacing
app_name = "Food"

urlpatterns = [
    #/food
    path('', views.index,name ="index"),
    # path('', views.IndexClassView.as_view(),name ="index"),
    # #/food/1
    #  path('<int:item_id>', views.detail,name ="detail"),
     path('<int:pk>', views.FoodDetail.as_view(),name ="detail"),
     #add
    #  path('add', views.create_item,name ="create_item"),

     path('add', views.CreateItem.as_view(),name ="create_item"),
     #edit
     path('update/<int:id>', views.update_item,name ="update_item"),
      #delete
     path('delete/<int:id>', views.delete_item,name ="delete_item"),
]

