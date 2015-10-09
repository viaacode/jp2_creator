from setuptools import setup

setup(name='jp2worker',
      version='0.1',
      description='VIAA tiff to jp2 convertor.',
      long_description='Tiff to jp2 convertor based on RabbitMQ messages.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: © 2015 VIAA',
        'Programming Language :: Python :: 3.4',
        'Topic :: Image Converting',
      ],
      keywords='tiff rabbit jp2 worker',
      author='Jonas Liekens',
      author_email='jonas.liekens@c4j.be',
      license='© 2015 VIAA',
      packages=['jp2worker'],
      install_requires=[
          'pika',
          'wand',
      ],
      entry_points={
          'console_scripts': ['jp2worker=jp2worker.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
