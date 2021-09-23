


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firstapp",
    version="0.0.1",
    author="Vishakha Tyagi",
    author_email="vishakhatyagi109@gmail.com",
    description="My first webapp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vishakha2002/cc-task1",
    project_urls={
        "Bug Tracker": "https://github.com/Vishakha2002/cc-task1/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points={  # Optional
        'console_scripts': [
            'webapp=webapp:main',
        ],
    },
)