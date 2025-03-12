from pytest_pyodide import run_in_pyodide


@run_in_pyodide(packages=["python-docx"])
def test_regex(selenium):
    import docx

    print(docx.__version__)
