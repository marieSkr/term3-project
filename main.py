import tkinter
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

from image_functions import * #Imports the functions for image and matrix transformations from a separate file

def Matrix_calc_open(): #Function that runs the matrix calculator window

#---------------------------------------Functions used by matrix calculator--------------------------
    def transp_button(matname): 
        newmat = matrix_transpose(matrices[matname])
        matrices[matname] = newmat      

    def listbox_convenience(name, mat):
        if name in matrices.keys():
            print("it already exists")
        else:
            matrixlistbox.insert(
                0, name+"("+str(len(mat))+"x"+str(len(mat[0]))+")")
            matrices[name] = mat

    def matrix_operations(a, b, newname, op):   #Function that is responsible for basic matrix operations
        operations = [matrix_addition, matrix_subtraction,
                      matrix_multiplication, scalar_multiplication]
        newmat = operations[op](a, b)
        listbox_convenience(newname, newmat)
   
    def matrix_define(rows, columns, elements, name): #Function for the matrix define button
        nonlocal matrices
        s = elements.split()
        a = []
        for i in range(rows):
            temp = []
            for j in range(columns):
                temp.append(float(s[i*columns+j]))               
            a.append(temp)
        listbox_convenience(name, a)

    def matrix_display(matname):  #Function for the matrix display button
        mat = matrices[matname]
        matrixwindow = tkinter.Toplevel()
        matrixwindow.title(matname)
        matrixwindow.geometry("400x400")
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                label = tkinter.Label(matrixwindow, textvariable=tkinter.StringVar(
                    matrixwindow, mat[i][j]), font=("Arial", 16, "bold"), fg="black")
                label.grid(row=i, column=j)

    def frameopen(a):  #Function that allows to change interface frames
        nonlocal frame
        if frame != 0:
            frame.pack_forget()
        a.pack()
        frame = a

# ------------------------------------------------------------------------------------------------------
    frame = 0      # a variable that determines which frame is currently open
    matrices = {}      # a dictionary storing all the matrices defined

    matrixcalc = tkinter.Toplevel()
    matrixcalc.geometry("820x400")
    matrixcalc.config(bg="gray90")  # defining a new window
    matrixcalc.resizable(True,False)
    matrixcalc.title("Matrix calculator")
    
    button1 = tkinter.Button(matrixcalc, text="Matrix \n creation", command=lambda: frameopen(
        framelist[0]), width=12, height=0, background="gray80")
    button1.grid(column=0, row=0, pady=20, padx=15)

    button2 = tkinter.Button(matrixcalc, text="Matrix \n manage", command=lambda: frameopen(
        framelist[1]), width=12, height=0, background="gray80")
    button2.grid(column=1, row=0, pady=20, padx=15)

    button3 = tkinter.Button(matrixcalc, text="Matrix \n operations", command=lambda: frameopen(
        framelist[2]), width=12, height=0, background="gray80")
    button3.grid(column=2, row=0, pady=20, padx=15)

    # a listbox that displays all the matrices stored in the current instance of calculator
    matrixlistbox = tkinter.Listbox(matrixcalc, width=40, height=13)
    matrixlistbox.grid(column=0, columnspan=3, row=1, padx=20)

    # a frame which serves as a placement anchor for other frames that the interface consists of
    emptyframe = tkinter.Frame(matrixcalc)
    emptyframe.grid(column=3, columnspan=3, row=1, padx=20)

    framelist = [tkinter.Frame(emptyframe, background="gray90", width=200, height=300), tkinter.Frame(
        emptyframe, background="gray90", width=200, height=300), tkinter.Frame(emptyframe, background="gray90", width=200, height=300)]
# ---------------------------------------------Matrix defining-------------------------------

    define_row_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
        framelist[0], "Rows:"), fg="black", bg="gray90", width=8)
    define_row_label.grid(row=0, column=0, pady=5, sticky="w")

    define_row_entry = tkinter.Entry(framelist[0])
    define_row_entry.grid(row=0, column=1, sticky="w")

    define_column_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
        framelist[0], "Columns:"), fg="black", bg="gray90", width=8)
    define_column_label.grid(row=1, column=0, pady=5, sticky="w")

    define_column_entry = tkinter.Entry(framelist[0])
    define_column_entry.grid(row=1, column=1, sticky="w")

    define_elements_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
        framelist[0], "Elements:"), fg="black", bg="gray90", width=8)
    define_elements_label.grid(row=2, column=0, pady=5, sticky="w")

    define_elements_entry = tkinter.Entry(framelist[0])
    define_elements_entry.grid(row=2, column=1, sticky="w")

    define_column_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
        framelist[0], "Name:"), fg="black", bg="gray90", width=8)
    define_column_label.grid(row=3, column=0, pady=5, sticky="w")

    define_name_entry = tkinter.Entry(framelist[0])
    define_name_entry.grid(row=3, column=1, sticky="w")

    button5 = tkinter.Button(framelist[0], text="Define the matrix", command=lambda: matrix_define(int(define_row_entry.get()), int(
        define_column_entry.get()), define_elements_entry.get(), define_name_entry.get()), width=20, height=0, background="gray90")
    button5.grid(column=1, row=4, pady=20)
# -----------------------------------------------Matrix managing---------------------------------
    manage_name_label = tkinter.Label(framelist[1], textvariable=tkinter.StringVar(
        framelist[1], "Name:"), fg="black", bg="gray90", width=8)
    manage_name_label.grid(row=0, column=0, pady=5, sticky="w")

    manage_name_entry = tkinter.Entry(framelist[1], width=35)
    manage_name_entry.grid(row=0, column=1)

    manage_name_button = tkinter.Button(framelist[1], text="Display the matrix", command=lambda: matrix_display(
        manage_name_entry.get()), width=20, height=0, background="gray90")
    manage_name_button.grid(row=1, column=1, pady=20, sticky="w")

    manage_trans_button = tkinter.Button(framelist[1], text="Transpose the matrix", command=lambda: transp_button(
        manage_name_entry.get()), width=20, height=0, background="gray90")
    manage_trans_button.grid(row=2, column=1, pady=20, sticky="w")
# -----------------------------------------------Two matrix operations-------------------------------------
    op_name1_label = tkinter.Label(framelist[2], textvariable=tkinter.StringVar(
        framelist[2], "First matrix:"), fg="black", bg="gray90", width=14)
    op_name1_label.grid(row=0, column=0, pady=5, sticky="w")

    op_name1_entry = tkinter.Entry(framelist[2], width=30)
    op_name1_entry.grid(row=0, column=1, pady=5, sticky="w", columnspan=3)

    op_name2_label = tkinter.Label(framelist[2], textvariable=tkinter.StringVar(
        framelist[2], "Matrix/scalar:"), fg="black", bg="gray90", width=14)
    op_name2_label.grid(row=1, column=0, sticky="w")

    op_name2_entry = tkinter.Entry(framelist[2], width=30)
    op_name2_entry.grid(row=1, column=1, sticky="w", columnspan=3)

    op_namenew_label = tkinter.Label(framelist[2], textvariable=tkinter.StringVar(
        framelist[2], "New matrix name:"), fg="black", bg="gray90", width=15)
    op_namenew_label.grid(row=2, column=0, pady=5, sticky="w")

    op_namenew_entry = tkinter.Entry(framelist[2], width=30)
    op_namenew_entry.grid(row=2, column=1, pady=5, sticky="w", columnspan=3)

    addition_button = tkinter.Button(framelist[2], text="Add the matrices", command=lambda: matrix_operations(
        matrices[op_name1_entry.get()], matrices[op_name2_entry.get()], op_namenew_entry.get(), 0), width=25,background="gray90")
    addition_button.grid(row=3, column=1, sticky="w", pady=5)

    subtraction_button = tkinter.Button(framelist[2], text="Subtract the matrices", command=lambda: matrix_operations(
        matrices[op_name1_entry.get()], matrices[op_name2_entry.get()], op_namenew_entry.get(), 1), width=25,   background="gray90")
    subtraction_button.grid(row=4, column=1, sticky="w")

    multplication_button = tkinter.Button(framelist[2], text="Multiply the matrices", command=lambda: matrix_operations(
        matrices[op_name1_entry.get()], matrices[op_name2_entry.get()], op_namenew_entry.get(), 2), width=25, background="gray90")
    multplication_button.grid(row=5, column=1, sticky="w", pady=5)

    scalar_button = tkinter.Button(framelist[2], text="Multiply the matrix by a scalar", command=lambda: matrix_operations(
        matrices[op_name1_entry.get()], float(op_name2_entry.get()), op_namenew_entry.get(), 3), width=25, background="gray90")
    scalar_button.grid(row=6, column=1, sticky="w")


def Image_calc_open(): #Function respinsible for image editor window
    def imageopen(): 
        
        nonlocal im
        path=filedialog.askopenfilename()
        a=Image.open(path)
        im=image_to_matrix(a)
        
        updatedimensions()
        future_memory.clear()
        past_memory.clear()
        
    def imagedisplay():
        if im == 0:
            tkinter.messagebox.showwarning("Action failed", "No image has been loaded")
            return
        matrix_to_image(im, "png").show("Your image")
        
    def updatedimensions():
            oldvar.set(str(len(im))+" x "+str(len(im[0])))
            newvar.set(str(len(im[0]))+" x "+str(len(im)))
    
    def frameopen(event):  # function that allows to change interface frames
        nonlocal opts
        nonlocal frame        
        a=framelist[opts[choicebox.get()][0]]        
        if frame != "":
            frame.grid_forget()
        a.grid(column=0, row=3, columnspan=3)
        frame = a

        
    def undo(direction):
        nonlocal im
        if direction=="b" and past_memory!=[]:
            future_memory.append(im)
            im=past_memory.pop()
        elif direction=="f" and future_memory!=[]:
            past_memory.append(im)
            im=future_memory.pop()
        if im !=0:  
            updatedimensions()
        
        
    def apply():
        
        nonlocal frame
        if frame !="":
        
            nonlocal im
            if im ==0:
                tkinter.messagebox.showwarning("Action failed", "No image has been loaded")
                return          
            past_memory.append(im)
            im=opts[choicebox.get()][1]()
            updatedimensions()
            future_memory.clear()

        
        
    def imagesave():
        nonlocal im
        if im ==0:
            tkinter.messagebox.showwarning("Action failed", "No image has been loaded")
            return     
        path=filedialog.asksaveasfilename(filetypes=[("JPG file", "*.jpg"),("PNG file","*.png")],defaultextension=".jpg")
        if path.endswith(".png"):
            matrix_to_image(im, "png").save(path)
        if path.endswith(".jpg"):
            matrix_to_image(im, "jpg").save(path)      
            
    x=""
    y=""      
    im = 0 #variable that stores the current image
    frame = "" #variable that indicates the current window layout
    past_memory=[]
    future_memory=[]
    #a dictionary to choose the function of the apply button
    opts={"Scale":(0, lambda:scale_matrix(im, float(img_scalarx_entry.get()), float(img_scalary_entry.get()), scalechoicebox.get(), scaleinterchoicebox.get())),
          "Skew":(1,lambda:skew_matrix(im, float(img_skewx_entry.get()), float(img_skewy_entry.get()),skewinterchoicebox.get())),
          "Rotate":(2, lambda:rotate_matrix(im, float(img_angle_entry.get()), rotinterchoicebox.get())),
          "Transpose":(3, lambda:matrix_transpose(im)), 
          "Adjust color":(4, lambda:color_matrix(im,sliderR.get(), sliderG.get(), sliderB.get()))}
    
    imagecalc = tkinter.Toplevel()
    imagecalc.title("Image editor")
    imagecalc.geometry("640x420")
    imagecalc.config(bg="gray90")
    imagecalc.resizable(True,False)
   
    framelist = [tkinter.Frame(imagecalc, background="gray90", width=200, height=200), tkinter.Frame(imagecalc, background="gray90", width=200, height=200), tkinter.Frame(imagecalc, background="gray90", width=200, height=200), tkinter.Frame(
        imagecalc, background="gray90", width=200, height=200), tkinter.Frame(imagecalc, background="gray90", width=200, height=200), tkinter.Frame(imagecalc, background="gray90", width=200, height=200)]
    imagecalc.rowconfigure(3, weight=1) 

    applybutton=tkinter.Button(imagecalc, text="Apply",command=lambda:apply(), width=12, height=0,background="gray80")
    applybutton.grid(column=2,row=4, pady=10, padx=30, sticky="s")
    
    button1=tkinter.Button(imagecalc,text="Open an \n image", command=lambda:imageopen(), width=12, height=0,background="gray80")
    button1.grid(column=0,row=0, pady=10, padx=30)

    button2=tkinter.Button(imagecalc, text="Display the \nimage", command=lambda:imagedisplay(), width=12, height=0,background="gray80")
    button2.grid(column=1,row=0, pady=10, padx=80)

    button3=tkinter.Button(imagecalc, text="Save the\n image",command=lambda:imagesave(), width=12, height=0,background="gray80")
    button3.grid(column=2,row=0, pady=10, padx=30)
    
    l1=tkinter.Canvas(imagecalc, width=520, height=4, bg="gray90", highlightthickness=0)
    l1.create_line(20,1,2000,1, width=1,fil="gray60")
    l1.grid(column=0, row=2, columnspan=3, sticky="", pady=10,padx=20)
    
    choicebox_label = tkinter.Label(imagecalc, textvariable=tkinter.StringVar(
        imagecalc, "Type of transformation:"), fg="black", bg="gray90", width=20)
    choicebox_label.grid(row=1, column=0, columnspan=1, sticky="e", padx=20)
    
    choicebox=ttk.Combobox(imagecalc, width=20,state="readonly", values=["Scale", "Skew", "Rotate", "Transpose", "Adjust color"])
    choicebox.grid(column=1, row=1, sticky="w", pady=5,columnspan=2, padx=0)
    choicebox.bind("<<ComboboxSelected>>", frameopen)
   
    
    button4=tkinter.Button(imagecalc, text="Undo",command=lambda:undo("b"), width=7, height=0,background="gray80")
    button4.grid(column=2,row=1, pady=10,padx=6,sticky="w")
    
    button5=tkinter.Button(imagecalc, text="Redo",command=lambda:undo("f"), width=7, height=0,background="gray80")
    button5.grid(column=2,row=1, pady=10, padx=6, sticky="e")
    # -------------------------------------------------Image scaling window----------------------------------

    img_scalarx_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
    framelist[0], "X factor:"), fg="black", bg="gray90", width=7)
    img_scalarx_label.grid(row=0, column=0)
    
    img_scalarx_entry = tkinter.Entry(framelist[0])
    img_scalarx_entry.grid(row=0, column=1)

    img_scalary_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
    framelist[0], "Y factor:"), fg="black", bg="gray90", width=7)
    img_scalary_label.grid(row=1, column=0)

    img_scalary_entry = tkinter.Entry(framelist[0])
    img_scalary_entry.grid(row=1, column=1, pady=20)

    
    scalechoicebox=ttk.Combobox(framelist[0], width=15, state="readonly",values=["set dimensions", "set coefficients"])
    scalechoicebox.grid(column=2, row=1, padx=20)
    scalechoicebox.current(0)
    
    img_interpolation_label = tkinter.Label(framelist[0], textvariable=tkinter.StringVar(
    framelist[0], "Interpolation:"), fg="black", bg="gray90", width=15)
    img_interpolation_label.grid(row=2, column=0)

    
    scaleinterchoicebox=ttk.Combobox(framelist[0], width=17, state="readonly",values=["nearest neighbor", "bilinear"])
    scaleinterchoicebox.grid(column=1, row=2,sticky="e")
    scaleinterchoicebox.current(0)
# ------------------------------------------------Image skewing window--------------------------------


    img_skewy_label = tkinter.Label(framelist[1], textvariable=tkinter.StringVar(
        framelist[1], "Y factor:"), fg="black", bg="gray90", width=7)
    img_skewy_label.grid(row=0, column=0, sticky="")

    img_skewy_entry = tkinter.Entry(framelist[1])
    img_skewy_entry.grid(row=0, column=1)

    img_skewx_label = tkinter.Label(framelist[1], textvariable=tkinter.StringVar(
        framelist[1], "X factor:"), fg="black", bg="gray90", width=7)
    img_skewx_label.grid(row=1, column=0, sticky="")

    img_skewx_entry = tkinter.Entry(framelist[1])
    img_skewx_entry.grid(row=1, column=1, pady=20)
    
    
    skewinterchoicebox=ttk.Combobox(framelist[1], width=17, state="readonly",values=["nearest neighbor", "bilinear"])
    skewinterchoicebox.grid(column=1, row=2,sticky="")
    skewinterchoicebox.current(0)
    
    img_interpolation_label2 = tkinter.Label(framelist[1], textvariable=tkinter.StringVar(
    framelist[1], "Interpolation:"), fg="black", bg="gray90", width=15)
    img_interpolation_label2.grid(row=2, column=0)


# -------------------------------------------------Image rotate window-------------------------------
    img_angle_label = tkinter.Label(framelist[2], textvariable=tkinter.StringVar(
        framelist[2], "Angle:"), fg="black", bg="gray90", width=5)
    img_angle_label.grid(row=0, column=0, sticky="")

    img_angle_entry = tkinter.Entry(framelist[2])
    img_angle_entry.grid(row=0, column=1)
    
        
    rotinterchoicebox=ttk.Combobox(framelist[2], width=17, state="readonly",values=["nearest neighbor", "bilinear"])
    rotinterchoicebox.grid(column=1, row=1,sticky="")
    rotinterchoicebox.current(0)
    
    img_interpolation_label3 = tkinter.Label(framelist[2], textvariable=tkinter.StringVar(
    framelist[2], "Interpolation:"), fg="black", bg="gray90", width=15)
    img_interpolation_label3.grid(row=1, column=0,pady=20)

# -----------------------------------------------Image recolor--------------------------------
    
    def slidetoentry(slider, entry, color):
        slider.configure(troughcolor='#%02x%02x%02x' % color)
        entry.set(slider.get())
        
    sliderR=tkinter.Scale(framelist[4], from_=-1, to=1,resolution=0.01, orient="horizontal",  showvalue=0, command=lambda a :slidetoentry(sliderR, varR,(int(128+127*sliderR.get()),0,0) ), length=200, bd=0, troughcolor="#800000")
    sliderR.grid(row=0,column=0)
    
    sliderG=tkinter.Scale(framelist[4], from_=-1, to=1,resolution=0.01, orient="horizontal", showvalue=0, command=lambda a :slidetoentry(sliderG, varG,(0,int(128+127*sliderG.get()),0)), length=200,bd=0,troughcolor="#008000" )
    sliderG.grid(row=1,column=0,pady=30)
    
    sliderB=tkinter.Scale(framelist[4], from_=-1, to=1,resolution=0.01, orient="horizontal", showvalue=0, command=lambda a :slidetoentry(sliderB, varB,(0,0,int(128+127*sliderB.get()))), length=200,bd=0,troughcolor="#000080")
    sliderB.grid(row=2,column=0)
    
    sliderR.set(0)
    sliderG.set(0)
    sliderB.set(0)
    
    varR=tkinter.StringVar(framelist[4], "")
    varG=tkinter.StringVar(framelist[4], "")
    varB=tkinter.StringVar(framelist[4], "") 
    
    varR.trace('w', lambda a,b,c: sliderR.set(float(varR.get()))) 
    varG.trace('w', lambda a,b,c: sliderG.set(float(varG.get())))
    varB.trace('w', lambda a,b,c: sliderB.set(float(varB.get())))
    
    entryR=tkinter.Entry(framelist[4], textvariable=varR)
    entryR.grid(row=0, column=2, padx=20)
    
    entryG=tkinter.Entry(framelist[4], textvariable=varG)
    entryG.grid(row=1, column=2, padx=20)
    
    entryB=tkinter.Entry(framelist[4], textvariable=varB)
    entryB.grid(row=2, column=2, padx=20)
    
#-------------------------------------------------Image transpose-------------------------
    img_tr_label = tkinter.Label(framelist[3], textvariable=tkinter.StringVar(
        framelist[3], "Current dimensions:"), fg="black", bg="gray90", width=20)
    img_tr_label.grid(row=0, column=0)
        
    img_tr_label = tkinter.Label(framelist[3], textvariable=tkinter.StringVar(
        framelist[3], "Transposed dimensions:"), fg="black", bg="gray90", width=20)
    img_tr_label.grid(row=1, column=0)
    
    oldvar=tkinter.StringVar(framelist[3])
    newvar=tkinter.StringVar(framelist[3])
    
    Old_entry = tkinter.Entry(framelist[3], textvariable=oldvar,state="readonly",readonlybackground="white")
    Old_entry.grid(row=0, column=1,sticky="w")

    New_entry = tkinter.Entry(framelist[3],textvariable=newvar,state="readonly", readonlybackground="white")
    New_entry.grid(row=1, column=1,pady=20,sticky="w")
    
main = tkinter.Tk()
main.geometry("400x240")
main.title("Matrix&Image editor")
main.resizable(True,False)
button = tkinter.Button(main, command=Matrix_calc_open, width=14,
                        height=5, background="gray80", text="open the \n matrix calculator")
button.grid(row=1, column=1, padx=50, pady=50)

button = tkinter.Button(main, command=Image_calc_open, width=14,
                        height=5, background="gray80", text="open the \n image calculator")
button.grid(row=1, column=2, pady=70)

main.mainloop()
