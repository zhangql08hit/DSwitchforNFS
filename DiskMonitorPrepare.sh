#!/bin/bash

fdisk -l | grep '^Disk /dev/sd' | awk '{print $2}' > pastr.txt
