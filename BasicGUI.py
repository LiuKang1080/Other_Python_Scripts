import tkinter
import os

# create the main window in tkinter, called the master window. Remember that not all objects in tkinter have a children, but all objects in tkinter have a parent object, except the master.
master = tkinter.Tk()
master.title = 'Advanced GUI Demo'
# the name of the main window. Now we will define the size of thw size of the window
master.geometry('1200x720')
# Here argument can also be in the form '1200x720-N1-N2' these last two numbers are offsets

# Define a label (Which parent window it's going to be in, text= what the text will say). we define where it is in the parent window
label = tkinter.Label(master, text='TKinter Grid Demo')
label.grid(row=0, column=1, columnspan=3)

# Configure each column:
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)
master.columnconfigure(2, weight=3)
master.columnconfigure(3, weight=3)
master.columnconfigure(4, weight=3)

# Now configure the rows:
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=10)
master.rowconfigure(2, weight=1)
master.rowconfigure(3, weight=3)
master.rowconfigure(4, weight=3)
# Here the weight determines how objects move when resizing the window.

# We will now create an object the file list, then we will map all file names in the windows folder directory into the list. we will then create a scroll bar, and then map that scroll bar to the list.
fileList = tkinter.Listbox(master)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.configure(border=2, relief='sunken')

# Now we will populate the list with the folder names with the Windows folder directory.\
for file in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, file)
# Here we are inserting at the END after each insertion.

# Now we will add the scroll bar and attach the function to the list.
listScroll = tkinter.Scrollbar(master, orient=tkinter.VERTICAL, command=fileList.yview)
# no argument provided for the yview, we are orientating it vertically, we can do it horizontally if we wanted to. now to actually place it since we created it.
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set


# Now we will make radio buttons, we will place them into an optional frame:
optionFrame = tkinter.Label(master, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)
# Set which radio button is highlighted by defualt.

# Now actually naming the radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='File Name', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='File Path ', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Time Stamp', value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


# Adding an entry widget:
resultLabel = tkinter.Label(master, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')

result = tkinter.Entry(master)
result.grid(row=2, column=2, sticky='new')


# Frame for the time spinners:
timeFrame = tkinter.LabelFrame(master, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

# Adding the time spinners:
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)

minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)

secondSpinner.grid(row=0, column=4)
# Here we are placing spaces in between the hour spinner and the minute spinner same between minute and seconds.

timeFrame ['padx'] = 36
# Padding within the time frame box.

# Frame for the Date Spinners:
dateFrame = tkinter.Frame(master)
dateFrame.grid(row=4, column=0, sticky='new')

#Date labels:
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Actual spinners for the dates:
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=1900, to=2100)

daySpin.grid(row=1, column=0, sticky='new')
monthSpin.grid(row=1, column=1, sticky='new')
yearSpin.grid(row=1, column=2, sticky='new')






















master.mainloop()

