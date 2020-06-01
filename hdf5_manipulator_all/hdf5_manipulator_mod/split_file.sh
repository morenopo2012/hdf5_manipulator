#!/bin/bash

REMDIR=/data/$USER

INPBASE=hadmultkineimgs_127x94_me1Fmc
INPNAME=${INPBASE}.hdf5
python split_big.py --input $REMDIR/$INPNAME --size 50000
