### Setup the boilerplate

Just run `setup.sh` to setup the boilerplate.

 The `run_scripts` directory contains the scripts that should be run for build and debugging. The most recent run will be logged in `telemetry_logs`directory. In that directory a file named `index.csv` will be generated, which is for the server's use. The `old_telemetry_logs` directory contains older telemetry logs which are shifted automatically upon every build.

The `helpers` directory contains helper functions for logging and other use cases. The `debug_logs`directory contains debugging logs (not ML telemetry data) The `.vscode` directory contains settings for configuration of buttons for build and debugging.


config.toml -> Contains configuration parameters (file paths, telemetry intervals etc)
hyperparameters.toml -> Contains hyperparameters

We will now be using miniconda instead of pip. It is much better suited for data science. Morever it is supported by HPC clusters where pip fails. The conda environment will be named `venv` and will go in folder named `.\venv` at the root. (The folder will be gitignored) Instead of `requirements.txt` file, we have `environment.yml` file.



## Adding a new package

The usual Conda workflow is:

### 1. Edit `environment.yml`

Add the package to the appropriate section.

For a Conda package:

```yaml
dependencies:
  - python=3.13
  - pytorch
  - pandas
  - numpy
  - pip
```

For a pip package:

```yaml
dependencies:
  - python=3.13
  - pip

  - pip:
      - petname
      - loguru
      - requests
```

### 2. Update the existing environment

```bash id="kttbop"
conda env update -p ./venv -f setup/environment.yml
```

Conda will install any missing packages.

### 3. Manual installation  
If you install packages interactively, example

```bash id="b2n3xg"
conda activate ./venv
conda install pandas
```

your `environment.yml` won't update automatically. You'll need to either:

* manually edit the YAML, or
* export the environment again:

```bash id="pmh4n4"
conda env export -p ./venv > environment.yml
```

Be careful: the exported file can become very large and include exact build versions.

### Recommended for projects

Treat `environment.yml` as the source of truth:

1. Edit `environment.yml`
2. Run:

```bash id="lk1c4v"
conda env update -p ./venv -f setup/environment.yml
```

3. Commit the YAML to version control

For your project, I'd structure it like:

```yaml
name: venv

channels:
  - pytorch
  - conda-forge

dependencies:
  - python=3.13
  - pytorch
  - torchvision
  - torchaudio
  - matplotlib
  - numpy
  - pip
  - pip:
      - petname
      - loguru
```

and whenever you need a new dependency, add it to the YAML and run:

```bash id="9u7w5w"
conda env update -p ./venv -f setup/environment.yml
```

This keeps everyone's environment reproducible.
