
from app.server import Server


def main():
    server = Server()
    server.run(debug=True)


if __name__ == "__main__":
    main()
