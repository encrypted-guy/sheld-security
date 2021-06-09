from django.shortcuts import render
from django.http import HttpResponse
from tld import get_fld
import os
import requests as rqst
# Create your views here.

def scanner(request):
    return render(request, 'tools/scan.html', {
        "title": "INTERCEPT",
        "search_action": "intercept_result"
    })
 
def result(request):
    # def get_domain_name(url):
    #     domain_name = get_fld(url, fix_protocol=True)
    #     return domain_name
    if 'url' in request.GET:
        # searched_url = get_domain_name(request.GET['url'])
        searched_url = request.GET['url']

    
    def request_header(url):
        res = rqst.get(url)
        page_headers = res.headers
        # making = f"status code: {str(res.status_code)} \n encoding type: {str(res.encoding)} \n\n {page_headers}"
        return page_headers

    def request_document(url):
        res = rqst.get(url)
        return res.text


    return render(request, 'tools/intercept_result.html', {
        "search_action": "intercept_result",
        'searched_url' : searched_url,
        'headers_result': request_header(searched_url),
        'request_document': request_document(searched_url)
        # 'headers_result': request_header(f'http://{searched_url}'),
        # 'request_document': request_document(f'http://{searched_url}')
    })
