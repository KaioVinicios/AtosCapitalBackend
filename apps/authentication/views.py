from django.http import JsonResponse
from rest_framework.decorators import api_view
from apps.employee.models import EmployeeUser


@api_view(["GET"])
def get_registred_whatsapp_numbers(request):
    whatsapp_numbers_list = [
        str(num)
        for num in EmployeeUser.objects.values_list("whatsapp_number", flat=True)
    ]

    data = {"whatsapp_numbers": whatsapp_numbers_list}

    return JsonResponse(data)
