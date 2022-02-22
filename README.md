# nrrd2nii
Command line tool designed to convert nrrd (or nrrd header and image) files to NIFTI-1 images.

## Installation
-----

### Dependencies

The required `python` v3.6+ dependencies include:      

* `nibabel`
* `numpy`
* `pynrrd`

The dependencies can be installed as followed:

```bash
git clone https://github.com/AdebayoBraimah/nrrd2nii.git
cd nrrd2nii
pip install -r requirements.txt
```


## Usage
-----

Example usage:

```zsh
./nrrd2nii.py --nrrd=image.nrrd --gzip
```

**NOTE**: The above example assumes that the files `nrrd2nii.py` and `image.nrrd` are in the same directory.

Typing: `./nrrd2nii.py -h` should show the help menu (shown below).

```
usage: nrrd2nii.py [-h] [-n <STR>] [-z]

Command line tool designed to convert nrrd (or nrrd header and image) files to NIFTI-1 images. The
corresponding output file is of the same name with a '.nii' or '.nii.gz' file extension.

optional arguments:
  -h, --help              show this help message and exit

Required Arguments:
  -n <STR>, --nrrd <STR>  REQUIRED: Input nrrd or nhdr file.

Optional Arguments:
  -z, --gzip              OPTIONAL: Gzips output file.
```
