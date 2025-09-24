# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import webbrowser

# class Developer:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1500x790+0+0")
#         self.root.title("Developer")

#         title_lbl=Label(self.root,text="DEVELOPER CONSOLE",font=("Times New Roman",40,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1600,height=55)

#         img_top=Image.open(r".\Images\developer2.png")
#         img_top=img_top.resize((1600,600),Image.Resampling.LANCZOS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)
#         first_lbl=Label(self.root,image=self.photoimg_top)
#         first_lbl.place(x=0,y=60,width=1600,height=600)

#         main_frame=Frame(self.root,bd=2,bg="white")
#         main_frame.place(x=0,y=605,width=1600,height=600)

#         # Displaying information of the team
#         people_info = [
#             {"name": "Anshu Priya", "email": "anshup.it.20@nitj.ac.in", "phone": "7903419622"},
#             {"name": "Neha Meensa", "email": "neham.it.20@nitj.ac.in", "phone": "9340499112"},
#             {"name": "Anu Bala", "email": "anub.it.20@nitj.ac.in", "phone": "9056484223"},
#             {"name": "Abhishek Tyagi", "email": "abhishektyagi9875@gmail.com", "phone": "9875066610"}
#         ]

#         for idx, person in enumerate(people_info, start=1):
#             person_lbl = Label(main_frame, text=f"Person {idx}:", font=("Arial", 18), bg="white")
#             person_lbl.grid(row=idx, column=0, padx=20, pady=10, sticky="w")

#             name_lbl = Label(main_frame, text=f"Name: {person['name']}", font=("Arial", 14), bg="white")
#             name_lbl.grid(row=idx, column=1, padx=20, pady=10, sticky="w")

#             email_lbl = Label(main_frame, text=f"Email: {person['email']}", font=("Arial", 14), bg="white", fg="blue", cursor="hand2")
#             email_lbl.grid(row=idx, column=2, padx=20, pady=10, sticky="w")
#             email_lbl.bind("<Button-1>", lambda e, email=person['email']: self.open_email(email))

#             phone_lbl = Label(main_frame, text=f"Phone: {person['phone']}", font=("Arial", 14), bg="white")
#             phone_lbl.grid(row=idx, column=3, padx=20, pady=10, sticky="w")


#     def open_email(self, email):
#         webbrowser.open_new("mailto:" + email)


# if __name__=="__main__":
#     root=Tk()
#     obj=Developer(root)
#     root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser
from ttkthemes import ThemedTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(self.root)
        try:
            selected_theme = "clam"
            self.root.set_theme(selected_theme)
            print(f"Using theme: {selected_theme}")
        except tk.TclError:
            print("ttkthemes theme not found or Tcl error, using default.")
            self.style.theme_use('clam')

        self.root.title("Meet the Developers")
        min_width = 800
        min_height = 550
        self.root.minsize(min_width, min_height)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initial_width = int(screen_width * 0.6)
        initial_height = int(screen_height * 0.6)
        x_cord = int((screen_width / 2) - (initial_width / 2))
        y_cord = int((screen_height / 2) - (initial_height / 2))
        self.root.geometry(f"{initial_width}x{initial_height}+{x_cord}+{y_cord}")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.configure_styles()
        self.create_ui()

    def configure_styles(self):
        """Configure ttk styles."""
        style = self.style

        primary_color = "#6f42c1" # A nice purple
        secondary_color = "#6c757d" # Gray
        link_color = "#0056b3"
        link_hover_color = "#003f7f"
        light_bg = style.lookup('TFrame', 'background')
        card_bg = "#ffffff" # White background for cards
        text_color = style.lookup('TLabel', 'foreground')
        button_fg = "#ffffff"
        button_bg = "#5a3d9e" # Slightly darker purple for buttons
        button_hover_bg = "#4a3282"

        style.configure("TFrame", background=light_bg)
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground=primary_color, anchor="center", background=light_bg)

        # --- Configure the standard TLabelframe style for the card appearance ---
        # Note: This will affect ALL default TLabelframes. If you need other
        #       LabelFrames with different styles, create a derived style later.
        style.configure("TLabelframe", background=card_bg, borderwidth=1, relief="solid", padding=(15,10))
        # Configure the label *within* the standard TLabelframe
        style.configure("TLabelframe.Label", font=("Helvetica", 12, "bold"), foreground=primary_color, background=card_bg)

        # --- Styles for elements INSIDE the card ---
        style.configure("Name.TLabel", font=("Helvetica", 14, "bold"), background=card_bg, anchor="w")
        style.configure("Role.TLabel", font=("Helvetica", 10, "italic"), background=card_bg, foreground=secondary_color, anchor="w")
        style.configure("Info.TLabel", font=("Helvetica", 10), background=card_bg, anchor="w")
        style.configure("Link.TLabel", font=("Helvetica", 10, "underline"), background=card_bg, foreground=link_color, anchor="w", cursor="hand2")
        # Style for the inner frame holding contact details
        style.configure("CardInner.TFrame", background=card_bg)

        # Style for Buttons linking externally
        style.configure("Accent.TButton", font=("Helvetica", 10),
                        foreground=button_fg, background=button_bg, padding=(8, 4), borderwidth=0)
        style.map("Accent.TButton",
                  background=[('active', button_hover_bg), ('!disabled', button_bg), ('hover', button_hover_bg)],
                  foreground=[('active', button_fg)])

    def create_ui(self):
        """Creates the main UI elements."""
        style = self.style

        title_lbl = ttk.Label(self.root, text="DEVELOPER TEAM", style="Title.TLabel")
        title_lbl.grid(row=0, column=0, pady=(20, 10), sticky="ew")

        content_frame = ttk.Frame(self.root, padding=(20, 10))
        content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        developer_info = [
            {"name": "Abhishek Tyagi", "role": "Project Lead | Full Stack Developer", "email": "abhishektyagi9875@gmail.com", "phone": "7589641230", "linkedin": "https://www.linkedin.com/in/abhishektyagi9875/"},
            {"name": "Anshu Priya", "role": "Backend Developer | ML Engineer", "email": "anshup.it.20@nitj.ac.in", "phone": "7894561230", "linkedin": "https://www.linkedin.com/in/..." },
            {"name": "Neha Meena", "role": "Frontend Developer | UI/UX", "email": "neham.it.20@nitj.ac.in", "phone": "9685741023", "linkedin": "https://www.linkedin.com/in/..."},
            {"name": "Anu Bala", "role": "Database Administrator | QA Tester", "email": "anub.it.20@nitj.ac.in", "phone": "8974561203", "linkedin": "https://www.linkedin.com/in/..." }
        ]

        num_cols = 2
        for i in range(num_cols):
            content_frame.grid_columnconfigure(i, weight=1, uniform="card_group", minsize=300)

        for idx, person in enumerate(developer_info):
            row = idx // num_cols
            col = idx % num_cols

            # --- Use the standard style name "TLabelframe" ---
            # The appearance comes from style.configure("TLabelframe", ...) defined above
            card_frame = ttk.LabelFrame(content_frame, text=f" Developer #{idx+1} ", style="TLabelframe") # padding is now part of style config
            card_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            card_frame.grid_columnconfigure(0, weight=1)

            # --- Card Content ---
            name_lbl = ttk.Label(card_frame, text=person['name'], style="Name.TLabel")
            name_lbl.grid(row=1, column=0, sticky="w")

            role_lbl = ttk.Label(card_frame, text=person['role'], style="Role.TLabel")
            role_lbl.grid(row=2, column=0, sticky="w", pady=(0, 8))

            # --- Contact Info within the card ---
            # Use the specific "CardInner.TFrame" style configured above
            contact_frame = ttk.Frame(card_frame, style="CardInner.TFrame", padding=(0, 5))
            contact_frame.grid(row=3, column=0, sticky="ew")
            contact_frame.grid_columnconfigure(0, weight=0)
            contact_frame.grid_columnconfigure(1, weight=1)

            # Email
            email_icon = ttk.Label(contact_frame, text="📧", style="Info.TLabel")
            email_icon.grid(row=0, column=0, sticky="w", padx=(0,5))
            email_link_lbl = ttk.Label(contact_frame, text=person['email'], style="Link.TLabel")
            email_link_lbl.grid(row=0, column=1, sticky="w")
            email_link_lbl.bind("<Button-1>", lambda e, email=person['email']: self.open_email(email))
            email_link_lbl.bind("<Enter>", lambda e, lbl=email_link_lbl: lbl.config(font=("Helvetica", 10, "underline", "bold")))
            email_link_lbl.bind("<Leave>", lambda e, lbl=email_link_lbl: lbl.config(font=("Helvetica", 10, "underline")))

            # Phone
            phone_icon = ttk.Label(contact_frame, text="📞", style="Info.TLabel")
            phone_icon.grid(row=1, column=0, sticky="w", padx=(0,5), pady=(2,0))
            phone_lbl = ttk.Label(contact_frame, text=person['phone'], style="Info.TLabel")
            phone_lbl.grid(row=1, column=1, sticky="w", pady=(2,0))

            # LinkedIn Button (Optional)
            if person.get('linkedin'):
                linkedin_btn = ttk.Button(card_frame, text="LinkedIn Profile", style="Accent.TButton", width=20,
                                           command=lambda url=person['linkedin']: self.open_link(url))
                linkedin_btn.grid(row=4, column=0, pady=(10, 5), sticky="w")

    # --- Action Methods --- (No changes needed here)
    def open_link(self, url):
        if not url or not url.startswith(('http://', 'https://')):
             messagebox.showwarning("Invalid URL", "Developer profile URL is missing or invalid.", parent=self.root)
             return
        try:
            print(f"Opening URL: {url}")
            webbrowser.open_new(url)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open link:\n{e}", parent=self.root)

    def open_email(self, email_address):
        if not email_address:
             messagebox.showwarning("Missing Info", "Email address is not available.", parent=self.root)
             return
        try:
            print(f"Opening mailto: {email_address}")
            webbrowser.open_new(f"mailto:{email_address}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open email client:\n{e}", parent=self.root)

if __name__ == "__main__":
    root = ThemedTk(theme="clam")
    obj = Developer(root)
    root.mainloop()