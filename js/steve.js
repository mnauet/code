		var mqtt;
		var reconnectTimeout = 2000;
		var host="127.0.0.1"; //change this
		var port=3000;

		function onFailure(message) {
			console.log("Connection Attempt to Host "+ host + "Failed");
			setTimeout(MQTTconnect, reconnectTimeout);
        }
		function onMessageArrived(msg){
			out_msg="Message received " + msg.payloadString + "<br>";
			out_msg=out_msg + "Message received Topic " + msg.destinationName;
			console.log(out_msg);

		}

		
	 	function onConnect() {
	  	// Once a connection has been made, make a subscription and send a message.
	
			console.log("Connected ");
			mqtt.subscribe("sensor1");
			message = new Paho.MQTT.Message("Hello World");
			message.destinationName = "sensor1";
			mqtt.send(message);
	  	}
	  	function MQTTconnect() {
			console.log("connecting to "+ host +" "+ port);
			mqtt = new Paho.MQTT.Client(host,port,"client-js-malik");
			var options = {
				timeout: 3,
				onSuccess: onConnect,
				onFailure: onFailure,
		  
		 	};

			mqtt.onMessageArrived = onMessageArrived
			mqtt.connect(options); //connect
		}
	 
