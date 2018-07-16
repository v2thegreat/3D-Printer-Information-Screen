from setuptools import setup, find_packages

setup(name='printer_que',
	version='0.5',
	description='A dependency for milkCan to enable it to run speed tests',
	url='https://github.com/v2thegreat/Concordia-Technology-Sandbox-3D-Printing-Queing-Software',
	author='v2thegreat',
	author_email='v2thegreat@gmail.com',
	license='MIT',
	packages=['printer_que'],
	zip_safe=False,
	install_requires=['PyQt5'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
	)
