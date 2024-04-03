from setuptools import setup, find_packages 

setup(
    Name="my-cute-package", 
    version="0.0.0", 
    packages=find_packages(), # It will find all packages in your code, if you want to specify ["packaing", 'packaging.sub_package'] 
    author="Aravind", 
    description="This is a cute project", 
    licence="MIT", 
    install_requires=["numpy==1.24.3"]

)

## To run this file: python setup.py build sdist (source distribuiton)
## This will create "dist" and "packaging.egg-info". Dist folder contains zip file you can install our code. 
## you can install the pacakge ` pip install dist/packaging-0.0.0.tar.gz`
## Now you have succesfuly packaged the code. you can check "pip list"
## Now you can import any higher directory module from lower module :) 

## You can check the package in this path: /workspaces/Learning_py_to_prod-pypi/venv/lib/python3.10/site-packages/packaging
## Basically all the packages will be in site-packages 

## If you're chaning anythign you have to uninstall this package and reinstall to get the new code. 
## But this is very Mandane task to do that. So you can use the --editable command. 
## simply it modify the new chagnes in the venv/site-packages.
## use this: `pip install --editable ./`




