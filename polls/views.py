from django.http import HttpResponse


def index(request):
    return HttpResponse("Polls index for Django2.0 Alpha.")
