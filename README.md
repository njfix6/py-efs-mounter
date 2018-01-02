# Py-efs-mounter

## Overview

This is a python command line module to mount to aws elastic file servic

### Prerequisites
[Python 3](https://www.python.org/downloads/) - Python 3


### Installation
Run `pip3 install py-efs-mounter`

### Usage
Run `py-efs-mounter --help
usage: py-efs-mounter [-h] [--test TEST] [--profile AWS_PROFILE]
                      [--mount-version MOUNT_VERSION] [--region REGION]
                      [--credentials AWS_CREDENTIALS] [--rsize RSIZE]
                      [--wsize WSIZE] [--resilience RESILIENCE]
                      [--timeo TIMEO] [--retrans RETRANS] --mount-point
                      EFS_MOUNT_POINT
                      {mount,unmount} ...

positional arguments:
  {mount,unmount}       commands
    mount               Mount to EFS
    unmount             Unmount from EFS

optional arguments:
  -h, --help            show this help message and exit
  --test TEST           Test the speed of file transfer
  --profile AWS_PROFILE
                        The aws cli profile
  --mount-version MOUNT_VERSION
                        The version for your mount executable
  --region REGION       The region your efs is in
  --credentials AWS_CREDENTIALS
                        The path to your aws credentials folder
  --rsize RSIZE         The the rsize for your efs
  --wsize WSIZE         The the wsize for your efs
  --resilience RESILIENCE
                        Wheather to wait if for efs to come back online or not
  --timeo TIMEO         Timeout wait for connection
  --retrans RETRANS     Number of retries to connect
  --mount-point EFS_MOUNT_POINT
                        The mount point for your efs`

### Testing
Clone the repo by running `git clone https://github.com/njfix6/py-efs-mounter.git`
Make a PR to the repo.

### Contributing

### Shout outs
Thanks to Jan-Philip Gehrcke for a sweet walk through on command line applications for python https://gehrcke.de/2014/02/distributing-a-python-command-line-application/
