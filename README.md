# shadowsocks-for-free
## how to use?
###1. configure Switch-Omega
   1. install the plugin named "switch-omega" into google-chrome
   2. click the icon located in up-right corner of the browser and select the 'auto-switch' option.
   3. configure proxy:<br>
   proxy scheme(代理协议): <b><em>socket5</em></b> <br>
   proxy server(代理服务器): <b><em>127.0.0.1</b></em><br>
   proxy port(代理端口): <b><em>1987</b></em><br>
   4. configure auto-swith rules: e.g. <b><em>*google.com</b></em>
   
###2. install python-dependency
$ pip install -r requirement.txt <br>
(if you want to bulid binary file under windows, download and install the py2exe binary file of verison 0.6.9)

###3. Launch a local server
#### unix-like os
  $ sudo python freess.py start/restart
#### windows
  1. $ python freess.py
  2. build binary via double-click the 'setup.py' file
     and you will get an executable located in diretory named "dist".
  
