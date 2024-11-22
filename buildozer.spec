[app]
# اسم التطبيق
title = Xcoin

# اسم الحزمة (يفضل أن يكون فريدًا)
package.name = myapp

# اسم المنظمة
package.domain = org.example

# الملف الرئيسي
source.main = main.py

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

# إعداد المعمارية
android.arch = arm64-v8a, armeabi-v7a

# إعداد نوع الإقلاع
android.bootstrap = sdl2
