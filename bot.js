const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
    host: '192.168.3.198', // Replace with your LAN IP
    port: 50006,           // Replace with your Minecraft server port
    username: 'BabyAI'
});

bot.on('spawn', () => {
    console.log('Bot has joined the world!');
});

bot.on('error', (err) => {
    console.error('An error occurred:', err);
});

bot.on('end', () => {
    console.log('Bot has disconnected.');
});
