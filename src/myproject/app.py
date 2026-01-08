from utils import greet
from newpo import API
from newpo import Sesion


def main():
    print(greet("World"))
    print(greet("Hello Russian turist"))

    API()
    Sesion()


if __name__ == "__main__":
    main()
