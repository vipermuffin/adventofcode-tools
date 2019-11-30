#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2018Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2018//')
  $genCmd 2018
fi
