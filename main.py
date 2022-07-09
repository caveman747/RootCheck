import os
import subprocess
import tkinter as tk

def main():
    if os.geteuid() == 0:
        root = tk.Tk()
        root.geometry("600x400")
        root.title("Root Check!")
        label1 = tk.Label(root, text="We rooted!")
        label1.pack()
        root.mainloop()
    else:
        root = tk.Tk()

        root.title("Root Check!")

        canvas1 = tk.Canvas(root, width=400, height=300)
        canvas1.pack()

        entry1 = tk.Entry(root)
        canvas1.create_window(200, 140, window=entry1)

        def RootCheck():
            rootpass = entry1.get()
            passfile = open("/home/john/PycharmProjects/AdJoiner/pass.txt", "w+")
            passfile.write(rootpass)
            passfile.close()
            subprocess.Popen(["sudo", "-S", "ls" "</passfile.txt"], stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE)

        button1 = tk.Button(text="Enter Root/Sudo Password", command=lambda: [RootCheck(), root.destroy()])
        canvas1.create_window(200, 180, window=button1)
        root.mainloop()

        subprocess.call(["sudo", "mkdir", "test"])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
