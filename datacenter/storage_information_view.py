from datacenter.models import Visit
from datacenter.get_visit_duration import get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):

    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        visitors_inside = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%d.%m.%Y %H:%M'),
            'duration': formatted_duration,
        }

        non_closed_visits.append(visitors_inside)

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
