=====
Usage
=====

After :doc:`installing <installation>`, you will be able to run RL experiments using the package.

----------
Experiment
----------

An experiment consists of two parts:
    - Training
    - Evaluation (optional)
        - Harness Evaluation
        - Local Evaluation

All the configurations and hyperparameters for an experiment must be specified in a **configuration file** in YAML. 

For evaluation, we use the Evaluation Harness, and, for tasks not implemented in the Evaluation Harness, we use custom scripts (This is what we call "Local Evaluation").

All evaluation jobs are submited to MareNostrum5 with dependencies to training jobs.

Note that evaluation is optional: if you do not specify an ``"evaluation"`` field in your `config.yaml` file, then only training will happen.


------------------------------------
Configuration file for an Experiment
------------------------------------

First, you will need a configuration file in YAML for your experiment (The values marked with ``None`` are computed internally by the package):

.. code-block:: yaml
    :caption: Example YAML configuration file
    :name: example_yaml_config

    execution:
        algorithm: "dpo"
        venv: "<path_to_your_venv>"
        output_dir: "<path_to_your_output_dir>"
        distributed_config: "DSZero3Offload"

    slurm:
        job-name: "<your_slurm_job_name>"
        # output: None
        # error: None
        nodes: 2
        cpus-per-task: 80
        gres: "gpu:4"
        time: "2:00:00"
        account: "bsc88"
        qos: "acc_debug"

    rl_script_args:
        dataset_name: "<path_to_rl_dataset>"

    model_config_args:
        model_name_or_path: "<path_to_model>"
        # output_dir: None
        attn_implementation: "flash_attention_2"
        torch_dtype: "bfloat16"

    rl_config_args:
        # RL configs are subclasses of transformers.TrainingArguments

        # Different RL algorithms have different uses of beta.
        # However, in most of them, it is the weight of the KL-divergence (Loss=reward+Beta*KL)
        beta: 0.2
        max_length: 8192
        max_prompt_length: 128 # Default. When specified, you use the default data collator
        remove_unused_columns: false
        dataset_num_proc: 1
        # ====
        # From `TrainingArguments`:
        # ===
        learning_rate: 5.0e-6
        num_train_epochs: 2
        bf16: true
        eval_strategy: "steps"
        eval_steps: 0.05

        # logging_dir: None
        # local_rank: None
        report_to: "wandb"
        # These arguments help to manage GPU memory
        per_device_train_batch_size: 2
        per_device_eval_batch_size: 2
        gradient_accumulation_steps: 8
        gradient_checkpointing: true

    environment:
        # Bash environment variables 
        WANDB_PROJECT: "salamandra_alignment"
        WANDB_NAME: "test_alignment"
        # WANDB_DIR: None

    # Evaluation is optional
    evaluation:
    "harness_tasks":
        - "flores_en-es"
        - "flores_es-ca"
        - "wnli_es"
        - "xlsum_es"
    "harness_slurm":
    # job name, logs, and gpus are automatically computed
        qos: "acc_bscls"
        account: "bsc88"
        nodes: 2
        time: "12:00:00"
        # job-name: None
        # output: None
        # error: None
        # cpus-per-task: None # 
        # gres : None  # "gpu:4"


----------------------
Running an experiment
----------------------

You can use your ``config.yaml`` file to run an experiment, using the :ref:`CLI <rl-salamandra-alignment.cli>`:

.. code-block:: console

    $ rl_salamandra_mn5 config.yaml

This will generate **and** submit slurm jobs to MareNostrum 5, you can find them in your ``output_dir``.

Debugging
==========

For debugging, use the ``--debug`` flag:

.. code-block:: console

    $ rl_salamandra_mn5 config.yaml --debug

In debugging mode, slurm scripts will be generated but not submitted.

Skipping evaluation
====================

If you only want to train but not evaluate nmodels, you can use the ``--no_evaluation`` flag

.. code-block:: console

    $ rl_salamandra_mn5 config.yaml --no_evaluation


This will create the training and evaluation jobs for slurm, but it will **only** submit the training jobs. This may be useful when the evaluation queue is long, or when you want to make a quick experiment.

---------------
Subexperiments
---------------

To experiment with different configurations of values, you can use **lists** in your `config.yaml` file.

For example, the following ``config.yaml`` for one experiment executes 12 subexperiments: 

- 6 runs of DPO: on 2 models with 3 learning rates, and
- 6 runs of KTO: on the same 2 models with the same 3 learning rates

Note that both hyphens (``-``) and square brackes (``[]``) work for writing lists in YAML.

.. code-block:: yaml
    :caption: Setting up subexperiments
    :name: example_subexperiments_config

    ...
    execution:
        algorithm: 
            - "dpo"
            - "kto"
    ...
    model_config_args:
        model_name_or_path: 
            - "model_1"
            - "model_2"
    ...
    rl_config_args:
        learning_rate: [5.0e-6, 1.0e-5, 1.0e-6]
    ...

Note that any of the values in the configuration can be a list, **except** ``output_dir`` under ``execution``. The ``output_dir`` must always be an absolute path. 

Furthermore, for a given configuration file, all subexperiments generated from it share the same ``evaluation`` field, which will **not** be unfolded. This means that you can specify lists inside the ``evaluation`` field (for example, lists of evaluation tasks), and doing so will not create more subexperiments. 