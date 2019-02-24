# speedometer
Speedometer to measure your Internet bandwidth speed with pure python; no extra modules or binaries needed

# Example usage:

On a laptop, via Wifi:
```
sander@witte:~/git/speedometer$ ./speedometer.py 
Basic measurement, with small download:
URL is http://download.thinkbroadband.com/5MB.zip
Downloaded bytes: 5242880
Speed in MB/s: 11.21
Speed in Mbps: 90.26


Measurement with bigger download, doable within 10 seconds
http://download.thinkbroadband.com/100MB.zip
URL is http://download.thinkbroadband.com/100MB.zip
Downloaded bytes: 104857600
Speed in MB/s: 25.98
Speed in Mbps: 209.13
```

On another device (ARM), via wired GigE, on a 250 Mbps FttH connection:

```
sander@nanopineo2:~/git/speedometer$ ./speedometer.py 
Basic measurement, with small download:
URL is http://download.thinkbroadband.com/5MB.zip
Downloaded bytes: 5242880
Speed in MB/s: 9.05
Speed in Mbps: 72.87


Measurement with bigger download, doable within 10 seconds
http://download.thinkbroadband.com/50MB.zip
URL is http://download.thinkbroadband.com/50MB.zip
Downloaded bytes: 52428800
Speed in MB/s: 29.27
Speed in Mbps: 235.63
```

# Bug

On very low memory systems (256 MB RAM) with high speed connections, strange things can happen: too low speed reported (because of swapping?), of "Killed"
