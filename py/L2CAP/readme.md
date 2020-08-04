
## Before running the example
* sudo apt-get install bluetooth libbluetooth-dev 
* pip3 install pybluez

## before starting the server.py 
* go to /etc/bluetooth/main.conf 
* if DisablePlugins exists change value to pnat
* if not exists add DisablePlugins = pnat 
* execute sudo systemctl restart bluetooth