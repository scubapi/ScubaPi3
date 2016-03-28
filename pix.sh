#!/bin/bash

d=`date +%H%M-%j`

mkdir $d
cd $d

/opt/vc/bin/raspistill -t 0 -tl 5000 -ex night -o pi-%04d.jpg
