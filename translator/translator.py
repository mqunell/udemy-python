from translate import Translator

translator = Translator(to_lang="es")


def safe_open_file(func):
    def wrap_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileNotFoundError as error:
            print("File not found")
            # raise error
        except IOError as error:
            print("IO error")
            # raise error

    return wrap_func


@safe_open_file
def append_line(input_line):
    with open("./output.txt", mode="+a") as output_file:
        print(f'Translating "{input_line}"')
        output_line = translator.translate(input_line)
        output_file.write(output_line + "\n")


@safe_open_file
def translate_file():
    with open("./input.txt", mode="r") as input_file:
        input_file.seek(0)
        while input_line := input_file.readline():
            append_line(input_line.strip())
        else:
            print("Done!")


# Run `py translator.py` from this directory so the relative file paths work
if __name__ == "__main__":
    translate_file()
