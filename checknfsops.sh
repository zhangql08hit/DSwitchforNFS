#!/bin/bash

a=`cat /proc/sys/fs/nfs/nlm_timeout`

while [ $a -ne '0' ];
do
	sleep 0.5
	a=`cat /proc/sys/fs/nfs/nlm_timeout`
	echo "check again, $a"
done
echo 'done'
