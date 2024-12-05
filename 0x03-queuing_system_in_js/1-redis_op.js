import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

const setNewSchool = (schoolName, value) => {
  redisClient.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  redisClient.get(schoolName, (err, value) => {
    if (err) {
      console.log('Failed to get a value for key=', schoolName);
    } else {
      console.log(value);
    }
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
