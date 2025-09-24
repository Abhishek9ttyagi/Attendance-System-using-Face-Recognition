# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import webbrowser

# class Help:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1500x790+0+0")
#         self.root.title("HelpDesk")

#         title_lbl = Label(self.root, text="24X7 HELP DESK", font=("Times New Roman", 40, "bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=2000, height=55)

#         img_top = Image.open(r".\Images\helpDesk.jpg")
#         img_top = img_top.resize((2000, 1200), Image.Resampling.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         first_lbl = Label(self.root, image=self.photoimg_top)
#         first_lbl.place(x=0, y=60, width=2000, height=1200)

#         # Description of the help desk
#         help_description = "Welcome to our 24x7 Help Desk!\n\nWe are here to assist you with any inquiries or issues you may have. For immediate assistance, please contact us via email at support@example.com."

#         # Create a label to display the description
#         self.description_lbl = Label(self.root, text=help_description, font=("Arial", 14), bg="white", fg="black", justify="left", bd=4, relief="solid", wraplength=1000)
#         self.description_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

#         # Create and display a clickable email link
#         email_lbl = Label(self.root, text="support@example.com", font=("Arial", 14, "underline"), bg="white", fg="blue", cursor="hand2")
#         email_lbl.place(relx=0.5, rely=0.6, anchor=CENTER)
#         email_lbl.bind("<Button-1>", lambda e: self.open_email())

#     def open_email(self):
#         webbrowser.open_new("mailto:support@example.com")


# if __name__ == "__main__":
#     root = Tk()
#     obj = Help(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser # For opening links
from ttkthemes import ThemedTk # Import ThemedTk

class Help:
    def __init__(self, root):
        self.root = root
        # Apply theme
        style = ttk.Style(self.root)
        try:
            selected_theme = "clam" # <-- CHANGE THEME HERE ('arc', 'equilux', etc.)
            self.root.set_theme(selected_theme)
            print(f"Using theme: {selected_theme}")
        except tk.TclError:
            print("ttkthemes theme not found or Tcl error, using default.")
            style.theme_use('clam') # Fallback theme

        self.root.title("Help Desk & Support")
        # Set minimum size and allow resizing
        min_width = 700
        min_height = 500
        self.root.minsize(min_width, min_height)

        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.5)
        initial_height = int(screen_height * 0.5)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")

        # --- Configure root grid layout for centering ---
        self.root.grid_columnconfigure(0, weight=1) # Allow content column to expand
        self.root.grid_rowconfigure(0, weight=0)    # Title row (fixed height)
        self.root.grid_rowconfigure(1, weight=1)    # Content row (expandable)
        self.root.grid_rowconfigure(2, weight=0)    # Padding/footer row

        # --- Style Configuration ---
        self.configure_styles(style)

        # --- Create UI Elements ---
        self.create_ui()


    def configure_styles(self, style):
        """Configure ttk styles."""
        primary_color = "#007bff" # Standard blue
        secondary_color = "#6c757d" # Gray
        link_color = "#0056b3"     # Darker blue for links
        link_hover_color = "#003f7f" # Even darker on hover
        light_bg = style.lookup('TFrame', 'background')
        text_color = style.lookup('TLabel', 'foreground')
        button_fg = "#ffffff"
        button_hover_bg = "#0056b3"

        style.configure("TFrame")
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground=primary_color, anchor="center")
        style.configure("Description.TLabel", font=("Helvetica", 11), anchor="center", padding=(0, 10))
        style.configure("Link.TLabel", font=("Helvetica", 11, "underline"), foreground=link_color, anchor="center", cursor="hand2")
        style.configure("Header.TLabel", font=("Helvetica", 12, "bold"), padding=(0, 5))

        # Style for Buttons linking externally (can look like links or buttons)
        style.configure("Accent.TButton", font=("Helvetica", 11, "bold"),
                        foreground=button_fg, background=primary_color, padding=(10, 5))
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', primary_color), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])

        # Configure hover effect for Link Labels (by changing foreground color)
        # Note: Changing font dynamically is trickier with ttk styles alone, often handled in event bindings
        # We'll use foreground color change here for simplicity via mapping if possible,
        # or handle font change in on_enter/on_leave bindings.

    def create_ui(self):
        """Creates the main UI elements."""
        # --- Title ---
        title_lbl = ttk.Label(self.root, text="Help Desk & Support", style="Title.TLabel")
        title_lbl.grid(row=0, column=0, pady=(20, 10), sticky="ew")

        # --- Content Frame (holds text and links/buttons) ---
        content_frame = ttk.Frame(self.root, padding=(20, 10))
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=10)
        content_frame.grid_columnconfigure(0, weight=1) # Center content horizontally

        # Description Text
        help_description = ("Welcome to the Help Desk!\n\n"
                            "If you encounter any issues or have questions about using the system, "
                            "please refer to the resources below or contact support directly.")
        description_lbl = ttk.Label(content_frame, text=help_description, style="Description.TLabel", justify="center", wraplength=self.root.winfo_width()-100) # Adjust wraplength
        # Update wraplength when window resizes
        description_lbl.bind('<Configure>', lambda e: description_lbl.config(wraplength=content_frame.winfo_width()-40))
        description_lbl.grid(row=0, column=0, pady=(10, 20), sticky="ew")


        # --- Links/Buttons Section ---
        links_frame = ttk.LabelFrame(content_frame, text="Resources", style="TLabelframe", padding=(15, 10))
        links_frame.grid(row=1, column=0, pady=20, sticky="ew")
        links_frame.grid_columnconfigure(0, weight=1) # Center items inside

        # Documentation Button/Link
        docs_btn = ttk.Button(links_frame, text="View Documentation", command=self.open_docs, style="Accent.TButton", width=25, cursor="hand2")
        docs_btn.grid(row=0, column=0, pady=5)

        # FAQ Button/Link
        faq_btn = ttk.Button(links_frame, text="Frequently Asked Questions (FAQ)", command=self.open_faq, style="Accent.TButton", width=25, cursor="hand2")
        faq_btn.grid(row=1, column=0, pady=5)

        # Email Contact Label
        email_frame = ttk.Frame(links_frame) # Frame to hold label and link together
        email_frame.grid(row=2, column=0, pady=(15, 5))

        contact_lbl = ttk.Label(email_frame, text="For further assistance, email us at:", font=("Helvetica", 11))
        contact_lbl.pack(side=tk.LEFT, padx=(0, 5))

        # Create a clickable email link Label
        email_link_lbl = ttk.Label(email_frame, text="support@example.com", style="Link.TLabel")
        email_link_lbl.pack(side=tk.LEFT)
        email_link_lbl.bind("<Button-1>", lambda e: self.open_email("support@example.com"))
        # Add hover effects (optional: change color or font underline)
        email_link_lbl.bind("<Enter>", lambda e: email_link_lbl.config(font=("Helvetica", 11, "underline", "bold"))) # Example font change
        email_link_lbl.bind("<Leave>", lambda e: email_link_lbl.config(font=("Helvetica", 11, "underline"))) # Revert font change


    # --- Action Methods ---

    def open_link(self, url):
        """Opens a given URL in the default web browser."""
        try:
            print(f"Opening URL: {url}")
            webbrowser.open_new(url)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open link:\n{e}", parent=self.root)

    def open_docs(self):
        """Opens the documentation link."""
        # --- REPLACE WITH YOUR ACTUAL DOCUMENTATION URL ---
        docs_url = "https://www.example.com/docs"
        self.open_link(docs_url)

    def open_faq(self):
        """Opens the FAQ link."""
        # --- REPLACE WITH YOUR ACTUAL FAQ URL ---
        faq_url = "https://www.example.com/faq"
        self.open_link(faq_url)

    def open_email(self, email_address):
        """Opens the default email client to compose a message."""
        try:
            print(f"Opening mailto: {email_address}")
            webbrowser.open_new(f"mailto:{email_address}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open email client:\n{e}", parent=self.root)


if __name__ == "__main__":
    root = ThemedTk(theme="clam") # Choose theme
    # If issues with ThemedTk:
    # root = tk.Tk()
    obj = Help(root)
    root.mainloop()