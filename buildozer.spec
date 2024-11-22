[app]
# اسم التطبيق
title = xcion

# اسم الحزمة (يفضل أن يكون فريدًا)
package.name = myapp

# اسم المنظمة
package.domain = org.example

# اسم الملف الرئيسي (الملف الذي يحتوي على الكود الأساسي)
source.main = main.py

# إصدار التطبيق
version = 0.1

# اتجاه الشاشة
orientation = portrait

# تمكين وضع ملء الشاشة
fullscreen = 1

# ملف الأيقونة (تأكد من وجود الملف في نفس المجلد)
icon.filename = icon.jpg

# المكتبات المطلوبة لتشغيل التطبيق (تم قراءتها من requirements.txt)
requirements = python3, kivy, threading, pyjnius, uiautomator2, adb-shell

# الصلاحيات المطلوبة بواسطة التطبيق
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW, WAKE_LOCK

# الحد الأدنى لإصدار Android
android.minapi = 21

# إصدار SDK الخاص بـ Android
android.api = 33

# إصدار NDK الخاص بـ Android
android.ndk = 25b

# إعداد معمارية المعالج
android.arch = arm64-v8a, armeabi-v7a

# تمكين الوصول لوحدات إضافية
p4a.branch = develop

# تمكين أزرار التنقل الافتراضية
android.allow_backup = 1

# تعطيل إضافة مكتبات أخرى تلقائيًا
android.bootstrap = sdl2
