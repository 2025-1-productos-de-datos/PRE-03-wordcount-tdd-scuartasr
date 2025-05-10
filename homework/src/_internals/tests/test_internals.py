import subprocess
import sys

from ...wordcount import parse_args, read_all_lines


def test_parse_args():

    # Llamada en el prompt:
    #
    #   $ python3 -m homework data/input/ data/output/
    #
    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == test_args[1]
    assert output_folder == test_args[2]


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )
