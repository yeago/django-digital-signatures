from setuptools import setup, find_packages

f = open('README')
readme = f.read()
f.close()

setup(
    name='django-digital-signature',
    version='0.0',
    description='Handles digital signatures of generic things',
    author='Steve Yeago',
    author_email='subsume@gmail.com',
    url='http://github.com/riltsken/django-digital-signatures/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
