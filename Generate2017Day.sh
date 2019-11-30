#!/usr/bin/env bash
if [[ $1 == "" ]]
then
  echo "Usage: ./Generate2017Day.sh <day>"
else
  genCmd=$(echo $0 $1| sed 's/2017//')
  $genCmd 2017
fi
