import unittest
import os
import tempfile
import shutil
import sys
import pathlib

# read the location of the LongFilePathScanner.py relative from here 

# Add the source directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
    
from LongFilePathScanner import find_long_file_paths

class TestLongFilePathScanner(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for each test.
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after each test.
        shutil.rmtree(self.test_dir)

    def test_no_long_paths(self):
        # Create a normal file and use a high threshold so none are marked as "long".
        file_path = os.path.join(self.test_dir, "testfile.txt")
        with open(file_path, "w") as f:
            f.write("Sample content")
        # Set max_length high enough that the file path is not considered long.
        long_files = find_long_file_paths(self.test_dir, max_length=500)
        self.assertEqual(long_files, [])

    def test_single_long_path(self):
        # Create a deeply nested directory to force a long file path.
        # Each segment is 30 characters long.
        segment = "a" * 30
        nested_dir = os.path.join(self.test_dir, segment, segment, segment)
        os.makedirs(nested_dir)
        file_path = os.path.join(nested_dir, "testfile.txt")
        with open(file_path, "w") as f:
            f.write("Sample content")
        # Lower threshold so that the long path is detected.
        long_files = find_long_file_paths(self.test_dir, max_length=100)
        self.assertIn(file_path, long_files)

    def test_multiple_long_paths(self):
        # Create several nested directories that produce long file paths.
        created_paths = []
        for i in range(3):
            nested_dir = self.test_dir
            # Vary the depth based on i; deeper structures yield longer paths.
            for j in range(4 + i):
                dir_name = "subdir_" + ("b" * (20 + i))
                nested_dir = os.path.join(nested_dir, dir_name)
                os.makedirs(nested_dir, exist_ok=True)
            file_path = os.path.join(nested_dir, f"file{i}.txt")
            with open(file_path, "w") as f:
                f.write("Content")
            created_paths.append(file_path)
        # Use a threshold that will pick up the long paths.
        found_long_files = find_long_file_paths(self.test_dir, max_length=150)
        for path in created_paths:
            self.assertIn(path, found_long_files)

    def test_exact_threshold(self):
        # Create a file whose path length is exactly the threshold.
        # Assuming that only file paths with a length greater than the threshold are considered long.
        base_path = self.test_dir
        file_name = "exact.txt"
        file_path = os.path.join(base_path, file_name)
        threshold = 200
        current_length = len(file_path)
        # Construct an additional directory name that brings the total length up
        # to exactly the threshold (file path length = directory + separator + file_name).
        additional_length = threshold - current_length
        if additional_length > len(os.sep):
            dirname = "x" * (additional_length - len(os.sep))
            new_dir = os.path.join(base_path, dirname)
            os.makedirs(new_dir)
            file_path = os.path.join(new_dir, file_name)
            with open(file_path, "w") as f:
                f.write("Content")
            found_long_files = find_long_file_paths(self.test_dir, max_length=threshold)
            # Expect that a file path equal to the threshold is not flagged as long.
            self.assertNotIn(file_path, found_long_files)
        else:
            self.skipTest("Threshold too small for this test.")

if __name__ == "__main__":
    unittest.main()