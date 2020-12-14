# alexa_lamp
A project to connect an Amazon Echo Dot to my Raspberry Pi Mood Lamp. I wanted to get a proof of concept using voice control working, and this is what I hit on. I already had built a pimoroni mood lamp from the pimoroni kit a year or two ago, and after my roomate gave me an echo dot I decided to revisit that project. You can see the pimoroni kit [here](https://shop.pimoroni.com/products/mood-light-pi-zero-w-project-kit).

I used mainly this tutorial: https://create.arduino.cc/projecthub/rajesh3/light-control-using-arduino-and-amazon-alexa-4de729?ref=tag&ref_id=alexa&offset=8

When it comes time to launch everything, in one terminal I run the below command using python2.
```
sudo python alexa_server.py
```

Then in a seperate terminal I run the below ngrok command to open a path to that local host that the internet can reach.
```
./ngrok http 5000
```

And because my Alexa skill is setup, I can then control the map. Pretty cool!
https://developer.amazon.com/alexa/console/ask
