[app]
title = My Telegram
package.name = mytelegram
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 33
minapi = 21
ndk = 25b
sdk = 33
android.accept_sdk_license = True
android.ndk_path = /data/data/com.termux/files/usr/lib/android-ndk
android.sdk_path = /data/data/com.termux/files/usr/lib/android-sdk
android.arch = arm64-v8a
android.permissions = INTERNET
android.extra_java_args = -Xmx1G
