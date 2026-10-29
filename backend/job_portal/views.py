from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Job Portal API is running", "status": "success"})
