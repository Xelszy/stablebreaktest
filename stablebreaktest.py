import subprocess

repo_path = '/content/stablebreaktest'

codetorun = """
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/stablebreaktest
%cd /content/stablebreaktest
#git switch sdxl
#git clone -b v2.1 https://github.com/camenduru/stable-diffusion-webui /content/stablebreaktest
!git clone https://github.com/Gerschel/sd-web-ui-quickcss /content/stablebreaktest/extensions/sd-web-ui-quickcss
!git clone https://github.com/vladmandic/sd-extension-system-info /content/stablebreaktest/extensions/sd-extension-system-info
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git /content/stablebreaktest/extensions/tag-autocomplete
!git clone https://github.com/P2Enjoy/sd-webui-roop-uncensored /content/stablebreaktest/extensions/sd-webui-roop-uncensored
!git clone https://github.com/ashen-sensored/stable-diffusion-webui-two-shot /content/stablebreaktest/extensions/stable-diffusion-webui-two-shot
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/stablebreaktest/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/stablebreaktest/scripts/run_n_times.py
!git clone https://github.com/thomasasfk/sd-webui-aspect-ratio-helper /content/stablebreaktest/extensions/sd-webui-aspect-ratio-helper
!git clone https://github.com/catppuccin/stable-diffusion-webui /content/stablebreaktest/extensions/stable-diffusion-webui
!git clone https://github.com/a2569875/stable-diffusion-webui-composable-lora /content/stablebreaktest/extensions/stable-diffusion-webui-composable-lora
!git clone https://github.com/ArtVentureX/sd-webui-agent-scheduler /content/stablebreaktest/extensions/sd-webui-agent-scheduler
!git clone https://github.com/hako-mikan/sd-webui-regional-prompter /content/stablebreaktest/extensions/sd-webui-regional-prompter
!git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/stablebreaktest/extensions/ultimate-upscale-for-automatic1111
!git clone https://github.com/hako-mikan/sd-webui-supermerger /content/stablebreaktest/extensions/sd-webui-supermerger
!git clone https://github.com/thomasasfk/sd-webui-aspect-ratio-helper /content/stablebreaktest/extensions/sd-webui-aspect-ratio-helper
!git clone https://github.com/Physton/sd-webui-prompt-all-in-one /content/stablebreaktest/extensions/sd-webui-prompt-all-in-one
!git clone https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper /content/stablebreaktest/extensions/Stable-Diffusion-Webui-Civitai-Helper
!git clone https://github.com/ashen-sensored/sd_webui_SAG /content/stablebreaktest/extensions/sd_webui_SAG
!git clone https://github.com/ashen-sensored/sd-dynamic-thresholding-rcfg /content/stablebreaktest/extensions/sd_webui_SAG
!git clone https://github.com/tjm35/asymmetric-tiling-sd-webui /content/stablebreaktest/extensions/asymmetric-tiling-sd-webui
!git clone https://github.com/hnmr293/sd-webui-llul /content/stablebreaktest/extensions/sd-webui-llul
!git clone https://github.com/takoyaro/db-storage1111 /content/stablebreaktest/extensions/db-storage1111
!git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /content/stablebreaktest/extensions/stable-diffusion-webui-model-toolkit
!git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris /content/stablebreaktest/extensions/a1111-sd-webui-lycoris
!git clone https://github.com/SignalFlagZ/sd-civitai-browser /content/stablebreaktest/extensions/sd-civitai-browser
!git clone https://github.com/Mikubill/sd-webui-controlnet /content/stablebreaktest/extensions/sd-webui-controlnet
!git clone https://github.com/camenduru/openpose-editor /content/stablebreaktest/extensions/openpose-editor
#!git clone https://github.com/jexom/sd-webui-depth-lib /content/stablebreaktest/extensions/sd-webui-depth-lib
!git clone https://github.com/hnmr293/posex /content/stablebreaktest/extensions/posex
!git clone https://github.com/Klokinator/Umi-AI /content/stablebreaktest/extensions/Umi-AI
!git clone https://github.com/hnmr293/sd-webui-cutoff /content/stablebreaktest/extensions/sd-webui-cutoff
!git clone https://github.com/Bing-su/sd-webui-tunnels /content/stablebreaktest/extensions/sd-webui-tunnels
!git clone https://github.com/zanllp/sd-webui-infinite-image-browsing /content/stablebreaktest/extensions/sd-webui-infinite-image-browsing
!git clone https://github.com/bbc-mc/sdweb-merge-block-weighted-gui /content/stablebreaktest/extensions/sdweb-merge-block-weighted-gui
!git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /content/stablebreaktest/extensions/stable-diffusion-webui-huggingface
!git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111 /content/stablebreaktest/extensions/multidiffusion-upscaler-for-automatic1111
!git clone https://github.com/etherealxx/batchlinks-webui /content/stablebreaktest/extensions/batchlinks-webui
!git clone https://github.com/nonnonstop/sd-webui-3d-open-pose-editor /content/stablebreaktest/extensions/sd-webui-3d-open-pose-editor
!git clone https://github.com/pharmapsychotic/clip-interrogator-ext /content/stablebreaktest/extensions/clip-interrogator-ext
!git clone https://github.com/Akegarasu/sd-webui-model-converter.git /content/stablebreaktest/extensions/sd-webui-model-converter
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/swl-models/Anything-v5.0-PRT/resolve/main/Anything-v5.0-PRT-RE.safetensors -d /content/stablebreaktest/models/Stable-diffusion -o Anything_V5.safetensors
%cd /content/stablebreaktest

!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/swl-models/Anything-v5.0-PRT/resolve/main/Anything-v5.0-PRT-RE.safetensors -d /content/stablebreaktest/models/Stable-diffusion -o Anything_V5.safetensors
%cd /content/stablebreaktest
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
