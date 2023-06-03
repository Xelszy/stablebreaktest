import subprocess

repo_path = '/content/stablebreaktest'

codetorun = """
!git clone -b v2.2 https://github.com/camenduru/stable-diffusion-webui /content/stablebreaktest
!git clone https://github.com/Xelszy/sd-webui-additional-networks /content/stablebreaktest/extensions/sd-webui-additional-networks
!git clone https://github.com/Gerschel/sd-web-ui-quickcss /content/stablebreaktest/extensions/sd-web-ui-quickcss
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git /content/stablebreaktest/extensions/tag-autocomplete
!git clone https://github.com/ashen-sensored/stable-diffusion-webui-two-shot /content/stablebreaktest/extensions/stable-diffusion-webui-two-shot
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/stablebreaktest/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/stablebreaktest/scripts/run_n_times.py
!git clone https://github.com/thomasasfk/sd-webui-aspect-ratio-helper /content/stablebreaktest/extensions/sd-webui-aspect-ratio-helper
!git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/stablebreaktest/extensions/ultimate-upscale-for-automatic1111
!git clone https://github.com/hako-mikan/sd-webui-supermerger /content/stablebreaktest/extensions/sd-webui-supermerger
!git clone https://github.com/hnmr293/sd-webui-llul /content/stablebreaktest/extensions/sd-webui-llul
!git clone https://github.com/zanllp/sd-webui-infinite-image-browsing /content/stablebreaktest/extensions/sd-webui-infinite-image-browsing 
!git clone https://github.com/takoyaro/db-storage1111 /content/stablebreaktest/extensions/db-storage1111
!git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /content/stablebreaktest/extensions/stable-diffusion-webui-model-toolkit
!git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris /content/stablebreaktest/extensions/a1111-sd-webui-lycoris
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
!git clone https://github.com/pharmapsychotic/clip-interrogator-ext /content/stablebreaktest/extensions/clip-interrogator-ext
!git clone https://github.com/Akegarasu/sd-webui-model-converter.git /content/stablebreaktest/extensions/sd-webui-model-converter

!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml -d /contentstablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_mlsd_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_normalbae_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_seg_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1e_sd15_tile_fp16.yaml -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.yaml
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_style_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_style_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_sketch_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_sketch_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_seg_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_seg_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_openpose_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_openpose_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_keypose_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_keypose_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_depth_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_depth_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_color_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_color_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_canny_sd14v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_canny_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_canny_sd15v2.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_canny_sd15v2.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_depth_sd15v2.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_depth_sd15v2.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_sketch_sd15v2.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_sketch_sd15v2.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_zoedepth_sd15v1.pth -d /content/stablebreaktest/extensions/sd-webui-controlnet/models -o t2iadapter_zoedepth_sd15v1.pth
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
