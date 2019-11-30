#!/usr/bin/env bash
if [[ $1 == "" || $2 == "" ]]
then
  echo "Usage: ./GenerateDay.sh <day> <year>"
else
  inputDay="$(printf "Day%02d" $1)"
  python ./Tools/DownloadDay.py $1 $2
  open -a "Markdown Pro" $inputDay/$inputDay.md
  cp ./Templates/BootstrapCMakeLists.txt.in "./$inputDay/CMakeLists.txt"
  cd $inputDay/bootstrap
  cmake ..
  cd ..
  rm -Rf bootstrap
  cp ../Templates/CMakeLists.txt.in ./CMakeLists.txt
  mkdir xcode
  cd xcode
  cmake -G Xcode ..
  xcodebuild -scheme ALL_BUILD build
  cp $inputDay.txt Debug/
  open -a Xcode $2_AoC_VM_$inputDay.xcodeproj
fi
