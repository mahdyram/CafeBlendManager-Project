import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3  
import datetime 


r = "#EAE7DC"
v = r

def load_data():
    global l, c
    try:
        with open('coffee_data.json', 'r') as f:
            data = json.load(f)
            l = data['names']
            c = data['prices']
    except FileNotFoundError:
        l = ['اتیوپی عربیکا', 'گواتمالا عربیکا', 'کلمبیا عربیکا', 'برزیل عربیکا',
             'اندونزی روبوستا', 'ویتنام روبوستا', 'پنجاه پنجاه', 'هفتاد سی']
        c = [1195, 840, 840, 680, 550, 495, 670, 590]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

def init_db():
    conn = sqlite3.connect('coffee_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history 
                      (id INTEGER PRIMARY KEY, date TEXT, result TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(result):
    conn = sqlite3.connect('coffee_history.db')
    cursor = conn.cursor()
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO history (date, result) VALUES (?, ?)", (date_time, result))
    conn.commit()
    conn.close()

def ask_to_save(result):
    save = messagebox.askyesno('ذخیره‌سازی', 'آیا می‌خواهید این ترکیب را در تاریخچه ذخیره کنید؟')
    if save:
        save_to_db(result)

def show_history():
    conn = sqlite3.connect('coffee_history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY date DESC")
    records = cursor.fetchall()
    conn.close()

    history_window = tk.Toplevel(root)
    history_window.title("تاریخچه محاسبات")
    history_window.geometry("300x500")

    canvas = tk.Canvas(history_window)
    scrollbar = tk.Scrollbar(history_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if records:
        for record in records:
            tk.Label(scrollable_frame, text=f"تاریخ: {record[1]}\nنتیجه: {record[2]}", bg=r, font=("Arial", 12), anchor="w", justify="left").pack(padx=10, pady=5, fill="x")
    else:
        tk.Label(scrollable_frame, text="تاریخچه‌ای وجود ندارد!", bg=r, font=("Arial", 14), anchor="w").pack(padx=10, pady=5)

init_db()
def calculate():
    try:
        v = int(entry_total.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()
        g = [int(entries[i].get() or 0) for i in range(len(l))]
        s = ''
        
        if unit == 1: 
            if mode == 1: 
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l)))
                    total_price_formatted = "{:,}".format(total_price)
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    result = f'قیمت نهایی: {total_price_formatted} تومان\n{s}'
                    messagebox.showinfo('نتیجه', result)
                    ask_to_save(result)
            elif mode == 2:
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    total_price_formatted = "{:,}".format(int(total_price))
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    result = f'قیمت نهایی: {total_price_formatted} تومان\n{s}'
                    messagebox.showinfo('نتیجه', result)
                    ask_to_save(result)

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    result = f'قیمت نهایی: {v:,} تومان\n{s}'
                    messagebox.showinfo('نتیجه', result)
                    ask_to_save(result)
            elif mode == 2: 
                if sum(g) != 100:messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    result = f'قیمت نهایی: {v:,} تومان\n{s}'
                    messagebox.showinfo('نتیجه', result)
                    ask_to_save(result)

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        label = tk.Label(coffee_frame, text=f':{l[i]} ({c[i]} تومان)', bg=r, font=("Mitra", 13))
        label.grid(row=i, column=1, sticky="e", padx=10, pady=5)
        entry = tk.Entry(coffee_frame, font=("Arial", 12))
        entry.grid(row=i, column=0, sticky="we", padx=10, pady=5)
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    
    if not coffee_to_remove:
        messagebox.showinfo("لغو شد", "حذف قهوه لغو شد.")
        return
    confirm = messagebox.askyesno("تایید حذف", f"آیا مطمئن هستید که می‌خواهید '{coffee_to_remove}' را حذف کنید؟")
    
    if confirm:
        if coffee_to_remove in l:
            index = l.index(coffee_to_remove)
            l.pop(index)
            c.pop(index)
            save_data()  
            update_coffee_entries()  
            messagebox.showinfo("حذف شد", f"قهوه '{coffee_to_remove}' با موفقیت حذف شد.")
        else:
            messagebox.showerror("خطا", f"قهوه '{coffee_to_remove}' پیدا نشد.")
    else:
        messagebox.showinfo("لغو شد", "حذف قهوه لغو شد.")

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set('لیست قهوه ها')  
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    def cancel_selection():
        selected_option.set('')  
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack(side="left", padx=10, pady=10)
    
    tk.Button(selection_window, text="لغو", command=cancel_selection).pack(side="right", padx=10, pady=10)

    selection_window.protocol("WM_DELETE_WINDOW", cancel_selection)  

    selection_window.wait_window()
    return selected_option.get()  

def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            save_data()
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

def update_price():
    coffee_to_update = select_from_list("تغییر قیمت قهوه", "قهوه‌ای را برای تغییر قیمت انتخاب کنید:", l)
    if coffee_to_update:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            update_coffee_entries()
            save_data()
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("درباره برنامه")
    about_window.configure(bg=r)

    tk.Label(
        about_window,
        text="درباره برنامه",
        font=("Mitra", 17, "bold"),
        bg=r
    ).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(
        about_window,
        text=".این برنامه برای محاسبه ترکیبات مختلف قهوه برای خام فروشی قهوه طراحی شده است\n"
             ".از امکانات این برنامه میتوان به ثبت تاریخچه، حذف، افزودن و یا تغییر قیمت قهوه های فعلی اشاره کرد",            
        font=("Mitra", 12),
        bg=r,
        justify="right"
    ).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="e")

    tk.Label(
        about_window,
        text=":نسخه \n1.0.0\n\n"
     ":سازنده \nمهدی رامشینی"             
             "\nmahdi ramshini\n\n"  
               ":ایمیل \nmahdyramshini@Gmail.com\n"             
     ":تلگرام \nhttps://t.me/mahdi_ramshini\n"             
        ":گیتهاب \nhttps://github.com/mahdyram\n"             
        , 
        font=("Mitra", 12),
        bg=r,
        justify="right"
    ).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.configure(bg=r)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="درباره", command=show_about)
settings_menu.add_command(label="تاریخچه", command=show_history)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", bg=v, font=("Mitra", 13)).grid(row=0, column=1, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, bg=r, cursor="hand2", font=("Mitra", 11)).grid(row=1, column=1, sticky="e", padx=10)
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, bg=r, cursor="hand2", font=("Mitra", 11)).grid(row=1, column=0, sticky="e", padx=10)

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", bg=v, font=("Mitra", 13)).grid(row=2, column=1, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, bg=r, cursor="hand2", font=("Mitra", 11)).grid(row=3, column=1, sticky="e", padx=10)
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, bg=r, cursor="hand2", font=("Mitra", 11)).grid(row=3, column=0, sticky="e", padx=10)

tk.Label(root, text=":مقدار کل", bg=v, font=("Bnazanin", 16)).grid(row=4, column=1, sticky="e", padx=10, pady=20)
entry_total = tk.Entry(root, font=("Arial", 12))
entry_total.grid(row=4, column=0, sticky="we", padx=10)

coffee_frame = tk.Frame(root, bg=r)
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

calculate_button = tk.Button(root, text="محاسبه", command=calculate, bg="#4CAF50", fg="white", font=("Mitra", 14, "bold"), activebackground="#45a049", padx=20, pady=3)
calculate_button.grid(row=7, column=0, columnspan=2, pady=15)
def on_enter(e):
    calculate_button['background'] = '#3e8e41'

def on_leave(e):
    calculate_button['background'] = '#4CAF50'

calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

root.mainloop()