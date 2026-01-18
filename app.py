import datetime

def greet(name):
    now = datetime.datetime.now()
    return f"Hello, {name}! Current time was {now.time()}"


if __name__ == "__main__":
    user = "World "
    print(greet(user))


