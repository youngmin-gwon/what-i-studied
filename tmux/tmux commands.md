---
aliases: []
date created: 2024-12-09 21:31:10 +09:00
date modified: 2024-12-16 12:20:56 +09:00
tags: [command, tmux]
title: tmux commands
---

## open

```bash
tmux
```

## window

__ctrl b__ + __c__ : create window

__ctrl b__ + __&__ : close window

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

connect to the target session

```zsh
tmux a -t $session_id
```

rename session

```zsh
tmux rename-session -t $session_id $new_session_name
```

## customization

reload tmux configuration

```zsh
tmux source-file ~/.tmux.conf
```

go to config file "*~/.tmux.conf*"
