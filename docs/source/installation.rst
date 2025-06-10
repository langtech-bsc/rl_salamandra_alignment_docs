.. highlight:: shell

============
Installation
============


Stable release
--------------

To install RL - Salamandra Alignment, first prepare a new virtual environment:

.. code-block:: console

    $ # Create a Python 3.12 venv
    $ module load impi intel hdf5 mkl cuda/12.6 python/3.12.1-gcc
    $ VENV_PATH=<your_venv_path>
    $ python -m venv $VENV_PATH


This is how you activate a `python 3.12` virtual environment in Mare Nostrum 5:

.. code-block:: console

    $ # Activate a Python 3.12 venv
    $ module load impi intel hdf5 mkl cuda/12.6 python/3.12.1-gcc
    $ VENV_PATH=<your_venv_path>
    $ # It is extremely important to change the python path
    $ export PYTHONPATH="$VENV_PATH/lib/python3.12/site-packages"
    $ source $VENV_PATH/bin/activate


The most complicated part of the installation is the compilation of `flash-attn`:  

.. code-block:: console
    
    $ # Inside yout Python 3.12.1 venv
    $ pip install wheel setuptools packaging
    $ pip install ninja==1.11.1.4
    $ pip install trl==0.18.1
    $ # Specify the compilers. cuda 12.6 is already loaded when activating the venv
    $ export CXX=g++
    $ export CC=gcc
    $ # Compiling flash attention can take between 1-2 hours
    $ MAX_JOBS=8 pip install --verbose flash-attn==2.7.4.post1 --no-build-isolation --use-pep517

Finally, you can install all the other requirements:

.. code-block:: console

    $ # Inside yout Python 3.12.1 venv
    $ pip install --upgrade transformers==4.51.3 sentencepiece==0.2.0 protobuf==5.29.3 deepspeed==0.16.4 wandb==0.19.7 importlib_metadata==8.6.1

Now, run this command in your terminal:

.. code-block:: console

    $ pip install --upgrade --force-reinstall git+https://github.com/langtech-bsc/rl_salamandra_alignment.git

This is the preferred method to install RL - Salamandra Alignment, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Experimental Release
------------

The experimental release is for custom changes to our package or to external packages, like `trl`.

The sources for RL - Salamandra Alignment can be downloaded from the `Github repo`_.

.. _Github repo: https://github.com/langtech-bsc/rl_salamandra_alignment

You will need to create and activate a virtual environment, like explained above.

To install `trl` for the experimental release, clone our `fork of TRL`_Github, checkout the relevant branch and install it:

.. code-block:: console
    $ cd <path to local trl repo>
    $ pip install -e trl

.. _fork of TRL: https://github.com/langtech-bsc/trl

Then, you can proceed with installing `flash-attn` and the other required packages.

Now, you can clone the public repository:

.. code-block:: console
    $ git clone https://github.com/langtech-bsc/rl_salamandra_alignment.git


Once you have a copy of the source, you can navigate to your developement branch, and install it in editable mode with:

.. code-block:: console
    $ cd <path to local rl repo>
    $ pip install -e rl_salamandra_alignment
