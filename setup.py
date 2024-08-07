from setuptools import setup, find_packages

setup(
    name='tfq-finance',
    version='1.0.2',
    description='A quantum machine learning library for quantitative finance built on top of TensorFlow Quantum',
    author='jialuechen',
    author_email='jialuechen@outlook.com',
    url='https://github.com/jialuechen/tfq-finance',
    packages=find_packages(),
    install_requires=[
        'tensorflow==2.11.0',
        'tensorflow-quantum',
        'cirq',
        'numpy',
        'sympy',
        'scipy',
        'pandas',
        'matplotlib',
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)