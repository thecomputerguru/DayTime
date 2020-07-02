#DayTime
#
#
#Import modules
import tkinter as tk
from datetime import date
from datetime import datetime
from datetime import timedelta
#
#Program methods
class Program():

    def getDate():  # Method to retrieve today's date
        today_date = date.today()
        current_date_label.config(text=date.today().strftime("%A, %B %d %Y"))
        get_date = root.after(1000,Program.getDate)   #Loop method

    def getTomorrowDate():  #Method to retrieve tomorrow's date
        today = date.today()
        tomorrow = today + timedelta(days=1)
        next_date_label.config(text=tomorrow.strftime('%A, %B %d %Y'))
        get_tomorrow_date = root.after(1000,Program.getTomorrowDate)    #Loop method

    def getTime():   #Method to retrieve current time
        time = datetime.now()
        current_time_label.config(text=time.strftime('%I:%M:%S %p'))
        get_time = root.after(1000,Program.getTime)   #Loop method

    def getRemainingTime():   #Method to retrieve remaining time for today
        hr = datetime.now().hour
        min = datetime.now().minute
        sec = datetime.now().second
        remainH = 23 - hr
        remainM = 59 - min
        remainS = 59 - sec
        remaining_time_label.config(text='-'+str(remainH)+':'+str(remainM)+':'+str(remainS))
        r_time = root.after(1000,Program.getRemainingTime)   #Loop method

class Window(tk.Frame):   #Window object
    def __init__(self,window):
        tk.Frame.__init__(self,window)
        self.window = window
        self.window.title('DayTime')
        self.window.geometry('245x260')
        global current_date_label,current_time_label,next_date_label,remaining_time_label
        current_date_frame = tk.LabelFrame(self.window,text='Today',width=200,height=45)
        current_date_label = tk.Label(self.window,text='')
        current_time_frame = tk.LabelFrame(self.window,text='Current Time',width=120,height=45)
        current_time_label = tk.Label(self.window,text='')
        next_date_frame = tk.LabelFrame(self.window,text='Tomorrow',width=200,height=45)
        next_date_label = tk.Label(self.window,text='')
        remaining_time_frame = tk.LabelFrame(self.window,text='Remaining time until next day',width=210,height=45)
        remaining_time_label = tk.Label(self.window,text='')
        current_date_frame.place(x=20,y=30)
        current_date_label.place(x=30,y=50)
        next_date_frame.place(x=20,y=80)
        next_date_label.place(x=35,y=100)
        current_time_frame.place(x=20,y=130)
        current_time_label.place(x=30,y=150)
        remaining_time_frame.place(x=20,y=180)
        remaining_time_label.place(x=30,y=200)

def start():    #Run program
    Program.getDate()
    Program.getTomorrowDate()
    Program.getTime()
    Program.getRemainingTime()

root = tk.Tk()
app = Window(root)
start()
root.mainloop()
