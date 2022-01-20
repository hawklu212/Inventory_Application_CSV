from tkinter import *
from tkinter import ttk
import csvCode


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("1265x590+0+0")
        self.root.configure(background='blue')
        self.productVar=StringVar()
        self.productVal=StringVar()
        self.prodName=StringVar()
        self.listVar=StringVar()
        self.statusvar=StringVar()
        self.createvaloption=StringVar()
        self.creatvalsuboption=StringVar()
        self.csvres=StringVar()
        self.groceries=['',"Fruits","Vegetables"]
        self.tech=['',"Laptop","Phones"]
        self.listoptions=['', 'All', 'Grocery', 'Tech',]
        self.initlist= "Products          Price           Quantity\n"

        def productOptions(event):
            base = self.initlist
            if self.productVar.get() == 'Grocery':
                self.productComboBox['value']=self.groceries
            elif self.productVar.get() == 'Tech':
                self.productComboBox['value']=self.tech
            elif self.productVar.get() =='All':
                self.productComboBox['value'] = ['']
            else:
                self.productComboBox['value']=['']
            self.productComboBox.current(0)
            self.listVar.set(csvCode.readCSV('test.csv',base, self.productVar.get()))

        def prodsubOptions(event):
            self.listVar.set(csvCode.readCSV('test.csv',self.initlist, self.productVal.get()))

        def createOptions(event):
            if self.createvaloption.get() == 'Grocery':
                self.createCombosubBox['value']=self.groceries
            elif self.createvaloption.get() == 'Tech':
                self.createCombosubBox['value']=self.tech
            else:
                self.createCombosubBox['value']=['']
            self.createCombosubBox.current(0)

        def creatButtonFunction(event):
            result = csvCode.createcsventry('test.csv',self.createvaloption.get(),self.creatvalsuboption.get(),
                                   self.rightprodname.get("1.0",END+"-1c"),
                                            self.rightprodprice.get("1.0",END+"-1c"),self.rightprodquantity.get("1.0",END+"-1c"))
            self.statusvar.set(result)

        def deleteButtonFunction(event):
            result = csvCode.deleteentry('test.csv',
                                   self.rightprodname.get("1.0",END+"-1c"))

            self.statusvar.set(result)

        def modifyButtonFunction(event):
            result = csvCode.modifyentry('test.csv',self.createvaloption.get(),self.creatvalsuboption.get(),
                                   self.rightprodname.get("1.0",END+"-1c"),
                                            self.rightprodprice.get("1.0",END+"-1c"),self.rightprodquantity.get("1.0",END+"-1c"))
            self.statusvar.set(result)
        def CsvButton(event):
            result = csvCode.exportcsv('test.csv',self.newCsvTxt.get("1.0",END+"-1c"))
            self.csvlabel.delete(1.0, END)
            self.csvlabel.insert(END, result)


        #=================Central Frame===============#
        mFrame = Frame(self.root, bd=20, width=1290, height=700, bg="cadet blue", relief=RIDGE)
        mFrame.grid()
        #=============================================#

        #===================Left Frame================#
        #Frame Initialization
        lFrame = Frame(mFrame, bd=10, width=600, height=570, pady=10, bg="powder blue", relief=RIDGE)
        lFrame.pack(side=LEFT)
        lFrame0 = Frame(lFrame, bd=10, width=600, height=100, padx=10, bg="powder blue", relief=RIDGE)
        lFrame0.grid(row=1, column=0)
        lFrame1 = Frame(lFrame, bd=10, width=600, height=100, padx=10, bg="white", relief=RIDGE)
        lFrame1.grid(row=0, column=0)
        lFrame2 = Frame(lFrame, bd=10, width=600, height=100, padx=10, bg="white", relief=RIDGE)
        lFrame2.grid(row=2, column=0)

        #lFrame0 Structure List GUI
        self.leftTItle=Label(lFrame1, font=('arial', 30, 'bold'), text="Product Listing", padx=2, pady=2, bg="white", )
        self.leftTItle.grid(row=0, column=2, sticky=W)


        self.leftprod = Label(lFrame0, font=('arial', 18, 'bold'), text="Categories:", padx=2, pady=2, bg="powder blue", )
        self.leftprod.grid(row=0, column=2, sticky=W)


        self.products = ttk.Combobox(lFrame0, textvariable=self.productVar, state='readonly',
                                     font=('arial', 18, 'bold'),width=10)
        self.products['value'] = self.listoptions
        self.products.current(0)
        self.products.grid(row=0, column=3)
        self.products.bind("<<ComboboxSelected>>", productOptions)

        self.leftstock = Label(lFrame0, font=('arial', 18, 'bold'), text="   Products:", padx=2, pady=2, bg="powder blue", )
        self.leftstock.grid(row=1, column=2, sticky=W)

        self.productComboBox=ttk.Combobox(lFrame0, textvariable=self.productVal, state='readonly',
                                     font=('arial', 18, 'bold'),width=10)
        self.productComboBox['value']=[]
        self.productComboBox.grid(row=1,column=3)
        self.productComboBox.bind("<<ComboboxSelected>>", prodsubOptions)
        self.listVar.set(self.initlist)
        self.leftname = Label(lFrame2, font=('arial', 10, 'bold'), padx=2, pady=2,
                               bg="white", height=20, width =40,textvariable=self.listVar)
        self.leftname.grid(row=0,column=0, sticky =W)

        # self.scrollbar = ttk.Scrollbar(root,orient='vertical',command=self.listVar.yview)
        #
        # self.leftname['yscrollcommand'] = self.scrollbar.set

        #=============================================#

        # ===================Right Frame================#
        rFrame = Frame(mFrame, bd=10, width=650, height=570, padx=0,pady=0, bg="powder blue", relief=RIDGE)
        rFrame.pack(side=RIGHT)

        # ======frame0===========#

        rFrame0 = Frame(rFrame, bd=10, width=600, height=100, padx=10, bg="white", relief=RIDGE)
        rFrame0.grid(row=0, column=0)

        self.rightTItle = Label(rFrame0, font=('arial', 30, 'bold'), text="Product Manager", padx=160, pady=2,
                                bg="white", )
        self.rightTItle.grid(row=0, column=2, sticky=W)

        # ==============frame1================#

        rFrame1 = Frame(rFrame, bd=10, width=600, height=100, padx=0, pady=0, bg="powder blue", relief=RIDGE)
        rFrame1.grid(row=1, column=0)

        self.inputTItle = Label(rFrame1, font=('arial', 30, 'bold'), text="Product Input", padx=270, pady=2,
                                bg="powder blue", )
        self.inputTItle.grid(row=0, column=0, sticky=W)

        #=========frame2==========# Parameters for button functions

        rFrame2 = Frame(rFrame1, bd=10, width=600, height=100, padx=0,pady=0, bg="powder blue", relief=RIDGE)
        rFrame2.grid(row=2, column=0)

        self.createComboBox = ttk.Combobox(rFrame2, textvariable=self.createvaloption, state='readonly',
                                            font=('arial', 10, 'bold'), width=10)

        oldlist=self.listoptions.copy()
        oldlist.remove("All")
        self.createComboBox['value']=oldlist
        self.createComboBox.grid(row=0,column=1)

        self.createLabel = Label(rFrame2, font=('arial', 14, 'bold'), text="Category:", padx=2, pady=2,
                               bg="powder blue", )
        self.createLabel.grid(row=0, column=0)

        self.createCombosubBox = ttk.Combobox(rFrame2, textvariable=self.creatvalsuboption, state='readonly',
                                           font=('arial', 10, 'bold'), width=10)
        self.createCombosubBox['value'] = []
        self.createCombosubBox.grid(row=0, column=3)

        self.createsubLabel = Label(rFrame2, font=('arial', 14, 'bold'), text="Products:", padx=2, pady=2,
                                 bg="powder blue", )
        self.createsubLabel.grid(row=0, column=2)

        self.createComboBox.bind("<<ComboboxSelected>>", createOptions)

        self.rightprod = Label(rFrame2, font=('arial', 14, 'bold'), text="ProductName:", padx=2, pady=2,
                               bg="powder blue", )
        self.rightprod.grid(row=2, column=0, sticky=W)

        self.rightprodname = Text(rFrame2, font=('arial', 10, 'bold'), padx=2, pady=2,
                                bg="white",height = 1, width =15 )
        self.rightprodname.grid(row=2, column=1, sticky=W)

        self.rightprodPr = Label(rFrame2, font=('arial', 14, 'bold'), text="ProductPrice:", padx=2, pady=2,
                               bg="powder blue", )
        self.rightprodPr.grid(row=2, column=2, sticky=W)

        self.rightprodprice = Text(rFrame2, font=('arial', 10, 'bold'), padx=2, pady=2,
                                  bg="white", height=1, width=15)
        self.rightprodprice.grid(row=2, column=3, sticky=W)

        self.rightprodQuant = Label(rFrame2, font=('arial', 14, 'bold'), text="ProductQuantity:", padx=2, pady=2,
                                 bg="powder blue", )
        self.rightprodQuant.grid(row=2, column=4, sticky=W)

        self.rightprodquantity = Text(rFrame2, font=('arial', 10, 'bold'), padx=2, pady=2,
                                   bg="white", height=1, width=15)
        self.rightprodquantity.grid(row=2, column=5, sticky=W)

        #=============#frame1&frame2Grouping==========#


        #===========frame3==========# Button functions for CRUD functionality

        rframe3 = Frame(rFrame1, bd=10, width=600, height=100, padx=0, bg="powder blue", relief=RIDGE)
        rframe3.grid(row=3, column=0)

        self.createbutton= Button(rframe3, font=('arial', 14, 'bold'), text="CreateProduct:", padx=2, pady=2,
                                 bg="light green",)
        self.createbutton.grid(row=0,column=0)
        self.createbutton.bind("<Button-1>",creatButtonFunction)

        self.modifybutton = Button(rframe3, font=('arial', 14, 'bold'), text="ModifyProduct:", padx=2, pady=2,
                                   bg="orange", )
        self.modifybutton.grid(row=0, column=1)
        self.modifybutton.bind("<Button-1>", modifyButtonFunction)

        self.deletebutton = Button(rframe3, font=('arial', 14, 'bold'), text="DeleteProduct:", padx=2, pady=2,
                                   bg="red", )
        self.deletebutton.grid(row=0, column=2)
        self.deletebutton.bind("<Button-1>",deleteButtonFunction)
        # =====================frame4-6========================# Button outcome output

        rFrame4 = Frame(rFrame, bd=10, width=600, height=100, padx=0, pady=0, bg="powder blue", relief=RIDGE)
        rFrame4.grid(row=2, column=0, sticky=W)

        rFrame5=Frame(rFrame4, bd=10, width=600, height=100, padx=0,pady=0, bg="powder blue", relief=RIDGE)
        rFrame5.grid(row=2, column=0,sticky=W)

        self.outputlb=Label(rFrame5, font=('arial', 30, 'bold'), text="Product Output", padx=30, pady=2,
                               bg="powder blue", )
        self.outputlb.grid(row=0, column=0, sticky=W)

        rFrame6 = Frame(rFrame5, bd=10, width=600, height=100, padx=0, pady=0, bg="powder blue", relief=RIDGE)
        rFrame6.grid(row=1, column=0)

        self.statusvar.set("")
        self.rightStatus = Label(rFrame6, font=('arial', 9, 'bold'), padx=2, pady=2,
                              bg="white", height=8, width=40, textvariable=self.statusvar)
        self.rightStatus.grid(row=1, column=0, sticky=W)

        #===========frame7==============# CSV export functionality

        rFrame7 = Frame(rFrame4, bd=10, width=440, height=265, padx=0, pady=0, bg="powder blue", relief=RIDGE)
        rFrame7.grid(row=2, column=1)

        self.csvManager= Label(rFrame7, font=('arial', 30, 'bold'), padx=2, pady=2,
                              bg="powder blue", text="CSV Manager")
        self.csvManager.grid(row=0,column=0)

        rFrame8= Frame(rFrame7, bd=10, width=40, height=40, padx=0, pady=0, bg="powder blue", relief=RIDGE)
        rFrame8.grid(row=1, column=0)

        self.newCsvName = Label(rFrame8, font=('arial', 14, 'bold'), padx=2, pady=2,
                                bg="powder blue", text="New CSV Name:")
        self.newCsvName.grid(row=0, column=0)
        self.newCsvTxt = Text(rFrame8, font=('arial', 10, 'bold'), padx=2, pady=2,
                                   bg="white", height=1, width=35)
        self.newCsvTxt.grid(row=0, column=1)

        self.exportcsv=Button(rFrame8, font=('arial', 14, 'bold'), text="ExportCsv:", padx=2, pady=2,
                                   bg="pink", )
        self.exportcsv.grid(row=1, column=0)
        self.exportcsv.bind("<Button-1>",CsvButton)

        self.csvresult= Label(rFrame8, font=('arial', 14, 'bold'), text= "Result:", padx=2, pady=2,
                                bg="powder blue", )
        self.csvresult.grid(row=2,column=0)

        self.csvlabel = Text(rFrame8, font=('arial', 10, 'bold'), padx=2, pady=2,
                                   bg="white", height=1, width=35)
        self.csvlabel.grid(row=2, column=1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    application = Inventory(root)
    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
