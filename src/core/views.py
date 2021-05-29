from django.shortcuts import render


def BootstrapFilterView(req):
    return render(req, "bootstrap_form.html")