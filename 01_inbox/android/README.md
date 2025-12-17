# Android Documentation Structure

## 📁 Folder Organization

The documentation is organized into the following categories:

### `/system` - System Core Components
Core Android system internals, kernel, and low-level infrastructure.

- `android-kernel.md` - Android kernel modifications (Binder driver, LMKD, etc.)
- `android-binder-and-ipc.md` - Inter-process communication mechanism
- `android-zygote-and-runtime.md` - Process creation and ART runtime
- `android-hal-and-kernel.md` - Hardware Abstraction Layer
- `android-init-and-services.md` - Init process and service management
- `android-boot-flow.md` - Boot sequence overview
- `android-activity-manager-and-system-services.md` - ActivityManager and system services
- `android-graphics-and-media.md` - Graphics pipeline and media framework
- `android-connectivity-and-networking.md` - Network stack
- `android-customization-and-oem.md` - OEM customization
- `android-process-and-memory.md` - Process and memory management

### `/security` - Security & Privacy
Security model, permissions, and privacy features.

- `android-security-and-sandboxing.md` - Security model and sandboxing
- `android-permissions-deep-dive.md` - Permission system details
- `android-privacy-features.md` - Privacy features

### `/development` - App Development
Application development, frameworks, and tools.

- `android-app-components-deep-dive.md` - Activity, Service, etc.
- `android-jetpack-architecture.md` - Architecture Components, ViewModel, etc.
- `android-compose-internals.md` - Jetpack Compose details
- `android-dependency-injection.md` - Hilt, Dagger, Koin
- `android-gradle-build-system.md` - Build system
- `android-ndk-jni.md` - Native development
- `android-large-screens.md` - Tablets, foldables
- `android-storage-systems.md` - File storage, databases
- `android-modular-system.md` - App bundles, dynamic delivery

### `/performance` - Performance & Debugging
Performance optimization, debugging tools, and profiling.

- `android-performance-and-debug.md` - Performance overview and checklist
- `android-debugging-techniques.md` - Debugging tools and techniques
- `android-profiling-tools.md` - Profiling and performance analysis

### `/reference` - Reference & Meta
Glossary, history, and general reference materials.

- `android-glossary.md` - Terminology
- `android-evolution-history.md` - Android version history
- `android-foundations.md` - Beginner-friendly overview
- `android-architecture-stack.md` - Architecture layers
- `android-internals-components.md` - Component overview
- `android-testing-and-quality.md` - Testing strategies
- `android-adb-and-images.md` - ADB and system images
- `android-os-development-guide.md` - AOSP development guide

---

## 📚 Reading Path

**For System Understanding**:
1. `reference/android-foundations.md` - Start here
2. `reference/android-architecture-stack.md` - Overall structure
3. `system/android-kernel.md` - Kernel basics
4. `system/android-binder-and-ipc.md` - IPC mechanism
5. `system/android-zygote-and-runtime.md` - Runtime
6. `system/android-init-and-services.md` - Init process
7. `security/android-security-and-sandboxing.md` - Security model

**For App Development**:
1. `development/android-app-components-deep-dive.md`
2. `development/android-jetpack-architecture.md`
3. `development/android-compose-internals.md`
4. `performance/android-performance-and-debug.md`

---

## ✨ Recently Improved (Tier 1)

These files have been comprehensively rewritten with historical context, mermaid diagrams, and technical depth:

- ✅ `system/android-binder-and-ipc.md` (51 → 700 lines)
- ✅ `system/android-zygote-and-runtime.md` (43 → 700 lines)
- ✅ `system/android-hal-and-kernel.md` (49 → 600 lines)
- ✅ `system/android-init-and-services.md` (72 → 700 lines)
- ✅ `security/android-security-and-sandboxing.md` (49 → 700 lines)

---

## 🔗 Cross-References

All documents are interlinked using `[[filename]]` syntax. Key reference documents:
- Operating systems: `[[kernel]]`, `[[selinux]]`, `[[virtual-memory]]`, `[[cpu-privilege-levels]]`, `[[buffer]]` (in `02_references/operating-systems/`)
- Android glossary: `[[android-glossary]]`
