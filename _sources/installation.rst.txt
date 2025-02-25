.. highlight:: shell

============
Installation
============


Stable release
--------------

To install RL - Salamandra Alignment, first prepare a new virtual environment:

.. code-block:: console
    $ # Python 3.9.16
    $ pip install wheel setuptools
    $ pip install trl==0.12.1
    $ MAX_JOBS=4 pip install flash-attn==2.7.3 --no-build-isolation
    $ pip install pip install --upgrade transformers==4.49.0 sentencepiece==0.2.0 protobuf==5.29.3 deepspeed==0.16.4 wandb==0.19.7 importlib_metadata==8.6.1
    $ pip uninstall triton -y

Now, run this command in your terminal:

.. code-block:: console

    $ pip install git+https://github.com/langtech-bsc/rl_salamandra_alignment.git

This is the preferred method to install RL - Salamandra Alignment, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Experimental Release
------------

The sources for RL - Salamandra Alignment can be downloaded from the `Github repo <https://github.com/langtech-bsc/rl_salamandra_alignment>`.

After preparing a new virtual environment (explained above), you can clone the public repository:

.. code-block:: console

    $ git clone https://github.com/langtech-bsc/rl_salamandra_alignment.git


Once you have a copy of the source, you can install it in editable mode with:

.. code-block:: console

    $ pip install -e rl_salamandra_alignment
