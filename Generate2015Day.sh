#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2015Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2015//')
  $genCmd 2015
fi
