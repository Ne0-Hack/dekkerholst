import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Callback, TelegramUsers
from WWW.models import SiteSettings

@csrf_exempt
def create_callback(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    body = json.loads(request.body)
    error = []
    if "name" not in body:
        error.append({"name": "is required"})
    elif len(body["name"]) < 1:
        error.append({"name": "is not null"})
    if "phone" not in body:
        error.append({"phone": "is required"})
    elif len(body["phone"]) < 1:
        error.append({"phone": "is not null"})

    if len(error) > 0:
        return HttpResponse(json.dumps({"error": error}), status=400)

    Callback.objects.create(name=body["name"], phone=body["phone"])
    send_to_telegram("Новая заявка на обратную связь")
    return HttpResponse(status=201)


def send_to_telegram(message):
    if SiteSettings.objects.first() is None:
        return False
    users = TelegramUsers.objects.all()
    for user in users:
        url = (f"https://api.telegram.org/bot{SiteSettings.objects.first().site_telegram}/sendMessage?"
               f"parse_mode=HTML"
               f"&text={message}"
               f"&chat_id={user.telegram}")
        requests.get(url)
    return True
