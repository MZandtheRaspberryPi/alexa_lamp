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

Then I navigate to edit the skill in the Amazon developper portal, and put the ngrok endpoint into the skill. Because ngrok creates a new link each time it is run, I have to update the link each time I want to run the service. At some point I'll move to a permanent endpoint, but while I'm testing this I'm ok updating the endpoint each time I use it.
https://developer.amazon.com/alexa/console/ask
