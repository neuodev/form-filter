from django.shortcuts import render
from django.db.models import Q
from .models import Journal,Category


def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(req):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    title_contains = req.GET.get('title_contains')
    id_exact = req.GET.get('id_exact')
    title_or_author = req.GET.get('title_or_author')
    view_count_min = req.GET.get('view_count_min')
    view_count_max = req.GET.get('view_count_max')
    date_min = req.GET.get('date_min')
    date_max = req.GET.get('date_max')
    category = req.GET.get('category')
    reviewed = req.GET.get('reviewed')
    notReviewed = req.GET.get('notReviewed')

    # Filter all journals
    if is_valid_queryparam(title_contains):
        qs = qs.filter(title__icontains=title_contains) 
    elif is_valid_queryparam(id_exact):
        qs = qs.filter(id__exact = id_exact)
    elif is_valid_queryparam(title_or_author): 
        qs = qs.filter(
            Q(title__icontains=title_or_author)|
            Q(author__name__icontains=title_or_author)
        ).distinct()
    
    if is_valid_queryparam(view_count_min) :
      qs = qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max) :
        qs.filter(views__lte=view_count_max)
    
    if is_valid_queryparam(date_min) :
      qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max) :
       qs = qs.filter(publish_date__lte=date_max)

    if reviewed:
        qs = qs.filter(reviewed=True)
    elif notReviewed:
        qs = qs.exclude(reviewed=True)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)
    return render(req, "bootstrap_form.html" , {
        'queryset':qs,
        'categories': categories
    })