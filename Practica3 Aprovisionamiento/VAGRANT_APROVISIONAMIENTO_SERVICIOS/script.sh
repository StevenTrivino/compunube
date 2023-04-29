#!/bin/bash

echo "configurando el resolv.conf con cat"
cat <<TEST> /etc/resolv.conf
nameserver 8.8.8.8
TEST

echo "instalando un servidor vsftpd"
sudo apt-get install vsftpd -y

echo “Modificando vsftpd.conf con sed”
sed -i 's/#write_enable=YES/write_enable=YES/g' /etc/vsftpd.conf
sudo service vsftpd restart

echo "configurando ip forwarding con echo"
sudo echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf

echo "instalando Jupiter notebooks"

sudo apt-get update -y
sudo apt install python3-pip -y
pip3 install jupyter
export PATH="$HOME/.local/bin:$PATH"
