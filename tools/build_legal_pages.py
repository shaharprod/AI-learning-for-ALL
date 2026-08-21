# -*- coding: utf-8 -*-
"""Generate privacy / accessibility / terms pages for all locales."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = "V1.1"  # bumped later to V0.1 by apply script
ICON = "images/%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A1%D7%9A%202026-02-09%20160037.png"
LOGO = "images/colorful%20digital%20media%20sy.png"

LANGS = {
    "he": {
        "html_lang": "he", "dir": "rtl", "suffix": "", "home": "index.html",
        "font": "Heebo:wght@300;400;500;700", "extra_style": "",
        "logo": "AI-learning-for-ALL", "ded": "נבנה עבור כל מי שרוצה ללמוד",
        "nav": [("index.html", "בית"), ("index.html#intro", "מה זה AI?"),
                ("pages/glossary.html", "מילון"), ("pages/ai-tools.html", "כלים"),
                ("index.html#about", "אודות")],
        "lessons_label": "שיעורים ▾", "search_ph": "חיפוש מילים ומושגים...", "search_aria": "חיפוש באתר",
        "menu": "תפריט", "lang_label": "בחירת שפה",
        "lessons": [
            ("pages/intro-to-ai.html", "1. מבוא ל-AI"),
            ("pages/ai-history.html", "2. ההיסטוריה של AI"),
            ("pages/machine-learning.html", "3. למידת מכונה"),
            ("pages/ai-daily-life.html", "4. AI בחיי היומיום"),
            ("pages/ai-tools.html", "5. כלים מעשיים"),
            ("pages/prompt-engineering.html", "6. הנדסת הנחייה"),
            ("pages/ai-ethics.html", "7. אתיקה ב-AI"),
            ("pages/ai-future.html", "8. העתיד של AI"),
            ("pages/glossary.html", "9. מילון מושגים"),
        ],
        "footer": "© 2026 AI-learning-for-ALL - כל הזכויות שמורות לשמוליק שחר יועץ לימודי המנגיש לימודי בינה מלאכותית לכל אדם",
        "phone": "טלפון", "email": "אימייל", "updated": "עודכן לאחרונה: 21 באוגוסט 2026",
        "site_title": "AI-learning-for-ALL",
    },
    "en": {
        "html_lang": "en", "dir": "ltr", "suffix": "-en", "home": "index-en.html",
        "font": "Heebo:wght@300;400;500;700", "extra_style": "body { direction: ltr; }",
        "logo": "AI-learning-for-ALL", "ded": "Built for anyone who wants to learn",
        "nav": [("index-en.html", "Home"), ("index-en.html#intro", "What is AI?"),
                ("pages/glossary-en.html", "Glossary"), ("pages/ai-tools-en.html", "Tools"),
                ("index-en.html#about", "About")],
        "lessons_label": "Lessons ▾", "search_ph": "Search words and terms...", "search_aria": "Search site",
        "menu": "Menu", "lang_label": "Language",
        "lessons": [
            ("pages/intro-to-ai-en.html", "1. Intro to AI"),
            ("pages/ai-history-en.html", "2. History of AI"),
            ("pages/machine-learning-en.html", "3. Machine Learning"),
            ("pages/ai-daily-life-en.html", "4. AI in Daily Life"),
            ("pages/ai-tools-en.html", "5. Practical Tools"),
            ("pages/prompt-engineering-en.html", "6. Prompt Engineering"),
            ("pages/ai-ethics-en.html", "7. AI Ethics"),
            ("pages/ai-future-en.html", "8. The Future of AI"),
            ("pages/glossary-en.html", "9. Glossary"),
        ],
        "footer": "© 2026 AI Learning – All rights reserved. Sam Shahar – Educational consultant making AI learning accessible to everyone.",
        "phone": "Phone", "email": "Email", "updated": "Last updated: 21 August 2026",
        "site_title": "AI Learning",
    },
    "ar": {
        "html_lang": "ar", "dir": "rtl", "suffix": "-ar", "home": "index-ar.html",
        "font": "Heebo:wght@300;400;500;700", "extra_style": "",
        "logo": "AI-learning-for-ALL", "ded": "بُني لكل من يريد أن يتعلم",
        "nav": [("index-ar.html", "الرئيسية"), ("index-ar.html#intro", "ما هو الذكاء الاصطناعي؟"),
                ("pages/glossary-ar.html", "المعجم"), ("pages/ai-tools-ar.html", "الأدوات"),
                ("index-ar.html#about", "عن الموقع")],
        "lessons_label": "الدروس ▾", "search_ph": "بحث عن كلمات ومصطلحات...", "search_aria": "بحث في الموقع",
        "menu": "القائمة", "lang_label": "اختيار اللغة",
        "lessons": [
            ("pages/intro-to-ai-ar.html", "1. مقدمة في الذكاء الاصطناعي"),
            ("pages/ai-history-ar.html", "2. تاريخ الذكاء الاصطناعي"),
            ("pages/machine-learning-ar.html", "3. تعلّم الآلة"),
            ("pages/ai-daily-life-ar.html", "4. الذكاء الاصطناعي في الحياة اليومية"),
            ("pages/ai-tools-ar.html", "5. أدوات عملية"),
            ("pages/prompt-engineering-ar.html", "6. هندسة الأوامر"),
            ("pages/ai-ethics-ar.html", "7. أخلاقيات الذكاء الاصطناعي"),
            ("pages/ai-future-ar.html", "8. مستقبل الذكاء الاصطناعي"),
            ("pages/glossary-ar.html", "9. المعجم"),
        ],
        "footer": "© 2026 موقع تعلّم الذكاء الاصطناعي — جميع الحقوق محفوظة لشموئيل شاحار.",
        "phone": "هاتف", "email": "البريد الإلكتروني", "updated": "آخر تحديث: 21 آب/أغسطس 2026",
        "site_title": "تعلّم الذكاء الاصطناعي",
    },
    "hi": {
        "html_lang": "hi", "dir": "ltr", "suffix": "-hi", "home": "index-hi.html",
        "font": "Heebo:wght@300;400;500;700", "extra_style": "body { direction: ltr; }",
        "logo": "AI-learning-for-ALL", "ded": "हर किसी के लिए जो सीखना चाहता है",
        "nav": [("index-hi.html", "होम"), ("index-hi.html#intro", "एआई क्या है?"),
                ("pages/glossary-hi.html", "शब्दावली"), ("pages/ai-tools-hi.html", "उपकरण"),
                ("index-hi.html#about", "परिचय")],
        "lessons_label": "पाठ ▾", "search_ph": "शब्द और शब्द खोजें...", "search_aria": "साइट खोज",
        "menu": "मेनू", "lang_label": "भाषा चुनें",
        "lessons": [
            ("pages/intro-to-ai-hi.html", "1. एआई का परिचय"),
            ("pages/ai-history-hi.html", "2. एआई का इतिहास"),
            ("pages/machine-learning-hi.html", "3. मशीन लर्निंग"),
            ("pages/ai-daily-life-hi.html", "4. रोज़मर्रा की ज़िंदगी में एआई"),
            ("pages/ai-tools-hi.html", "5. व्यावहारिक उपकरण"),
            ("pages/prompt-engineering-hi.html", "6. प्रॉम्प्ट इंजीनियरिंग"),
            ("pages/ai-ethics-hi.html", "7. एआई नैतिकता"),
            ("pages/ai-future-hi.html", "8. एआई का भविष्य"),
            ("pages/glossary-hi.html", "9. शब्दावली"),
        ],
        "footer": "© 2026 एआई लर्निंग — सर्वाधिकार सुरक्षित, शमूएल शाहर।",
        "phone": "फ़ोन", "email": "ईमेल", "updated": "अंतिम अद्यतन: 21 अगस्त 2026",
        "site_title": "एआई सीखना",
    },
    "ru": {
        "html_lang": "ru", "dir": "ltr", "suffix": "-ru", "home": "index-ru.html",
        "font": "Roboto:wght@300;400;500;700", "extra_style": "body { direction: ltr; }",
        "logo": "AI-learning-for-ALL", "ded": "Создано для всех, кто хочет учиться",
        "nav": [("index-ru.html", "Главная"), ("index-ru.html#intro", "Что такое ИИ?"),
                ("pages/glossary-ru.html", "Словарь"), ("pages/ai-tools-ru.html", "Инструменты"),
                ("index-ru.html#about", "О сайте")],
        "lessons_label": "Уроки ▾", "search_ph": "Поиск слов и терминов...", "search_aria": "Поиск по сайту",
        "menu": "Меню", "lang_label": "Язык",
        "lessons": [
            ("pages/intro-to-ai-ru.html", "1. Введение в ИИ"),
            ("pages/ai-history-ru.html", "2. История ИИ"),
            ("pages/machine-learning-ru.html", "3. Машинное обучение"),
            ("pages/ai-daily-life-ru.html", "4. ИИ в повседневной жизни"),
            ("pages/ai-tools-ru.html", "5. Практические инструменты"),
            ("pages/prompt-engineering-ru.html", "6. Промпт-инжиниринг"),
            ("pages/ai-ethics-ru.html", "7. Этика ИИ"),
            ("pages/ai-future-ru.html", "8. Будущее ИИ"),
            ("pages/glossary-ru.html", "9. Словарь терминов"),
        ],
        "footer": "© 2026 Сайт для изучения искусственного интеллекта — все права принадлежат Шмулику Шахару.",
        "phone": "Телефон", "email": "Эл. почта", "updated": "Последнее обновление: 21 августа 2026",
        "site_title": "Обучение ИИ",
    },
}

TITLES = {
    "privacy": {"he": "מדיניות פרטיות", "en": "Privacy policy", "ar": "سياسة الخصوصية", "hi": "गोपनीयता नीति", "ru": "Политика конфиденциальности"},
    "accessibility": {"he": "הצהרת נגישות", "en": "Accessibility statement", "ar": "بيان إمكانية الوصول", "hi": "सुगम्यता विवरण", "ru": "Заявление о доступности"},
    "terms": {"he": "תנאי שימוש", "en": "Terms of use", "ar": "شروط الاستخدام", "hi": "उपयोग की शर्तें", "ru": "Условия использования"},
}

BODIES = {}

BODIES["privacy", "he"] = """
<p class="legal-notice">מסמך זה הוא מידע כללי ואינו ייעוץ משפטי. לשאלות ספציפיות מומלץ לפנות לעורך דין המתמחה בהגנת הפרטיות.</p>
<h2>1. מי אנחנו</h2>
<p>האתר «AI-learning-for-ALL» מופעל בידי <strong>שחר הפקות / שמואל (שמוליק) שחר</strong>, יועץ לימודי. האתר נבנה עבור כל מי שרוצה ללמוד. דגם / גרסה: שחר הפקות AI · {ver}.</p>
<p>יצירת קשר: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a> | טלפון: <a href="tel:+972522603831">+972522603831</a>.</p>
<h2>2. איזה מידע נאסף</h2>
<p>האתר הוא אתר לימודי סטטי. אין בו הרשמה, חשבון משתמש או טופסי איסוף נתונים. אנחנו <strong>לא</strong> מפעילים כלי אנליטיקה שיווקיים ולא מוכרים מידע אישי.</p>
<ul>
<li><strong>פנייה יזומה שלכם:</strong> אם תשלחו אימייל או תתקשרו, נשמור את פרטי הקשר רק כדי להשיב.</li>
<li><strong>העדפות נגישות:</strong> נשמרות במכשיר שלכם בלבד (localStorage), לצורך תפריט הנגישות. זה מידע חיוני להנגשת השירות.</li>
<li><strong>אחסון האתר:</strong> האתר מתארח ב-GitHub Pages. ספק האחסון עשוי לרשום יומני שרת טכניים (למשל כתובת IP) לפי מדיניותו.</li>
<li><strong>צדדים שלישיים בתצוגה:</strong> גופנים מ-Google Fonts ותמונות מ-Unsplash. טעינתם עשויה להעביר מזהים טכניים (כגון IP) לספקים אלה.</li>
</ul>
<p>לפי תיקון 13 לחוק הגנת הפרטיות, התשמ"א-1981, גם מזהים מקוונים (כגון כתובת IP) עשויים להיחשב מידע אישי.</p>
<h2>3. מטרת השימוש</h2>
<p>המידע משמש רק להפעלת האתר הלימודי, להנגשה, ולמענה לפניות. אין שימוש לשיווק ישיר וללא העברה לצדדים שלישיים למטרות פרסום.</p>
<h2>4. העברה לחו"ל</h2>
<p>האירוח ב-GitHub ובגופנים/תמונות חיצוניים עשוי לכלול עיבוד מחוץ לישראל (למשל ארצות הברית). ההעברה נעשית לצורך אספקת השירות המבוקש.</p>
<h2>5. זכויותיכם</h2>
<p>לפי חוק הגנת הפרטיות ניתן לבקש עיון (סעיף 13) ותיקון או מחיקה של מידע שאינו מדויק (סעיף 14). נשיב בתוך 30 יום לפנייה לכתובת האימייל למעלה. ביטול הסכמה צריך להיות קל כמו נתינתה.</p>
<h2>6. אבטחה וילדים</h2>
<p>האתר אינו אוסף מאגרי מידע על משתמשים. התוכן לימודי ומיועד לקהל הרחב; אין לנו כוונה לאסוף מידע מילדים.</p>
<h2>7. שינויים</h2>
<p>נעדכן מדיניות זו בעת שינוי מהותי באופן איסוף או שימוש במידע. התאריך בראש העמוד מציין את העדכון האחרון.</p>
""".format(ver=VER)

BODIES["privacy", "en"] = """
<p class="legal-notice">This document is general information and is not legal advice. For specific questions, consult a privacy lawyer.</p>
<h2>1. Who we are</h2>
<p>The site «AI-learning-for-ALL» is operated by <strong>Shahar Productions / Shmuel (Sam) Shahar</strong>, an educational consultant. Built for anyone who wants to learn. Product / model: שחר הפקות AI · {ver}.</p>
<p>Contact: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a> | Phone: <a href="tel:+972522603831">+972522603831</a>.</p>
<h2>2. What data we collect</h2>
<p>This is a static educational site. There are no accounts or data-collection forms. We do <strong>not</strong> run marketing analytics and we do not sell personal data.</p>
<ul>
<li><strong>If you contact us:</strong> email or phone details are used only to reply.</li>
<li><strong>Accessibility preferences:</strong> stored only on your device (localStorage) for the accessibility menu. This is essential to provide the service accessibly.</li>
<li><strong>Hosting:</strong> GitHub Pages may keep technical server logs (for example IP addresses) under GitHub’s policy.</li>
<li><strong>Display third parties:</strong> Google Fonts and Unsplash images may receive technical identifiers (such as IP) when pages load.</li>
</ul>
<p>Under Amendment 13 to Israel’s Privacy Protection Law, 5741-1981, online identifiers such as IP addresses may count as personal data.</p>
<h2>3. Purpose</h2>
<p>Data is used only to run the learning site, accessibility features, and replies to inquiries. No direct marketing and no sale to advertisers.</p>
<h2>4. Transfers abroad</h2>
<p>Hosting and external fonts/images may involve processing outside Israel (for example the United States), as needed to provide the requested service.</p>
<h2>5. Your rights</h2>
<p>You may request access (section 13) and correction or deletion of inaccurate data (section 14). We respond within 30 days via the email above. Withdrawing consent must be as easy as giving it.</p>
<h2>6. Security and children</h2>
<p>We do not maintain user databases. Content is educational for a general audience; we do not intend to collect children’s data.</p>
<h2>7. Changes</h2>
<p>We will update this policy if collection or use changes materially. The date at the top shows the last update.</p>
""".format(ver=VER)

BODIES["privacy", "ar"] = """
<p class="legal-notice">هذه معلومات عامة وليست استشارة قانونية.</p>
<h2>1. من نحن</h2>
<p>يدير الموقع <strong>شاحار Productions / شموئيل (سام) شاحار</strong>. بُني لكل من يريد أن يتعلم. الطراز: שחר הפקות AI · {ver}.</p>
<p>التواصل: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a> | <a href="tel:+972522603831">+972522603831</a>.</p>
<h2>2. البيانات</h2>
<p>موقع تعليمي ثابت بلا حسابات. لا نبيع بيانات شخصية ولا نشغّل تحليلات تسويقية. تُحفظ تفضيلات إمكانية الوصول على جهازك فقط. قد تسجّل GitHub وGoogle Fonts وUnsplash معرّفات تقنية (مثل عنوان IP).</p>
<h2>3. الحقوق</h2>
<p>يمكن طلب الاطلاع والتصحيح بموجب قانون حماية الخصوصية الإسرائيلي. نرد خلال 30 يومًا عبر البريد الإلكتروني أعلاه.</p>
""".format(ver=VER)

BODIES["privacy", "hi"] = """
<p class="legal-notice">यह सामान्य जानकारी है, कानूनी सलाह नहीं।</p>
<h2>1. हम कौन हैं</h2>
<p>साइट <strong>शाहर प्रोडक्शन्स / शमूएल (सैम) शाहर</strong> द्वारा संचालित है। हर किसी के लिए जो सीखना चाहता है। मॉडल: שחר הפקות AI · {ver}।</p>
<p>संपर्क: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a> | <a href="tel:+972522603831">+972522603831</a>.</p>
<h2>2. डेटा</h2>
<p>यह स्थिर शैक्षिक साइट है। कोई खाता नहीं। हम व्यक्तिगत डेटा नहीं बेचते। सुगम्यता सेटिंग्स केवल आपके उपकरण पर सहेजी जाती हैं। GitHub, Google Fonts और Unsplash तकनीकी पहचानकर्ता प्राप्त कर सकते हैं।</p>
<h2>3. अधिकार</h2>
<p>इज़राइली गोपनीयता कानून के तहत पहुँच और सुधार का अनुरोध किया जा सकता है। हम ऊपर दिए ईमेल पर 30 दिनों में उत्तर देते हैं।</p>
""".format(ver=VER)

BODIES["privacy", "ru"] = """
<p class="legal-notice">Это общая информация, а не юридическая консультация.</p>
<h2>1. Кто мы</h2>
<p>Сайт ведёт <strong>Шahar Productions / Шмуэль (Сэм) Шахар</strong>. Создано для всех, кто хочет учиться. Модель: שחר הפקות AI · {ver}.</p>
<p>Связь: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a> | <a href="tel:+972522603831">+972522603831</a>.</p>
<h2>2. Какие данные собираются</h2>
<p>Это статический учебный сайт без учётных записей. Мы не продаём персональные данные и не ведём маркетинговую аналитику. Настройки доступности хранятся только на вашем устройстве. GitHub Pages, Google Fonts и Unsplash могут получать технические идентификаторы (например IP).</p>
<p>Согласно поправке 13 к Закону о защите частной жизни Израиля, онлайн-идентификаторы могут считаться персональными данными.</p>
<h2>3. Ваши права</h2>
<p>Можно запросить доступ и исправление данных. Ответ — в течение 30 дней на указанную почту.</p>
""".format(ver=VER)

BODIES["accessibility", "he"] = """
<p class="legal-notice">אנו שואפים לעמוד בתקן ישראלי 5568 ובהנחיות WCAG 2.0 ברמת AA, בהתאם לתקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), תשע"ג-2013. המסמך אינו מחליף ייעוץ משפטי ואינו מהווה אישור ביקורת נגישות חיצונית.</p>
<h2>1. התאמות באתר</h2>
<ul>
<li>מבנה סמנטי, ניווט מקלדת וסימון פוקוס נראה.</li>
<li>קישור «דלג לתוכן» וווידג'ט נגישות קבוע (אייקון) עם הגדלת טקסט, ניגודיות, גווני אפור, הדגשת קישורים, גופן קריא, עצירת אנימציה וסמן גדול.</li>
<li>העדפות נשמרות במכשיר שלכם.</li>
</ul>
<h2>2. רכז נגישות</h2>
<p><strong>שמואל (שמוליק) שחר</strong><br>
טלפון: <a href="tel:+972522603831">+972522603831</a><br>
אימייל: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
<p>אם נתקלתם בחסם נגישות — פנו אלינו ונשתדל לתת מענה סביר בהקדם.</p>
<h2>3. מגבלות ידועות</h2>
<ul>
<li>חלק מהתמונות מגיעות מ-Unsplash; תיאור חלופי קיים אך אינו תמיד מפורט.</li>
<li>גופנים נטענים מ-Google Fonts.</li>
<li>האתר מתארח ב-GitHub Pages; ממשק האחסון עצמו אינו בשליטתנו.</li>
</ul>
<h2>4. תאריך</h2>
<p>הצהרה זו עודכנה ב-21 באוגוסט 2026. נמשיך לשפר את הנגישות באופן שוטף. דגם האתר: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["accessibility", "en"] = """
<p class="legal-notice">We aim to meet Israeli Standard 5568 and WCAG 2.0 Level AA, under the Equal Rights for Persons with Disabilities (Service Accessibility Adjustments) Regulations, 5773-2013. This is not legal advice and is not an external accessibility audit certificate.</p>
<h2>1. Adjustments on this site</h2>
<ul>
<li>Semantic structure, keyboard navigation, and a visible focus mark.</li>
<li>A skip-to-content link and a persistent accessibility widget (icon) for larger text, high contrast, grayscale, highlighted links, readable font, paused animation, and a large cursor.</li>
<li>Preferences are stored on your device.</li>
</ul>
<h2>2. Accessibility contact</h2>
<p><strong>Shmuel (Sam) Shahar</strong><br>
Phone: <a href="tel:+972522603831">+972522603831</a><br>
Email: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
<p>If you hit a barrier, contact us and we will try to provide a reasonable solution promptly.</p>
<h2>3. Known limits</h2>
<ul>
<li>Some images come from Unsplash; alternative text exists but is not always detailed.</li>
<li>Fonts load from Google Fonts.</li>
<li>Hosting is GitHub Pages; that platform’s own UI is outside our control.</li>
</ul>
<h2>4. Date</h2>
<p>This statement was updated on 21 August 2026. We continue to improve accessibility. Site model: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["accessibility", "ar"] = """
<p class="legal-notice">نسعى للامتثال للمواصفة الإسرائيلية 5568 وWCAG 2.0 بمستوى AA. هذا ليس شهادة تدقيق خارجي.</p>
<h2>1. التسهيلات</h2>
<p>قائمة إمكانية وصول دائمة (أيقونة)، رابط تخطٍ إلى المحتوى، تكبير النص، تباين عالٍ، إبراز الروابط، وخط واضح. تُحفظ التفضيلات على جهازك.</p>
<h2>2. جهة الاتصال</h2>
<p><strong>شموئيل شاحار</strong> — <a href="tel:+972522603831">+972522603831</a> — <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
<h2>3. قيود</h2>
<p>صور Unsplash وخطوط Google Fonts والاستضافة على GitHub Pages قد تحدّ من التحكم الكامل.</p>
<p>الطراز: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["accessibility", "hi"] = """
<p class="legal-notice">हम इज़राइली मानक 5568 और WCAG 2.0 AA का पालन करने का प्रयास करते हैं। यह बाहरी ऑडिट प्रमाणपत्र नहीं है।</p>
<h2>1. सुविधाएँ</h2>
<p>स्थायी सुगम्यता मेनू (आइकन), मुख्य सामग्री पर जाएँ, बड़ा टेक्स्ट, उच्च कंट्रास्ट, लिंक हाइलाइट, पढ़ने योग्य फ़ॉन्ट। सेटिंग्स आपके उपकरण पर सहेजी जाती हैं।</p>
<h2>2. संपर्क</h2>
<p><strong>शमूएल शाहर</strong> — <a href="tel:+972522603831">+972522603831</a> — <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
<p>मॉडल: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["accessibility", "ru"] = """
<p class="legal-notice">Мы стремимся соответствовать израильскому стандарту 5568 и WCAG 2.0 уровня AA. Это не сертификат внешнего аудита.</p>
<h2>1. Возможности сайта</h2>
<ul>
<li>Семантика, клавиатура и видимый фокус.</li>
<li>Постоянное меню доступности (значок): крупный текст, контраст, оттенки серого, выделение ссылок, читаемый шрифт, остановка анимации, большой курсор.</li>
</ul>
<h2>2. Контакт по доступности</h2>
<p><strong>Шмуэль Шахар</strong> — <a href="tel:+972522603831">+972522603831</a> — <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
<p>Модель сайта: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["terms", "he"] = """
<p class="legal-notice">השימוש באתר מהווה הסכמה לתנאים אלה. המסמך אינו ייעוץ משפטי.</p>
<h2>1. מטרת האתר</h2>
<p>האתר מספק תוכן לימודי על בינה מלאכותית למתחילים. הוא מכין ידע כללי <strong>ואינו מחליף</strong> ייעוץ מקצועי, משפטי, רפואי או חשבונאי.</p>
<h2>2. קניין רוחני</h2>
<p>התכנים שייכים לשמוליק שחר / שחר הפקות, למעט תמונות או סימנים של צדדים שלישיים (Unsplash, שמות מוצרים כגון ChatGPT). אין להעתיק את האתר בשלמותו לשימוש מסחרי ללא רשות.</p>
<h2>3. דיוק המידע</h2>
<p>תחום ה-AI משתנה במהירות. אנו משתדלים לעדכן, אך ייתכנו אי-דיוקים. השימוש במידע על אחריות המשתמש בלבד.</p>
<h2>4. למי מיועד האתר</h2>
<p>האתר נבנה עבור כל מי שרוצה ללמוד.</p>
<h2>5. הגבלת אחריות</h2>
<p>במידה המרבית שמתיר הדין, לא נהיה אחראים לנזק עקיף הנובע משימוש באתר או מהסתמכות על התכנים.</p>
<h2>6. דין</h2>
<p>על תנאים אלה יחול דין מדינת ישראל. דגם האתר: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["terms", "en"] = """
<p class="legal-notice">Using the site means you accept these terms. This is not legal advice.</p>
<h2>1. Purpose</h2>
<p>The site offers beginner educational content about AI. It provides general knowledge and <strong>does not replace</strong> professional, legal, medical, or accounting advice.</p>
<h2>2. Intellectual property</h2>
<p>Content belongs to Sam Shahar / Shahar Productions, except third-party images or marks (Unsplash, product names such as ChatGPT). Do not copy the site as a whole for commercial use without permission.</p>
<h2>3. Accuracy</h2>
<p>AI changes quickly. We try to keep material current, but errors may remain. Use is at your own risk.</p>
<h2>4. Who this site is for</h2>
<p>The site was built for anyone who wants to learn.</p>
<h2>5. Liability</h2>
<p>To the fullest extent allowed by law, we are not liable for indirect damage from using the site or relying on its content.</p>
<h2>6. Law</h2>
<p>These terms are governed by the laws of the State of Israel. Site model: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["terms", "ar"] = """
<p class="legal-notice">استخدام الموقع يعني قبول هذه الشروط.</p>
<h2>1. الغرض</h2>
<p>محتوى تعليمي للمبتدئين في الذكاء الاصطناعي، ولا يُعد استشارة مهنية أو قانونية.</p>
<h2>2. الملكية</h2>
<p>المحتوى لشמוئيل شاحار / شاحار للإنتاج، باستثناء مواد الغير. لا يُنسخ الموقع كاملًا للاستخدام التجاري دون إذن.</p>
<h2>3. القانون</h2>
<p>بُني الموقع لكل من يريد أن يتعلم. يسري قانون دولة إسرائيل. الطراز: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["terms", "hi"] = """
<p class="legal-notice">साइट का उपयोग इन शर्तों की स्वीकृति है।</p>
<h2>1. उद्देश्य</h2>
<p>यह शुरुआती लोगों के लिए शैक्षिक सामग्री है, पेशेवर या कानूनी सलाह नहीं।</p>
<h2>2. स्वामित्व</h2>
<p>सामग्री शमूएल शाहर की है, तृतीय-पक्ष चित्रों को छोड़कर। बिना अनुमति व्यावसायिक पूर्ण प्रतिलिपि न करें।</p>
<h2>3. यह साइट किसके लिए है</h2>
<p>साइट हर किसी के लिए बनी है जो सीखना चाहता है। इज़राइल का कानून लागू। मॉडल: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)

BODIES["terms", "ru"] = """
<p class="legal-notice">Используя сайт, вы принимаете эти условия. Это не юридическая консультация.</p>
<h2>1. Назначение</h2>
<p>Учебные материалы об ИИ для начинающих. Это общие сведения и <strong>не заменяет</strong> профессиональную, юридическую или бухгалтерскую консультацию.</p>
<h2>2. Права</h2>
<p>Контент принадлежит Шмулику Шахару / Shahar Productions, кроме материалов третьих лиц. Не копируйте сайт целиком в коммерческих целях без разрешения.</p>
<h2>3. Право</h2>
<p>Сайт создан для всех, кто хочет учиться. Применяется право Государства Израиль. Модель: שחר הפקות AI · {ver}.</p>
""".format(ver=VER)


def lang_switcher(kind, lang):
    names = {"he": "עברית", "en": "English", "ar": "العربية", "hi": "हिन्दी", "ru": "Русский"}
    bits = []
    for code in ("he", "en", "ar", "hi", "ru"):
        suf = LANGS[code]["suffix"]
        href = kind + suf + ".html"
        label = names[code]
        if code == lang:
            bits.append('<span class="lang-active" aria-current="page">%s</span>' % label)
        else:
            bits.append('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (href, code, code, label))
    return "\n                ".join(bits)


def render(kind, lang):
    L = LANGS[lang]
    title_page = TITLES[kind][lang]
    lessons = "\n".join(
        '                        <li><a href="%s">%s</a></li>' % (href, lab)
        for href, lab in L["lessons"]
    )
    nav_items = "".join('<li><a href="%s">%s</a></li>\n                ' % (h, lab) for h, lab in L["nav"][:2])
    extra = ('    <style>%s</style>\n' % L["extra_style"]) if L["extra_style"] else ""
    body = BODIES[kind, lang]
    return """<!DOCTYPE html>
<html lang="{html_lang}" dir="{dir}" data-version="{ver}">
<head>
    <meta charset="UTF-8">
    <meta name="version" content="{ver}">
    <meta name="application-name" content="שחר הפקות AI {ver}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" href="{icon}">
    <title>{title_page} | {site_title} · שחר הפקות AI · {ver} · {ded}</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family={font}&display=swap" rel="stylesheet">
{extra}</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">
                <a href="{home}">
                    <img src="{logoimg}" alt="" class="logo-icon">
                    <span class="logo-stack">
                        <span class="logo-text">{logo}</span>
                        <span class="logo-byline">שחר הפקות AI · {ver}</span>
                        <span class="logo-dedication">{ded}</span>
                    </span>
                </a>
            </div>
            <ul class="nav-links">
                {nav_items}<li class="dropdown">
                    <a href="{home}#topics" class="dropdown-toggle">{lessons_label}</a>
                    <ul class="dropdown-menu">
{lessons}
                    </ul>
                </li>
                <li><a href="{nav2}">{nav2lab}</a></li>
                <li><a href="{nav3}">{nav3lab}</a></li>
                <li><a href="{nav4}">{nav4lab}</a></li>
            </ul>
            <form class="nav-search" id="site-search" role="search">
                <input type="search" name="q" placeholder="{search_ph}" aria-label="{search_aria}" />
                <button type="submit" aria-label="{search_aria}">🔍</button>
            </form>
            <nav class="lang-switcher" aria-label="{lang_label}">
                {switcher}
            </nav>
            <button type="button" class="mobile-menu-btn" aria-label="{menu}"><span></span><span></span><span></span></button>
        </nav>
    </header>
    <main id="main-content" class="legal-page-wrap">
        <div class="legal-page">
            <h1>{title_page}</h1>
            <p class="legal-updated">{updated} · שחר הפקות AI · {ver}</p>
            {body}
        </div>
    </main>
    <footer class="footer">
        <div class="container">
            <p class="site-version" aria-label="version">{ver} · שחר הפקות AI · {ded}</p>
            <p>{footer}</p>
            <p class="footer-contact">{phone}: <a href="tel:+972522603831">+972522603831</a> | {email}: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
""".format(
        html_lang=L["html_lang"], dir=L["dir"], ver=VER, icon=ICON, title_page=title_page,
        site_title=L["site_title"], ded=L["ded"], font=L["font"], extra=extra, home=L["home"],
        logoimg=LOGO, logo=L["logo"], nav_items=nav_items, lessons_label=L["lessons_label"],
        lessons=lessons, nav2=L["nav"][2][0], nav2lab=L["nav"][2][1],
        nav3=L["nav"][3][0], nav3lab=L["nav"][3][1], nav4=L["nav"][4][0], nav4lab=L["nav"][4][1],
        search_ph=L["search_ph"], search_aria=L["search_aria"], lang_label=L["lang_label"],
        switcher=lang_switcher(kind, lang), menu=L["menu"], updated=L["updated"], body=body,
        footer=L["footer"], phone=L["phone"], email=L["email"],
    )


def main():
    n = 0
    for kind in ("privacy", "accessibility", "terms"):
        for lang in LANGS:
            html = render(kind, lang)
            name = kind + LANGS[lang]["suffix"] + ".html"
            (ROOT / name).write_text(html, encoding="utf-8")
            n += 1
            print(name)
    print("wrote", n)


if __name__ == "__main__":
    main()
