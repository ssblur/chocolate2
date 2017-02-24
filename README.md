# Chocolate Py 2
#### A sequel to the worst wiki ever

## Index
1. [Requirements](#requirements)
1. [Installation](#installation)
	1. [Optional Instructions](#optional)
	2. [Using Python with Apache](#python-and-apache)

## Requirements

Chocolate Py 2, by default, has two dependencies:
* Python 3.3+ - https://www.python.org
* Markdown for Python - https://pypi.python.org/pypi/Markdown

## Installation

Setup for this wiki software is simple.

1. Copy this repository onto your web server. You may or may not wish to use git.
1. If using the default 'parse' module, install Markdown for python.
	* If not using the default 'parse' module, this step is unnecessary.
1. Install Python, and set it up for your web server. [Instructions for Apache](#python-and-apache)
1. Add index.py as a valid index file 

### Optional

* Forbid everything except index.py from access using your preferred web server. (Recommended)

### Python and Apache

This is a simple tutorial to install Python with Apache. This tutorial will likely not work with other web servers.

#### Prerequisites:
* Python 3.3+
* Apache Web Server

#### Instructions

* Access your Apache config ( httpd.conf or apache2.conf, usually ), or site-specific config for the site you wish to use ( usually in /sites-available/\[sitename\].conf )
* Within your Apache config, search for the directory in which you will be installing Chocolate. It may look like this:
		```
		<Directory /var/www/>
			
			...
			
		</Directory>
		```
* Add a new line to this document. This line will allow CGI execution within the directory. The line should read:
		`Options +ExecCGI`
* Now that you have allowed script execution within the directory, you need to set .py files to be run as scripts. You need to find a line that reads something like the following:
		`AddHandler cgi-script .cgi .php`
* Add the text " .py" to the end of the line, as such:
		`AddHandler cgi-script .cgi .php .py`
* Now all there is left to do is add 'index.py' as a valid index file. This is simple enough to do, first, find a line which reads something like the following:
		`DirectoryIndex index.cgi index.html index.php`
* Now add " index.py" to the end, as such:
		`DirectoryIndex index.cgi index.html index.php index.py`
* That's all! Save the configuration file, then reload or restart your web server (on Linux "service apache2 reload").
