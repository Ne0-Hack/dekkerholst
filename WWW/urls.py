from django.urls import path
from .views import main_page, document_policy_page, document_offer_page

urlpatterns = [
    path('', main_page, name="main-page"),
    path('policy', document_policy_page, name="document-policy"),
    path('offer', document_offer_page, name="document-offer")
]
