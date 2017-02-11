#!/bin/bash

while getopts ":v:" opt; do
  case $opt in
    v) version="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

if [ $version == "" ]; then
  echo "-v (build version) is required"
  exit
fi

echo Cleanup build directory
rm -rf build
mkdir -p build

echo
echo
echo Build dev-client for all supported platforms..
echo
echo "Target LINUX, ARM, GOARM=5"
env GOOS=linux GOARCH=arm GOARM=5 go build && mv dev-client build/dev-client-linux-arm-$version
echo "Target LINUX, 32bit"
env GOOS=linux GOARCH=386 go build && mv dev-client build/dev-client-linux-32-$version
echo "Target LINUX, 64bit"
env GOOS=linux GOARCH=amd64 go build && mv dev-client build/dev-client-linux-64-$version
echo "Target DARWIN, 32bit"
env GOOS=darwin GOARCH=386 go build && mv dev-client build/dev-client-mac-32-$version
echo "Target DARWIN 64bit"
env GOOS=darwin GOARCH=386 go build && mv dev-client build/dev-client-mac-64-$version
echo "Target DARWIN ARM 32bit"
env GOOS=darwin GOARCH=arm go build && mv dev-client build/dev-client-mac-arm-$version
echo "Target WINDOWS, 32bit "
env GOOS=windows GOARCH=386 go build && mv dev-client.exe build/dev-client-win-32-$version.exe
echo "Target WINDOWS, 64bit"
env GOOS=windows GOARCH=amd64 go build && mv dev-client.exe build/dev-client-win-64-$version.exe

cd build && zip -r -X dev-client-bins-$version.zip * && cd ../
cd build && tar czf dev-client-bins-$version.tar.gz * && cd ../
