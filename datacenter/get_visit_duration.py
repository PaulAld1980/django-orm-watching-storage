from django.utils.timezone import now


def get_duration(visit):

    if not visit.leaved_at:
        duration = now() - visit.entered_at
    else:
        duration = visit.leaved_at - visit.entered_at
    return duration.total_seconds()


def is_visit_long(visit):
    duration = get_duration(visit)
    return duration > 3600


def format_duration(duration):

    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
