import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, ProductionOrder
from callbacks.views import send_to_telegram


@csrf_exempt
def create_order(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    body = json.loads(request.body)
    error = []
    if "callback" not in body:
        error.append({"callback": "is required"})
    if "name" not in body["callback"]:
        error.append({"name": "is required"})
    elif len(body["callback"]["name"]) < 1:
        error.append({"name": "is not null"})
    if "phone" not in body["callback"]:
        error.append({"phone": "is required"})
    elif len(body["callback"]["phone"]) < 1:
        error.append({"phone": "is not null"})
    if "data" not in body:
        error.append({"data": "is required"})
    elif len(body["data"]) < 1:
        error.append({"data": "is not null"})

    if len(error) > 0:
        return HttpResponse(json.dumps({"error": error}), status=400)

    production = []
    for item in body["data"]:
        product = ProductionOrder.objects.filter(id=item["selected"], category_id=item["id"])
        if len(product) != 0:
            production.append(product[0].id)
    Order.objects.create(
        client_name=body["callback"]["name"],
        client_phone=body["callback"]["phone"]
    ).product.set(production)
    send_to_telegram("Новый заказ")
    return HttpResponse(status=201)
