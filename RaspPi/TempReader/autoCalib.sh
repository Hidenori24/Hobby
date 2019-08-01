#!/bin/bash

for var in {1..50}
do
  sudo ./dht11_test_cpp $var > result/result$var.dat
  echo "$var times Calib end"
done
echo "Just Calib end!"
