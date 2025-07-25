from setuptools import setup, find_packages

setup(
    name='unilog-enrichment',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'unilog-enrichment=main:main',
        ],
    },
    author='Fatwa Nugroho',
    author_email='youremail@example.com',
    description='Simple middleware enrichment tool for log pipeline (GeoIP & logtype tagging)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/username/unilog-enrichment',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    python_requires='>=3.7',
)