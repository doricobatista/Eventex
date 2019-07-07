from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from sistema.subscriptions.forms import SubscriptionForm
from django.conf import settings


def subscribe(request):
    # Quando o método é POST, redirecionar
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    # Transforma os objetos recebidos em objetos e alto nível do python e veifica se é válido.
    # form.full_clean() para apenas transformar em objetos de alto nível.
    if not form.is_valid():
        return render(request, 'subscriptions/subscriptions_form.html', {'form': form})
    
    _send_email('subscriptions/subscription_email.txt',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                form.cleaned_data,
                'Confirmação de inscrição',
                )
    
    messages.success(request, 'Inscrição realizada com sucesso!')
    
    return HttpResponseRedirect('/inscricao/')

def new(request):
    return render(request, 'subscriptions/subscriptions_form.html', {'form': SubscriptionForm()})

def _send_email(template_name, from_, to, context, subject):
    body = render_to_string(template_name, context)
    
    mail.send_mail(subject, body, from_, [from_, to])



