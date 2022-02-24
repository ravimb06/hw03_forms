from datetime import datetime


def year(request):
    year = datetime.now().year
    context = {
        'year': year,
    }
    return (context)
