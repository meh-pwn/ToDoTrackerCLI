from setuptools import setup

setup(
    name="tasker",
    version="1.0.0",
    description="Console app for task manager",
    author="meh-pwn",
    author_email="andreeww027@gmail.com",
    url="https://github.com/meh-pwn/ToDoTrackerCLI.git",
    py_modules=["task_manager"],
    entry_points={
        "console_scripts": [
            "tasker=task_manager:main",
        ],
    },
    test_requires=[
        "pytest",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ]
)