
from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def render(self):
        pass

class PlainText(Text):
    def __init__(self, msg):
        self.msg = msg
    def render(self):
        return f"<PlainText>{self.msg}</PlainText>"

class TextDecorator(Text):
    def __init__(self, text_class_obj):
        self.text_class_obj = text_class_obj
    def render(self):
        return self.text_class_obj.render()
    

class ItalicText(TextDecorator):
    def render(self):
        return f"<Italic>{self.text_class_obj.render()}</Italic>"

class BoldText(TextDecorator):
    def render(self):
        return f"<Bold>{self.text_class_obj.render()}</Bold>"



def main():
    t1 = PlainText("Sale")
    print(f"{t1.render()}")
    t2 = BoldText(ItalicText(PlainText("Sale")))
    print(t2.render())
    t3 = BoldText(PlainText("Sale"))
    print(t3.render())
    t4 = ItalicText(PlainText("Sale"))
    print(t4.render())


main()

    