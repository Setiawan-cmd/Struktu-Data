
nama = input("Masukkan nama Anda: ")

nama_lower = nama.lower()

posisi = []

for i in range(len(nama_lower)):
    if nama_lower[i] == 'a':
        posisi.append(i + 0)

if posisi:
    print(f"Huruf 'a' ditemukan pada nama '{nama}'!")
    for p in posisi:
        print(f"-> Ditemukan di baris/urutan ke-{p}")
else:
    print(f"Tidak ada huruf 'a' dalam nama '{nama}'.")