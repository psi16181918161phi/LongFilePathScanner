Feature: Long File Path Scanner

    As a user
    I want to scan directories for file paths that exceed a specified maximum length
    So that I can identify files with potentially problematic long paths

    Scenario: Detect long file paths in a directory
        Given a directory "C:/TestDirectory" with the following files:
            | filename             | full_path                                        |
            | "short.txt"          | "C:/TestDirectory/short.txt"                     |
            | "very_long_file.txt" | "C:/TestDirectory/SubDir/very_long_file.txt"     |
        When the LongFilePathScanner runs with a maximum allowed length of 50 characters
        Then the output should include the following file path:
            | full_path                                        |
            | "C:/TestDirectory/SubDir/very_long_file.txt"     |

    Scenario: No long file paths found in the directory
        Given a directory "C:/TestDirectory" with files that all have paths shorter than the maximum allowed length
        When the LongFilePathScanner runs with a maximum allowed length of 100 characters
        Then the output should indicate that no long file paths were found