from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import qrcode
from PIL import Image
from io import BytesIO
import base64

# Create your views here.


def index(request):
    if request.method == "POST":
        registeruser = RegisterU()
        name = request.POST.get("name")
        photo = request.POST.get("photo")
        allowed = request.POST.get("allowed")
        allowed1 = False
        if allowed == 'on':
            allowed1 = True
        else:
            allowed1 = False
        registeruser.name = name
        registeruser.photo = photo
        registeruser.allowed = allowed1
        registeruser.save()
        return HttpResponse("<h1> thank you for registeration <h1>")
    return render(request, "UserReg/register.html")


def searchpage(request):
    return render(request, 'UserReg/search.html')


def search(request, id):
    userdetail = RegisterU.objects.get(id=id)
    context = {
        "user": userdetail
    }
    return render(request, 'UserReg/search.html', context, name='search')


def indexqr(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        register1 = RegisterU.objects.all()
        qr_image = qrcode.make(qr_text, box_size=15)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
    return render(request, 'UserReg/qrcode.html', context=context)
