
from argparse import ArgumentParser

def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate appropriate greetings")
    parser.add_argument('--title', '-t')
    parser.add_argument('--polite','-p', action="store_true")
    parser.add_argument('personal')
    parser.add_argument('family')
    arguments= parser.parse_args()
    
    message = greet(arguments.personal, arguments.family,
                    arguments.title, arguments.polite)
    print(message)