## WebIOPi사용하기 ##

#### wget [http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz](http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz "http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz") 

#### wget [https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch](https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch "https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch")


## Bluetooh ##

#### sudo nano /etc/systemd/system/dbus-org.bluez.service 

#### git clone [https://github.com/karulis/pybluez.git](https://github.com/karulis/pybluez.git "https://github.com/karulis/pybluez.git") 



## OpenCV ##
### 설치 
#### git clone [https://github.com/dltpdn/opencv-for-rpi.git](https://github.com/dltpdn/opencv-for-rpi.git "https://github.com/dltpdn/opencv-for-rpi.git")  


## LAMP 설치 ##
### Apache 설치 ###
#### sudo apt install apache2 –y 
#### sudo chown -R pi:www-data /var/www/html/  
#### sudo chmod -R 770 /var/www/html/ 

#### sudo service apache2 stop 
#### sudo service apache2 start 

#### sudo mv index.html index.html.bak 
#### sudo nano index.html 

### PHP 설치
#### sudo apt install php php-mbstring  
#### sudo rm /var/www/html/index.html 
#### echo "<?php phpinfo ();?>" > /var/www/html/index.php 

### MySQL
#### sudo apt install mysql-server mysql-client php-mysql 
#### sudo mysql –u root –p 
#### <패스워드는 그냥 Enter> 
#### use mysql #### 

####  describe user; //테이블 구조 표시 

#### UPDATE mysql.user SET authentication_string=PASSWORD('root') WHERE user='root';   

#### flush privileges;
#### quit  

###사용자 추가
#### create user 'pi' identified by 'raspberry'; 
#### select user, password from user; 

#### grant all privileges on *.* to 'pi'; 
#### quit 

####  sudo mysql –u pi –p raspberry 

### Apche2 설정
#### sudo nano /etc/apache2/apache2.conf 

<맨 끝줄에>
####  Include /etc/phpmyadmin/apache.conf 
<저장>

#### sudo service apache2 restart


### root 권한으로 로그인 
#### sudo mysql –u root –p 
#### select user, plugin from useer; 

#### UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root'; 

#### FLUSH PRIVILEGES;  


###워드프레스 설치
#### cd /var/www/html/
#### sudo rm * 
#### sudo wget [http://wordpress.org/latest.tar.gz](http://wordpress.org/latest.tar.gz  "http://wordpress.org/latest.tar.gz") 
#### sudo tar xzf latest.tar.gz 
#### sudo mv wordpress/* . 
#### sudo rm -rf wordpress latest.tar.gz 

<설치후>

#### sudo chown -R www-data: . 

