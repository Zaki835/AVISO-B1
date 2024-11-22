[app]
# اسم التطبيق
title = MyApp

# اسم الحزمة (يفضل أن يكون فريدًا)
package.name = myapp

# اسم المنظمة
package.domain = org.example

# الملف الرئيسي
source.main = main.py

# المجلد الذي يحتوي على ملفات المشروع (عادة يكون ".")
source.dir = .

# إصدار التطبيق
version = 0.1

# اتجاه الشاشة
orientation = portrait

# تمكين وضع ملء الشاشة
fullscreen = 1

# الأيقونة (إذا كانت لديك)
icon.filename = icon.jpg

# المكتبات المطلوبة (نفس المكتبات الموجودة في requirements.txt)
requirements = python3, kivy, threading, pyjnius, uiautomator2, adb-shell

# الصلاحيات المطلوبة
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW, WAKE_LOCK

# إعداد المعمارية (استخدم `android.archs` بدلاً من `android.arch`)
android.archs = arm64-v8a, armeabi-v7a

# إعداد نوع الإقلاع (bootstrap الجديد)
p4a.bootstrap = sdl2
