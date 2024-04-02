# Python Packaging Index

The pypi website contains the **zip file** contains python code as well as crucial metadata about the code and allows us to run it ourself. So a **package** is a distributable set of python code together with the metadata about how to run that code. 

## Why do we need to package the code? 

The first advantage is that **distributing your code**, there are lot of ways you can distribute your code like `cli`, and `executable`. Packaging is one of the way you can **distribute** our code. Eventhough you're a team of one, packaging a code can give lot of benefits. Will discuss this part later.

The second advantage is that **non-painful import statements**. If you're working with multiple python files, you will sure have a problem with import the module for 1 dir away. 

The third advantage is that **reproducibility**, it means the ability to run your code or rerun your code and always get consistent results.

And, having this skill is going to seriously improve quality of life while you're writing code. 

## Concepts in packaging

### 1. PythonPath

There are two types of import in python
   1. Relative Import 
   2. absolute Import 
   
**Relative**: `from ..myotherfile import CONSTANT`

**Absolute**: `from packaging.myotherfile import CONSTANT`


You can easily import a file under your file directory however If you want to import a file above your file directory using **relative** or **absolute** import you wil get a error like **module** not found. 

To solve this issue we can use **PYTHONPATH** variable to solve this problem. **PYTHONPATH** variable contains a list of folders where python looks for modules when you do these import statements.  


**First method to solve the issue**: 

If you want to import a module which contains above your directory you can use **append** the parent directory to the python path and then you can import a module without any error. 

`PYTHONPATH=$PYTHONPATH:/workspaces/Learning_py_to_prod-pypi python packaging/sub_package/myfile.py`

But this will only work if you're calling the file with python path, if you're calling normal way `python packaging/sub_package/myfile.py` it won't work. You will get a error like **package** (module) not found. 

**Second method to solve this issue**: 

In last approach we have to call the file with pythonpath, let's solve this issue by adding the path to the sys. 

```python
import sys 
sys.path.insert(0, "/workspaces/Learning_py_to_prod-pypi")
from packaging.myotherfile import CONSTANT
```

It will work for sure, because we are adding to the path everytime we are calling the function. But this is the **worst way of doing this**. 

-------------------------------
-----------------------------
### 2. Module 

Module is a **single piece** of an **import path** in python. People also say that module is a **file** ends in **.py** however folders can be a **module**. 


