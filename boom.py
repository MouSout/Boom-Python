import time
import tkinter as tk
from PIL import Image, ImageTk

def blue_screen():
    root = tk.Tk()
    root.title("Blue Screen of Death")
    root.geometry("1920x1080")

    current_state = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not current_state)

    root.config(cursor="none")

    try:
        image = Image.open("blue_screen.png")
        image = image.resize((1920, 1080), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error occurred: {e}")
        return
    label = tk.Label(root, image=photo)
    label.pack()

    label.image = photo

    root.mainloop()
print("warning: Your computer will blue screen in 5 seconds.")
print("so, you want exit this program!")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
blue_screen()
print("Congratulations! You know this is a joker program, so you can exit this program now.")
time.sleep(86400)
exit()