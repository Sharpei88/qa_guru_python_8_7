import os

current_file = os.path.abspath(__file__)
print(current_file)
project_root_dir = os.path.dirname(current_file)
print(project_root_dir)

join = os.path.join(project_root_dir, 'tmp', '../new', 'new')
print(join)
print(os.path.getsize("../resources/hello.zip"))
import shutil

shutil.rmtree('tmp', ignore_errors=True)
