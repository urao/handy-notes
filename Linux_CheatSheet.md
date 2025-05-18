### List of useful linux commands

```
tar -T <filename> -czvf archive.tgz
```

### Create a large file
```
fallocate -l 10G tmp_file.img
```
```
cat /dev/zero > /var/log/application.log
```

### Sed command
```
sed -i -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/127.0.0.1/g' /.../myfile.txt


:%s/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}//g
:%s/x,x,,x/,,,/
:%s/\/[0-9]*//
```
