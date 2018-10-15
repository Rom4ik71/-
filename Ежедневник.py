import calendar
import sys
try:
    import Tkinter
    import tkFont
except ImportError: 
    import tkinter as Tkinter
    import tkinter.font as tkFont
import sqlite3
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys
def delit(a):
    conn = sqlite3.connect("база_данных_ежедневника.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ежедневник WHERE Напоминание = ?",[a])
    conn.commit()
    conn.close()
    
def read():
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    baze=[]
    con=sqlite3.connect('база_данных_ежедневника.db')
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM Ежедневник")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            A.append(row[0])
            B.append(row[1])
            C.append(row[2])
            D.append(row[3])
            E.append(row[4])
            F.append(row[5])
            G.append(row[6])
    baze=[A,B,C,D,E,F,G]
    
    return baze

def ins(datecreat,date,sost,text,repeat,typ):
    con=sqlite3.connect('база_данных_ежедневника.db')
    kyrsor=con.cursor()
    kyrsor.execute("insert into Ежедневник values (?,?,?,?,?,?,'Нет')",[(datecreat),(date),(sost),(text),(repeat),(typ)])
    con.commit()
    con.close()    
    
class db:
    def __init__(self):
        self.con=sqlite3.connect('база_данных_ежедневника.db')
        self.kyrsor=self.con.cursor()
        self.kyrsor.execute('''CREATE TABLE IF NOT EXISTS Ежедневник(Дата создания text,Дата выполнения text,Состояние text,Текст напоминания text,Повтор напоминания text,Группа напоминания text, Просрочено? text)''')
        self.con.commit()        
class Main(tk.Frame):#Frame - контейнер\онструктор класса

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar=tk.Frame(bg="white",bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)

        self.add_png=tk.PhotoImage(file="иконка_добавить_задачу.png")
        btn_open_win=tk.Button(toolbar,text="Новое напоминание",command=self.open1,bd=0,compound=tk.TOP,image=self.add_png)
        btn_open_win.pack(side=tk.LEFT)

        self.add_png2=tk.PhotoImage(file="иконка_списка.png")
        btn_open_win2=tk.Button(toolbar,text="Напоминания",command=self.open2,bd=0,compound=tk.TOP,image=self.add_png2)
        btn_open_win2.pack(side=tk.LEFT)

        
        
    def open1(self):
        Child1()
    def open2(self):
        Child2()
    

class Child1(tk.Toplevel):        
    def ins1(self):
        n=int(self.combobox_date.get())
        b=int(self.combobox_month.get())
        if self.combobox_repeat.get()=="Никогда":
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),self.entry_disc.get(),self.combobox_repeat.get(),self.combobox_grup.get())
            self.destroy()
        if self.combobox_repeat.get()=="День":
            if n==31:
                n=0
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),self.entry_disc.get(),self.combobox_repeat.get(),self.combobox_grup.get())
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(n+1),self.combobox_sost.get(),str(self.entry_disc.get())+"-(повтор)",self.combobox_repeat.get(),self.combobox_grup.get())
            self.destroy()
        if self.combobox_repeat.get()=="Неделю":
            if n+7>31:
                n=31-n
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),self.entry_disc.get(),self.combobox_repeat.get(),self.combobox_grup.get())
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(n),self.combobox_sost.get(),str(self.entry_disc.get())+"-(повтор)",self.combobox_repeat.get(),self.combobox_grup.get())
            self.destroy()
        if self.combobox_repeat.get()=="Месяц":
            if b==12:
                b=0
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),self.entry_disc.get(),self.combobox_repeat.get(),self.combobox_grup.get())
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(b+1)+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),str(self.entry_disc.get())+"-(повтор)",self.combobox_repeat.get(),self.combobox_grup.get())
            self.destroy()
        if self.combobox_repeat.get()=="Год":
            ins(str(datetime.datetime.today()).split()[0],str(self.combobox_year.get())+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),self.entry_disc.get(),self.combobox_repeat.get(),self.combobox_grup.get())
            ins(str(datetime.datetime.today()).split()[0],str(int(self.combobox_year.get())+1)+'-'+str(self.combobox_month.get())+'-'+str(self.combobox_date.get()),self.combobox_sost.get(),str(self.entry_disc.get())+"-(повтор)",self.combobox_repeat.get(),self.combobox_grup.get())
            self.destroy()
            
    def __init__(self):
        super().__init__(root)
        self.init_child1()

    def init_child1(self):

        self.title("Новое напоминание")
        self.geometry("320x250")
        self.resizable(False,False)

        label_date=tk.Label(self,text="Дата напоминания:")
        label_date.place(x=10,y=20)

        label_date=tk.Label(self,text="Статус:")
        label_date.place(x=10,y=80)

        label_disc=tk.Label(self,text="Напоминание:")
        label_disc.place(x=10,y=120)

        label_repeat=tk.Label(self,text="Повторить через:")
        label_repeat.place(x=10,y=160)

        label_grup=tk.Label(self,text="Группа:")
        label_grup.place(x=10,y=200)
        
        self.combobox_date=ttk.Combobox(self,values=[u"01",u"02",u"03",u"04",u"05",u"06",u"07",u"08",u"09",u"10",u"11",u"12",u"13",u"14",u"15",u"16",u"17",u"18",u"19",u"20",u"21",u"22",u"23",u"24",u"25",u"26",u"27",u"28",u"29",u"30",u"31"])
        self.combobox_date.current(0)
        self.combobox_date.place(x=125,y=0)

        self.combobox_month=ttk.Combobox(self,values=[u"01",u"02",u"03",u"04",u"05",u"06",u"07",u"08",u"09",u"10",u"11",u"12"])
        self.combobox_month.current(0)
        self.combobox_month.place(x=125,y=20)

        self.combobox_year=ttk.Combobox(self,values=[u"2018",u"2019",u"2020",u"2021",u"2022",u"2023",u"2024"])
        self.combobox_year.current(0)
        self.combobox_year.place(x=125,y=40)
        
        self.combobox_sost=ttk.Combobox(self,values=["Не срочно","Срочно","Очень важно"])
        self.combobox_sost.current(0)
        self.combobox_sost.place(x=125,y=80)
        
        self.entry_disc=ttk.Entry(self)
        self.entry_disc.place(x=125,y=120)
        
        self.combobox_repeat=ttk.Combobox(self,values=[u"Никогда",u"День",u"Неделю",u"Месяц",u"Год"])
        self.combobox_repeat.current(0)
        self.combobox_repeat.place(x=125,y=160)
        
        self.combobox_grup=ttk.Combobox(self,values=["Общее","Дом","Работа","Отдых"])
        self.combobox_grup.current(0)
        self.combobox_grup.place(x=125,y=200)

        btn_save=ttk.Button(self,text="Сохранить",command=self.ins1)
        btn_save.place(x=15,y=225)

        
        
        btn_out=ttk.Button(self,text="Выход",command=self.destroy)
        btn_out.place(x=230,y=225)
        
        self.grab_set()
        self.focus_set()

class Child2(tk.Toplevel):

    def open6(self):
        Child2()
        self.destroy()
            
    def open5(self):
        if len(read()[0])>0:
            Redactor1()
            self.destroy()
        else:
            mb.showerror("Ошибка","У вас нет напоминаний!!!")

    def open4(self):
        if len(read()[0])>0:
            Redactor()
            self.destroy()
        else:
            mb.showerror("Ошибка","У вас нет напоминаний!!!")
    
    def __init__(self):
        super().__init__(root)
        self.init_child2()

    def init_child2(self):
        self.title("Напоминания")
        self.geometry("955x400")
        self.resizable(False,False)       
    
        self.tree=ttk.Treeview(self, columns=("Дата создания", "Дата выполнения", "Состояние", "Напоминание","Повтор напоминания","Группа напоминания","Просрочено?"), height=15, show="headings")

        self.tree.column("Дата создания", width=100, anchor=tk.CENTER)
        self.tree.column("Дата выполнения", width=115, anchor=tk.CENTER)
        self.tree.column("Состояние", width=100, anchor=tk.CENTER)
        self.tree.column("Напоминание", width=300, anchor=tk.CENTER)
        self.tree.column("Повтор напоминания", width=120, anchor=tk.CENTER)
        self.tree.column("Группа напоминания", width=130, anchor=tk.CENTER)
        self.tree.column("Просрочено?", width=85, anchor=tk.CENTER)
        
        self.tree.heading("Дата создания", text="Дата создания")
        self.tree.heading("Дата выполнения", text="Дата выполнения")
        self.tree.heading("Состояние", text="Состояние")
        self.tree.heading("Напоминание", text="Текст напоминания")
        self.tree.heading("Повтор напоминания", text="Напомнить через:")
        self.tree.heading("Группа напоминания", text="Группа напоминания")
        self.tree.heading("Просрочено?", text="Просрочено?")

        self.data=read()
        self.pref=[]

        for i in range(0,len(self.data[0])):
            for n in range(7):
                self.pref.append(self.data[0:7][n][i])
            self.tree.insert('','end',values=self.pref)
            self.pref=[]
                
        self.tree.pack()

        btn_out=ttk.Button(self,text="Редактировать",command=self.open5)
        btn_out.place(x=150,y=350)
        
        btn_out=ttk.Button(self,text="Удалить напоминание",command=self.open4)
        btn_out.place(x=550,y=350)

        btn_out=ttk.Button(self,text='обновить',command=self.open6)
        btn_out.place(x=350,y=350)

        btn_out=ttk.Button(self,text="Выход",command=self.destroy)
        btn_out.place(x=850,y=350)

        self.grab_set()
        self.focus_set()

class Redactor1(tk.Toplevel):
        def open1(self):
            Child1()
            delit(self.combobox_repeat.get())
            self.destroy()
        def __init__(self):
                super().__init__(root)
                self.init_Redactor1()
    
        def init_Redactor1(self):
            self.title("Изминить напоминание")
            self.geometry("270x130")
            self.resizable(False,False)

            label_grup=tk.Label(self,text="Какое напоминание вы хотите изминить:")
            label_grup.place(x=25,y=20)

            btn_out=ttk.Button(self,text="Редактировать",command=self.open1)
            btn_out.place(x=10,y=100)

            self.combobox_repeat=ttk.Combobox(self,values=read()[3])
            self.combobox_repeat.current(0)
            self.combobox_repeat.place(x=60,y=60)

            btn_out=ttk.Button(self,text="Выход",command=self.destroy)
            btn_out.place(x=100,y=100)
            
            self.grab_set()
            
class Redactor(tk.Toplevel): 
        def delit1(self):
            delit(self.combobox_repeat.get())
            self.destroy()
            Child2()
        def __init__(self):
                super().__init__(root)
                self.init_Redactor()
        
        def init_Redactor(self):
            self.title("Удалить напоминание")
            self.geometry("270x130")
            self.resizable(False,False)

            label_grup=tk.Label(self,text="Какое напоминание вы хотите удалить:")
            label_grup.place(x=25,y=20)

            btn_out=ttk.Button(self,text="Удалить",command=self.delit1)
            btn_out.place(x=10,y=100)

            self.combobox_repeat=ttk.Combobox(self,values=read()[3])
            self.combobox_repeat.current(0)
            self.combobox_repeat.place(x=60,y=60)

            btn_out=ttk.Button(self,text="Выход",command=self.destroy)
            btn_out.place(x=100,y=100)
            
            self.grab_set()
            self.focus_set()


def get_calendar(locale, fwday):
    if locale is None:
        return calendar.TextCalendar(fwday)
    else:
        return calendar.LocaleTextCalendar(fwday, locale)

class Calendar(ttk.Frame):

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, **kw):

        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = self.datetime(year, month, 1)
        self._selection = None 

        ttk.Frame.__init__(self, master, **kw)

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()      
        self.__place_widgets()      
        self.__config_calendar()   
        self.__setup_selection(sel_bg, sel_fg)

        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        self._build_calendar()
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        hframe = ttk.Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font()
        self._canvas = canvas = Tkinter.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    def _pressed(self, evt):
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            return

        item_values = widget.item(item)['values']
        if not len(item_values): 
            return

        text = item_values[int(column[1]) - 1]
        if not text: 
            return

        bbox = widget.bbox(item, column)
        if not bbox: 
            return

        
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

    def _prev_month(self):
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() 

    def _next_month(self):
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() 

    @property
    def selection(self):
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))


def myfunction():
    root2=Tkinter.Toplevel(root)
    ttkcal = Calendar(root2,firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=1, fill='both')
if __name__=="__main__":
    root=tk.Tk()
    app=Main(root)
    app.pack
    root.title("Ежедневник")
    root.geometry("255x320")
    root.resizable(False,False)
    frame=Tkinter.Frame(root)
    frame.place(x=10,y=150)
    ttkcal = Calendar(frame,firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=1, fill='both')
    root.mainloop()
