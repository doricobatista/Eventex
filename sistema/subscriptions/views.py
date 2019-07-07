from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from sistema.subscriptions.forms import SubscriptionForm

def subscribe(request):
    
    # Quando o método é POST, redirecionar
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        
        if form.is_valid(): # Transforma os objetos recebidos em objetos e alto nível do python e veifica se é válido.
                            # form.full_clean() para apenas transformar em objetos de alto nível.
                    
            body = render_to_string('subscriptions/subscription_email.txt', 
                                    form.cleaned_data)
            
            mail.send_mail('Confirmação de inscrição',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']])
            
            messages.success(request, 'Inscrição realizada com sucesso!')
            
            return HttpResponseRedirect('/inscricao/')
        else:
            
            return render(request, 'subscriptions/subscriptions_form.html', {'form':form})
    else:
        context = { 'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscriptions_form.html', context)
