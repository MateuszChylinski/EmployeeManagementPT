from view import View
from model import Model


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    # to test which button has been clicked
    def on_button_click(self, btn_caption):
        print("Button", btn_caption)


if __name__ == '__main__':
    controller = Controller()
    controller.main()
