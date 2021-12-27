from bs4 import BeautifulSoup
import requests

def cloudfront(subdomain):
    response = requests.get(f"https://{subdomain}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if (response.status_code == 404 and soup.h1.text == "404 ERROR"):
        return f"{subdomain}: Conceivable takeover"
    else:
        return f"{subdomain}: No takeover"