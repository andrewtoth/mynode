import os
import subprocess
from config import *


# Generic service check
def is_service_enabled(service):
    cmd = "systemctl status {} --no-pager".format(service)
    try:
        results = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        if "enabled;" in results:
            return True
    except:
        return False
    return False


# Enable disable functions on homepage
def is_lndhub_enabled():
    if os.path.isfile(LNDHUB_ENABLED_FILE):
        return True
    return False

def enable_lndhub():
    os.system("systemctl enable lndhub --no-pager")
    os.system("systemctl start lndhub --no-pager")
    open(LNDHUB_ENABLED_FILE, 'a').close() # touch file

def disable_lndhub():
    if os.path.isfile(LNDHUB_ENABLED_FILE):
        os.remove(LNDHUB_ENABLED_FILE)
    os.system("systemctl stop lndhub --no-pager")
    os.system("systemctl disable lndhub --no-pager")


def is_electrs_enabled():
    if os.path.isfile(ELECTRS_ENABLED_FILE):
        return True
    return False

def enable_electrs():
    os.system("systemctl enable electrs --no-pager")
    os.system("systemctl start electrs --no-pager")
    open(ELECTRS_ENABLED_FILE, 'a').close() # touch file

def disable_electrs():
    if os.path.isfile(ELECTRS_ENABLED_FILE):
        os.remove(ELECTRS_ENABLED_FILE)
    os.system("killall -9 electrs") # Hard kill since we are disabing
    os.system("systemctl stop electrs --no-pager")
    os.system("systemctl disable electrs --no-pager")


def is_btcrpcexplorer_enabled():
    if os.path.isfile(BTCRPCEXPLORER_ENABLED_FILE):
        return True
    return False

def enable_btcrpcexplorer():
    os.system("systemctl enable btc_rpc_explorer --no-pager")
    os.system("systemctl start btc_rpc_explorer --no-pager")
    open(BTCRPCEXPLORER_ENABLED_FILE, 'a').close() # touch file

def disable_btcrpcexplorer():
    if os.path.isfile(BTCRPCEXPLORER_ENABLED_FILE):
        os.remove(BTCRPCEXPLORER_ENABLED_FILE)
    #os.system("killall -9 electrs") # Hard kill since we are disabing
    os.system("systemctl stop btc_rpc_explorer --no-pager")
    os.system("systemctl disable btc_rpc_explorer --no-pager")


def is_vpn_enabled():
    if os.path.isfile(VPN_ENABLED_FILE):
        return True
    return False

def enable_vpn():
    os.system("systemctl enable vpn --no-pager")
    os.system("systemctl start vpn --no-pager")
    open(VPN_ENABLED_FILE, 'a').close() # touch file

def disable_vpn():
    if os.path.isfile(VPN_ENABLED_FILE):
        os.remove(VPN_ENABLED_FILE)
    os.system("systemctl stop vpn --no-pager")
    os.system("systemctl disable vpn --no-pager")
    os.system("systemctl stop openvpn --no-pager")
    os.system("systemctl disable openvpn --no-pager")


def is_netdata_enabled():
    return is_service_enabled("netdata")

def enable_netdata():
    os.system("systemctl enable netdata --no-pager")
    os.system("systemctl start netdata --no-pager")

def disable_netdata():
    os.system("systemctl stop netdata --no-pager")
    os.system("systemctl disable netdata --no-pager")