# Sky is the limit, let's bring that limit higher

exec {'fix Web Server':
    command => "sed -i 's/15/1000/g' /etc/default/nginx",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec {'restart nginx web server':
    command => 'service nginx restart',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
