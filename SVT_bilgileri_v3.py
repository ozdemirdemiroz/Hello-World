import pandas as pd

import glob
import tkinter 
#from tkinter import *
#from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

main_win = tkinter.Tk()
main_win.geometry("210x150")
main_win.title("SVT")
sahaID=tkinter.StringVar()
main_win.sourceFolder = ''
main_win.sourceFile2G = ''
main_win.sourceFile3G = ''
main_win.sourceFile4G = ''
main_win.saha = ''

def sec():

	main_win.saha=sahaID.get()
 
	#sahaID.set("")

def chooseDir():
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Dosyaların olduğu klasörü seçiniz')

b_chooseDir = tkinter.Button(main_win, text = "...", width = 3, height = 1, command = chooseDir)
b_chooseDir.place(x = 0,y = 10)
b_chooseDir.width = 100

klasor=main_win.sourceFolder
def chooseFile2G():
    main_win.sourceFile2G = filedialog.askopenfilename(parent=main_win, initialdir= klasor , title='2G DB yi seçiniz')


def chooseFile3G():
    main_win.sourceFile3G = filedialog.askopenfilename(parent=main_win, initialdir= klasor, title='3G DB yi seçiniz')


def chooseFile4G():
    main_win.sourceFile4G = filedialog.askopenfilename(parent=main_win, initialdir= klasor, title='4G DB yi seçiniz')


b_chooseFile2G = tkinter.Button(main_win, text = "2G", width = 5, height = 1,bg='blue', command = chooseFile2G)
b_chooseFile2G.place(x = 30,y =10)
b_chooseFile2G.width = 50

b_chooseFile3G = tkinter.Button(main_win, text = "3G", width = 5, height = 1,bg='green', command = chooseFile3G)
b_chooseFile3G.place(x = 80,y =10)
b_chooseFile3G.width = 50

b_chooseFile4G = tkinter.Button(main_win, text = "4G", width = 5, height = 1,bg='purple', command = chooseFile4G)
b_chooseFile4G.place(x = 130,y =10)
b_chooseFile4G.width = 50

name_label = tkinter.Label(main_win, text = 'Saha', font=('calibre',10, 'bold'))
name_label.place(x=30,y=50)

name_entry = tkinter.Entry(main_win,textvariable = sahaID, font=('calibre',10,'normal'),width=10)
name_entry.place(x=70,y=50)

sub_btn=tkinter.Button(main_win,text = 'Seç', command = sec)
sub_btn.place(x=150,y=50)

def run():

    print("saha id")
    print(main_win.saha)
    print()
    print("2G dosya:")
    print(main_win.sourceFile2G)
    print()
    print("3G dosya:")
    print(main_win.sourceFile3G)
    print()
    print("4G dosya:")
    print(main_win.sourceFile4G)

    GSM = main_win.sourceFile2G
    WCDMA = main_win.sourceFile3G
    LTE = main_win.sourceFile4G
    saha = main_win.saha.upper()
    kayityeri=main_win.sourceFolder
    df2Gorj= pd.read_excel(GSM,sheet_name="Cell Parameters Nokia 2G",usecols='B,F,G,C,H,s,R') #excel den okuyup dataframe e işliyoruz
    df3Gorj= pd.read_excel(WCDMA,sheet_name="Cell Parameters Nokia 3G",usecols='D,C,G,P,S,T,U,V')
    df4Gorj= pd.read_excel(LTE,sheet_name="Cell Parameters Nokia 4G",usecols='A,C,M,N,O,Q')


    df2G=df2Gorj.iloc[:,[0,1,4,5,6,2,3]].sort_values(by=['CELL_NAME'])   
    df2Gson=df2G[df2G['SITE']==saha].style.hide_index().format({         
        'LATITUDE': '{:,.6f}'.format,
        'LONGITUDE': '{:,.6f}'.format,
        'ARFCN': '{:,.0f}'.format,
        'BSIC': '{:,.0f}'.format,
        'AZIMUTH': '{:,.0f}'.format,
        })

    df3G=df3Gorj.iloc[:,[1,0,2,3,7,5,6,4]].sort_values(by=['CELL_NAME'])
    df3G_flitre = df3G.query('Uarfcn_Dl in [2938, 10738]')
    #saha ismi AN0002 olanları seçelim
    df3Gson=df3G_flitre[df3G_flitre['SITE ID']==saha].style.hide_index().format({
        'LATITUDE': '{:,.6f}'.format,
        'LONGITUDE': '{:,.6f}'.format,
        'Uarfcn_Dl': '{:,.0f}'.format,
        'PSC': '{:,.0f}'.format,
        'AZIMUTH': '{:,.0f}'.format,
        })

    df4G=df4Gorj.iloc[:,[0,1,5,4,2,3]].sort_values(by=['LoCell Name'])
    df4Gson=df4G[df4G['e-NODEB Name']=='L'+saha].style.hide_index().format({
        'LATITUDE': '{:,.6f}'.format,
        'LONGITUDE': '{:,.6f}'.format,
        'AZIMUTH': '{:,.0f}'.format,
        'Physical cell ID': '{:,.0f}'.format,
        })
    with pd.ExcelWriter(kayityeri+"/SVT_bilgileri.xlsx") as writer:
        df2Gson.to_excel(writer, sheet_name="2G", index=False)
        df3Gson.to_excel(writer, sheet_name="3G", index=False)
        df4Gson.to_excel(writer, sheet_name="4G", index=False)
        
        
"""    
df2Gson.to_excel(r'C:/Users/ozdemir.demiroz/Desktop/sil/deneme.xlsx',sheet_name="2G",index=(False))
df3Gson.to_excel(r'C:/Users/ozdemir.demiroz/Desktop/sil/deneme.xlsx',sheet_name="3G",index=(False))
df4Gson.to_excel(r'C:/Users/ozdemir.demiroz/Desktop/sil/deneme.xlsx',sheet_name="4G",index=(False))
"""
run_btn=tkinter.Button(main_win,text = 'KOŞ', command = run,width=20,bg='orange')
run_btn.place(x=30,y=80)  


main_win.mainloop()