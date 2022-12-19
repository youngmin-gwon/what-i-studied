## open

```bash
tmux
```

## window

__ctrl b__ + __c__ : create window

__ctrl b__ + __,__ : edit window name

__ctrl b__ & __l__ : change window to next one

__ctrl b__ + __w__ : show all windows

__ctrl b__ + __f__ : find window by name

## pane

__ctrl b__ + __%__ : horizontal split

__ctrl b__ + __"__ : vertical split

## session

__ctrl b__ + __d__ : close tmux but leave session

connect to the last session
```zsh
tmux attach
```

check tmux session list
```zsh
tmux ls
```

conect to the target session
```zsh
tmux a -t $session_id
```

rename session
```zsh
tmux rename-session -t $session_id $new_session_name
```