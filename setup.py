import setuptools
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setuptools.setup(
  name='pdftotextsimple',
  version='0.0.2',
  description='a module that can convert pdf to text',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Tech-with-anmol/pdftotexthttps://github.com/Tech-with-anmol/pdftotextsimple',  
  author='Anmol.py',
  author_email='anmollklfh@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pdf', 
  packages=setuptools.find_packages(where="src"),
  install_requires=['PyPDF2'],
  package_dir={"":"src"},
  python_requires=">=3.6",
  py_modules=['main']
)