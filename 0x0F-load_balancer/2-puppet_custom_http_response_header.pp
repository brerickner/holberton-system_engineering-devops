#installing web-02 to be identical to web-01

exec { 'apt-get install nginx':
  command  => 'apt-get update',
  provider => '/usr/bin/bash',
}
->
package { 'nginx':
  ensure  => 'installed',
}
->
file { '/etc/nginx/sites-available/default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => 'add_header X-Served-By $hostname;',
}
->
service {'nginx':
  ensure => running,
}
