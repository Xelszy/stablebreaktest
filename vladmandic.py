import subprocess

repo_path = '/content/stablebreaktest'

codetorun = """
!git clone https://github.com/vladmandic/automatic /content/stablebreaktest/
!git clone https://github.com/kohya-ss/sd-webui-additional-networks /content/stablebreaktest/extensions/sd-webui-additional-networks
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git /content/stablebreaktest/extensions/tag-autocomplete
!git clone https://github.com/ashen-sensored/stable-diffusion-webui-two-shot /content/stablebreaktest/extensions/stable-diffusion-webui-two-shot
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/stablebreaktest/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/stablebreaktest/scripts/run_n_times.py
!git clone https://github.com/hako-mikan/sd-webui-supermerger /content/stablebreaktest/extensions/sd-webui-supermerger
!git clone https://github.com/hnmr293/sd-webui-llul /content/stablebreaktest/extensions/sd-webui-llul
!git clone https://github.com/takoyaro/db-storage1111 /content/stablebreaktest/extensions/db-storage1111
!git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /content/stablebreaktest/extensions/stable-diffusion-webui-model-toolkit
!git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-locon /content/stablebreaktest/extensions/a1111-sd-webui-locon
!git clone https://github.com/camenduru/sd-civitai-browser /content/stablebreaktest/extensions/sd-civitai-browser
!git clone https://github.com/Mikubill/sd-webui-controlnet /content/stablebreaktest/extensions/sd-webui-controlnet
!git clone https://github.com/camenduru/openpose-editor /content/stablebreaktest/extensions/openpose-editor
!git clone https://github.com/jexom/sd-webui-depth-lib /content/stablebreaktest/extensions/sd-webui-depth-lib
!git clone https://github.com/hnmr293/posex /content/stablebreaktest/extensions/posex
!git clone https://github.com/Klokinator/Umi-AI /content/stablebreaktest/extensions/Umi-AI
!git clone https://github.com/hnmr293/sd-webui-cutoff /content/stablebreaktest/extensions/sd-webui-cutoff
!git clone https://github.com/camenduru/sd-webui-tunnels /content/stablebreaktest/extensions/sd-webui-tunnels
!git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /content/stablebreaktest/extensions/stable-diffusion-webui-images-browser 
!git clone https://github.com/bbc-mc/sdweb-merge-block-weighted-gui /content/stablebreaktest/extensions/sdweb-merge-block-weighted-gui
!git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /content/stablebreaktest/extensions/stable-diffusion-webui-huggingface
!git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111 /content/stablebreaktest/extensions/multidiffusion-upscaler-for-automatic1111
!git clone https://github.com/etherealxx/batchlinks-webui /content/stablebreaktest/extensions/batchlinks-webui
!git clone https://github.com/nonnonstop/sd-webui-3d-open-pose-editor /content/stablebreaktest/extensions/sd-webui-3d-open-pose-editor
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
