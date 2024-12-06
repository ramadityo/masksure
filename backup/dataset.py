import os
import shutil
import random

# Path awal dan tujuan
train_dir = "train"
validation_dir = "val"

# Proporsi data validation
validation_split = 0.2  # 20% dari total dataset

# Buat folder validation jika belum ada
os.makedirs(validation_dir, exist_ok=True)

# Ambil semua file di dalam folder "train"
all_files = os.listdir(train_dir)

# Acak urutan file
random.shuffle(all_files)

# Hitung jumlah file untuk validation
num_validation = int(len(all_files) * validation_split)

# Pisahkan file untuk validation
validation_files = all_files[:num_validation]

# Pindahkan file ke folder "validation"
for file_name in validation_files:
    src_path = os.path.join(train_dir, file_name)
    dest_path = os.path.join(validation_dir, file_name)
    shutil.move(src_path, dest_path)

print("Dataset telah dibagi!")
