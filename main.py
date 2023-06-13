import os
import shutil

def clean_temp_files():
    temp_folder = "/tmp"
    if os.path.exists(temp_folder):
        print(f"Geçici dosyalar temizleniyor: {temp_folder}")
        for root, _, files in os.walk(temp_folder):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Hata: {e}")

    trash_folder = os.path.expanduser("~/.local/share/Trash/files")
    if os.path.exists(trash_folder):
        print(f"Çöp dosyaları temizleniyor: {trash_folder}")
        try:
            shutil.rmtree(trash_folder)
        except Exception as e:
            print(f"Hata: {e}")

    print("Temizleme tamamlandı.")

clean_temp_files()

