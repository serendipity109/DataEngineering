CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255) NOT NULL,
    trip_id VARCHAR(255),
    direction_id TINYINT,
    label VARCHAR(50),
    stop_id VARCHAR(50),
    latitude DECIMAL(11,8) NOT NULL,
    longitude DECIMAL(11,8) NOT NULL,
    bearing INT,
    current_status VARCHAR(50),
    current_stop_sequence INT,
    occupancy_status VARCHAR(50),
    updated_at DATETIME
);