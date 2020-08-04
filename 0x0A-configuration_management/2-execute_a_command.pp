# Manifest that kills a process named killmenow.
exec { 'pkill':
    command => 'pkill killmenow',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  }
