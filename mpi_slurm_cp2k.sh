#!/bin/bash

cp2k_inputfile=`readlink -f ./base/cp2k_input.inp`

if [ $# -ne 1 ]; then
 echo use ./$0 directory_name 
 echo exit ... 
 exit 
fi 

dir=$1 

for filepath in $dir/*xyz; do 

file=$(basename $filepath)

tmpdir=${file%.xyz}

mkdir $tmpdir

cp $filepath $tmpdir
pushd $tmpdir 

  sed -e  "s/@xyzfile@/$file/" $cp2k_inputfile  > cp2k.inp 

  docker run -v $PWD:/mnt --shm-size=1g cp2k/cp2k:9.1 mpiexec -genv OMP_NUM_THREADS=1 -np 8 cp2k -i cp2k.inp -o cp2k.out

popd 

done 



