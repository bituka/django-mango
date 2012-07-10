from django.shortcuts import render

from conference.models import Conference


def conference_detail(request):
    try:
        active_conference = Conference.objects.get(is_enabled=True)
    except Conference.DoesNotExist:
        active_conference = None
    context = {
        'active_conference': active_conference
    }
    return render(request, 'conference/conference_detail.html', context)
