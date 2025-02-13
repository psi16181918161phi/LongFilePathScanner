import os
import sys
from LongFilePathScanner import scan_directory, print_results

def main():
    """
    Entry point of the application.
    Usage: python -m LongFilePathScanner <directory> [max_length]
    """
    if len(sys.argv) < 2:
        print("Usage: python -m LongFilePathScanner <directory> [max_length]")
        sys.exit(1)

    start_dir = sys.argv[1]
    max_length = 260
    if len(sys.argv) > 2:
        try:
            max_length = int(sys.argv[2])
        except ValueError:
            print("Invalid max_length specified, it must be an integer.")
            sys.exit(1)

    if not os.path.isdir(start_dir):
        print(f"Error: The directory '{start_dir}' does not exist or is not accessible.")
        sys.exit(1)

    long_files = scan_directory(start_dir, max_length)
    print_results(long_files)

if __name__ == '__main__':
    main()
