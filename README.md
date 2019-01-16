## RPi.GPIO 참고 사이트  ##
https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

## WebIOPi사용하기 ##
wget [http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz](http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz "http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz") <br/>
wget [https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch](https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch "https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch")


## Bluetooh ##
sudo nano /etc/systemd/system/dbus-org.bluez.service <br/>
git clone [https://github.com/karulis/pybluez.git](https://github.com/karulis/pybluez.git "https://github.com/karulis/pybluez.git") 



## OpenCV ##
git clone [https://github.com/dltpdn/opencv-for-rpi.git](https://github.com/dltpdn/opencv-for-rpi.git "https://github.com/dltpdn/opencv-for-rpi.git")  


## LAMP 설치 ##
### Apache 설치 ###
sudo apt install apache2 –y  <br/>
sudo chown -R pi:www-data /var/www/html/   <br/>
sudo chmod -R 770 /var/www/html/  <br/>
sudo service apache2 stop  <br/>
sudo service apache2 start  <br/>
sudo mv index.html index.html.bak  <br/>
sudo nano index.html  <br/>

### PHP 설치
sudo apt install php php-mbstring   <br/>
sudo rm /var/www/html/index.html  <br/>
echo "<?php phpinfo ();?>" > /var/www/html/index.php  <br/>

### MySQL
sudo apt install mysql-server mysql-client php-mysql  <br/>
sudo mysql –u root –p  <br/>
<패스워드는 그냥 Enter>  <br/>
use mysql  <br/>
describe user; //테이블 구조 표시  <br/>
UPDATE mysql.user SET authentication_string=PASSWORD('root') WHERE user='root';    <br/>
flush privileges;  <br/>
quit   <br/>

###사용자 추가
create user 'pi' identified by 'raspberry';  <br/>
select user, password from user;  <br/>
grant all privileges on *.* to 'pi';  <br/>
quit  <br/>
sudo mysql –u pi –p raspberry  <br/>

### Apche2 설정
sudo nano /etc/apache2/apache2.conf  <br/>

<맨 끝줄에 추가>   <br/>
Include /etc/phpmyadmin/apache.conf  <br/>
<저장> <br/>

sudo service apache2 restart <br/>


root 권한으로 로그인  <br/>
sudo mysql –u root –p  <br/>
select user, plugin from useer;  <br/>
UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root';  <br/>
FLUSH PRIVILEGES;   <br/>


###워드프레스 설치
cd /var/www/html/  <br/>
sudo rm *  <br/>
sudo wget [http://wordpress.org/latest.tar.gz](http://wordpress.org/latest.tar.gz  "http://wordpress.org/latest.tar.gz")  <br/>
sudo tar xzf latest.tar.gz  <br/>
sudo mv wordpress/* .  <br/>
sudo rm -rf wordpress latest.tar.gz  <br/>
<설치후> <br/>
sudo chown -R www-data: .  <br/>

