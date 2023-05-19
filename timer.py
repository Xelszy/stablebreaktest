import os
import shutil

static_dir = '/content/stablebreaktest/static'
os.makedirs(static_dir, exist_ok=True)

timer_dir = '/content/stablebreaktest/extensions-builtin/nocrypt-colab-timer/javascript'
os.makedirs(timer_dir, exist_ok=True)

timer_script = 'colab-timer.js'
timer_script_path = os.path.join(timer_dir, timer_script)

if not os.path.exists(timer_script_path):
    curdir = os.path.dirname(os.path.realpath(__file__))
    src_timer_script = os.path.join(curdir, timer_script)
    shutil.copy2(src_timer_script, timer_script_path)

#import os, shutil
#curdir = os.path.dirname(os.path.realpath(__file__))
#os.makedirs('/content/stablebreaktest/static', exist_ok=True)
#timerscriptdir = '/content/stablebreaktest/extensions-builtin/nocrypt-colab-timer/javascript'
#os.makedirs(timerscriptdir, exist_ok=True)
#timerscriptpath = os.path.join(timerscriptdir, 'colab-timer.js')
#if not os.path.exists(timerscriptpath):
 #   shutil.copy2(os.path.join(curdir, 'colab-timer.js'), os.path.join(timerscriptpath))
  
