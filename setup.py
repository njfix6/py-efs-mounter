import re
from setuptools import setup
from pip.req import parse_requirements
install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('py-efs-mounter/__init__.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(name='py-efs-mounter',
      version='0.1',
      description='Mount and unmount to efs',
      entry_points = {
        "console_scripts": ['py-efs-mounter = py-efs-mounter.main:main']
        },
      url='',
      author='Nicholas Fix',
      author_email='njfix6@gmail.com',
      packages=['py-efs-mounter'],
      long_description = long_descr,
      install_requires=reqs,
      version=version
)
