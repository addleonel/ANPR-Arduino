from django.shortcuts import render
from plate.models import PlateModel, PlateCapturedModel


def home(request):
    return render(request, 'plate/plate_home.html')

def plate_list(request):
    plates_captured = PlateCapturedModel.objects.all()

    context = {
        'plates_captured': plates_captured,
    } 
    
    return render(request, 'plate/plate_pictures.html', context)