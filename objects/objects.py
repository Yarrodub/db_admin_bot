from aiogram.fsm.state import State, StatesGroup

class FSMOrders(StatesGroup):
    show = State()


class OrdersHistoryPage:
    def __init__(self, current_page: str | int = 0, pages_num: str | int = 0, button_pressed: str | None = None):
        self.current_page: int = int(current_page)
        self.pages_num: int = int(pages_num)
        self.same_text = None

        if button_pressed == 'previous':
            if self.current_page != 0:
                self.current_page -= 1
            else:
                self.same_text = True

        elif button_pressed == 'next':
            if self.current_page != self.pages_num:
                self.current_page += 1
            else:
                self.same_text = True

        elif button_pressed == 'last':
            if self.current_page != self.pages_num:
                self.current_page = self.pages_num
            else:
                self.same_text = True

        elif button_pressed == 'first':
            if self.current_page != 0:
                self.current_page = 0
            else:
                self.same_text = True

        if button_pressed == 'page':
            self.same_text = True

    text_string: str
    first_order_num: int
    last_order_num: int
