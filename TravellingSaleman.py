

from tkinter import *
from tkinter import messagebox
import sqlite3
ARIAL = ("arial",10,"bold")

class tsp:
    def __init__(self,root):
        self.conn = sqlite3.connect("travelling.db", timeout=100)
        self.login = False
        self.root = root
         #for the heading
        self.header2 = Label(self.root, text="Travelling Salesman",bg="#5858FA", fg="white", font=("arial", 20, "bold"))
        self.header2.pack(fill=X)

        self.frame = Frame(self.root,width=600,height=400,bg='#CEF6F5')  #
        #Login Page Form Component
        self.header = Label(self.frame, text="Welcome Login...",bg='#CEF6F5',fg="#FF5B33", font=("arial", 20, "bold"))  #bg="#66ffff",

        self.userlabel =Label(self.frame,text="Username",bg="#81BEF7",fg="white",font=ARIAL)
        self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#07E4F5",
           highlightthickness=3,        #for the thickness of the fields
            highlightbackground="black")

        self.plabel = Label(self.frame, text="Password",bg="#81BEF7",fg="white",font=ARIAL)##50A8B0
        self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#07E4F5" ,#"#2E2EFE",
           highlightthickness=3,
            highlightbackground="black")

        self.button = Button(self.frame,text="LOGIN",bg="#04B45F",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Quit",bg="#FF0000",fg="white",font=ARIAL,command = self.root.destroy)
        self.header.place(x=140, y=2, width=300, height=30)
        self.userlabel.place(x=153,y=100,width=120,height=20)
        self.uentry.place(x=153,y=130,width=200,height=22)  # username entry
        self.plabel.place(x=153,y=160,width=120,height=20)
        self.pentry.place(x=153,y=190,width=200,height=22)  # password entry
        self.button.place(x=153,y=230,width=80,height=20)
        self.q.place(x=273,y=230,width=80,height=20)
        self.frame.pack()

    def verify(self):  # verifying of authorised user
        ac = False
        self.temp = self.conn.execute("select * from salesman where u_name = ? ", (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[3] == self.pentry.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                messagebox._show("Login Info", m)

                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login Unsucessful ! Wrong Password"
                messagebox._show("Login Info!", m)

        if not ac:
            m = " Wrong Username !"
            messagebox._show("Login Info!", m)

    def MainMenu(self):
        self.frame = Frame(self.root,width=80,height=40)    #,bg='#FAD7A0'

        root.geometry("600x800")

        self.labelde = Label(self.frame, text='Select starting point', fg='#E74C3C', font=("ARIAL", 15))  #bg='#FAD7A0',
        self.labelde.pack(ipadx=5,pady=5)


        self.city = StringVar(root)
        self.city.set("Jalandhar")  # fix default place

        w = OptionMenu(self.frame, self.city, "Jalandhar", "Chandigarh", "Ludhiyana", "Patiyala", "Amritsar")
        w.configure(bg='#3498DB',fg='white',font=ARIAL,highlightcolor="red")
        w.pack(ipadx=5)

        self.detail = Button(self.frame, text="Shortest dist.", bg="#1393A3", fg="white", font=ARIAL, command=self.bulao)
        self.detail.pack(ipadx=5)

        self.clr = Button(self.frame, text="clear", bg="#0A69C5", fg="white", font=ARIAL, command=self.clr)
        self.clr.pack(ipadx=8)


        self.frame.pack()


    def clr(self):
        self.frame.destroy()
        self.MainMenu()


    def bulao(self):
        self.routes = []

        def find_paths(node, cities, path, distance):
            # Add node

            path.append(node)

            # Calculate path length
            if len(path) > 1:
                distance += cities[path[i]][node]

            # If path contains all cities and is not a dead end,
            # add path from last to first city and return.
            if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
                path.append(path[0])
                distance += cities[path[i]][path[0]]

                self.label11 = Label(self.frame, text=path, font=ARIAL,fg='#0ACBEB')
                self.label11.pack()
                self.routes.append([distance, path])

            # paths for all possible cities not yet used
            for city in cities:
                if (city not in path) and (node in cities[city]):
                    find_paths(city, dict(cities), list(path), distance)

        cities = {
            'Ludhiyana': {'Ludhiyana': 0, 'Jalandhar': 61, 'Amritsar': 140, 'Chandigarh': 106, 'Patiyala': 93},
            'Jalandhar': {'Ludhiyana': 61, 'Jalandhar': 0, 'Amritsar': 80, 'Chandigarh': 149, 'Patiyala': 154},
            'Amritsar': {'Ludhiyana': 140, 'Jalandhar': 80, 'Amritsar': 0, 'Chandigarh': 229, 'Patiyala': 235},
            'Chandigarh': {'Ludhiyana': 106, 'Jalandhar': 149, 'Amritsar': 229, 'Chandigarh': 0, 'Patiyala': 75},
            'Patiyala': {'Ludhiyana': 93, 'Jalandhar': 154, 'Amritsar': 235, 'Chandigarh': 75, 'Patiyala': 0},
        }
        start = str(self.city.get())
        text1 = 'Start from : ' + start
        self.label2 = Label(self.frame, text=text1, font=ARIAL,fg='#8E44AD')
        self.label2.pack()
        self.label3 = Label(self.frame, text="All Possible Ways for Returning  " +start , font=ARIAL,fg='#3341FF')
        self.label3.pack()
        if (start == 'Jalandhar'):
            i = -2;
        else:
            i = -1;
        find_paths(start, cities, [], 0)

        self.routes.sort()
        if len(self.routes) != 0 and start == 'Jalandhar':

            text2 = 'Shortest Route : ' + str(self.routes[0][1])
            self.label3 = Label(self.frame, text=text2, font=ARIAL,fg='#FF5B33')
            self.label3.pack()
        else:

            text3 = 'Shortest Route : ' + str(self.routes[0][1])  #[1]
            self.label4 = Label(self.frame, text=text3, font=ARIAL,fg='#FF5B33')
            self.label4.pack()
root = Tk()
root.title("TRAVELLING SALESMAN")
root.geometry("600x420")
#root.wm_iconbitmap("subway.png")
obj = tsp(root)

root.mainloop()
