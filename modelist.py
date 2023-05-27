import os
import urllib.request
from tqdm import tqdm
# Daftar model yang tersedia
models = {
    'iXsAniModel_NSFW (my model)': 'https://huggingface.co/ixelszy/For-upload-folder/resolve/main/anime_model_goodfornsfw.safetensors',
    'Graupel': 'https://huggingface.co/p1atdev/graupel-v1/resolve/main/graupel-v1-nobody-fp16.safetensors',
    'iXsRealModel (my model)': 'https://huggingface.co/ixelszy/For-upload-folder/resolve/main/merge.3.safetensors',
    'sd_1.5': 'https://huggingface.co/ckpt/sd15/resolve/main/v1-5-pruned-emaonly.ckpt',
    'BPModel': 'https://huggingface.co/ckpt/BPModel/resolve/main/bp_1024_with_vae_te.ckpt',
    'henmixReal_v40': 'https://huggingface.co/ckpt/henmixreal/resolve/main/henmixReal_v40.safetensors',
    'Anything5.0': 'https://huggingface.co/ckpt/anything-v5.0/resolve/main/AnythingV5V3_v5PrtRE.safetensors',
    'anything-v4.0-pru': 'https://huggingface.co/ckpt/anything-v4.0/resolve/main/anything-v4.0-pruned.ckpt',
    'anything-v4.5-pru': 'https://huggingface.co/ckpt/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors',
    'Anything-V3.0-pru': 'https://huggingface.co/ckpt/anything-v3.0/resolve/main/Anything-V3.0-pruned.safetensors',
    'Counterfeit-V3.0': 'https://huggingface.co/ckpt/Counterfeit-V3.0/resolve/main/Counterfeit-V3.0_fp32.safetensors',
    'AOM2-Hard': 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors',
}
# Menampilkan daftar model yang tersedia
print("Model yang tersedia (Untuk sementara hanya sedikit, model bisa di download dengan extension civitai):")
for idx, model_name in enumerate(models.keys(), 1):
    print(f"{idx}. {model_name}")

model_indices = input("Masukkan nomor model yang ingin dipilih (pisahkan dengan spasi, misal 1 3 2 4): ")
selected_models = []
for model_idx in model_indices.split():
   try:
        model_name = list(models.keys())[int(model_idx)-1]
        selected_models.append(model_name)
   except (ValueError, IndexError):
        print(f"Nomor model '{model_idx}' tidak valid. Melewati model tersebut.")
# Path folder tujuan
destination_folder = '/content/stablebreaktest/models/Stable-diffusion'
# Membuat folder tujuan jika belum ada
os.makedirs(destination_folder, exist_ok=True)
# Mendownload file untuk setiap model yang dipilih
for model_name in selected_models:
    model_link = models[model_name]
    file_name = model_link.split('/')[-1]  # Mendapatkan nama file dari tautan

# Mendownload file 
    print(f"Mendownload file '{file_name}' untuk model '{model_name}'...")
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, ncols=80) as t:
        urllib.request.urlretrieve(model_link, file_name, reporthook=lambda x, y, z: t.update(y))     

 # Memindahkan file ke folder tujuan
    os.rename(file_name, destination_folder)

    print(f"File '{file_name}' berhasil dipindahkan ke folder '{destination_folder}' untuk model '{model_name}'.")                     
