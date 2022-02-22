"""sharemyspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .controllers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin',addadmin),
    path('',indexpage),
    path('Addadmin',Addadminpage),
    path('addadminaction',addadminaction),
    path('viewadmin',viewadmin),
    path('editadmin',editadmin),
    path('deleteadmin',deleteadmin),
    path('editadminaction',editadminaction),
    path('addCategorypage',addCategorypage),
    path('addcategoryaction',addcategoryaction),
    path('viewcategory',viewcategory),
    path('adminviewrooms',adminviewrooms),
    path('adminshowroomdeatil',adminshowroomdetail),
    path('deletecategory',deletecategory),
    path('editcategoryaction',editcategoryaction),
    path('editcategory',editcategory),
    path('usersignup',usersignup),
    path('usersignupaction',usersignupaction),
    path('userlogout',userlogout),
    path('userlogin',userlogin),
    path('userloginaction',userloginaction),
    path('userhomepage',userhomepage),
    path('changepassword',changepassword),
    path('changepasswordaction',changepasswordaction),
    path('adminlogin',adminlogin),
    path('adminloginaction',adminloginaction),
    path('adminhomepage',adminhomepage),
    path('myprofile',myprofile),
    path('myprofileaction',myprofileaction),
    path('seller',seller),
    path('buyer',buyer),
    path('approvebuyer',approvebuyer),
    path('rejectbuyer',rejectbuyer),
    path('approveseller',approveseller),
    path('rejectseller',rejectseller),
    path('rentroom',rentroom),
    path('rentroomaction',rentroomaction),
    path('viewroom',viewroom),
    path('deleteroom',deleteroom),
    path('editroom',editroom),
    path('editroomaction',editroomaction),
    path('adminlogout',adminlogout),
    path('addroomphoto',addroomphoto),
    path('addroomphotoaction',addroomphotoaction),
    path('viewroomphoto',viewroomphoto),
    path('deleteroomphoto',deleteroomphoto),
    path('addamenity',addamenity),
    path('addamenityaction',addamenityaction),
    path('viewamenity',viewamenity),
    path('editamenityaction',editamenityaction),
    path('editamenity',editamenity),
    path('deleteamenity',deleteamenity),
    path('roomsearch',roomsearch),
    path('roomsearchaction',roomsearchaction),
    path('roomdetail',roomdetail),
    path('roomphotos',roomphotos),
    path('getallcityname',getallcityname),
    path('bookingpage',bookingpage),
    path('bookingaction',bookingaction),
    path('bookingactionold',bookingactionold),
    path('confirmbooking', confirmbooking),
    path('mybooking', mybooking),
    path('showmybookings',showmybookings),
    path('checkavailability', checkavailability),
    path('getbookingdetail', getbookingdetail),

]
