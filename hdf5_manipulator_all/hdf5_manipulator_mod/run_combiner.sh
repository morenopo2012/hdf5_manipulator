#!/bin/bash

INP1_BASE="../hadmultkineimgs_127x94_pc_mc" #../HDF5files/minosmatch_nukecczdefs_genallz_pcodecap66_127x50x25_xuv_me1Bmc_100kevts"
INP2="../hadmultkineimgs_127x94_pc_mc" #"minosmatch_kinedat_me1Bmc.hdf5"
OUTP_BASE="../hadmultkineimgs_127x94_pc_mc" #"minosmatch_nukecczdefs_genallz_pcodecap66_kinedat_127x50x25_xuv_me1Bmc"

START=1 #0
STOP=2 #44

for i in `seq ${START} 1 ${STOP}`
do
  filenum=`echo $i | perl -ne 'printf "%03d",$_;'`
  INP1=${INP1_BASE}${filenum}.hdf5
  OUTP=${OUTP_BASE}${filenum}.hdf5

cat << EOF
    python combine.py \
      --input1 $INP1 \
      --input2 $INP2 \
      --output $OUTP \
      --match eventids \
      --keys1 hits-u,hits-v,hits-x,planecodes,segments,zs

    python fuelme.py $OUTP 0.86 0.07
EOF

  python combine.py \
    --input1 $INP1 \
    --input2 $INP2 \
    --output $OUTP \
    --match eventids \
    --keys1 hits-u,hits-v,hits-x,planecodes,segments,zs

  python fuelme.py $OUTP 0.86 0.07

done
