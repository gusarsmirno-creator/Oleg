from utils import greet
import API_client


def main():
    print(greet("World"))
    print(greet("Hello Russian turist"))

    API_client.API()
    API_client.Sesion()
    API_client.Dog()


if __name__ == "__main__":
    main()
