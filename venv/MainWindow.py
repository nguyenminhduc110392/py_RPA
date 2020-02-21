import json
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
    rootframe = Tk()
    width = 800
    height = 620
    rootframe.geometry('{}x{}'.format(width, height))

    # menu bar
    menubar = Menu(rootframe)
    filemenu = Menu(menubar, tearoff=0)
    runmenu = Menu(menubar, tearoff=0)
    viewmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    # create all of the main containers
    topframe = Frame(rootframe, bg='cyan', width=450, height=50, pady=3)
    center = Frame(rootframe, bg='gray2', width=50, height=40, padx=3, pady=3)
    # btmframe = Frame(rootframe, bg='white', width=450, height=45, pady=3)
    # btmframe2 = Frame(rootframe, bg='lavender', width=450, height=60, pady=3)

    # layout all of the main containers
    rootframe.grid_rowconfigure(1, weight=1)
    rootframe.grid_columnconfigure(0, weight=1)

    topframe.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")

    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    controlleft = Frame(center, bg='blue', width=300)
    controlmid = Frame(center, bg='yellow', width=250, padx=3, pady=3)
    controlright = Frame(center, bg='green', width=300, padx=3, pady=3)

    controlleft.grid(row=0, column=0, sticky="ns")
    controlmid.grid(row=0, column=1, sticky="nsew")
    controlright.grid(row=0, column=2, sticky="ns")

    bottompanel = PanedWindow(rootframe, orient=VERTICAL)
    panelframe = Frame(bottompanel, bg="#9dc8e3")
    bottompanel.add(panelframe, minsize=150)
    bottompanel.grid(row=3, column=0, sticky="nsew")
    top = Label(panelframe, text="PANEL")
    top.pack(fill=BOTH, expand=1)

    librarytreeviewscollbar = Scrollbar(controlleft)
    librarytreeview = ttk.Treeview(controlleft)
    librarytreeviewscollbar.config(command=librarytreeview.yview)
    librarytreeviewscollbar.pack(side="right", fill="y")

    librarytreeview.config(show="tree", yscrollcommand=librarytreeviewscollbar.set)
    librarytreeview.pack(side="left", fill="y")

    actionlistbox = Listbox(controlmid, width=230)
    actionlistbox.pack(side="left", fill="y")

    actionlistboxscollbar = Scrollbar(controlmid, orient="vertical")
    actionlistboxscollbar.config(command=actionlistbox.yview)
    actionlistboxscollbar.pack(side="right", fill="y")
    actionlistbox.config(yscrollcommand=actionlistboxscollbar.set)

    selectlabel = Label(controlright, width=30)
    selectlabel.pack(fill="both")

    mainscript = script.Script()
    variablelist = variablelist.VariableList()

    file = None
    def __init__(self, **kwargs):
        # Set icon
        try:
            self.rootframe.wm_iconbitmap("robot-ico.ico")
        except:
            pass

        # Window title
        self.rootframe.title("NewFile - pyRPA")
        self.menubar.add_cascade(label="File",
                                 menu=self.filemenu)

        # To open new file
        self.filemenu.add_command(label="New",
                                  command=self.new_file_command)

        # To open a already existing file
        self.filemenu.add_command(label="Open",
                                  command=self.open_file_command)

        # To save current file
        self.filemenu.add_command(label="Save",
                                  command=self.save_file_command)

        # To save current file
        self.filemenu.add_command(label="Save As",
                                  command=self.save_file_as_command)

        # To create a line in the menu
        self.filemenu.add_separator()

        # To create a Script help
        self.menubar.add_cascade(label="Script",
                                 menu=self.runmenu)
        # To run the scenario
        self.runmenu.add_command(label="Run",
                                 command=self.run_script)
        # To Exit application
        self.filemenu.add_command(label="Exit",
                                  command=self.quit_application)

        # To create a menu help
        self.menubar.add_cascade(label="Help",
                                 menu=self.helpmenu)

        # To create a feature of description of the application
        self.helpmenu.add_command(label="About",
                                  command=self.show_about)

        self.rootframe.config(menu=self.menubar)

        # self.actionlistbox.config(yscrollcommand=self.actionlistboxscollbar.set)
        # self.actionlistbox.grid(row=0, column=3, columnspan=2, rowspan=6)
        # self.actionlistbox.bind('<<ListboxSelect>>', self.onselect)

        self.librarytreeview.bind("<Double-1>", self.event_on_add)
        self.actionlistbox.bind("<ButtonRelease-1>", self.event_on_select)
        self.actionlistbox.bind("<Double-1>", self.event_on_access)
        # self.librarytreeview.bind("<ButtonPress-1>", self.bDown)
        # self.librarytreeview.bind("<ButtonRelease-1>", self.bUp)
        # self.librarytreeview.bind("<B1-Motion>", self.bMove)

        # self.actionlistboxscollbar.config(command=self.__thisActionListBox.yview)
        # self.actionlistboxscollbar.grid(row=0, column=6, columnspan=1, rowspan=6)
        self.load_tree_view()

    def event_on_access(self, event):
        selector = event.widget
        index = int(selector.curselection()[0])
        index_value = selector.get(index)
        if hasattr(self.mainscript.node_list[index], 'accessible'):
            if self.mainscript.node_list[index].accessible==True:
                self.access_node(self.mainscript.node_list[index])
        return

    def access_node(self,element):
        print("accessed")
        pass

    def event_on_select(self, event):
        selector = event.widget
        index = int(selector.curselection()[0])
        index_value = selector.get(index)
        self.selectlabel.config(text=index_value + " setting")
        self.load_properties(self.mainscript.node_list[index])
        return

    def load_properties(self,element):
        properties_dic = element.load_properties_list()

    def event_on_add(self, event):
        selected = self.librarytreeview.focus()
        if self.librarytreeview.item(selected)['tags'] != ['Fd']:
            self.actionlistbox.insert(END, self.librarytreeview.item(self.librarytreeview.focus())['text'])
            self.add_action_to_script(self.librarytreeview.item(self.librarytreeview.focus())['text'])
        return

    def add_action_to_script(self, type):
        if type == "assign":
            self.variablelist.__adduniqueitem__(variable.Variable("driver", ""))
            self.variablelist.__adduniqueitem__(variable.Variable("url", "http://gmail.com"))
            #self.mainscript.__additem__(assnode.AssignNode("abc", "123"))
        elif type == "if-else":
            self.mainscript.__additem__(ifnode.IfNode("", "", ""))
        elif type == "node-base":
            self.mainscript.__additem__(nodebase.NodeBase("", "test_func1"))
        elif type == "test_func1":
            self.mainscript.__additem__(nodebase.NodeBase("node-base1", "test_func1"))
        elif type == "test_func2":
            self.mainscript.__additem__(nodebase.NodeBase("node-base2", "test_func2"))
        elif type == "open_chrome":
            self.mainscript.__additem__(nodebase.NodeBase("node-base1", "open_chrome"))
        elif type == "open_gmail":
            self.mainscript.__additem__(nodebase.NodeBase("node-base2", "open_gmail"))
        elif type == "message-box":
            self.mainscript.__additem__(nodebase.NodeBase("node-base2", "message_box"))
        elif type == "group":
            self.mainscript.__additem__(nodegroup.NodeGroup("node-group1", "group1"))
        return

    def bDown(self, event):
        tv = event.widget
        if tv.identify_row(event.y) not in tv.selection():
            tv.selection_set(tv.identify_row(event.y))
            print(tv.selection_set(tv.identify_row(event.y)))
        return

    def bUp(self, event):
        tv = event.widget
        if tv.identify_row(event.y) in tv.selection():
            tv.selection_set(tv.identify_row(event.y))
        return

    def bMove(self, event):
        tv = event.widget
        moveto = tv.index(tv.identify_row(event.y))
        for s in tv.selection():
            tv.move(s, '', moveto)

    def run(self):
        # Run main application
        self.rootframe.mainloop()

    def new_file_command(self):
        pass

    def open_file_command(self):
        self.file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.rootframe.title(os.path.basename(self.file) + " - Notepad")
            # self.__thisTextArea.delete(1.0,END)

            file = open(self.file, "r")
            self.mainscript = json.loads(file.read())
            file.close()

    def save_file_command(self):
        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.mainscript.toJSON())
                #json.dump(self.mainscript.toJSON(), file)
                file.close()

                # Change the window title
                self.rootframe.title(os.path.basename(self.file))
        else:
            file = open(self.file, "w")
            file.write(self.mainscript.toJSON())
            #print(self.mainscript.toJSON())
            #json.dump(self.mainscript.toJSON(), file)
            file.close()

    def save_file_as_command(self):
        pass

    def run_script(self):
        self.mainscript.__run__()
        pass

    def quit_application(self):
        pass

    def show_about(self):
        pass

    def load_tree_view(self):
        # create node folder
        # list_node = (
        #     "group", "node-base", "assign", "if-else", "multi-if", "for-loop", "while-loop", "do-while-loop", "break",
        #     "continue", "try-catch", "subscript-call", "subscript-create", "return","message-box")
        nodeList = (
            "group", "node-base", "assign", "if-else", "message-box")
        f1 = self.librarytreeview.insert("", 0, iid="Main Node", text="Node", tags="Fd")
        for i in nodeList:
            self.librarytreeview.insert(f1, "end", text=i)

        # create library folder
        f2 = self.librarytreeview.insert("", "end", iid="Library Node", text="Library", tags="Fd")
        self.librarytreeview.insert(f2, "end", text="test_func1")
        self.librarytreeview.insert(f2, "end", text="test_func2")
        self.librarytreeview.insert(f2, "end", text="open_chrome")
        self.librarytreeview.insert(f2, "end", text="open_gmail")
        return
