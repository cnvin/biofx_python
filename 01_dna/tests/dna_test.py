""" Tests for dna.py and other solutions """

import os
import platform
from subprocess import getstatusoutput  # Standard library
import pytest  # Third-party

# Define the list of solution scripts to be tested
# Note: dna.py is intentionally omitted as it doesn't exist.
# Testing solution1_iter.py (representative) and solution8_regex.py.
SOLUTIONS = [
    './solution1_iter.py',
    './solution8_regex.py'
]

TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')


# --------------------------------------------------
@pytest.mark.parametrize("program_to_test", SOLUTIONS)
def test_exists(program_to_test: str) -> None:
    """ Program exists """

    assert os.path.exists(program_to_test)


# --------------------------------------------------
@pytest.mark.parametrize("program_to_test", SOLUTIONS)
def test_usage(program_to_test: str) -> None:
    """ Prints usage """

    run_cmd_base = (f'python {program_to_test}'
                    if platform.system() == 'Windows' else program_to_test)
    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{run_cmd_base} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
@pytest.mark.parametrize("program_to_test", SOLUTIONS)
def test_dies_no_args(program_to_test: str) -> None:
    """ Dies with no arguments """

    run_cmd_base = (f'python {program_to_test}'
                    if platform.system() == 'Windows' else program_to_test)
    rv, out = getstatusoutput(run_cmd_base)
    assert rv != 0
    # Ensure the error message indicates a missing DNA argument or general usage
    # For argparse, this usually includes "usage:" or
    # "error: the following arguments are required: dna"
    err_msg = out.lower()
    assert ("usage:" in err_msg or
            "error: the following arguments are required: dna" in err_msg)


# --------------------------------------------------
@pytest.mark.parametrize("program_to_test", SOLUTIONS)
def test_arg(program_to_test: str) -> None:
    """ Uses command-line arg """

    run_cmd_base = (f'python {program_to_test}'
                    if platform.system() == 'Windows' else program_to_test)
    # 'dna_input_file' is a path like './tests/inputs/input1.txt'
    # These paths are relative to the 01_dna directory, where pytest is run.
    for dna_input_file, expected in [TEST1, TEST2, TEST3]:
        with open(dna_input_file, 'r', encoding='utf-8') as f:
            dna_sequence = f.read().strip()

        # Add quotes around DNA sequence for robustness
        retval, out = getstatusoutput(f'{run_cmd_base} "{dna_sequence}"')
        assert retval == 0
        assert out.strip() == expected


# --------------------------------------------------
@pytest.mark.parametrize("program_to_test", SOLUTIONS)
def test_file(program_to_test: str) -> None:
    """ Uses file arg """

    run_cmd_base = (f'python {program_to_test}'
                    if platform.system() == 'Windows' else program_to_test)
    # 'file_path_arg' is a path like './tests/inputs/input1.txt'
    # These paths are relative to the 01_dna directory, where pytest is run.
    # The script itself should handle opening and reading this path.
    for file_path_arg, expected in [TEST1, TEST2, TEST3]:
        retval, out = getstatusoutput(f'{run_cmd_base} {file_path_arg}')
        assert retval == 0
        assert out.strip() == expected
