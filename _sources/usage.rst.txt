=====
Usage
=====

After :doc:`installing <installation>`, you will be able to run RL experiments using the package.

Configuration file for Experiment
---------------------------------

First, you will need a configuration file in YAML for your experiment:

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


The values marked with ``None`` are computed internally by the package.


Subexperiments
--------------

To experiment with different configurations of values, you can use lists in your `config.yaml` file.

For example, the following ``config.yaml`` for one experiment executes 12 experiments: 

- 6 runs of DPO on 2 models with 3 learning rates, and
- other 6 runs for KTO

.. code-block:: yaml
    :caption: Setting up subexperiments
    :name: example_subexperiments_config

    ...
    execution:
        algorithm: ["dpo", "kto"]
    ...
    model_config_args:
        model_name_or_path: ["model_1", "model_2"]
    ...
    rl_config_args:
        learning_rate: [5.0e-6, 1.0e-5, 1.0e-6]
    ...

Note that any of the values can be a list, **except** ``output_dir`` under ``execution``. The ``output_dir`` must always be an absolute path. 

Generating Job scripts
----------------------

You can use your ``config.yaml`` file to run an experiment, using the :ref:`CLI <rl-salamandra-alignment.cli>`:

.. code-block:: console

    $ rl_salamandra_mn5 config.yaml

This will generate slurm jobs in your ``output_dir``, which you can submit to MareNostrum 5.

