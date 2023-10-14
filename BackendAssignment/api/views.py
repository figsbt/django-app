from django.http import HttpResponse


def info(request):
    return HttpResponse("This is an introduction to api-app in BackendAssignment django-project!")
