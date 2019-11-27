#!/usr/bin/env bash

PYTHON=python3
DIST_DIR=dist
TMP_VENV_DIR=tmp

mkdir -p cache
curl -L -o cache/assert.tar.gz https://github.com/yosugi/assert.bash/archive/v0.3.0.tar.gz
(cd cache && tar xf assert.tar.gz)
source cache/assert.bash-0.3.0/assert.bash

# package find
NUM=`ls dist/*.tar.gz | wc -l`
assert ${NUM} -eq 1

NUM=`ls dist/*.whl | wc -l`
assert ${NUM} -eq 1

# create venv
${PYTHON} -m venv ${TMP_VENV_DIR}
${TMP_VENV_DIR}/bin/python -m pip install -U setuptools wheel pip

# install
${TMP_VENV_DIR}/bin/python -m pip install ${DIST_DIR}/*.whl


# clean
rm -rf ${TMP_VENV_DIR} cache
