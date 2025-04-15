from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Tbvendasdashboard
from django.db.models import Q

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def require_all_daily_sales(request):
    
    # Filtra vendas onde vlvenda não é nulo, usando o banco atos_db
    sales = Tbvendasdashboard.objects.using('atos_db').filter(~Q(vlvenda__isnull=True))

    # Obtém as filiais únicas baseadas em nmfilial, usando o banco atos_db
    unique_branches = (
        Tbvendasdashboard.objects.using('atos_db')
        .filter(~Q(vlvenda__isnull=True))
        .values('nmfilial', 'nrcnpj')
        .distinct()
    )

    response_data = {
        "branches": [
            {
                "name": branch['nmfilial'],  
                "cnpj": branch['nrcnpj'],   
            }
            for branch in unique_branches
        ],
        "sales": [
            {
                "id": sale.idvendas,        
                "cnpj": sale.nrcnpj,        
                "branche_name": sale.nmfilial,
                "date": sale.dtvenda,       
                "value": float(sale.vlvenda) if sale.vlvenda is not None else None,  
                "goal": float(sale.txmeta) if sale.txmeta is not None else None,    
            }
            for sale in sales
        ],
    }

    return JsonResponse(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def require_daily_sales_by_date(request, date):

    # date type string in format == year-month-day (YY-MM-DD)

    sales = Tbvendasdashboard.objects.using('atos_db').filter(~Q(vlvenda__isnull=True), dtvenda = date)

    unique_branches = (
        Tbvendasdashboard.objects.using('atos_db')
        .filter(~Q(vlvenda__isnull=True), dtvenda = date)
        .values('nmfilial', 'nrcnpj')
        .distinct()
    )

    response_data = {
        "branches": [
            {
                "name": branch['nmfilial'],  
                "cnpj": branch['nrcnpj'],   
            }
            for branch in unique_branches
        ],
        "sales": [
            {
                "id": sale.idvendas,        
                "cnpj": sale.nrcnpj,        
                "branche_name": sale.nmfilial,
                "date": sale.dtvenda,       
                "value": float(sale.vlvenda) if sale.vlvenda is not None else None,  
                "goal": float(sale.txmeta) if sale.txmeta is not None else None,    
            }
            for sale in sales
        ],
    }

    return JsonResponse(response_data)
