from setuptools import setup

install_requires = [
  'lz4==3.1.0',
  'pydub==0.24.1',
]

test_require = [
  'pytest==6.2.5',
]

extras_require = {
    'test': test_require,
}

def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(
  name='nxpy',
  version='0.0.1',
  author='Sebastian Dang',
  author_email='SebastianDang@users.noreply.github.com',
  description='A python Nx parser',
  long_description=long_description(),
  long_description_content_type='text/markdown',
  url = "https://github.com/SebastianDang/nxpy",
  packages=['nxpy'],
  install_requires=install_requires,
  extras_require=extras_require
)
