from django.shortcuts import render
from .models import Worksheet
from datetime import date

def home(request):
    today = date.today()
    today_worksheets = Worksheet.objects.filter(date=today)
    return render(request, 'worksheet/home.html', {
        'worksheets': today_worksheets,
        'today': today  # 👈 pass the date to the template
    })

