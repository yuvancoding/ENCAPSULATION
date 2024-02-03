from tkinter import *
root = Tk()
root.title("Encapsulation")
root.geometry("400x400")
label_name = Label(root, text="Name: ")
label_name.place(relx=0.3,rely=0.1, anchor= CENTER)
input_name = Entry(root)
input_name.place(relx=0.6,rely=0.1, anchor= CENTER)
label_password = Label(root, text="Password: ")
label_password.place(relx=0.3,rely=0.2, anchor= CENTER)
input_password = Entry(root)
input_password.place(relx=0.6,rely=0.2, anchor= CENTER)
label_captcha = Label(root, text="Captcha: ")
label_captcha.place(relx=0.3,rely=0.3, anchor= CENTER)
input_captcha = Entry(root)
input_captcha.place(relx=0.6,rely=0.3, anchor= CENTER)
label_show_name = Label(root)
label_show_name.place(relx=0.5,rely=0.7, anchor= CENTER)
label_show_password = Label(root)
label_show_password.place(relx=0.5,rely=0.8, anchor= CENTER)
label_show_captcha = Label(root)
label_show_captcha.place(relx=0.5,rely=0.9, anchor= CENTER)
class userDB():
    def __init__(self):
        self.__username = "James"
        self.__password = "James76*"
        self.captcha = "A7d"
    def showUser(self):
        label_show_name["text"] = "Name : "+self.__username
        label_show_password["text"] = "Password : "+self.__password
        label_show_captcha["text"] = "Captcha : "+self.captcha
user = userDB()
def addUser():
    global user
    user.username = input_name.get()
    user.password = input_password.get()
    user.captcha = input_captcha.get()
    print("Details Updated")
btn = Button(root, text="Update Login Details", command=addUser)
btn.place(relx=0.3,rely=0.5, anchor= CENTER)
btn = Button(root, text="Show Profile", command=user.showUser)
btn.place(relx=0.7,rely=0.5, anchor= CENTER)
root.mainloop()