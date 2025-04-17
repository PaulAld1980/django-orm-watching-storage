from datacenter.models import Passcard, Visit
from datacenter.get_visit_duration import get_duration, is_visit_long
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    suspicious_visits = []

    for visit in visits:
        duration = get_duration(visit)
        formatted_duration = f"{int(duration // 3600):02}:{int((duration % 3600) // 60):02}:{int(duration % 60):02}"
        is_strange = is_visit_long(visit)

        visit_info = {
            'entered_at': visit.entered_at.strftime('%d-%m-%Y'),
            'duration': formatted_duration,
            'is_strange': is_strange,
        }

        this_passcard_visits.append(visit_info)

        if is_strange:
            suspicious_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
        'suspicious_visits': suspicious_visits,
    }

    return render(request, 'passcard_info.html', context)
