
const MongoClient = require('mongodb').MongoClient;

// Connection URL
const url = 'mongodb://localhost:27017';

// Database Name
const dbName = 'dbPDS';

// Create a new MongoClient
const client = new MongoClient(url, { monitorCommands: true });
console.log("\n\n\n\nTESTE\n\n\n\n");
// Connect to the MongoDB server
// Connect to the MongoDB server
async function connect() {
    try {
        await client.connect();
        console.log('Connected to MongoDB');
        
        // Create a new database
        const db = client.db(dbName);
        
        try{
        // Perform other database operations here
            getOrgInfo("https://api.github.com/orgs/systems-furg-edu/members", token);
        }catch(err){
            console.log("Error: "+err);
        }
        // sleep to wait for the data to be inserted
        await new Promise(resolve => setTimeout(resolve, 1000));

        // print the data inserted
        const collection = db.collection('users');
        const docs = await collection.find({}).toArray();
        // console.log(docs);

  
    } catch (err) {
        console.log("Can't connect to MongoDB" + err);
        
        // Ensure that the client will close when you finish using it
        await client.close();
    }
}
connect().catch(console.error);
// client.connect(function(err) {
//     if (err) {
//         console.error('Failed to connect to MongoDB:', err);
//         return;
//     }
    
//     console.log('Connected successfully to MongoDB');
//     console.log("\n\n\n\n"+client+"\n\n\n\n");

//     // const db = client.db(dbName);

//     // Perform database operations
//     // ...

//     // Close the connection
//     client.close();
// });



const token = "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";
let orgData;

function getOrgInfo(url, token){
    fetch(url , {
        headers: {
            "Accept": "application/vnd.github+json",
            "Authorization": `Bearer ${token}`,
            "X-GitHub-Api-Version": "2022-11-28"
        }
    })
        .then(response => response.json())
        .then( returnedData => {
            returnedData.map( member => {
                getUserInfo(member.login, token);
            });
        })
        .catch(error => {
            console.error(error);
        });
}
function getUserInfo(username, token){
    fetch("https://api.github.com/users/"+username , {
        headers: {
            "Accept": "application/vnd.github+json",
            "Authorization": `Bearer ${token}`,
            "X-GitHub-Api-Version": "2022-11-28"
        }
    })
        .then(response => response.json())
        .then( returnedData => {

            console.log(returnedData);   
            // Filter out the null values
            const filteredData = Object.fromEntries(
                Object.entries(returnedData).filter(([key, value]) => value !== null)
            );
            
            console.log(filteredData);
            // Insert a single document
            const db = client.db(dbName);
            const collection = db.collection('users');
            collection.insertOne(filteredData);

            // add the data to it like a json structure in txt file
            // const fs = require('fs');
            // fs.appendFileSync('data.txt', JSON.stringify(filteredData));

            
            
            
            console.log('Data added to MongoDB');

            // console.log(returnedData);
        })
        .catch(error => {
            console.error(error);
        });
}


