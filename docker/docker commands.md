---
aliases: []
date created: 2024-12-09 21:31:10 +09:00
date modified: 2024-12-16 12:22:05 +09:00
tags: [command, docker]
title: docker commands
---

- List all docker containers (running and stopped):

```bash
docker ps --all
```

- Start a container from an image, with a custom name:

```bash
docker run --name container_name image
```

- Start or stop an existing container:

```bash
docker start|stop container_name
```

- Pull an image from a docker registry:

```bash
docker pull image
```

- Display the list of already downloaded images:

```bash
docker images
```

- Open a shell inside a running container:

```bash
docker exec -it container_name sh
```

- Remove a stopped container:

```bash
docker rm container_name
```

- Fetch and follow the logs of a container:

```bash
docker logs -f container_name
```
