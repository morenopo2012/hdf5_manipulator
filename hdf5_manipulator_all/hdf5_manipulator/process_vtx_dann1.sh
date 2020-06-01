#!/bin/bash

REMDIR=/data/minerva/DANN_hdf5

# INPBASE=minosmatch_nukecczdefs_genallz_pcodecap66_127x50x25_xuv_me1Bmc
# INPNAME=${INPBASE}.hdf5
# python split_big.py --input $REMDIR/$INPNAME --size 50000
# NMAX=`ls $REMDIR/${INPBASE}_*.hdf5 | wc -l`
# NMAX=$((NMAX - 1))

# for i in `seq 0 1 $NMAX`
# do
#   filenum=`echo $i | perl -ne 'printf "%03d",$_;'`
#   echo $filenum
#   cp $REMDIR/${INPBASE}_${filenum}.hdf5 $REMDIR/unrenamed/${INPBASE}_${filenum}.hdf5
#   python rename_dataset.py --input $REMDIR/${INPBASE}_${filenum}.hdf5 \
#     --dataset hits-x --name hits-x-MEMC
#   python rename_dataset.py --input $REMDIR/${INPBASE}_${filenum}.hdf5 \
#     --dataset hits-u --name hits-u-MEMC
#   python rename_dataset.py --input $REMDIR/${INPBASE}_${filenum}.hdf5 \
#     --dataset hits-v --name hits-v-MEMC
# done

INPBASE=hadmultkineimgs_127x94_me1Lmc_001
INPNAME=${INPBASE}.hdf5
#NMAX=`ls $REMDIR/${INPBASE}_*.hdf5 | wc -l`
#NMAX=$((NMAX - 1))
#for i in `seq 0 1 $NMAX`
#do
 # filenum=`echo $i | perl -ne 'printf "%03d",$_;'`
  echo $filenum
  python rename_dataset.py --input $REMDIR/${INPBASE}.hdf5 \
    --dataset hitimes-x --name hitimes-x-me1LOPmc
  python rename_dataset.py --input $REMDIR/${INPBASE}.hdf5 \
    --dataset hitimes-u --name hitimes-u-me1LOPmc
  python rename_dataset.py --input $REMDIR/${INPBASE}.hdf5 \
    --dataset hitimes-v --name hitimes-v-me1LOPmc
#done
#INPBASE=mnvimgs_127x94_me1Pdata_subset
#INPNAME=${INPBASE}.hdf5
#NMAX=`ls $REMDIR/${INPBASE}_*.hdf5 | wc -l`
#NMAX=$((NMAX - 1))

#for i in `seq 0 1 $NMAX`
#do
#  filenum=`echo $i | perl -ne 'printf "%03d",$_;'`
#  echo $filenum
#  python rename_dataset.py --input $REMDIR/${INPBASE}_${filenum}.hdf5 \
#    --dataset hitimes-v-meLOPdata --name hitimes-v-me1LOPdata
#done
