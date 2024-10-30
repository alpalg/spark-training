# spark-training
Personal Apache Spark training

# How to use
Create pyspark script in scripts folder
```bash
make submit S=<name-of-your-script-without-extension> # "base" is set by default
```

# Poetry
Poetry env is optional, execution would work without it, but it can be handy for code completion, highlights, etc.  


# uv setup
### uv installation for Linux/MacOS
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Autocompletion
```shell
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```
### Python install
```shell
uv python install 3.12
```

### Install requirements
```shell
uv sync
```