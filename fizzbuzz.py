import os


def main():
    result = []
    # Get env variables
    prenom = os.getenv("PRENOM", "Toto")

    print("Bonjour je m'appelle:", prenom)
    print("~~~")
    for i in range(100):
        if not(i % 3 | i % 5):
            result.append("fizzbuzz")
        elif not(i % 3):
            result.append("fizz")
        elif not(i % 5):
            result.append("buzz")
        else:
            result.append(i)

    return result


if __name__ == '__main__':
    result = main()
    print(result)
