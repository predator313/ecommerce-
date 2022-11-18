
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="About Us"),
    path("contact/",views.contact,name="Contact Us"),
    path("tracker/",views.tracker,name="Tracking Status"),
    path("search/",views.search,name="Search"),
    path("product/",views.product,name="Products"),
    path("checkout/",views.checkout,name="checkout"),

]
