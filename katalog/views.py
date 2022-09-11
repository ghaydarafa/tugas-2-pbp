from django.shortcuts import render
from katalog.models import CatalogItem
...

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'item_list': data_barang_katalog,
        'name': 'Ghayda Rafa Hernawan',
        'student_id': '2106634332'
    }
    return render(request, "katalog.html", context)