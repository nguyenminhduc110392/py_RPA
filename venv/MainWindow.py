import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *

import VariableList as variablelist
import Variable as variable
import Script as script
import NodeBase as nodebase
import NodeGroup as nodegroup
import IfNode as ifnode
import ForNode as fornode
import AssignNode as assnode
import BreakNode as breaknode
import Expresstion as exp


class MainWindow(object):
    __root = Tk()
    # default window width and height
    __thisWidth = 540
    __thisHeight = 300
    # __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)

    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisRunMenu = Menu(__thisMenuBar, tearoff=0)
    __thisViewMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # __thisRunButton = Button(__root)
    __thisAddButton = Button(__root)
    __thisDeleteButton = Button(__root)
    __thisActionListBox = Listbox(__root)
    __thisLibraryTreeView = ttk.Treeview(__root)
    # To add scrollbar
    __thisLibraryTreeViewScrollBar = Scrollbar(__root)
    __thisActionListBoxScrollBar = Scrollbar(__root)
    __thisSelectLabel = Label(__root)
    # __thisTopWinDow = Toplevel()

    __thisScript = script.Script()
    __thisVariableList = variablelist.VariableList()
    __file = None

    def __init__(self, **kwargs):
        # Set icon
        try:
            self.__root.wm_iconbitmap("robot-ico.ico")
        except:
            pass
        # Set window size (the default is 300x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled - pyRPA")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))
        # self.__thisRunButton.pack(side=LEFT)
        # To make the textarea auto resizable
        # self.__root.grid_rowconfigure(0, weight=1)
        # self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        # self.__thisTextArea.grid(sticky = N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)

        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        self.__thisViewMenu.add_command(label="Editor",
                                        command=self.__openEditor)
        # To give a feature of cut
        self.__thisViewMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisViewMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisViewMenu.add_command(label="Paste",
                                        command=self.__paste)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="View",
                                       menu=self.__thisViewMenu)

        self.__thisMenuBar.add_cascade(label="Run",
                                       menu=self.__thisRunMenu)

        self.__thisRunMenu.add_command(label="Excute",
                                       command=self.__runScript)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About pyRPA",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        # self.__thisScrollBar.pack(side=RIGHT,fill=Y)

        # Scrollbar will adjust automatically according to the content
        # self.__thisRunButton.config(text='Run', width=7, height=3, command=self.__runScript)
        # self.__thisRunButton.grid(row=0, column=0)
        self.__thisAddButton.config(text='Add', command=self.__addNode)
        self.__thisAddButton.grid(row=0, column=0, rowspan=1, columnspan=1)

        self.__thisDeleteButton.config(text='Delete', command=self.__deleteNode)
        self.__thisDeleteButton.grid(row=0, column=3, rowspan=1, columnspan=1)

        self.__thisActionListBox.config(yscrollcommand=self.__thisActionListBoxScrollBar.set)
        self.__thisActionListBox.grid(row=0, column=3, columnspan=2, rowspan=6)
        self.__thisActionListBox.bind('<<ListboxSelect>>', self.onselect)
        self.__thisActionListBoxScrollBar.config(command=self.__thisActionListBox.yview)
        self.__thisActionListBoxScrollBar.grid(row=0, column=6, columnspan=1, rowspan=6)
        self.__thisSelectLabel.grid(row=0, column=7)
        self.__thisLibraryTreeView.config(show="tree", yscrollcommand=self.__thisLibraryTreeViewScrollBar.set)
        self.__thisLibraryTreeView.grid(row=1, column=0, columnspan=2, rowspan=4)
        self.__thisLibraryTreeViewScrollBar.config(command=self.__thisLibraryTreeView.yview)
        self.__thisLibraryTreeViewScrollBar.grid(row=1, column=2, columnspan=1, rowspan=4)

        #self.__thisConfigNodeFrame()
        self.__loadTreeView()

        # self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    def onselect(self,evt):
        selector = evt.widget
        index = int(selector.curselection()[0])
        index_value = selector.get(index)
        self.__thisSelectLabel.config(text=index_value)

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __loadTreeView(self):
        list_node = (
            "group", "node-base", "assign", "if-else", "multi-if", "for-loop", "while-loop", "do-while-loop", "break",
            "continue", "try-catch", "subscript-call", "subscript-create", "return")
        f1 = self.__thisLibraryTreeView.insert("", 0, iid="Main Node", text="Node")
        for i in list_node:
            self.__thisLibraryTreeView.insert(f1, "end", text=i)
        f2 = self.__thisLibraryTreeView.insert("", "end", iid="Library Node", text="Library")
        self.__thisLibraryTreeView.insert(f2, "end", text="test_func1")
        self.__thisLibraryTreeView.insert(f2, "end", text="test_func2")
        self.__thisLibraryTreeView.insert(f2, "end", text="open_chrome")
        self.__thisLibraryTreeView.insert(f2, "end", text="open_gmail")

    def __addNode(self):
        self.__thisActionListBox.insert(END,
                                        self.__thisLibraryTreeView.item(self.__thisLibraryTreeView.focus())['text'])
        self.__addActionToScript(self.__thisLibraryTreeView.item(self.__thisLibraryTreeView.focus())['text'])
        # self.__thisScript.__additem__()
        return

    def __addActionToScript(self, type):
        if type == "assign":
            self.__thisVariableList.__adduniqueitem__(variable.Variable("driver", "", ""))
            self.__thisVariableList.__adduniqueitem__(variable.Variable("url", "", "http://gmail.com"))
            # self.__thisScript.__additem__(assnode.AssignNode("", ""))
        elif type == "if-else":
            self.__thisScript.__additem__(ifnode.IfNode("", "", ""))
        elif type == "node-base":
            self.__thisScript.__additem__(nodebase.NodeBase("", "test_func1"))
        elif type == "test_func1":
            self.__thisScript.__additem__(nodebase.NodeBase("node-base1", "test_func1"))
        elif type == "test_func2":
            self.__thisScript.__additem__(nodebase.NodeBase("node-base2", "test_func2"))
        elif type == "open_chrome":
            self.__thisScript.__additem__(nodebase.NodeBase("node-base1", "open_chrome"))
        elif type == "open_gmail":
            self.__thisScript.__additem__(nodebase.NodeBase("node-base2", "open_gmail"))

    def __deleteNode(self):
        self.__thisActionListBox.delete(ANCHOR)
        return

    def __showAbout(self):
        showinfo("pyRPA", "wingchaos2012@gmail.com")

    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            # self.__thisTextArea.delete(1.0,END)

            file = open(self.__file, "r")

            # self.__thisTextArea.insert(1.0,file.read())

            file.close()

    def __newFile(self):
        self.__root.title("new file - pyRPA")
        self.__file = None
        self.__thisActionListBox.delete(0,END)
        self.__thisScript.__del__()

        del self.__thisVariableList
        print(self.__thisVariableList.__getleng__())
        self.__thisScript = script.Script()
        self.__thisVariableList = variablelist.VariableList()
        self.__thisLibraryTreeView.item("Main Node", open=False)
        self.__thisLibraryTreeView.item("Library Node", open=False)
        # self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                # file.write(self.__thisTextArea.get(1.0,END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        # self.__thisTextArea.event_generate("<<Cut>>")
        pass

    def __copy(self):
        # self.__thisTextArea.event_generate("<<Copy>>")
        pass

    def __paste(self):
        # self.__thisTextArea.event_generate("<<Paste>>")
        pass

    def __runScript(self):
        self.__thisScript.__run__()
        pass

    def __openEditor(self):
        pass

    def run(self):
        # Run main application
        self.__root.mainloop()
