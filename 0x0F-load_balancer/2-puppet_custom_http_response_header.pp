#installing web-02 to be identical to web-01

package { 'nginx':
  ensure   => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "add_header X-Served-By ${hostname};",
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
