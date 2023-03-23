import os
import tkinter as tk
from tkinter import filedialog



def zmien_nazwe_pliku(nazwa_pliku):
    # Utwórz słownik z mappingiem dla polskich liter
    polskie_litery = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}

    # Zmień polskie litery na odpowiadające im litery bez znaków diakrytycznych
    for k, v in polskie_litery.items():
        nazwa_pliku = nazwa_pliku.replace(k, v).replace(k.upper(), v.upper())

    # Zamień spacje na podkreślenia
    nazwa_pliku = nazwa_pliku.replace(' ', '_')

    return nazwa_pliku

def zmien_nazwy_plikow():
    # Pobierz listę plików w wybranym folderze
    pliki = os.listdir(DOMYSLNY_FOLDER)

    # Iteruj po wszystkich plikach w folderze i zmień ich nazwy
    for plik in pliki:
        stara_nazwa = os.path.join(DOMYSLNY_FOLDER, plik)
        nowa_nazwa = os.path.join(DOMYSLNY_FOLDER, zmien_nazwe_pliku(plik))
        os.rename(stara_nazwa, nowa_nazwa)

def wybierz_folder():
    global DOMYSLNY_FOLDER   # Declare DOMYSLNY_FOLDER as a global variable
    folder_path = filedialog.askdirectory(initialdir=DOMYSLNY_FOLDER)

    if folder_path:
        # Zapisz wybrany folder jako folder domyślny
        DOMYSLNY_FOLDER = folder_path
        label.config(text="Folder domyślny: " + DOMYSLNY_FOLDER)

def start():
    zmien_nazwy_plikow()
    label.config(text="Nazwy plików zostały zmienione!")

# Ustaw folder domyślny
DOMYSLNY_FOLDER = 'C:/Users/KotewiczK/Documents/PLIKI_DO_ZMIANY_NAZWY'


# Utwórz okno główne
root = tk.Tk()
root.title("Zmiana nazw plików")

# Utwórz etykietę z informacją o folderze domyślnym
label = tk.Label(root, text="Folder domyślny: " + DOMYSLNY_FOLDER, font=("Arial", 12))
label.pack(pady=10)

# Utwórz przycisk do wybierania folderu
button_folder = tk.Button(root, text="Wybierz folder", font=("Arial", 12), command=wybierz_folder)
button_folder.pack(pady=10)

# Utwórz przycisk start
button_start = tk.Button(root, text="Start", font=("Arial", 12), command=start)
button_start.pack(pady=10)

# Utwórz pustą etykietę, aby uzyskać odstęp między przyciskiem a etykietą o autorze
spacer = tk.Label(root, text="", height=0)
spacer.pack()

# Utwórz etykietę z informacją o autorze
label_author = tk.Label(root, text="Created by Karol Kotewicz", font=("Arial", 10))
label_author.pack(side=tk.BOTTOM, padx=10, pady=10)

# Centruj okno na ekranie
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Ustaw minimalną szerokość i wysokość okna
root.wm_minsize(700, 200)

# Uruchom pętlę główną aplikacji
root.mainloop()
