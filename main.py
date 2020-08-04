#!/usr/bin/python3

# A Break Timer which is helpful for taking short breaks
# when staring at the screen for long time

from tkinter import *
from tkinter.ttk import *

# length and max of the progress bar
breakbar_length_max = 15000

# The time step
sleep_time_one_second = 0.001

# Start the timer
def startBreakTimer():
    import time

    for i in range(1, breakbar_length_max, 1):
        breakbar["value"] = i
        root.update_idletasks()
        time_remaining_str = (
            "Time Remaining:  "
            + str(round((breakbar_length_max - i) / 1000, 1))
            + " seconds"
        )
        time_remain.configure(
            text=time_remaining_str, foreground="white", background="black"
        )
        time.sleep(sleep_time_one_second)
    breakbar["value"] = breakbar_length_max
    root.destroy()


# ----------------------------------------------------------------------------

# Root Window
root = Tk()
root["background"] = "#000000"
root.title("Break Timer")
root.resizable(False, False)

# Center The window
window_height = 900
window_width = 1200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(
    "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
)

# --------------------------------------------------------------------------------

# The image
meditation_img = PhotoImage(file="meditation.gif")
meditate_label = Label(root, image=meditation_img)
meditate_label.pack(padx=50, pady=50)

# some style
s = Style()
s.theme_use("clam")
s.configure(
    "Horizontal.TProgressbar",
    troughcolor="white",
    foreground="red",
    background="red",
    thickness=10,
)

# --------------------------------------------------------------------------------

# configure the image
meditate_label.configure(background="#000031")

# The progress bar
breakbar = Progressbar(
    root,
    style="Horizontal.TProgressbar",
    length=1000,
    mode="determinate",
    maximum=breakbar_length_max,
    value=300,
)
breakbar.pack(padx=20, pady=5)

# The time remaining label
time_remain = Label(root, font=("Libre Baskerville", 12), justify=LEFT)
time_remain.pack(padx=2, pady=10)


# The message to be shown
label_text = """\
ENOUGH  STARING  AT  THE  SCREEN...

Stretch yourself. Take your eyes away from the screen.
Just Relax and Continue :)
"""

# label essentials
label = Label(root, text=label_text, font=("Libre Baskerville", 20), justify=CENTER)
label.pack(padx=10, pady=50)
label.configure(foreground="yellow", background="#000000")

# start
startBreakTimer()

# The main loop
root.mainloop()
