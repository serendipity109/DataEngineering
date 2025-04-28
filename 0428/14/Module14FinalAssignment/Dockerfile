FROM mysql:8.0
    
ENV MYSQL_DATABASE=employeedb \
    MYSQL_ROOT_PASSWORD=MyNewPass
    
ADD employee.sql /docker-entrypoint-initdb.d
    
EXPOSE 3306
    
    