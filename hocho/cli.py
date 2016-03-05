import click
import inquirer
import os.path


"""
QUESTIONS
"""


def ask_questions():
    questions = [
        inquirer.List(
            "type",
            message="What do you want to create?",
            choices=["stylesheet"],
        ),
    ]
    answer = inquirer.prompt(questions)

    return answer


def ask_filename():
    questions = [
        inquirer.Text(
            'name',
            message="What is the name of the file?"),
    ]
    answer = inquirer.prompt(questions)

    return answer


def create_stylesheet(name):
    file_name = name["name"] + '.styl'
    fileExists = os.path.isfile(file_name)

    if not fileExists:
        stylesheet = open(file_name, 'x')
        stylesheet.close()
        print("Stylesheet created, happy styling!")
    else:
        print("whoa!  That shit exists.  Maybe use a different name?")


"""
COMMANDS
"""


@click.group()
def main():
    click.echo(click.style("Hey there, what's your hocho?", fg="green"))


@click.command()
def stir():
    answer = ask_questions()

    if answer["type"] == "stylesheet":
        file_answer = ask_filename()

        create_stylesheet(file_answer)

main.add_command(stir)

if __name__ == "__main__":
    main()
