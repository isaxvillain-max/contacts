[app]
# (str) Title of your application
title = ShareContactsIsa
# (str) Package name
package.name = sharecontactsisa
# (str) Package domain (reverse domain)
package.domain = org.isa
# (str) Source dir
source.dir = .
# (list) Application requirements
requirements = python3,kivy,pyjnius
# (str) Android API to target
android.api = 33
# (str) Android NDK version
android.ndk = 25b
# (str) Presplash
presplash.filename =
# (str) Icon
icon.filename =
# (str) Application version
version = 0.1
# (str) Version regex (optional, leave commented if using simple version)
# version.regex =
# (str) Orientation
orientation = portrait
# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level
log_level = 2
# (str) Build directory
build_dir = .buildozer
# (str) Bin directory
bin_dir = bin
