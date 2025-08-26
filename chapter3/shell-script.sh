#Install Apache
yum install -y --quiet httpd http-devel
# Copy config in place
cp httpd.conf /etc/httpd/conf/httpd.conf
cd httpd-vhosts /etc/httpd/conf/httpd-vhosts.conf

#Start Apache and config it to run automatically on boot
systemctl start httpd
chkconfig httpd on