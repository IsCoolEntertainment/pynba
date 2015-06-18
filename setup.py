from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.5.0'

install_requires = [
    'pynba>=0.5.0',
    'six'
]

setup(
    name='iscool_e.pynba',
    version=version,
    description=str(
        'lightweight timers and wsgi middleware to '
        'monitor performance in production systems'
    ),
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities"
    ],
    keywords='pinba wsgi monitoring',
    author='Xavier Barbosa',
    author_email='xavier.barbosa@iscool-e.com',
    url='https://github.com/IsCoolEntertainment/pynba',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['iscool_e'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
)
