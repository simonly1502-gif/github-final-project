#!/bin/bash
# Script to calculate simple interest

# Input principal amount
echo "Enter the principal:"
read p

# Input annual rate of interest
echo "Enter rate of interest per annum:"
read r

# Input time period in years
echo "Enter time period in years:"
read t

# Calculate simple interest
s=`expr $p \* $t \* $r / 100`

echo "The simple interest is: "
echo $s
