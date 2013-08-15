SECTIONS = ['global','defaults', 'listen', 'frontend', 'backend']
GLOBAL_PARAMS = ['ca-base', 'chroot','crt-base', 'daemon', 'gid', 
'group', 'log', 'log-send-hostname', 'nbproc', 'pidfile', 'uid', 
'ulimit-n', 'user', 'stats', 'node', 'description', 'unix-bind', 
'maxconn', 'maxconnrate', 'maxcomprate', 'maxcompcpuusage', 'maxpipes',
'maxsslconn', 'noepoll', 'nokqueue', 'nopol', 'nosplice', 'spread-checks',
'tune.bufsize', 'tune.chksize', 'tune.comp.maxlevel', 'tune.http.cookielen',
'tune.http.maxhdr', 'tune.maxaccept', 'tune.maxpollevents', 'tune.maxrewrite',
'tune.pipesize', 'tune.rcvbuf.client', 'tune.rcvbuf.server', 'tune.sndbuf.client',
'tune.sndbuf.server', 'tune.ssl.cachesize', 'tune.ssl.lifetime', 'tune.ssl.maxrecord',
'tune.zlib.memlevel', 'tune.zlib.windowsize', 'debug', 'quiet']