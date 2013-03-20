#pelican-purple
###A pelican theme

This is a theme for the [Pelican](http://getpelican.org) static site generator.

With social icons from [Font Awesome](http://fortawesome.github.com/Font-Awesome/)

And background from [Subtle Patterns](http://subtlepatterns.com/gradient-squares/)

Watch it in [Action](http://fik1.net/2013/12/this-is-a-theme-testing-post/)

This theme is capable of listing links to Social sites with the SOCIAL tuple in pelican.conf
There is also the possibility to add a hidden vCard in the source

	VCARD = True
	AUTHOR_ADDRESS = (
		('street-address', 	u'Street 13'),
		('postal-code', 	u'00890'),
		('locality', 		u'Helsinki'),
		('country-name', 	u'Finland'),
	)

Under the social list the users phonenumber and email will be printed if
AUTHOR_PHONE
AUTHOR_EMAIL
is set

Also implemented is the [Github Ribbon](https://github.com/blog/273-github-ribbons) if
GITHUB_URL is set

The [Pelican Latex Plugin](https://github.com/barrysteyn/pelican_plugin-latex) is supported
