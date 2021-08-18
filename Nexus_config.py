from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file = "config.yaml", dry_run=True,
)
Nex1=nr.run(netmiko_send_config, config_file="Nexus.txt")
Nex2=nr.run(netmiko_send_config, config_file="vlan.txt")
Nex3=nr.run(netmiko_send_config, config_commands=["interface lo 16", "description config con Nornir", "ip add 6.6.8.9/32"])
Nex4=nr.run(netmiko_send_command, command_string="show ip int brief")
Nex5=nr.run(netmiko_send_command, command_string="show vlan b")
print_result(Nex1)
print_result(Nex2)
print_result(Nex3)
print_result(Nex4)
print_result(Nex5)