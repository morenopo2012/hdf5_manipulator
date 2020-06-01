#!/bin/bash

REMDIR=/data/jbonilla

INPBASE=hadmultkineimgs_127x94_pc_mc
INPNAME=${INPBASE}.hdf5
python split_big.py --input $REMDIR/$INPNAME --size 25000
