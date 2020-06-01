#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --nodelist=gpu2
#SBATCH --job-name=split_file
echo "started "`date`" "`date +%s`""

nvidia-smi -L

NGPU=1

# pick up singularity v2.2
export PATH=/usr/local/singularity/bin:$PATH
# which singularity image
SNGLRTY="/data/minerva/anushree/simg_file/anushree85-singularity_imgs-master-wilson_caffe_0.15_dann_cuda7.5_cudnn5.simg"
CAFFE="/opt/caffe/build/tools/caffe"
NETWORKDIR=/data/aghosh12/hdf5_manipulator

# show what we will do...
cat << EOF
singularity exec $SNGLRTY ./split_file.sh
EOF
# do the thing...
singularity exec --nv $SNGLRTY ./split_file.sh
nvidia-smi

echo "finished "`date`" "`date +%s`""
exit 0
