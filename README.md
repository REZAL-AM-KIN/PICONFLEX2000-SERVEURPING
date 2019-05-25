# Configuration de A à Z serveurs
## Serveur BDD
### Installation mysql  
> sudo apt install mysql-server php-mysql  
> sudo mysql --user=root  
### Creation d’un utilisateur avec tout les droit  
> DROP USER 'root'@'localhost';  
> CREATE USER 'XXX'@'%' IDENTIFIED BY 'YYY';  
> GRANT ALL PRIVILEGES ON . TO 'XXX'@'%’ WITH GRANT OPTION;  
(Lors de vos prochaine connections, vous pourrez donc utilisez la commande)  
> mysql --user=XXX --password=YYY  
### Installation phpmyadmin  
> sudo apt install phpmyadmin  
(Selectionner php puis no)  
> sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin  
## Serveur WEB
## Serveur MAJ
### Installation Fabric  
> pip3 install fabric3  
