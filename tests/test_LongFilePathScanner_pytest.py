import os
import pytest
import sys
import pathlib

# read the location of the LongFilePathScanner.py relative from here 

# Add the source directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
    
from LongFilePathScanner import find_long_file_paths
def test_no_long_files(tmp_path):
    # Create a file with a short path.
    file = tmp_path / "short.txt"
    file.write_text("content")
    result = scan_directory(str(tmp_path), max_length=30)
    # Expect no file path longer than 30 characters.
    assert result == []

def test_long_file_detected(tmp_path):
    # Create a file with a long name.
    long_name = "a" * 40 + ".txt"
    file = tmp_path / long_name
    file.write_text("content")
    result = scan_directory(str(tmp_path), max_length=30)
    expected = str(file)
    assert expected in result

def test_multiple_files(tmp_path):
    # Create a mix of short and long files.
    short_file = tmp_path / "short.txt"
    short_file.write_text("hello")
    long_file = tmp_path / ("b" * 35 + ".txt")
    long_file.write_text("world")
    result = scan_directory(str(tmp_path), max_length=30)
    assert str(long_file) in result
    assert str(short_file) not in result

def test_recursive_scan(tmp_path):
    # Create a nested structure with files.
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()
    long_file = sub_dir / ("c" * 31 + ".log")
    long_file.write_text("data")
    short_file = sub_dir / "file.log"
    short_file.write_text("data")
    result = scan_directory(str(tmp_path), max_length=30)
    assert str(long_file) in result
    assert str(short_file) not in result

def test_equal_length_file(tmp_path):
    # When the file path is exactly the threshold, assume it should not be flagged.
    file = tmp_path / ("d" * 20 + ".txt")
    file.write_text("data")
    threshold = len(str(file))
    result = scan_directory(str(tmp_path), max_length=threshold)
    assert str(file) not in result

def test_nonexistent_directory():
    # Passing a nonexistent directory should raise an exception.
    with pytest.raises(Exception):
        scan_directory("/path/that/does/not/exist", max_length=10)