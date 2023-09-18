class MainClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text=None):
        if text is not None:
            self.text = text


class Subclass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number


main_obj = MainClass("Hello")
main_obj.set_text("Jumanazar")
print(main_obj.text)

sub_obj = Subclass("Hello", 143)
print(sub_obj.text)
print(sub_obj.number)