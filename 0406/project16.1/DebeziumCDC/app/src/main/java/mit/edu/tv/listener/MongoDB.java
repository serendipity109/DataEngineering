package mit.edu.tv.listener;

import java.util.ArrayList;
import java.util.List;

import org.bson.Document;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;

public class MongoDB {

    public void testConnection() {
        String connectionString = "mongodb://some-mongo:27017";
        try {
            MongoClient mongoClient = MongoClients.create(connectionString);
            List<Document> databases = mongoClient.listDatabases().into(new ArrayList<>());
            databases.forEach(db -> System.out.println(db.toJson()));
        } catch (Exception e) {
        }

    }

    public void insertRecord(String record) {
        String connectionString = "mongodb://some-mongo:27017";
        try {
            MongoClient mongoClient = MongoClients.create(connectionString);
            MongoDatabase database = mongoClient.getDatabase("myDatabase");
            Document document = new Document();
            document.append("recordId", "CDC");
            document.append("value", record);
            database.getCollection("myCollection").insertOne(document);
        } catch (Exception e) {
        }
    }
}
