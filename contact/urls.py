from django.urls import path

from .views import ContactFormView, EmailSentView

app_name = 'contact'

urlpatterns = [
    path('', ContactFormView.as_view(), name='send'),
    path('email-sent/', EmailSentView.as_view(), name='email-sent'),
]