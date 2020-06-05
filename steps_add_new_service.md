### Steps to add a custom service in centos
```
cd /usr/lib/systemd/system
create <service_name>.timer
create <service_name>.service
```

### Sample timer file
```
[Unit]
Description= Run this service every hourly
Requires=<service_name>.service

[Timer]
Unit=<service_name>.service
OnCalendar=hourly

[Install]
Wanted=timers.target
```

### Sample service file
```
[Unit]
Description= Run this service every hourly
Wants=<service_name>.timer

[Service]
ExecStart=<Location of the script>

[Install]
Wanted=multi-user.target
```
