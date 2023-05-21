import os
import urllib.request
from tqdm import tqdm
from IPython.display import display, clear_output
import ipywidgets as widgets

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

# Membuat checkboxes untuk pemilihan model
model_checkboxes = []
for model_name in models.keys():
    checkbox = widgets.Checkbox(value=False, description=model_name)
    model_checkboxes.append(checkbox)

# Tombol Setujui
approve_button = widgets.Button(description='Setujui', button_style='success', layout=widgets.Layout(width='100px'))

# Menampilkan checkboxes dan tombol Setujui
display(widgets.VBox(model_checkboxes + [approve_button]))

# Variabel untuk menyimpan model yang dipilih
selected_models = []

# Callback function untuk tombol Setujui
def approve_button_clicked(b):
    for i, checkbox in enumerate(model_checkboxes):
        if checkbox.value:
            selected_models.append(checkbox.description)
    
    clear_output()
    print("\n\033[92mModel yang disetujui:\033[0m\n", selected_models)
    download_models()

# Assign callback function ke tombol Setujui
approve_button.on_click(approve_button_clicked)

# Fungsi untuk mengunduh model
def download_models():
    # Path folder tujuan
    destination_folder = '/content/models'

    # Membuat folder tujuan jika belum ada
    os.makedirs(destination_folder, exist_ok=True)

    # Mendownload file untuk setiap model yang dipilih
    for model_name in selected_models:
        model_link = models[model_name]
        file_name = model_link.split('/')[-1]  # Mendapatkan nama file dari tautan

        # Mendownload file
        print(f"\n\033[92mMendownload file '{file_name}' untuk model '{model_name}'...\033[0m\n")
        with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, ncols=80) as t:
            urllib.request.urlretrieve(model_link, os.path.join(destination_folder, file_name), reporthook=lambda x, y, z: t.update(y))
            print(f"\n\033[92mFile '{file_name}' berhasil diunduh untuk model '{model_name}'.\033[0m\n")

    print("\n\033[92mProses pemilihan model selesai.\033[0m\n")
