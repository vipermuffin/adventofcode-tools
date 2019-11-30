#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2016Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2016//')
  $genCmd 2016
fi
