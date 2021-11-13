import os


def clear():
    """Clear the console"""
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        # If OS is macOS or Linux
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')
