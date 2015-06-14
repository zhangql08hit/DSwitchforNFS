#!/bin/bash

#a=`fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}' | wc -l`
#astr=`fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}'`
astr=`cat pastr.txt`
a=`cat pastr.txt | wc -l`
b=`fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}' | wc -l`

echo 'Start Monitoring Disks...'

while [ $a -eq $b ];
do
	b=`fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}' | wc -l`
	echo 'refresh'
	sleep 0.5
done

bstr=`fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}'`

if [ $a -gt $b ]; then
	echo 'disk removed'
else
	echo 'disk added'
	for i in $bstr
	do
		rst=`echo $astr | grep $i`
		if [ -z $rst ]; then
			disk=$i
			break
		fi
	done
	echo "the added disk: $disk"
	len=`expr length $disk`
	llen=`expr $len - 1`
	part=`echo $disk | cut -b 1-$llen`
	mount -t ext4 "${part}1" /home/disk1
fi
