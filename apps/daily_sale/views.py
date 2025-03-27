from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Tbvendasdashboard
from django.db.models import Q

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def show_daily_sales_by_date(request):
    
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
                "name": branch['nmfilial'],  # Nome da filial
                "cnpj": branch['nrcnpj'],   # CNPJ da filial
            }
            for branch in unique_branches
        ],
        "sales": [
            {
                "id": sale.idvendas,        # ID da venda
                "cnpj": sale.nrcnpj,        # CNPJ
                "branche_name": sale.nmfilial,  # Nome da filial
                "date": sale.dtvenda,       # Data da venda
                "value": float(sale.vlvenda) if sale.vlvenda is not None else None,  # Valor da venda (convertido para float)
                "goal": float(sale.txmeta) if sale.txmeta is not None else None,    # Meta (convertido para float)
            }
            for sale in sales
        ],
    }

    return JsonResponse(response_data)