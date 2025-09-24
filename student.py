# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2


# class Student:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Students")

#         #variables
#         self.var_dep=StringVar()
#         self.var_course=StringVar()
#         self.var_year=StringVar()
#         self.var_sem=StringVar()
#         self.var_stdID=StringVar()
#         self.var_stdName=StringVar()
#         self.var_div=StringVar()
#         self.var_rollNO=StringVar()
#         self.var_gender=StringVar()
#         self.var_DOB=StringVar()
#         self.var_email=StringVar()
#         self.var_phNO=StringVar()
#         self.var_address=StringVar()
#         self.var_teacher=StringVar()
#         self.var_photo=StringVar()

#         #first image
#         img1=Image.open(r".\Images\img1.jpg")
#         img1=img1.resize((500,130),Image.Resampling.LANCZOS)
#         self.photoimg1=ImageTk.PhotoImage(img1)
#         first_lbl=Label(self.root,image=self.photoimg1)
#         first_lbl.place(x=0,y=0,width=500,height=130)



#         #second image
#         img2=Image.open(r".\Images\img2.jpg")
#         img2=img2.resize((500,130),Image.Resampling.LANCZOS)
#         self.photoimg2=ImageTk.PhotoImage(img2)
#         first_lbl=Label(self.root,image=self.photoimg2)
#         first_lbl.place(x=500,y=0,width=500,height=130)



#         #third image
#         img3=Image.open(r".\Images\img3.jpg")
#         img3=img3.resize((500,130),Image.Resampling.LANCZOS)
#         self.photoimg3=ImageTk.PhotoImage(img3)
#         first_lbl=Label(self.root,image=self.photoimg3)
#         first_lbl.place(x=1000,y=0,width=500,height=130)

#         #background image
#         img4=Image.open(r".\Images\background_img.jpg")
#         img4=img4.resize((1500,790),Image.Resampling.LANCZOS)
#         self.photoimg4=ImageTk.PhotoImage(img4)
#         bg_img=Label(self.root,image=self.photoimg4)
#         bg_img.place(x=0,y=130,width=1500,height=790)
#         title_lbl=Label(bg_img,text="Students Management System",font=("Times New Roman",40,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1530,height=55)

#         main_frame=Frame(bg_img,bd=2)
#         main_frame.place(x=20,y=80,width=1450,height=680)

#         #left frame
#         left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
#         left_frame.place(x=10,y=10,width=700,height=640)
#         img_lf=Image.open(r".\Images\leftFrame_img.jpg")
#         img_lf=img_lf.resize((720,150),Image.Resampling.LANCZOS)
#         self.photoimg_lf=ImageTk.PhotoImage(img_lf)
#         first_lbl=Label(left_frame,image=self.photoimg_lf)
#         first_lbl.place(x=10,y=5,width=680,height=130)
#         #current course
#         subFrame_lf=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
#         subFrame_lf.place(x=10,y=160,width=680,height=120)

#         #department
#         dep_label=Label(subFrame_lf,text="Department",font=("times new roman",12,"bold"),bg="white")
#         dep_label.grid(row=0,column=0,padx=10)

#         dep_combo=ttk.Combobox(subFrame_lf,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=17,state="readonly")
#         dep_combo["values"]=("Select Department","Computer Science","Information Technology","Civil","Chemical")
#         dep_combo.current(0)
#         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#         #course
#         cor_label=Label(subFrame_lf,text="Course",font=("times new roman",12,"bold"),bg="white")
#         cor_label.grid(row=0,column=2,padx=10)
        
#         cor_combo=ttk.Combobox(subFrame_lf,textvariable=self.var_course,font=("times new roman",10,"bold"),width=17,state="readonly")
#         cor_combo["values"]=("Select Course","OOPS","DSA","DBMS","CGA")
#         cor_combo.current(0)
#         cor_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#         #year
#         yr_label=Label(subFrame_lf,text="Year",font=("times new roman",12,"bold"),bg="white")
#         yr_label.grid(row=1,column=0,padx=10)
        
#         yr_combo=ttk.Combobox(subFrame_lf,textvariable=self.var_year,font=("times new roman",10,"bold"),width=17,state="readonly")
#         yr_combo["values"]=("Select Year","first","second","third","fourth")
#         yr_combo.current(0)
#         yr_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#         #semester
#         sem_label=Label(subFrame_lf,text="Semester",font=("times new roman",12,"bold"),bg="white")
#         sem_label.grid(row=1,column=2,padx=10)
        
#         sem_combo=ttk.Combobox(subFrame_lf,textvariable=self.var_sem,font=("times new roman",10,"bold"),width=17,state="readonly")
#         sem_combo["values"]=("Select Semester","first","second","third","fourth","fifth","sixth","seventh","eighth")
#         sem_combo.current(0)
#         sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#         #class student information
#         class_stu_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
#         class_stu_frame.place(x=10,y=300,width=680,height=310)

#         #studentID
#         Student_id_label=Label(class_stu_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
#         Student_id_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)
#         Student_id_entry=ttk.Entry(class_stu_frame,textvariable=self.var_stdID,width=20,font=("times new roman",12,"bold"))
#         Student_id_entry.grid(row=0,column=1,padx=7,pady=5,sticky=W)

#         #student name
#         stuName_label=Label(class_stu_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
#         stuName_label.grid(row=0,column=2,padx=7,pady=5,sticky=W)
#         stuName_entry=ttk.Entry(class_stu_frame,textvariable=self.var_stdName,width=20,font=("times new roman",12,"bold"))
#         stuName_entry.grid(row=0,column=3,padx=7,pady=5,sticky=W)

#         #class division
#         classDiv_label=Label(class_stu_frame,text="class Division",font=("times new roman",12,"bold"),bg="white")
#         classDiv_label.grid(row=1,column=0,padx=7,pady=5,sticky=W)
#         # classDiv_entry=ttk.Entry(class_stu_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
#         # classDiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
#         division_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),width=17,state="readonly")
#         division_combo["values"]=("Select Division","A","B","C","D")
#         division_combo.current(0)
#         division_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#         #Roll Number
#         RollNo_label=Label(class_stu_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
#         RollNo_label.grid(row=1,column=2,padx=7,pady=5,sticky=W)
#         RollNo_entry=ttk.Entry(class_stu_frame,textvariable=self.var_rollNO,width=20,font=("times new roman",12,"bold"))
#         RollNo_entry.grid(row=1,column=3,padx=7,pady=5,sticky=W)

#         #Gender
#         Gender_label=Label(class_stu_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
#         Gender_label.grid(row=2,column=0,padx=7,pady=5,sticky=W)
#         # Gender_entry=ttk.Entry(class_stu_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
#         # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
#         gender_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17,state="readonly")
#         gender_combo["values"]=("Select Gender","Male","Female","Other")
#         gender_combo.current(0)
#         gender_combo.grid(row=2,column=1,padx=2,pady=15,sticky=W)

#         #Date of Birth
#         DOB_label=Label(class_stu_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
#         DOB_label.grid(row=2,column=2,padx=7,pady=5,sticky=W)
#         DOB_entry=ttk.Entry(class_stu_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
#         DOB_entry.grid(row=2,column=3,padx=7,pady=5,sticky=W)

#         #email Id
#         email_label=Label(class_stu_frame,text="Email ID",font=("times new roman",12,"bold"),bg="white")
#         email_label.grid(row=3,column=0,padx=7,pady=5,sticky=W)
#         email_entry=ttk.Entry(class_stu_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
#         email_entry.grid(row=3,column=1,padx=7,pady=5,sticky=W)

#         #Phone Number
#         PhNo_label=Label(class_stu_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
#         PhNo_label.grid(row=3,column=2,padx=7,pady=5,sticky=W)
#         PhNo_entry=ttk.Entry(class_stu_frame,textvariable=self.var_phNO,width=20,font=("times new roman",12,"bold"))
#         PhNo_entry.grid(row=3,column=3,padx=7,pady=5,sticky=W)

#         #Address
#         address_label=Label(class_stu_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
#         address_label.grid(row=4,column=0,padx=7,pady=5,sticky=W)
#         address_entry=ttk.Entry(class_stu_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
#         address_entry.grid(row=4,column=1,padx=7,pady=5,sticky=W)

#         #Teacher Name
#         teacher_label=Label(class_stu_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
#         teacher_label.grid(row=4,column=2,padx=7,pady=5,sticky=W)
#         teacher_entry=ttk.Entry(class_stu_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
#         teacher_entry.grid(row=4,column=3,padx=7,pady=5,sticky=W)

#         #radio buttons for photo sample
#         self.var_photo=StringVar()
#         radioBtn1=ttk.Radiobutton(class_stu_frame,variable=self.var_photo,text="Take photo sample",value="YES")
#         radioBtn1.grid(row=5,column=0)

#         radioBtn2=ttk.Radiobutton(class_stu_frame,variable=self.var_photo,text="No photo sample",value="NO")
#         radioBtn2.grid(row=5,column=1)

#         #Button frame1
#         btn_frame1=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
#         btn_frame1.place(x=5,y=220,width=650,height=40)

#         save_btn=Button(btn_frame1,text="Save",command=self.add_data,width=22,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         save_btn.grid(row=0,column=0)

#         update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=22,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         update_btn.grid(row=0,column=1)

#         delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,width=22,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         delete_btn.grid(row=0,column=2)

#         reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=22,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         reset_btn.grid(row=0,column=3)

#         #button frame2
#         btn_frame2=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
#         btn_frame2.place(x=5,y=248,width=650,height=27)

#         TakePhoto_btn=Button(btn_frame2,text="Take photo Sample",command=self.generate_dataset,width=46,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         TakePhoto_btn.grid(row=0,column=0)

#         updatePhoto_btn=Button(btn_frame2,text="Update photo Sample",width=46,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         updatePhoto_btn.grid(row=0,column=1)




#         #right frame
#         right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
#         right_frame.place(x=730,y=10,width=700,height=640)

#         img_rf=Image.open(r".\Images\leftFrame_img.jpg")
#         img_rf=img_rf.resize((720,150),Image.Resampling.LANCZOS)
#         self.photoimg_rf=ImageTk.PhotoImage(img_rf)
#         first_lbl=Label(right_frame,image=self.photoimg_rf)
#         first_lbl.place(x=10,y=5,width=680,height=130)

#         #search system
#         search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
#         search_frame.place(x=5,y=135,width=685,height=70)

#         search_label=Label(search_frame,text="Search by : ",font=("times new roman",13,"bold"),bg="white",fg="black")
#         search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

#         search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
#         search_combo["values"]=("Select","Roll_No","Phone_No")
#         search_combo.current(0)
#         search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#         search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
#         search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

#         search_btn=Button(search_frame,text="Search",width=15,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         search_btn.grid(row=0,column=3,padx=5,pady=5,sticky=W)

#         showAll_btn=Button(search_frame,text="Show All",width=15,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         showAll_btn.grid(row=0,column=4,padx=5,pady=5,sticky=W)

#         #Table frame
#         table_frame=Frame(right_frame,bd=2,relief=RIDGE)
#         table_frame.place(x=5,y=210,width=685,height=400)
#         #scroll bars
#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

#         self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","name","div","rollNO","gender","DOB","email","phNO","address","teacherName","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)

#         self.student_table.heading("dep",text="Department")
#         self.student_table.heading("course",text="Course")
#         self.student_table.heading("year",text="Year")
#         self.student_table.heading("sem",text="Semester")
#         self.student_table.heading("ID",text="Student ID")
#         self.student_table.heading("name",text="Name")
#         self.student_table.heading("div",text="Division")
#         self.student_table.heading("rollNO",text="Roll number")
#         self.student_table.heading("gender",text="Gender")
#         self.student_table.heading("DOB",text="Date of Birth")
#         self.student_table.heading("email",text="Email ID")
#         self.student_table.heading("phNO",text="Phone Number")
#         self.student_table.heading("address",text="Address")
#         self.student_table.heading("teacherName",text="Teacher's Name")
#         self.student_table.heading("photo",text="Photo sample status")
#         self.student_table["show"]="headings"

#         self.student_table.column("dep",width=100)
#         self.student_table.column("course",width=100)
#         self.student_table.column("year",width=100)
#         self.student_table.column("sem",width=100)
#         self.student_table.column("ID",width=100)
#         self.student_table.column("name",width=100)
#         self.student_table.column("div",width=100)
#         self.student_table.column("rollNO",width=100)
#         self.student_table.column("gender",width=100)
#         self.student_table.column("DOB",width=100)
#         self.student_table.column("email",width=100)
#         self.student_table.column("phNO",width=100)
#         self.student_table.column("address",width=100)
#         self.student_table.column("teacherName",width=100)
#         self.student_table.column("photo",width=100)

#         self.student_table.pack(fill=BOTH,expand=1)
#         self.student_table.bind("<ButtonRelease>",self.get_cursor)
#         self.fetch_data()



#     #function for inserting data into database

#     def add_data(self):
#         if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdID.get()=="":
#             messagebox.showerror("ERROR","All fields are Required",parent=self.root)
#         else:
#             try:
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#                 my_cursor=conn.cursor()
#                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
#                                                                                                             self.var_dep.get(),
#                                                                                                             self.var_course.get(),
#                                                                                                             self.var_year.get(),
#                                                                                                             self.var_sem.get(),
#                                                                                                             self.var_stdID.get(),
#                                                                                                             self.var_stdName.get(),
#                                                                                                             self.var_div.get(),
#                                                                                                             self.var_rollNO.get(),
#                                                                                                             self.var_gender.get(),
#                                                                                                             self.var_DOB.get(),
#                                                                                                             self.var_email.get(),
#                                                                                                             self.var_phNO.get(),
#                                                                                                             self.var_address.get(),
#                                                                                                             self.var_teacher.get(),
#                                                                                                             self.var_photo.get()
#                                                                                                         ))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("SUCCESS","Student details have been added successfully",parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("ERROR",f"Due to : {str(es)}",parent=self.root)


#     # function for fetching data from database and showing on app
#     def fetch_data(self):
#         conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#         my_cursor=conn.cursor()
#         my_cursor.execute("select * from student")
#         data=my_cursor.fetchall()

#         if len(data)!=0:
#             self.student_table.delete(*self.student_table.get_children())
#             for i in data:
#                 self.student_table.insert("",END,values=i)
#             conn.commit()
#         conn.close()


#     #function for getting cursor
#     def get_cursor(self,event=""):
#         cursor_focus=self.student_table.focus()
#         content=self.student_table.item(cursor_focus)
#         data=content["values"]

#         self.var_dep.set(data[0]),
#         self.var_course.set(data[1]),
#         self.var_year.set(data[2]),
#         self.var_sem.set(data[3]),
#         self.var_stdID.set(data[4]),
#         self.var_stdName.set(data[5]),
#         self.var_div.set(data[6]),
#         self.var_rollNO.set(data[7]),
#         self.var_gender.set(data[8]),
#         self.var_DOB.set(data[9]),
#         self.var_email.set(data[10]),
#         self.var_phNO.set(data[11]),
#         self.var_address.set(data[12]),
#         self.var_teacher.set(data[13]),
#         self.var_photo.set(data[14])



#     #update function
#     def update_data(self):
#         if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdID.get()=="":
#             messagebox.showerror("ERROR","All fields are Required",parent=self.root)
#         else:
#             try:
#                 update=messagebox.askyesno("UPDATE","Do you want to update student details",parent=self.root)
#                 if update>0:
#                     conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#                     my_cursor=conn.cursor()
#                     my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,gender=%s,DOB=%s,email=%s,phNO=%s,address=%s,teacher=%s,photo=%s WHERE Student_id=%s",(
#                                                                                                                                                                                                       self.var_dep.get(),
#                                                                                                                                                                                                        self.var_course.get(),
#                                                                                                                                                                                                         self.var_year.get(),
#                                                                                                                                                                                                         self.var_sem.get(),
#                                                                                                                                                                                                         self.var_stdName.get(),
#                                                                                                                                                                                                         self.var_div.get(),
#                                                                                                                                                                                                         self.var_rollNO.get(),
#                                                                                                                                                                                                         self.var_gender.get(),
#                                                                                                                                                                                                         self.var_DOB.get(),
#                                                                                                                                                                                                         self.var_email.get(),
#                                                                                                                                                                                                         self.var_phNO.get(),
#                                                                                                                                                                                                         self.var_address.get(),
#                                                                                                                                                                                                         self.var_teacher.get(),
#                                                                                                                                                                                                         self.var_photo.get(),
#                                                                                                                                                                                                         self.var_stdID.get()
#                                                                                         ))
#                 else:
#                     if not update:
#                         return
#                 messagebox.showinfo("SUCCESS","Student details successfully updated",parent=self.root)
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()

#             except Exception as es:
#                 messagebox.showerror("ERROR",f"Due to : {str(es)}",parent=self.root)


#     #delete function
#     def delete_data(self):
#         if self.var_stdID.get()=="":
#             messagebox.showerror("ERROR","Student ID is required",parent=self.root)
#         else:
#             try:
#                 delete=messagebox.askyesno("CONFIRMATION","Do you want to delete this record?")
#                 if delete>0:
#                     conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#                     my_cursor=conn.cursor()
#                     sql="DELETE FROM student WHERE Student_id=%s"
#                     val=(self.var_stdID.get(),)
#                     my_cursor.execute(sql,val)
#                 else:
#                     if not delete:
#                         return
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("DELETED","Record successfully deleted",parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("ERROR",f"Due to : {str(es)}",parent=self.root)


#     #reset function
#     def reset_data(self):
#         self.var_dep.set("Select Department"),
#         self.var_course.set("Select Course"),
#         self.var_year.set("Select Year"),
#         self.var_sem.set("Select Semester"),
#         self.var_stdID.set(""),
#         self.var_stdName.set(""),
#         self.var_div.set("Select Division"),
#         self.var_rollNO.set(""),
#         self.var_gender.set("Select Gender"),
#         self.var_DOB.set(""),
#         self.var_email.set(""),
#         self.var_phNO.set(""),
#         self.var_address.set(""),
#         self.var_teacher.set(""),
#         self.var_photo.set("")

#     #generate dataset or take photo samples
#     def generate_dataset(self):
#         if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdID.get()=="":
#             messagebox.showerror("ERROR","All fields are Required",parent=self.root)
#         else:
#             try:
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#                 my_cursor=conn.cursor()
#                 my_cursor.execute("SELECT * FROM student")
#                 myresult=my_cursor.fetchall()
#                 id=0
#                 for x in myresult:
#                     id+=1
#                 my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,gender=%s,DOB=%s,email=%s,phNO=%s,address=%s,teacher=%s,photo=%s WHERE Student_id=%s",(
#                                                                                                                                                                                                       self.var_dep.get(),
#                                                                                                                                                                                                        self.var_course.get(),
#                                                                                                                                                                                                         self.var_year.get(),
#                                                                                                                                                                                                         self.var_sem.get(),
#                                                                                                                                                                                                         self.var_stdName.get(),
#                                                                                                                                                                                                         self.var_div.get(),
#                                                                                                                                                                                                         self.var_rollNO.get(),
#                                                                                                                                                                                                         self.var_gender.get(),
#                                                                                                                                                                                                         self.var_DOB.get(),
#                                                                                                                                                                                                         self.var_email.get(),
#                                                                                                                                                                                                         self.var_phNO.get(),
#                                                                                                                                                                                                         self.var_address.get(),
#                                                                                                                                                                                                         self.var_teacher.get(),
#                                                                                                                                                                                                         self.var_photo.get(),
#                                                                                                                                                                                                         self.var_stdID.get()==id+1
#                                                                                         ))
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()

#                 #loading data samples from frontal_face openCV 
#                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#                 def face_cropped(img):
#                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #to convert bgr image in grey scale
#                     faces=face_classifier.detectMultiScale(gray,1.3,5)  #here scaling_factor=1.3 and minimum_neighbour=5

#                     for (x,y,w,h) in faces:  #w is width and h is height
#                         face_cropped=img[y:y+h,x:x+w]
#                         return face_cropped
                
#                 cap=cv2.VideoCapture(0)
#                 img_id=0
#                 while True:
#                     ret,img_frame=cap.read()
#                     if face_cropped(img_frame) is not None:
#                         img_id+=1
#                         face=cv2.resize(face_cropped(img_frame),(450,450))
#                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
#                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
#                         cv2.imwrite(file_name_path,face)
#                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                         cv2.imshow("Cropped face",face)

#                     if cv2.waitKey(1)==13 or int(img_id)==10:
#                         break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result","Generating dataset completed successfully")

#             except Exception as es:
#                 messagebox.showerror("ERROR",f"Due to : {str(es)}",parent=self.root)








# if __name__=="__main__":
#     root=Tk()
#     obj=Student(root)
#     root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox, Frame, Label, LabelFrame, Button, Radiobutton, HORIZONTAL, VERTICAL, BOTTOM, X, RIGHT, Y, W, BOTH, END, StringVar, E
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from ttkthemes import ThemedTk # Import ThemedTk

class Student:
    def __init__(self, root):
        self.root = root
        # Apply a theme using ThemedTk (passed from main app or created here)
        # If root is already a ThemedTk instance, this might not be needed,
        # but ttk.Style works on standard Tk roots too.
        style = ttk.Style(self.root)
        # try:
        #     # Choose a theme: 'arc', 'equilux', 'plastik', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
        #     selected_theme = "clam"  # <-- CHANGE THEME HERE
        #     self.root.set_theme(selected_theme)
        #     print(f"Using theme: {selected_theme}")
        # except tk.TclError:
        #     print("ttkthemes theme not found or Tcl error, using default ttk theme.")
        #     # Fallback ttk theme
        #     style.theme_use('clam') # Good fallback

        # self.root.title("Student Management System")
        # Apply a theme only if the root supports it
        if hasattr(self.root, "set_theme"):
            try:
                selected_theme = "clam"  # Change theme if needed
                self.root.set_theme(selected_theme)
                print(f"Using theme: {selected_theme}")
            except Exception as e:
                print(f"Error applying theme: {e}")
        else:
            print("Root does not support themes. Skipping theme application.")

        self.root.title("Student Management System")

        # Set minimum size and allow resizing
        min_width = 1200
        min_height = 700
        self.root.minsize(min_width, min_height)
        # Optional: Start maximized or centered
        # self.root.state('zoomed')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.85)
        initial_height = int(screen_height * 0.8)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")

        # --- Variables ---
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stdID = StringVar()
        self.var_stdName = StringVar()
        self.var_div = StringVar()
        self.var_rollNO = StringVar()
        self.var_gender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_phNO = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio = StringVar(value="No") # Default photo sample to No
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()

        # Store PhotoImage objects
        self.image_references = []

        # --- Configure root grid layout ---
        self.root.grid_columnconfigure(0, weight=1) # Main content column expands
        self.root.grid_rowconfigure(1, weight=1)    # Main content row expands

        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Header ---
        self.create_header()

        # --- Main Content Area ---
        main_frame = ttk.Frame(self.root, style="TFrame", padding=(10, 10))
        main_frame.grid(row=1, column=0, sticky="nsew")
        # Configure main_frame grid (e.g., 2 columns, 1 row, allow resizing)
        main_frame.grid_columnconfigure(0, weight=1, minsize=450) # Form area (adjust weight/minsize as needed)
        main_frame.grid_columnconfigure(1, weight=3) # Table area
        main_frame.grid_rowconfigure(0, weight=1)

        # --- Left Frame (Student Form) ---
        self.create_form_panel(main_frame)

        # --- Right Frame (Search & Table) ---
        self.create_table_panel(main_frame)

        # --- Initial data fetch ---
        self.fetch_data() # Load data into the table when the app starts


    def configure_styles(self, style):
        """Configure ttk styles for widgets."""
        primary_color = "#007bff"  # A modern blue
        secondary_color = "#6c757d" # Gray
        light_bg = style.lookup('TFrame', 'background') # Get theme's background
        header_bg = "#ffffff"
        text_color = style.lookup('TLabel', 'foreground') # Get theme's text color
        button_fg = "#ffffff"
        button_hover_bg = "#0056b3" # Darker blue on hover

        style.configure("Header.TFrame", background=header_bg)
        style.configure("Title.TLabel", background=header_bg, foreground=primary_color,
                        font=("Helvetica", 24, "bold"), anchor="center", padding=(0, 10))

        # General Frame style (uses theme background)
        style.configure("TFrame")
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TEntry", font=("Helvetica", 10), padding=(5, 5))
        style.configure("TCombobox", font=("Helvetica", 10), padding=(5, 5))
        style.configure("Header.TLabel", font=("Helvetica", 11, "bold")) # For LabelFrame text

        # Custom Button Style
        style.configure("Accent.TButton", font=("Helvetica", 10, "bold"),
                        foreground=button_fg, background=primary_color,
                        padding=(10, 5), borderwidth=0)
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', primary_color), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])

        # Style for Radiobuttons
        style.configure("TRadiobutton", font=("Helvetica", 10), background=light_bg)

        # Style Treeview
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", rowheight=25, font=("Helvetica", 9))


    def create_header(self):
        """Creates the header section."""
        header_frame = ttk.Frame(self.root, style="Header.TFrame", padding=(0, 0))
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)

        # --- Optional Single Banner Image ---
        try:
            img_banner = Image.open(r".\Images\background_img.jpg") # Create or choose a suitable banner
            banner_height = 70
            aspect_ratio = img_banner.width / img_banner.height
            banner_width = min(int(banner_height * aspect_ratio), self.root.winfo_screenwidth()) # Limit width
            img_banner = img_banner.resize((banner_width, banner_height), Image.Resampling.LANCZOS)
            self.photoimg_banner = ImageTk.PhotoImage(img_banner)
            self.image_references.append(self.photoimg_banner)
            # If using a banner, create a label for it here and grid it
            # banner_lbl = ttk.Label(header_frame, image=self.photoimg_banner)
            # banner_lbl.grid(row=0, column=0, pady=(0, 5), sticky='ew')
            # Adjust title row if banner is present
            title_row = 1
        except FileNotFoundError:
            print("Banner image not found (banner.jpg), using text title only.")
            title_row = 0
        except Exception as e:
            print(f"Error loading banner image: {e}")
            title_row = 0

        # --- Main Title ---
        title_lbl = ttk.Label(header_frame, text="Student Management System", style="Title.TLabel")
        title_lbl.grid(row=title_row, column=0, sticky="ew")

        # Separator
        sep = ttk.Separator(header_frame, orient='horizontal')
        sep.grid(row=title_row + 1, column=0, sticky='ew', pady=(5, 0))

    def _create_form_field(self, parent, row, col, label_text, variable, widget_type='entry', values=None, **kwargs):
        """Helper to create a label and an entry/combobox field."""
        label = ttk.Label(parent, text=label_text, style="TLabel")
        label.grid(row=row, column=col, padx=5, pady=5, sticky="w")

        col_span = kwargs.pop('colspan', 1) # Allow spanning columns

        if widget_type == 'combobox':
            widget = ttk.Combobox(parent, textvariable=variable, values=values, state="readonly", style="TCombobox", **kwargs)
            if values:
                widget.current(0) # Set default selection
        else: # Default to entry
            widget = ttk.Entry(parent, textvariable=variable, style="TEntry", **kwargs)

        widget.grid(row=row, column=col + 1, padx=5, pady=5, sticky="ew", columnspan=col_span)
        return widget

    def create_form_panel(self, parent):
        """Creates the left panel containing the student data form."""
        form_frame = ttk.LabelFrame(parent, text="Student Details", style="TLabelframe", padding=(15, 10))
        form_frame.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky="nsew")
        form_frame.grid_columnconfigure(1, weight=1) # Make entry column expandable
        form_frame.grid_columnconfigure(3, weight=1) # Make entry column expandable

        # Current Course Information Frame
        course_frame = ttk.LabelFrame(form_frame, text="Course Information", style="TLabelframe", padding=(10, 5))
        course_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="ew")
        course_frame.grid_columnconfigure(1, weight=1)
        course_frame.grid_columnconfigure(3, weight=1)

        self._create_form_field(course_frame, 0, 0, "Department:", self.var_dep, 'combobox', ("Select Department", "Computer Science", "Information Technology", "Civil", "Mechanical", "Electrical","Chemical"))
        self._create_form_field(course_frame, 0, 2, "Course:", self.var_course, 'combobox', ("Select Course", "B.Tech", "B.Sc", "BCA", "MCA", "M.Tech"))
        self._create_form_field(course_frame, 1, 0, "Year:", self.var_year, 'combobox', ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24","2024-25"))
        self._create_form_field(course_frame, 1, 2, "Semester:", self.var_sem, 'combobox', ("Select Semester", "Semester-1", "Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8"))

        # Class Student Information Frame
        student_frame = ttk.LabelFrame(form_frame, text="Student Information", style="TLabelframe", padding=(10, 5))
        student_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=10, sticky="ew")
        student_frame.grid_columnconfigure(1, weight=1)
        student_frame.grid_columnconfigure(3, weight=1)

        self._create_form_field(student_frame, 0, 0, "Student ID:", self.var_stdID)
        self._create_form_field(student_frame, 0, 2, "Student Name:", self.var_stdName)
        self._create_form_field(student_frame, 1, 0, "Division:", self.var_div, 'combobox', ("Select Division", "A", "B", "C"))
        self._create_form_field(student_frame, 1, 2, "Roll No:", self.var_rollNO)
        self._create_form_field(student_frame, 2, 0, "Gender:", self.var_gender, 'combobox', ("Select Gender", "Male", "Female", "Other"))
        self._create_form_field(student_frame, 2, 2, "DOB (YYYY-MM-DD):", self.var_DOB) # Added format hint
        self._create_form_field(student_frame, 3, 0, "Email:", self.var_email)
        self._create_form_field(student_frame, 3, 2, "Phone No:", self.var_phNO)
        self._create_form_field(student_frame, 4, 0, "Address:", self.var_address, colspan=3) # Span address entry
        self._create_form_field(student_frame, 5, 0, "Teacher Name:", self.var_teacher, colspan=3) # Span teacher entry

        # Radio Buttons Frame for Photo Sample
        radio_frame = ttk.Frame(student_frame)
        radio_frame.grid(row=6, column=0, columnspan=4, pady=(10, 5), sticky='w')
        radio_lbl = ttk.Label(radio_frame, text="Photo Sample Taken?")
        radio_lbl.pack(side=tk.LEFT, padx=(0, 10))
        radioBtn1 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="Yes", value="Yes")
        radioBtn1.pack(side=tk.LEFT, padx=5)
        radioBtn2 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="No", value="No")
        radioBtn2.pack(side=tk.LEFT, padx=5)


        # Button Frame
        btn_frame = ttk.Frame(form_frame, padding=(0, 10))
        btn_frame.grid(row=2, column=0, columnspan=4, pady=(15, 5), sticky="ew")
        # Configure button frame columns to distribute space
        btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)


        save_btn = ttk.Button(btn_frame, text="Save", command=self.add_data, style="Accent.TButton", width=12, cursor="hand2")
        save_btn.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        update_btn = ttk.Button(btn_frame, text="Update", command=self.update_data, style="Accent.TButton", width=12, cursor="hand2")
        update_btn.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_data, style="Accent.TButton", width=12, cursor="hand2")
        delete_btn.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

        reset_btn = ttk.Button(btn_frame, text="Reset", command=self.reset_data, style="Accent.TButton", width=12, cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

        # Photo Button Frame (Separate row for clarity)
        photo_btn_frame = ttk.Frame(form_frame, padding=(0, 5))
        photo_btn_frame.grid(row=3, column=0, columnspan=4, pady=(5, 5), sticky="ew")
        photo_btn_frame.grid_columnconfigure((0, 1), weight=1) # Distribute space

        takePhoto_btn = ttk.Button(photo_btn_frame, text="Take Photo Sample", command=self.generate_dataset, style="Accent.TButton", width=25, cursor="hand2")
        takePhoto_btn.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        updatePhoto_btn = ttk.Button(photo_btn_frame, text="Update Photo Sample", command=self.generate_dataset, style="Accent.TButton", width=25, cursor="hand2")
        updatePhoto_btn.grid(row=0, column=1, padx=5, pady=5, sticky='ew')


    def create_table_panel(self, parent):
        """Creates the right panel containing search and the student table."""
        table_frame_container = ttk.LabelFrame(parent, text="Student Records", style="TLabelframe", padding=(15, 10))
        table_frame_container.grid(row=0, column=1, padx=(10, 0), pady=(0, 10), sticky="nsew")
        table_frame_container.grid_rowconfigure(1, weight=1)    # Allow table row to expand
        table_frame_container.grid_columnconfigure(0, weight=1) # Allow content to expand width-wise

        # Search Frame
        search_frame = ttk.Frame(table_frame_container, padding=(0, 10))
        search_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        # Configure search frame columns
        search_frame.grid_columnconfigure(3, weight=1) # Allow entry to take space

        search_label = ttk.Label(search_frame, text="Search By:", style="TLabel")
        search_label.grid(row=0, column=0, padx=(0, 5), pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by,
                                    values=("Select", "Roll_No", "Phone_No", "Student_id", "Name"),
                                    state="readonly", width=12, style="TCombobox")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_text, width=20, style="TEntry")
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        search_btn = ttk.Button(search_frame, text="Search", command=self.search_data, style="Accent.TButton", width=10, cursor="hand2")
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=E) # Align right

        showAll_btn = ttk.Button(search_frame, text="Show All", command=self.fetch_data, style="Accent.TButton", width=10, cursor="hand2")
        showAll_btn.grid(row=0, column=4, padx=5, pady=5, sticky=E) # Align right

        # Table Frame (includes Treeview and Scrollbars)
        table_area = ttk.Frame(table_frame_container)
        table_area.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        table_area.grid_rowconfigure(0, weight=1)
        table_area.grid_columnconfigure(0, weight=1)

        # Scroll Bars
        scroll_x = ttk.Scrollbar(table_area, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_area, orient=VERTICAL)

        # Treeview Widget
        self.student_table = ttk.Treeview(
            table_area,
            columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            style="Treeview"
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Define Headings
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Status")

        # Hide the default first column (#0)
        self.student_table["show"] = "headings"

        # Set Column Widths (adjust as needed)
        col_width = 120
        for col in self.student_table["columns"]:
            self.student_table.column(col, width=col_width, minwidth=80, anchor=W)

        self.student_table.pack(fill=BOTH, expand=1)

        # Bind click event to populate form
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor) # Use ButtonRelease-1 for better compatibility


    # ================== Database Connection =====================
    def _db_connect(self):
        """Establishes and returns a database connection."""
        try:
            conn = mysql.connector.connect(
                host="localhost",         # Replace with your host if different
                username="root",          # Replace with your MySQL username
                password="Abhishri#@9875",    # Replace with your MySQL password
                database="face_recognition_system" # Replace with your DB name
            )
            return conn
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect to database: {err}", parent=self.root)
            return None

    # ================== CRUD Functions ==========================

    def add_data(self):
        """Adds student data to the database."""
        # Basic Validation
        if (self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or
            self.var_stdID.get() == "" or self.var_email.get() == "" or self.var_phNO.get() == ""):
            messagebox.showerror("Validation Error", "Department, Name, ID, Email, and Phone are required fields.", parent=self.root)
            return

        conn = None # Initialize connection variable
        try:
            conn = self._db_connect()
            if conn is None: return # Check if connection failed

            my_cursor = conn.cursor()
            sql = """INSERT INTO student (Dep, course, Year, Semester, Student_id, Name, Division, Roll, gender, DOB, email, phNO, address, teacher, photo)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                self.var_sem.get(), self.var_stdID.get(), self.var_stdName.get(),
                self.var_div.get(), self.var_rollNO.get(), self.var_gender.get(),
                self.var_DOB.get(), self.var_email.get(), self.var_phNO.get(),
                self.var_address.get(), self.var_teacher.get(), self.var_radio.get()
            )
            my_cursor.execute(sql, values)
            conn.commit()
            self.fetch_data() # Refresh table
            self.reset_data() # Clear form
            messagebox.showinfo("Success", "Student details added successfully.", parent=self.root)

        except mysql.connector.Error as err:
            # Check for duplicate entry specifically
            if err.errno == 1062: # Error code for duplicate entry
                 messagebox.showerror("Database Error", f"Student ID '{self.var_stdID.get()}' already exists.", parent=self.root)
            else:
                messagebox.showerror("Database Error", f"Error adding data: {err}", parent=self.root)
            if conn: conn.rollback() # Rollback on error
        except Exception as es:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
            if conn: conn.rollback()
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()


    def fetch_data(self):
        """Fetches all student data and populates the table."""
        conn = None
        try:
            conn = self._db_connect()
            if conn is None: return

            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Dep, course, Year, Semester, Student_id, Name, Division, Roll, gender, DOB, email, phNO, address, teacher, photo FROM student")
            data = my_cursor.fetchall()

            # Clear existing table data
            self.student_table.delete(*self.student_table.get_children())

            if data:
                for i in data:
                    # Ensure data alignment with columns
                    self.student_table.insert("", END, values=i)
            else:
                 # Optional: Show a message if no data
                 # messagebox.showinfo("Info", "No student records found.", parent=self.root)
                 pass


        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error fetching data: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()


    def get_cursor(self, event=""):
        """Populates form fields when a table row is clicked."""
        try:
            cursor_row = self.student_table.focus()
            if not cursor_row: # No row selected
                return
            content = self.student_table.item(cursor_row)
            data = content["values"]

            if data: # Ensure data is not empty
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_sem.set(data[3])
                self.var_stdID.set(data[4])
                self.var_stdName.set(data[5])
                self.var_div.set(data[6])
                self.var_rollNO.set(data[7])
                self.var_gender.set(data[8])
                self.var_DOB.set(data[9])
                self.var_email.set(data[10])
                self.var_phNO.set(data[11])
                self.var_address.set(data[12])
                self.var_teacher.set(data[13])
                self.var_radio.set(data[14])
        except IndexError:
             messagebox.showwarning("Selection Error", "Could not retrieve data for the selected row. Please try again.", parent=self.root)
        except Exception as es:
             messagebox.showerror("Error", f"An error occurred while getting cursor data: {str(es)}", parent=self.root)


    def update_data(self):
        """Updates selected student data in the database."""
         # Basic Validation
        if (self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or
            self.var_stdID.get() == "" or self.var_email.get() == "" or self.var_phNO.get() == ""):
            messagebox.showerror("Validation Error", "Department, Name, ID, Email, and Phone are required fields.", parent=self.root)
            return

        if not self.var_stdID.get():
             messagebox.showerror("Error", "Student ID is required to update.", parent=self.root)
             return

        if messagebox.askyesno("Confirm Update", "Do you want to update this student's details?", parent=self.root):
            conn = None
            try:
                conn = self._db_connect()
                if conn is None: return

                my_cursor = conn.cursor()
                sql = """UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,
                         Division=%s, Roll=%s, gender=%s, DOB=%s, email=%s, phNO=%s, address=%s,
                         teacher=%s, photo=%s WHERE Student_id=%s"""
                values = (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                    self.var_sem.get(), self.var_stdName.get(), self.var_div.get(),
                    self.var_rollNO.get(), self.var_gender.get(), self.var_DOB.get(),
                    self.var_email.get(), self.var_phNO.get(), self.var_address.get(),
                    self.var_teacher.get(), self.var_radio.get(), self.var_stdID.get()
                )
                my_cursor.execute(sql, values)

                if my_cursor.rowcount == 0:
                    messagebox.showwarning("Update Warning", f"No student found with ID '{self.var_stdID.get()}'. No changes made.", parent=self.root)
                else:
                    conn.commit()
                    messagebox.showinfo("Success", "Student details updated successfully.", parent=self.root)
                    self.fetch_data() # Refresh table
                    self.reset_data() # Clear form after successful update

            except mysql.connector.Error as err:
                 messagebox.showerror("Database Error", f"Error updating data: {err}", parent=self.root)
                 if conn: conn.rollback()
            except Exception as es:
                 messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
                 if conn: conn.rollback()
            finally:
                 if conn and conn.is_connected():
                     my_cursor.close()
                     conn.close()


    def delete_data(self):
        """Deletes the selected student record."""
        if not self.var_stdID.get():
            messagebox.showerror("Error", "Student ID is required to delete.", parent=self.root)
            return

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student ID {self.var_stdID.get()}?\nThis action cannot be undone.", parent=self.root, icon='warning'):
            conn = None
            try:
                conn = self._db_connect()
                if conn is None: return

                my_cursor = conn.cursor()
                sql = "DELETE FROM student WHERE Student_id=%s"
                val = (self.var_stdID.get(),)
                my_cursor.execute(sql, val)

                if my_cursor.rowcount == 0:
                     messagebox.showwarning("Delete Warning", f"No student found with ID '{self.var_stdID.get()}'. No record deleted.", parent=self.root)
                else:
                     conn.commit()
                     messagebox.showinfo("Deleted", "Record successfully deleted.", parent=self.root)
                     self.fetch_data() # Refresh table
                     self.reset_data() # Clear form

            except mysql.connector.Error as err:
                 messagebox.showerror("Database Error", f"Error deleting data: {err}", parent=self.root)
                 if conn: conn.rollback()
            except Exception as es:
                 messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
                 if conn: conn.rollback()
            finally:
                 if conn and conn.is_connected():
                     my_cursor.close()
                     conn.close()

    def reset_data(self):
        """Clears all form fields."""
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stdID.set("")
        self.var_stdName.set("")
        self.var_div.set("Select Division")
        self.var_rollNO.set("")
        self.var_gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phNO.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("No") # Reset radio to default 'No'
        self.var_search_by.set("Select")
        self.var_search_text.set("")
        # Optionally clear selection in the treeview
        # selection = self.student_table.selection()
        # if selection:
        #     self.student_table.selection_remove(selection)


    def search_data(self):
        """Searches student data based on selected criteria."""
        search_by = self.var_search_by.get()
        search_text = self.var_search_text.get().strip()

        if search_by == "Select":
            messagebox.showwarning("Search Error", "Please select a search criterion.", parent=self.root)
            return
        if not search_text:
            messagebox.showwarning("Search Error", "Please enter text to search for.", parent=self.root)
            return

        # Map combobox values to actual database column names
        column_map = {
            "Roll_No": "Roll",
            "Phone_No": "phNO",
            "Student_id": "Student_id",
            "Name": "Name"
        }
        db_column = column_map.get(search_by)

        if not db_column:
            messagebox.showerror("Search Error", "Invalid search criterion selected.", parent=self.root)
            return

        conn = None
        try:
            conn = self._db_connect()
            if conn is None: return

            my_cursor = conn.cursor()
            # Use parameterization to prevent SQL injection
            # Use LIKE for partial matches, adjust as needed (e.g., exact match for ID/Roll?)
            # For exact match use: query = f"SELECT ... FROM student WHERE {db_column} = %s"
            query = f"SELECT Dep, course, Year, Semester, Student_id, Name, Division, Roll, gender, DOB, email, phNO, address, teacher, photo FROM student WHERE {db_column} LIKE %s"
            search_pattern = f"%{search_text}%" # Search for text anywhere in the field

            my_cursor.execute(query, (search_pattern,))
            data = my_cursor.fetchall()

            self.student_table.delete(*self.student_table.get_children()) # Clear table

            if data:
                for i in data:
                    self.student_table.insert("", END, values=i)
            else:
                 messagebox.showinfo("Search Result", f"No records found matching '{search_text}' in {search_by}.", parent=self.root)


        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error during search: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An unexpected error occurred during search: {str(es)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()


    # ================== Photo Generation ========================

    def generate_dataset(self):
        """Captures face samples for the selected student."""
        student_id = self.var_stdID.get()
        student_name = self.var_stdName.get() # For user feedback

        # --- Pre-checks ---
        if (self.var_dep.get() == "Select Department" or student_name == "" or student_id == ""):
            messagebox.showerror("Error", "Please select/enter Department, Name, and Student ID before taking photos.", parent=self.root)
            return

        # Check if student exists (optional but good practice)
        if not self._check_student_exists(student_id):
             messagebox.showerror("Error", f"Student ID {student_id} not found in the database. Please save the student first.", parent=self.root)
             return

        # Check for Haar Cascade file
        cascade_path = "haarcascade_frontalface_default.xml"
        if not os.path.exists(cascade_path):
            messagebox.showerror("Error", f"Haar Cascade file not found:\n{cascade_path}\nPlease download it and place it in the application directory.", parent=self.root)
            return

        # Check and create 'data' directory if it doesn't exist
        data_dir = "data"
        if not os.path.exists(data_dir):
            try:
                os.makedirs(data_dir)
                print(f"Created directory: {data_dir}")
            except OSError as e:
                 messagebox.showerror("Error", f"Could not create data directory '{data_dir}': {e}", parent=self.root)
                 return

        # --- Update Photo Status in DB (Do this *after* successful capture or prompt user) ---
        # It might be better to update *after* capture is confirmed successful.
        # Moved the update logic inside the try block after capture loop.

        try:
            face_classifier = cv2.CascadeClassifier(cascade_path)

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                cropped_faces = []
                for (x, y, w, h) in faces:
                    face_crop = img[y:y+h, x:x+w]
                    cropped_faces.append(face_crop)
                return cropped_faces # Return list of detected faces

            cap = cv2.VideoCapture(0) # 0 for default webcam
            if not cap.isOpened():
                messagebox.showerror("Camera Error", "Could not open webcam.", parent=self.root)
                return

            img_id = 0
            target_samples = 20 # Number of samples to collect
            print(f"Starting photo capture for Student ID: {student_id}, Name: {student_name}")
            messagebox.showinfo("Starting Capture", f"Look at the camera. Capturing {target_samples} samples for {student_name} (ID: {student_id}).\nPress Enter or wait for completion.", parent=self.root)

            while True:
                ret, img_frame = cap.read()
                if not ret:
                    print("Warning: Could not read frame from camera.")
                    continue # Skip this frame

                cropped_face_list = face_cropped(img_frame)

                if cropped_face_list:
                    for face in cropped_face_list: # Process each detected face (usually just one)
                        img_id += 1
                        # Resize and convert to grayscale
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Construct filename: user.<student_id>.<sample_number>.jpg
                        file_name_path = os.path.join(data_dir, f"user.{student_id}.{img_id}.jpg")
                        cv2.imwrite(file_name_path, face)

                        # Display feedback on the captured face window
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Capturing Face...", face)

                # Check for exit conditions
                key = cv2.waitKey(1) # Wait 1ms for a key press
                if key == 13 or img_id >= target_samples: # 13 is Enter key
                    break

            cap.release()
            cv2.destroyAllWindows()

            if img_id < target_samples:
                 messagebox.showwarning("Capture Incomplete", f"Only captured {img_id} samples. Process stopped.", parent=self.root)
            else:
                 messagebox.showinfo("Result", f"Dataset generation completed successfully for ID: {student_id}", parent=self.root)

            # --- Update Photo Status in Database *after* successful capture ---
            self._update_photo_status(student_id, "Yes")
            self.fetch_data() # Refresh the table to show updated status
            # self.reset_data() # Optional: Reset form after capture

        except cv2.error as cv_err:
             messagebox.showerror("OpenCV Error", f"OpenCV error during face capture: {cv_err}", parent=self.root)
             if 'cap' in locals() and cap.isOpened(): cap.release() # Ensure camera is released on error
             cv2.destroyAllWindows()
        except Exception as es:
             messagebox.showerror("Error", f"An unexpected error occurred during dataset generation: {str(es)}", parent=self.root)
             if 'cap' in locals() and cap.isOpened(): cap.release()
             cv2.destroyAllWindows()

    def _check_student_exists(self, student_id):
        """Checks if a student ID exists in the database."""
        conn = None
        exists = False
        try:
            conn = self._db_connect()
            if conn is None: return False # Can't check if DB unavailable
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT 1 FROM student WHERE Student_id = %s LIMIT 1", (student_id,))
            result = my_cursor.fetchone()
            exists = bool(result)
        except mysql.connector.Error as err:
            print(f"DB Error checking student existence: {err}") # Log error, don't bother user
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()
        return exists

    def _update_photo_status(self, student_id, status):
        """Updates the 'photo' field for a given student ID."""
        conn = None
        try:
            conn = self._db_connect()
            if conn is None: return
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE student SET photo = %s WHERE Student_id = %s", (status, student_id))
            conn.commit()
            # Update the radio button variable directly if the updated student is currently loaded in the form
            if self.var_stdID.get() == student_id:
                self.var_radio.set(status)
            print(f"Photo status for ID {student_id} updated to {status}")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to update photo status: {err}", parent=self.root)
            if conn: conn.rollback()
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()


if __name__ == "__main__":
    # Use ThemedTk for the root window to easily apply themes
    root = ThemedTk(theme="clam") # Choose theme: clam, arc, plastique, etc.
    # If issues with ThemedTk, fallback to standard Tk:
    # root = tk.Tk()
    obj = Student(root)
    root.mainloop()