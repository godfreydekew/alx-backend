import redis from 'redis';

const client = redis.createClient();

const cities = {
    Portland: 50,
    Seattle: 80,
    'New York': 20, 
    Bogota: 20,
    Cali: 40,
    Paris: 2
};
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});



for (const city in cities) {
    client.hset('HolbertonSchools', city, cities[city], (err, reply) => {
        if (err) throw err;
        console.log(`Reply: ${reply}`);
    });
}


client.hgetall('HolbertonSchools', (err, value) => {
    if (err) throw err;
    console.log(value);
});
