from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.http import JsonResponse
from apps.enterprise.models import Enterprise
from apps.branche.models import Branche
from apps.daily_sale.models import DailySale
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


@api_view(["POST"])
# @permission_classes([SessionAuthentication])
# @authentication_classes([IsAuthenticated])
def show_daily_sales_by_date(request, enterprise_url):

    enterprise = get_object_or_404(Enterprise, url_name=enterprise_url)
    branches = enterprise.branche.all()
    sales = DailySale.objects.filter(branche__in=branches)

    response_data = {
        "enterprise": enterprise.name,
        "branches": [
            {"id": branch.id, "name": branch.name, "cnpj": branch.cnpj}
            for branch in branches
        ],
        "sales": [
            {
                "id": sale.id,
                "date": sale.date,
                "value": sale.value,
                "goal": sale.goal,
                "branche_id": sale.branche.id,
                "branche_name": sale.branche.name,
            }
            for sale in sales
        ],
    }

    return JsonResponse(response_data)
