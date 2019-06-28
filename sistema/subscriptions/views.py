from django.shortcuts import render
from sistema.subscriptions.forms import SubscriptionForm

def subscribe(request):
    context = { 'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscriptions_form.html', context)

