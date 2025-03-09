import requests

def get_headers(url):
    try:
        resp = requests.get(f"https://{url}")
        print("Headers:")
        for k, v in resp.headers.items():
            print(f"{k}: {v}")
    except:
        print("Error fetching headers")

if __name__ == "__main__":
    target = input("Enter a domain (e.g., scanme.nmap.org): ")
    get_headers(target)
