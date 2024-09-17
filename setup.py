from setuptools import setup, find_packages

setup(
    name='catbox_uploader',
    version='2.9',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['requests'],
    author='viendi',
    author_email='viendii@gmail.com',
    description='A simple Python library to upload files and URLs to Catbox.moe',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lunaticsm/catbox-uploader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
