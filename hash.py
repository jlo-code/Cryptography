import hashlib
import argparse
import ctypes
import gc
import getpass

# Define the function to hash the input using the specified algorithm
def hash_string(string_bytes, algorithm):
    try:
        # Get the corresponding hash function dynamically
        hash_func = getattr(hashlib, algorithm)
        # Return the hexadecimal digest of the hash
        return hash_func(string_bytes).hexdigest()
    except AttributeError:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

# Function to securely overwrite memory of sensitive data
def clear_memory(data):
    """
    Overwrite the memory of a bytearray to clear sensitive data.
    """
    if isinstance(data, bytearray):
        for i in range(len(data)):
            data[i] = 0

# Main function to handle command-line arguments
def main():
    # Supported hashing algorithms
    supported_algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Hash a string using different cryptographic algorithms.")
    
    # Argument for selecting the algorithm
    parser.add_argument(
        '-a', '--algorithm',
        type=str,
        choices=supported_algorithms,
        default='sha256',
        help=f"Choose the hash algorithm (default: sha256). Supported algorithms: {', '.join(supported_algorithms)}"
    )
    
    # Argument for the string to hash
    parser.add_argument(
        'string', 
        type=str, 
        help="The string to hash"
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the string to a bytearray for mutable memory handling
    input_bytes = bytearray(args.string.encode('utf-8'))

    # Call the hash_string function
    hashed_string = hash_string(input_bytes, args.algorithm)

    # Output the result
    print(f"Algorithm: {args.algorithm}")
    print(f"Original String: {args.string}")
    print(f"Hashed String: {hashed_string}")

    # Clear the sensitive input from memory
    clear_memory(input_bytes)
    args.string = None

    # Force garbage collection to free memory
    gc.collect()

if __name__ == "__main__":
    main()
