from utils import greet
from newpo import API


def main():
    print(greet("World"))
    print(greet("Hello Russian turist"))

    API()


if __name__ == "__main__":
    main()
