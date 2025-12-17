---
title: apple-urlsession-deep-dive
tags: [apple, networking, urlsession, http]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## URLSession Deep Dive apple networking urlsession http

URLSession 을 사용한 네트워킹. 기본은 [[apple-networking-and-cloud]] 참고.

### URLSession Configuration

```swift
// Default
let defaultSession = URLSession(configuration: .default)

// Ephemeral (캐시 안 함)
let ephemeralSession = URLSession(configuration: .ephemeral)

// Background
let backgroundConfig = URLSessionConfiguration.background(withIdentifier: "com.example.bg")
let backgroundSession = URLSession(configuration: backgroundConfig)
```

### Data Task

```swift
func fetchData() async throws -> Data {
    let url = URL(string: "https://api.example.com/data")!
    let (data, response) = try await URLSession.shared.data(from: url)
    
    guard let httpResponse = response as? HTTPURLResponse,
          (200...299).contains(httpResponse.statusCode) else {
        throw NetworkError.invalidResponse
    }
    
    return data
}
```

### Upload Task

```swift
func uploadFile(data: Data) async throws {
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let (_, response) = try await URLSession.shared.upload(for: request, from: data)
    
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw NetworkError.uploadFailed
    }
}
```

### Download Task

```swift
func downloadFile() async throws -> URL {
    let url = URL(string: "https://example.com/file.pdf")!
    let (localURL, response) = try await URLSession.shared.download(from: url)
    
    // 파일을 영구 위치로 이동
    let documentsURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
    let destinationURL = documentsURL.appendingPathComponent("file.pdf")
    
    try FileManager.default.moveItem(at: localURL, to: destinationURL)
    return destinationURL
}
```

### 더 보기

[[apple-networking-and-cloud]], [[apple-codable-json]], [[apple-swift-concurrency]]
