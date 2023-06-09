import distro
import os
import platform
import psutil

cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | cut -c14- | sed -n 1p").read()
content = f"<h1>{distro.name()} {distro.version()}</h1>" \
"<h2>Userspace</h2>" \
f"<p>user: {os.getenv('USER')}" \
f"<p>hostname: {os.getenv('HOSTNAME')}" \
f"<p>Desktop Environment: {os.getenv('DESKTOP_SESSION')}" \
f"<p>session type: {os.getenv('XDG_SESSION_TYPE')}" \
"<h2>System Software Components</h2>" \
f"<p>kernel: {platform.release()}</p>" \
"<h2>Computer Hardware</h2>" \
f"<p>CPU: {cpu}" \
f"<p>RAM: {str(psutil.virtual_memory().total / (1024 * 1024 * 1024))[0:4]} GB" 