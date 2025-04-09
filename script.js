(async function loopTasks() {
    while (true) {
        try {
            // 1. انتظار مدة 3 ثواني قبل البدء
            console.log("انتظار 3 ثواني...");
            await new Promise(res => setTimeout(res, 3000));

            // 2. البحث عن أول زر "Посмотреть видео" والضغط عليه
            const startBtn = document.querySelector("span[id^='link_ads_start_']");
            if (!startBtn) {
                console.log("لا يوجد فيديو حالي للتشغيل.");
                await new Promise(res => setTimeout(res, 5000));
                continue;
            }

            // استخراج رقم المهمة من ID
            const taskId = startBtn.id.replace("link_ads_start_", "");

            // 3. استخراج مدة الفيديو من الخاصية onclick (مثلاً 'funcjs["start_youtube_new"](5308727, "10");')
            const onclickAttr = startBtn.getAttribute("onclick");
            const durationMatch = onclickAttr.match(/'start_youtube_new'\d+,\s*'(\d+)'/);
            const durationSeconds = durationMatch ? parseInt(durationMatch[1]) : 20;

            console.log(`تشغيل الفيديو ${taskId} لمدة ${durationSeconds} ثانية...`);
            startBtn.click();

            // 4. الانتظار لمدة الفيديو + 3 ثواني إضافية
            await new Promise(res => setTimeout(res, (durationSeconds + 3) * 1000));

            // 5. إغلاق التبويبة الحالية والرجوع للرئيسية
            if (window.openedTab) {
                window.openedTab.close();
            } else {
                window.close(); // في حال كانت الإضافة في نفس التبويب
            }

            // 6. النقر على زر "Подтвердить просмотр" لتأكيد المهمة
            const confirmBtn = document.querySelector(`#ads_btn_confirm_${taskId}`);
            if (confirmBtn) {
                console.log("يتم تأكيد المشاهدة...");
                confirmBtn.click();
            } else {
                console.log("لم يتم العثور على زر تأكيد المهمة.");
            }

        } catch (error) {
            console.error("حدث خطأ في التنفيذ:", error);
        }

        // انتظار قبل تكرار الدورة التالية
        await new Promise(res => setTimeout(res, 5000));
    }
})();
