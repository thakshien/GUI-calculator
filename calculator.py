import tkinter as tk

def click(x):
    if x == "=":
        try:
            v.set(eval(v.get()))
        except:
            v.set("Error")
    elif x == "C":
        v.set("")
    else:
        v.set(v.get() + x)

root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")

v = tk.StringVar()

tk.Entry(root, textvariable=v, font=("Arial", 20), justify="right").pack(fill="x", padx=10, pady=10)

for row in ["789/", "456*", "123-", "0.=+"]:
    f = tk.Frame(root)
    f.pack(expand=True, fill="both")
    for x in row:
        tk.Button(f, text=x, font=("Arial", 18),
                  command=lambda x=x: click(x)).pack(side="left", expand=True, fill="both")

tk.Button(root, text="C", font=("Arial", 18),
          command=lambda: click("C")).pack(fill="both", padx=10, pady=5)

root.mainloop()