import subprocess

def create_user_account(username, password):
    # Follow best practice #1: Use a strong password
    if not is_strong_password(password):
        raise ValueError("Password is not strong enough")

    # Follow best practice #2: Do not use default or easily guessable user names
    if is_default_username(username) or is_guessable_username(username):
        raise ValueError("Invalid username")

    # Follow best practice #3: Use separate accounts for different functions
    if is_admin_account(username):
        raise ValueError("Admin accounts should not be used for daily tasks")

    # Follow best practice #4: Enable multi-factor authentication
    enable_mfa(username)

    # Follow best practice #5: Use account-level access controls
    set_access_controls(username)

    # Create the user account
    subprocess.run(["useradd", "-m", "-p", password, username])

def is_strong_password(password):
    # Implement password strength checker
    pass

def is_default_username(username):
    # Check if username is a default system username
    pass

def is_guessable_username(username):
    # Check if username is easily guessable
    pass

def is_admin_account(username):
    # Check if username is an admin account
    pass

def enable_mfa(username):
    # Enable multi-factor authentication for the given user
    pass

def set_access_controls(username):
    # Set appropriate access controls for the given user
    pass
