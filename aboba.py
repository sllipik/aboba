import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.overrideredirect(True)
    
class WelcomeWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("АБОБА")
        center_window(self.window, 300, 150)
        self.window.resizable(False, False)

        frame = ttk.Frame(self.window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(frame, text="Добро пожаловать в Клан!\n Докажи что ты истинный абоба!", font=("Arial", 12, "bold"), justify='center', anchor='center')
        label.pack(pady=10)

        btn = ttk.Button(frame, text="Доказать", command=self.close_and_open_auth)
        btn.pack(pady=10)

    def close_and_open_auth(self):
        self.window.destroy()
        open_auth_window()

def open_auth_window():
    root_auth = tk.Tk()
    login_app = LoginWindow(root_auth)
    root_auth.mainloop()
    
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('АБОБА')
        center_window(self.root, 300, 200)
        self.root.resizable(False, False)

        frame = ttk.Frame(root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text='Введи свое имя: ').grid(row=0, column=0, sticky='w', pady=5)
        self.entry_login = ttk.Entry(frame, width=20)
        self.entry_login.grid(row=0, column=1, pady=5)

        btn_login = ttk.Button(frame, text='Доказать!', command=self.check_auth)
        btn_login.grid(row=2, column=0, columnspan=2, pady=20)

        self.entry_login.bind('<Return>', lambda e: self.check_auth())

    def check_auth(self):
        login = self.entry_login.get().strip()

        if not login:
            messagebox.showwarning('СТОЯТЬ!', 'ВВЕДИ СВОЕ ИМЯ ЧТОБЫ УЗНАТЬ КТО ТЫ!')
            return

        if login == 'АБОБА':
            self.login_success()
        else:
            messagebox.showerror('СТОЯТЬ!', 'ТЫ НЕ ПОХОЖ НА АБОБУ!')

    def login_success(self):
        self.root.destroy()
        main_root = tk.Tk()
        main_root.title('АБОБА')
        center_window(main_root, 400, 200)
        app = App(main_root)
        main_root.mainloop()

class App:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        self.spam = False
        self.windows = []
        label = ttk.Label(frame, text=f'ТЫ ПРАВДА АБОБА!', font=("Arial", 12, "bold"), justify='center', anchor='center')
        label.pack(side=tk.TOP)

        self.btn1 = ttk.Button(frame, text='БОЛЬШЕ АБОБЫ', command=self.start_aboba)
        self.btn1.pack(pady=10)

        btn2 = ttk.Button(frame, text='ОТКАЗАТЬ АБОБЕ', command=self.stop_aboba)
        btn2.pack(pady=10)


    def start_aboba(self):
        if not self.spam:
            self.spam = True
            self._spamaboba()
            
            self.btn1.config(text=f'ЕЩЕ БОЛЬШЕ АБОБЫ!!!!', command=self.speed_up)
            
    def speed_up(self):
        if self.spam:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            win_width = 200
            win_height = 100
            x = random.randint(0, screen_width - win_width)
            y = random.randint(0, screen_height - win_height)

            new_win = tk.Toplevel(self.root)
            new_win.title("АБОБА")
            new_win.overrideredirect(True)
            new_win.geometry(f"{win_width}x{win_height}+{x}+{y}")
            label = ttk.Label(new_win, text="АБОБА", font=("Arial", 20, "bold"))
            label.pack(expand=True)
            self.windows.append(new_win)
            new_win.protocol("WM_DELETE_WINDOW", lambda w=new_win: self._close_aboba(w))
            self.root.after(50, self._spamaboba)

    def _spamaboba(self):
        if self.spam:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            win_width = 200
            win_height = 100
            x = random.randint(0, screen_width - win_width)
            y = random.randint(0, screen_height - win_height)

            new_win = tk.Toplevel(self.root)
            new_win.title("АБОБА")
            new_win.overrideredirect(True)
            new_win.geometry(f"{win_width}x{win_height}+{x}+{y}")
            label = ttk.Label(new_win, text="АБОБА", font=("Arial", 20, "bold"))
            label.pack(expand=True)
            self.windows.append(new_win)

            new_win.protocol("WM_DELETE_WINDOW", lambda w=new_win: self._close_aboba(w))
            self.root.after(200, self._spamaboba)

    def _close_aboba(self, win):
        if win in self.windows:
            self.windows.remove(win)
        win.destroy()

    def stop_aboba(self):
        self.spam = False
        for win in self.windows:
            win.destroy()
        self.windows.clear()
        self.root.destroy()
        show_farewell()
    
def show_farewell():
    farewell = tk.Tk()
    farewell.title("неет....")
    farewell.overrideredirect(True)
    farewell.geometry("400x200")
    farewell.resizable(False, False)
    farewell.update_idletasks()
    w = farewell.winfo_width()
    h = farewell.winfo_height()
    x = (farewell.winfo_screenwidth() - w) // 2
    y = (farewell.winfo_screenheight() - h) // 2
    farewell.geometry(f"+{x}+{y}")

    frame = ttk.Frame(farewell, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    msg = ttk.Label(frame, text="Ты отказался от абобы...\nАбоба покидает тебя.", font=("Arial", 12, "bold"), justify='center')
    msg.pack(expand=True, pady=20)
    farewell.after(2000, lambda: sys.exit(0))

    farewell.mainloop()

if __name__ == '__main__':
    welcome = WelcomeWindow()
    welcome.window.mainloop()