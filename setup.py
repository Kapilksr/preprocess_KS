import setuptools

with open('README.md','r') as file:
	long_description=file.read()


setuptools.setup(
	name='preprocess_KS', ## this should be unique
	version='0.1',
	author='Kapil Singh',
	author_email='kapilsingh236142@gmail.com',
	description='This is text preprocessing tool',
	Long_description=long_description,
	Long_description_content_type='text/markdown',
	packages=setuptools.find_packages,
	classifiers=[
	'programming language :: Python :: 3',
	'License type :: OSI approved :: MIT License',
	'Operating System :: OS Independent'],
	python_requires='>=3.5'

	)