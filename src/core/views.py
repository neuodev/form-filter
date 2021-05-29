from django.shortcuts import render
from django.db.models import Q
from .models import Journal

def BootstrapFilterView(req):
    qs = Journal.objects.all()
    title_contains = req.GET.get('title_contains')
    id_exact = req.GET.get('id_exact')
    title_or_author = req.GET.get('title_or_author')
    view_count_min = req.GET.get('view_count_min')
    view_count_max = req.GET.get('view_count_max')
    date_min = req.GET.get('date_min')
    date_min = req.GET.get('date_min')
    date_max = req.GET.get('date_max')
    category = req.GET.get('category')

    # Filter the all journals
    if title_contains != '' and title_contains is not None:
        qs = qs.filter(title__icontains=title_contains) 
    elif id_exact != '' and id_exact is not None:
        qs = qs.filter(id__exact = id_exact)
    elif title_or_author != '' and title_or_author is not None: 
        qs = qs.filter(
            Q(title__icontains=title_or_author)|
            Q(author__name__icontains=title_or_author)
        ).distinct()
    return render(req, "bootstrap_form.html" , {
        'queryset':qs
    })