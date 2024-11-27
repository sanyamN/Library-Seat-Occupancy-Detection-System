import tkinter
import customtkinter
from functions import is_valid_chars_space, is_valid_chars, check_security_answer, get_security_question, is_valid_email, get_countries, toggle_password, register_user, test_buttons, check_login, generate_temporary_password, send_password_reset_email, email_exists, update_password
from PIL import ImageTk, Image
from tkinter import messagebox
from test import *
import cv2

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.setup_login_frame()

    def setup_login_frame(self):

        #Create Login FRAME
        self.login_frame = customtkinter.CTkFrame(master=self, width=320, height=380)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #TOP text
        self.text = customtkinter.CTkLabel(master=self.login_frame, text="Log Into Account", font=('Century Gothic', 25))
        self.text.place(x=50, y=45)

        self.error_label = customtkinter.CTkLabel(master=self.login_frame, text="", font=('Century Gothic', 12), text_color="red")
        self.error_label.place(x=25, y=80)

        #Username entry block
        self.u_block = customtkinter.CTkEntry(master=self.login_frame, width=220, placeholder_text="Username")
        self.u_block.place(x=50, y=110)

        #Password entry block
        self.show_password_var = customtkinter.BooleanVar()
        self.p_block = customtkinter.CTkEntry(master=self.login_frame, width=220, placeholder_text="Password", show="*")
        self.p_block.place(x=50, y=150)

        #checkbox for showing password
        self.show_password = customtkinter.CTkCheckBox(master=self.login_frame, text="Show Password", font=('Century Gothic', 12), command=lambda: toggle_password(self.p_block, self.show_password_var), variable=self.show_password_var)
        self.show_password.place(x=50, y=190)

        #Forgot password text
        self.label3 = customtkinter.CTkLabel(master=self.login_frame, text="", font=('Century Gothic', 10))
        self.label3.place(x=180, y=180)
        self.label3.bind("<Enter>", lambda event: self.label3.configure(cursor="hand2"))
        # Change cursor back to the default arrow when mouse leaves the widget
        self.label3.bind("<Leave>", lambda event: self.label3.configure(cursor="arrow"))
        # Bind the click event to open the Forgot Password frame
        self.label3.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())

        #Login button
        self.login_button = customtkinter.CTkButton(master=self.login_frame, width=100, text="Login", corner_radius=6, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.check_login_credentials)
        self.login_button.place(x=110, y=230)

        #Register button
        self.register_button = customtkinter.CTkButton(master=self.login_frame, width=100, text="Register", corner_radius=6, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.master.open_register_frame)
        self.register_button.place(x=110, y=270)

        #Google and facebook logos
        self.g_logo = customtkinter.CTkImage(Image.open("images/g.png").resize((20, 20), Image.LANCZOS))
        self.fb_logo = customtkinter.CTkImage(Image.open("images/fb.png").resize((20, 20), Image.LANCZOS))

        #Google login button
        self.g_button = customtkinter.CTkButton(master=self.login_frame, width=100, image=self.g_logo, text="Google", corner_radius=6, fg_color="white", text_color="black", compound="left", hover_color="#f0f0f0", anchor="w", command=test_buttons)
        self.g_button.place(x=10, y=340)

        #Facebook login button
        self.fb_button = customtkinter.CTkButton(master=self.login_frame, width=100, image=self.fb_logo, text="Facebook", corner_radius=6, fg_color="white", text_color="black", compound="left", hover_color="#f0f0f0", anchor="w", command=test_buttons)
        self.fb_button.place(x=210, y=340)

    def check_login_credentials(self):
        # Get the username and password from the input fields
        username = self.u_block.get()
        password = self.p_block.get()

        # Call the check_login function from functions.py
        if check_login(username, password):
            # Login successful, open LoggedInFrame
            self.master.open_loggedin_frame()
        else:
            # Login failed, show an error message
            self.error_label.configure(text="Invalid username or password. Please try again.")

class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.setup_register_frame()

    def setup_register_frame(self):
        self.master.change_title("Registration")
        # Create the registration frame
        self.registration_frame = customtkinter.CTkFrame(master=self, width=320, height=380)
        self.registration_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.back_button = customtkinter.CTkButton(
            master=self,
            width=30,
            height=30,
            text="◀️",  # Use the left arrow character as the text
            corner_radius=6,
            fg_color="#3498db",
            text_color="#ffffff",
            hover_color="#2980b9",
            command=self.master.open_main_frame
        )
        self.back_button.place(x=10, y=10)

        # Entry fields for registration form
        self.name_entry = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="First Name")
        self.name_entry.place(x=50, y=50)

        self.surname_entry = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="Last Name")
        self.surname_entry.place(x=50, y=80)

        # Create a CTkOptionMenu for the country dropdown
        #self.country_var = customtkinter.StringVar(value="Select Country")
        #self.country_box = customtkinter.CTkComboBox(master=self.registration_frame, variable=self.country_var, values=get_countries(),
                                                        #width=220, state="readonly")
        #self.country_box.place(x=50, y=110)

        self.username_entry = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="Username")
        self.username_entry.place(x=50, y=110)

        self.email_entry = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="Enter your email")
        self.email_entry.place(x=50, y=140)

        self.p_block = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="Choose a password", show="*")
        self.p_block.place(x=50, y=170)

        self.security_question_label = customtkinter.CTkLabel(master=self.registration_frame, text="Security Question", font=('Century Gothic', 10))
        self.security_question_label.place(x=50, y=230)

        self.security_questions = ["What is your mother's maiden name?", "What is your favorite pet's name?", "Where were you born?", "What is your favorite movie?", "What is your favorite book?"]
        self.security_question_var = customtkinter.StringVar(value="Select Security Question")
        self.security_question_dropdown = customtkinter.CTkComboBox(master=self.registration_frame, variable=self.security_question_var, values=self.security_questions, width=220, state="readonly")
        self.security_question_dropdown.place(x=50, y=260)

        # Security Answer entry field
        self.security_answer_entry = customtkinter.CTkEntry(master=self.registration_frame, width=220, placeholder_text="Security Answer")
        self.security_answer_entry.place(x=50, y=290)

        # Registration button
        self.register_button = customtkinter.CTkButton(master=self.registration_frame, width=100, text="Register",
                                                  corner_radius=6,
                                                  fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9",
                                                  command=self.new_user_data)
        self.register_button.place(x=110, y=340)

    def new_user_data(self):
        # Get user inputs from the registration form
        first_name = self.name_entry.get()
        last_name = self.surname_entry.get()
        #country = self.country_box.get()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.p_block.get()
        security_question = self.security_question_var.get()  # Get the selected security question
        security_answer = self.security_answer_entry.get()

        if not first_name or not last_name or not username or not password:
            print("Please fill in all required fields.")
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
        if not is_valid_chars_space(first_name) or not is_valid_chars_space(last_name):
            print("Name and Surname must contain only English letters.")
            messagebox.showerror("Error", "Use Only English letters.")
            return
        # Check if fields contain only English letters and standard characters
        if not is_valid_chars(username) or not is_valid_chars(password):
            print("Fields must contain only English letters and standard characters.")
            messagebox.showerror("Error", "Use Only English letters and standard characters without spaces.")
            return
        #if country == "Select Country":
            #print("No country Selected")
            #messagebox.showerror("Error", "Please select a country.")
            #return
        if security_question == "Select Security Question":
            print("Invalid Security Question")
            messagebox.showerror("Error", "Invalid Security Question.")
            return
        if not is_valid_email(email):
            print("Invalid email address")
            messagebox.showerror("Error", "Please enter a valid email address.")
            return
        # Call the register_user function from functions.py
        if register_user(first_name, last_name,security_answer, username, email, password, security_question, security_answer):
            # Registration successful
            print("Registration successful!")
            messagebox.showinfo("Success", "Registration was successful!")
            self.registration_frame.place_forget()
            self.master.open_main_frame()
            return
        else:
            # Handle the case where the username or email is already taken
            print("Username or email is already in use.")
            messagebox.showerror("Error", "The username or e-mail already exists.")
            return


class ForgotPasswordFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_forgot_password_frame()  # Correct method name

    def setup_forgot_password_frame(self):  # Correct method name
        # Create the Forgot Password frame
        self.master.change_title("Forgot Password")
        self.forgot_password_frame = customtkinter.CTkFrame(master=self, width=320, height=380)
        self.forgot_password_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.back_button = customtkinter.CTkButton(
            master=self,
            width=30,
            height=30,
            text="◀️",  # Use the left arrow character as the text
            corner_radius=6,
            fg_color="#72bcd4",
            text_color="#1e5364",
            hover_color="#e8f4f8",
            command=self.master.open_main_frame
        )
        self.back_button.place(x=10, y=10)

        self.text = customtkinter.CTkLabel(master=self.forgot_password_frame, text="Enter Your E-Mail", font=('Century Gothic', 25))
        self.text.place(x=50, y=45)
        # Email entry block
        self.email_block = customtkinter.CTkEntry(master=self.forgot_password_frame, width=220, placeholder_text="Email")
        self.email_block.place(x=50, y=110)
        # Submit button
        self.submit_button = customtkinter.CTkButton(master=self.forgot_password_frame, width=100, text="Submit", corner_radius=6, fg_color="#72bcd4", text_color="#1e5364", hover_color="#e8f4f8", command=self.handle_reset_password)
        self.submit_button.place(x=110, y=230)

    def handle_reset_password(self):
        # Get the user's email address from the entry field
        user_email = self.email_block.get()
        check_exists = email_exists(user_email)
        security_question = get_security_question(user_email)
        if not is_valid_email(user_email):
            print("Invalid email address")
            messagebox.showerror("Error", "Please enter a valid email address.")
            return
        if check_exists:
            # Remove the ForgotPasswordFrame and show the next step/frame
            self.master.destroy_all_frames()
            self.master.open_forgot_password_frame2(user_email)
        else:
            messagebox.showerror("Error", "E-Mail doesn't exists!")
            return

class ForgotPasswordFrame2(customtkinter.CTkFrame):
    def __init__(self, master, user_email):
        super().__init__(master)
        self.master = master
        self.user_email = user_email
        self.setup_forgot_password_frame2()

    def setup_forgot_password_frame2(self):
        # Create the Forgot Password step 2 frame
        self.master.change_title("Forgot Password - Step 2")
        self.forgot_password2_frame = customtkinter.CTkFrame(master=self, width=320, height=380)
        self.forgot_password2_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.back_button = customtkinter.CTkButton(
            master=self,
            width=30,
            height=30,
            text="◀️",  # Use the left arrow character as the text
            corner_radius=6,
            fg_color="#72bcd4",
            text_color="#1e5364",
            hover_color="#e8f4f8",
            command=self.master.open_main_frame
        )
        self.back_button.place(x=10, y=10)

        self.text = customtkinter.CTkLabel(master=self.forgot_password2_frame, text="Step 2", font=('Century Gothic', 25))
        self.text.place(x=50, y=45)

        # Security Question entry block
        security_question = get_security_question(self.user_email)  # You can pass user_email here or retrieve it from somewhere
        self.security_question_label = customtkinter.CTkLabel(master=self.forgot_password2_frame, text=security_question, font=('Century Gothic', 14))
        self.security_question_label.place(x=50, y=110)

        # Security Answer entry block
        self.security_answer_block = customtkinter.CTkEntry(master=self.forgot_password2_frame, width=220, placeholder_text="Security Answer")
        self.security_answer_block.place(x=50, y=160)

        # Submit button for step 2
        #self.submit_button2 = customtkinter.CTkButton(master=self.forgot_password2_frame, width=100, text="Reset Password", corner_radius=6, fg_color="#72bcd4", text_color="#1e5364", hover_color="#e8f4f8", command=self.handle_reset_password)
        #self.submit_button2.place(x=110, y=230)

    def handle_reset_password(self):
        # Get the user's security answer
        user_answer = self.security_answer_block.get()

        # Check if the security answer is correct
        if check_security_answer(self.user_email, user_answer):  # Pass user_email here or retrieve it from somewhere
            # Generate a temporary password (or token)
            temporary_password = generate_temporary_password()
            update_password(self.user_email, temporary_password)  # Pass user_email here or retrieve it from somewhere
            # Send the password reset email
            send_password_reset_email(self.user_email, temporary_password)  # Pass user_email here or retrieve it from somewhere
            # Inform the user (you can customize this part)
            messagebox.showinfo("Password Reset", "An email with instructions has been sent to your email address.")

            # Remove the ForgotPassword2Frame and show the login frame again
            self.master.destroy_all_frames()
            self.master.open_main_frame()
        else:
            messagebox.showerror("Error", "Security answer does not match.")

class LoggedInFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_loggedin_frame()

    def setup_loggedin_frame(self):
        self.occupied_count=0
        self.unoccupied_count=0
        self.total_count=0
        self.master.change_geometry("1280x720")
        self.im=ImageTk.PhotoImage(Image.open("images/logo.png"))
        customtkinter.CTkLabel(master=self,image=self.im).place(x=120,y=30)
        
        self.loggedin_frame1=customtkinter.CTkFrame(master=self, width=500, height=500)
        self.loggedin_frame1.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
        self.loggedin_frame2=customtkinter.CTkFrame(master=self, width=320, height=250)
        self.loggedin_frame2.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
        self.titlelabel_frame2=customtkinter.CTkLabel(master=self.loggedin_frame2, text="Occupencies Details", font=('Century Gothic', 20,"bold"))
        self.titlelabel_frame2.place(x=60,y=0)
        self.opencamera_button1=customtkinter.CTkButton(master=self.loggedin_frame1, width=200, text="Open Camera", corner_radius=6, fg_color="#72bcd4", text_color="#1e5364", hover_color="#e8f4f8", command=self.OpenCamera)
        self.opencamera_button1.place(x=30,y=20)
        self.opencamera_button2=customtkinter.CTkButton(master=self.loggedin_frame1, width=200, text="Close Camera", corner_radius=6, fg_color="#72bcd4", text_color="#1e5364", hover_color="#e8f4f8", command=self.closeCamera)
        self.opencamera_button2.place(x=250,y=20)
        customtkinter.CTkLabel(master=self.loggedin_frame2, text="Total Seats:", font=('Century Gothic', 20,"bold")).place(x=5,y=40)
        self.totallabel_frame2=customtkinter.CTkLabel(master=self.loggedin_frame2, text=str(self.total_count), font=('Century Gothic', 20,"bold"))
        self.totallabel_frame2.place(x=140,y=40)
        customtkinter.CTkLabel(master=self.loggedin_frame2, text="Occupied Seats:", font=('Century Gothic', 20,"bold")).place(x=5,y=90)
        self.occupiedlabel_frame2=customtkinter.CTkLabel(master=self.loggedin_frame2, text=str(self.occupied_count), font=('Century Gothic', 20,"bold"))
        self.occupiedlabel_frame2.place(x=190,y=90)
        customtkinter.CTkLabel(master=self.loggedin_frame2, text="Unoccupied Seats:", font=('Century Gothic', 20,"bold")).place(x=5,y=140)
        self.unoccupiedlabel_frame2=customtkinter.CTkLabel(master=self.loggedin_frame2, text=str(self.occupied_count), font=('Century Gothic', 20,"bold"))
        self.unoccupiedlabel_frame2.place(x=220,y=140)
#         self.canvas_frame1 = customtkinter.CTkCanvas(self.loggedin_frame1, width = 480, height = 360)
#         self.canvas_frame1.place(x=10,y=100)
        self.ImageLabel_frame1=customtkinter.CTkLabel(master=self.loggedin_frame1,image=None)
        self.ImageLabel_frame1.place(x=10,y=120)
        
        
    def OpenCamera(self):
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Error: Could not open video stream from camera.")
                exit()
            
            
            
            self.delay = 15
            self.update()

            # Process the frame
            
            
            
            
            # Display the resulting frame
            # cv2.imshow('Real-time Object Detection', self.processed_frame)
            

          
    def closeCamera(self):
         self.cap.release()
         cv2.destroyAllWindows()
    def update(self):
        # Get a frame from the video source
        ret, self.frame = self.cap.read()
        
        if ret:
            self.frame=cv2.resize(self.frame,(480,360), interpolation=cv2.INTER_AREA)
            self.processed_frame,occupied_count,unoccupied_count = process_frame(self.frame)
            self.occupied_count=occupied_count
            self.unoccupied_count=unoccupied_count
            self.total_count=occupied_count+unoccupied_count
            self.occupiedlabel_frame2.configure(text=self.occupied_count)
            self.unoccupiedlabel_frame2.configure(text=self.unoccupied_count)
            self.totallabel_frame2.configure(text=self.total_count)
        
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(self.processed_frame))
            self.ImageLabel_frame1.configure(image=self.photo)
            
 
        self.master.after(self.delay, self.update)
