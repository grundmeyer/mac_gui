import tkinter as tk

def printing(mac):
    listOne = []
    listCisco = []
    stringOne = ""
    stringCisco = ""
    bigString = ""
    i = 0
    while i < 12:
        stringOne += mac[i]
        stringCisco += mac[i]
        i += 1
        if len(stringOne) == 2:
            listOne.append(stringOne)
            stringOne = ""
        if len(stringCisco) == 4:
            listCisco.append(stringCisco)
            stringCisco = ""
    myList = ["", ":", "-"]
    for i in myList:
        bigString += "\n" + ((i.join(listOne)).lower())
        bigString += "\n" + ((i.join(listOne)).upper())
    bigString += "\n" + ((".".join(listCisco)).lower())
    bigString += "\n" + ((".".join(listCisco)).upper())
    return bigString

def returnText(enteredMac):
    mac = enteredMac.strip() 
    endGoal = ""

    if (":" in mac):
        endGoal = printing("".join(mac.split(":")))
    elif ("-" in mac):
        endGoal = printing("".join(mac.split("-")))
    elif ("." in mac):
        endGoal = printing("".join(mac.split(".")))   
    elif (len(mac) == 12):
        endGoal = printing(mac)
    return endGoal

def handle_keypress(event, entry_window, result_label):
    mac = entry_window.get()
    result_label.delete(1.0, tk.END)
    result_label.tag_configure("center", justify="center")
    result_label.insert(1.0, returnText(mac), "center")

def main():
    window = tk.Tk()
    window.title("MAC Address Converter")
    greeting = tk.Label(text="Enter a MAC")
    entry = tk.Entry()
    result = tk.Text(height=10, width= 50, padx=25, pady=10, font=("Consolas", 11))
    
    greeting.pack()
    entry.pack()
    result.pack()

    # ChatGPT helped here
    entry.bind("<Return>", lambda event: handle_keypress(event, entry, result))
    result.configure(state="normal")
    window.mainloop()

if __name__ == "__main__":
    main()