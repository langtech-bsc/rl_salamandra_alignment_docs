.. highlight:: shell

============
Installation
============


Stable release
--------------

To install RL - Salamandra Alignment, first prepare a new virtual environment:

.. code-block:: console
    
    $ pip install trl==0.13.0
    $ pip install wheel
    $ pip install flash-attn==2.6.3 --no-build-isolation
    $ pip install sentencepiece==0.2.0 protobuf==5.28.2
    $ pip install deepspeed==0.15.1
    $ pip uninstall triton -y
    $ pip install wandb

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
