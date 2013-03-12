Title: Git, Gitolite and Pelican
Slug: git-pelican
Tags: git, gitolite, pelican, python, make
Summary: The story of how to generate a static website with [Pelican](http://getpelican.com/) using [[Git](http://git-scm.org) and Gitolite

Firstly you need a server with Git and SSH.

Install Gitolite according to [Gitolite](https://github.com/sitaramc/gitolite#readme)
Add a repo, for example blog
on your local machine edit

gitolite-admin/conf/gitolite.conf and add

	repo blog
		RW+		=	"your username"


Add a post-receive hook to the blog repo
on the server log in as the git user and create a post-receive hook in the repo
~/repositories/blog.git/hooks/post-receive

	#!/bin/bash
	umask 0022

	TMP_DIR="$(mktemp -d)"
	git archive master | tar -C "${TMP_DIR}" -xf -

	source ~/.pelican/bin/activate
	echo "Rebuilding..."
	cd $TMP_DIR
	make html
	rm -rf "${TMP_DIR}"

make it executable and add permissions

	chmod a+xr ~/repositories/blog.git/hooks/post-receive


We will also make a virtualenv for pelican on the server

	virtualenv2 ~/.pelican
	source ~/.pelican/bin/activate
	pip install pelican markdown pygments


Now switch over to your local machine and clone the blog repo

	git clone git@host:/blog

Start your pelican project in the blog folder, the pelican-quickstart does well.
We will use the Makefile in the blog repo that generates the site with Pelican
You should only have to edit the OUTPUTDIR to the location where Your blog will be served from.
ex OUTPUTDIR=/home/srv/http

On your local machine again you can now edit pelicanconf.py to your needs and add all your pages.
When you are ready, add the pages, commit and push

	git add content/*
	git commit -m "Explaining commit message" -a
	git push

Now the site should be visible somewhere if you have a webserver setup

