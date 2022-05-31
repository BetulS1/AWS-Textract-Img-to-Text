import tkinter as tk 
from tkinter import*
from tkinter.filedialog import askopenfilename
import boto3 
from PIL import Image, ImageTk

window=tk.Tk(className=' AWS Textract Projesi') ##pencere başlığı
window.geometry("900x600") ##boyutu
window.configure(bg='#0066CC')##pencere rengi
window.resizable(width=FALSE, height=FALSE) ##pecrenin boyutu kullanıcı tarafından değiştirilemez
Label(window, text="Taranan Belgeden Metin Çıkarma Uygulaması",bg='#f8f8ff' ).place(x=320, y=10) 
button1= Button(text = "Başlat", command=lambda: img_yukle() ,bg='white',activebackground = 'blue', activeforeground = 'white',width=15,height=2) 
button1.place(x=50, y=70) 

def img_yukle():
    aws_management = boto3.session.Session(profile_name='root')
    client= aws_management.client(service_name='textract',region_name='us-east-1')
    global img 
    filename=open("test.jpg",'rb' )
    img = Image.open(filename)
    img_resize = img.resize((600,400))
    img = ImageTk.PhotoImage(img_resize)
    imgBytes= image_byte(filename)
    button2= Button(window, image=img) 
    button2.place(x=50, y=150) 
    response = client.detect_document_text(
        Document={
            'Bytes':imgBytes
        }
    )
    #text yazdırma sonuç ekranı 
    for item in response['Blocks']:
        if item['BlockType']=='WORD':
            print(item['Text'])

#dönüşüm img to byte
def image_byte(filename):
    filename = askopenfilename()
    with open(filename,'rb') as imageFile: 
        return imageFile.read() 

##çıkış butonu pencereyi kapatır
kapatbtn= Button(text = "KAPAT", command=window.quit, bg='white',activebackground = 'red', activeforeground = 'white') 
kapatbtn.place(x=830, y=560) 
window.mainloop()
