import customtkinter as ctk
import textwrap
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import playsound
import threading
import pygame


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

class GeografyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoGame")  
        self.TinggiLayar = root.winfo_screenheight()
        self.LebarLayar = root.winfo_screenwidth()
        self.root.geometry(f"{self.LebarLayar}x{self.TinggiLayar}") 
      
        self.flag_folder = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "flags")

        self.flags = [f for f in os.listdir(self.flag_folder) if f.endswith(".png")]
        random.shuffle(self.flags)  # Mengacak urutan bendera
        self.total_rounds =  len(self.flags) 
        self.current_round = 0
        self.score = 0
        self.quiz_round = 0

        

        self.Kumpulan_soal = [
    {
         "pertanyaan" : "Negara apa yang menjadi rumah bagi Gunung Everest?",
         "pilihan" : ["Hawai", "Nepal", "Rusia"],
         "jawaban" : "Nepal"
    },
    {    "pertanyaan" : "Dimanakah ibukota negara Australia?",
         "pilihan" : ["Canberra", "Sydney", "Melbourne"],
         "jawaban" : "Canberra"
    },
    {    "pertanyaan" : "Mana yang merupakan negara Baltic?",
         "pilihan" : ["Latvia", "Belarus", "Norwegia"],
         "jawaban" : "Latvia"
    },
    {    "pertanyaan" : "Berapa banyak benua yang ada di bumi?",
         "pilihan" : ["Lima", "Delapan", "Tujuh"],
         "jawaban" : "Tujuh"
    },
    {    "pertanyaan" : "Negara yang memiliki populasi paling sedikit?",
         "pilihan" : ["Vatikan", "Korea Utara", "Mongolia"],
         "jawaban" : "Vatikan"
    },
    {    "pertanyaan" : "Apa negara yang berbatasan dengan Britania Raya?",
         "pilihan" : ["Georgia", "Irlandia", "Scotlandia"],
         "jawaban" : "Irlandia"
    },
    {    "pertanyaan" : "Negara apa yang terkenal dengan kincir anginnya?",
         "pilihan" : ["Belanda", "Swiss", "Polandia"],
         "jawaban" : "Belanda"
    }, 
    {    "pertanyaan" : "Mbappe merupakan pemain yang berasal dari?",
         "pilihan" : ["Spanyol", "Perancis", "Belgia"],
         "jawaban" : "Perancis"
    },
    {    "pertanyaan" : "Dimanakah ibu kota negara Kanada?",
         "pilihan" : ["Ottawa", "Toronto", "Montreal"],
         "jawaban" : "Ottawa"
    },
    {    "pertanyaan" : "Negara yang terletal di dua benua",
         "pilihan" : ["Ukraina", "Bulgaria", "Turki"],
         "jawaban" : "Turki"
    } 
         ]
        
        self.banyak_round = len(self.Kumpulan_soal)
        self.SuaraBack1()
        self.HalamanUtama()
        
       
    
        
    
    
        

    def HalamanUtama(self):

        for widget in self.root.winfo_children():
            widget.destroy()
        BackGroundAwal = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "Bagus.jpg")
        self.Foto1 = Image.open(BackGroundAwal)  
        self.Foto1 = self.Foto1.resize((2900, 1900))  
        self.Background_Halaman = ImageTk.PhotoImage(self.Foto1)
        self.Background_Halaman1 = ctk.CTkLabel(self.root, text="", image=self.Background_Halaman)
        self.Background_Halaman1.place(x=0,y=0)

        GambarExit0 = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "Exit.png")
        GambarKeluar = Image.open(GambarExit0)    
        GambarExit = ctk.CTkImage(dark_image=GambarKeluar, light_image=GambarKeluar)

        self.KeluarGame = ctk.CTkButton(self.root, 
                                        text="EXIT", 
                                        command=self.TombolExit, 
                                        width=90, 
                                        height=50, 
                                        text_color="black",
                                        fg_color="white",
                                        border_color="saddlebrown",
                                        border_width=3,
                                        font=("Comic Sans MS", 16),
                                        compound="left",
                                        image=GambarExit,
                                        hover="disabled")
        self.KeluarGame.place(x=40, y=40)

        GambarMainQuiz = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "RumusBumi.png")
        self.GambarQuiz = Image.open(GambarMainQuiz)  
        self.GambarQuiz = self.GambarQuiz.resize((200, 170))  
        self.GambarQuiz1 = ImageTk.PhotoImage(self.GambarQuiz)
        

        self.Opsi_Quiz = ctk.CTkButton(self.root, 
                                       text="MAIN QUIZ", 
                                       text_color="black",
                                       fg_color="white", 
                                       width=300,
                                       height=200, 
                                       corner_radius=10,
                                       font=("Comic Sans MS",22),
                                       border_width=5,
                                       border_color="tan4",
                                       hover_color="white",
                                       command=self.MainQuiz,
                                       image=self.GambarQuiz1,
                                       compound="top"
                                       
                                       
                                       
                                       )
                                       
        self.Opsi_Quiz.place(x=350, y=250)

        GambarGlobe0 = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "GlobeBendera.png")
        self.GambarGlobe = Image.open(GambarGlobe0)  
        self.GambarGlobe = self.GambarGlobe.resize((200, 180))  
        self.GambarGlobe1 = ImageTk.PhotoImage(self.GambarGlobe)

        self.Opsi_Globe = ctk.CTkButton(self.root, 
                                       text="TEBAK BENDERA", 
                                       text_color="black",
                                       fg_color="white", 
                                       width=300,
                                       height=200, 
                                       corner_radius=10,
                                       font=("Comic Sans MS",22),
                                       border_width=5,
                                       border_color="tan4",
                                       command=self.TebakNegara,
                                       hover_color="white",
                                       image=self.GambarGlobe1,
                                       compound="top"                                   
                                       )
                                       
        self.Opsi_Globe.place(x=750, y=250)

        GambarTandaTanya = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "TandaTanya.png")
        self.GambarTanya = Image.open(GambarTandaTanya)  
        self.GambarTanya = self.GambarTanya.resize((140, 120))  
        self.GambarTanya1 = ImageTk.PhotoImage(self.GambarTanya)
        

        self.ComingSoon = ctk.CTkButton(self.root, 
                                       text="COMING SOON", 
                                       text_color="black",
                                       fg_color="white", 
                                       width=300,
                                       height=200, 
                                       corner_radius=10,
                                       font=("Comic Sans MS",22),
                                       border_width=5,
                                       border_color="tan4",
                                       hover_color="white",
                                       image=self.GambarTanya1,
                                       compound="bottom"                                   
                                       )
        self.ComingSoon.place(x=550, y=500)

    def TombolExit(self):   
        self.HilangSuara()  
        self.root.quit()
        

    def SuaraBack (self):
        pygame.mixer.init()
        BGM = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Suara", "POU2.mp3")
        pygame.mixer.music.load(BGM)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)   

    def SuaraBack1 (self):
        self.SuaraAntiGanggu2= threading.Thread(target=self.SuaraBack)  
        self.SuaraAntiGanggu2.start()

    def HilangSuara(self):
        pygame.mixer.music.stop() 

           
    def TebakNegara(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.score = 0
        self.current_round = 0

        BackgroundSaatGame = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "OK.jpg")
        self.Foto2 = Image.open(BackgroundSaatGame)  
        self.Foto2 = self.Foto2.resize((2900, 1900))  
        self.Background2 = ImageTk.PhotoImage(self.Foto2)
        self.BackgroundGame = ctk.CTkLabel(self.root, image=self.Background2, text="")
        self.BackgroundGame.place(x=0, y=0)

        self.MainFrame = ctk.CTkFrame(self.root, 
                                       width=500, 
                                       height=650, 
                                       fg_color="burlywood3", 
                                       border_width=3,
                                       border_color="orange4" )
        self.MainFrame.place(x=720-250,y=100)


        self.TitleLabel = ctk.CTkLabel(self.root, 
                                        text="GUESS THE FLAG", 
                                        bg_color="burlywood3", 
                                        text_color="lightgoldenrod1", 
                                        font=("Helvatica", 43, "bold"))
        self.TitleLabel.place(x=(1440/ 2) - 185, y=(self.TinggiLayar / 2) - 280)

       
        self.FlagLabel = ctk.CTkLabel(self.root, text="")
        self.FlagLabel.place(x=(1440/2) - 185, y=(self.TinggiLayar / 2) - 200)

        
        self.AnswerEntry = ctk.CTkEntry(self.root, 
                                         font=("Arial", 16), 
                                         width=420, 
                                         height=40, 
                                         bg_color="burlywood3",
                                         placeholder_text="Masukkan nama negara", 
                                         corner_radius=15, )
        self.AnswerEntry.place(x=(self.LebarLayar / 2) - 210, y=(self.TinggiLayar / 2) + 120)

       
        self.SubmitButton = ctk.CTkButton(self.root, 
                                           text="Tebak", 
                                           command=self.CekJawabanBendera, 
                                           bg_color="burlywood3", 
                                           width=420, 
                                           fg_color="saddlebrown", 
                                           text_color="white", 
                                           font=("Comic Sans MS", 16), 
                                           corner_radius=20)
        self.SubmitButton.place(x=(self.LebarLayar / 2) - 210,y=(self.TinggiLayar / 2) + 180)
        self.root.bind('<Return>', lambda event: self.CekJawabanBendera()) 
        
        self.ScoreLabel = ctk.CTkLabel(self.root, 
                                        text=f"Score : {self.score}", 
                                        font=("Comic Sans MS", 24, "bold"), 
                                        text_color="black", 
                                        fg_color="burlywood3")
        self.ScoreLabel.place(x=665, y=110)

        self.BackButton = ctk.CTkButton(self.root, 
                                         text="Kembali", 
                                         border_width=2,
                                         border_color="orange4", 
                                         text_color="white", 
                                         font=("Comic Sans MS", 24), 
                                         width=180,
                                         height=60,
                                         fg_color="burlywood3",
                                         
                                         command=self.HalamanUtama
                            
                                         )
        self.BackButton.place(x=30,y=40)

        self.Pemberitahun = ctk.CTkLabel(self.root, 
                                         text="", 
                                         bg_color="burlywood3", 
                                         font=("Comic Sans MS", 20), 
                                         text_color="red3")
        self.Pemberitahun.place(x=620, y=520)

        
        if self.current_round >= self.total_rounds:
            messagebox.showinfo("Permainan Selesai", f"Permainan selesai! Skor akhir Anda: {self.score}/{self.total_rounds}")
            self.root.quit()
            return

        # Mengambil bendera tanpa ngulang
        self.current_flag = self.flags[self.current_round]
        self.current_flag_name = os.path.splitext(self.current_flag)[0].lower()  # Jawabannya sesuai nama file gambar
        self.current_round += 1

        # Ngeluarin gambar bendera
        flag_image = Image.open(os.path.join(self.flag_folder, self.current_flag))
        flag_image = flag_image.resize((750, 420), Image.LANCZOS)
        self.flag_photo = ImageTk.PhotoImage(flag_image)
        self.FlagLabel.configure(image=self.flag_photo)

        # Ngosongin Entry
        self.AnswerEntry.delete(0, ctk.END)

    def GantiBendera(self):
        
        if self.current_round >= self.total_rounds:
            messagebox.showinfo("Permainan Selesai", f"Permainan selesai! Skor akhir Anda: {self.score}/{self.total_rounds}")
            self.SubmitButton.configure(self.root, state="disabled")
            return

        
        self.current_flag = self.flags[self.current_round]
        self.current_flag_name = os.path.splitext(self.current_flag)[0].lower() 
        self.current_round += 1

        
        flag_image = Image.open(os.path.join(self.flag_folder, self.current_flag))
        flag_image = flag_image.resize((750, 420), Image.LANCZOS)
        self.flag_photo = ImageTk.PhotoImage(flag_image)
        self.FlagLabel.configure(image=self.flag_photo)

    
        self.AnswerEntry.delete(0, ctk.END)


    def CekJawabanBendera(self):
        self.root.bind('<Return>', lambda event: self.CekJawabanBendera()) 
        user_answer = self.AnswerEntry.get().strip().lower()

        
        if user_answer == self.current_flag_name:
            self.score += 1
            self.Pemberitahun.configure(self.root, text= "")
            self.SuaraBenar()
            self.ScoreLabel.configure(text=f"Score: {self.score}")
            self.GantiBendera()
        elif user_answer == "":
            self.Pemberitahun.configure(self.root, text= "Isi Jawabannya dulu!!")
        else:
            self.SuaraSalah()
            self.ScoreLabel.configure(text=f"Score: {self.score}")
            self.GantiBendera()


    def MainQuiz(self):
        self.quiz_round = 0
        self.quiz_score = 0
        for widget in self.root.winfo_children():
            widget.destroy()

        
        BackgroundSaatGame = os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Gambar", "OK.jpg")
        self.background_image = Image.open(BackgroundSaatGame)  
        self.background_image = self.background_image.resize((2900, 1900))  
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = ctk.CTkLabel(self.root, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0)

        self.my_frame = ctk.CTkFrame(self.root, fg_color="burlywood3", 
                                     corner_radius=15, 
                                     width=450, 
                                     height=900, 
                                     border_width=10, 
                                     border_color="white")
        self.my_frame.place(x=720-225, y=-10)

        self.my_score = ctk.CTkLabel(self.root, text=(f"Score : {self.quiz_score} / {self.banyak_round}"), 
                                     bg_color="burlywood3", 
                                     font=("Comic Sans MS", 25), 
                                     text_color="white")
        self.my_score.place(x=645, y=60)

        self.back2_button = ctk.CTkButton(self.root, 
                                         text="Kembali", 
                                         border_width=2,
                                         border_color="orange4", 
                                         text_color="white", 
                                         font=("Comic Sans MS", 24), 
                                         width=180,
                                         height=60,
                                         fg_color="burlywood3",
                                         
                                         command=self.HalamanUtama
                            
                                         )
        self.back2_button.place(x=30,y=40)

        self.my_pertanyaan = ctk.CTkLabel(self.root, 
                                          text=textwrap.fill(self.Kumpulan_soal[self.quiz_round]["pertanyaan"], 
                                                             width=30), 
                                          bg_color="burlywood3", 
                                          font=("Comic Sans MS", 20),
                                          text_color="white")
        self.my_pertanyaan.pack(pady=130)

        self.my_pernyataan = ctk.CTkLabel(self.root, text="", bg_color="burlywood3", font=("Comic Sans MS", 18))
        self.my_pernyataan.pack(pady=30)

        for soal in self.Kumpulan_soal[self.quiz_round]["pilihan"]:
            self.my_jawab = ctk.CTkButton(self.root, 
                                          text=soal, 
                                          command=lambda answer=soal :self.CekJawabanQuiz(answer), 
                                          width=380,
                                          height=100,
                                          corner_radius=10,
                                          bg_color="burlywood3",
                                          fg_color="tan4",
                                          text_color="white",
                                          font=("Comic Sans MS", 20))
            self.my_jawab.pack(pady=5)

 
        
    

    def Suara1(self):
        playsound.playsound(os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Suara", "Benar.mp3"))

    def SuaraBenar (self):
        SuaraAntiGanggu= threading.Thread(target=self.Suara1)  
        SuaraAntiGanggu.start()

    def Suara2(self):
        playsound.playsound(os.path.join("TA_PROGDAS_Yusuf Afaf Nur Abdillah_21120124130100_GeoGame (Geography Quiz Game)", "Suara", "Salah2.mp3"))

    def SuaraSalah (self):
        SuaraAntiGanggu1= threading.Thread(target=self.Suara2)  
        SuaraAntiGanggu1.start()
    
     
    def CekJawabanQuiz(self, answer):
        if answer == self.Kumpulan_soal[self.quiz_round]["jawaban"]:
            self.SuaraBenar()
            self.quiz_round +=1
            self.quiz_score +=1     
            self.Selesai_Quiz()           
            self.GantiSoalQuiz()
            

        else:
            self.SuaraSalah()
            self.quiz_round += 1
            self.Selesai_Quiz()           
            self.GantiSoalQuiz()
    
 
               
            
    def GantiSoalQuiz(self):
        widgetGaHilang = [self.background_label,self.back2_button, self.my_frame, self.my_pertanyaan]
        for widget in self.root.winfo_children():
            if widget not in widgetGaHilang:  
                widget.destroy()
        
        self.my_score = ctk.CTkLabel(self.root, text=(f"Score : {self.quiz_score} / {self.banyak_round}"), 
                                     bg_color="burlywood3", 
                                     font=("Comic Sans MS", 25), 
                                     text_color="white")
        self.my_score.place(x=645, y=60)

        if self.quiz_round <= 9:
            self.my_pertanyaan.configure(self.root,text=textwrap.fill(self.Kumpulan_soal[self.quiz_round]["pertanyaan"], 
                                                                  width=30))
        else:
            pass                                                          

        self.my_pernyataan = ctk.CTkLabel(self.root, text="", bg_color="burlywood3")
        self.my_pernyataan.pack(pady=30)

        if self.quiz_round <= 9:
            for soal in self.Kumpulan_soal[self.quiz_round]["pilihan"]:
                self.my_jawab = ctk.CTkButton(self.root, 
                                          text=soal, 
                                          command=lambda answer=soal :self.CekJawabanQuiz(answer), 
                                          width=380,
                                          height=100,
                                          corner_radius=10,
                                          bg_color="burlywood3",
                                          fg_color="tan4",
                                          text_color="white",
                                          font=("Comic Sans MS", 20))
                self.my_jawab.pack(pady=5)

    def Selesai_Quiz(self):
        if (self.quiz_round ) == ( self.banyak_round ):
                messagebox.showinfo("Permainan selesai", "Permainan selesai!")
                self.my_pertanyaan.destroy()


                
if __name__ == "__main__":
    root = ctk.CTk()  
    app = GeografyGame(root)
    root.mainloop()
    
