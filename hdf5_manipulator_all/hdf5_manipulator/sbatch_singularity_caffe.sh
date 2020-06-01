#!/bin/bash
DAT=`date +%s`
OUTFILENAME="./rename_1lmc_missing.txt"
NGPU=1
#show what we will do...
cat << EOF
sbatch --gres=gpu:${NGPU} slurm_singularity_caffe.sh
EOF

# do the thing, etc.
sbatch --gres=gpu:${NGPU} -p gpu -o $OUTFILENAME slurm_singularity_caffe.sh
