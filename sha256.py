import hashlib
import argparse

# Define the function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main function to handle command-line arguments
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Hash a password using SHA-256')
    parser.add_argument('password', type=str, help='Password to be hashed')

    # Parse arguments
    args = parser.parse_args()

    # Call the hash_password function
    hashed_password = hash_password(args.password)

    # Output the hashed password
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    main()
