from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "#x2713"
reps = 0
timer_reset = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer_reset)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text=f"Long break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # call the method itemconfig in canvas,
                                                                    # pass which element is going to be changed and
                                                                    # what is going to change

    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for n in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # read the image
canvas.create_image(175, 112, image=tomato_img)  # specify X and Y position and the image
timer_text = canvas.create_text(178, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=('', 15))
check_mark.grid(row=3, column=1)

window.mainloop()
