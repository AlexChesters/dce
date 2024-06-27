from colored import Fore, Back, Style

class Logger:
    def info(self, *msgs):
        msg_string = "".join(msgs)
        colour = f"{Fore.green}{Back.black}"

        print(f"{colour}[INFO]{Style.reset} - {msg_string}")

    def plain(self, *msgs):
        print("".join(msgs))
