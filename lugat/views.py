from django.shortcuts import render, redirect
from .models import *

def home(request):
    qidirish = request.GET.get("searched")
    a = Togri.objects.filter(soz=qidirish)

    if len(a) == 0:
        t_s = ["Soz omborda yoq"]
        n_s = ["Soz omborda yoq"]
    if len(a) > 0:
            t_s = Togri.objects.filter(soz=qidirish)
            if t_s:
                n_s = NoTogri.objects.filter(t_soz = t_s[0])
            else:
                n_s = NoTogri.objects.filter(notogri=qidirish)
                t_s = n_s[0].t_soz
                n_s = NoTogri.objects.filter(t_soz=t_s)

    elif qidirish == "":
        t_s = [""]
        n_s = ""

    date = {
        "togrisi": t_s[0],
        "notogri": n_s[0],
    }
    return render(request, "result.html", date)
