#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# TODO: package for MacOS

"""

 Usage (Mac OS X):
     python setup.py py2app

 Usage (Windows):
     python setup.py py2exe

"""


from setuptools import setup, find_packages
import glob

try:
	import py2app  ## for MAC package
except ImportError:
	pass

try:
	import py2exe  ## to generate an exe file
except:
	pass



setup( 
	name = "alfanousDesktop",
	description = "Desktop interface for alfanous Quranic search engine API",
	version = "0.7.00", # Don't modify version here, modify it in Makefile
	platforms = "ALL",
	license = "AGPL",
	packages = ["alfanousDesktop"],
	install_requires = ['alfanous', 'configobj', 'pyparsing',"jinja2","pyside"],
	author = "Assem Chelli",
	author_email = "assem.ch@gmail.com",
	maintainer = "Assem Chelli",
	maintainer_email = "assem.ch@gmail.com",

	package_dir = {'alfanousDesktop':'.'},
	long_description = """A desktop GUI interface for alfanous Quran search engine API""",
	keywords = "quran search indexing engine alfanous",
	url = "http://www.alfanous.org/",
	download_url = "",


  	package_data = {'alfanousDesktop': ['UI/*.ui', 'templates/*.html', 'babel.ini', 'locale/*/LC_MESSAGES/*', 'i18n/*', '*.pro']},
	include_package_data = True,


	entry_points = { 'gui_scripts': ['alfanous-desktop = alfanousDesktop.Gui:main', ]},


	## WINDOWS	
	 windows = [{
			"script": "../../resources/launchers/alfanousDesktop-win.py",
			"icon_resources": [( 1, "../../resources/Alfanous.ico" )]
		}],

	#tested: freezing works, but the folder templates should moved manually
	# There is a bug when executing the app
	## MAC
	app=["Gui.py"],

	options = {
			"py2exe" : {
					"includes" : ["sip","jinja2.ext"],
					"optimize":2,
					"skip_archive":True
				    },
			"py2app":{'argv_emulation': True}
			},

	classifiers = [
	"Development Status :: 4 - Beta",
	"Intended Audience :: Religion",
	"License :: OSI Approved :: GNU General Public License (GPL)",
	"Natural Language :: Arabic",
	"Natural Language :: English",
	"Operating System :: OS Independent",
	"Programming Language :: Python :: 2.6",
	]
 )
