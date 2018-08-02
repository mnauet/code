var mosca = require('mosca');
var settings = {
  port: 1883,
  http: {
	port:3000
}
};
 
//here we start mosca
var server = new mosca.Server(settings);
server.on('ready', setup);
 
// fired when the mqtt server is ready
function setup() {
  console.log('Mosca server is up and running')
}
 
// fired whena  client is connected
server.on('clientConnected', function(client) {
  console.log('client connected -client Id ', client.id);
});
 
// fired when a message is received
server.on('published', function(packet, client) {
  console.log('Published -> packet.payload : ', packet.payload);
});
 
// fired when a client subscribes to a topic
server.on('client subscribed to a topic', function(topic, client) {
  console.log('subscribed client - topic : ',client, topic);
});
 
// fired when a client subscribes to a topic
server.on('unsubscribed', function(topic, client) {
  console.log('unsubscribed : ', topic);
});
 
// fired when a client is disconnecting
server.on('clientDisconnecting', function(client) {
  console.log('clientDisconnecting : ', client.id);
});
 
// fired when a client is disconnected
server.on('clientDisconnected', function(client) {
  console.log('clientDisconnected : ', client.id);
});
