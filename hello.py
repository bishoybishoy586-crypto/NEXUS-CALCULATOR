import tkinter as tk 
from PIL import Image, ImageTk
 
window=tk.Tk()
window.geometry("1400x700")


background_image = Image.open("background.png")
background_image = background_image.resize((1400, 700))

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(
    window,
    image=background_photo
)
background_label.place(
    x=0, y=0,
    relwidth=1,
    relheight=1
)
background_label.lower()




window.title("canculator")

# কালার চেঞ্জ করার কোডঃ 
clour="gray"
def window_colur():
    global clour
    if clour == "gray":
        clour = "red"
    elif clour == "red":
        clour = "Indigo"
    elif clour == "Indigo":
        clour = "Violet"
    elif clour == "Violet":
        clour = "Blue"
    elif clour == "Blue":
        clour = "Green"
    elif clour == "Green":
        clour = "Yellow"
    elif clour == "Yellow":
        clour = "Orange"
    elif clour == "Orange":
        clour = "black"
    elif clour == "black":
        clour = "gray"
        
    window.config(bg=clour)

# স্ক্রিনে নাম্বার যোগ করার কোড:

def number1():
    scrine.insert(tk.END,"1")


def number2():
    scrine.insert(tk.END,"2")
    
    
def number3():
    scrine.insert(tk.END,"3")

    

def number4():
    scrine.insert(tk.END,"4")
    
    

def number5():
    scrine.insert(tk.END,"5")
    
    

def number6():
    scrine.insert(tk.END,"6")
    
    
def number7():
    scrine.insert(tk.END,"7")


def number8():
    scrine.insert(tk.END,"8")
    

def number9():
    scrine.insert(tk.END,"9")
    

def number0():
    scrine.insert(tk.END,"0")
    
def dot():
    scrine.insert(tk.END,".")

def delete_scrine():
    scrine.delete(0,tk.END)




number=""
oparator=""

def plassw():
    global number, oparator
    number = float(scrine.get())
    oparator = "+"
    scrine.delete(0,tk.END)
def mainas_w():
    global number, oparator
    number = float(scrine.get())
    oparator ="-"
    scrine.delete(0,tk.END)
def gun_w():
    global number, oparator
    number = float(scrine.get())
    oparator="*"
    scrine.delete(0,tk.END)
def vag_w():
    global number,oparator
    number =float(scrine.get())
    oparator="/"
    scrine.delete(0,tk.END)

def calculate():
    global number, oparator ,index

    second_number = float(scrine.get())

    if oparator == "+":
        result = number + second_number

    elif oparator == "-":
        result = number - second_number
    elif oparator == "/":
        result=number/second_number
    elif oparator == "*":
        result= number*second_number
    elif oparator == "**":
        result=number**second_number
    elif oparator == "^":
        result = number * number

    history_box.insert(tk.END,f"({index}){number} {oparator} {second_number} = {result}\n")
    index+=1
    scrine.delete(0, tk.END)
    scrine.insert(tk.END, str(result))

    number = result

def cline_history():
    history_box.delete("1.0",tk.END)

# হিস্টরি বক্স
def opene_history():
    global history_box 
    history_box=tk.Text(window,font=("Comic Sans",10),height=20,width=20,bg="black",fg="white")
    history_box.place(x=1100,y=300)
    
    
index = 1

def rootw():
    global index
    number = float(scrine.get())
    result = number ** 0.5
    scrine.delete(0, tk.END)
    scrine.insert(tk.END, str(result))
    history_box.insert(tk.END,f"({index})√{number} = {result}\n")
    index+=1
def power_w():
    global index
    number = float(scrine.get())
    result = number * number
    scrine.delete(0,tk.END)
    scrine.insert(tk.END,str(result))
    history_box.insert(tk.END,f"({index})^ {number} = {result}\n")
    index+=1

def cros_1():
    if scrine.get():
        scrine.delete(len(scrine.get())-1,tk.END)


# satting ফাংশন এর কোডঃ
def setting_fangson():
    secondry_manu=tk.Toplevel(window)
    secondry_manu.title("⚙ Setting")
    secondry_manu.geometry("100x200+400+50")
    def gray_clure():
        window.config(bg="gray")
    settting_button1=tk.Button(secondry_manu,text="gray Thim",command=gray_clure,fg="black")
    settting_button1.place(x=3,y=2)
    def white():
        window.config(bg="white")
    settting_button2=tk.Button(secondry_manu,text="white Thim",fg="black",command=white)
    settting_button2.place(x=3,y=30)

    def system():
        window.config(bg="black")
    settting_button3=tk.Button(secondry_manu,text="System💻",fg="black",command=system)
    settting_button3.place(x=3,y=60)


    def close_history():
        history_box.destroy()
    history_clos=tk.Button(secondry_manu,text="Close History",command=close_history)
    history_clos.place(x=3,y=90)
           
        
    
    




# কালার চেঞ্জ বাটন
 
button=tk.Button(window,text="Custom Theme",bg="gray",command=window_colur)
button.place(x=150,y=7)

# স্ক্রিন এবং বাটন এর কোড 

scrine=tk.Entry(window,font=("Comic Sans",33))
scrine.place(x=50,y=100)

# সুইচ এর কোড 

button1=tk.Button(window,font=("Comic Sans",30),text="1",command=number1)
button1.place(x=50,y=200)

button2=tk.Button(window,text="2",font=("Comic Sans",30),command=number2)
button2.place(x=130,y=200 )

button3=tk.Button(window,text="3",font=("Comic Sans",30),command=number3)
button3.place(x=210,y=200)

button4=tk.Button(window,text="4",font=("Comic Sans",30),command=number4)
button4.place(x=290,y=200)

button5=tk.Button(window,text="5",font=("Comic Sans",30),command=number5)
button5.place(x=370,y=200)

button6=tk.Button(window,text="6",font=("Comic Sans",30),command=number6)
button6.place(x=50,y=300)

button7=tk.Button(window,text="7",font=("Comic Sans",30),command=number7)
button7.place(x=130,y=300)

button8=tk.Button(window,text="8",font=("Comic Sans",30),command=number8)
button8.place(x=210,y=300)

button9=tk.Button(window,text="9",font=("Comic Sans",30),command=number9)
button9.place(x=290,y=300)

button0=tk.Button(window,text="0",font=("Comic Sans",30),command=number0)
button0.place(x=370,y=300)

plass=tk.Button(window,text="+",font=("Comic Sans",20),command=plassw,width=5)
plass.place(x=470,y=200)

mainas=tk.Button(window,text="-",font=("Comic Sans",20),command=mainas_w,width=5)
mainas.place(x=470,y=300)


maltipla=tk.Button(window,text="*",font=("Comic Sans",20),command=gun_w,width=5)
maltipla.place(x=470,y=400)

vag=tk.Button(window,text="/",font=("Comic Sans",20),command=vag_w,width=5)
vag.place(x=470,y=500)


rut=tk.Button(window,text="√",font=("Comic Sans",30),command=rootw)
rut.place(x=50,y=400)

cros=tk.Button(window,text="X",font=("Comic Sans",30),command=cros_1)
cros.place(x=130,y=400)

power=tk.Button(window,text="^",font=("Comic Sans",30),command=power_w)
power.place(x=50,y=500)

delete=tk.Button(window,text="Delete",width=8,font=("Comic Sans",30),bg="red",command=delete_scrine)
delete.place(x=130,y=500)

delete_history=tk.Button(window,text="Clear\n History",width=5,font=("Comic Sans",19),bg="red",command=cline_history)
delete_history.place(x=340,y=500)

settting=tk.Button(window,text="   ⚙ Settings   ",bg="gray",command=setting_fangson)
settting.place(x=390,y=7)

equal=tk.Button(window,text="=",width=9,font=("Comic Sans",30),command=calculate,bg="pink")
equal.place(x=210,y=400)

op_history=tk.Button(window,text="      history      ",command=opene_history,bg="gray")
op_history.place(x=490,y=7)


# সাজানোর পর এর কাজ 

up_boundry=tk.Text(window,height=18,width=1,bg="black")
up_boundry.place(x=440,y=190)


# সেকেন্ডেরই স্ক্রিন 

def secondry_window():
    scientific = tk.Toplevel(window)
    scientific.title("Scientific Calculator - Student")
    scientific.geometry("600x600")
    scientific.config(bg="gray")

    screen = tk.Entry(
        scientific,
        font=("Arial", 25),
        justify="right"
    )
    screen.pack(fill="x", padx=10, pady=10, ipady=10)

    def insert(value):
        screen.insert(tk.END, value)

    def clear():
        screen.delete(0, tk.END)

    def calculate_scientific():   
        import math

        expression = screen.get()

        try:
            expression = expression.replace("^", "**")

            allowed = {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log": math.log10,
                "ln": math.log,
                "pi": math.pi,
                "e": math.e
            }

            result = eval(
                expression,
                {"__builtins__": {}},
                allowed
            )

            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))

        except Exception:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Invalid input")

    buttons = [
        ["sin(", "cos(", "tan(", "sqrt("],
        ["log(", "ln(", "pi", "e"],
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"], 
        ["1", "2", "3", "-"],
        ["0", ".", "^", "+"],
        ["(", ")", "C", "="]
    ]

    for row in buttons:
        frame = tk.Frame(scientific, bg="gray")
        frame.pack(fill="both", expand=True)

        for value in row:
            if value == "C":
                action = clear
            elif value == "=":
                action = calculate_scientific
            else:
                action = lambda v=value: insert(v)

            tk.Button(
                frame,
                text=value,
                font=("Arial", 15),
                command=action
            ).pack(
                side="left",
                fill="both",
                expand=True,
                padx=3,
                pady=3
            )
new_window=tk.Button(
    window,
    text="Scientific · Student Mode",
    bg="gray",
    command=secondry_window
)
new_window.place(x=0,y=7)


#প্রগ্রামার কেঙ্কুলেত্রঃ
def last_window1():
    last_window=tk.Tk()
    last_window.geometry("600x500")
    
last_window_button=tk.Button(window,text="programar canculator",command=last_window1,bg="gray")
last_window_button.place(x=250,y=7)

#প্রগ্রামার কেঙ্কুলেত্রঃ
def last_window1():
    last_window=tk.Tk()
    last_window.geometry("600x500")

last_window_button=tk.Button(window,text="programar canculator",command=last_window1,bg="gray")
last_window_button.place(x=250,y=7)


# প্রগ্রামার কেঙ্কুলেত্রঃ

def last_window1():
    last_window = tk.Toplevel(window)
    last_window.title("Programmer Calculator")
    last_window.geometry("900x650")
    last_window.config(bg="#202B38")

    mode = {"value": "DEC"}

    # সংখ্যা লেখার স্ক্রিন
    screen = tk.Entry(
        last_window,
        font=("Comic Sans", 30),
        bg="black",
        fg="white",
        justify="right"
    )
    screen.place(x=50, y=50, width=550, height=60)

    # বর্তমান মোড
    mode_label = tk.Label(
        last_window,
        text="Mode: DEC",
        font=("Comic Sans", 18),
        bg="#202B38",
        fg="white"
    )
    mode_label.place(x=50, y=125)

    # মোড পরিবর্তনের কোড
    def bin_w():
        mode["value"] = "BIN"
        mode_label.config(text="Mode: BIN")

    def oct_w():
        mode["value"] = "OCT"
        mode_label.config(text="Mode: OCT")

    def dec_w():
        mode["value"] = "DEC"
        mode_label.config(text="Mode: DEC")

    def hex_w():
        mode["value"] = "HEX"
        mode_label.config(text="Mode: HEX")

    # স্ক্রিনে সংখ্যা লেখার কোড
    def number0():
        screen.insert(tk.END, "0")

    def number1():
        screen.insert(tk.END, "1")

    def number2():
        screen.insert(tk.END, "2")

    def number3():
        screen.insert(tk.END, "3")

    def number4():
        screen.insert(tk.END, "4")

    def number5():
        screen.insert(tk.END, "5")

    def number6():
        screen.insert(tk.END, "6")

    def number7():
        screen.insert(tk.END, "7")

    def number8():
        screen.insert(tk.END, "8")

    def number9():
        screen.insert(tk.END, "9")

    def numberA():
        screen.insert(tk.END, "A")

    def numberB():
        screen.insert(tk.END, "B")

    def numberC():
        screen.insert(tk.END, "C")

    def numberD():
        screen.insert(tk.END, "D")

    def numberE():
        screen.insert(tk.END, "E")

    def numberF():
        screen.insert(tk.END, "F")

    def delete_screen():
        screen.delete(0, tk.END)

    # সংখ্যা পদ্ধতিতে রূপান্তর
    def convert_number():
        try:
            text = screen.get().strip()

            if mode["value"] == "BIN":
                number = int(text, 2)
            elif mode["value"] == "OCT":
                number = int(text, 8)
            elif mode["value"] == "DEC":
                number = int(text, 10)
            else:
                number = int(text, 16)

            if mode["value"] == "BIN":
                result = format(number, "b")
            elif mode["value"] == "OCT":
                result = format(number, "o")
            elif mode["value"] == "DEC":
                result = str(number)
            else:
                result = format(number, "X")

            screen.delete(0, tk.END)
            screen.insert(tk.END, result)

        except ValueError:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Invalid number")

    # দুইটি সংখ্যার Bitwise হিসাব
    def bitwise(operator):
        try:
            text = screen.get().strip()

            if mode["value"] == "BIN":
                first = int(text, 2)
            elif mode["value"] == "OCT":
                first = int(text, 8)
            elif mode["value"] == "DEC":
                first = int(text, 10)
            else:
                first = int(text, 16)

            if operator == "NOT":
                result = ~first
            else:
                screen.delete(0, tk.END)
                screen.insert(tk.END, str(first))
                screen.insert(tk.END, " ")
                screen.insert(tk.END, operator)
                screen.insert(tk.END, " ")
                screen.insert(tk.END, "Enter B separately")
                return

            screen.delete(0, tk.END)

            if mode["value"] == "BIN":
                answer = format(result, "b")
            elif mode["value"] == "OCT":
                answer = format(result, "o")
            elif mode["value"] == "DEC":
                answer = str(result)
            else:
                answer = format(result, "X")

            screen.insert(tk.END, answer)

        except ValueError:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Invalid number")

    # মোডের বাটন
    bin_button = tk.Button(
        last_window, text="BIN",
        font=("Comic Sans", 18), command=bin_w
    )
    bin_button.place(x=50, y=170)

    oct_button = tk.Button(
        last_window, text="OCT",
        font=("Comic Sans", 18), command=oct_w
    )
    oct_button.place(x=150, y=170)

    dec_button = tk.Button(
        last_window, text="DEC",
        font=("Comic Sans", 18), command=dec_w
    )
    dec_button.place(x=250, y=170)

    hex_button = tk.Button(
        last_window, text="HEX",
        font=("Comic Sans", 18), command=hex_w
    )
    hex_button.place(x=350, y=170)

    convert_button = tk.Button(
        last_window, text="Convert",
        font=("Comic Sans", 16), command=convert_number
    )
    convert_button.place(x=460, y=170)

    # সংখ্যার বাটন
    button1 = tk.Button(
        last_window, text="1",
        font=("Comic Sans", 22), command=number1
    )
    button1.place(x=50, y=250)

    button2 = tk.Button(
        last_window, text="2",
        font=("Comic Sans", 22), command=number2
    )
    button2.place(x=140, y=250)

    button3 = tk.Button(
        last_window, text="3",
        font=("Comic Sans", 22), command=number3
    )
    button3.place(x=230, y=250)

    button4 = tk.Button(
        last_window, text="4",
        font=("Comic Sans", 22), command=number4
    )
    button4.place(x=50, y=330)

    button5 = tk.Button(
        last_window, text="5",
        font=("Comic Sans", 22), command=number5
    )
    button5.place(x=140, y=330)

    button6 = tk.Button(
        last_window, text="6",
        font=("Comic Sans", 22), command=number6
    )
    button6.place(x=230, y=330)

    button7 = tk.Button(
        last_window, text="7",
        font=("Comic Sans", 22), command=number7
    )
    button7.place(x=50, y=410)

    button8 = tk.Button(
        last_window, text="8",
        font=("Comic Sans", 22), command=number8
    )
    button8.place(x=140, y=410)

    button9 = tk.Button(
        last_window, text="9",
        font=("Comic Sans", 22), command=number9
    )
    button9.place(x=230, y=410)

    button0 = tk.Button(
        last_window, text="0",
        font=("Comic Sans", 22), command=number0
    )
    button0.place(x=140, y=490)

    # Hexadecimal বাটন
    buttonA = tk.Button(
        last_window, text="A",
        font=("Comic Sans", 22), command=numberA
    )
    buttonA.place(x=350, y=250)

    buttonB = tk.Button(
        last_window, text="B",
        font=("Comic Sans", 22), command=numberB
    )
    buttonB.place(x=440, y=250)

    buttonC = tk.Button(
        last_window, text="C",
        font=("Comic Sans", 22), command=numberC
    )
    buttonC.place(x=530, y=250)

    buttonD = tk.Button(
        last_window, text="D",
        font=("Comic Sans", 22), command=numberD
    )
    buttonD.place(x=350, y=330)

    buttonE = tk.Button(
        last_window, text="E",
        font=("Comic Sans", 22), command=numberE
    )
    buttonE.place(x=440, y=330)

    buttonF = tk.Button(
        last_window, text="F",
        font=("Comic Sans", 22), command=numberF
    )
    buttonF.place(x=530, y=330)

    # Clear বাটন
    clear_button = tk.Button(
        last_window, text="C",
        font=("Comic Sans", 22),
        bg="red", command=delete_screen
    )
    clear_button.place(x=350, y=410)

    # Bitwise বাটন
    and_button = tk.Button(
        last_window, text="AND",
        font=("Comic Sans", 16),
        command=lambda: bitwise("AND")
    )
    and_button.place(x=650, y=250)

    or_button = tk.Button(
        last_window, text="OR",
        font=("Comic Sans", 16),
        command=lambda: bitwise("OR")
    )
    or_button.place(x=650, y=310)

    xor_button = tk.Button(
        last_window, text="XOR",
        font=("Comic Sans", 16),
        command=lambda: bitwise("XOR")
    )
    xor_button.place(x=650, y=370)

    not_button = tk.Button(
        last_window, text="NOT",
        font=("Comic Sans", 16),
        command=lambda: bitwise("NOT")
    )
    not_button.place(x=650, y=430)


last_window_button = tk.Button(
    window,
    text="Programmer Calculator",
    command=last_window1,
    bg="gray"
)
last_window_button.place(x=250, y=7)

window.mainloop()