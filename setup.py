from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f: 
    long_description = f.read()

setup(
    name                = 'notionist',
    version             = '0.1', 
    long_description    = long_description, 
    long_description_content_type = 'text/markdown', 
    description         = 'Life is divided into before and after meeting Notion', 
    author              = 'Jaehuck Heo', 
    author_email        = 'wogur379@gmail.com', 
    url                 = 'https://github.com/TooTouch/notionist', 
    download_url        = 'https://github.com/TooTouch/notionist/archive/v0.1.tar.gz', # release 이름
    install_requires    =  ["notion"], 
    packages            = find_packages(exclude = []),
    keywords            = ['notion'], 
    python_requires     = '>=3.6', 
    package_data        = {}, 
    zip_safe            = False,
    classifiers         = [   
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)