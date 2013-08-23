from setuptools import setup

setup(name='UsingSQLAlchemy', version='1.0',
      description='Code example demonstrating how to use SQLAlchemy in Python using Flask',
      author='L. Guruprasad', author_email='lgp171188@gmail.com',
      url='http://www.lguruprasad.in/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask', 'flask-sqlalchemy',
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
