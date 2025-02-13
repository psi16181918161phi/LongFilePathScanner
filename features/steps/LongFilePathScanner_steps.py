

from behave import given, when, then

# add the /source directory to the path relative to here 
import sys
import os 
import pathlib
# Add the source directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

from LongFilePathScanner import LongFilePathScanner

@given("the scanner is initialized")
def step_impl_initialize_scanner(context):
    # Initialize the scanner object and any required state.
    context.scanner = None  # Replace with actual scanner initialization code
    print("Scanner initialized.")

@when("the scanner runs on the target directory")
def step_impl_scan_directory(context):
    # Execute the scanning logic on the target directory.
    # Replace the following line with the actual scanning implementation.
    context.scan_results = []  # Example: list of files with long paths
    print("Scanning the target directory.")

@then("the scanner reports all files with long paths")
def step_impl_report_long_paths(context):
    # Check the scan_results for files with long paths and report them.
    # Replace with the appropriate checking and reporting code.
    if context.scan_results:
        print("Found files with long paths:")
        for file in context.scan_results:
            print(file)
    else:
        print("No files with long paths found.")