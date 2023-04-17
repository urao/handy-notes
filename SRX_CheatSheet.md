```
Below commands to execute on Juniper SRX FW device
```

```
monitor security packet-drop
```

```
show interfaces extensive ae1.2* | match "face:|logical|description|input :|output:|Statistics.*pps"
show interfaces extensive ae2.3[1357] | match "face:|logical|description|input :|output:|Statistics.*pps"
show interfaces ae1.2* | match "face:|logical|description|input :|output:|Statistics.*pps"
show interfaces ae2.3[1357] | match "face:|logical|description|input :|output:|Statistics.*pps"
show interfaces ae*.[23]* | match "face:|logical|description|input :|output:|Statistics.*pps"
show interfaces "ae*.[23][0-7]" | match "face:|logical|description|input :|output:|Statistics.*pps"
```
