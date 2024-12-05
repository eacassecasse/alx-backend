import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

const redisSet = promisify(redisClient.set).bind(redisClient);
const redisGet = promisify(redisClient.get).bind(redisClient);
const setNewSchool = async (schoolName, value) => {
  try {
    await redisSet(schoolName, value);
    redis.print(null, 'OK');
  } catch (e) {
    console.log('Failed to set a new value:', e);
  }
};

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await redisGet(schoolName);
    console.log(value);
  } catch (e) {
    console.log('Failed to get a value', e);
  }
};

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
