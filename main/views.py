from django.shortcuts import render
from django.http import HttpResponse
from googleapiclient.discovery import build
from django.views.generic import TemplateView
from .results_helper import SearchResults


google_api_key = "AIzaSyAJ9J7fRq5vnk1dVFPigmfEObyr3axmkPg"
google_engine_id = '007158505335621513591:xij5lqqbjq8'

# Create your views here.

def index(response):
    return render(response, "main/base.html")

class SearchView(TemplateView):
    template_name = "main/search_results.html"

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)

        service = build("customsearch", "v1",
                        developerKey=google_api_key)

        res = service.cse().list(
            q=self.request.GET.get('q', ''),
            start=self.page_to_index(),
            cx=google_engine_id,
        ).execute()

        pages = self.calculate_pages()
        res = SearchResults(res)





        context.update({
            'items': res.items,
            'total_results': res.total_results,
            'search_terms': res.search_terms,
            'current_page': pages[1],
            'prev_page': pages[0],
            'next_page': pages[2]
        })

        return context

    def calculate_pages(self):
        current_page = int(self.request.GET.get('p', 1))
        return (current_page - 1, current_page, current_page + 1)

    def page_to_index(self, page=None):
        if page is None:
            page = self.request.GET.get('p', 1)

        return int(page) * 10 + 1 - 10



