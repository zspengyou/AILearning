from pathlib import Path
import os

print(os.name)
p = Path(__file__).with_name('__init__.py')
print(str(p))
print(p.name)

