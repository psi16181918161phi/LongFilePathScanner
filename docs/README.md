# Long File Path Scanner

A simple tool for scanning directories to find files with long file paths.

## Features

- Recursively scans directories.
- Detects files exceeding a specified path length.
- Generates a report of findings.

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/psi16181918161phi/LongFilePathScanner.git
    ```
2. Navigate into the project directory:
    ```
    cd LongFilePathScanner
    ```
3. Follow the additional setup instructions provided in the documentation.

## Usage

Run the scanner by executing the following command:
```
python scanner.py --path /path/to/your/directory --limit 260
```

Customize the parameters as necessary:
- `--path`: The target directory to scan.
- `--limit`: The file path length limit.

## Contributing

Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.