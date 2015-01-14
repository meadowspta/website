import json

from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from meta.views import Meta

from .forms import VolunteerSignupForm, NotificationSignupForm
from .models import Ticket


def home(request):
    volunteer_signup_form = VolunteerSignupForm(request.POST or None)

    payload = {
        'volunteer_signup_form': volunteer_signup_form,
        'quantity_range': range(1, 101),
    }

    return render_to_response('crabfeed/home.html', payload, context_instance=RequestContext(request))

def tickets(request):
    payload = {
        'quantity_range': range(1, 101),
    }

    return render_to_response('crabfeed/tickets.html', payload, context_instance=RequestContext(request))

def confirmation(request):
    return render_to_response('crabfeed/confirmation.html', context_instance=RequestContext(request))

def cancellation(request):
    return render_to_response('crabfeed/cancellation.html', context_instance=RequestContext(request))

def save_the_date(request):
    notification_signup_form = NotificationSignupForm(request.POST or None)

    if notification_signup_form.is_valid():
        notification_signup_form.save()
        return HttpResponseRedirect('?confirmation=true')

    payload = {
        'notification_signup_form': notification_signup_form,
        'display_thankyou': request.GET.get('confirmation'),
    }

    return render_to_response('crabfeed/save-the-date.html', payload, context_instance=RequestContext(request))

def test(request):
    payload = {

    }

    return render_to_response('crabfeed/test.html', payload, context_instance=RequestContext(request))

def dashboard(request):
    payload = {

    }

    return render_to_response('crabfeed/dashboard.html', payload, context_instance=RequestContext(request))

def check_in(request):
    id_hash = request.GET.get('id')
    ticket = Ticket.objects.get(id_hash=id_hash)

    payload = {
        'ticket': ticket,
    }

    return render_to_response('crabfeed/check-in.html', payload, context_instance=RequestContext(request))

def search(request):
    return render_to_response('crabfeed/search.html', {}, context_instance=RequestContext(request))

def api_search(request):
    q = request.GET.get('q')
    results = []

    tickets = Ticket.search(q)
    for ticket in tickets:
        results.append(ticket.as_api_object())

    response = {
        'statusCode': 200,
        'response': results,
    }

    return HttpResponse(json.dumps(response), mimetype='application/json')

def api_tickets(request):
    data = []

    tickets = Ticket.objects.all()
    for ticket in tickets:
        data.append(ticket.as_api_object())

    response = {
        'statusCode': 200,
        'response': data,
    }

    return HttpResponse(json.dumps(response), mimetype='application/json')

def api_volunteer_signup_save(request):
    volunteer_signup_form = VolunteerSignupForm(request.POST or None)
    full_name = request.GET.get('full-name')
    email = request.GET.get('email')

    volunteer_signup_form.save()

    response = {
        'statusCode': 200,
        'full_name': full_name,
        'email': email,
    }

    return HttpResponse(json.dumps(response), mimetype='application/json')