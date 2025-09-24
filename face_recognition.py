# import os
# import numpy as np
# import face_recognition
# from time import strftime
# from datetime import datetime
# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2

# class Face_Recognition:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition")

#         title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 40, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1600, height=45)

#         img_left = Image.open(r".\Images\face_recognition.jpg")
#         img_left = img_left.resize((800, 600), Image.Resampling.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_left)
#         first_lbl = Label(self.root, image=self.photoimg_top)
#         first_lbl.place(x=0, y=60, width=800, height=600)

#         b1_1 = Button(self.root, text="FACE RECOGNITION", cursor="hand2",font=("Times New Roman", 18, "bold"), bg="white", fg="blue",command=self.face_recog)
#         b1_1.place(x=0, y=660, width=1600, height=45)


#         img_right = Image.open(r".\Images\face_recog2.png")
#         img_right = img_right.resize((800, 600), Image.Resampling.LANCZOS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_right)
#         first_lbl = Label(self.root, image=self.photoimg_bottom)
#         first_lbl.place(x=800, y=60, width=800, height=600)

#     #marking attendance
#     def mark_attendance(self,i,r,n,d):
#         with open("attendance.csv","r+",newline="\n") as f:
#             myDataList=f.readlines()
#             name_list=[]
#             for line in myDataList:
#                 entry=line.split((","))
#                 name_list.append(entry[0])
#             if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
#                 now=datetime.now()
#                 d1=now.strftime("%d/%m/%Y")
#                 dtString=now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

#     #face recognition function
#     def face_recog(self):
#         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#             coord=[]

#             for(x,y,w,h) in features:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                 confidence=int((100*(1-predict/300)))
 
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhishri#@9875",database="face_recognition_system")
#                 my_cursor=conn.cursor()
        
#                 my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
#                 n=my_cursor.fetchone()
#                 if n:
#                     n="+".join(n)

                
#                 my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
#                 r=my_cursor.fetchone()
#                 if r:
#                     r="+".join(r)

             
#                 my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
#                 d=my_cursor.fetchone()
#                 if d:
#                     d="+".join(d)

#                 my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (id,))
#                 i=my_cursor.fetchone()
#                 if i:
#                     i = "+".join(map(str, i))

#                 if confidence>77:
#                     cv2.putText(img,f"Student_ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Roll Number:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     self.mark_attendance(i,r,n,d)
#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Not Registered",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 coord=[x,y,w,h]
            
#             return coord
        
#         def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
        
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap=cv2.VideoCapture(0)

#         while True:
#             ret,img=video_cap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Welcome to Face Recognition window",img)

#             if cv2.waitKey(1)==13:
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()


# if __name__=="__main__":
#     root=Tk()
#     obj=Face_Recognition(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import csv
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import threading # For running recognition in background
from ttkthemes import ThemedTk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        # Apply theme
        style = ttk.Style(self.root)
        # try:
        #     selected_theme = "clam" # <-- CHANGE THEME HERE
        #     self.root.set_theme(selected_theme)
        #     print(f"Using theme: {selected_theme}")
        # except tk.TclError:
        #     print("ttkthemes theme not found or Tcl error, using default.")
        #     style.theme_use('clam')

        # Apply theme only if the root supports it
        if hasattr(self.root, "set_theme"):
            try:
                selected_theme = "clam"  # Change theme if needed
                self.root.set_theme(selected_theme)
                print(f"Using theme: {selected_theme}")
            except Exception as e:
                print(f"Error applying theme: {e}")
        else:
            print("Root does not support themes. Skipping theme application.")


        self.root.title("Face Recognition & Attendance")
        # Set minimum size and make resizable
        min_width = 1000
        min_height = 650
        self.root.minsize(min_width, min_height)

        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.8)
        initial_height = int(screen_height * 0.8)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")

        # --- Variables ---
        self.current_status = tk.StringVar(value="Ready")
        self.marked_ids_today = set() # Keep track of IDs marked in this session/day
        self.today_date_str = datetime.now().strftime("%d/%m/%Y")

        # --- Threading Control ---
        self.recognition_thread = None
        self.stop_event = threading.Event()

        # --- Resources ---
        self.video_capture = None
        self.faceCascade = None
        self.clf = None # LBPH Recognizer
        self.db_conn = None
        self.db_cursor = None

        # --- Configure root grid layout ---
        self.root.grid_columnconfigure(0, weight=1) # Main content column expands
        self.root.grid_rowconfigure(1, weight=1)    # Main content row expands

        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Title ---
        title_lbl = ttk.Label(self.root, text="FACE RECOGNITION", style="Title.TLabel")
        title_lbl.grid(row=0, column=0, pady=(10, 5), sticky="ew")
        sep = ttk.Separator(self.root, orient='horizontal')
        sep.grid(row=0, column=0, sticky='sew', padx=10, pady=(55, 0))

        # --- Main Content Frame ---
        main_frame = ttk.Frame(self.root, style="TFrame", padding=(10, 10))
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=3) # Video area larger
        main_frame.grid_columnconfigure(1, weight=1) # Info/Controls area
        main_frame.grid_rowconfigure(0, weight=1)

        # --- Video Display Label (Left) ---
        video_frame = ttk.LabelFrame(main_frame, text="Camera Feed", style="TLabelframe")
        video_frame.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="nsew")
        video_frame.grid_columnconfigure(0, weight=1)
        video_frame.grid_rowconfigure(0, weight=1)

        # Label to display video frames
        self.video_label = ttk.Label(video_frame, anchor="center", background="black") # Start with black background
        self.video_label.grid(row=0, column=0, sticky="nsew")

        # --- Info and Controls Panel (Right) ---
        controls_frame = ttk.LabelFrame(main_frame, text="Controls & Status", style="TLabelframe", padding=(15, 10))
        controls_frame.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="nsew")
        controls_frame.grid_columnconfigure(0, weight=1)
        # Configure rows for spacing
        controls_frame.grid_rowconfigure(0, weight=0) # Start button
        controls_frame.grid_rowconfigure(1, weight=0) # Stop button
        controls_frame.grid_rowconfigure(2, weight=1) # Status label (expandable space above)
        controls_frame.grid_rowconfigure(3, weight=0) # Status label row


        # Start Button
        self.start_button = ttk.Button(controls_frame, text="Start Recognition", command=self.start_recognition, style="Accent.TButton", cursor="hand2")
        self.start_button.grid(row=0, column=0, padx=5, pady=(10,5), sticky="ew")

        # Stop Button
        self.stop_button = ttk.Button(controls_frame, text="Stop Recognition", command=self.stop_recognition, style="Accent.TButton", cursor="hand2", state="disabled")
        self.stop_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Status Label
        status_display_label = ttk.Label(controls_frame, textvariable=self.current_status, style="Status.TLabel", anchor="center", wraplength=controls_frame.winfo_reqwidth() - 40) # Adjust wraplength
        status_display_label.grid(row=3, column=0, padx=5, pady=(20, 10), sticky="sew")


        # --- Graceful Exit ---
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # --- Load Resources ---
        self._load_resources()


    def configure_styles(self, style):
        """Configure ttk styles."""
        primary_color = "#28a745" # Green
        secondary_color = "#6c757d" # Gray
        light_bg = style.lookup('TFrame', 'background')
        text_color = style.lookup('TLabel', 'foreground')
        button_fg = "#ffffff"
        button_hover_bg = "#218838" # Darker Green

        style.configure("TFrame")
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground=primary_color, anchor="center")
        style.configure("Header.TLabel", font=("Helvetica", 11, "bold"))
        style.configure("Status.TLabel", font=("Helvetica", 12), foreground=secondary_color)
        style.configure("Accent.TButton", font=("Helvetica", 12, "bold"),
                        foreground=button_fg, background=primary_color, padding=(10, 5))
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', primary_color), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])
        style.map('Accent.TButton',
          foreground=[('disabled', secondary_color)],
          background=[('disabled', light_bg)])


    def _update_status(self, message):
        """Safely updates the status label from any thread."""
        # Use root.after to schedule the update on the main thread
        self.root.after(0, lambda: self.current_status.set(message))

    def _update_video_label(self, photo_image):
         """Safely updates the video label from the background thread."""
         # Keep a reference to avoid garbage collection if needed immediately
         # self.video_label.photo_image = photo_image
         self.video_label.config(image=photo_image)
         self.video_label.image = photo_image # Keep reference


    def _load_resources(self):
        """Load cascade and recognizer model."""
        cascade_path = "haarcascade_frontalface_default.xml"
        classifier_path = "classifier.xml"

        if not os.path.exists(cascade_path):
            messagebox.showerror("Error", f"Haar Cascade file not found: {cascade_path}", parent=self.root)
            self._update_status(f"Error: Haar Cascade not found.")
            self.start_button.config(state="disabled") # Prevent starting
            return False
        self.faceCascade = cv2.CascadeClassifier(cascade_path)

        if not os.path.exists(classifier_path):
             messagebox.showerror("Error", f"Classifier model file not found: {classifier_path}\nPlease train the model first.", parent=self.root)
             self._update_status(f"Error: Classifier not found.")
             self.start_button.config(state="disabled") # Prevent starting
             return False
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            self.clf.read(classifier_path)
        except cv2.error as e:
             messagebox.showerror("Error", f"Failed to load classifier: {e}\nEnsure it's a valid OpenCV Recognizer file.", parent=self.root)
             self._update_status(f"Error: Failed to load classifier.")
             self.start_button.config(state="disabled")
             return False

        # Check attendance file header
        self._check_attendance_file()
        return True


    def _check_attendance_file(self):
        """Checks if attendance.csv exists and has a header, creates if not."""
        fname = "attendance.csv"
        header = "ID,Roll,Name,Department,Time,Date,Status\n"
        try:
            if not os.path.exists(fname) or os.path.getsize(fname) == 0:
                with open(fname, "w", newline='') as f:
                    f.write(header)
                print(f"Created/Initialized {fname}")
            else:
                # Optional: check if header exists
                with open(fname, "r", newline='') as f:
                    first_line = f.readline()
                    if not first_line.strip().replace('"','').startswith("ID,Roll,Name"):
                         print(f"Warning: {fname} seems to lack a valid header.")
                         # Decide whether to prepend header or just warn
        except Exception as e:
            messagebox.showerror("File Error", f"Could not access or create attendance file '{fname}': {e}", parent=self.root)
            self._update_status(f"Error: Attendance file issue.")


    def _connect_db(self):
        """Connects to the MySQL database."""
        try:
            self.db_conn = mysql.connector.connect(
                host="localhost",       # Your host
                user="root",            # Your username
                password="Abhishri#@9875",  # Your password
                database="face_recognition_system" # Your database
            )
            self.db_cursor = self.db_conn.cursor(buffered=True) # Buffered cursor can be helpful
            print("Database connected.")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect to database: {err}", parent=self.root)
            self._update_status(f"Error: DB Connection Failed.")
            return False

    def _disconnect_db(self):
        """Disconnects from the database."""
        try:
            if self.db_cursor:
                self.db_cursor.close()
                self.db_cursor = None
            if self.db_conn and self.db_conn.is_connected():
                self.db_conn.close()
                self.db_conn = None
                print("Database disconnected.")
        except mysql.connector.Error as err:
            print(f"Error disconnecting from DB: {err}")


    def start_recognition(self):
        """Starts the face recognition process in a background thread."""
        if self.recognition_thread and self.recognition_thread.is_alive():
            messagebox.showwarning("In Progress", "Recognition is already running.", parent=self.root)
            return

        if not self.faceCascade or not self.clf:
             if not self._load_resources(): # Try loading again
                 return # Exit if loading failed

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self._update_status("Initializing...")

        self.stop_event.clear() # Ensure stop event is not set
        self.recognition_thread = threading.Thread(target=self._recognition_loop, daemon=True)
        self.recognition_thread.start()

    def stop_recognition(self):
        """Signals the recognition thread to stop."""
        if self.recognition_thread and self.recognition_thread.is_alive():
            self.stop_event.set() # Signal the thread to stop
            self.stop_button.config(state="disabled") # Disable while stopping
            self._update_status("Stopping...")
        else:
            # If thread is not running, just reset buttons
             self.start_button.config(state="normal")
             self.stop_button.config(state="disabled")
             self._update_status("Ready")


    def on_closing(self):
        """Handles window close event."""
        print("Window closing...")
        self.stop_recognition() # Signal thread to stop if running
        if self.recognition_thread is not None:
             self.recognition_thread.join(timeout=2) # Wait briefly for thread to finish
        self._disconnect_db() # Ensure DB is disconnected
        self.root.destroy() # Close the Tkinter window


    def _get_student_details(self, student_id):
         """Fetches student details from the database for a given ID."""
         if not self.db_cursor or not self.db_conn or not self.db_conn.is_connected():
             print("DB cursor/connection not available for fetching details.")
             # Try to reconnect? Or just return None? For now, return None.
             # if not self._connect_db(): return None
             return None
         try:
             # Ensure ID is an integer if the DB column is INT
             try:
                query_id = int(student_id)
             except ValueError:
                 print(f"Invalid student ID format for query: {student_id}")
                 return None

             query = "SELECT Student_id, Roll, Name, Dep FROM student WHERE Student_id = %s"
             self.db_cursor.execute(query, (query_id,))
             result = self.db_cursor.fetchone()

             if result:
                 # Return details as a dictionary for easy access
                 return {"id": str(result[0]), "roll": str(result[1]), "name": str(result[2]), "dep": str(result[3])}
             else:
                 return None
         except mysql.connector.Error as err:
              print(f"Database error fetching student details for ID {student_id}: {err}")
              # Handle potential connection loss during query
              if err.errno == 2006 or err.errno == 2013: # MySQL server has gone away / Lost connection
                    self._disconnect_db() # Clean up potentially broken connection
              return None
         except Exception as e:
              print(f"Unexpected error fetching student details: {e}")
              return None


    def _mark_attendance_logic(self, details):
        """Checks if attendance needs marking and writes to CSV."""
        current_date_str = datetime.now().strftime("%d/%m/%Y")
        student_id = details["id"]

        # Reset marked list if the day has changed
        if current_date_str != self.today_date_str:
            print(f"Date changed from {self.today_date_str} to {current_date_str}. Resetting marked list.")
            self.marked_ids_today.clear()
            self.today_date_str = current_date_str

        # Check if already marked today
        if student_id in self.marked_ids_today:
            # print(f"ID {student_id} already marked today.") # Optional debug print
            return # Already marked, do nothing

        # Mark attendance
        try:
            with open("attendance.csv", "a", newline='') as f: # Use 'a' (append mode)
                now = datetime.now()
                time_str = now.strftime("%H:%M:%S")
                # Header: ID,Roll,Name,Department,Time,Date,Status
                csv_writer = csv.writer(f)
                csv_writer.writerow([
                    details["id"], details["roll"], details["name"], details["dep"],
                    time_str, current_date_str, "Present"
                ])
            # Add to marked list *after* successful write
            self.marked_ids_today.add(student_id)
            status_msg = f"Attendance Marked: {details['name']} ({details['id']})"
            print(status_msg)
            self._update_status(status_msg)
        except IOError as e:
            error_msg = f"Error writing attendance for ID {student_id}: {e}"
            print(error_msg)
            self._update_status(f"Error: Could not write to attendance file.")
        except Exception as e:
            error_msg = f"Unexpected error marking attendance for {student_id}: {e}"
            print(error_msg)
            self._update_status(f"Error: Attendance marking failed.")


    def _recognition_loop(self):
        """The main loop for video capture and face recognition (runs in background)."""
        frame_count = 0
        try:
            # Connect to DB before loop
            if not self._connect_db():
                self._update_status("Error: Database connection failed. Stopping.")
                # Signal GUI to reset buttons (need self.root.after)
                self.root.after(0, lambda: (
                    self.start_button.config(state="normal"),
                    self.stop_button.config(state="disabled")
                ))
                return # Stop thread if DB connection fails

            # Initialize camera
            self.video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Try CAP_DSHOW for Windows if default is slow
            if not self.video_capture or not self.video_capture.isOpened():
                 raise IOError("Cannot open webcam")

            self._update_status("Camera Ready. Recognizing...")
            self.marked_ids_today.clear() # Clear marked list for new session
            self.today_date_str = datetime.now().strftime("%d/%m/%Y")

            while not self.stop_event.is_set():
                ret, img = self.video_capture.read()
                if not ret or img is None:
                    print("Warning: Failed to grab frame.")
                    # self.stop_event.set() # Option: Stop if camera fails
                    continue

                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # For Pillow/Tkinter
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = self.faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5) # Adjust params if needed

                processed_img = img.copy() # Draw on a copy

                for (x, y, w, h) in features:
                    try:
                        # Predict face
                        face_roi = gray_image[y:y+h, x:x+w]
                        id_val, predict = self.clf.predict(face_roi)
                        confidence = int((100 * (1 - predict / 300))) # Adjust 300 based on training range if needed

                        details = None
                        display_text = "Unknown"
                        box_color = (0, 0, 255) # Red for unknown/low confidence

                        if confidence > 75: # Confidence threshold - ADJUST AS NEEDED
                            # Get details from DB
                            details = self._get_student_details(id_val)
                            if details:
                                display_text = f"{details['name']}"
                                box_color = (0, 255, 0) # Green for recognized
                                # Mark attendance if needed
                                self._mark_attendance_logic(details)
                            else:
                                display_text = f"ID:{id_val} (Not in DB)"
                                box_color = (0, 255, 255) # Yellow for recognized ID but no DB entry
                        else:
                             display_text = "Unknown" # Low confidence

                        # Draw rectangle and text
                        cv2.rectangle(processed_img, (x, y), (x + w, y + h), box_color, 2)
                        cv2.putText(processed_img, display_text, (x, y - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, box_color, 2)
                        if details and confidence > 75:
                            # Add optional extra info
                             cv2.putText(processed_img, f"ID: {details['id']}", (x, y + h + 15), cv2.FONT_HERSHEY_PLAIN, 0.9, (255,255,255), 1)
                             cv2.putText(processed_img, f"Roll: {details['roll']}", (x, y + h + 30), cv2.FONT_HERSHEY_PLAIN, 0.9, (255,255,255), 1)


                    except cv2.error as cv_err:
                         print(f"OpenCV error during prediction/drawing: {cv_err}")
                    except Exception as e:
                         print(f"Error processing face at ({x},{y}): {e}")


                # --- Update Tkinter UI ---
                # Convert processed frame for Tkinter
                img_tk = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_tk)

                 # Resize to fit label while maintaining aspect ratio (optional but recommended)
                label_w = self.video_label.winfo_width()
                label_h = self.video_label.winfo_height()
                if label_w > 1 and label_h > 1: # Ensure label has dimensions
                     img_pil.thumbnail((label_w, label_h), Image.Resampling.LANCZOS)

                photo_image = ImageTk.PhotoImage(image=img_pil)

                # Schedule the update on the main thread
                self.root.after(0, self._update_video_label, photo_image)

                frame_count += 1


        except IOError as e:
            print(f"Camera Error: {e}")
            self._update_status(f"Error: {e}")
        except Exception as e:
            print(f"Error in recognition loop: {e}")
            self._update_status(f"Error: Recognition loop failed.")
            import traceback
            traceback.print_exc() # Print full traceback to console
        finally:
            # --- Cleanup ---
            print("Recognition loop finished. Cleaning up...")
            if self.video_capture:
                self.video_capture.release()
                self.video_capture = None
            self._disconnect_db() # Disconnect DB when loop ends

            # Schedule button/status reset on main thread
            final_status = "Recognition Stopped." if self.stop_event.is_set() else "Recognition Finished/Error."
            self.root.after(0, lambda: (
                self.start_button.config(state="normal"),
                self.stop_button.config(state="disabled"),
                self.current_status.set(final_status),
                # Optionally clear video label - THIS LINE IS SUFFICIENT
                self.video_label.config(image='')
            ))
            print("Cleanup complete.")


if __name__ == "__main__":
    root = ThemedTk(theme="clam")
    app = Face_Recognition(root)
    root.mainloop()