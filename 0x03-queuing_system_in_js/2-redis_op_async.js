import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (!err) {
            redis.print(`Reply: ${reply}`);
        } 
    });
}

async function displaySchoolValue(schoolName) {   
    try {
        const value = await getAsync(schoolName);
        if (value) {
            console.log(value);
        } 
    } catch {
        console.error('Failed to fetch data');
        return null;
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
