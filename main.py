# ❌ Insecure function usage
user_input = input("Enter command: ")
eval(user_input)

# ❌ Hardcoded credentials
password = "superSecret123"

# ❌ Unsafe system call
import os
os.system("rm -rf /")
