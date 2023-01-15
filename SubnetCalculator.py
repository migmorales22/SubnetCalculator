#! /usr/bin/env Subnet Calculator
import argparse
from ipaddress import ip_interface

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--host", help="host address", required=True)
    parser.add_argument("-m", "--mask", help="mask", required=True)

    args = parser.parse_args()

    iface = ip_interface(f"{args.host}/{args.mask}")
    network = iface.network.with_netmask
    network2 = iface.network.with_prefixlen
    broadcast = iface.network.broadcast_address
    wildcard = iface.network.with_hostmask
    hostmask = iface.hostmask
    hosts = list(iface.network.hosts())
    minimum_host = min(hosts, default=None) 
    maximum_host = max(hosts, default=None)
    num_address = iface.network.num_addresses
    print(f"""
Network:              {network} or {network2}
Wilcard:              {wildcard}
Broadcast:            {broadcast}
Minimum Host:         {minimum_host}
Maximum Host:         {maximum_host}
Hosts per Network:    {len(hosts)}
Number of Address:    {num_address}
""")

if __name__ == "__main__":
    main()
