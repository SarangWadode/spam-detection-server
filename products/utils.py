from django.db.models import QuerySet

def create_json(results: QuerySet, start: int):
    return {
        'start': start,
        'count': results.count(),
        'results': list(results)
    }
