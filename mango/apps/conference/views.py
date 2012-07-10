from django.shortcuts import render

from conference.models import Conference
from conference.forms import ConferenceForm


def conference_detail(request):
    try:
        active_conference = Conference.objects.get(is_enabled=True)
    except Conference.DoesNotExist:
        active_conference = None
    context = {
        'active_conference': active_conference
    }
    return render(request, 'conference/conference_detail.html', context)


def conference_create(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
    else:
        form = ConferenceForm()
    context = {
        'form': form
    }
    return render(request, 'conference/conference_create.html', context)
