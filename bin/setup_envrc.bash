#!/usr/bin/env bash
# encoding: utf-8

set -euo pipefail

SCRIPT_DIR="$(dirname "$0")"

cd "${SCRIPT_DIR}"

ENV_FILE=../.envrc

function get_data_zip_password() {
  read -r -s -p "Please paste the password for the zip file: " response
  echo "${response}" | tr -d '[:space:]'
}

function save_value_to_envrc() {
  key=$1
  value=$2
  echo "${key}=${value}" >> "${ENV_FILE}"
}

save_value_to_envrc "DATA_ZIP_PASSWORD" "$(get_data_zip_password)"
