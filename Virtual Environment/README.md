# Virtual Environments


##### Install virtualenv package using pip
    pip install virtualenv
    
##### Create a virtual environment called abcd
    virtualenv abcd

__OR you can create the environment with your preferred python__

##### Create a virtual environment with python3
    virtualenv -p python3 abcd

##### Activate the environment abcd
    source abcd/bin/activate
##### check which python is running
    which python
Now you can install your packages
##### Now your tenserflow will be installed solely inside your abcd environment
    pip install tenserflow

##### Get out of the environment abcd
    deactivate

##### Installing with python3
    python3 -m venv demo