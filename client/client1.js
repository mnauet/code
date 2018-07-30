var GPIO = require ('onoff').Gpio;
var led = new GPIO(23, 'out');
var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://localhost');

client.on('connect', function () {
	client.subscribe('led1')
	client.publish('debug', 'node.js client1 connected ...')

})


client.on('message', function(topic,message) {
	if(message == 1){
		console.log("LED ON");
		led.writeSync(0);
		}
else if(message == 0){
	console.log("LED OFF ");
	led.writeSync(0);
	}
else{
	console.log("unsupported message");
	console.log(message.toString());
	}

})



