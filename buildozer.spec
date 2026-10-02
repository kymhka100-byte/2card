[app]

title = 2장 까기
package.name = memorycard
package.domain = org.yeongmin

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
source.exclude_dirs = .github,.git,bin,.buildozer

version = 1.0

requirements = python3,kivy==2.3.0,plyer,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = VIBRATE

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

p4a.branch = v2024.01.21

[buildozer]

log_level = 2
warn_on_root = 1
