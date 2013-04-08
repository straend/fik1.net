Title: Cheating SVT
Tags: svt, privoxy
Slug: svt-play
Summary: How to watch SVT outside of Sweden

Since [SVT](http://svt.se) decided to stream live television and publish almost all of its contents on [SVTPlay](http://svtplay.se) i thought it would be nice to watch them. But since I'm in Finland [SVT](http://svt.se) wont allow me to watch everything.

#####So what to do?
*	Get a VPS in Sweden, Check out [EDIS](http://www.edis.at/en/server/linux-vserver/sweden/) they have great prices. And remember to check for deals at [LowEndBox](http://www.lowendbox.com/tag/sweden/)
*	Instead	of tunneling all Your traffic through the little box I use [Privoxy](http://privoxy.org)

#####How to do it
Setup Your new/old VPS with ssh access. Keybased login, becouse we are alla lazy(specially me, so [DuckDuckGo](https://duckduckgo.com/?q=keybased+ssh+login+) it)
Launch a ssh connection to your server with Dynamic portforwarding
This will tunnel traffic from port 9090 on localhost to your server, it functions like a socks proxy
	ssh user@your.swedish.server -D 9090

If you then put localhost and port 9090 as a socks proxy in your browser of choice, you could watch everything on SVTPlay, but all othter traffic would also be tunneled through your server.

So we install Privoxy and configure it to send only specific traffic through the server.
Minimal Privoxy config stolen from [Tor Wiki](https://trac.torproject.org/projects/tor/wiki/doc/PrivoxyConfig) and modified.
Remember to change the portnumber

	# Generally, this file goes in /etc/privoxy/config
	#
	# SVTPlay forwards
	forward-socks4a .akamai.net/            127.0.0.1:9090 .
	forward-socks4a .akamaitech.net/        127.0.0.1:9090 .
	forward-socks4a .akamaihd.net/          127.0.0.1:9090 .
	forward-socks4a .svt.se/                127.0.0.1:9090 .
	forward-socks4a .svtplay.se/            127.0.0.1:9090 .
	forward-socks4a .omtrdc.net/            127.0.0.1:9090 .
	forward-socks4a .edgesuite.net/         127.0.0.1:9090 .
	# End SVTPlay

	confdir /etc/privoxy
	logdir /var/log/privoxy
	# actionsfile standard  # Internal purpose, recommended
	actionsfile default.action   # Main actions file
	actionsfile user.action      # User customizations
	filterfile default.filter

	# Don't log interesting things, only startup messages, warnings and errors
	logfile logfile
	#jarfile jarfile
	#debug   0    # show each GET/POST/CONNECT request
	debug   4096 # Startup banner and warnings
	debug   8192 # Errors - *we highly recommended enabling this*

	# Listen on all interfaces
	listen-address  0.0.0.0:8118
	toggle  1
	enable-remote-toggle 0
	enable-edit-actions 1
	enable-remote-http-toggle 1
	buffer-limit 4096

Thats it. Now start/restart Privoxy and change your proxyserver in the browser and You are good to go