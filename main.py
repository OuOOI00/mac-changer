import subprocess as sbp
import optparse as opt
import re


def get_arguments():
    parser = opt.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="\n-i/--interface is your parametr of interface ")
    parser.add_option("-m", "--mac", dest="new_mac", help="\n-m/new_mac is your parametr of new Mac address")
    (options, arguments) = parser.parse_args()

    if not options.interface and not options.new_mac:
        parser.error("[-] Please, specify an new Interface and a new Mac address, use help command \"--help/h\" for more information ")
    elif not options.new_mac:
        parser.error("[-] Please, specify a new Mac address, use help command \"--help/h\" for more information ")
    elif not options.interface:
        parser.error("[-] Please, specify an interface, use help command \"--help/-h\" for more information ")
    return options

def mc_changer(interface,new_mac):
    print("[+] eth0 Mac address " + interface + " changed to " + new_mac)
    sbp.call(["ifconfig", interface, "down"])
    sbp.call(["ifconfig", interface, "hw", "ether", new_mac])
    sbp.call(["ifconfig", interface, "up"])
    43
    
def get_currentMC(interface):
    ifconfig_param = sbp.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_param)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Couldn't read MAC ADDRESS!")

options = get_arguments()

current_mac = get_currentMC(options.interface)
print("Current eth0 Mac address = " + str(current_mac))

mc_changer(options.interface,options.new_mac)

current_mac = get_currentMC(options.interface)
if current_mac == options.new_mac:
    print("[+] Current eth0 Mac address = " + str(current_mac))
else:
    print("[-] Mac address don't be change ")
