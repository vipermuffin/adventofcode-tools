#!/usr/bin/env bash
if [[ $1 == "" || $2 == "" ]]
then
  echo "Usage: ./GenerateDay.sh <day> <year>"
else
  inputDay="$(printf "Day%02d" $1)"
  python ./Tools/DownloadDay.py $1 $2
  retext --preview $inputDay/$inputDay.md&
  cp ./Templates/BootstrapCMakeLists.txt.in "./$inputDay/CMakeLists.txt"
  cd $inputDay/bootstrap
  cmake ..
  cd ..
  rm -Rf bootstrap
  cp ../Templates/CMakeLists.txt.in ./CMakeLists.txt
  mkdir codeblocks
  cd codeblocks
  cmake -G CodeBlocks ..
  ninja
  #cp $inputDay.txt Debug/
  codeblocks 2018_AoC_VM_$inputDay.cbp&
fi
