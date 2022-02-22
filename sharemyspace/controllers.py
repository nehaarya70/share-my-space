import datetime
from urllib import request
from django.core.files.storage import FileSystemStorage
from django.http import *
from django.shortcuts import *
from .connection import *
from django.views.decorators.csrf import *
from datetime import *


def Addadminpage(request):
    return render(request, "addadmin.html")


def indexpage(request):
    return render(request, 'indexpage.html')


def adminlogout(request):
    del request.session['ADMINEMAIL']
    return HttpResponseRedirect('/adminlogin')


def addadminaction(request):
    conn = connection.connection('')
    email = request.POST["email"]
    password = request.POST["password"]
    admintype = request.POST["admintype"]
    query = "insert into admintable values ('" + email + "','" + password + "','" + admintype + "')"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    d['msg'] = "Data Saved Successfully"

    conn.close()
    return render(request, "addadmin.html", d)


def viewadmin(request):
    conn = connection.connection('')
    query = "select * from admintable"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["Email"] = p[0]
        d["Password"] = p[1]
        d["AdminType"] = p[2]
        x.append(d)

    return render(request, "viewadmin.html", {'x': x})


def deleteadmin(request):
    conn = connection.connection('')
    email = request.GET["email"]
    query = "delete from admintable where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    return HttpResponseRedirect("/viewadmin")


def editadmin(request):
    conn = connection.connection('')
    email = request.GET['email']
    qr = "select * from admintable where email='" + email + "'"
    r = conn.cursor()
    r.execute(qr)
    res = r.fetchone()
    d = {}
    d['email'] = email
    d['admintype'] = res[2]
    # print(d['admintype'])
    return render(request, "editadmin.html", d)


def editadminaction(request):
    conn = connection.connection('')
    admintype = request.POST["admintype"]
    email = request.POST["email"]
    query = "update admintable set admintype='" + admintype + "' where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/viewadmin")


def addCategorypage(request):
    return render(request, "addcategory.html")


def addcategoryaction(request):
    conn = connection.connection('')
    cat = request.POST["cat"]
    des = request.POST["des"]

    query = "insert into categorytable values ('" + cat + "','" + des + "')"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    d['msg'] = "Data Saved Successfully"
    conn.close()
    return render(request, "addcategory.html", d)


def viewcategory(request):
    conn = connection.connection('')
    query = "select * from categorytable"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["cat"] = p[0]
        d["des"] = p[1]

        x.append(d)

    return render(request, "viewcategory.html", {'x': x})




def adminviewrooms(request):
    conn = connection.connection('')
    query = "select * from roomtable"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}

        d["roomid"] = p[0]
        d["title"] = p[1]
        d["priceperday"] = p[2]
        d["des"] = p[3]
        d["photo"] = p[4]
        d["email"] = p[5]
        d["city"] = p[6]

        x.append(d)

    return render(request, "adminviewrooms.html", {'x': x})


def adminshowroomdetail(request):
    conn = connection.connection('')
    roomid = request.GET["roomid"]
    query = "select DISTINCT bookingid from bookingdetail where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    res = r.fetchall()
    print(res)
    x=[]
    for p in res:
        d = {}
        query1 = "select email,name,mobileno from bookingtable where bid='" + p[0] + "'"
        r = conn.cursor()
        r.execute(query1)
        res1 = r.fetchone()
        d['email'] = res1[0]
        d['name'] = res1[1]
        d['mobileno'] = res1[2]
        x.append(d)

    return render(request, "adminshowroomdetail.html", {'y' : x})


def deletecategory(request):
    conn = connection.connection('')
    cat = request.GET["cat"]
    query = "delete from categorytable where categoryname='" + cat + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    return HttpResponseRedirect("/viewcategory")


def editcategory(request):
    conn = connection.connection('')
    cat = request.GET['cat']
    qr = "select * from categorytable where categoryname='" + cat + "'"
    r = conn.cursor()
    r.execute(qr)
    res = r.fetchone()
    d = {}
    d['cat'] = cat
    d['des'] = res[1]
    # print(d['admintype'])
    return render(request, "editcategory.html", d)


def editcategoryaction(request):
    conn = connection.connection('')
    cat = request.POST["cat"]
    des = request.POST["des"]
    query = "update categorytable set description='" + des + "' where categoryname='" + cat + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/viewcategory")


def userlogout(request):
    del request.session['USEREMAIL']
    return HttpResponseRedirect('/userlogin')


def usersignup(request):
    return render(request, "usersignup.html")

@csrf_exempt
def usersignupaction(request):
    conn = connection.connection('')
    fullname = request.POST["fullname"]
    mobile = request.POST["mobile"]
    city = request.POST["city"]
    address = request.POST["address"]
    photo = request.FILES["photo"]
    email = request.POST["email"]
    usertype = request.POST["usertype"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    status = "Pending"
    d = {}

    if (password == repassword):
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        photoname = fs.url(filename)
        query = "insert into usersignup values ('" + email + "','" + password + "','" + fullname + "','" + mobile + "','" + address + "','" + photoname + "','" + status + "','" + usertype + "','" + city + "')"
        r = conn.cursor()
        r.execute(query)
        conn.commit()
        d['msg'] = "User Signed Up Successfully"
        conn.close()
    else:
        d['msg'] = "Password does not match"
    return render(request,"usersignup.html",d)


def userlogin(request):
    return render(request, "userlogin.html")


@csrf_exempt
def userhomepage(request):
    conn = connection.connection('')
    email=request.session['USEREMAIL']
    query = "select city from usersignup where email='" + email + "' "
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    city =  result[0]
    print(city)
    q = "select * from roomtable where city='" + city + "'"
    r1 = conn.cursor()
    r1.execute(q)
    result1 = r1.fetchall()
    print(q)
    x = []
    for p in result1:
        d = {}
        d["roomid"] = p[0]
        d["title"] = p[1]
        d["priceperday"] = p[2]
        d["des"] = p[3]
        d["photo"] = p[4]
        d["email"] = p[5]
        d["city"] = p[6]
        x.append(d)
    conn.commit()
    return render(request, "userhomepage.html",{'x': x})




def userloginaction(request):
    conn = connection.connection('')
    email = request.POST["email"]
    password = request.POST["password"]
    s = "Approved"
    query = "select * from usersignup where email='" + email + "' and password='" + password + "' and status='" + s + "' "
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    conn.commit()
    if (result != None):
        request.session['USEREMAIL'] = email
        print(request.session['USEREMAIL'])
        return HttpResponseRedirect("/userhomepage")
    else:
        d = {}
        d['msg'] = "Invalid Email or password"
    return render(request, "userlogin.html", d)
    #return JsonResponse(d, safe=False)

def changepassword(request):
    return render(request, "changepassword.html")


def changepasswordaction(request):
    conn = connection.connection('')
    email = request.POST["email"]
    oldpassword = request.POST["oldpassword"]
    newpassword = request.POST["newpassword"]
    confirmpassword = request.POST["confirmpassword"]
    query = "select password from usersignup where email='" + email + "' and password='" + oldpassword + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    d = {}

    if (result != None):
        qr = "update usersignup set password='" + newpassword + "' where email='" + email + "'"
        # print(qr)
        r1 = conn.cursor()
        r1.execute(qr)
        conn.commit()
        d['msg'] = "Password Updated"
        return render(request, "changepassword.html", d)
    else:
        d['msg'] = "Old password is incorrect"
    return render(request, "changepassword.html", d)


def adminlogin(request):
    return render(request, "adminlogin.html")


def adminhomepage(request):
    return render(request, "adminhomepage.html")




def adminloginaction(request):
    conn = connection.connection('')
    email = request.POST["email"]
    password = request.POST["password"]
    query = "select * from admintable where email='" + email + "' and password='" + password + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    conn.commit()

    if (result != None):
        request.session['ADMINEMAIL'] = email
        print(request.session['ADMINEMAIL'])
        return HttpResponseRedirect("/adminhomepage")
    else:
        d = {}
        d['msg'] = "Invalid Email or password"
    return render(request, "adminlogin.html", d)


def myprofile(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select * from usersignup where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    d = {}
    d["fullname"] = result[2]
    d["mobileno"] = result[3]
    d["address"] = result[4]
    d["photo"] = result[5]
    # d["status"] = result[6]
    d["usertype"] = result[7]
    d["city"] = result[8]
    return render(request, "myprofile.html", d)


@csrf_exempt
def myprofileaction(request):
    conn = connection.connection('')
    fullname = request.POST["fullname"]
    mobileno = request.POST["mobileno"]
    city = request.POST["city"]
    print(city)
    # photo = request.FILES["photo"]
    email = request.session["USEREMAIL"]

    address = request.POST["address"]
    usertype = request.POST["usertype"]

    if len(request.FILES) != 0:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        photoname = fs.url(filename)
        query = "update usersignup set fullname='" + fullname + "',mobileno='" + mobileno + "',address='" + address + "',usertype='" + usertype + "',photo='" + photoname + "',city='" + city + "' where email='" + email + "'"
    else:
        query = "update usersignup set fullname='" + fullname + "',mobileno='" + mobileno + "',address='" + address + "',usertype='" + usertype + "',city='" + city + "' where email='" + email + "'"

    print(query)

    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    d['msg'] = "Profile Updated Successfully"
    conn.close()
    return JsonResponse(d, safe=False)
    # return HttpResponseRedirect("/myprofile")


def seller(request):
    conn = connection.connection('')
    s = "Pending"
    a = "Seller"
    query = "select * from usersignup where status='" + s + "' and usertype='" + a + "'"
    print(query)
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["email"] = p[0]
        d["fullname"] = p[2]
        d["mobileno"] = p[3]
        d["address"] = p[4]
        d["photo"] = p[5]
        # d["status"] = result[6]

        x.append(d)
    conn.commit()
    print(x)
    return render(request, "seller.html", {'x': x})


def buyer(request):
    conn = connection.connection('')
    s = "Pending"
    a = "Buyer"
    query = "select * from usersignup where status='" + s + "' and usertype='" + a + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["email"] = p[0]
        d["fullname"] = p[2]
        d["mobileno"] = p[3]
        d["address"] = p[4]
        d["photo"] = p[5]
        # d["status"] = result[6]

        x.append(d)
    # conn.commit()

    return render(request, "buyer.html", {'x': x})


def approvebuyer(request):
    conn = connection.connection('')
    email = request.GET['email']
    s = "Approved"

    query = "update usersignup set status='" + s + "' where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/buyer")


def rejectbuyer(request):
    conn = connection.connection('')
    email = request.GET['email']
    s = "Rejected"

    query = "update usersignup set status='" + s + "' where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/buyer")


def approveseller(request):
    conn = connection.connection('')
    email = request.GET['email']
    s = "Approved"

    query = "update usersignup set status='" + s + "' where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/seller")


def rejectseller(request):
    conn = connection.connection('')
    email = request.GET['email']
    s = "Rejected"

    query = "update usersignup set status='" + s + "' where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    return HttpResponseRedirect("/seller")


def rentroom(request):
    return render(request, "rentroom.html")


def rentroomaction(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    title = request.POST["title"]
    priceperday = request.POST["priceperday"]
    city = request.POST["city"]
    des = request.POST["des"]
    photo = request.FILES["photo"]
    d = {}
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    photoname = fs.url(filename)
    query = "insert into roomtable values (null,'" + title + "','" + priceperday + "','" + des + "','" + photoname + "','" + email + "','" + city + "')"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d['msg'] = "Room added Successfully"
    conn.close()

    return render(request, "rentroom.html", d)


def viewroom(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select * from roomtable where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["roomid"] = p[0]
        d["title"] = p[1]
        d["priceperday"] = p[2]
        d["des"] = p[3]
        d["photo"] = p[4]
        d["city"] = p[6]
        # d["status"] = result[6]

        x.append(d)
    # conn.commit()

    return render(request, "viewroom.html", {'x': x})


def deleteroom(request):
    conn = connection.connection('')
    roomid = request.GET["roomid"]
    query = "delete from roomtable where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    return HttpResponseRedirect("/viewroom")


def editroom(request):
    conn = connection.connection('')
    roomid = request.GET['roomid']
    qr = "select * from roomtable where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(qr)
    p = r.fetchone()
    d = {}
    d['roomid'] = p[0]
    d["title"] = p[1]
    d["priceperday"] = p[2]
    d["des"] = p[3]
    d["photo"] = p[4]
    d["city"] = p[6]
    # print(d['admintype'])
    return render(request, "editroom.html", d)


@csrf_exempt
def editroomaction(request):
    conn = connection.connection('')
    roomid = request.POST["roomid"]
    title = request.POST["title"]
    priceperday = request.POST["priceperday"]
    city = request.POST["city"]
    des = request.POST["des"]
    if len(request.FILES) != 0:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        photoname = fs.url(filename)
        query = "update roomtable set title ='" + title + "',priceperday='" + priceperday + "',description='" + des + "',photo='" + photoname + "',city='" + city + "' where roomid='" + roomid + "'"
    else:
        query = "update roomtable set title ='" + title + "',priceperday='" + priceperday + "',description='" + des + "',city='" + city + "' where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()

    d = {}
    d["msg"] = "Data Updated Successfully"

    return HttpResponseRedirect("/viewroom")


def addroomphoto(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select * from roomtable where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["roomid"] = p[0]
        d["title"] = p[1]
        x.append(d)
    return render(request, "addroomphoto.html", {'x': x})


@csrf_exempt
def addroomphotoaction(request):
    conn = connection.connection('')
    title = request.POST["title"]
    roomid = request.POST["roomid"]
    photo = request.FILES["photo"]
    d = {}
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    photoname = fs.url(filename)
    query = "insert into roomphotos values (null,'" + title + "','" + photoname + "','" + roomid + "')"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    d['msg'] = "Room Photo added Successfully"
    conn.close()
    return JsonResponse(d, safe=False)


def viewroomphoto(request):
    conn = connection.connection('')
    roomid = request.GET['roomid']
    query = "select * from roomphotos where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()

    result = r.fetchall()

    x = []
    for p in result:
        d = {}
        d["id"] = p[0]
        d["title"] = p[1]
        d["photo"] = p[2]
        d['roomid'] = roomid
        # d["status"] = result[6]

        x.append(d)
    # conn.commit()

    return render(request, "viewroomphoto.html", {'x': x})


def roomphotos(request):
    conn = connection.connection('')
    roomid = request.GET['roomid']
    query = "select * from roomphotos where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    print(query)
    result = r.fetchall()

    x = []
    for p in result:
        d = {}
        d["id"] = p[0]
        d["title"] = p[1]
        d["photo"] = p[2]
        d['roomid'] = roomid
        # d["status"] = result[6]

        x.append(d)
    return JsonResponse(x, safe=False)


def getallcityname(request):
    conn = connection.connection('')
    query = "select DISTINCT(city) from roomtable order by city"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    print(query)
    result = r.fetchall()

    x = []
    for p in result:
        print(p[0], ' ----')
        x.append(p[0])
    print(x)
    return JsonResponse(x, safe=False)


def deleteroomphoto(request):
    conn = connection.connection('')
    photoid = request.GET["photoid"]
    roomid = request.GET["roomid"]

    query = "delete from roomphotos where id='" + photoid + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    return HttpResponseRedirect("/viewroomphoto?roomid=" + roomid)


def addamenity(request):
    return render(request, "addamenities.html")


@csrf_exempt
def addamenityaction(request):
    conn = connection.connection('')
    name = request.POST["name"]
    # roomid = request.POST["roomid"]
    icon = request.FILES["icon"]
    fs = FileSystemStorage()
    filename = fs.save(icon.name, icon)
    iconname = fs.url(filename)
    query = "insert into amenities values (null,'" + name + "','" + iconname + "')"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    d = {}
    d['msg'] = "Amenity added Successfully"
    conn.close()
    return JsonResponse(d, safe=False)


def viewamenity(request):
    conn = connection.connection('')
    query = "select * from amenities"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["id"] = p[0]
        d["name"] = p[1]
        d["icon"] = p[2]
        # d["status"] = result[6]

        x.append(d)
    # conn.commit()

    return render(request, "viewamenities.html", {'x': x})


def deleteamenity(request):
    conn = connection.connection('')
    id = request.GET["id"]
    query = "delete from amenities where id='" + id + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    return HttpResponseRedirect("/viewamenity")


def editamenity(request):
    conn = connection.connection('')
    id = request.GET['id']
    qr = "select * from amenities where id='" + id + "'"
    r = conn.cursor()
    r.execute(qr)
    p = r.fetchone()
    d = {}
    d['id'] = p[0]
    d["name"] = p[1]
    d["icon"] = p[2]
    # print(d['admintype'])
    return render(request, "editamenities.html", d)


@csrf_exempt
def editamenityaction(request):
    conn = connection.connection('')
    id = request.POST["id"]
    name = request.POST["name"]
    if len(request.FILES) != 0:
        photo = request.FILES["icon"]
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        photoname = fs.url(filename)
        query = "update amenities set name ='" + name + "',icon='" + photoname + "' where id='" + id + "'"
    else:
        query = "update amenities set name ='" + name + "' where id='" + id + "'"
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    # d = {}
    # d["msg"] = "Data Updated Successfully"

    return HttpResponseRedirect("/viewamenity")


def roomsearch(request):
    return render(request, "searchroom.html")


@csrf_exempt
def roomsearchaction(request):
    conn = connection.connection('')
    city = request.POST["city"]
    query = "select * from roomtable where city='" + city + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchall()
    x = []
    for p in result:
        d = {}
        d["roomid"] = p[0]
        d["title"] = p[1]
        d["priceperday"] = p[2]
        d["des"] = p[3]
        d["photo"] = p[4]
        d["email"] = p[5]
        d["city"] = p[6]
        x.append(d)
    return JsonResponse(x, safe=False)




def roomdetail(request):
    conn = connection.connection('')
    roomid = request.GET["roomid"]
    query = "select * from roomtable where roomid='" + roomid + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    query1 = "select * from roomtable where roomid='" + roomid + "'"
    r1 = conn.cursor()
    r1.execute(query1)
    result1 = r.fetchone()
    x = []
    d = {}
    d["roomid"] = result[0]
    d["title"] = result[1]
    d["priceperday"] = result[2]
    d["des"] = result[3]
    d["photo"] = result[4]
    d["email"] = result[5]
    d["city"] = result[6]
    # x.append(d)

    # for p in result1:
    #     a={}
    #     a["pic"]=p[0]
    #     x.append(a)
    #
    print(d)

    return render(request, "roomdetail.html", d)


@csrf_exempt
def bookingactionold(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    print(email)
    roomid = request.POST.get("roomid")
    bookername = request.POST.get("bookername")
    mobileno = request.POST.get("mobileno")
    noofperson = request.POST.get("noofperson")
    totalcost = request.POST.get("totalcost")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")
    bookingdate = '2019-03-09'

    d = {}
    query = "insert into bookingtable (email,name,mobileno,noofperson,totalcost,dateofbooking) values ('" + str(
        email) + "','" + str(bookername) + "','" + str(mobileno) + "','" + str(noofperson) + "','" + str(
        totalcost) + "','" + str(bookingdate) + "')"
    print(query)
    r = conn.cursor()
    r.execute(query)
    conn.commit()

    d['msg'] = "Room Booked Successfully"
    conn.close()
    return HttpResponse(query)


def bookingpage(request):
    conn = connection.connection('')
    roomid = request.GET['roomid']
    priceperday = request.GET['priceperday']

    query = "select date1 from bookingdetail where roomid='" + str(roomid) + "'"
    print(query)
    r = conn.cursor()
    r.execute(query)
    conn.commit()
    conn.close()
    dayslist = []
    res = r.fetchall()
    for p in res:
        t = p[0]
        k = t.strftime('%m/%d/%Y')
        print(k)
        dayslist.append(t)
    # dayslist = dayslist[:-1]
    d = {}
    d["roomid"] = roomid
    d["priceperday"] = priceperday
    d['email'] = request.session['USEREMAIL']
    d['dayslist'] = dayslist

    return render(request, "bookingpage.html", d)


def confirmbooking(request):
    conn = connection.connection('')
    bookingid = request.GET["bookingid"]
    query = "select bookingtable.bid,bookingtable.email,bookingtable.name,bookingtable.mobileno,bookingtable.noofperson,bookingtable.totalcost,roomtable.roomid,roomtable.title from bookingtable INNER JOIN roomtable on bookingtable.email=roomtable.email where bookingtable.bid='" + bookingid + "'"
    r = conn.cursor()
    r.execute(query)
    result = r.fetchone()
    print(result)

    d = {}
    d["bid"] = result[0]
    d["email"] = result[1]
    d["name"] = result[2]
    d["mobileno"] = result[3]
    d["noofperson"] = result[4]
    d["totalcost"] = result[5]
    d["roomid"] = result[6]
    d["title"] = result[7]

    conn.commit()

    return render(request, "confirmbooking.html", d)

def mybooking(request):
    return render(request,'mybooking.html')

def showmybookings(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select * from bookingtable where email='" + email + "'"
    r = conn.cursor()
    r.execute(query)
    res = r.fetchall()
    print(res)
    x=[]
    for p in res:
        d={}
        d['bookingid'] = p[0]
        d["name"]=p[2]
        d["noofperson"] = p[4]
        d["totalcost"] = p[5]
        d["dob"] = p[6]
        x.append(d)
    # for p in res:
    #
    #     query1 = "select roomid from bookingdetail where bookingid='" + str(p[0]) + "'"
    #     r = conn.cursor()
    #     r.execute(query1)
    #     res1 = r.fetchall()
    # print(res1)
    # for p in res1:
    #
    #     query1 = "select * from roomtable where roomid='" + p[0] + "'"
    #     r = conn.cursor()
    #     r.execute(query1)
    #     res2 = r.fetchall()
    # y=[]
    # for p in res2:
    #     d={}
    #     d['title']=p[1]
    #     d['photo'] = p[4]
    #     d['city'] = p[6]
    #     y.append(d)
    # print(res2)
    return JsonResponse(x,safe=False)

def getbookingdetail(request):
    bookingid = request.GET['bookingid']
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select bookingdetail.*,roomtable.title,roomtable.photo from bookingdetail,roomtable where roomtable.roomid=bookingdetail.roomid and  bookingid='" + bookingid + "'"
    r = conn.cursor()
    r.execute(query)
    res = r.fetchall()
    print(res)
    x = []
    for p in res:
        d = {}
        d['date1'] = p[3]
        d['price'] = p[4]
        d['title'] = p[5]
        d['photo'] = p[6]
        x.append(d)
    return JsonResponse(x,safe=False)

def checkavailability(request):
    conn = connection.connection('')
    roomid = request.GET["roomid"]
    fromdate = request.GET["fromdate"]
    todate = request.GET["todate"]

    fromdate = datetime.strptime(fromdate, '%m/%d/%Y').strftime('%Y-%m-%d')
    todate = datetime.strptime(todate, '%m/%d/%Y').strftime('%Y-%m-%d')

    qr = "Select * from bookingdetail where date1>='" + str(fromdate) + "' and date1<='" + str(todate) + "' and roomid='"+str(roomid)+"'"
    r = conn.cursor()
    r.execute(qr)
    res = r.fetchall()
    d = {}
    if len(res) > 0:
        d['error_date'] = '1'
    else:
        d['error_date'] = '2'
    return JsonResponse(d, safe=False)


@csrf_exempt
def bookingaction(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    print(email)
    priceperday = request.POST['priceperday']
    roomid = request.POST["roomid"]
    bookername = request.POST["bookername"]
    mobileno = request.POST["mobileno"]
    noofperson = request.POST["noofperson"]
    totalcost = request.POST["totalcost"]
    fromdate = request.POST["fromdate"]
    todate = request.POST["todate"]
    bookingdate = datetime.now().strftime("%y-%m-%d")
    alldays = request.POST['alldays']

    noofdays = alldays.split(',')
    print(noofdays, ' ---------')

    d = {}
    query = "insert into bookingtable (email,name,mobileno,noofperson,totalcost,dateofbooking) values ('" + str(
        email) + "','" + str(bookername) + "','" + str(mobileno) + "','" + str(noofperson) + "','" + str(
        totalcost) + "','" + str(bookingdate) + "')"

    print(query)
    r = conn.cursor()
    r.execute(query)
    conn.commit()

    bookingid = r.lastrowid

    for i in range(0, len(noofdays)):
        qr = "insert into bookingdetail values (null," + str(bookingid) + "," + str(roomid) + ",'" + str(
            noofdays[i]) + "','" + str(priceperday) + "')"
        r1 = conn.cursor()
        r1.execute(qr)
        conn.commit()

    d['bookingid'] = bookingid
    conn.close()
    return JsonResponse(d, safe=False)
