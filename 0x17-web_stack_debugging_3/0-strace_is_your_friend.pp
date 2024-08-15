# Fixes Apache 500 error by correcting the 'phpp' typo in wp-settings.php if the file exists

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin:/usr/local/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
