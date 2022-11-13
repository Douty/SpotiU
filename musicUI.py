import customtkinter
from tkinter import ttk
import time
from main import *



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{800}x{800}")
        self.title("Music Match Maker")
        self.maxsize(800,800)
        self.minsize(800,800)
        customtkinter.set_appearance_mode("system")
        
        self.Title = customtkinter.CTkLabel(self,text="SpotiU",width=200,height=100,text_font=("Arial","50"))  # type: ignore
        self.Title.pack(pady=10)
        
        self.program_details= customtkinter.CTkLabel(self,text="Authorize your spotify and see your personal spotify stats!!!!", width=10,height=50,text_font=("Arial","12"))  # type: ignore
        self.program_details.pack(pady=10)
        #function to connect to spotify services 
        def authorize():
            results = sp.current_user_top_artists(limit=20, offset=0, time_range='long_term')
            self.authorize_btn.state=customtkinter.DISABLED
            self.authorize_btn.configure(text="Authorized!")
            return results

        #Creates button 
        self.authorize_btn = customtkinter.CTkButton(self,text="Authorize!",text_font="Arial",command=lambda:authorize(),fg_color = "#1DB954",hover=True,hover_color="#191414")
        self.authorize_btn.pack(pady=10)
        #If user already did not authorize their account then allow them to click the button
        if os.path.isfile(".cache"):
                self.authorize_btn.state=customtkinter.DISABLED
                self.authorize_btn.configure(text="Authorized!")
                
        def combobox_callback(choice):
            match choice:
                case "Top artists":
                    print("user selected top artists")
                case "Top Tracks":
                    print("user selected top tracks")

        user_select_box= customtkinter.CTkComboBox(master=self,
                                     values=["Top artists", "Top Tracks"],
                                     command=combobox_callback)
        user_select_box.pack(padx=20, pady=10)
                    
        user_results = customtkinter.CTkTextbox(self,width=500, height=250)
        user_results.pack(padx=10)

        user_results.insert("0.0", "lol")  # insert at line 0 character 0
        # get text from line 0 character 0 till the end

        user_results.configure(state="disabled")  # configure textbox to be read-only
        
                
        
                

                
     
        
        
        

     

app = App()
app.mainloop()