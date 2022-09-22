from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

# Create your views here.
def show_watchlist(request):
    data_movie = MyWatchList.objects.all()
    context = {
        'item_list': data_movie,
        'name': 'Ghayda Rafa Hernawan',
        'student_id': '2106634332'
    }
    return render(request, "mywatchlist.html", context)
    
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    if "json":
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    elif "xml":
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")