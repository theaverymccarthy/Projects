from tkinter import *
import numpy as np

def interface():
    root = Tk()
    root.geometry("300x300")
    root.title("Sir Craigulon searcher of lists")
    wants = np.array([])
    
    def takeInput():
        INPUT = inputtxt.get("1.0", "end-1c")
        Output.insert(0,INPUT + " ")
        wants.append(INPUT)
        inputtxt.delete("1.0", END)
        
    l = Label(text = "What is it you wish to search for peasant?")
    inputtxt = Text(
        root, 
        height = 10,
        width = 25,
        bg = "orange"
        )
    
    Output = Entry(
        root,  
        width = 25,
        bg = "light cyan"
        )
    
    Display = Button(
        root, height = 2,
        width = 20, 
        text ="Log Desire",
        command = lambda:takeInput()
        )
                    

    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()

    
    mainloop()
    for i in wants:
        print(i)
    return wants


if __name__ == '__main__':
    interface()
