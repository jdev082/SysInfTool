import distro
import os
import platform
import psutil

cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | cut -c14- | sed -n 1p").read()
instdat = os.popen("stat / | grep 'Birth' | sed 's/Birth: //g' | cut -b 2-11").read()
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
<p>CPU: {cpu}
<p>RAM: {str(psutil.virtual_memory().total / (1024 * 1024 * 1024))[0:4]} GB""" 