import subprocess

repo_path = '/content/stablebreaktest'

codetorun = """
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/stable-diffusion-webui/scripts/run_n_times.py
!git clone https://github.com/kohya-ss/sd-webui-additional-networks /content/stable-diffusion-webui/extensions/sd-webui-additional-networks
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git /content/stable-diffusion-webui/extensions/tag-autocomplete
!git clone https://github.com/ashen-sensored/stable-diffusion-webui-two-shot /content/stable-diffusion-webui/extensions/stable-diffusion-webui-two-shot
!git clone https://github.com/hako-mikan/sd-webui-supermerger /content/stable-diffusion-webui/extensions/sd-webui-supermerger
!git clone https://github.com/hnmr293/sd-webui-llul /content/stable-diffusion-webui/extensions/sd-webui-llul
!git clone https://github.com/takoyaro/db-storage1111 /content/stable-diffusion-webui/extensions/db-storage1111
!git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /content/stable-diffusion-webui/extensions/stable-diffusion-webui-model-toolkit
!git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-locon /content/stable-diffusion-webui/extensions/a1111-sd-webui-locon
!git clone -b v2.0 https://github.com/camenduru/sd-civitai-browser /content/stable-diffusion-webui/extensions/sd-civitai-browser
!git clone https://github.com/Mikubill/sd-webui-controlnet /content/stable-diffusion-webui/extensions/sd-webui-controlnet
!git clone https://github.com/camenduru/openpose-editor /content/stable-diffusion-webui/extensions/openpose-editor
!git clone https://github.com/jexom/sd-webui-depth-lib /content/stable-diffusion-webui/extensions/sd-webui-depth-lib
!git clone https://github.com/hnmr293/posex /content/stable-diffusion-webui/extensions/posex
!git clone https://github.com/Klokinator/Umi-AI /content/stable-diffusion-webui/extensions/Umi-AI
!git clone https://github.com/hnmr293/sd-webui-cutoff /content/stable-diffusion-webui/extensions/sd-webui-cutoff
!git clone https://github.com/camenduru/sd-webui-tunnels /content/stable-diffusion-webui/extensions/sd-webui-tunnels
!git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /content/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser 
!git clone https://github.com/bbc-mc/sdweb-merge-block-weighted-gui /content/stable-diffusion-webui/extensions/sdweb-merge-block-weighted-gui
!git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /content/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface
!git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111 /content/stable-diffusion-webui/extensions/multidiffusion-upscaler-for-automatic1111
!git clone https://github.com/etherealxx/batchlinks-webui /content/stable-diffusion-webui/extensions/batchlinks-webui
"""

codetorun2 = """
!git reset --hard
!git -C /content/stablebreaktest/repositories/stable-diffusion-stability-ai reset --hard
"""

lines = codetorun.splitlines()

def rulesbroken(codetoexecute, cwd=''):
    for line in lines:
        line = line.strip()
        if line.startswith('!'):
            line = line[1:]
        if not line == '':
            try:
                if cwd:
                    subprocess.run(line, shell=True, check=True, cwd=repo_path)
                else:
                    subprocess.run(line, shell=True, check=True)
            except Exception as e:
                print("Exception: " + str(e))

rulesbroken(lines)

lines = codetorun2.splitlines()

rulesbroken(lines, repo_path)
