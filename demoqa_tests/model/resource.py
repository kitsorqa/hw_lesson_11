import os
import demoqa_tests.tests


def file_path(file_name):
    return os.path.abspath(
        os.path.join(
            os.path.dirname(demoqa_tests.tests.__file__), f'../data/imgs/{file_name}'
        )
    )