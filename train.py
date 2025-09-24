# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# import face_recognition

# class Train:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("DatasetTraining")


#         title_lbl=Label(self.root,text="TRAIN DATASET",font=("Times New Roman",40,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=2000,height=55)

#         img_top=Image.open(r".\Images\trainDataset.jpg")
#         img_top=img_top.resize((2000,350),Image.Resampling.LANCZOS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)
#         first_lbl=Label(self.root,image=self.photoimg_top)
#         first_lbl.place(x=0,y=60,width=2000,height=350)
#         #button
#         b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Times New Roman",35,"bold"),bg="white",fg="blue")
#         b1_1.place(x=0,y=410,width=2000,height=45)


#         img_bottom=Image.open(r".\Images\people.jpeg")
#         img_bottom=img_bottom.resize((2000,350),Image.Resampling.LANCZOS)
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
#         first_lbl=Label(self.root,image=self.photoimg_bottom)
#         first_lbl.place(x=0,y=455,width=2000,height=350)


#     def train_classifier(self):
#         data_dir=("data")
#         path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

#         faces=[]
#         ids=[]

#         for image in path:
#             img=Image.open(image).convert('L')  #to convert into gray scale image
#             imageNp=np.array(img,'uint8')
#             id=int(os.path.split(image)[1].split('.')[1])

#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training",imageNp)
#             cv2.waitKey(1) == 13
#         ids=np.array(ids)

#         #train the classifier and save
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces,ids)
#         clf.write("classifier.xml")
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result","Training of datasets completed")




# if __name__=="__main__":
#     root=Tk()
#     obj=Train(root)
#     root.mainloop()


# #this code uses face_recognition library bcz the library used in video was not able to train dataset. This code is given by chatgpt
# # from tkinter import *
# # from tkinter import ttk
# # from PIL import Image, ImageTk
# # from tkinter import messagebox
# # import os
# # import numpy as np
# # import face_recognition
# # from sklearn import neighbors
# # import pickle

# # class Train:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry("2000x1000+0+0")
# #         self.root.title("DatasetTraining")

# #         title_lbl = Label(self.root, text="TRAIN DATASET", font=("Times New Roman", 40, "bold"), bg="white", fg="red")
# #         title_lbl.place(x=0, y=0, width=2000, height=55)

# #         img_top = Image.open(r"C:\Users\KRISHAN KUMAR SINGH\Desktop\MajorProject\Images\trainDataset.jpg")
# #         img_top = img_top.resize((2000, 350), Image.Resampling.LANCZOS)
# #         self.photoimg_top = ImageTk.PhotoImage(img_top)
# #         first_lbl = Label(self.root, image=self.photoimg_top)
# #         first_lbl.place(x=0, y=60, width=2000, height=350)

# #         # button
# #         b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
# #                       font=("Times New Roman", 35, "bold"), bg="white", fg="blue")
# #         b1_1.place(x=0, y=410, width=2000, height=45)

# #         img_bottom = Image.open(r"C:\Users\KRISHAN KUMAR SINGH\Desktop\MajorProject\Images\people.jpeg")
# #         img_bottom = img_bottom.resize((2000, 350), Image.Resampling.LANCZOS)
# #         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
# #         first_lbl = Label(self.root, image=self.photoimg_bottom)
# #         first_lbl.place(x=0, y=455, width=2000, height=350)

# #     def train_classifier(self):
# #         data_dir = "data"
# #         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

# #         faces = []
# #         ids = []

# #         for image in path:
# #             img = face_recognition.load_image_file(image)
# #             encoding = face_recognition.face_encodings(img)

# #             if len(encoding) > 0:
# #                 id = int(os.path.split(image)[1].split('.')[1])

# #                 faces.append(encoding[0])
# #                 ids.append(id)

# #         faces = np.array(faces)
# #         ids = np.array(ids)

# #         # Train the classifier and save
# #         clf = neighbors.KNeighborsClassifier(n_neighbors=1)
# #         clf.fit(faces, ids)

# #         with open("classifier.pkl", 'wb') as f:
# #             pickle.dump(clf, f)

# #         print("Training of datasets completed")


# # if __name__ == "__main__":
# #     root = Tk()
# #     obj = Train(root)
# #     root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import threading # Import threading
from ttkthemes import ThemedTk # Import ThemedTk

class Train:
    def __init__(self, root):
        self.root = root
        # Apply a theme using ThemedTk
        style = ttk.Style(self.root)

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

        self.root.title("Train Model")
        

        # Make window resizable (within limits if desired)
        min_width = 800
        min_height = 500
        self.root.minsize(min_width, min_height)

        # Center the window on launch (optional)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.6)
        initial_height = int(screen_height * 0.6)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")


        # --- Configure root grid layout for centering ---
        self.root.grid_columnconfigure(0, weight=1) # Column expands
        self.root.grid_rowconfigure(0, weight=1)    # Title row
        self.root.grid_rowconfigure(1, weight=3)    # Content/Feedback row
        self.root.grid_rowconfigure(2, weight=1)    # Button row
        self.root.grid_rowconfigure(3, weight=1)    # Padding row


        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Title ---
        title_lbl = ttk.Label(self.root, text="TRAIN DATASET", style="Title.TLabel")
        title_lbl.grid(row=0, column=0, pady=(20, 10), sticky="n")

        # --- Feedback Area Frame ---
        feedback_frame = ttk.Frame(self.root, style="TFrame")
        feedback_frame.grid(row=1, column=0, pady=20, padx=50, sticky="nsew")
        feedback_frame.grid_columnconfigure(0, weight=1) # Center content

        # Status Label
        self.status_var = tk.StringVar(value="Ready to train.")
        status_lbl = ttk.Label(feedback_frame, textvariable=self.status_var, style="Status.TLabel", wraplength=initial_width - 100) # Wrap text
        status_lbl.grid(row=0, column=0, pady=(10, 10))

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(feedback_frame, orient="horizontal",
                                            length=300, mode='determinate', variable=self.progress_var)
        self.progress_bar.grid(row=1, column=0, pady=(10, 20))


        # --- Action Button ---
        self.train_button = ttk.Button(self.root, text="TRAIN DATA", command=self.start_training_thread,
                                      style="Accent.TButton", width=20, cursor="hand2")
        self.train_button.grid(row=2, column=0, pady=20, sticky="n")

        # Store PhotoImage objects if needed (not using large bg images anymore)
        self.image_references = []


    def configure_styles(self, style):
        """Configure ttk styles."""
        primary_color = "#007bff"
        secondary_color = "#6c757d"
        light_bg = style.lookup('TFrame', 'background')
        text_color = style.lookup('TLabel', 'foreground')
        button_fg = "#ffffff"
        button_hover_bg = "#0056b3"

        style.configure("TFrame") # Use theme's default frame background
        style.configure("Title.TLabel", font=("Helvetica", 28, "bold"), foreground=primary_color, anchor="center")
        style.configure("Status.TLabel", font=("Helvetica", 12), anchor="center")
        style.configure("Accent.TButton", font=("Helvetica", 14, "bold"),
                        foreground=button_fg, background=primary_color, padding=(15, 8))
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', primary_color), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])
        # Style for disabled button
        style.map('Accent.TButton',
          foreground=[('disabled', secondary_color)],
          background=[('disabled', light_bg)])


    def start_training_thread(self):
        """Initiates the training process in a separate thread."""
        # Disable button immediately
        self.train_button.config(state="disabled")
        # Reset progress and status
        self._update_status("Starting training process...")
        self._update_progress(0)
        self.progress_bar.config(mode='determinate') # Ensure determinate mode

        # Create and start the background thread
        self.training_thread = threading.Thread(target=self._train_classifier_logic, daemon=True)
        self.training_thread.start()


    def _update_status(self, message):
        """Safely updates the status label from any thread."""
        self.root.after(0, self.status_var.set, message)

    def _update_progress(self, value):
        """Safely updates the progress bar from any thread."""
        self.root.after(0, self.progress_var.set, value)

    def _training_complete(self, message):
        """Actions to perform after successful training."""
        self._update_status(message)
        self._update_progress(100) # Fill progress bar
        self.train_button.config(state="normal") # Re-enable button
        messagebox.showinfo("Success", message, parent=self.root)

    def _training_error(self, error_message):
        """Actions to perform if training fails."""
        self._update_status(f"Error: {error_message}")
        self._update_progress(0) # Reset progress
        self.progress_bar.config(mode='determinate') # Ensure progress bar stops indeterminate mode if it was used
        self.train_button.config(state="normal") # Re-enable button
        messagebox.showerror("Training Error", error_message, parent=self.root)


    def _train_classifier_logic(self):
        """Contains the actual training logic (runs in background thread)."""
        data_dir = "data"
        classifier_file = "classifier.xml" # LBPH uses XML

        try:
            # --- Basic Checks ---
            if not os.path.isdir(data_dir):
                self._training_error(f"Data directory not found: '{data_dir}'")
                return

            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

            if not path:
                self._training_error(f"No images found in the data directory: '{data_dir}'")
                return

            self._update_status("Loading images and extracting IDs...")
            faces = []
            ids = []
            total_images = len(path)

            for i, image_path in enumerate(path):
                try:
                    # Update progress and status
                    progress = (i + 1) / total_images * 90 # Reserve last 10% for training itself
                    status_msg = f"Processing image {i+1}/{total_images}: {os.path.basename(image_path)}"
                    self._update_status(status_msg)
                    self._update_progress(progress)

                    # Open image in grayscale
                    img = Image.open(image_path).convert('L')
                    imageNp = np.array(img, 'uint8')

                    # Extract ID from filename (assuming format like user.ID.sample.jpg)
                    try:
                        filename = os.path.basename(image_path)
                        # Handle potential variations in filename format
                        parts = filename.split('.')
                        if len(parts) < 3 or not parts[1].isdigit():
                            print(f"Warning: Skipping file with unexpected name format: {filename}")
                            continue # Skip this image if ID cannot be extracted reliably
                        id_val = int(parts[1])
                    except (IndexError, ValueError) as e:
                         print(f"Warning: Could not parse ID from filename '{filename}': {e}. Skipping.")
                         continue # Skip this image

                    faces.append(imageNp)
                    ids.append(id_val)

                    # Brief pause to allow GUI updates (optional, can slow down processing)
                    # import time
                    # time.sleep(0.01)

                except Exception as img_err:
                     print(f"Warning: Error processing image {image_path}: {img_err}. Skipping.")
                     continue # Skip problematic images

            if not faces or not ids:
                 self._training_error("No valid faces/IDs found after processing images.")
                 return

            ids = np.array(ids)

            # --- Train the LBPH Classifier ---
            self._update_status("Training LBPH classifier...")
            self._update_progress(95) # Indicate training phase

            # Check if cv2.face is available
            if not hasattr(cv2, 'face') or not hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
                 self._training_error("cv2.face module not found. Ensure 'opencv-contrib-python' is installed.")
                 return

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write(classifier_file)

            self._update_progress(100)
            self._training_complete(f"Training complete. Classifier saved as '{classifier_file}'.")

        except Exception as e:
            self._training_error(f"An unexpected error occurred: {str(e)}")
            # Print traceback for debugging in console
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    # Use ThemedTk for easy theme application
    root = ThemedTk(theme="clam") # Choose theme
    # If issues with ThemedTk:
    # root = tk.Tk()
    obj = Train(root)
    root.mainloop()