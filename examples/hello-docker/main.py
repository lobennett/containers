# main.py
import os
import typing


def create_greeting(name: str) -> str:
    return f"Hello, {name}! Welcome to my python script. \n"


if __name__ == "__main__":
    # Get the 'NAME' environment variable, default to 'World!' if it does not exist
    name = os.environ.get("NAME", "World")
    message = create_greeting(name)
    out_path = "./log/message.txt"

    if not os.path.exists("./log"):
        os.makedirs("./log")

    with open("./log/message.txt", "a") as f:
        f.write(message)
