from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def detail_view(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Receiving a post request...')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            form.save()
            print('The lead has been created.')
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)