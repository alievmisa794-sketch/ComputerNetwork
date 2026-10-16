#!/usr/bin/env python3
"""Проверка математических расчётов IPv4, только ipaddress из stdlib."""
import ipaddress
parent=ipaddress.ip_network('192.168.127.0/24')
subnets=list(parent.subnets(new_prefix=27))
assert len(subnets)==8
assert all(n.num_addresses-2==30 for n in subnets)
for i,network in enumerate(subnets[:5],1):
    hosts=list(network.hosts())
    print(f'Здание {i}: {network}  usable: {hosts[0]} — {hosts[-1]}  broadcast: {network.broadcast_address}')
parent2=ipaddress.ip_network('192.168.126.0/23')
parts=list(parent2.subnets(new_prefix=28))
assert len(parts)==32 and parts[0].num_addresses-2==14
print('Для 20 подсетей по 10+ хостов: родитель /23, дочерние /28, 32 подсети по 14 хостов')
