from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "app": "MovieMate Backend",
        "status": "ok"
    })
