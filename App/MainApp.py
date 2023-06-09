from tkinter import *
from tkinter import messagebox

from App.AirSigning.PDFAirSignerApp import PDFAirSignerApp

signature = Tk()
signature.rowconfigure(0, weight=1)
signature.columnconfigure(0, weight=1)
height = 650
width = 1240
x = (signature.winfo_screenwidth() // 2) - (width // 2)
y = (signature.winfo_screenheight() // 4) - (height // 4)

signature.geometry('{}x{}+{}+{}'.format(width, height, x, y))

signature.title('Air Signature')

sign_in = Frame(signature)
sign_up = Frame(signature)
index_page = Frame(signature)

for frame in (index_page, sign_in, sign_up):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(ui):
    ui.tkraise()


def show_password(entry):
    if entry.cget('show') == '*':
        entry.config(show='')
    else:
        entry.config(show='*')


show_frame(index_page)

# ====================================================================================
# =========================== INDEX PAGE START HERE ================================
# ====================================================================================
index_page.configure(bg="#525561")

# ================Background Image ====================
index_page_bg_image = PhotoImage(file="assets\\image_1.png")
index_bg_image = Label(
    index_page,
    image=index_page_bg_image,
    bg="#525561"
)
index_bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
index_headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
index_headerText_image_label1 = Label(
    index_bg_image,
    image=index_headerText_image_left,
    bg="#272A37"
)
index_headerText_image_label1.place(x=60, y=45)

index_headerText1 = Label(
    index_bg_image,
    text="Air Signature",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
index_headerText1.place(x=110, y=45)

# ================ Header Text Down ====================
index_headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
index_headerText_image_label3 = Label(
    index_bg_image,
    image=index_headerText_image_down,
    bg="#272A37"
)
index_headerText_image_label3.place(x=650, y=530)

index_headerText3 = Label(
    index_bg_image,
    text="Powered by Signature Group",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
index_headerText3.place(x=700, y=530)

# ============== Right Button ========================
signButton = Button(
    index_bg_image,
    text="Sign with \n Verification",
    fg="#206DB4",
    font=("yu gothic ui Bold", 40 * -1),
    bg="#272A60",
    bd=5,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_in),
)
signButton.place(x=590, y=140, width=350, height=350)

# ================ Left Button ====================
signButton = Button(
    index_bg_image,
    text="Sign without \nVerification",
    fg="#206DB4",
    font=("yu gothic ui Bold", 40 * -1),
    bg="#272A60",
    bd=5,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda : PDFAirSignWithoutVerify()
)
signButton.place(x=75, y=140, width=350, height=350)

# ====================================================================================
# =========================== SIGN UP PAGE START HERE ================================
# ====================================================================================

# Sign Up Text Variables
FirstName = StringVar()
LastName = StringVar()
Email = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()

sign_up.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_image = Label(
    sign_up,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="Air Signature",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label2 = Label(
    bg_image,
    image=headerText_image_right,
    bg="#272A37"
)
headerText_image_label2.place(x=640, y=45)

headerText2 = Label(
    bg_image,
    anchor="nw",
    text="Signatures",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#272A37"
)
headerText2.place(x=690, y=45)

# ============== SHOW ALL SIGNATURES ========================
sign_image_right = PhotoImage(file="assets\\button_1.png").zoom(20).subsample(30)
for i in range(5):
    sign_image_label = Label(
        bg_image,
        image=sign_image_right,
        bg="red"
    )
    sign_image_label.place(x=640, y=(121 + i * 70))

# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="Login",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_in)
)
switchLogin.place(x=230, y=185, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets\\input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(
    firstName_image_Label,
    text="First name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets\\name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=FirstName
)
firstName_entry.place(x=8, y=17, width=140, height=27)

# ================ Last Name Section ====================
lastName_image = PhotoImage(file="assets\\input_img.png")
lastName_image_Label = Label(
    bg_image,
    image=lastName_image,
    bg="#272A37"
)
lastName_image_Label.place(x=293, y=242)

lastName_text = Label(
    lastName_image_Label,
    text="Last name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(file="assets\\name_icon.png")
lastName_icon_Label = Label(
    lastName_image_Label,
    image=lastName_icon,
    bg="#3D404B"
)
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
    lastName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=LastName
)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(file="assets\\email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#272A37"
)
emailName_image_Label.place(x=80, y=311)

emailName_text = Label(
    emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(file="assets\\email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Email
)
emailName_entry.place(x=8, y=17, width=354, height=27)

# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets\\input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#272A37"
)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    show="*",
    textvariable=Password
)
passwordName_entry.place(x=8, y=17, width=140, height=27)

password_check_btn = Checkbutton(bg_image, text='show password', fg="#FFFFFF", bg='#272A37', selectcolor='#272A37',
                                 activebackground='#272A37',
                                 bd=0,
                                 font=("yu gothic ui", 11, 'bold'), command=lambda: show_password(passwordName_entry))
password_check_btn.place(x=120, y=440)

# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(file="assets\\input_img.png")
confirm_passwordName_image_Label = Label(
    bg_image,
    image=confirm_passwordName_image,
    bg="#272A37"
)
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = Label(
    confirm_passwordName_image_Label,
    text="Confirm Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
confirm_passwordName_icon_Label = Label(
    confirm_passwordName_image_Label,
    image=confirm_passwordName_icon,
    bg="#3D404B"
)
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
    confirm_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    show="*",
    textvariable=ConfirmPassword
)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

confirm_check_btn = Checkbutton(bg_image, text='show password', fg="#FFFFFF", bg='#272A37', selectcolor='#272A37',
                                activebackground='#272A37',
                                bd=0,
                                font=("yu gothic ui", 11, 'bold'),
                                command=lambda: show_password(confirm_passwordName_entry))
confirm_check_btn.place(x=330, y=440)

# =============== Add Sign Button ====================
add_sign_buttonImage = PhotoImage(file="assets\\email.png")
add_sign_button = Button(
    bg_image,
    text="Add Signatures",
    fg="#206DB4",
    font=("yu gothic ui Bold", 25 * -1),
    bg="#2c3042",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: add_signature()
)

add_sign_button.place(x=144, y=480, width=300, height=45)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(
    file="assets\\button_1.png")
submit_button = Button(
    bg_image,
    image=submit_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
    command=lambda: signup()
)
submit_button.place(x=130, y=530, width=333, height=65)

# ================ Header Text Down ====================
headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_down,
    bg="#272A37"
)
headerText_image_label3.place(x=650, y=530)

headerText3 = Label(
    bg_image,
    text="Powered by Signature Group",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText3.place(x=700, y=530)


def add_signature():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Draw Signatures')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)


def clear_signup():
    FirstName.set("")
    LastName.set("")
    Email.set("")
    Password.set("")
    ConfirmPassword.set("")

    password_check_btn.deselect()
    confirm_check_btn.deselect()


def signup():
    user = dict()

    if firstName_entry.get() == "" or lastName_entry.get() == "" or emailName_entry.get() == "" or passwordName_entry.get() == "" or confirm_passwordName_entry.get() == "":
        messagebox.showerror("Error", "All Fields are Required")
    elif passwordName_entry.get() != confirm_passwordName_entry.get():
        messagebox.showerror("Error", "Password and Confirmed Password Didn't Match")
    else:
        user['firstName'] = firstName_entry.get()
        user['lastName'] = lastName_entry.get()
        user['email'] = emailName_entry.get()
        user['password'] = passwordName_entry.get()

        clear_signup()
        show_frame(sign_in)
        print(user.values())


# ====================================================================================
# =========================== LOGIN PAGE START HERE ================================
# ====================================================================================

# Login Text Variables
email = StringVar()
password = StringVar()

sign_in.configure(bg="#525561")

# ================Background Image ====================
Login_backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_imageLogin = Label(
    sign_in,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=120, y=28)

# ================ Header Text Left ====================
Login_headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
Login_headerText_image_label1 = Label(
    bg_imageLogin,
    image=Login_headerText_image_left,
    bg="#272A37"
)
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(
    bg_imageLogin,
    text="Air Signature",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
Login_headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
# Login_headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
# Login_headerText_image_label2 = Label(
#     bg_imageLogin,
#     image=Login_headerText_image_right,
#     bg="#272A37"
# )
# Login_headerText_image_label2.place(x=400, y=45)
#
# Login_headerText2 = Label(
#     bg_imageLogin,
#     anchor="nw",
#     text="Some Extra Text",
#     fg="#FFFFFF",
#     font=("yu gothic ui Bold", 20 * -1),
#     bg="#272A37"
# )
# Login_headerText2.place(x=450, y=45)

# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Login to continue",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
loginAccount_header.place(x=75, y=121)

# ================ NOT A MEMBER TEXT ====================
loginText = Label(
    bg_imageLogin,
    text="Not a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================
switchSignup = Button(
    bg_imageLogin,
    text="Sign Up",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_up)
)
switchSignup.place(x=220, y=185, width=70, height=35)

# ================ Email Name Section ====================
Login_emailName_image = PhotoImage(file="assets\\email.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="#272A37"
)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = PhotoImage(file="assets\\email-icon.png")
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#3D404B"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=email
)
Login_emailName_entry.place(x=8, y=17, width=354, height=27)

# ================ Password Name Section ====================
Login_passwordName_image = PhotoImage(file="assets\\email.png")
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="#272A37"
)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#3D404B"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    show='*',
    textvariable=password
)
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(file="assets\\button_1.png")
Login_button_1 = Button(
    bg_imageLogin,
    image=Login_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: signin(),
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
Login_button_1.place(x=120, y=445, width=333, height=65)

# ================ Home Button ====================
home_image_right = PhotoImage(file="assets\\home.png", palette='red')
home_button = Button(
    bg_imageLogin,
    image=home_image_right,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(index_page),
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
home_button.place(x=860, y=45, width=105, height=50)

# ================ Header Text Down ====================
Login_headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
Login_headerText_image_label3 = Label(
    bg_imageLogin,
    image=Login_headerText_image_down,
    bg="#272A37"
)
Login_headerText_image_label3.place(x=650, y=530)

Login_headerText3 = Label(
    bg_imageLogin,
    text="Powered by Signature Group",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
Login_headerText3.place(x=700, y=530)

login_check_btn = Checkbutton(bg_imageLogin, text='show password', fg="#FFFFFF", bg='#272A37', selectcolor='#272A37',
                              activebackground='#272A37',
                              font=("yu gothic ui", 11, 'bold'),
                              bd=0,
                              command=lambda: show_password(Login_passwordName_entry))
login_check_btn.place(x=210, y=390)


def clear_signin():
    email.set("")
    password.set("")

    login_check_btn.deselect()


def signin():
    login_user = dict()

    if Login_emailName_entry.get() == "" or Login_passwordName_entry.get() == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        login_user['email'] = Login_emailName_entry.get()
        login_user['password'] = Login_passwordName_entry.get()

        clear_signin()

        print(login_user.values())

def PDFAirSignWithoutVerify():
    root = Tk()
    root.configure(bg='black')
    root.title('Air Signing')
    root.geometry("630x700+700+100")
    app = PDFAirSignerApp(root)
    root.mainloop()

signature.resizable(False, False)
signature.mainloop()
