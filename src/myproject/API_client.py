import requests


def API():
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    response = requests.get("https://api.adviceslip.com/advice", timeout=5)
    response.raise_for_status()
    advice_data = response.json()
    advice_text = advice_data["slip"]["advice"]
    print(advice_text)


def Sesion():
    for i in range(3):
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        response.raise_for_status()
        print(response.text)
        print("Status code:", response.status_code)


def Dog(ip="https://dog.ceo/api/breeds/image/random"):
    r = requests.get(ip, timeout=5)
    r.raise_for_status()
    print(r.url)
    print(r.status_code)
    data = r.json()
    print(data)
    image_url = data["message"]
    print(image_url)


def Four():
    r = requests.get("https://jsonplaceholder.typicode.com/xyz", timeout=5)
    if r.status_code >= 400:
        print(f"{r.status_code} {r.reason}")
