from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from meta.views import Meta
from meadowspta.contrib.auction.models import Item, Donor

def list(request):
    items = Item.objects.all().order_by('-publish_date')
    return render_to_response('auction/list.html', {'items': items}, context_instance=RequestContext(request))

def item_view(request, slug):
    item = Item.objects.get(slug=slug)
    return render_to_response('auction/item/view.html', {'item': item}, context_instance=RequestContext(request))