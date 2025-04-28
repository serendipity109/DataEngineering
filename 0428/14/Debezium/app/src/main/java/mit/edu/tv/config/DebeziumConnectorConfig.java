package mit.edu.tv.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.File;
import java.io.IOException;

@Configuration
public class DebeziumConnectorConfig {

    /**
     * Employee Database Connector Configuration
     */
    @Bean
    public io.debezium.config.Configuration employeeConnector() throws IOException {
        String absolutePath = System.getProperty("user.dir");
        File currentDir = new File(absolutePath);
        String parentDir = currentDir.getParent();
        String offsetFile = parentDir + "/employee-offset.dat";
        String historyFile = parentDir + "/employee-history.dat";

        System.out.println("Debezium offset file: " + offsetFile);
        System.out.println("Debezium history file: " + historyFile);

        return io.debezium.config.Configuration.create()
                .with("name", "employee-mysql-connector")
                .with("connector.class", "io.debezium.connector.mysql.MySqlConnector")
                .with("offset.storage", "org.apache.kafka.connect.storage.FileOffsetBackingStore")
                .with("offset.storage.file.filename", offsetFile)
                .with("offset.flush.interval.ms", "60000")
                .with("database.hostname", "mysqlmasterdb")
                .with("database.port", 3306)
                .with("database.user", "root")
                .with("database.password", "my-secret-pw")
                .with("database.dbname", "employeedb")
                .with("database.include.list", "employeedb")
                .with("table.include.list", "employeedb.employee")
                .with("include.schema.changes", "false")

                .with("database.allowPublicKeyRetrieval", "true")
                .with("database.server.id", "10181")
                .with("database.server.name", "localhost_employeedb")

                .with("database.history", "io.debezium.relational.history.FileDatabaseHistory")
                .with("database.history.file.filename", historyFile)
                .build();
    }
}
