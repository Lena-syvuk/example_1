from tkinter import *
root = Tk()
root.geometry("700x250")

main_menu = Menu()
main_menu.add_command(label="Creating a record")
main_menu.add_command(label="Looking for a record")
main_menu.add_command(label="Editing a record")
main_menu.add_command(label="Deleting a record")
main_menu.add_separator()
main_menu.add_command(label="Exit")

root.config(menu=main_menu)
root.mainloop()

