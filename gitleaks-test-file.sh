#!/bin/bash

# ❌ Hardcoded secret (ERROR)
DB_PASSWORD="supersecret123"

# ❌ Insecure file permissions (ERROR)
echo "$DB_PASSWORD" > /tmp/db_pass.txt
chmod 777 /tmp/db_pass.txt  # Too permissive

# ❌ Command injection via unvalidated input (ERROR)
echo "Enter filename to delete:"
read filename
rm -rf "/home/user/$filename"  # Unsafe if $filename = "*/"

# ❌ Use of temporary file without mktemp (ERROR)
TMP_FILE="/tmp/mytempfile.txt"
echo "Sensitive data" > "$TMP_FILE"

# ❌ curl to HTTP endpoint without SSL (ERROR)
curl http://example.com/ap
