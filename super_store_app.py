
from Smartphone import Smartphone
from Laptop import Laptop
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validitors import *

store = SuperStore(products_cvs='products_supply', clients_csv='clients', shirts_csv='shirts', orders_csv='orders')
window = Tk()
window.title("SuperStore")
window.geometry("1000x700")
current_row = 0


lbl = Label(window, text="Products", font=("Bernard MT Condensed", 20), fg="pink")
lbl.grid(row=current_row, column=3)
current_row += 2

w=Label(window, text="WELCOME TO \n Super Store App", font=("Bernard MT Condensed", 15), fg="black")
w.grid(row=current_row-2, column=0)


prod_combo = ttk.Combobox(window, values=("All products", "Laptops", "Smartphone", "Shirts"))
prod_combo.grid(row=current_row+1, column=1)
current_row += 1


def handel_display():
    prod_list.delete(0, END)  # clear listbox
    prod = prod_combo.get()
    if prod== "All products":
        for p in store.product_list:
            prod_list.insert(END, str(p))
    if prod == "Laptops":
        for p in store.product_list:
            if type(p)== Laptop:
                prod_list.insert(END, str(p))
    if prod == "Smartphone":
        for p in store.product_list:
            if type(p) == Smartphone:
                prod_list.insert(END, str(p))
    if prod == "Shirts":
        for p in store.get_all_shirt():
            prod_list.insert(END, str(p))



book_btn = Button(window, text="Display products", width=15, height=1, fg="red",command=handel_display)
book_btn.grid(row=current_row, column=2)


prod_list = Listbox(window, width=60)
prod_list.grid(row=current_row,column=3)
current_row += 1

lbl = Label(window, text="Add New Product", font=("Bernard MT Condensed", 15), fg="pink")
lbl.grid(row=10, column=1)

status_lbl = Label(window, text="", fg="red")
status_lbl.grid(row=11, column=1)


id_lbl = Label(window, text="id")
id_lbl.grid(row=12, column=1)
id_lbl = Entry(window,width=20)
id_lbl.grid(row=13, column=1)
id_lbl.focus()

price_lbl = Label(window, text="price")
price_lbl.grid(row=12, column=2)
price_lbl = Entry(window,width=20)
price_lbl.grid(row=13, column=2)
price_lbl.focus()

brand_lbl = Label(window, text="brand")
brand_lbl.grid(row=14, column=1)
brand_lbl = Entry(window,width=20)
brand_lbl.grid(row=15, column=1)
brand_lbl.focus()

model_lbl = Label(window, text="model")
model_lbl.grid(row=14, column=2)
model_lbl = Entry(window,width=20)
model_lbl.grid(row=15, column=2)
model_lbl.focus()

year_lbl = Label(window, text="year")
year_lbl.grid(row=16, column=1)
year_lbl = ttk.Combobox(window, values=(list(range(1970, 2024))))
year_lbl.grid(row=17, column=1)
current_row=15

types_var = IntVar()

def handel_laptop_or_smartphone():
    if types_var.get() == 1:
        cpu_lbl.configure(state=NORMAL)
        disk_lbl.configure(state=NORMAL)
        screen_lbl.configure(state=NORMAL)
        cel_lbl.configure(state=DISABLED)
        cores_lbl.configure(state=DISABLED)
        camRes_lbl.configure(state=DISABLED)
    else:
        cpu_lbl.configure(state=DISABLED)
        disk_lbl.configure(state=DISABLED)
        screen_lbl.configure(state=DISABLED)
        cel_lbl.configure(state=NORMAL)
        cores_lbl.configure(state=NORMAL)
        camRes_lbl.configure(state=NORMAL)

types_var = IntVar()
r1 = Radiobutton(window,text="Laptop",variable=types_var, value=1,command=handel_laptop_or_smartphone)
r1.grid(column=1, row=19)


cpu_lbl = Label(window, text="CPU")
cpu_lbl.grid(row=18, column=2)
cpu_lbl = Entry(window,width=20)
cpu_lbl.grid(row=19, column=2)
cpu_lbl.focus()

disk_lbl = Label(window, text="Hard disk")
disk_lbl.grid(row=18, column=3)
disk_lbl = Entry(window,width=20)
disk_lbl.grid(row=19, column=3)
disk_lbl.focus()

screen_lbl = Label(window, text="Screen")
screen_lbl.grid(row=18, column=4)
screen_lbl = Entry(window,width=20)
screen_lbl.grid(row=19, column=4)
screen_lbl.focus()

r2 = Radiobutton(window,text="Smartphone",variable=types_var, value=2,command=handel_laptop_or_smartphone)
r2.grid(sticky=W, column=1, row=21)

cel_lbl = Label(window, text="Cellular Network")
cel_lbl.grid(row=20, column=2)
cel_lbl = Entry(window,width=20)
cel_lbl.grid(row=21, column=2)
cel_lbl.focus()

cores_lbl = Label(window, text="Number of cores")
cores_lbl.grid(row=20, column=3)
cores_lbl = Entry(window,width=20)
cores_lbl.grid(row=21, column=3)
cores_lbl.focus()

camRes_lbl = Label(window, text="Camera resulution")
camRes_lbl.grid(row=20, column=4)
camRes_lbl = Entry(window,width=20)
camRes_lbl.grid(row=21, column=4)
camRes_lbl.focus()


def is_empty_Laptop():
    validNotEmpty1 = True
    if types_var.get() == 1:
        if len(id_lbl.get()) == 0:
            validNotEmpty1 = False
            id_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Id"))
        elif len(model_lbl.get()) == 0:
            validNotEmpty1 = False
            model_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Model"))
        elif len(brand_lbl.get()) == 0:
            validNotEmpty1 = False
            brand_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Brand"))
        elif len(price_lbl.get()) == 0:
            validNotEmpty1 = False
            price_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Price"))
        elif len(year_lbl.get()) == 0:
            validNotEmpty1 = False
            status_lbl.configure(text=str("select Year"))
        elif len(cpu_lbl.get()) == 0:
            validNotEmpty1 = False
            cpu_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert CPU"))
        elif len(disk_lbl.get()) == 0:
            validNotEmpty1 = False
            disk_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Hard Disk"))
        elif len(screen_lbl.get()) == 0:
            validNotEmpty1 = False
            screen_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Screen"))


        return validNotEmpty1


def is_empty_Phone():
    validNotEmpty2 = True

    if types_var.get() == 2:
        if len(id_lbl.get()) == 0:
            validNotEmpty2 = False
            id_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Id"))
        elif len(model_lbl.get()) == 0:
            validNotEmpty2 = False
            model_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Model"))
        elif len(brand_lbl.get()) == 0:
            validNotEmpty2 = False
            brand_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Brand"))
        elif len(price_lbl.get()) == 0:
            validNotEmpty2 = False
            price_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert Price"))
        elif len(year_lbl.get()) == 0:
            validNotEmpty2 = False
            status_lbl.configure(text=str("select Year"))
        elif len(cel_lbl.get()) == 0:
            validNotEmpty2 = False
            cel_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert cellular network"))
        elif len(cores_lbl.get()) == 0:
            validNotEmpty2 = False
            cores_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert num cores"))
        elif len(camRes_lbl.get()) == 0:
            validNotEmpty2 = False
            camRes_lbl.config(bg="RED")
            status_lbl.configure(text=str("insert camera resolution"))

        return validNotEmpty2


def handel_display():
    product_id = id_lbl.get()
    brand = brand_lbl.get()
    model = model_lbl.get()
    year = year_lbl.get()
    price = price_lbl.get()
    id_lbl.config(bg="WHITE")
    brand_lbl.config(bg="WHITE")
    model_lbl.config(bg="WHITE")
    price_lbl.config(bg="WHITE")
    cpu_lbl.config(bg="WHITE")
    disk_lbl.config(bg="WHITE")
    screen_lbl.config(bg="WHITE")
    cel_lbl.config(bg="WHITE")
    cores_lbl.config(bg="WHITE")
    camRes_lbl.config(bg="WHITE")

    if types_var.get() == 1:
        CPU=cpu_lbl.get()
        hard_disk=disk_lbl.get()
        screen=screen_lbl.get()
        if is_empty_Laptop()==False:
            is_empty_Laptop()
            cpu_lbl.delete(0, END)
            disk_lbl.delete(0, END)
            screen_lbl.delete(0, END)
            cel_lbl.delete(0, END)
            cores_lbl.delete(0, END)
            camRes_lbl.delete(0, END)
            id_lbl.delete(0, END)
            brand_lbl.delete(0, END)
            model_lbl.delete(0, END)
            year_lbl.delete(0, END)
            price_lbl.delete(0, END)
        else:

            try:
                new_prod1 = Laptop(product_id, brand, model, year, price, CPU, hard_disk, screen)
                valid1=True
                status_int_id1=True



            except IDvalueError as e:
                valid1 = False
                status_int_id1=False
                print(f"{e}\nenter valid product id! try again")
                status_lbl.configure(text=str("ID not int"))
            except PricevalueError as e:
                valid1 = False
                print(f"{e}\nenter valid price! try again")
                id_lbl.config(bg="WHITE")
                status_lbl.configure(text=str("Price not int"))
            except HardDiskError as e:
                valid1 = False
                print(f"{e}\nenter valid Hard Disk! try again")
                status_lbl.configure(text=str("Hard Disk not int"))
            except ScreenError as e:
                valid1=False
                print(f"{e}\nenter valid Screen! try again")
                status_lbl.configure(text=str("Screen not int"))



            if status_int_id1 == True:

                try:
                    validate_ID(int(product_id))
                    valid1 = True


                except IDNotFoundError:
                    valid1=False
                    status_lbl.configure(text=str("Id exists"))



            if valid1 == False:
                cpu_lbl.delete(0, END)
                disk_lbl.delete(0, END)
                screen_lbl.delete(0, END)
                cel_lbl.delete(0, END)
                cores_lbl.delete(0, END)
                camRes_lbl.delete(0, END)
                id_lbl.delete(0, END)
                brand_lbl.delete(0, END)
                model_lbl.delete(0, END)
                year_lbl.delete(0, END)
                price_lbl.delete(0, END)


            if valid1==True and is_empty_Laptop()==True:
                store.__iadd__(new_prod1)
                messagebox.showinfo(message=f"New product created!\n {new_prod1}")
                status_lbl.configure(text="")
                cpu_lbl.delete(0, END)
                disk_lbl.delete(0, END)
                screen_lbl.delete(0, END)
                cel_lbl.delete(0, END)
                cores_lbl.delete(0, END)
                camRes_lbl.delete(0, END)
                id_lbl.delete(0, END)
                brand_lbl.delete(0, END)
                model_lbl.delete(0, END)
                year_lbl.delete(0, END)
                price_lbl.delete(0, END)

    if types_var.get() == 2:
        cell_net = cel_lbl.get()
        num_cores = cores_lbl.get()
        cam_res = camRes_lbl.get()
        id_lbl.config(bg="WHITE")
        brand_lbl.config(bg="WHITE")
        model_lbl.config(bg="WHITE")
        price_lbl.config(bg="WHITE")
        cpu_lbl.config(bg="WHITE")
        disk_lbl.config(bg="WHITE")
        screen_lbl.config(bg="WHITE")
        cel_lbl.config(bg="WHITE")
        cores_lbl.config(bg="WHITE")
        camRes_lbl.config(bg="WHITE")
        if is_empty_Phone()==False:
            is_empty_Phone()
            cpu_lbl.delete(0, END)
            disk_lbl.delete(0, END)
            screen_lbl.delete(0, END)
            cel_lbl.delete(0, END)
            cores_lbl.delete(0, END)
            camRes_lbl.delete(0, END)
            id_lbl.delete(0, END)
            brand_lbl.delete(0, END)
            model_lbl.delete(0, END)
            year_lbl.delete(0, END)
            price_lbl.delete(0, END)
        else:
            try:
                new_prod2 = Smartphone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)
                valid2 = True
                status_int_id2 = True

            except IDvalueError as e:
                valid2 = False
                status_int_id2 = False
                print(f"{e}\nenter valid product id! try again")
                status_lbl.configure(text=str("ID not int"))
            except PricevalueError as e:
                valid2 = False
                print(f"{e}\nenter valid price! try again")
                status_lbl.configure(text=str("Price not int"))
            except NumCError as e:
                valid2 = False
                print(f"{e}\nenter valid Num Cores! try again")
                status_lbl.configure(text=str("Num Cores not int"))
            except CamRError as e:
                valid2 = False
                print(f"{e}\nenter valid Camera Resolution! try again")
                status_lbl.configure(text=str("Camera Resolution not int"))

            if status_int_id2 == True:
                try:
                    validate_ID(int(product_id))
                    valid2 = True
                except IDNotFoundError:
                    valid2=False
                    status_lbl.configure(text=str("Id exists"))



            if valid2==False :
                cpu_lbl.delete(0, END)
                disk_lbl.delete(0, END)
                screen_lbl.delete(0, END)
                cel_lbl.delete(0, END)
                cores_lbl.delete(0, END)
                camRes_lbl.delete(0, END)
                id_lbl.delete(0, END)
                brand_lbl.delete(0, END)
                model_lbl.delete(0, END)
                year_lbl.delete(0, END)
                price_lbl.delete(0, END)

            if valid2==True :
                store.__iadd__(new_prod2)
                messagebox.showinfo(message=f"New product created!\n {new_prod2}")
                status_lbl.configure(text="")
                cpu_lbl.delete(0, END)
                disk_lbl.delete(0, END)
                screen_lbl.delete(0, END)
                cel_lbl.delete(0, END)
                cores_lbl.delete(0, END)
                camRes_lbl.delete(0, END)
                id_lbl.delete(0, END)
                brand_lbl.delete(0, END)
                model_lbl.delete(0, END)
                year_lbl.delete(0, END)
                price_lbl.delete(0, END)


book_btn = Button(window, text="create", width=10, height=2, command=handel_display)
book_btn.grid(row=25, column=0)

def handel_search():
    s=search_lbl.get()
    if store.get_product(int(s)) is not None:
        a=store.get_product(int(s))
        messagebox.showinfo(message=f"the product is: \n {a}")
    else:
        messagebox.showinfo(message=f"the product dont exists")
    search_lbl.delete(0, END)


Search = Label(window, text="Search By ID- Enter ID", font=("Bernard MT Condensed", 15), fg="pink")
Search.grid(row=29, column=3)
search_lbl = Entry(window,width=15)
search_lbl.grid(row=30, column=3)
search_lbl.focus()
Search_btn = Button(window, text="Search laptop/smartphone/shirts", width=28, height=2, command=handel_search)
Search_btn.grid(row=31, column=3)

window.mainloop()
