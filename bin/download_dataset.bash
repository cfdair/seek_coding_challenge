#!/usr/bin/env bash
# encoding: utf-8

set -euo pipefail

SCRIPT_DIR="$(dirname "$0")"

DATA_DIR="../data"
DATA_ZIP_PATH="${DATA_DIR}/test-data.zip"

cd "${SCRIPT_DIR}"

command -v curl >/dev/null 2>&1 || { echo >&2 "Please install curl. Aborting."; exit 72; }
command -v unzip >/dev/null 2>&1 || { echo >&2 "Please install unzip. Aborting."; exit 72; }

test -z ${DATA_ZIP_PASSWORD+y} && { echo >&2 "The envvar DATA_ZIP_PASSWORD wasn't set. It should be. Aborting."; exit 1; }

function download_dataset() {
  mkdir -p "${DATA_DIR}"
  wget \
  -O "${DATA_ZIP_PATH}" \
    https://coding-challenge-public.s3.ap-southeast-2.amazonaws.com/test-data.zip
}

function unzip_dataset() {
  unzip \
    -P "${DATA_ZIP_PASSWORD}" \
    -d "${DATA_DIR}" \
    "${DATA_ZIP_PATH}"
}

echo "Downloading dataset for the coding challenge..."
download_dataset
echo "Unzipping the zip file..."
unzip_dataset
echo "Done."
