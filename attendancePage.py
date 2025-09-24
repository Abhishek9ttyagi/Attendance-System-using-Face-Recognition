# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import os
# import csv
# from tkinter import filedialog

# myData=[]
# class Attendance:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1500x790+0+0")
#         self.root.title("Attendance Window")

#         #----variables------
#         self.var_stuID=StringVar()
#         self.var_rollNO=StringVar()
#         self.var_name=StringVar()
#         self.var_date=StringVar()
#         self.var_time=StringVar()
#         self.var_dep=StringVar()
#         self.var_atten=StringVar()


#         #first image
#         img1=Image.open(r".\Images\AttendancePage1.jpg")
#         img1=img1.resize((800,300),Image.Resampling.LANCZOS)
#         self.photoimg1=ImageTk.PhotoImage(img1)
#         first_lbl=Label(self.root,image=self.photoimg1)
#         first_lbl.place(x=0,y=0,width=800,height=300)

#         #second image
#         img2=Image.open(r".\Images\AttendancePage2.jpg")
#         img2=img2.resize((800,300),Image.Resampling.LANCZOS)
#         self.photoimg2=ImageTk.PhotoImage(img2)
#         first_lbl=Label(self.root,image=self.photoimg2)
#         first_lbl.place(x=800,y=0,width=800,height=300)

#         title_lbl=Label(self.root,text="ATTENDANE RECORDS",font=("Times New Roman",40,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=300,width=1600,height=45)

#         #main frame
#         main_frame=Frame(self.root,bd=2,bg="white")
#         main_frame.place(x=0,y=345,width=1600,height=600)
#         #left frame
#         left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
#         left_frame.place(x=5,y=5,width=800,height=440)
#         img_lf=Image.open(r".\Images\leftFrame_img.jpg")
#         img_lf=img_lf.resize((765,170),Image.Resampling.LANCZOS)
#         self.photoimg_lf=ImageTk.PhotoImage(img_lf)
#         first_lbl=Label(left_frame,image=self.photoimg_lf)
#         first_lbl.place(x=0,y=5,width=765,height=170)

#         left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
#         left_inside_frame.place(x=0,y=180,width=800,height=400)

#         #---------------------------labels and entries
#         #studentID
#         stuID_label=Label(left_inside_frame,text="StudentID",font=("times new roman", 12, "bold"),bg="white")
#         stuID_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)
#         stuID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_stuID,font=("times new roman", 12, "bold"))
#         stuID_entry.grid(row=0,column=1,padx=7,pady=5,sticky=W)
#         #studentRollNO
#         rollNO_label=Label(left_inside_frame,text="Roll Number",font=("times new roman", 12, "bold"),bg="white")
#         rollNO_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)
#         rollNO_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_rollNO,font=("times new roman", 12, "bold"))
#         rollNO_entry.grid(row=0,column=1,padx=7,pady=5,sticky=W)
#         #student Name
#         stuName_label=Label(left_inside_frame,text="Student Name",font=("times new roman", 12, "bold"))
#         stuName_label.grid(row=1,column=0,padx=7,pady=5,sticky=W)
#         stuName_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman", 12, "bold"))
#         stuName_entry.grid(row=1,column=1,padx=7,pady=5,sticky=W)
#         #Date
#         date_label=Label(left_inside_frame,text="Date",font=("times new roman", 12, "bold"))
#         date_label.grid(row=2,column=0,padx=7,pady=5,sticky=W)
#         date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman", 12, "bold"))
#         date_entry.grid(row=2,column=1,padx=7,pady=5,sticky=W)
#         #Time
#         time_label=Label(left_inside_frame,text="Time",font=("times new roman", 12, "bold"))
#         time_label.grid(row=2,column=2,padx=7,pady=5,sticky=W)
#         time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("times new roman", 12, "bold"))
#         time_entry.grid(row=2,column=3,padx=7,pady=5,sticky=W)
#         #Department
#         dep_label=Label(left_inside_frame,text="Department",font=("times new roman", 12, "bold"))
#         dep_label.grid(row=3,column=0,padx=7,pady=5,sticky=W)
#         dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman", 12, "bold"))
#         dep_entry.grid(row=3,column=1,padx=7,pady=5,sticky=W)
#         #attendance
#         attendance_label=Label(left_inside_frame,text="Attendance status",bg="white",font=("times new roman", 12, "bold"))
#         attendance_label.grid(rows=3,column=0)
#         self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten,font=("times new roman", 12, "bold"),state="readonly")
#         self.atten_status["values"]=("Status","Present","Absent")
#         self.atten_status.grid(rows=3,column=1,pady=8)
#         self.atten_status.current(0)

#         #buttons 
#         btn_frame1=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
#         btn_frame1.place(x=5,y=200,width=800,height=30)

#         import_btn=Button(btn_frame1,text="importCSV",command=self.importCSV,width=25,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         import_btn.grid(row=0,column=0)

#         export_btn=Button(btn_frame1,text="exportCSV",command=self.exportCSV,width=25,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         export_btn.grid(row=0,column=1)

#         update_btn=Button(btn_frame1,text="Update",width=25,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         update_btn.grid(row=0,column=2)

#         reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=25,font=("Times New Roman",10,"bold"),bg="blue",fg="white")
#         reset_btn.grid(row=0,column=3)


#         #right frame
#         right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
#         right_frame.place(x=800,y=10,width=800,height=400)

#         #table frame
#         table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
#         table_frame.place(x=5,y=5,width=780,height=380)
#         #scroll bars
#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

#         self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","rollNO","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         self.AttendanceReportTable.heading("ID",text="Student ID")
#         self.AttendanceReportTable.heading("rollNO",text="Roll Number")
#         self.AttendanceReportTable.heading("name",text="Name")
#         self.AttendanceReportTable.heading("date",text="Date")
#         self.AttendanceReportTable.heading("time",text="Time")
#         self.AttendanceReportTable.heading("department",text="Department")
#         self.AttendanceReportTable.heading("attendance",text="Attendance Status")

#         self.AttendanceReportTable["show"]="headings"

#         self.AttendanceReportTable.column("ID",width=150)
#         self.AttendanceReportTable.column("rollNO",width=150)
#         self.AttendanceReportTable.column("name",width=150)
#         self.AttendanceReportTable.column("date",width=150)
#         self.AttendanceReportTable.column("time",width=150)
#         self.AttendanceReportTable.column("department",width=150)
#         self.AttendanceReportTable.column("attendance",width=150)

#         self.AttendanceReportTable.pack(fill=BOTH,expand=1)

#         self.AttendanceReportTable.bind("<ButtonRelease>",self.getCursor)

#     #funcion for fetching data
#     def fetchData(self,rows):
#         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
#         for i in rows:
#             self.AttendanceReportTable.insert("",END,values=i)
#     #function for importing data into our attendance window 
#     def importCSV(self):
#         global myData
#         myData.clear()
#         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
#         with open(fln) as myfile:
#             csvread=csv.reader(myfile,delimiter=",")
#             for i in csvread:
#                 myData.append(i)
#             self.fetchData(myData)
#     #function to save the data present in attendance report window , into some other csv file
#     def exportCSV(self):
#         try:
#             if len(myData)<1:
#                 messagebox.showerror("No Data","No Data found to export",parent=self.root)
#                 return False
#             fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
#             with open(fln,mode="w",newline="") as myfile:
#                 exp_write=csv.writer(myfile,delimiter=",")
#                 for i in myData:
#                     exp_write.writerow(i)
#                 messagebox.showinfo("Info","Your data exported to "+os.path.basename(fln)+"  successfully")
#         except Exception as es:
#             messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

#     def getCursor(self,event=""):
#         cursor_row=self.AttendanceReportTable.focus()
#         content=self.AttendanceReportTable.item(cursor_row)
#         rows=content['values']
#         self.var_stuID.set(rows[0])
#         self.var_rollNO.set(rows[1])
#         self.var_name.set(rows[2])
#         self.var_dep.set(rows[3])
#         self.var_time.set(rows[4])
#         self.var_date.set(rows[5])
#         self.var_atten.set(rows[6])

#     def reset_data(self):
#         self.var_stuID.set("")
#         self.var_rollNO.set("")
#         self.var_name.set("")
#         self.var_dep.set("")
#         self.var_time.set("")
#         self.var_date.set("")
#         self.var_atten.set("")




# if __name__=="__main__":
#     root=Tk()
#     obj=Attendance(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, Frame, Label, LabelFrame, Button, HORIZONTAL, VERTICAL, BOTTOM, X, RIGHT, Y, W, BOTH, END, StringVar
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog
from ttkthemes import ThemedTk

class Attendance:
    def __init__(self, root):
        self.root = root
        style = ttk.Style(self.root)
        # try:
        #     selected_theme = "clam"
        #     self.root.set_theme(selected_theme)
        #     print(f"Using theme: {selected_theme}")
        # except tk.TclError:
        #     print("ttkthemes theme not found or Tcl error, using default.")
        #     style.theme_use('clam')

        # self.root.title("Attendance Records Management")

        if hasattr(self.root, "set_theme"):
            try:
                selected_theme = "clam"  # Change theme if needed
                self.root.set_theme(selected_theme)
                print(f"Using theme: {selected_theme}")
            except Exception as e:
                print(f"Error applying theme: {e}")
        else:
            print("Root does not support themes. Skipping theme application.")

        self.root.title("Attendance Management System")
        

        min_width = 1100
        min_height = 600
        self.root.minsize(min_width, min_height)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.8)
        initial_height = int(screen_height * 0.75)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")

        # --- Variables ---
        self.var_stuID = StringVar()
        self.var_rollNO = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_atten = StringVar()

        # --- Internal Data Store ---
        self.attendance_data = [] # Stores list of lists (rows)
        self.selected_item_iid = None # Store the IID (internal ID) of the selected Treeview item
        self.selected_data_index = None # Store the index in self.attendance_data corresponding to selected_item_iid

        # --- Configure root grid layout ---
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Title ---
        title_lbl = ttk.Label(self.root, text="ATTENDANCE RECORDS", style="Title.TLabel")
        title_lbl.grid(row=0, column=0, pady=(10, 5), sticky="ew")
        sep = ttk.Separator(self.root, orient='horizontal')
        sep.grid(row=0, column=0, sticky='sew', padx=10, pady=(45, 0))

        # --- Main Content Area ---
        main_frame = ttk.Frame(self.root, style="TFrame", padding=(10, 10))
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1, minsize=350)
        main_frame.grid_columnconfigure(1, weight=3)
        main_frame.grid_rowconfigure(0, weight=1)

        # --- Left Panel (Details & Actions) ---
        self.create_left_panel(main_frame)

        # --- Right Panel (Attendance Table) ---
        self.create_right_panel(main_frame)

    def configure_styles(self, style):
        """Configure ttk styles for widgets."""
        primary_color = "#17a2b8"
        secondary_color = "#6c757d"
        light_bg = style.lookup('TFrame', 'background')
        text_color = style.lookup('TLabel', 'foreground')
        button_fg = "#ffffff"
        button_hover_bg = "#117a8b"

        style.configure("TFrame")
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground=primary_color, anchor="center")
        style.configure("Header.TLabel", font=("Helvetica", 11, "bold"))
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TEntry", font=("Helvetica", 10), padding=(5, 5)) # Default style for editable entry
        style.configure("TCombobox", font=("Helvetica", 10), padding=(5, 5))

        style.configure("Accent.TButton", font=("Helvetica", 10, "bold"),
                        foreground=button_fg, background=primary_color,
                        padding=(10, 5), borderwidth=0)
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', primary_color), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])

        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", rowheight=25, font=("Helvetica", 9))

    def _create_editable_field(self, parent, row, col, label_text, variable, widget_type='entry', values=None):
        """Helper to create a label and an *editable* entry/combobox field."""
        label = ttk.Label(parent, text=label_text, style="TLabel")
        label.grid(row=row, column=col, padx=5, pady=(5,0), sticky="w") # Reduced pady bottom

        if widget_type == 'combobox':
            widget = ttk.Combobox(parent, textvariable=variable, values=values, style="TCombobox", state="readonly") # Keep combobox readonly for status
            if values and variable.get() not in values:
                 widget.current(0) # Default selection if current value isn't valid
            elif variable.get() in values:
                 widget.set(variable.get()) # Set current value if valid
            else:
                 widget.current(0)

        else: # Default to entry
            widget = ttk.Entry(parent, textvariable=variable, style="TEntry") # Use default editable style

        widget.grid(row=row, column=col + 1, padx=5, pady=(5,0), sticky="ew")
        return widget

    def create_left_panel(self, parent):
        """Creates the left panel for editing details and action buttons."""
        left_frame_container = ttk.Frame(parent, padding=(0, 0))
        left_frame_container.grid(row=0, column=0, padx=(0, 10), pady=(0, 0), sticky="nsew")
        left_frame_container.grid_rowconfigure(0, weight=0)
        left_frame_container.grid_rowconfigure(1, weight=0)
        left_frame_container.grid_columnconfigure(0, weight=1)

        # Details Frame (Editable)
        details_frame = ttk.LabelFrame(left_frame_container, text="Edit Record Details", style="TLabelframe", padding=(15, 5)) # Reduced bottom padding
        details_frame.grid(row=0, column=0, sticky="new")
        details_frame.grid_columnconfigure(1, weight=1)

        # --- Labels and Editable Entries ---
        # Note: Editing Student ID or Roll might be problematic if used as keys.
        # Consider making them readonly if they shouldn't be changed.
        self._create_editable_field(details_frame, 0, 0, "Student ID:", self.var_stuID)
        self._create_editable_field(details_frame, 1, 0, "Roll Number:", self.var_rollNO)
        self._create_editable_field(details_frame, 2, 0, "Student Name:", self.var_name)
        self._create_editable_field(details_frame, 3, 0, "Department:", self.var_dep)
        self._create_editable_field(details_frame, 4, 0, "Time:", self.var_time)
        self._create_editable_field(details_frame, 5, 0, "Date:", self.var_date)
        self._create_editable_field(details_frame, 6, 0, "Status:", self.var_atten, 'combobox', ("Present", "Absent")) # Only allow valid status


        # --- Action Buttons Frame ---
        btn_frame = ttk.LabelFrame(left_frame_container, text="Actions", style="TLabelframe", padding=(15, 10))
        btn_frame.grid(row=1, column=0, pady=(10, 0), sticky="sew") # Reduced pady top
        btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1) # Use 4 columns

        import_btn = ttk.Button(btn_frame, text="Import CSV", command=self.importCSV, style="Accent.TButton", width=12, cursor="hand2")
        import_btn.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        export_btn = ttk.Button(btn_frame, text="Export CSV", command=self.exportCSV, style="Accent.TButton", width=12, cursor="hand2")
        export_btn.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        update_btn = ttk.Button(btn_frame, text="Update", command=self.update_data, style="Accent.TButton", width=12, cursor="hand2") # Now enabled
        update_btn.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

        reset_btn = ttk.Button(btn_frame, text="Reset View", command=self.reset_data, style="Accent.TButton", width=12, cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

    def create_right_panel(self, parent):
        """Creates the right panel containing the attendance records table."""
        right_frame_container = ttk.LabelFrame(parent, text="Attendance Records", style="TLabelframe", padding=(15, 10))
        right_frame_container.grid(row=0, column=1, padx=(10, 0), pady=(0, 0), sticky="nsew")
        right_frame_container.grid_rowconfigure(0, weight=1)
        right_frame_container.grid_columnconfigure(0, weight=1)

        table_area = ttk.Frame(right_frame_container)
        table_area.grid(row=0, column=0, sticky="nsew")
        table_area.grid_rowconfigure(0, weight=1)
        table_area.grid_columnconfigure(0, weight=1)

        scroll_x = ttk.Scrollbar(table_area, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_area, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_area,
            columns=("id", "roll", "name", "dep", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            style="Treeview"
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Student ID")
        self.AttendanceReportTable.heading("roll", text="Roll Number")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        col_width = 120
        for col in self.AttendanceReportTable["columns"]:
            self.AttendanceReportTable.column(col, width=col_width, minwidth=80, anchor=W)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.getCursor)

    # ================== Data Handling Functions ==========================

    def fetchData(self, rows):
        """Clears the table and populates it with the provided data rows."""
        try:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            # Store the mapping from IID to list index when inserting
            self.iid_to_data_index_map = {}
            for index, i in enumerate(rows):
                if len(i) == len(self.AttendanceReportTable["columns"]):
                    # Insert row and get its IID
                    iid = self.AttendanceReportTable.insert("", END, values=i)
                    self.iid_to_data_index_map[iid] = index # Store mapping
                else:
                    print(f"Warning: Skipping row with incorrect number of columns: {i}")
        except Exception as e:
             messagebox.showerror("Fetch Data Error", f"An error occurred while populating the table: {e}", parent=self.root)

    def importCSV(self):
        """Imports data from a selected CSV file into the table."""
        self.attendance_data.clear()
        self.reset_selection_state() # Clear selection state on new import
        try:
            fln = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Select CSV Attendance File",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            if not fln: return

            with open(fln, mode='r', newline='', encoding='utf-8') as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                header = next(csvread, None)

                for i in csvread:
                    if any(field.strip() for field in i):
                         # Ensure row has the correct number of columns, pad if necessary (or skip)
                         if len(i) == 7: # Expect 7 columns
                            self.attendance_data.append(i)
                         else:
                             # Handle rows with incorrect column count - e.g., skip and warn
                             print(f"Skipping row with incorrect column count ({len(i)} instead of 7): {i}")

            if not self.attendance_data:
                 messagebox.showwarning("Import Warning", "No valid data rows (with 7 columns) found in the selected CSV file.", parent=self.root)
                 return

            self.fetchData(self.attendance_data)
            messagebox.showinfo("Import Success", f"{len(self.attendance_data)} records imported successfully from\n{os.path.basename(fln)}", parent=self.root)

        except FileNotFoundError:
             messagebox.showerror("Import Error", f"File not found:\n{fln}", parent=self.root)
        except Exception as es:
             messagebox.showerror("Import Error", f"An error occurred during CSV import:\n{str(es)}", parent=self.root)

    def exportCSV(self):
        """Exports the *current* data (including any updates) to a CSV file."""
        try:
            if not self.attendance_data:
                messagebox.showerror("Export Error", "No data available to export.", parent=self.root)
                return

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save Attendance Data As CSV",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
                defaultextension=".csv",
                parent=self.root
            )
            if not fln: return

            with open(fln, mode="w", newline="", encoding='utf-8') as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                # Write header row based on Treeview columns
                header = [self.AttendanceReportTable.heading(col)["text"] for col in self.AttendanceReportTable["columns"]]
                exp_write.writerow(header)
                # Write data rows from the *internal self.attendance_data list*
                for i in self.attendance_data:
                    exp_write.writerow(i)

            messagebox.showinfo("Export Success", f"Data exported successfully to:\n{os.path.basename(fln)}", parent=self.root)

        except Exception as es:
            messagebox.showerror("Export Error", f"An error occurred during CSV export:\n{str(es)}", parent=self.root)

    def getCursor(self, event=""):
        """Populates the detail fields when a table row is clicked and stores selection state."""
        self.reset_selection_state() # Clear previous selection state first
        cursor_row_iid = self.AttendanceReportTable.focus() # Get the Item ID (IID)

        if not cursor_row_iid: return # No row selected

        try:
            content = self.AttendanceReportTable.item(cursor_row_iid)
            rows = content['values']

            if rows and len(rows) == 7:
                self.var_stuID.set(rows[0])
                self.var_rollNO.set(rows[1])
                self.var_name.set(rows[2])
                self.var_dep.set(rows[3])
                self.var_time.set(rows[4])
                self.var_date.set(rows[5])
                self.var_atten.set(rows[6])

                # Store the IID and find the corresponding index in self.attendance_data
                self.selected_item_iid = cursor_row_iid
                if hasattr(self, 'iid_to_data_index_map') and cursor_row_iid in self.iid_to_data_index_map:
                    self.selected_data_index = self.iid_to_data_index_map[cursor_row_iid]
                else:
                    # Fallback: Search manually (less efficient but robust)
                    try:
                       # Assuming student ID is unique enough for finding the index
                       target_id = rows[0]
                       self.selected_data_index = next(idx for idx, data_row in enumerate(self.attendance_data) if data_row[0] == target_id)
                    except StopIteration:
                        print(f"Warning: Could not find index for selected item {cursor_row_iid} in data list.")
                        self.reset_selection_state()


            else:
                print(f"Warning: Invalid data retrieved from row: {rows}")
                self.reset_data() # Clear form if data is invalid

        except IndexError:
            messagebox.showwarning("Selection Error", "Could not retrieve data for the selected row.", parent=self.root)
            self.reset_data()
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred while getting cursor data: {str(es)}", parent=self.root)
            self.reset_data()

    def reset_data(self):
        """Clears the detail form fields and the table selection."""
        self.var_stuID.set("")
        self.var_rollNO.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten.set("") # Consider setting to default like "Present" or keeping blank
        self.reset_selection_state()

        # Also clear selection in Treeview visually
        selection = self.AttendanceReportTable.selection()
        if selection:
            self.AttendanceReportTable.selection_remove(selection)

    def reset_selection_state(self):
        """Clears the stored information about the selected item."""
        self.selected_item_iid = None
        self.selected_data_index = None


    def update_data(self):
        """Updates the selected record in the internal list and refreshes the table."""
        # Check if a row index is stored (meaning a valid row was selected)
        if self.selected_data_index is None:
            messagebox.showerror("Update Error", "Please select a record from the table to update.", parent=self.root)
            return

        # Check if the index is still valid for the current data list length
        if self.selected_data_index >= len(self.attendance_data):
             messagebox.showerror("Update Error", "Selected record index is out of bounds. Please re-select.", parent=self.root)
             self.reset_selection_state() # Clear invalid state
             return

        try:
            # Get the new data from the form fields
            updated_row = [
                self.var_stuID.get(),
                self.var_rollNO.get(),
                self.var_name.get(),
                self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_atten.get()
            ]

            # Ask for confirmation
            if messagebox.askyesno("Confirm Update", "Are you sure you want to update this record?", parent=self.root):
                # Update the record in the internal list using the stored index
                self.attendance_data[self.selected_data_index] = updated_row

                # Refresh the entire table to show the change
                self.fetchData(self.attendance_data)

                messagebox.showinfo("Update Success", "Record updated successfully.", parent=self.root)
                self.reset_selection_state() # Clear selection after update

        except Exception as es:
             messagebox.showerror("Update Error", f"An error occurred during update:\n{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = ThemedTk(theme="clam")
    obj = Attendance(root)
    root.mainloop()