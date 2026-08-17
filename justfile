set dotenv-load

alias install := bootstrap
alias i := bootstrap
alias b := build

VENV_DIR := ".venv"
PYTHON := if os_family() == "windows" {
  VENV_DIR + "/Scripts/python.exe"
} else {
  VENV_DIR + "/bin/python3"
}

bootstrap:
  if ! test -e {{ VENV_DIR }}; then python3 -m venv {{ VENV_DIR }}; fi
  {{ PYTHON }} -m pip install -e .

  cd client/ && pnpm install

build:
  # wip