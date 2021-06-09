from django.shortcuts import render, redirect
from tld import get_fld
import nmap
import socket
# Create your views here.

def search(request):
    return render(request, 'tools/scan.html', {
        'title': 'PORT SCANNER',
        "search_action": "portscan_result"
    })

def result(request):
    def get_domain_name(url):
        domain_name = get_fld(url, fix_protocol=True)
        return domain_name
    
    if 'url' in request.GET and '.' in request.GET['url']:
        searched_url = get_domain_name(request.GET['url'])
    else:
        return redirect('portscan')
        # output an error here
    
    def nm__scanner(url):
        try:
            ip = socket.gethostbyname(searched_url)
            nm = nmap.PortScanner()
            nm.scan(ip, '1-1000', '-v -sS -sV -A -O')
            result = nm[ip]['tcp']
            return result
        except:
            return redirect('portscan')
            # output an error here    | please try again later

    # WITHOUT ROOT pRV
    # def nm__scanner(url):
    #     try:
    #         ip = socket.gethostbyname(searched_url)
    #         nm = nmap.PortScanner()
    #         nm.scan(ip, '1-1000', '-v  -sV ')
    #         result = nm[ip]['tcp']
    #         return result
    #     except:
    #         return redirect('portscan')
    #         # output an error here    | please try again later

    
    # ip = socket.gethostbyname(searched_url)
    # nm = nmap.PortScanner()
    # nm.scan(ip, '1-1000', '-v -sS -sV -A -O')
    # # nm.scan(ip, '1-1000', '-v  -sV ')
    # result = nm[ip]['tcp']
    # print(result)
    # print('DONE....')

    # print('progess....')
    # nm_result = nm__scanner(searched_url)
    # print(nm_result)
    # print('\n DONE....| 1 |==================================================')
    # for i in nm_result:
    #     print(i)
    # print('\n DONE....| 2 |==================================================')
    # for key, value in nm_result.items():
    #     print(key)
    #     print('[[[[[[[[[[[[[[[[[[[[[[[[[')
    #     print(value)
    # print('\n DONE....| 3 |==================================================')
    # for keys, values in nm_result.items():
    #     print(keys, '=======')
    #     for k,v in values.items():
    #         print(f'{k}:\t{v}')

    # print('DONE')


    return render(request, 'tools/portscan_result.html',{
        "search_action": "portscan_result",
        'searched_url' : searched_url,
        'nmap_results': nm__scanner(searched_url)
    })