import distro
import os
import platform
import psutil

cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | cut -c14- | sed -n 1p").read()
instdat = os.popen("stat / | grep 'Birth' | sed 's/Birth: //g' | cut -b 2-11").read()
net = os.popen("nmcli device status").read()
storage = os.popen("df -h").read()
gpu = os.popen('GPU=$(lspci | grep VGA | cut -d ":" -f3);RAM=$(cardid=$(lspci | grep VGA |cut -d " " -f1);lspci -v -s $cardid | grep " prefetchable"| cut -d "=" -f2);echo $GPU').read()[0:50]
gpu_vram = os.popen('RAM=$(cardid=$(lspci | grep VGA |cut -d " " -f1);lspci -v -s $cardid | grep " prefetchable"| cut -d "=" -f2);echo $RAM').read().replace("]", " ")

content = f"""
<h1>{distro.name()} {distro.version()}</h1>
<h2>Userspace</h2>
<p>user: {os.getenv('USER')}
<p>hostname: {os.getenv('HOSTNAME')}
<p>Desktop Environment: {os.getenv('DESKTOP_SESSION')}
<p>session type: {os.getenv('XDG_SESSION_TYPE')}
<h2>System Software Components</h2>
<p>kernel: {platform.release()}</p>
<p>installation date: {instdat}</p>
<h2>Computer Hardware</h2>
<p>CPU: {cpu}</p>
<p>GPU: {gpu}, {gpu_vram}</p>
<p>RAM: {str(psutil.virtual_memory().total / (1024 * 1024 * 1024))[0:4]} GB
<h2>Networking</h2>
<pre>{net}</pre>
<h2>Storage</h2>
<pre>{storage}</pre>
"""