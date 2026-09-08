batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedial = []

print("=== Pengelompokkan nilai ujian mahasiswa ===")
print("batas lulus: ", batas_nilai[0])
print("Nilai maksimal: ", batas_nilai[1])

while True:
    nilai_input = input("Masukkan nilai (ketik 'selesai' untuk berhenti); ")

    if nilai_input.lower() == "selesai":
        if len(nilai_masuk) < 5:
            print("anda harus memasukkan minimal 5 nilai.")
            continue

        if len(lulus) == 0 or len(remedial) == 0:
            print("Harus ada nilai lulus dan remedial.")
            continue

        break

    nilai = int(nilai_input)
    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
        print("nilai masuk kelompok lulus.")
    else:
        remedial.append(nilai)
        print("nilai masuk kelompok remedial.")

print("\nnilai yang sudah dimasukkan:", nilai_masuk)

hapus = input("Masukkan nilai yaang ingin dihapus: ")

nilai_hapus = int(hapus)

if nilai_hapus in nilai_masuk:
    nilai_masuk.remove(nilai_hapus)

    if nilai_hapus in lulus:
        lulus.remove(nilai_hapus)
    elif nilai_hapus in remedial:
        remedial.remove(nilai_hapus)

    print("nilai berhasil dihapus.")
else:
    print("nilai tidak ditemukan.")

print("\n=== Hasil akhir ===")
print("nilai masuk :", nilai_masuk)
print("lulus :", lulus)
print("remedial :", remedial)




