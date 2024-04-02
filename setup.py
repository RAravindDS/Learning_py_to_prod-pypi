from setuptools import setup 

setup(
    Name="my-cute-package", 
    version="0.0.0", 
    packages=['packaging'], 
    author="Aravind", 
    description="This is a cute project", 

)

## To run this file: python setup.py build sdist (source distribuiton)
## This will create "dist" and "packaging.egg-info". Dist folder contains zip file you can install our code. 
## you can install the pacakge ` pip install dist/packaging-0.0.0.tar.gz`
## Now you have succesfuly packaged the code. you can check "pip list"


