# Subnet Calculator

This script is a simple yet powerful tool for calculating subnets. It uses the built-in 'ipaddress' library to perform various subnetting operations such as finding the network address, broadcast address, and the range of IP addresses within a subnet. It also includes a user-friendly interface that makes it easy to input and process subnet information. Whether you are a network administrator or a student studying networking, this script is a valuable tool to have in your toolbox.

**Note:** You just need to run the python in your cmd like this:

```js
python3 SubnetCalculator.py -a {ip-address} -m {subnet-mask}
```
You can put the subnet mask complete or abbreviate, for example:
```js
python3 SubnetCalculator.py -a 181.232.180.1 -m 255.255.252.0 

or

python3 SubnetCalculator.py -a 181.232.180.1 -m 24
```

And the output would be:
```js
user@user % python3 SubnetCalculator.py -a 181.232.180.1 -m 255.255.252.0 

Network:              181.232.180.0/255.255.252.0 or 181.232.180.0/22
Wilcard:              181.232.180.0/0.0.3.255
Broadcast:            181.232.183.255
Minimum Host:         181.232.180.1
Maximum Host:         181.232.183.254
Hosts per Network:    1022
Number of Address:    1024
```
## Requirements

* argparse
* ipaddress
* Python 3.9 =>


