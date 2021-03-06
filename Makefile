all : templates client-devel
production :  templates client-production
.PHONY: templates all client-devel client-production devel-server production
templates :
	find ./templates -name "*.tmpl" -exec sh -c 'T=$$(echo {}); T=$${T#./templates/}; cheetah compile --nobackup --odir cmpltmpl --idir templates "$$T"' \;
client-production :
	webpack-cli --config webpack.prod.js
client-devel :
	webpack-cli --config webpack.dev.js
devel-server :
	webpack-dev-server --config webpack.dev.js
