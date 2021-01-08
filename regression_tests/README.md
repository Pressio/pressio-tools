
Guidelines to create a regression test:
1. create a subdirectory and name it properly:

	TBD

2. add a "test_<some_name>_main.py" inside the test directory.
You can have multiple mains but make sure you name them uniquely.
And make sure the file starts with "test_"

3. add other files needed for the test, e.g. inputs, basis files, etc

4. If you need to read/load auxiliary files within the test directory,
in your main.py you need to do like this:

  import pathlib, sys
  file_path = pathlib.Path(__file__).parent.absolute()
  ...
  ...
  mybasisFile = str(file_path) + "/basis_euler.txt")
  phi = np.loadtxt(mybasisFi


--------------------------------------------------------------
This is it! What happens then? Pytest takes care of the rest.