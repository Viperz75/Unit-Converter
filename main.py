from tkinter import *
from tkinter import messagebox
import webbrowser

# Window/Widget
window = Tk()
window.title("Unit Converter")


def length():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    # Developer Tag
    company_name = Label(file_new_frame, text="Length Converter", font=("MV Boli", 15, "bold"))
    company_name.pack()

    # Choice Options
    my_label = Label(file_new_frame, text="Choose a Unit")
    my_label.pack()
    choices = ['Inch', 'Centimeter', 'Feet', 'Meter', 'Yard', 'Miles', 'Km', 'Nautical Mile', 'Parsec']

    variable = StringVar()
    variable.set("")
    w = OptionMenu(file_new_frame, variable, *choices)
    w.pack()

    # Creating Entry
    creating_entry = Entry(file_new_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry.pack()
    my_label = Label(file_new_frame, text="Convert to")
    my_label.pack()
    to = StringVar()
    w = OptionMenu(file_new_frame, to, *choices)
    w.pack()

    # Converter Function
    def converter():
        convert = variable.get()
        convert_to = to.get()
        num = float(creating_entry.get())

        # Inch To Cm & Cm to Inch
        if convert == 'Inch' and convert_to == 'Centimeter':
            converted_num = num * 2.54
        elif convert == 'Centimeter' and convert_to == 'Inch':
            converted_num = num / 2.54
        # Feet to Meter
        elif convert == 'Feet' and convert_to == 'Meter':
            converted_num = num / 3.281
        elif convert == 'Meter' and convert_to == 'Feet':
            converted_num = num * 3.281
        # Yard to Meter and Meter To Yard
        elif convert == 'Yard' and convert_to == 'Meter':
            converted_num = num / 1.094
        elif convert == 'Meter' and convert_to == 'Yard':
            converted_num = num * 1.094
        # Miles to Km and Km To Miles
        elif convert == 'Miles' and convert_to == 'Km':
            converted_num = num * 1.609
        elif convert == 'Km' and convert_to == 'Miles':
            converted_num = num / 1.609
        # N Mile to Meter and Meter to N Mile
        elif convert == 'Nautical Mile' and convert_to == 'Meter':
            converted_num = num * 1852
        elif convert == 'Meter' and convert_to == 'Nautical Mile':
            converted_num = num / 1852
        # Pc to Km and Km to Pc
        elif convert == 'Parsec' and convert_to == 'Km':
            converted_num = num * 3.086e+13
        elif convert == 'Km' and convert_to == 'Parsec':
            converted_num = num / 3.086e+13
        # Feet to Inch and Inch to Feet
        elif convert == 'Feet' and convert_to == 'Inch':
            converted_num = num * 12
        elif convert == 'Inch' and convert_to == 'Feet':
            converted_num = num / 12
        # Feet to Yard and Yard to Feet
        elif convert == 'Feet' and convert_to == 'Yard':
            converted_num = num / 3
        elif convert == 'Yard' and convert_to == 'Feet':
            converted_num = num * 3
        # Feet to Cm and Cm to Feet
        elif convert == 'Feet' and convert_to == 'Centimeter':
            converted_num = num * 30.48
        elif convert == 'Centimeter' and convert_to == 'Feet':
            converted_num = num / 30.48
        # Cm to Meter and Meter to Cm
        elif convert == 'Centimeter' and convert_to == 'Meter':
            converted_num = num / 100
        elif convert == 'Meter' and convert_to == 'Centimeter':
            converted_num = num * 100
        # Meter to Km and Km to Meter
        elif convert == 'Meter' and convert_to == 'Km':
            converted_num = num / 1000
        elif convert == 'Km' and convert_to == 'Meter':
            converted_num = num * 1000
        # Feet to Meter and Meter to Feet
        elif convert == 'Feet' and convert_to == 'Meter':
            converted_num = num / 3.2808399
        elif convert == 'Meter' and convert_to == 'Feet':
            converted_num = num * 3.2808399
        else:
            converted_num = num

        result_label.config(text=f"{converted_num} {convert_to}")

    # Calculate Button
    calculate = Button(file_new_frame, text='Calculate', command=converter, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(file_new_frame, text="0")
    result_label.pack()


def area():
    hide_all_frames()
    file_another_frame.pack(fill="both", expand=1)
    # Developer Tag
    company = Label(file_another_frame, text="Area Converter", font=("MV Boli", 15, "bold"))
    company.pack()

    # Choice Options
    label = Label(file_another_frame, text="Choose a Unit")
    label.pack()
    choices2 = ['Acre', 'Square Meter', 'Square Kilometer', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch',
                'Hectare', 'Shotangsho', 'Katha', 'Bigha']

    variable2 = StringVar()
    variable2.set("")
    w = OptionMenu(file_another_frame, variable2, *choices2)
    w.pack()

    # Creating Entry
    creating_entry2 = Entry(file_another_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry2.pack()
    my_label = Label(file_another_frame, text="Convert to")
    my_label.pack()
    to2 = StringVar()
    w2 = OptionMenu(file_another_frame, to2, *choices2)
    w2.pack()

    def converter2():
        convert = variable2.get()
        convert_to = to2.get()
        num = float(creating_entry2.get())

        # Acre to Square Meter and Meter to Acre
        if convert == 'Acre' and convert_to == 'Square Meter':
            converted_num2 = num * 4047
        elif convert == 'Square Meter' and convert_to == 'Acre':
            converted_num2 = num / 4047
        # Square Meter to Square Kilometer and Square Kilometer to Square Meter
        elif convert == 'Square Meter' and convert_to == 'Square Kilometer':
            converted_num2 = num / 1e+6
        elif convert == 'Square Kilometer' and convert_to == 'Square Meter':
            converted_num2 = num * 1000000
        # Square Mile to Square Yard and Square Yard to Square Mile
        elif convert == 'Square Mile' and convert_to == 'Square Yard':
            converted_num2 = num * 3097600
        elif convert == 'Square Yard' and convert_to == 'Square Mile':
            converted_num2 = num / 3.0976E+6
        # Square Feet to Square Inch and Square Inch to Square Feet
        elif convert == 'Square Foot' and convert_to == 'Square Inch':
            converted_num2 = num * 144
        elif convert == 'Square Inch' and convert_to == 'Square Foot':
            converted_num2 = num / 144
        # Hectare to Acre and Acre to Hectare
        elif convert == 'Hectare' and convert_to == 'Acre':
            converted_num2 = num * 2.47105381
        elif convert == 'Acre' and convert_to == 'Hectare':
            converted_num2 = num / 2.47105381
        # Shotangsho to Square Foot and Square Foot to Shotangsho
        elif convert == 'Shotangsho' and convert_to == 'Square Foot':
            converted_num2 = num * 435.6
        elif convert == 'Square Foot' and convert_to == 'Shotangsho':
            converted_num2 = num / 435.6
        # Shotangsho to Katha and Katha to Shotangsho
        elif convert == 'Shotangsho' and convert_to == 'Katha':
            converted_num2 = num * 0.605
        elif convert == 'Katha' and convert_to == 'Shotangsho':
            converted_num2 = num / 0.605
        # Shotangsho to Bigha and Bigha to Shotangsho
        elif convert == 'Shotangsho' and convert_to == 'Bigha':
            converted_num2 = num * 0.03025
        elif convert == 'Bigha' and convert_to == 'Shotangsho':
            converted_num2 = num / 0.03025
        else:
            converted_num2 = num

        result_label.config(text=f"{converted_num2} {convert_to}")

    # Calculate Button
    calculate = Button(file_another_frame, text='Calculate', command=converter2, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(file_another_frame, text="0")
    result_label.pack()


def mass():
    hide_all_frames()
    mass_frame.pack(fill="both", expand=1)
    # Developer Tag
    company = Label(mass_frame, text="Mass Converter", font=("MV Boli", 15, "bold"))
    company.pack()

    # Choice Options
    label = Label(mass_frame, text="Choose a Unit")
    label.pack()
    choices2 = ['Tons', 'Pound', 'Kilogram', 'Grams', 'Milligrams', 'Ounce']

    variable2 = StringVar()
    variable2.set("")
    w = OptionMenu(mass_frame, variable2, *choices2)
    w.pack()

    # Creating Entry
    creating_entry2 = Entry(mass_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry2.pack()
    my_label = Label(mass_frame, text="Convert to")
    my_label.pack()
    to2 = StringVar()
    w2 = OptionMenu(mass_frame, to2, *choices2)
    w2.pack()

    def converter2():
        convert = variable2.get()
        convert_to = to2.get()
        num = float(creating_entry2.get())

        # Tons to Kilogram and Kilogram to Tons
        if convert == 'Tons' and convert_to == 'Kilogram':
            converted_num2 = num * 1016.04691
        elif convert == 'Kilogram' and convert_to == 'Tons':
            converted_num2 = num / 1016.04691
        # Pound to Tons and Tons to Pound
        elif convert == 'Pound' and convert_to == 'Tons':
            converted_num2 = num / 2240
        elif convert == 'Tons' and convert_to == 'Pound':
            converted_num2 = num * 2240
        # Pound to Kilogram and Kilogram to Pound
        elif convert == 'Pound' and convert_to == 'Kilogram':
            converted_num2 = num / 2.20462262
        elif convert == 'Kilogram' and convert_to == 'Pound':
            converted_num2 = num * 2.20462262
        # Kilogram to Grams and Grams to Kilogram
        elif convert == 'Kilogram' and convert_to == 'Grams':
            converted_num2 = num * 1000
        elif convert == 'Grams' and convert_to == 'Kilogram':
            converted_num2 = num / 1000
        # Grams to Milligrams and Milligrams to Grams
        elif convert == 'Grams' and convert_to == 'Milligrams':
            converted_num2 = num * 1000
        elif convert == 'Milligrams' and convert_to == 'Grams':
            converted_num2 = num / 1000
        # Ounce to Grams and Grams to Ounce
        elif convert == 'Ounce' and convert_to == 'Grams':
            converted_num2 = num * 28.3495231
        elif convert == 'Grams' and convert_to == 'Ounce':
            converted_num2 = num / 28.3495231
        else:
            converted_num2 = num

        result_label.config(text=f"{converted_num2} {convert_to}")

    # Calculate Button
    calculate = Button(mass_frame, text='Calculate', command=converter2, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(mass_frame, text="0")
    result_label.pack()


def volume():
    hide_all_frames()
    volume_frame.pack(fill="both", expand=1)
    # Developer Tag
    company = Label(volume_frame, text="Volume Converter", font=("MV Boli", 15, "bold"))
    company.pack()

    # Choice Options
    label = Label(volume_frame, text="Choose a Unit")
    label.pack()
    choices2 = ['Liter', 'Milliliter', 'Cubic Feet', 'Cubic Inch']

    variable2 = StringVar()
    variable2.set("")
    w = OptionMenu(volume_frame, variable2, *choices2)
    w.pack()

    # Creating Entry
    creating_entry2 = Entry(volume_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry2.pack()
    my_label = Label(volume_frame, text="Convert to")
    my_label.pack()
    to2 = StringVar()
    w2 = OptionMenu(volume_frame, to2, *choices2)
    w2.pack()

    def converter2():
        convert = variable2.get()
        convert_to = to2.get()
        num = float(creating_entry2.get())

        # Liter to Milliliter and Milliliter to Liter
        if convert == 'Liter' and convert_to == 'Milliliter':
            converted_num2 = num * 1000
        elif convert == 'Milliliter' and convert_to == 'Liter':
            converted_num2 = num / 1000
        #Cubic Foot to Cubic Inch and Cubic Inch to Cubic Feet
        elif convert == 'Cubic Foot' and convert_to == 'Cubic Inch':
            converted_num2 = num * 1728
        elif convert == 'Cubic Inch' and convert_to == 'Cubic Foot':
            converted_num2 = num / 1728

        else:
            converted_num2 = num

        result_label.config(text=f"{converted_num2} {convert_to}")

    # Calculate Button
    calculate = Button(volume_frame, text='Calculate', command=converter2, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(volume_frame, text="0")
    result_label.pack()


def data_storage():
    hide_all_frames()
    data_storage_frame.pack(fill="both", expand=1)
    # Developer Tag
    company = Label(data_storage_frame, text="Data Storage Converter", font=("MV Boli", 15, "bold"))
    company.pack()

    # Choice Options
    label = Label(data_storage_frame, text="Choose a Unit")
    label.pack()
    choices2 = ['Bytes', 'Kilobyte', 'Megabyte', 'Bits', 'Gigabyte', 'Petabyte', 'Pebibyte']

    variable2 = StringVar()
    variable2.set("")
    w = OptionMenu(data_storage_frame, variable2, *choices2)
    w.pack()

    # Creating Entry
    creating_entry2 = Entry(data_storage_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry2.pack()
    my_label = Label(data_storage_frame, text="Convert to")
    my_label.pack()
    to2 = StringVar()
    w2 = OptionMenu(data_storage_frame, to2, *choices2)
    w2.pack()

    def converter2():
        convert = variable2.get()
        convert_to = to2.get()
        num = float(creating_entry2.get())

        # Bytes to Kilobyte and Kilobyte to Bytes
        if convert == 'Bytes' and convert_to == 'Kilobyte':
            converted_num2 = num / 1000
        elif convert == 'Kilobyte' and convert_to == 'Bytes':
            converted_num2 = num * 1000
        #Kilobyte to Megabyte and Megabyte to Kilobyte
        elif convert == 'Kilobyte' and convert_to == 'Megabyte':
            converted_num2 = num / 1000
        elif convert == 'Megabyte' and convert_to == 'Kilobyte':
            converted_num2 = num * 1000
        #Bits to Bytes and Bytes to Bits
        elif convert == 'Bits' and convert_to == 'Bytes':
            converted_num2 = num / 8
        elif convert == 'Bytes' and convert_to == 'Bits':
            converted_num2 = num * 8
        #Megabyte to Gigabyte and Gigabyte to Megabyte
        elif convert == 'Megabyte' and convert_to == 'Gigabyte':
            converted_num2 = num / 1000
        elif convert == 'Gigabyte' and convert_to == 'Megabyte':
            converted_num2 = num * 1000
        #Gigabyte to Petabyte and Petabyte to Gigabyte
        elif convert == 'Gigabyte' and convert_to == 'Petabyte':
            converted_num2 = num / 1000000
        elif convert == 'Petabyte' and convert_to == 'Gigabyte':
            converted_num2 = num * 1000000
        #Petabyte to Pebibyte and Pebibyte to Petabyte
        elif convert == 'Petabyte' and convert_to == 'Pebibyte':
            converted_num2 = num / 1.12589991
        elif convert == 'Pebibyte' and convert_to == 'Petabyte':
            converted_num2 = num * 1.12589991
        #Megabyte to Petabyte and Petabyte to Megabyte
        elif convert == 'Megabyte' and convert_to == 'Petabyte':
            converted_num2 = num / 1.0000E+9
        elif convert == 'Petabyte' and convert_to == 'Megabyte':
            converted_num2 = num * 1.0000E+9
        else:
            converted_num2 = num

        result_label.config(text=f"{converted_num2} {convert_to}")

    # Calculate Button
    calculate = Button(data_storage_frame, text='Calculate', command=converter2, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(data_storage_frame, text="0")
    result_label.pack()


def time():
    hide_all_frames()
    time_frame.pack(fill="both", expand=1)
    # Developer Tag
    company = Label(time_frame, text="Time Converter", font=("MV Boli", 15, "bold"))
    company.pack()

    # Choice Options
    label = Label(time_frame, text="Choose a Unit")
    label.pack()
    choices2 = ['Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month',
                'Year', 'Decade', 'Century']

    variable2 = StringVar()
    variable2.set("")
    w = OptionMenu(time_frame, variable2, *choices2)
    w.pack()

    # Creating Entry
    creating_entry2 = Entry(time_frame, highlightthickness=0, font=("Times New Roman", 9, "normal"))
    creating_entry2.pack()
    my_label = Label(time_frame, text="Convert to")
    my_label.pack()
    to2 = StringVar()
    w2 = OptionMenu(time_frame, to2, *choices2)
    w2.pack()

    def converter2():
        convert = variable2.get()
        convert_to = to2.get()
        num = float(creating_entry2.get())

        # Nanosecond to Microsecond and Microsecond to Nanosecond
        if convert == 'Nanosecond' and convert_to == 'Microsecond':
            converted_num2 = num / 1000
        elif convert == 'Microsecond' and convert_to == 'Nanosecond':
            converted_num2 = num * 1000
        #Millisecond to Microsecond and Microsecond to Millisecond
        elif convert == 'Millisecond' and convert_to == 'Microsecond':
            converted_num2 = num * 1000
        elif convert == 'Microsecond' and convert_to == 'Millisecond':
            converted_num2 = num / 1000
        #Millisecond to Second and Second to Millisecond
        elif convert == 'Millisecond' and convert_to == 'Second':
            converted_num2 = num / 1000
        elif convert == 'Second' and convert_to == 'Millisecond':
            converted_num2 = num * 1000
        #Second to Minute and Minute to Second
        elif convert == 'Second' and convert_to == 'Minute':
            converted_num2 = num / 60
        elif convert == 'Minute' and convert_to == 'Second':
            converted_num2 = num * 60
        #Hour to Second and Second to Hour
        elif convert == 'Hour' and convert_to == 'Second':
            converted_num2 = num * 3600
        elif convert == 'Second' and convert_to == 'Hour':
            converted_num2 = num / 3600
        #Hour to Minute and Minute to Hour
        elif convert == 'Hour' and convert_to == 'Minute':
            converted_num2 = num * 60
        elif convert == 'Minute' and convert_to == 'Hour':
            converted_num2 = num / 60
        #Day to Second and Second to Day
        elif convert == 'Day' and convert_to == 'Second':
            converted_num2 = num * 86400
        elif convert == 'Second' and convert_to == 'Day':
            converted_num2 = num / 86400
        #Day to Hour and Hour to Day
        elif convert == 'Day' and convert_to == 'Hour':
            converted_num2 = num * 24
        elif convert == 'Hour' and convert_to == 'Day':
            converted_num2 = num / 24
        #Week to Second and Second to Week
        elif convert == 'Week' and convert_to == 'Second':
            converted_num2 = num * 604800
        elif convert == 'Second' and convert_to == 'Week':
            converted_num2 = num / 604800
        #Week to Hour and Hour to Week
        elif convert == 'Week' and convert_to == 'Hour':
            converted_num2 = num * 168
        elif convert == 'Hour' and convert_to == 'Week':
            converted_num2 = num / 168
        #Month to Week and Week to Month
        elif convert == 'Month' and convert_to == 'Week':
            converted_num2 = num * 4.3452381
        elif convert == 'Week' and convert_to == 'Month':
            converted_num2 = num / 4.3452381
        #Month to Hour and Hour to Month
        elif convert == 'Month' and convert_to == 'Hour':
            converted_num2 = num * 730
        elif convert == 'Hour' and convert_to == 'Month':
            converted_num2 = num / 730
        #Year to Month and Month to Year
        elif convert == 'Year' and convert_to == 'Month':
            converted_num2 = num * 12
        elif convert == 'Month' and convert_to == 'Year':
            converted_num2 = num / 12
        #Year to Week and Week to Year
        elif convert == 'Year' and convert_to == 'Week':
            converted_num2 = num * 52.1428571
        elif convert == 'Week' and convert_to == 'Year':
            converted_num2 = num / 52.1428571
        #Decade to year and Year to Decade
        elif convert == 'Decade' and convert_to == 'Year':
            converted_num2 = num * 10
        elif convert == 'Year' and convert_to == 'Decade':
            converted_num2 = num / 10
        #Decade to Week and Week to Decade
        elif convert == 'Decade' and convert_to == 'Week':
            converted_num2 = num * 521.428571
        elif convert == 'Week' and convert_to == 'Decade':
            converted_num2 = num / 521.428571
        #Century to Decade and Decade to Century
        elif convert == 'Century' and convert_to == 'Decade':
            converted_num2 = num * 10
        elif convert == 'Decade' and convert_to == 'Century':
            converted_num2 = num / 10
        #Century to Week and Week to Century
        elif convert == 'Century' and convert_to == 'Week':
            converted_num2 = num * 5214.28571
        elif convert == 'Week' and convert_to == 'Century':
            converted_num2 = num / 5214.28571
        else:
            converted_num2 = num

        result_label.config(text=f"{converted_num2} {convert_to}")

    # Calculate Button
    calculate = Button(time_frame, text='Calculate', command=converter2, highlightthickness=0)
    calculate.pack()

    # Result Label
    result_label = Label(time_frame, text="0")
    result_label.pack()


def developer_name():
    messagebox.showinfo(title="About", message="Developer: Niaz Mahmud Akash "
                                               "\nContributor: Jalish Mahmud Sujon "
                                               "\nGithub: https://github.com/Viperz75"
                                               "\n\nUnit Converter by Brother's Co.")


def faq():
    messagebox.showinfo(title="FAQ", message="Coming Soon!")


def back_function():
    webbrowser.open(url="https://github.com/Viperz75")


def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    for widget in file_another_frame.winfo_children():
        widget.destroy()
    for widget in mass_frame.winfo_children():
        widget.destroy()
    for widget in volume_frame.winfo_children():
        widget.destroy()
    for widget in data_storage_frame.winfo_children():
        widget.destroy()
    for widget in time_frame.winfo_children():
        widget.destroy()
    for widget in back_ground_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    file_another_frame.pack_forget()
    mass_frame.pack_forget()
    volume_frame.pack_forget()
    data_storage_frame.pack_forget()
    time_frame.pack_forget()
    back_ground_frame.pack_forget()


# Top Menu Bar
menu_bar = Menu(window)
unit_menu = Menu(menu_bar, tearoff=0)
unit_menu.add_command(label="Length", command=length)
unit_menu.add_command(label="Area", command=area)
unit_menu.add_command(label="Mass", command=mass)
unit_menu.add_command(label="Volume", command=volume)
unit_menu.add_command(label="Data Storage", command=data_storage)
unit_menu.add_command(label="Time", command=time)
unit_menu.add_separator()
unit_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="Units", menu=unit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=developer_name)
help_menu.add_command(label="FAQ", command=faq)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(padx=30, pady=20, menu=menu_bar, bg="#FFFFFF")

# Creating New Frame
back_ground_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
file_new_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
file_another_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
mass_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
volume_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
data_storage_frame = Frame(window, width=30, height=30, bg="#FFFFFF")
time_frame = Frame(window, width=30, height=30, bg="#FFFFFF")


#Background Design
hide_all_frames()
COLOR = "#FFFFFF"
back_ground_label = Label(back_ground_frame, text="Brother's Co. Converter", font=("Algerian", 15, "normal"), bg=COLOR)
window.minsize(width=30, height=200)
back_ground_frame.pack(fill="both", expand=1)
back_ground_label.grid(row=0, column=0)

#Background Buttons
length_img = PhotoImage(file="length.png")
area_img = PhotoImage(file="area.png")
mass_img = PhotoImage(file="mass.png")
volume_img = PhotoImage(file="volume.png")
data_img = PhotoImage(file="data.png")
time_img = PhotoImage(file="time.png")
back_img = PhotoImage(file="icons.png")
window.iconbitmap("converter_icon.ico")

length_button = Button(back_ground_frame, image=length_img, command=length, highlightthickness=0, border=0)
area_button = Button(back_ground_frame, image=area_img, command=area, highlightthickness=0, border=0)
mass_button = Button(back_ground_frame, image=mass_img, command=mass, highlightthickness=0, border=0)
volume_button = Button(back_ground_frame, image=volume_img, command=volume, highlightthickness=0, border=0)
data_storage_button = Button(back_ground_frame, image=data_img, command=data_storage, highlightthickness=0, border=0)
time_button = Button(back_ground_frame, image=time_img, command=time, highlightthickness=0, border=0)
back = Button(back_ground_frame, highlightthickness=0, border=0, image=back_img, command=back_function)


length_button.place(x=10, y=40)
area_button.place(x=10, y=75)
mass_button.place(x=10, y=110)
volume_button.place(x=220, y=40)
data_storage_button.place(x=220, y=75)
time_button.place(x=220, y=110)
back.place(x=100, y=55)


window.mainloop()
