"""
Shutdown timer
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import asyncio
import datetime


class shutdown(toga.App):
    async def A_shutdown(self, widget):
        # get the value of A_hour_input and A_minute_input
        A_hour = self.A_hour_input.value
        A_minute = self.A_minute_input.value
        A_time = "%s:%s" % (A_hour, A_minute)
         # get the time 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        while A_time != current_time:
            ''' SHUT DOWN'''
            print("asd")

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        TIME_SELECTION = toga.Box(style=Pack(direction=COLUMN))
        AT_TIME = toga.Box(style=Pack(direction=COLUMN))
        T_hour_box = toga.Box(style=Pack(direction=ROW))
        T_minute_box = toga.Box(style=Pack(direction=ROW))
        T_second_box = toga.Box(style=Pack(direction=ROW))
        A_hour_box = toga.Box(style=Pack(direction=ROW))
        A_minute_box = toga.Box(style=Pack(direction=ROW))

        T_hour_label = toga.Label('Hour:', style=Pack(padding=0, font_size=15,))
        T_minute_label = toga.Label('Minute:', style=Pack(padding=0, font_size=15,))
        T_second_label = toga.Label('Second:', style=Pack(padding=0, font_size=15,))

        self.T_hour_input = toga.NumberInput(style=Pack(padding=5, font_size=14, flex=1, height=20), min_value=0, max_value=24)
        self.T_minute_input = toga.NumberInput(style=Pack(padding=5, font_size=14, flex=1, height=20), min_value=0, max_value=59)
        self.T_second_input = toga.NumberInput(style=Pack(padding=5, font_size=14, flex=1, height=20), min_value=0, max_value=59)

        A_hour_label = toga.Label('(24) Hour:', style=Pack(padding=0, font_size=15,))
        A_minute_label = toga.Label('(60) Minute:', style=Pack(padding=0, font_size=15,))
        
        self.A_hour_input = toga.NumberInput(style=Pack(padding=5, font_size=14, flex=1, height=20), min_value=0, max_value=23)
        self.A_minute_input = toga.NumberInput(style=Pack(padding=5, font_size=14, flex=1, height=20), min_value=0, max_value=59)
    
        T_hour_box.add(T_hour_label)
        T_hour_box.add(T_hour_input)
        T_minute_box.add(T_minute_label)
        T_minute_box.add(T_minute_input)
        T_second_box.add(T_second_label)
        T_second_box.add(T_second_input)
        A_hour_box.add(A_hour_label)
        A_hour_box.add(A_hour_input)
        A_minute_box.add(A_minute_label)
        A_minute_box.add(A_minute_input)

        T_button = toga.Button(
            "Enter Time",
            on_press=self.T_shutdown,
            style=Pack(padding=5, width=500, height=30, font_size=15),
        )
        A_button = toga.Button(
            "Enter Time",
            on_press=self.A_shutdown,
            style=Pack(padding=5, width=500, height=30, font_size=15),
        )

        TIME_SELECTION.add(T_hour_box)
        TIME_SELECTION.add(T_minute_box)
        TIME_SELECTION.add(T_second_box)
        TIME_SELECTION.add(T_button)

        AT_TIME.add(A_hour_box)
        AT_TIME.add(A_minute_box)
        AT_TIME.add(A_button)

        container = toga.OptionContainer()

        container.add('Time Till', TIME_SELECTION)
        container.add('At Time', AT_TIME)

        self.time_input = toga.TextInput(placeholder="Enter a time", style=Pack(width=500, height=20, font_size=15))

        time_box = toga.Box(style=Pack(direction=ROW, padding=5))
        time_box.add(self.time_input)

        

        main_box.add(container)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()




            


    async def T_shutdown(self, widget):
        """
        Print "Hello <whatever the user typed>" to the console.
        """
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = "You fucker didnt type anything!"

        self.main_window.info_dialog("Hello")


def main():
    return shutdown()
