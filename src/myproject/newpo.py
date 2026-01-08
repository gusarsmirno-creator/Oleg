import requests


def API():
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    response = requests.get("https://api.adviceslip.com/advice", timeout=5)
    response.raise_for_status()
    advice_data = response.json()
    advice_text = advice_data["slip"]["advice"]
    print(advice_text)


def Sesion():
    session = requests.Session()
    for i in range(3):  # цикл на 3 раза
        response = session.get("https://api.adviceslip.com/advice", timeout=5)
        print(response.text)
        print("Status code:", response.status_code)
        print()
