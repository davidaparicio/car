#!/usr/bin/env bash
# Why is #!/usr/bin/env bash superior to #!/bin/bash? https://stackoverflow.com/q/21612980

# Enable alias expansion
# shopt -s expand_aliases

# USE BASH STRICT MODE - http://www.redsymbol.net/articles/unofficial-bash-strict-mode/
# set -euo pipefail
# IFS=$'\n\t'

alias venv="if [ -e ./.venv/bin/activate ]; then source ./.venv/bin/activate; else python3 -m venv .venv && source ./.venv/bin/activate; fi"
venv
pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev-requirements.txt
# pip freeze > full_requirements.txt

if command -v pre-commit >/dev/null 2>&1
then
  echo -e "pre-commit already present. \t Installation skipped..."
  # pre-commit install && pre-commit autoupdate && pre-commit run -a
else
  echo "Installing the latest pre-commit version for Python3 into a venv.." && \
  echo "(venv == a virtual Python3 environment dedicated for this project)." && \
  pip3 install pre-commit && \
  echo "Installing the git hook scripts.." && \
  pre-commit install && \
  echo "Run against all the files.." && \
  pre-commit autoupdate && \
  pre-commit run -a
  # https://github.com/antonbabenko/pre-commit-terraform
  # https://www.unixdaemon.net/cloud/preventing-aws-creds-in-git-with-pre-commit/
fi
