#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2019Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2019//')
  $genCmd 2019
fi
