from django.urls import path
from . import views

urlpatterns = [
    path("adminhomepage/", views.listBook, name='view'),
    path("BookDetails/<int:book_id>",views.details,name='details'),
    path("Addbook/", views.creatBook, name='add'),
    path("Updatebook/<int:book_id>", views.updateBook, name='update'),
    path("Deletebook/<int:book_id>", views.deleteBook, name='delete'),
    path("NewAuthor",views.creatAuthor,name='AddAuthor'),
    path('search/',views.SerachBox,name='search'),
]
