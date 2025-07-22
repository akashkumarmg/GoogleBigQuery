#!/bin/bash

# ❌ Hardcoded password: Semgrep rule sqli-hardcoded-password
export AWS_SECRET="AKIA123456789EXAMPLE"

# ❌ Insecure file permissions: Semgrep rule insecure-file-permissions
echo "$AWS_SECRET" > /tmp/aws_secret.txt
chmod 666 /tmp/aws_secret.txt

# ❌ Command injection via unvalidated argument: sqli-shell-injection
function delete_user(){
  USER_ID="$1"
  rm -rf "/var/data/users/$USER_ID"
}

# ❌ Unsafe temp file without mktemp: insecure-tempfile
LOG_FILE="/tmp/logfile"
echo "log entry" >> "$LOG_FILE"

# ❌ Insecure network call (HTTP, no TLS): insecure-curl-https
curl -X POST http://internal-api.local/upload -d "token=$AWS_SECRET"

# ❌ Dangerous eval on untrusted input: dangerous-eval
function run_calc(){
  read -p "Enter calc expr: " EXPR
  eval "echo $EXPR"
}

# ❌ Sourcing arbitrary script: insecure-source
read -p "Enter plugin name: " PLUGIN
source "./plugins/$PLUGIN"

# ❌ PATH injection: insecure-envvar
export PATH="./bin:$PATH"

# ❌ Use of uname without quotes: command-injection-risk
read -p "Enter host to check: " HOST
ping -c 1 $HOST

# ❌ Writing sensitive file to world-readable dir: insecure-file
echo "db_pass=TopSecret!" > ~/public/db.conf

# Run functions to simulate usage
delete_user "$1"
run_calc
