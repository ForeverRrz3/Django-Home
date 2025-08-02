from django.db.models import Q

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id=int(query))

    vector  = SearchVector("name","decription")
    query = SearchQuery(query)

    return Products.objects.annotate(search=SearchRank(vector, query)).order_by("-rank")
