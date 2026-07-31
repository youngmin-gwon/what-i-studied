---
title: BufferQueue는 producer와 consumer를 버퍼 소유권으로 분리한다
tags: [android, android/graphics, android/ipc]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

BufferQueue는 그래픽 버퍼를 만드는 producer와 그 버퍼를 표시하거나 처리하는 consumer를 연결한다. producer는 빈 버퍼를 얻고 내용을 채운 뒤 queue에 넣고, consumer는 준비된 버퍼를 acquire해서 사용한 뒤 release한다.

이 구조 덕분에 앱 프로세스, system_server, SurfaceFlinger, media service처럼 서로 다른 프로세스와 스레드가 버퍼를 직접 복사하지 않고 소유권과 동기화 신호를 주고받을 수 있다. Binder는 버퍼 핸들과 제어 메시지를 전달하는 경계로 함께 등장한다.

BufferQueue는 항상 “트리플 버퍼링” 하나로 설명하면 안 된다. 큐 깊이, blocking 여부, discard 동작, producer/consumer 속도는 대상 Surface와 시스템 정책에 따라 달라진다.

성능 문제에서는 큐가 비어 있는지, 가득 차 있는지, producer가 기다리는지, consumer가 늦는지를 구분해야 한다. 같은 dropped frame이라도 앱이 늦은 경우와 consumer가 늦은 경우의 처방은 다르다.

관련 노트: {link(ANDROID / "01_system_internals/ipc-and-process/android-binder-and-ipc.md", "Android Binder and IPC")}, {link(contracts_hub / "surface-based-media-pipeline-avoids-app-level-pixel-copy.md", "Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다")}

근거: [AOSP BufferQueue and Gralloc](https://source.android.com/docs/core/graphics/arch-bq-gralloc)
