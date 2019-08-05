#!/bin/bash

for var in `seq -f %02g 24 65`
do
  sudo ./dht11_test_cpp $var > result/result$var.dat
  echo "$var times Calib end"
done
echo "Just Calib end!"
