
from setuptools import setup, find_packages

setup(
    name='dcs_calc_preprocessing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here, for example:
        # 'numpy>=1.18.0',
    ],
    entry_points={
        'console_scripts': [
            'preprocess_dcs_calc=preprocess_dCScalc_file_names:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package for preprocessing dCS calc file names.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wkm200/module_repository',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
