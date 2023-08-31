const getData = require('./functions');

// Define a callback function to handle the data received from the bot
function dataCallback(data) {
  console.log(`Voice channels in this server: ${data}`);
}

// Call the getData function and pass the dataCallback function as the callback
getData(dataCallback);