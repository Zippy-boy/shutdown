"""
Shutdown timer
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import asyncio
from datetime import datetime
import os


class shutdown(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.veiw_box = toga.Box(style=Pack(direction=COLUMN, text_align="center"))
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        TIME_SELECTION = toga.Box(style=Pack(direction=COLUMN))
        AT_TIME = toga.Box(style=Pack(direction=COLUMN))
        T_hour_box = toga.Box(style=Pack(direction=ROW))
        T_minute_box = toga.Box(style=Pack(direction=ROW))
        T_second_box = toga.Box(style=Pack(direction=ROW))
        A_hour_box = toga.Box(style=Pack(direction=ROW))
        A_minute_box = toga.Box(style=Pack(direction=ROW))

        T_hour_label = toga.Label(
            "Hour:",
            style=Pack(
                padding=0,
                font_size=15,
            ),
        )
        T_minute_label = toga.Label(
            "Minute:",
            style=Pack(
                padding=0,
                font_size=15,
            ),
        )
        T_second_label = toga.Label(
            "Second:",
            style=Pack(
                padding=0,
                font_size=15,
            ),
        )

        self.T_hour_input = toga.NumberInput(
            style=Pack(padding=5, font_size=14, flex=1, height=20),
            min_value=0,
            max_value=24,
        )
        self.T_minute_input = toga.NumberInput(
            style=Pack(padding=5, font_size=14, flex=1, height=20),
            min_value=0,
            max_value=59,
        )
        self.T_second_input = toga.NumberInput(
            style=Pack(padding=5, font_size=14, flex=1, height=20),
            min_value=0,
            max_value=59,
        )

        A_hour_label = toga.Label(
            "(24) Hour:",
            style=Pack(
                padding=0,
                font_size=15,
            ),
        )
        A_minute_label = toga.Label(
            "(60) Minute:",
            style=Pack(
                padding=0,
                font_size=15,
            ),
        )

        self.A_hour_input = toga.NumberInput(
            style=Pack(padding=5, font_size=14, flex=1, height=20),
            min_value=0,
            max_value=23,
        )
        self.A_minute_input = toga.NumberInput(
            style=Pack(padding=5, font_size=14, flex=1, height=20),
            min_value=0,
            max_value=59,
        )

        T_hour_box.add(T_hour_label)
        T_hour_box.add(self.T_hour_input)
        T_minute_box.add(T_minute_label)
        T_minute_box.add(self.T_minute_input)
        T_second_box.add(T_second_label)
        T_second_box.add(self.T_second_input)
        A_hour_box.add(A_hour_label)
        A_hour_box.add(self.A_hour_input)
        A_minute_box.add(A_minute_label)
        A_minute_box.add(self.A_minute_input)

        T_button = toga.Button(
            "Enter Time",
            on_press=self.T_shutdown,
            style=Pack(padding=5, flex=1, height=30, font_size=15),
        )
        A_button = toga.Button(
            "Enter Time",
            on_press=self.A_shutdown,
            style=Pack(padding=5, flex=1, height=30, font_size=15),
        )

        TIME_SELECTION.add(T_hour_box)
        TIME_SELECTION.add(T_minute_box)
        TIME_SELECTION.add(T_second_box)
        TIME_SELECTION.add(T_button)

        AT_TIME.add(A_hour_box)
        AT_TIME.add(A_minute_box)
        AT_TIME.add(A_button)

        container = toga.OptionContainer()

        container.add("Time Till", TIME_SELECTION)
        container.add("At Time", AT_TIME)

        self.time_input = toga.TextInput(
            placeholder="Enter a time", style=Pack(width=500, height=20, font_size=15)
        )

        time_box = toga.Box(style=Pack(direction=ROW, padding=5))
        time_box.add(self.time_input)

        self.veiw_box.add(container)
        self.main_box.add(self.veiw_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    async def A_shutdown(self, widget):
        # get the value of A_hour_input and A_minute_input
        A_hour = str(self.A_hour_input.value)
        A_minute = str(self.A_minute_input.value)
        A_hour = A_hour.zfill(2)
        A_minute = A_minute.zfill(2)
        if A_hour == "None":
            A_hour = "00"
        if A_minute == "None":
            A_minute = "00"
        A_time = "%s:%s" % (A_hour, A_minute)

        # get the time
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        # clear the window
        # create a label that shows the time and the time when shutdown
        self.main_box.remove(self.veiw_box)
        time_label = toga.Label(
            "Current Time: %s" % current_time, style=Pack(padding=0, font_size=15)
        )
        self.main_box.add(time_label)
        # get the current time in seconds
        A = current_time.split(":")
        temp = int(A[0])
        temp2 = int(A[1])
        current_time_seconds = temp * 3600 + temp2 * 60

        # get the time when shutdown in seconds
        A = A_time.split(":")
        temp = int(A[0])
        temp2 = int(A[1])
        A_time_seconds = temp * 3600 + temp2 * 60

        difference = A_time_seconds - current_time_seconds
        if difference < 0:
            difference = difference + 86400

        b = difference

        def asd(num, in_min, in_max, out_min, out_max):
            return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        progress = toga.ProgressBar(
            max=100, value=0, style=Pack(padding=5, flex=1, font_size=15)
        )

        timeA = toga.Label(
            "Shut down time: %s" % A_time, style=Pack(padding=0, font_size=15)
        )

        seconds_till = toga.Label(
            "Seconds till shutdown: %s" % b, style=Pack(padding=0, font_size=15)
        )

        self.main_box.add(time_label)
        self.main_box.add(progress)
        self.main_box.add(toga.Divider())
        self.main_box.add(seconds_till)
        self.main_box.add(timeA)
        def convert(seconds):
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
      
            return "%d:%02d:%02d" % (hour, minutes, seconds)

        while b >= 0:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            time_label.text = "Current Time: %s" % current_time

            b = b - 1
            ayy = 100 - round(asd(b, 1, difference, 1, 100))
            print(ayy)
            if ayy > 100:
                ayy = 100
            progress.value = ayy
            seconds_till.text = "Time till shutdown: %s" % convert(b)
            await asyncio.sleep(1)

        print("!!!TIME!!!")
        os.system("shutdown /s /t 1")

    async def T_shutdown(self, widget):
        try:
            T_hour = self.T_hour_input.value
            T_minute = self.T_minute_input.value
            T_second = self.T_second_input.value
            if T_hour == None and T_minute == None and T_second == None:
                self.main_window.error_dialog("!Error!", "Enter a time that is not 0")
                return
            if T_hour == None and T_minute == None and T_second == 1:
                self.main_window.error_dialog(
                    "!Error!", "Enter a time that is bigger then 1 second"
                )
                return

            print("______________" + str(T_hour), str(T_minute), str(T_second))

            if T_hour == None:
                T_hour = 00
            if T_minute == None:
                T_minute = 00
            if T_second == None:
                T_second = 00

            print("______________" + str(T_hour), str(T_minute), str(T_second))

            T_tot = T_hour * 3600 + T_minute * 60 + T_second

            # calk the time at which the shutdown will happen
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_time_seconds = (
                int(current_time.split(":")[0]) * 3600
                + int(current_time.split(":")[1]) * 60
                + int(current_time.split(":")[2])
            )
            shutdown_time_seconds = current_time_seconds + T_tot
            shutdown_time = datetime.fromtimestamp(shutdown_time_seconds).strftime(
                "%H:%M"
            )
            time_label = toga.Label(
                "Current Time: %s" % current_time, style=Pack(padding=0, font_size=15)
            )

            # clear the window
            # create a label that shows the time and the time when shutdown
            self.main_box.remove(self.veiw_box)
            time_label = toga.Label(
                "Current Time: %s" % current_time, style=Pack(padding=0, font_size=15)
            )
            self.main_box.add(time_label)

            def asd(num, in_min, in_max, out_min, out_max):
                return (num - in_min) * (out_max - out_min) / (
                    in_max - in_min
                ) + out_min

            progress = toga.ProgressBar(
                max=1000, value=0, style=Pack(padding=5, flex=1, font_size=15)
            )
            b = T_tot
            timeA = toga.Label(
                "Shut down time: %s" % shutdown_time,
                style=Pack(padding=0, font_size=15),
            )
            seconds_l = toga.Label(
                "Seconds to death", style=Pack(padding=0, font_size=15)
            )
            self.main_box.add(time_label)
            self.main_box.add(progress)
            self.main_box.add(toga.Divider())
            self.main_box.add(seconds_l)
            self.main_box.add(timeA)

            def convert(seconds):
                seconds = seconds % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60
      
                return "%d:%02d:%02d" % (hour, minutes, seconds)

            while b >= 0:
                b = b - 1
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                seconds_l.text = "Time till shutdown: %s" % convert(b)
                time_label.text = "Current Time: %s" % current_time

                ayy = 1000 - round(asd(b, 1, T_tot, 1, 1000))
                print(ayy)
                if ayy > 1000:
                    ayy = 1000
                progress.value = ayy
                await asyncio.sleep(1)

            print("!!!TIME!!!")
            os.system("shutdown /s /t 1")
        except:
            self.main_window.error_dialog(
                "!Error!",
                "Make sure that you enter a time that is higher then 1 seconds\nIf this error keeps occuring, contact the developer",
            )
            return
        return


def main():
    return shutdown()
