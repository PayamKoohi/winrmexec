from setuptools import setup, find_packages

setup(
    name='winrmexec',
    version='0.1.0',
    packages=find_packages(),
    scripts=['winrmexec.py'],
    install_requires=['pywinrm'],
    entry_points={
        'console_scripts': [
            'winrm-exec=winrmexec.main:main'
        ]
    },
    author='Payam Koohi',
    author_email='payam.koohii@gmail.com',
    description='A simple script to execute PowerShell commands on a remote machine via WinRM.',
    url='https://github.com/your-username/your-repo',
    license='MIT',
    python_requires='>=3.6'
)
