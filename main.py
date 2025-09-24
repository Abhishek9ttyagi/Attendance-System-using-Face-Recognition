
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from ttkthemes import ThemedTk # Import ThemedTk

# --- Import your other module classes ---
# Make sure these files exist and have the correct classes
try:
    from student import Student
    from train import Train
    from face_recognition import Face_Recognition
    from attendancePage import Attendance
    from developer import Developer
    from help import Help
except ImportError as e:
    messagebox.showerror("Import Error", f"Failed to import module: {e}\nPlease ensure student.py, train.py, etc., are in the same directory or Python path.")
    # You might want to exit or disable buttons if imports fail
    # For now, we'll define dummy classes so the main app can run
    class Student: pass
    class Train: pass
    class Face_Recognition: pass
    class Attendance: pass
    class Developer: pass
    class Help: pass
# --- End Import ---

class Face_Recognition_System:

    def __init__(self, root):
        self.root = root
        # Use ThemedTk - choose a theme ('arc', 'equilux', 'plastik', 'clam', 'vista', etc.)
        
        # Store PhotoImage objects to prevent garbage collection
        self.image_references = []
        
        # self.root = ThemedTk(theme="arc") # Or apply theme to existing root
        style = ttk.Style(self.root)
        # --- Choose a Theme ---
        # Print available themes: print(style.theme_names())
        try:
            # Try a modern theme
            # Common good themes: 'clam', 'alt', 'default', 'classic',
            # From ttkthemes: 'arc', 'equilux', 'plastik', 'adapta', 'ubuntu', 'radiance'
            selected_theme = "clam" # <-- CHANGE THEME HERE IF YOU WANT
            self.root.set_theme(selected_theme)
            print(f"Using theme: {selected_theme}")
        except tk.TclError:
            print("ttkthemes theme not found, using default.")
            # Fallback theme if ttkthemes isn't installed properly or theme missing
            # style.theme_use('clam') # Good fallback

        self.root.title("Attendance System")
        # Set minimum size and allow resizing - more responsive
        min_width = 1200
        min_height = 700
        self.root.minsize(min_width, min_height)

        # Get screen dimensions for initial centering/sizing (optional)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Start maximized or near-maximized
        # self.root.state('zoomed') # Platform specific, might not work everywhere
        # Or set geometry closer to screen size
        initial_width = int(screen_width * 0.9)
        initial_height = int(screen_height * 0.9)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")


        # Configure root grid layout
        self.root.grid_rowconfigure(1, weight=1)  # Main content row expands
        self.root.grid_columnconfigure(0, weight=1) # Main content column expands

        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Header Frame ---
        self.create_header()

        # --- Main Content Frame (Buttons) ---
        self.create_main_content()

        # --- Footer Frame (Time) ---
        self.create_footer()


    def configure_styles(self, style):
        """Configure ttk styles for widgets."""
        # Define some colors (adapt as needed)
        primary_color = "#0d6efd" # Bootstrap primary blue
        light_bg = "#f8f9fa"     # Light gray background
        dark_text = "#212529"    # Dark text
        header_bg = "#ffffff"    # White header
        button_hover_bg = "#e9ecef" # Light gray for hover

        style.configure("TFrame", background=light_bg)
        style.configure("Header.TFrame", background=header_bg)
        style.configure("Footer.TFrame", background=header_bg)

        style.configure("Title.TLabel", background=header_bg, foreground=primary_color,
                        font=("Helvetica", 28, "bold"), anchor="center")
        style.configure("Time.TLabel", background=header_bg, foreground=dark_text,
                        font=("Helvetica", 12))

        # Style for the main buttons
        style.configure("Card.TButton", font=("Helvetica", 12, "bold"),
                        foreground=dark_text, background=header_bg,
                        borderwidth=1, relief="raised", anchor="center",
                        padding=(10, 10)) # Padding inside button
        style.map("Card.TButton",
                  background=[('active', primary_color), ('!disabled', header_bg), ('hover', button_hover_bg)],
                  foreground=[('active', 'white')])

        # Style for button text labels (if used separately - now integrated)
        style.configure("CardText.TLabel", background=light_bg, foreground=primary_color,
                        font=("Helvetica", 14, "bold"), anchor="center")


    def create_header(self):
        """Creates the header section with title and optional banner."""
        header_frame = ttk.Frame(self.root, style="Header.TFrame", padding=(10, 5))
        header_frame.grid(row=0, column=0, sticky="ew") # Span across width
        header_frame.grid_columnconfigure(0, weight=1) # Allow title to center

        # --- Optional Banner Image ---
        try:
            # Use a single wider banner image if available
            img_banner = Image.open(r".\Images\background_img.jpg") # Adjust path/filename
            # Resize banner intelligently, keep aspect ratio if possible
            banner_height = 80 # Target height
            aspect_ratio = img_banner.width / img_banner.height
            banner_width = int(banner_height * aspect_ratio)
            img_banner = img_banner.resize((banner_width, banner_height), Image.Resampling.LANCZOS)
            self.photoimg_banner = ImageTk.PhotoImage(img_banner)
            self.image_references.append(self.photoimg_banner) # Keep reference

            banner_lbl = ttk.Label(header_frame, image=self.photoimg_banner, style="Header.TLabel")
            # Place banner - adjust grid column/row if needed, or use pack
            # banner_lbl.grid(row=0, column=0, pady=(0, 10)) # Example placement
        except FileNotFoundError:
            print("Banner image not found, skipping.")
        except Exception as e:
            print(f"Error loading banner image: {e}")
        # --- End Banner ---


        # --- Main Title ---
        title_lbl = ttk.Label(header_frame, text="Face Recognition Attendance System", style="Title.TLabel")
        # Place below banner or adjust grid accordingly
        title_lbl.grid(row=1, column=0, pady=(5, 5), sticky="ew")


    def create_main_content(self):
        """Creates the central area with function buttons."""
        main_frame = ttk.Frame(self.root, style="TFrame", padding=20)
        main_frame.grid(row=1, column=0, sticky="nsew")

        # Configure grid columns and rows within the main frame to be responsive
        num_cols = 4
        num_rows = 2
        for i in range(num_cols):
            main_frame.grid_columnconfigure(i, weight=1, uniform="button_group")
        for i in range(num_rows):
            main_frame.grid_rowconfigure(i, weight=1, uniform="button_group")

        # --- Buttons Data (Text, Image Path, Command) ---
        button_data = [
            ("Student Details", r".\Images\btn1_img.jpg", self.student_details),
            ("Face Detection", r".\Images\btn2_img.png", self.face_data),
            ("Attendance", r".\Images\btn3_img.png", self.attendance_report),
            ("Help Desk", r".\Images\btn4_img.png", self.help_desk),
            ("Train Model", r".\Images\btn5_img.jpg", self.train_data),
            ("Photos Folder", r".\Images\btn6_img.png", self.open_img),
            ("Developer", r".\Images\btn7_img.jpg", self.developer_data),
            ("Exit", r".\Images\btn8_img.png", self.exit_func)
        ]

        # --- Create Buttons using a loop and helper function ---
        button_size = (120, 120) # Desired image size within buttons
        for idx, (text, img_path, command) in enumerate(button_data):
            row = idx // num_cols
            col = idx % num_cols
            btn = self._create_button(main_frame, text, img_path, command, button_size)
            # Add padding around each button and make it fill its cell
            btn.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

    def _create_button(self, parent, text, image_path, command, size):
        """Helper function to create a styled button with an image."""
        try:
            img = Image.open(image_path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            self.image_references.append(photo_img) # Keep reference!

            button = ttk.Button(parent, text=text, image=photo_img,
                                command=command, style="Card.TButton",
                                compound=tk.TOP, # Place image above text
                                cursor="hand2")
            button.image = photo_img # Keep reference on widget itself too
            return button

        except FileNotFoundError:
            print(f"Warning: Image not found at {image_path}. Creating text-only button.")
            button = ttk.Button(parent, text=text, command=command,
                                style="Card.TButton", cursor="hand2")
            return button
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            button = ttk.Button(parent, text=text + " (Img Err)", command=command,
                                style="Card.TButton", cursor="hand2")
            return button


    def create_footer(self):
        """Creates the footer section with the time display."""
        footer_frame = ttk.Frame(self.root, style="Footer.TFrame", padding=(10, 5))
        footer_frame.grid(row=2, column=0, sticky="ew") # Span across width
        footer_frame.grid_columnconfigure(0, weight=1) # Allow time to center or align

        self.time_lbl = ttk.Label(footer_frame, font=("Helvetica", 12), style="Time.TLabel")
        self.time_lbl.grid(row=0, column=0, sticky='e', padx=10) # Align right
        self.update_time()


    def update_time(self):
        """Updates the time label every second."""
        string = strftime(" %I:%M:%S %p ") # 12-hour format with AM/PM
        self.time_lbl.config(text=string)
        self.time_lbl.after(1000, self.update_time) # Schedule next update


    # ================= Button Command Functions ==================
    # (These remain largely the same, opening new Toplevel windows)

    def open_img(self):
        """Opens the 'data' directory."""
        try:
            # Use os.path.abspath to handle relative paths more robustly
            data_dir = os.path.abspath("data")
            if os.path.isdir(data_dir):
                os.startfile(data_dir)
            else:
                messagebox.showwarning("Not Found", f"Directory not found: {data_dir}")
        except Exception as e:
             messagebox.showerror("Error", f"Could not open directory:\n{e}")

    def _open_module_window(self, ModuleClass, title):
        """Helper function to open a Toplevel window for a module."""
        # Check if window already exists (optional, prevents multiple openings)
        # You might need a more robust way to track open windows if needed
        # if hasattr(self, f"win_{ModuleClass.__name__}") and self.win_... .winfo_exists():
        #    self.win_... .focus()
        #    return

        new_window = tk.Toplevel(self.root)
        new_window.title(title)
        # You might want to set geometry or minsize for these windows too
        # e.g., new_window.geometry("1000x600+50+50")
        app = ModuleClass(new_window)
        # Optional: store reference if needed
        # setattr(self, f"win_{ModuleClass.__name__}", new_window)

    def student_details(self):
        self._open_module_window(Student, "Student Management")

    def train_data(self):
        self._open_module_window(Train, "Train Model")

    def face_data(self):
        self._open_module_window(Face_Recognition, "Face Recognition")

    def attendance_report(self):
        self._open_module_window(Attendance, "Attendance Report")

    def developer_data(self):
        self._open_module_window(Developer, "Developer Information")

    def help_desk(self):
        self._open_module_window(Help, "Help Desk")

    def exit_func(self):
        """Confirms and exits the application."""
        if messagebox.askyesno("Exit Application", "Are you sure you want to exit?", parent=self.root):
            self.root.quit() # More graceful exit than destroy sometimes
            self.root.destroy()


if __name__ == "__main__":
    # Use ThemedTk for the root window to apply themes easily
    root = ThemedTk(theme="arc") # Choose your preferred theme here
    # If you don't want ThemedTk, use root = tk.Tk() and apply style manually in __init__
    app = Face_Recognition_System(root)
    root.mainloop()