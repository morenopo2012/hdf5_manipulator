"""
HDF5 files tools for HDF5 Manipulator
"""

import h5py


def load(filename):

    """Load hdf5 file to data dictionary and return it.

    Keyword arguments:
    filename -- the full path to hdf5 file
    """

    f = h5py.File(filename, 'r')

    data = {}

    for key in f:
        data[key] = f[key][...]

    f.close()

    return data


def save(filename, data):

    """Create hdf5 file with given data.

    Keyword arguments:
    filename -- the full path to hdf5 file
    data -- dictionary with data
    """

    f = h5py.File(filename, 'w')

    for key in data:
        for member in data[key]:
             f.create_dataset(key, member, data[key][member].shape, dtype=data[key][member].dtype,
                         compression='gzip')[...] = data[key][member]

    f.close()


def save_subset(filename, data, begin, end):

    """Create hdf5 file with subset [begin, end) of given data.

    Keyword arguments:
    filename -- the full path to hdf5 file
    data -- dictionary with data
    begin -- start saving from index=i
    end -- finish savin at index=end
    """

    subset = {}

    for key in data:
        for member in data[key]:
           subset[key][member] = data[key][member][begin:end]

    save(filename, subset)


def save_subset_big(filename, data, begin, end):

    """Create hdf5 file with subset [begin, end) of given data.

    Keyword arguments:
    filename -- the full path to hdf5 file
    data -- input file
    begin -- start saving from index=i
    end -- finish savin at index=end
    """

    o = h5py.File(filename, 'w')

    for key in data:
        print "key", key
        #grp = o.create_group(key)
        for member in data[key]:
            shape = list(data[key][member].shape)
            dtype=data[key][member].dtype
            #print data[key][member][begin:end]
            shape[0] = end - begin
            o.create_dataset(member, shape, dtype,
                         compression='gzip')[...] = data[key][member][begin:end]
            #grp.create_dataset(member, shape, dtype,
            #             compression='gzip')[...] = data[key][member][begin:end]

    o.close()
