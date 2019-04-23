from django.shortcuts import render
from django.http import HttpResponse
from googleapiclient.discovery import build
from django.views.generic import TemplateView
from .results_helper import SearchResults


google_api_key = "AIzaSyAJ9J7fRq5vnk1dVFPigmfEObyr3axmkPg"
google_engine_id = '007158505335621513591:xij5lqqbjq8'

# Create your views here.

def index(response):
    # service = build("customsearch", "v1",
    #                 developerKey=google_api_key)
    #
    # res = service.cse().list(
    #     q='lectures',
    #     cx=google_engine_id,
    # ).execute()

    return HttpResponse("<h1>DualSearch</h1>")

class SearchView(TemplateView):
    template_name = "search_results.html"

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)

        service = build("customsearch", "v1",
                        developerKey=google_api_key)

        res = service.cse().list(
            q=self.request.GET.get('q', ''),
            cx=google_engine_id,
        ).execute()

        # print(res)
        #
        res = SearchResults(res)

        context.update({
            'items': res.items,
            'total_results': res.total_results,
            'search_terms': res.search_terms,
        })

        return context




