import json
from django.shortcuts import render
from works.models import Work
from orders.models import CategoryOrder, ProductionOrder
from django.conf import settings


def main_page(request):
    works = Work.objects.all()
    order = []
    for i in CategoryOrder.objects.all().values():
        order_data = []
        for item in ProductionOrder.objects.filter(category_id=i["id"]):
            img = item.upload.name
            if len(img) > 1:
                img = settings.MEDIA_URL + img
            else:
                img = None
            order_data.append({
                "id": item.id,
                "title": item.title,
                "img": img,
                "price": item.price
            })
        order.append({
            "title": i["title"],
            "coefficient": i['coefficient'],
            "id": i["id"],
            "data": order_data
        })
    ctx = {
        "works": works,
        "order": json.dumps(order)
    }
    return render(request, 'WWW/main.html', context=ctx)


def document_policy_page(request):
    ctx = {
        "policy_url": request.build_absolute_uri(location='/')
    }
    return render(request, 'WWW/policy.html', context=ctx)


def document_offer_page(request):
    return render(request, 'WWW/offer.html')
