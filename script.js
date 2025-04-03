// انتظر حتى يتم تحميل الصفحة بالكامل
window.addEventListener("load", function() {
    console.log("🔹 Aviso Bot: الصفحة تم تحميلها.");

    // البحث عن زر "Посмотреть видео" والنقر عليه
    let videoButton = document.querySelector("span[onclick^=\"funcjs['start_youtube_new']\"]");
    if (videoButton) {
        console.log("✅ العثور على زر مشاهدة الفيديو.");
        videoButton.click();
        console.log("🎬 تم النقر على زر مشاهدة الفيديو.");
    } else {
        console.log("❌ لم يتم العثور على زر مشاهدة الفيديو.");
    }

    // الانتظار لفترة قبل النقر على زر "Подтвердить просмотр"
    setTimeout(() => {
        let confirmButton = document.querySelector("span[onclick^=\"funcjs['viewCheckDirect']\"]");
        if (confirmButton) {
            console.log("✅ العثور على زر تأكيد المشاهدة.");
            confirmButton.click();
            console.log("✔️ تم النقر على زر تأكيد المشاهدة.");
        } else {
            console.log("❌ لم يتم العثور على زر تأكيد المشاهدة.");
        }
    }, 10000); // الانتظار 10 ثوانٍ قبل الضغط
});
