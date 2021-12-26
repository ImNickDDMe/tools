import requests

def cloudflare(domain, queryType="A"):
    BASE_URL = "https://cloudflare-dns.com/dns-query"

    parameters = {
        "name": domain,
        "type": queryType
    }

    headers = {
        "Accept": "application/dns-json"
    }

    response = requests.get(BASE_URL, headers=headers, params=parameters)
    return response.json()

def google(domain, queryType="A"):
    BASE_URL = "https://dns.google/resolve"

    parameters = {
        "name": domain,
        "type": queryType
    }

    headers = {
        "Accept": "application/dns-json"
    }

    response = requests.get(BASE_URL, headers=headers, params=parameters)
    return response.json()