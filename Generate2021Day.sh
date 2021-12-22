#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2021Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2021//')
  $genCmd 2021
fi
