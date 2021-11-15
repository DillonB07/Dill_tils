import os


def clear():
    """Clear the console"""
    # Check if Operating System is Mac and Linux or Windows
    try:
        if os.name == 'posix':
            # If OS is macOS or Linux
            _ = os.system('clear')
        elif os.name == 'nt':
            # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')
        return True

    except Exception as e:
        print(e)
        return False
