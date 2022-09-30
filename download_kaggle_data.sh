#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: ./download_kaggle_data.sh -d <parameter>"
   echo -e "\t-d The name of the Kaggle dataset to download."
   exit 1 # exit script after printing help
}

# retrieve dataset name as parameter
while getopts "d:" opt
do
   case "$opt" in
      d ) KAGGLE_DATA="$OPTARG" ;;
      ? ) helpFunction ;; # print helpFunction in case parameter is non-existent
   esac
done

# print helpFunction in case parameter is empty
if [ -z "$KAGGLE_DATA" ]
then
   echo "The parameter is empty!";
   helpFunction
fi

# prepare environment
sudo apt install unzip
make install
sudo ln -s ~/.local/bin/kaggle /usr/bin/kaggle

# dowanload data
echo "First arg: $KAGGLE_DATA"
kaggle competitions download -c $KAGGLE_DATA

# unzip data
rm -rf data
mkdir data
unzip $KAGGLE_DATA.zip -d data