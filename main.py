import os
import shutil
import zipfile

def papka_backuplash(papka_nomi):
    # Papka mavjudligini tekshiramiz
    if not os.path.exists(papka_nomi):
        print(f"Papka {papka_nomi} mavjud emas.")
        return

    # Zip arxivini yaratamiz
    zip_nomi = papka_nomi + '.zip'
    with zipfile.ZipFile(zip_nomi, 'w') as zip_file:
        # Papka ichidagi fayllarni zip arxiviga yuklaymiz
        for root, dirs, files in os.walk(papka_nomi):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, papka_nomi)
                zip_file.write(file_path, rel_path)

    print(f"Papka {papka_nomi} backup qilindi.")

# Backup qilish uchun papka nomini kiritishingiz kerak
papka_nomi = input("Papka nomini kiriting: ")
papka_backuplash(papka_nomi)
