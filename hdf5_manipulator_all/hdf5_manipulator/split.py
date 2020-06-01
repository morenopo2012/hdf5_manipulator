#!/usr/bin/env python
"""
Split hdf5 file
"""
import os
import sys
from collections import OrderedDict
from parser import get_args_split as parser
import msg
import hdf5
import check


def generate_filelist(prefix, old_size, new_size):

    """Generate filenames for output files
    and return as a dict (file: [begin, end]).

    Keyword arguments:
    prefix -- common path/to/basename
    old_size -- size of input hdf5 files
    new_size -- requested size for output hdf5 files
    """
    print "i am hereeeeee", new_size, old_size
    if new_size >= old_size:
        msg.error("Use splitter wisely...")
        sys.exit(1)

    nof_files, leftover = old_size / new_size, old_size % new_size

    files = OrderedDict()
    for i in range(nof_files + int(leftover > 0)):
        filename = "%(prefix)s_%(id)03d.hdf5" % {"prefix": prefix, "id": i}
        begin = i * new_size
        end = (i + 1) * new_size if i < nof_files else i * new_size + leftover
        files[filename] = [begin, end]

    print "files", nof_files
    return files


def save_filelist(filename, filelist):

    """Save the list of created files.

    Keyword arguments:
    filename -- the path to txt file
    filelist -- the list of files
    """

    f = open(filename, 'w')

    for fn in filelist:
        print >>f, os.path.abspath(fn)

    f.close()

if __name__ == '__main__':

    msg.box("HDF5 MANIPULATOR: SPLIT")

    args = parser()
    data = hdf5.load(args.input)

    print "The following datasets were found in %s:\n" % args.input
    print "data=", data
    msg.list_dataset(data)
    filelist = generate_filelist(
        args.prefix or os.path.splitext(args.input)[0],
        check.get_size(data), int(args.size))

    print "\nSaving output files woww:\n"
    print "iteritmes",  filelist.iteritems()
    for f, r in filelist.iteritems():
        print "i am inside split now"
        msg.list_fileinfo(f, r)
        print "r[0] r[1]", r[0], r[1]
        hdf5.save_subset(f, data, r[0], r[1])

    if args.filelist:
        save_filelist(args.filelist, filelist.keys())

    msg.info("Done")
