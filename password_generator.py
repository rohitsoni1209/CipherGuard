from email.policy import default

from random_password_creator import Password
import argparse

args = argparse.ArgumentParser(
            "\n\033[1;34m"
            "╔═════════════════════════════════════════════════════════════╗\n"
            "║      Random Password Generator Tool by -- 'Rohit Soni'      ║\n"
            "║                     \033[1;32mBuilt with Python\033[1;34m                       ║\n"
            "╚═════════════════════════════════════════════════════════════╝\n\n"
            "\033[0m"
            "This tool helps you generate secure random passwords with customizable options.\n"
            "Choose character sets and length for your password according to your needs.\n\n"
            "\033[1;33m"
            "Usage:\n"
            "  -c, --charset  : Set the character sets for password generation\n"
            "  -l, --length   : Set the password length\n"
            "\033[0m"
            "\033[1;36m"
            "# Available Character Sets:\n"
            "  l   - Lowercase alphabets\n"
            "  u   - Uppercase alphabets\n"
            "  d   - Digits\n"
            "  s   - Special characters\n"
            "\033[0m"
            "\033[1;32m"
            "You can combine the above character sets for a customized password.\n\n"
            "# Default Values:\n"
            "  Charset : 'ldus' (all character sets)\n"
            "  Length  : 8 characters\n\n"
            "\033[0m"
            "\033[1;35m"
            "Example:\n"
            "  python generator.py -c ld -l 12  # Generates a 12-character password with lowercase letters and digits\n"
            "\033[0m"
            "\033[1;31m"
            "Stay Secure! 🔒\n"
            "\033[0m")

args.add_argument('-c','--charset', type = str, default='ldus')
args.add_argument('-l','--length', type = int, default=8)
options = args.parse_args()
print(options.charset)
print(options.length)

password = Password(options.charset, int(options.length))
password.set_the_charset()
password.generate_password()
print("The random password is: ", password.get_password())