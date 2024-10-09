l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]


def f1():
    while True:
        v = int(input('chand geram mikhay?\n'))
        g1 = int(input('chand geram etiopi arabika?\n'))
        g2 = int(input('chand geram goatmala arabika\n'))
        g3 = int(input('chand geram brezil arabika\n'))
        g4 = int(input('chand geram colombia arabika\n'))
        g5 = int(input('chand geram andonezi robosta\n'))
        g6 = int(input('chand geram vietnam robosta\n'))
        if v != (g1 + g2 + g3 + g4 + g5 + g6):
            print('majmooe nemikhoone, mojaddad begoo')
        else:
            print('tashakkor\n')
            break
        
    x = g1*c[0] + g2*c[1] + g3*c[2] + g4*c[3] + g5*c[4] + g6*c[5]
    print(f'gheymate nahaii {x} tooman hast')
        
    y = [g1, g2, g3, g4, g5, g6]
    for i in range(6):
        if y[i] != 0:
            print(f'{y[i]} geram {l[i]}')


def f2():
    while True:
        v = int(input('chand geram mikhay?\n'))
        g1 = int(input('chand darsad etiopi arabika?\n'))
        g2 = int(input('chand darsad goatmala arabika\n'))
        g3 = int(input('chand darsad brezil arabika\n'))
        g4 = int(input('chand darsad colombia arabika\n'))
        g5 = int(input('chand darsad andonezi robosta\n'))
        g6 = int(input('chand darsad vietnam robosta\n'))
        if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
            print('majmooe nemikhoone, mojaddad begoo')
        else:
            print('tashakkor\n')
            break
        
    x = (g1*c[0] + g2*c[1] + g3*c[2] + g4*c[3] + g5*c[4] + g6*c[5])*v/100
    print(f'gheymate nahaii {x} tooman hast')

    y = [g1, g2, g3, g4, g5, g6]
    for i in range(6):
        if y[i] != 0:
            print(f'{y[i]*v/100} geram {l[i]}')


def f3():
    while True:
        v = int(input('chand tooman mikhay?\n'))
        g1 = int(input('chand tooman etiopi arabika?\n'))
        g2 = int(input('chand tooman goatmala arabika\n'))
        g3 = int(input('chand tooman brezil arabika\n'))
        g4 = int(input('chand tooman colombia arabika\n'))
        g5 = int(input('chand tooman andonezi robosta\n'))
        g6 = int(input('chand tooman vietnam robosta\n'))
        if v != (g1 + g2 + g3 + g4 + g5 + g6):
            print('majmooe nemikhoone, mojaddad begoo')
        else:
            print('tashakkor\n')
            break
        
    x = (g1/c[0] + g2/c[1] + g3/c[2] + g4/c[3] + g5/c[4] + g6/c[5])*1000
    print(f'vazne nahaii {x} geram hast')

    y = [g1, g2, g3, g4, g5, g6]
    for i in range(6):
        if y[i] != 0:
            print(f'{y[i]*1000/c[i]} geram {l[i]}')


def f4():
    while True:
        v = int(input('chand tooman mikhay?\n'))
        g1 = int(input('chand darsad etiopi arabika?\n'))
        g2 = int(input('chand darsad goatmala arabika\n'))
        g3 = int(input('chand darsad brezil arabika\n'))
        g4 = int(input('chand darsad colombia arabika\n'))
        g5 = int(input('chand darsad andonezi robosta\n'))
        g6 = int(input('chand darsad vietnam robosta\n'))
        if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
            print('majmooe nemikhoone, mojaddad begoo')
        else:
            print('tashakkor\n')
            break
        
    x = (g1/c[0] + g2/c[1] + g3/c[2] + g4/c[3] + g5/c[4] + g6/c[5])*v*10
    print(f'vazne nahaii {x} geram hast')

    y = [g1, g2, g3, g4, g5, g6]
    for i in range(6):
        if y[i] != 0:
            print(f'{y[i]*v*10/c[i]} geram {l[i]}')

def f5():
    a = int(input('geram(1) ya tooman(2)?\n'))
    if a==1:
        b = int(input('geram(1) ya darsad(2)?\n'))
        if b == 1:
            f1()
        else:
            f2()
    else:
        b = int(input('tooman(1) ya darsad(2)?\n'))
        if b == 1:
            f3()
        else:
            f4()
f5()

#######################################################


l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

def get_inputs(is_percentage=False):
    v = int(input('meghdar ra vared konid (geram ya tooman):\n'))
    weights = []
    for i in l:
        prompt = f'chand {"darsad" if is_percentage else "geram"} {i}?\n'
        weights.append(int(input(prompt)))
    return v, weights

def calculate_total(v, weights, is_percentage, is_cost):
    if is_percentage:
        weights = [w * v / 100 for w in weights]
    if is_cost:
        total_weight = sum([w / p for w, p in zip(weights, c)]) * 1000
        print(f'vazne nahaii {total_weight} geram hast')
    else:
        total_price = sum([w * p for w, p in zip(weights, c)])
        print(f'gheymate nahaii {total_price} tooman hast')

    for w, coffee in zip(weights, l):
        if w != 0:
            print(f'{w:.2f} geram {coffee}')

def f5():
    a = int(input('geram(1) ya tooman(2)?\n'))
    is_cost = (a == 2)
    b = int(input('geram(1) ya darsad(2)?\n'))
    is_percentage = (b == 2)
    v, weights = get_inputs(is_percentage)
    calculate_total(v, weights, is_percentage, is_cost)

f5()


#################################################

import tkinter as tk
from tkinter import messagebox

# داده‌های مربوط به انواع قهوه و قیمت آنها
l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

# تابع برای بررسی ورودی‌ها و انجام محاسبات بر اساس سناریوهای مختلف
def calculate():
    try:
        v = int(entry_total.get())  # مقدار ورودی کل قهوه یا مبلغ
        g1 = int(entry_g1.get())
        g2 = int(entry_g2.get())
        g3 = int(entry_g3.get())
        g4 = int(entry_g4.get())
        g5 = int(entry_g5.get())
        g6 = int(entry_g6.get())
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:  # اگر به صورت مستقیم گرم برای هر قهوه وارد شود
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌های وارد شده برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:  # اگر درصد هر قهوه وارد شود
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:  # اگر به صورت مستقیم پول برای هر قهوه وارد شود
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌های وارد شده برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:  # اگر درصد هر قهوه وارد شود
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفا مقادیر معتبر وارد کنید!')

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی‌ها برای قهوه‌های مختلف
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

labels = ['اتیوپی عربیکا', 'گواتمالا عربیکا', 'برزیل عربیکا', 'کلمبیا عربیکا', 'اندونزی روبوستا', 'ویتنام روبوستا']
entries = []

for i in range(6):
    tk.Label(root, text=f'{labels[i]}:').pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# اجرای برنامه
root.mainloop()


##########################################################

import tkinter as tk
from tkinter import messagebox, simpledialog

# لیست اولیه قهوه‌ها و قیمت‌ها
l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

# تابع برای محاسبات مختلف
def calculate():
    try:
        v = int(entry_total.get())
        g1 = int(entry_g1.get())
        g2 = int(entry_g2.get())
        g3 = int(entry_g3.get())
        g4 = int(entry_g4.get())
        g5 = int(entry_g5.get())
        g6 = int(entry_g6.get())
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

# تابع برای اضافه کردن قهوه جدید
def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

# تابع برای حذف قهوه موجود
def remove_coffee():
    coffee_to_remove = simpledialog.askstring("حذف قهوه", "نام قهوه‌ای که می‌خواهید حذف کنید را وارد کنید:")
    if coffee_to_remove in l:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")
    else:
        messagebox.showerror("خطا", "قهوه مورد نظر پیدا نشد!")

# تابع برای به‌روزرسانی فیلدهای ورودی قهوه
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]}:').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی مجموع
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# فریم برای ورودی‌های قهوه
coffee_frame = tk.Frame(root)
coffee_frame.pack()

# فیلدهای ورودی برای قهوه‌ها
entries = []
update_coffee_entries()

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# منوی تنظیمات برای افزودن و حذف قهوه
menu = tk.Menu(root)
root.config(menu=menu)
settings_menu = tk.Menu(menu)
menu.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)

# اجرای برنامه
root.mainloop()

##########################################################

import tkinter as tk
from tkinter import messagebox, simpledialog

# لیست اولیه قهوه‌ها و قیمت‌ها
l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

# تابع برای محاسبات مختلف
def calculate():
    try:
        v = int(entry_total.get() or 0)  # اگر فیلد خالی بود مقدار صفر در نظر بگیرد
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

# تابع برای اضافه کردن قهوه جدید
def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

# تابع برای حذف قهوه موجود
def remove_coffee():
    coffee_to_remove = simpledialog.askstring("حذف قهوه", "نام قهوه‌ای که می‌خواهید حذف کنید را وارد کنید:")
    if coffee_to_remove in l:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")
    else:
        messagebox.showerror("خطا", "قهوه مورد نظر پیدا نشد!")

# تابع برای تغییر قیمت قهوه موجود
def update_price():
    coffee_to_update = simpledialog.askstring("تغییر قیمت", "نام قهوه‌ای که می‌خواهید قیمتش را تغییر دهید وارد کنید:")
    if coffee_to_update in l:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")
    else:
        messagebox.showerror("خطا", "قهوه مورد نظر پیدا نشد!")

# تابع برای به‌روزرسانی فیلدهای ورودی قهوه
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]}:').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی مجموع
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# فریم برای ورودی‌های قهوه
coffee_frame = tk.Frame(root)
coffee_frame.pack()

# فیلدهای ورودی برای قهوه‌ها
entries = []
update_coffee_entries()

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# منوی تنظیمات برای افزودن، حذف و تغییر قیمت قهوه
menu = tk.Menu(root)
root.config(menu=menu)
settings_menu = tk.Menu(menu)
menu.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

# اجرای برنامه
root.mainloop()


#########################

import tkinter as tk
from tkinter import messagebox, simpledialog

# لیست اولیه قهوه‌ها و قیمت‌ها
l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

# تابع برای محاسبات مختلف
def calculate():
    try:
        v = int(entry_total.get() or 0)  # اگر فیلد خالی بود مقدار صفر در نظر بگیرد
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

# تابع برای اضافه کردن قهوه جدید
def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            update_coffee_options()
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

# تابع برای حذف قهوه موجود
def remove_coffee():
    coffee_to_remove = selected_coffee.get()
    if coffee_to_remove in l:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        update_coffee_options()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")
    else:
        messagebox.showerror("خطا", "قهوه مورد نظر پیدا نشد!")

# تابع برای تغییر قیمت قهوه موجود
def update_price():
    coffee_to_update = selected_coffee.get()
    if coffee_to_update in l:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")
    else:
        messagebox.showerror("خطا", "قهوه مورد نظر پیدا نشد!")

# تابع برای به‌روزرسانی فیلدهای ورودی قهوه
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]}:').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# تابع برای به‌روزرسانی منوی انتخاب قهوه‌ها
def update_coffee_options():
    menu_coffee['menu'].delete(0, 'end')
    for coffee in l:
        menu_coffee['menu'].add_command(label=coffee, command=tk._setit(selected_coffee, coffee))

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی مجموع
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# فریم برای ورودی‌های قهوه
coffee_frame = tk.Frame(root)
coffee_frame.pack()

# فیلدهای ورودی برای قهوه‌ها
entries = []
update_coffee_entries()

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# منوی کشویی برای انتخاب قهوه
selected_coffee = tk.StringVar(root)
selected_coffee.set(l[0])  # قهوه پیش‌فرض
menu_coffee = tk.OptionMenu(root, selected_coffee, *l)
menu_coffee.pack()

# منوی تنظیمات برای افزودن، حذف و تغییر قیمت قهوه
menu = tk.Menu(root)
root.config(menu=menu)
settings_menu = tk.Menu(menu)
menu.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

# به‌روزرسانی منوی قهوه‌ها
update_coffee_options()

# اجرای برنامه
root.mainloop()
##################################@@@@###@@##

import tkinter as tk
from tkinter import messagebox, simpledialog

# لیست اولیه قهوه‌ها و قیمت‌ها
l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
c = [1195, 840, 680, 640, 550, 495]

# تابع برای محاسبات مختلف
def calculate():
    try:
        v = int(entry_total.get() or 0)  # اگر فیلد خالی بود مقدار صفر در نظر بگیرد
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

# تابع برای اضافه کردن قهوه جدید
def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

# تابع برای حذف قهوه موجود
def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

# تابع برای تغییر قیمت قهوه موجود
def update_price():
    coffee_to_update = select_from_list("تغییر قیمت قهوه", "قهوه‌ای را برای تغییر قیمت انتخاب کنید:", l)
    if coffee_to_update:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")

# تابع برای انتخاب از لیست
def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])  # مقدار پیش‌فرض
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()  # منتظر بمانید تا کاربر انتخاب خود را انجام دهد
    return selected_option.get()

# تابع برای به‌روزرسانی فیلدهای ورودی قهوه
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]}:').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی مجموع
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# فریم برای ورودی‌های قهوه
coffee_frame = tk.Frame(root)
coffee_frame.pack()

# فیلدهای ورودی برای قهوه‌ها
entries = []
update_coffee_entries()

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# منوی تنظیمات برای افزودن، حذف و تغییر قیمت قهوه
menu = tk.Menu(root)
root.config(menu=menu)
settings_menu = tk.Menu(menu)
menu.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

# اجرای برنامه
root.mainloop()

########################

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# لیست اولیه قهوه‌ها و قیمت‌ها
def load_data():
    global l, c
    try:
        with open('coffee_data.json', 'r') as f:
            data = json.load(f)
            l = data['names']
            c = data['prices']
    except FileNotFoundError:
        # اگر فایل وجود ندارد، داده‌های پیش‌فرض را تنظیم کن
        l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 'andonezi robosta', 'vietnam robosta']
        c = [1195, 840, 680, 640, 550, 495]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

# بارگذاری داده‌ها در ابتدای برنامه
load_data()

# تابع برای محاسبات مختلف
def calculate():
    try:
        v = int(entry_total.get() or 0)  # اگر فیلد خالی بود مقدار صفر در نظر بگیرد
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:  # اگر ورودی به صورت گرم باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] + g5 * c[4] + g6 * c[5]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  # اگر ورودی به صورت تومان باشد
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] + g5 / c[4] + g6 / c[5]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

# تابع برای اضافه کردن قهوه جدید
def add_coffee():
    new_coffee = simpledialog.askstring("افزودن قهوه", "نام قهوه جدید را وارد کنید:")
    if new_coffee:
        new_price = simpledialog.askinteger("قیمت قهوه", f"قیمت {new_coffee} به تومان:")
        if new_price:
            l.append(new_coffee)
            c.append(new_price)
            update_coffee_entries()
            save_data()  # ذخیره داده‌ها پس از افزودن قهوه
            messagebox.showinfo("موفقیت", f"{new_coffee} با قیمت {new_price} تومان اضافه شد.")

# تابع برای حذف قهوه موجود
def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()  # ذخیره داده‌ها پس از حذف قهوه
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

# تابع برای تغییر قیمت قهوه موجود
def update_price():
    coffee_to_update = select_from_list("تغییر قیمت قهوه", "قهوه‌ای را برای تغییر قیمت انتخاب کنید:", l)
    if coffee_to_update:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            save_data()  # ذخیره داده‌ها پس از تغییر قیمت قهوه
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")

# تابع برای انتخاب از لیست
def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])  # مقدار پیش‌فرض
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()  # منتظر بمانید تا کاربر انتخاب خود را انجام دهد
    return selected_option.get()

# تابع برای به‌روزرسانی فیلدهای ورودی قهوه
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]}:').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6 = entries

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

# انتخاب نوع ورودی (وزن یا تومان)
var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

# انتخاب حالت (مقدار یا درصد)
var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

# ورودی مجموع
tk.Label(root, text="مجموع گرم/تومان:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# فریم برای ورودی‌های قهوه
coffee_frame = tk.Frame(root)
coffee_frame.pack()

# فیلدهای ورودی برای قهوه‌ها
entries = []
update_coffee_entries()

# دکمه محاسبه
tk.Button(root, text="محاسبه", command=calculate).pack()

# منوی تنظیمات برای افزودن، حذف و تغییر قیمت قهوه
menu = tk.Menu(root)
root.config(menu=menu)
settings_menu = tk.Menu(menu)
menu.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

# اجرای حلقه
root.mainloop()
#################################

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

def load_data():
    global l, c
    try:
        with open('coffee_data.json', 'r') as f:
            data = json.load(f)
            l = data['names']
            c = data['prices']
    except FileNotFoundError:
        l = ['etiopi arabika', 'goatmala arabika', 'brezil arabika', 'colombia arabika', 
             'andonezi robosta', 'vietnam robosta', '50,50', '70,30']
        c = [1195, 840, 680, 640, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

def calculate():
    try:
        v = int(entry_total.get() or 0)
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        g7 = int(entry_g7.get() or 0)
        g8 = int(entry_g8.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] +
                                   g5 * c[4] + g6 * c[5] + g7 * c[6] + g8 * c[7])
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] +
                                   g5 * c[4] + g6 * c[5] + g7 * c[6] + g8 * c[7]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] +
                                    g5 / c[4] + g6 / c[5] + g7 / c[6] + g8 / c[7]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] +
                                    g5 / c[4] + g6 / c[5] + g7 / c[6] + g8 / c[7]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

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

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

def update_price():
    coffee_to_update = select_from_list("تغییر قیمت قهوه", "قهوه‌ای را برای تغییر قیمت انتخاب کنید:", l)
    if coffee_to_update:
        new_price = simpledialog.askinteger("قیمت جدید", f"قیمت جدید برای {coffee_to_update} به تومان:")
        if new_price:
            index = l.index(coffee_to_update)
            c[index] = new_price
            update_coffee_entries()  # به‌روزرسانی لیست قهوه‌ها
            save_data()
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').pack()  # نمایش قیمت در پرانتز
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6, entry_g7, entry_g8
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6, entry_g7, entry_g8 = entries

root = tk.Tk()
root.title("محاسبه ترکیب قهوه")

var_unit = tk.IntVar()
tk.Label(root, text="ورودی به صورت:").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text="نوع وارد کردن:").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text="مقدار کل:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).pack()
tk.Button(root, text="افزودن قهوه", command=add_coffee).pack()
tk.Button(root, text="حذف قهوه", command=remove_coffee).pack()
tk.Button(root, text="تغییر قیمت قهوه", command=update_price).pack()

root.mainloop()
####################################################

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

def load_data():
    global l, c
    try:
        with open('coffee_data.json', 'r') as f:
            data = json.load(f)
            l = data['names']
            c = data['prices']
    except FileNotFoundError:
        l = ['اتیوپی عربیکا', 'گواتمالا عربیکا', 'کلمبیا عربیکا', 'برزیل عربیکا'
                 , 'اندونزی روبوستا', 'ویتنام روبوستا', '۵۰|۵۰', '۷۰|۳۰']            
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

def calculate():
    try:
        v = int(entry_total.get() or 0)
        g1 = int(entry_g1.get() or 0)
        g2 = int(entry_g2.get() or 0)
        g3 = int(entry_g3.get() or 0)
        g4 = int(entry_g4.get() or 0)
        g5 = int(entry_g5.get() or 0)
        g6 = int(entry_g6.get() or 0)
        g7 = int(entry_g7.get() or 0)
        g8 = int(entry_g8.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()

        if unit == 1:
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] +
                                   g5 * c[4] + g6 * c[5] + g7 * c[6] + g8 * c[7])
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = (g1 * c[0] + g2 * c[1] + g3 * c[2] + g4 * c[3] +
                                   g5 * c[4] + g6 * c[5] + g7 * c[6] + g8 * c[7]) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:
            if mode == 1:
                if v != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] +
                                    g5 / c[4] + g6 / c[5] + g7 / c[6] + g8 / c[7]) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2:
                if 100 != (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8):
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = (g1 / c[0] + g2 / c[1] + g3 / c[2] + g4 / c[3] +
                                    g5 / c[4] + g6 / c[5] + g7 / c[6] + g8 / c[7]) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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
            update_coffee_entries()  # به‌روزرسانی لیست قهوه‌ها
            save_data()
            messagebox.showinfo("موفقیت", f"قیمت {coffee_to_update} به {new_price} تومان تغییر یافت.")

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f':{l[i]} ({c[i]} تومان)').pack()  # نمایش قیمت در پرانتز
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)
    
    global entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6, entry_g7, entry_g8
    entry_g1, entry_g2, entry_g3, entry_g4, entry_g5, entry_g6, entry_g7, entry_g8 = entries

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text=":مقدار کل").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).pack()
tk.Button(root, text="افزودن قهوه", command=add_coffee).pack()
tk.Button(root, text="حذف قهوه", command=remove_coffee).pack()
tk.Button(root, text="تغییر قیمت قهوه", command=update_price).pack()

root.mainloop()
####################################################3

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

def load_data():
    global l, c
    try:
        with open('coffee_data.json', 'r') as f:
            data = json.load(f)
            l = data['names']
            c = data['prices']
    except FileNotFoundError:
        l = ['اتیوپی عربیکا', 'گواتمالا عربیکا', 'کلمبیا عربیکا', 'برزیل عربیکا', 
             'اندونزی روبوستا', 'ویتنام روبوستا', '۵۰|۵۰', '۷۰|۳۰']            
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

def calculate():
    try:
        v = int(entry_total.get() or 0)
        mode = var_mode.get()
        unit = var_unit.get()
        g = [int(entries[i].get() or 0) for i in range(len(l))]
        
        if unit == 1: 
            if mode == 1: 
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع گرم‌ها برابر با مقدار کل نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l)))
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    messagebox.showinfo('نتیجه', f'قیمت نهایی: {total_price} تومان')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    total_weight = sum(g[i] / c[i] for i in range(len(l))) * 1000
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_weight = sum(g[i] / c[i] for i in range(len(l))) * v * 10
                    messagebox.showinfo('نتیجه', f'وزن نهایی: {total_weight} گرم')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text=":مقدار کل").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).pack()
tk.Button(root, text="افزودن قهوه", command=add_coffee).pack()
tk.Button(root, text="حذف قهوه", command=remove_coffee).pack()
tk.Button(root, text="تغییر قیمت قهوه", command=update_price).pack()

root.mainloop()
#####################################
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text=":مقدار کل").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).pack()
tk.Button(root, text="افزودن قهوه", command=add_coffee).pack()
tk.Button(root, text="حذف قهوه", command=remove_coffee).pack()
tk.Button(root, text="تغییر قیمت قهوه", command=update_price).pack()

root.mainloop()
#####################################

import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')
def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text=":مقدار کل").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

# ایجاد باکس تنظیمات
settings_frame = tk.Frame(root, bd=2, relief="sunken")
settings_frame.pack(pady=10)

tk.Label(settings_frame, text="تنظیمات قهوه‌ها").pack()

tk.Button(settings_frame, text="افزودن قهوه", command=add_coffee).pack(pady=5)
tk.Button(settings_frame, text="حذف قهوه", command=remove_coffee).pack(pady=5)
tk.Button(settings_frame, text="تغییر قیمت قهوه", command=update_price).pack(pady=5)

tk.Button(root, text="محاسبه", command=calculate).pack()

root.mainloop()
##############%######%#%#%##%
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').pack()
        entry = tk.Entry(coffee_frame)
        entry.pack()
        entries.append(entry)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

# ایجاد منوی کشویی
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).pack()

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).pack()

tk.Label(root, text=":مقدار کل").pack()
entry_total = tk.Entry(root)
entry_total.pack()

coffee_frame = tk.Frame(root)
coffee_frame.pack()

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).pack()

root.mainloop()
######################3
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):', font=('Arial', 12), fg='#333').pack(pady=2)
        entry = tk.Entry(coffee_frame, font=('Arial', 12), bg='#e0e0e0')
        entry.pack(pady=2)
        entries.append(entry)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    selection_window.geometry('300x150')
    selection_window.configure(bg='#f7f7f7')
    
    tk.Label(selection_window, text=prompt, font=('Arial', 12), bg='#f7f7f7').pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection, bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.geometry('400x600')
root.configure(bg='#f7f7f7')

# Heading
tk.Label(root, text="محاسبه قیمت قهوه", font=('Arial', 16, 'bold'), bg='#f7f7f7', fg='#333').pack(pady=10)

# Input type selection
var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", font=('Arial', 12), bg='#f7f7f7').pack()
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, font=('Arial', 12), bg='#f7f7f7').pack()
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, font=('Arial', 12), bg='#f7f7f7').pack()

# Mode selection
var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", font=('Arial', 12), bg='#f7f7f7').pack()
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, font=('Arial', 12), bg='#f7f7f7').pack()
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, font=('Arial', 12), bg='#f7f7f7').pack()

# Total input
tk.Label(root, text=":مقدار کل", font=('Arial', 12), bg='#f7f7f7').pack(pady=5)
entry_total = tk.Entry(root, font=('Arial', 12), bg='#e0e0e0')
entry_total.pack(pady=5)

# Coffee list frame
coffee_frame = tk.Frame(root, bg='#f7f7f7')
coffee_frame.pack(pady=10)

update_coffee_entries()

# Buttons
tk.Button(root, text="محاسبه", command=calculate, bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)

# Settings Menu
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("تنظیمات")
    settings_window.geometry('300x200')
    settings_window.configure(bg='#f7f7f7')
    
    tk.Button(settings_window, text="افزودن قهوه", command=add_coffee, bg='#2196F3', fg='white', font=('Arial', 12)).pack(pady=10)
    tk.Button(settings_window, text="حذف قهوه", command=remove_coffee, bg='#F44336', fg='white', font=('Arial', 12)).pack(pady=10)
root.mainloop()
################$$$$$$$$$$$$$$$$$
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):').grid(row=i, column=0, sticky="w")
        entry = tk.Entry(coffee_frame)
        entry.grid(row=i, column=1, sticky="we")
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack()
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack()

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack()
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")

# ایجاد منوی کشویی
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت").grid(row=0, column=0, sticky="w")
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1).grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2).grid(row=1, column=1, sticky="w")

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن").grid(row=2, column=0, sticky="w")
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1).grid(row=3, column=0, sticky="w")
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2).grid(row=3, column=1, sticky="w")

tk.Label(root, text=":مقدار کل").grid(row=4, column=0, sticky="w")
entry_total = tk.Entry(root)
entry_total.grid(row=4, column=1, sticky="we")

coffee_frame = tk.Frame(root)
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate).grid(row=6, column=0, columnspan=2, pady=10)

# تنظیمات واکنش‌گرایی
root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)

root.mainloop()

##############################
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        label = tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):', bg="#F0E5CF", font=("Arial", 12))
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(coffee_frame, font=("Arial", 12))
        entry.grid(row=i, column=1, sticky="we", padx=10, pady=5)
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack(pady=10)
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.configure(bg="#EAE7DC")

# ایجاد منوی کشویی
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", bg="#EAE7DC", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, bg="#EAE7DC", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10)
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, bg="#EAE7DC", font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=10)

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", bg="#EAE7DC", font=("Arial", 14)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, bg="#EAE7DC", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10)
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, bg="#EAE7DC", font=("Arial", 12)).grid(row=3, column=1, sticky="w", padx=10)

tk.Label(root, text=":مقدار کل", bg="#EAE7DC", font=("Arial", 14)).grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_total = tk.Entry(root, font=("Arial", 12))
entry_total.grid(row=4, column=1, sticky="we", padx=10)

coffee_frame = tk.Frame(root, bg="#EAE7DC")
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate, bg="#D8C3A5", font=("Arial", 12)).grid()
root.mainloop()

####################
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        label = tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):', bg="#F0E5CF", font=("Arial", 12), anchor="e")
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(coffee_frame, font=("Arial", 12), justify="right")
        entry.grid(row=i, column=1, sticky="we", padx=10, pady=5)
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt, justify="right").pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack(pady=10)
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.configure(bg="#EAE7DC")

# ایجاد منوی کشویی
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", bg="#EAE7DC", font=("Arial", 14), anchor="e").grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=1, column=0, sticky="e", padx=10)
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=1, column=1, sticky="e", padx=10)

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", bg="#EAE7DC", font=("Arial", 14), anchor="e").grid(row=2, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=3, column=0, sticky="e", padx=10)
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=3, column=1, sticky="e", padx=10)

tk.Label(root, text=":مقدار کل", bg="#EAE7DC", font=("Arial", 14), anchor="e").grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_total = tk.Entry(root, font=("Arial", 12))
entry_total.grid(row=4, column=1, sticky="we", padx=10)

coffee_frame = tk.Frame(root, bg="#EAE7DC")
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate, bg="#D8C3A5", font=("Arial", 12), anchor="e").grid()
root.mainloop()

#################################3

import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {g[i]} گرم\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v} تومان\n {s}')

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        label = tk.Label(coffee_frame, text=f'{l[i]} ({c[i]} تومان):', bg="#F0E5CF", font=("Arial", 12), anchor="e")
        label.grid(row=i, column=0, sticky="e", padx=10, pady=5)
        entry = tk.Entry(coffee_frame, font=("Arial", 12), justify="right")
        entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt, justify="right").pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack(pady=10)
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.configure(bg="#EAE7DC")

# ایجاد منوی کشویی
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", bg="#EAE7DC", font=("Arial", 14), anchor="e").grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=1, column=0, sticky="e", padx=10)
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=1, column=1, sticky="e", padx=10)

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", bg="#EAE7DC", font=("Arial", 14), anchor="e").grid(row=2, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=3, column=0, sticky="e", padx=10)
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, bg="#EAE7DC", font=("Arial", 12), anchor="e").grid(row=3, column=1, sticky="e", padx=10)

tk.Label(root, text=":مقدار کل", bg="#EAE7DC", font=("Arial", 14)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_total = tk.Entry(root, font=("Arial", 12))
entry_total.grid(row=4, column=1, sticky="we", padx=10)

coffee_frame = tk.Frame(root, bg="#EAE7DC")
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

tk.Button(root, text="محاسبه", command=calculate, bg="#D8C3A5", font=("Arial", 12)).grid()
root.mainloop()
#########################
import json
from math import ceil
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        c = [1195, 840, 840, 680, 550, 495, 670, 620]

def save_data():
    data = {'names': l, 'prices': c}
    with open('coffee_data.json', 'w') as f:
        json.dump(data, f)

load_data()

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
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price_formatted} تومان\n {s}')
            elif mode == 2:  
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    total_price = sum(g[i] * c[i] for i in range(len(l))) * v / 100
                    total_price_formatted = "{:,}".format(int(total_price)) 
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]*v/100)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {total_price_formatted} تومان\n {s}')

        elif unit == 2:  
            if mode == 1:  
                if v != sum(g):
                    messagebox.showerror('خطا', 'مجموع مبلغ‌ها برابر با مقدار کل نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*1000)} گرم ({g[i]} تومان)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v:,} تومان\n {s}')  
            elif mode == 2: 
                if sum(g) != 100:
                    messagebox.showerror('خطا', 'مجموع درصدها برابر با 100 نیست!')
                else:
                    for i in range(len(g)):
                        if g[i] != 0:
                            s += f'{l[i]}:  {ceil(g[i]/c[i]*v*10)} گرم ({g[i]} درصد)\n'
                    messagebox.showinfo('نتیجه', f'قیمت نهایی:  {v:,} تومان\n {s}')  

    except ValueError:
        messagebox.showerror('خطا', 'لطفاً مقادیر معتبر وارد کنید!')

def update_coffee_entries():
    for widget in coffee_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []
    for i in range(len(l)):
        label = tk.Label(coffee_frame, text=f':{l[i]} ({c[i]} تومان)', bg="#F9E5CF", font=("Arial", 14))
        label.grid(row=i, column=1, sticky="e", padx=10, pady=5)
        entry = tk.Entry(coffee_frame, font=("Arial", 12))
        entry.grid(row=i, column=0, sticky="we", padx=10, pady=5)
        entries.append(entry)

    coffee_frame.columnconfigure(1, weight=1)

def remove_coffee():
    coffee_to_remove = select_from_list("حذف قهوه", "قهوه‌ای را برای حذف انتخاب کنید:", l)
    if coffee_to_remove:
        index = l.index(coffee_to_remove)
        l.pop(index)
        c.pop(index)
        update_coffee_entries()
        save_data()
        messagebox.showinfo("موفقیت", f"{coffee_to_remove} حذف شد.")

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

def select_from_list(title, prompt, options):
    selection_window = tk.Toplevel(root)
    selection_window.title(title)
    
    tk.Label(selection_window, text=prompt).pack(pady=10)
    
    selected_option = tk.StringVar(selection_window)
    selected_option.set(options[0])
    
    dropdown = tk.OptionMenu(selection_window, selected_option, *options)
    dropdown.pack(pady=10)

    def confirm_selection():
        selection_window.destroy()

    tk.Button(selection_window, text="انتخاب", command=confirm_selection).pack(pady=10)
    
    selection_window.wait_window()
    return selected_option.get()

root = tk.Tk()
root.title("محاسبه قیمت کافه محمد")
root.configure(bg="#EAE7DC")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="تنظیمات", menu=settings_menu)
settings_menu.add_command(label="حذف قهوه", command=remove_coffee)
settings_menu.add_command(label="افزودن قهوه", command=add_coffee)
settings_menu.add_command(label="تغییر قیمت قهوه", command=update_price)

var_unit = tk.IntVar()
tk.Label(root, text=":ورودی به صورت", bg="#eed5bd", font=("Arial", 14)).grid(row=0, column=1, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="گرم", variable=var_unit, value=1, bg="#EAE7DC", font=("Arial", 12)).grid(row=1, column=1, sticky="e", padx=10)
tk.Radiobutton(root, text="تومان", variable=var_unit, value=2, bg="#EAE7DC", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10)

var_mode = tk.IntVar()
tk.Label(root, text=":نوع وارد کردن", bg="#eed5bd", font=("Arial", 14)).grid(row=2, column=1, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="مقدار", variable=var_mode, value=1, bg="#EAE7DC", font=("Arial", 12)).grid(row=3, column=1, sticky="e", padx=10)
tk.Radiobutton(root, text="درصد", variable=var_mode, value=2, bg="#EAE7DC", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=10)

tk.Label(root, text=":مقدار کل", bg="#eed5bd", font=("Arial", 15)).grid(row=4, column=1, sticky="e", padx=10, pady=20)
entry_total = tk.Entry(root, font=("Arial", 12))
entry_total.grid(row=4, column=0, sticky="we", padx=10)

coffee_frame = tk.Frame(root, bg="#EAE7DC")
coffee_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

update_coffee_entries()

calculate_button = tk.Button(root, text="محاسبه", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), activebackground="#45a049", padx=20, pady=10)
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)
def on_enter(e):
    calculate_button['background'] = '#3e8e41'

def on_leave(e):
    calculate_button['background'] = '#4CAF50'

calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

root.mainloop()
###############












