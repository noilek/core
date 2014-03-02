#!/usr/bin/env python

import sys, os
from setuptools import setup, find_packages

setup(
        name = "Brave Core Services",
        version = "0.1",
        description = "EVE Online authentication, authorization, and API proxy service.",
        author = "Alice Bevan-McGregor",
        author_email = "alice@gothcandy.com",
        license = "MIT",
        
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        paster_plugins = ['PasteScript', 'WebCore'],
        namespace_packages = ['brave'],
        
        tests_require = ['nose', 'webtest', 'coverage'],
        test_suite = 'nose.collector',
        
        install_requires = [
                'WebCore>=1.1.2',
                'MongoEngine>=0.7.999',
                'Mako>=0.4.1',
                'beaker>=1.5',
                'requests==1.1.0',
                'blinker',
                'pyyaml',
                'ecdsa',
                'relaxml',
                'ipython',
                'scrypt',
                'pudb',
                'webassets',
                'babel',
                'marrow.mailer',
                'yubico',
                'futures',
            ],
        
    )
