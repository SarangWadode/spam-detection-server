from django.db.models import QuerySet


def create_json(results: QuerySet, start: int):
    return {
        'results': list(results),
        'start': start,
        'count': results.count()
    }
