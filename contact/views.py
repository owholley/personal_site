from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "contact/email_form.html"
    success_url = 'email-sent/'

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='contact-form@owenwholley.com',
            recipient_list=[settings.DEFAULT_FROM_EMAIL],)
        return super(ContactFormView, self).form_valid(form)


class EmailSentView(TemplateView):
    template_name = "contact/email_sent.html"