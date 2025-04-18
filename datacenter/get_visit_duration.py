from django.utils.timezone import now

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    if not visit.leaved_at:
        duration = now() - visit.entered_at
    else:
        duration = visit.leaved_at - visit.entered_at
    return duration.total_seconds()


def is_visit_long(visit):
    return get_duration(visit) > SECONDS_IN_HOUR


def format_duration(duration):
    hours = int(duration // SECONDS_IN_HOUR)
    minutes = int((duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    seconds = int(duration % SECONDS_IN_MINUTE)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
