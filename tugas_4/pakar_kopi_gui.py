import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pyswip import Prolog

# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Minuman Kopi")

# Inisialisasi frame utama
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Membuat widget yang diperlukan
tk.Label(
    mainframe,
    text="Aplikasi Rekomendasi Minuman Kopi",
    font=("Arial", 16)
).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Cari Rekomendasi", command=lambda: mulai_diagnosa())
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Tambah padding ke setiap widget
for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("/home/anas/Projek/PrakKB/pakar-kopi-gui.pl")

# Variabel global
kopi = []
rekomen = {}
index_kopi = 0
index_rekomen = 0
current_kopi = ""
current_rekomen = ""


def mulai_diagnosa():
    global kopi, rekomen, index_kopi, index_rekomen

    # Bersihkan database Prolog
    prolog.retractall("rekomen_pos(_)") 
    prolog.retractall("rekomen_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    # Mendapatkan daftar kopi dan rekomen
    kopi = [p["X"].decode() for p in list(prolog.query("kopi(X)"))]
    for p in kopi:
        rekomen[p] = [g["X"] for g in list(prolog.query(f"rekomen(X, \"{p}\")"))]

    index_kopi = 0
    index_rekomen = -1
    pertanyaan_selanjutnya()


def pertanyaan_selanjutnya(ganti_kopi=False):
    global current_kopi, current_rekomen, index_kopi, index_rekomen

    # Atur index kopi
    if ganti_kopi:
        index_kopi += 1
        index_rekomen = -1

    # Apabila daftar kopi sudah habis
    if index_kopi >= len(kopi):
        hasil_diagnosa()
        return

    current_kopi = kopi[index_kopi]

    # Atur index rekomen
    index_rekomen += 1

    # Apabila semua rekomen dari kopi habis
    if index_rekomen >= len(rekomen[current_kopi]):
        hasil_diagnosa(current_kopi)
        return

    current_rekomen = rekomen[current_kopi][index_rekomen]

    # Cek status rekomen di database Prolog
    if list(prolog.query(f"rekomen_pos({current_rekomen})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"rekomen_neg({current_rekomen})")):
        pertanyaan_selanjutnya(ganti_kopi=True)
        return

    # Mendapatkan pertanyaan baru
    pertanyaan = list(prolog.query(f"pertanyaan({current_rekomen}, Y)"))[0]["Y"].decode()

    # Set pertanyaan ke kotak pertanyaan
    tampilkan_pertanyaan(pertanyaan)


def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)


def jawaban(jwb):
    if jwb:
        prolog.assertz(f"rekomen_pos({current_rekomen})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"rekomen_neg({current_rekomen})")
        pertanyaan_selanjutnya(ganti_kopi=True)


def hasil_diagnosa(kopi=""):
    if kopi:
        messagebox.showinfo("Hasil Rekomendasi", f"Minuman {kopi}.")
    else:
        messagebox.showinfo("Hasil Rekomendasi", "Tidak terdeteksi kopi.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)


# Menjalankan GUI
root.mainloop()
