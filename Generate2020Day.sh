#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2020Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2020//')
  $genCmd 2020
fi
