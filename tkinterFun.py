import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd


from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.title('Foo')

class fooFrame(tk.Frame):
    
    def __init__(self, master):
        super(fooFrame,self).__init__()
        
        self.optionFrame = tk.Frame(self,borderwidth=1, relief="solid")
        self.optionFrame.pack(side=tk.LEFT)
        
        self.parameterFrame = tk.Frame(self,borderwidth=1, relief="solid")
        self.parameterFrame.pack(side=tk.LEFT)
        
        self.deleteButtonFrame = tk.Frame(self,borderwidth=1, relief="solid")
        self.deleteButtonFrame.pack(side=tk.LEFT)
        
        self.button1 = tk.Button(self.optionFrame,text="Button",command=lambda: buttonPress(self,master))
        self.button1.pack()
        self.entry = tk.Entry(self.parameterFrame)
        self.entry.pack()
        self.button2 = tk.Button(self.deleteButtonFrame,text="another button",command=lambda: buttonPress2(self))
        self.button2.pack()
        
class menuFrame(tk.Frame):
    
    def __init__(self, master, **kwargs):
        super(menuFrame, self).__init__(master=master, **kwargs)
        
        self.optionFrame = optionFrame(self)
        self.optionFrame.pack(side=tk.LEFT)
             
        self.parameterFrame = parameterFrame(self)
        self.parameterFrame.pack(side=tk.LEFT)
        
        self.deleteButtonFrame = deleteButtonFrame(self,borderwidth=1, relief="solid")
        self.deleteButtonFrame.pack(side=tk.RIGHT)
        
class optionFrame(tk.Frame):
    
    def __init__(self, master, **kwargs):
        super(optionFrame, self).__init__(master=master, **kwargs)
          
        self.opts = ["Univariate Logit","Multivariate Logit","Polar Plots", 'Pe Comparison']
        self.var = tk.StringVar()
        self.var.set('Ignore')
        
        # self.opts = root.data.columns.values
        # print(root.data.columns.values)
        
        self.opt = tk.OptionMenu(self,self.var,*self.opts)
        self.opt.pack()
        # self.opt = tk.OptionMenu(self,self.var,*root.data.columns.values)
        # self.opt.pack()
        
        self.var.trace_add('write', lambda *_, var=self: OptionMenu_SelectionEvent(self))
        
class parameterFrame(tk.Frame):
    
    def __init__(self, master, **kwargs):
        super(parameterFrame, self).__init__(master=master)
        
        paramFrameType = self.master.optionFrame.var.get()
        
        multiVariateOpts = ['Continuous',
                            'Categorical (Ref)',
                            'Categorical (Zero Sum)',
                            'Response',
                            'Fixed',
                            'Ignore']
        
    
        if paramFrameType == 'Ignore':
            self.label = tk.Label(self,text='No Analysis Selected')
            self.label.pack()           

        elif paramFrameType == 'Univariate Logit':
            # self.label = tk.Label(self,text='Univariate')
            # self.label.pack()
            print('work in progress...')
                

        elif paramFrameType == 'Multivariate Logit':
            for headerVar in root.data.columns.values:
                self.multivariateFrame = multivariateFrame(self, headerVar)
                self.multivariateFrame.pack(side=tk.TOP,anchor=tk.E)
                    

        elif paramFrameType == 'Polar Plots':
            for headerVar in root.data.columns.values:
                self.polarFrame = polarFrame(self, headerVar)
                self.polarFrame.pack(side=tk.TOP,anchor=tk.E)
 
        
        elif paramFrameType == 'Pe Comparison':
            for headerVar in root.data.columns.values:
                self.peComparisonFrame = peComparisonFrame(self, headerVar)
                self.peComparisonFrame.pack(side=tk.TOP,anchor=tk.E)
            

        else:
            self.label = tk.Label(self,text='Invalid Option Detected')
            self.label.pack()       

class peComparisonFrame(tk.Frame):
    
    def __init__(self, master, varName, **kwargs):
        super(peComparisonFrame, self).__init__(master=master)
        
        univariateOpts = ['Independent Variable',
                          'Response Variable',
                          'Separate Curves',
                          'Separate Figures',
                          'Fixed',
                          'Ignore']
        
            
        self.var = tk.StringVar()
        self.var.set('Ignore')
        
        self.label = tk.Label(self,text=varName)
        self.label.grid(row = 0, column=0)
        
        self.opt = tk.OptionMenu(self,self.var,*univariateOpts)
        self.opt.grid(row = 0, column=1)

class multivariateFrame(tk.Frame):
    
    def __init__(self, master, varName, **kwargs):
        super(multivariateFrame, self).__init__(master=master)
        
        multiVariateOpts = ['Continuous',
                            'Categorical (Ref)',
                            'Categorical (Zero Sum)',
                            'Response',
                            'Fixed',
                            'Ignore']
        
            
        self.var = tk.StringVar()
        self.var.set('Ignore')
        
        self.label = tk.Label(self,text=varName)
        self.label.grid(row = 0, column=0)
        
        self.opt = tk.OptionMenu(self,self.var,*multiVariateOpts)
        self.opt.grid(row = 0, column=1)


class polarFrame(tk.Frame):
    
    def __init__(self, master, varName, **kwargs):
        super(polarFrame, self).__init__(master=master)
        
        polarOpts = ['Range',
                          'Azimuth',
                          'Separate Figures',
                          'Ensemble',
                          'Ignore']
        
            
        self.var = tk.StringVar()
        self.var.set('Ignore')
        
        self.label = tk.Label(self,text=varName)
        self.label.grid(row = 0, column=0)
        
        self.opt = tk.OptionMenu(self,self.var,*polarOpts)
        self.opt.grid(row = 0, column=1)
        
            
class univariateFrame(tk.Frame):
    
    def __init__(self, master, varName, **kwargs):
        super(univariateFrame, self).__init__(master=master)
        
        univariateOpts = ['Independent Variable',
                          'Response Variable',
                          'Separate Curves',
                          'Separate Figures',
                          'Fixed',
                          'Ignore']
        
            
        self.var = tk.StringVar()
        self.var.set('Ignore')
        
        self.label = tk.Label(self,text=varName)
        self.label.grid(row = 0, column=0)
        
        self.opt = tk.OptionMenu(self,self.var,*univariateOpts)
        self.opt.grid(row = 0, column=1)
            
            

        
class deleteButtonFrame(tk.Frame):
    
    def __init__(self, master, **kwargs):
        super(deleteButtonFrame, self).__init__(master=master)
        
        self.xPhoto = tk.PhotoImage(file = 'redX.png')
        self.xPhoto = self.xPhoto.subsample(20,20)

        # deleteButton = tk.Button(self, image = self.xPhoto, command=self.destroyMenuFrame)
        deleteButton = tk.Button(self, image = self.xPhoto, command=lambda: self.destroyMenuFrame(self))
        deleteButton.pack()
        
    # def destroyMenuFrame(self):
    def destroyMenuFrame(self,*args):
        # print('foo')
        self.master.destroy()
        
        
class fileSelectFrame(tk.Frame):
    
    def __init__(self, master, **kwargs):
        super(fileSelectFrame, self).__init__(master=master, **kwargs)
        
        self.fileButton = tk.Button(self,text='Select File', command = lambda:self.openFile())
        self.fileButton.pack(side=tk.LEFT)
        self.fileLabel = tk.Label(self,width = 100)
        self.fileLabel.pack(side=tk.LEFT)

        
        
    def openFile(self,*args):
        root.filename =  askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("CSV Files","*.csv"),("all files","*.*")))
        if root.filename is not None:
            # self.fileLabel.delete(0,tk.END)
            self.fileLabel['text'] = root.filename
        root.data = pd.read_csv(root.filename)
        goButton['state'] = tk.NORMAL
        addButton['state'] = tk.NORMAL
        
                    
def buttonPress(self, master):
    # print(foo)
    # print(re.findall(r'\d+', str(self)))
    print(self)
    print(master)

def buttonPress2(self):
    
    # parent = self.winfo_parent()
    # print(parent)
    # children = parent.winfo_children()
    # print(children)
    print('*********self*********')
    print(self)
    print('*******children*******')
    print(self.winfo_children())
    # print('*children of children*')
    # print(self.winfo_children().winfo_children())
    parent = self.winfo_parent()
    print('********parent********')
    print(parent)

def printValues():
    print('\n\n')
    # for menuFrame in root.menuFrames:
    for child in root.winfo_children():
        # children_widgets = root.menuFrame.winfo_children()
        # if('menuframe' in child):
        print(child)
        # print(type(child))
        for child2 in child.winfo_children():
            print('\t'+str(child2))

    print('\n\n')
    for analysisOpts in range(3,len(root.winfo_children())):
        # print(root.winfo_children()[3].optionFrame.var.get())
        print(root.winfo_children()[analysisOpts].optionFrame.var.get())
        for parameters in root.winfo_children()[analysisOpts].parameterFrame.winfo_children():
        # for parameters in root.winfo_children()[analysisOpts].parameterFrame.winfo_children():
            # print('\t'+root.winfo_children()[analysisOpts].parameterFrame.winfo_children()[parameters].label.text())
            print('\t'+str(parameters.label['text']+': '+parameters.var.get()))
    print('\n\n')
    
    
    
# def goButton():
#     for child in root.winfo_children():
#         if 'menuframe' in str(child):
#             print(child)
#             print(root.children[child])
#             # for child2 in root.children[child].winfo_children():
#             #     print('\t'+str(child2))
        
def tree_select_event(self, event):
    item_iid = self.tree.selection()[0]
    parent_iid = self.tree.parent(item_iid)

    if parent_iid:
        print(self.tree.item(parent_iid)['text'])
    else:
        print(self.tree.item(item_iid)['text'])
        
def OptionMenu_SelectionEvent(self,*args): # I'm not sure on the arguments here, it works though

    print('**************************')
    for child in self.master.children:
        print(self.master.children[child])
        
    self.master.parameterFrame.destroy()
    
    self.master.parameterFrame = parameterFrame(self.master,name='parameterframe')
    self.master.parameterFrame.pack(side=tk.RIGHT)
    
def createMenuFrame():
    
    root.menuFrame = menuFrame(root,borderwidth=1, relief=tk.SOLID)
    root.menuFrames.append(menuFrame)

    root.menuFrame.pack(side="top", fill="x")

    
    
    
    


root.menuFrames = []


fileSelect = fileSelectFrame(root,borderwidth=1, relief=tk.GROOVE)
fileSelect.pack()

goButton = tk.Button(root,text="Go",command = printValues)
goButton.pack(side=tk.BOTTOM)
goButton['state'] = tk.DISABLED

addButton = tk.Button(root, text="Add Analysis", command=createMenuFrame)
addButton.pack(side=tk.BOTTOM)
addButton['state'] = tk.DISABLED
        

        
        
        
root.mainloop()