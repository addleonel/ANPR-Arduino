from django.shortcuts import render
from plate.models import PlateCapturedModel


def home(request):
    """
    Home page
    """
    return render(request, 'plate/plate_home.html')


def plate_list(request):
    """
    List of plates
    """
    plates_captured = PlateCapturedModel.objects.all().order_by('-created_at')

    context = {
        'plates_captured': plates_captured,
    }

    return render(request, 'plate/plate_pictures.html', context)
