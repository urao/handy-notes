# CheatSheet to create a tmux session and navigate around

### Create a new session
```
tmux new -s <session-name>
```

### List all sessions
```
tmux ls
```

### Connect to a specific session
```
tmux a -t <session-name>
```

### Create a new pane and close
```
Ctrl-b c
Ctrl-b &
```

### List all the panes/windows
```
Ctrl-b w
```

### Nagviate to previous, next window
```
Ctrl-b p
Ctrl-b n
```

### Dettach from tmux session
```
Ctrl-b d
```

### Move cursor
```
Ctrl-b [
move cursor
q
```
