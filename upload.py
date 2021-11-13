import os

TWINE_USERNAME = os.environ['TWINE_USERNAME']
TWINE_PASSWORD = os.environ['TWINE_PASSWORD']

print('Building package')
print('--------------------------------')
print(os.system("python setup.py sdist bdist_wheel"))
print('--------------------------------')
print('Uploading package')
print(
    os.system(f"twine upload dist/* -u {TWINE_USERNAME} -p {TWINE_PASSWORD}"))
print('--------------------------------')
print('Uploaded package to PyPi')
