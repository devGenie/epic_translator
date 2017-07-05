from setuptools import setup
"""
	This packages the cmd app so that it can be easily installed on a user's maschine
	To install Epic Translator, on the commandline type :-
		python setupe.py install
"""

#specifying dependencies
dependencies=['docopt']

setup(
		name="Epic Translator",
		version="o.0.1",
		author="Onen Julius",
		author_email="jonen54@gmail.com",
		description="Epic translator helps you translate any test to any language",
		"url"="https://github.com/devGenie/epic_translator",
		install_requires=dependencies,
		packages=["app"],
		entry_points={
			"console_scripts":["epictranslator=app.main.start"]
		}
	)