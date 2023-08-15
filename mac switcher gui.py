import tkinter as tk

def printing(myString, n):
    myList = ["", ":", "-"]
    bigString = ""
    for i in myList:
        bigString += "\n" + i.join((myString.lower()).split(n))
        bigString += "\n" + i.join((myString.upper()).split(n))
    return bigString

def printingTwo(myString):
    bigString = ""
    listOne = []
    stringOne = ""
    i = 0
    while i < 12:
        stringOne += myString[i]
        i += 1
        if len(stringOne) == 2:
            listOne.append(stringOne)
            stringOne = ""
    myList = ["", ":", "-"]
    for i in myList:
        bigString += "\n" + (i.join(listOne)).lower()
        bigString += "\n" + (i.join(listOne)).upper()
    return bigString

def returnText(enteredMac):
    endGoal = ""
    if (":" in enteredMac):
        endGoal = printing(enteredMac, ":")
    elif ("-" in enteredMac):
        endGoal = printing(enteredMac, "-")
    elif (len(enteredMac) == 12):
        endGoal = printingTwo(enteredMac)
    return endGoal

def handle_keypress(event, entry_window, result_label):
    mac = entry_window.get()
    result_label.insert(1.0, mac + "\n" + returnText(mac))

def main():
    window = tk.Tk()
    greeting = tk.Label(text="Enter a MAC")
    entry = tk.Entry()
    result = tk.Text()
    
    greeting.pack()
    entry.pack()
    result.pack()
    mac = entry.get()

    # ChatGPT helped here
    entry.bind("<Return>", lambda event: handle_keypress(event, entry, result))
    result.configure(state="normal")
    window.mainloop()

if __name__ == "__main__":
    main()