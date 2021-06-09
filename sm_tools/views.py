from django.shortcuts import render
from django.http import HttpResponse
from tld import get_fld
import os
# Create your views here.

# NSLOOKUP
def nslookup_scan(request):
    return render(request, 'tools/scan.html', {
        "title": "NSLOOKUP",
        "search_action": "nslookup_result"
    })

def nslookup_result(request):
    # print(request.GET['url'])

    def run_nslookup(host):
        command = f"nslookup {host}"
        process = os.popen(command)
        results = str(process.read())
        return results
    
    def get_domain_name(url):
        domain_name = get_fld(url, fix_protocol=True)
        return domain_name
    if 'url' in request.GET:
        searched_url = get_domain_name(request.GET['url'])
    

    return render(request, 'tools/result.html',{
        "search_action": "nslookup_result",
        'searched_url' : searched_url,
        'result__of': run_nslookup(searched_url)
    })

# ======================================================

# TRACEROUTE
def traceroute_scan(request):
    return render(request, 'tools/scan.html', {
        "title": "TRACEROUTE",
        "search_action": "traceroute_result"
    })

def traceroute_result(request):
    def get_domain_name(url):
        domain_name = get_fld(url, fix_protocol=True)
        return domain_name
    if 'url' in request.GET:
        searched_url = get_domain_name(request.GET['url'])
    
    def run_traceroute(host):
        command = f"traceroute {host}"
        process = os.popen(command)
        results = str(process.read())
        return results


    return render(request, 'tools/result.html', {
        "search_action": "traceroute_result",
        'searched_url' : searched_url,
        'result__of': run_traceroute(searched_url)
    })

# ======================================================
 

# WHOIS
def whois_scan(request):
    return render(request, 'tools/scan.html', {
        "title": "WHOIS",
        "search_action": "whois_result"
    })

def whois_result(request):

    def run_whois(host):
        command = f"whois {host}"
        process = os.popen(command)
        results = str(process.read())
        return results
    def get_domain_name(url):
        domain_name = get_fld(url, fix_protocol=True)
        return domain_name
    if 'url' in request.GET:
        searched_url = get_domain_name(request.GET['url'])
    
    return render(request, 'tools/result.html', {
        "search_action": "whois_result",
        'searched_url' : searched_url,
        'result__of': run_whois(searched_url)
    })

