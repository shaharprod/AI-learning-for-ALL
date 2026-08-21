# -*- coding: utf-8 -*-
"""Generate Arabic + Hindi lesson/search pages for AI learning site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

LESSONS = [
    ("intro-to-ai", "1"),
    ("ai-history", "2"),
    ("machine-learning", "3"),
    ("ai-daily-life", "4"),
    ("ai-tools", "5"),
    ("prompt-engineering", "6"),
    ("ai-ethics", "7"),
    ("ai-future", "8"),
    ("glossary", "9"),
]

# ---- Arabic chrome & lesson bodies ----
AR = {
    "font": "Noto+Sans+Arabic:wght@300;400;500;700",
    "font_family": "'Noto Sans Arabic', sans-serif",
    "dir": "rtl",
    "lang": "ar",
    "logo": "AI-learning-for-ALL",
    "byline": "שחר הפקות AI · B0.14",
    "home": "الرئيسية",
    "lessons": "الدروس ▾",
    "glossary_nav": "القاموس",
    "tools_nav": "الأدوات",
    "about": "عن الموقع",
    "search_ph": "بحث...",
    "search_aria": "بحث",
    "menu": "القائمة",
    "lang_aria": "اختيار اللغة",
    "active": "العربية",
    "footer": "© 2026 تعلّم الذكاء الاصطناعي – جميع الحقوق محفوظة. سام شاحار – مستشار تعليمي.",
    "contact": "هاتف",
    "email": "بريد",
    "read_more_prev": "السابق",
    "next": "التالي",
    "minutes": "دقائق قراءة",
    "beginner": "مستوى: مبتدئون",
    "lesson_titles": {
        "intro-to-ai": "مقدمة في الذكاء الاصطناعي",
        "ai-history": "تاريخ الذكاء الاصطناعي",
        "machine-learning": "تعلّم الآلة",
        "ai-daily-life": "الذكاء الاصطناعي في الحياة اليومية",
        "ai-tools": "أدوات عملية",
        "prompt-engineering": "هندسة الأوامر",
        "ai-ethics": "أخلاقيات الذكاء الاصطناعي",
        "ai-future": "مستقبل الذكاء الاصطناعي",
        "glossary": "قاموس المصطلحات",
    },
    "lesson_menu": [
        ("intro-to-ai", "1. مقدمة في الذكاء الاصطناعي"),
        ("ai-history", "2. تاريخ الذكاء الاصطناعي"),
        ("machine-learning", "3. تعلّم الآلة"),
        ("ai-daily-life", "4. الذكاء الاصطناعي في الحياة اليومية"),
        ("ai-tools", "5. أدوات عملية"),
        ("prompt-engineering", "6. هندسة الأوامر"),
        ("ai-ethics", "7. أخلاقيات الذكاء الاصطناعي"),
        ("ai-future", "8. مستقبل الذكاء الاصطناعي"),
        ("glossary", "9. قاموس المصطلحات"),
    ],
}

HI = {
    "font": "Noto+Sans+Devanagari:wght@300;400;500;700",
    "font_family": "'Noto Sans Devanagari', sans-serif",
    "dir": "ltr",
    "lang": "hi",
    "logo": "AI-learning-for-ALL",
    "byline": "שחר הפקות AI · B0.14",
    "home": "होम",
    "lessons": "पाठ ▾",
    "glossary_nav": "शब्दावली",
    "tools_nav": "उपकरण",
    "about": "परिचय",
    "search_ph": "खोजें...",
    "search_aria": "खोज",
    "menu": "मेनू",
    "lang_aria": "भाषा चुनें",
    "active": "हिन्दी",
    "footer": "© 2026 एआई सीखना – सर्वाधिकार सुरक्षित। सैम शहार – शैक्षिक सलाहकार।",
    "contact": "फ़ोन",
    "email": "ईमेल",
    "read_more_prev": "पिछला",
    "next": "अगला",
    "minutes": "मिनट पढ़ना",
    "beginner": "स्तर: शुरुआती",
    "lesson_titles": {
        "intro-to-ai": "एआई का परिचय",
        "ai-history": "एआई का इतिहास",
        "machine-learning": "मशीन लर्निंग",
        "ai-daily-life": "रोज़मर्रा की ज़िंदगी में एआई",
        "ai-tools": "व्यावहारिक उपकरण",
        "prompt-engineering": "प्रॉम्प्ट इंजीनियरिंग",
        "ai-ethics": "एआई नैतिकता",
        "ai-future": "एआई का भविष्य",
        "glossary": "शब्दावली",
    },
    "lesson_menu": [
        ("intro-to-ai", "1. एआई का परिचय"),
        ("ai-history", "2. एआई का इतिहास"),
        ("machine-learning", "3. मशीन लर्निंग"),
        ("ai-daily-life", "4. रोज़मर्रा की ज़िंदगी में एआई"),
        ("ai-tools", "5. व्यावहारिक उपकरण"),
        ("prompt-engineering", "6. प्रॉम्प्ट इंजीनियरिंग"),
        ("ai-ethics", "7. एआई नैतिकता"),
        ("ai-future", "8. एआई का भविष्य"),
        ("glossary", "9. शब्दावली"),
    ],
}

CONTENT_AR = {
    "intro-to-ai": """
                <h1>مقدمة في الذكاء الاصطناعي</h1>
                <p class="article-meta">📚 وقت القراءة: 12 دقيقة | مستوى: مبتدئون</p>
                <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=400&fit=crop" alt="ذكاء اصطناعي" class="article-header-image">
                <section>
                    <h2 id="what-is-ai">ما هو الذكاء الاصطناعي؟</h2>
                    <p>الذكاء الاصطناعي (AI) فرع من علوم الحاسوب يهتم ببناء أنظمة تستطيع أداء مهام تتطلب عادةً ذكاءً بشرياً: التعلّم، الاستدلال، حل المشكلات، فهم اللغة، والإدراك.</p>
                    <ul class="benefits-list">
                        <li><strong>التعلّم:</strong> اكتساب معرفة جديدة من التجربة</li>
                        <li><strong>الاستدلال:</strong> استخلاص استنتاجات من المعلومات</li>
                        <li><strong>حل المشكلات:</strong> إيجاد حلول في مواقف جديدة</li>
                        <li><strong>فهم اللغة:</strong> فهم وإنتاج لغة طبيعية</li>
                        <li><strong>الإدراك:</strong> التعرّف على الصور والأصوات والبيئة</li>
                    </ul>
                    <div class="info-card tip">
                        <strong>💡 الفرق عن البرمجة العادية:</strong>
                        <p>في البرمجة العادية يكتب المطوّر قواعد صريحة. في الذكاء الاصطناعي يتعلّم النظام من أمثلة وبيانات.</p>
                    </div>
                </section>
                <section>
                    <h2 id="how-ai-works">كيف يعمل؟ الفكرة الأساسية</h2>
                    <p>معظم أنظمة اليوم تعتمد على <strong>التعلّم من الأمثلة</strong>: بيانات ← تدريب ← نموذج ← استخدام على أمثلة جديدة.</p>
                    <div class="example-box">
                        <h4>مثال: التعرّف على القطط</h4>
                        <ol>
                            <li>عرض ملايين الصور (مع قطط وبدونها)</li>
                            <li>اكتشاف أنماط مشتركة</li>
                            <li>بناء نموذج داخلي لـ«ما هو القط»</li>
                            <li>تصنيف صور جديدة</li>
                        </ol>
                    </div>
                </section>
                <section>
                    <h2 id="types">أنواع الذكاء الاصطناعي</h2>
                    <ul class="benefits-list">
                        <li><strong>ضيق (ANI):</strong> متخصّص في مهمة واحدة (مثل التوصيات أو الترجمة)</li>
                        <li><strong>عام (AGI):</strong> قدرات واسعة شبيهة بالإنسان — ما زال هدفاً بحثياً</li>
                        <li><strong>تعلّم آلة / تعلّم عميق:</strong> طرق شائعة لبناء أنظمة اليوم</li>
                    </ul>
                </section>
                <section>
                    <h2 id="takeaway">خلاصة</h2>
                    <p>الذكاء الاصطناعي أداة قوية تتعلّم من البيانات. فهم الأساسيات يساعدكم على استخدام الأدوات بوعي ومسؤولية.</p>
                </section>
""",
    "ai-history": """
                <h1>تاريخ الذكاء الاصطناعي</h1>
                <p class="article-meta">📅 الدرس 2 – من بابيج حتى 2026</p>
                <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=400&fit=crop" alt="تاريخ الحوسبة" class="article-header-image">
                <section>
                    <h2 id="intro">مقدمة</h2>
                    <p>فكرة الآلات التي تحسب و«تفكّر» سبقت الحاسوب الإلكتروني. فيما يلي محطات أساسية.</p>
                </section>
                <section>
                    <h2 id="timeline">خط زمني مختصر</h2>
                    <div class="timeline">
                        <div class="timeline-item"><span class="year">1837</span><p><strong>بابيج ولافليس</strong> – فكرة آلة حساب قابلة للبرمجة.</p></div>
                        <div class="timeline-item"><span class="year">1950</span><p><strong>آلان تورينغ</strong> – اختبار تورينغ وسؤال «هل يمكن للآلات أن تفكّر؟»</p></div>
                        <div class="timeline-item"><span class="year">1956</span><p><strong>دارتموث</strong> – ولادة مصطلح الذكاء الاصطناعي.</p></div>
                        <div class="timeline-item"><span class="year">1997</span><p><strong>Deep Blue</strong> يهزم كاسباروف في الشطرنج.</p></div>
                        <div class="timeline-item"><span class="year">2012+</span><p>طفرة التعلّم العميق ورؤية الحاسوب.</p></div>
                        <div class="timeline-item"><span class="year">2022–2026</span><p>نماذج لغوية كبيرة (مثل ChatGPT) تصبح أدوات يومية.</p></div>
                    </div>
                </section>
""",
    "machine-learning": """
                <h1>تعلّم الآلة</h1>
                <p class="article-meta">🔮 الدرس 3 | مبتدئون</p>
                <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=400&fit=crop" alt="تعلم آلة" class="article-header-image">
                <section>
                    <h2 id="what">ما هو تعلّم الآلة؟</h2>
                    <p>تعلّم الآلة (ML) يمكّن الحاسوب من تحسين أدائه عبر البيانات دون برمجة كل قاعدة يدوياً.</p>
                </section>
                <section>
                    <h2 id="types">أنواع شائعة</h2>
                    <ul class="benefits-list">
                        <li><strong>بإشراف:</strong> أمثلة مع تسميات صحيحة (تصنيف، تنبؤ)</li>
                        <li><strong>بدون إشراف:</strong> اكتشاف أنماط وتجميعات بدون تسميات</li>
                        <li><strong>تعزيز:</strong> التعلّم عبر مكافآت وعقوبات</li>
                        <li><strong>تعلّم عميق:</strong> شبكات عصبية متعددة الطبقات</li>
                    </ul>
                </section>
                <section>
                    <h2 id="data">أهمية البيانات</h2>
                    <p>جودة البيانات وحجمها يحدّدان جودة النموذج. بيانات منحازة تنتج قرارات منحازة.</p>
                </section>
""",
    "ai-daily-life": """
                <h1>الذكاء الاصطناعي في الحياة اليومية</h1>
                <p class="article-meta">💡 الدرس 4</p>
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=400&fit=crop" alt="حياة يومية" class="article-header-image">
                <section>
                    <h2 id="examples">أين نلتقي به؟</h2>
                    <ul class="benefits-list">
                        <li>توصيات أفلام وموسيقى</li>
                        <li>مساعدات صوتية وترجمة فورية</li>
                        <li>كاميرات الهاتف وتحسين الصور</li>
                        <li>التنقّل والخرائط وتقدير الوقت</li>
                        <li>كشف الاحتيال في البنوك</li>
                        <li>تصفية البريد المزعج</li>
                    </ul>
                </section>
                <section>
                    <h2 id="note">ملاحظة</h2>
                    <p>كثيراً ما يعمل الذكاء الاصطناعي «خلف الكواليس». إدراك وجوده يساعد على فهم الخصوصية والاختيارات الرقمية.</p>
                </section>
""",
    "ai-tools": """
                <h1>أدوات عملية للذكاء الاصطناعي</h1>
                <p class="article-meta">🛠️ الدرس 5</p>
                <img src="https://images.unsplash.com/photo-1676299080920-2c3b9f0b0b0b?w=800&h=400&fit=crop" alt="أدوات" class="article-header-image">
                <section>
                    <h2 id="chat">محادثات ونصوص</h2>
                    <ul class="benefits-list">
                        <li><strong>ChatGPT / Claude / Gemini:</strong> كتابة، تلخيص، شرح، عصف ذهني</li>
                        <li>استخدموا أوامر واضحة وحدّدوا الجمهور والنبرة</li>
                    </ul>
                </section>
                <section>
                    <h2 id="media">صور ووسائط</h2>
                    <p>أدوات توليد الصور والفيديو تساعد في التصميم والتعليم — راجعوا دائماً الحقوق والدقة.</p>
                </section>
                <section>
                    <h2 id="tips">نصائح استخدام آمن</h2>
                    <ul class="benefits-list">
                        <li>لا تشاركوا أسراراً أو بيانات حسّاسة</li>
                        <li>تحققوا من الحقائق المهمة</li>
                        <li>اعتبروا المخرجات مسودة تحتاج مراجعة بشرية</li>
                    </ul>
                </section>
""",
    "prompt-engineering": """
                <h1>هندسة الأوامر (Prompt Engineering)</h1>
                <p class="article-meta">✍️ الدرس 6</p>
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop" alt="أوامر" class="article-header-image">
                <section>
                    <h2 id="what">ما هو الأمر (Prompt)؟</h2>
                    <p>الأمر هو التعليمات التي تعطونها للنموذج. كلما كان أوضح وأكثر تحديداً، تحسّنت النتيجة.</p>
                </section>
                <section>
                    <h2 id="formula">صيغة مفيدة</h2>
                    <div class="example-box">
                        <ol>
                            <li><strong>الدور:</strong> من هو المساعد؟ (معلّم، محرّر...)</li>
                            <li><strong>المهمة:</strong> ماذا تريدون بالضبط؟</li>
                            <li><strong>السياق:</strong> جمهور، طول، نبرة، قيود</li>
                            <li><strong>الشكل:</strong> قائمة، جدول، خطوات...</li>
                        </ol>
                    </div>
                </section>
                <section>
                    <h2 id="example">مثال</h2>
                    <p>«أنت معلّم للمرحلة الإعدادية. اشرح تعلّم الآلة بثلاث فقرات قصيرة وبالعربية الفصحى البسيطة، مع مثال من الحياة اليومية.»</p>
                </section>
""",
    "ai-ethics": """
                <h1>أخلاقيات الذكاء الاصطناعي</h1>
                <p class="article-meta">⚖️ الدرس 7</p>
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=400&fit=crop" alt="أخلاقيات" class="article-header-image">
                <section>
                    <h2 id="topics">قضايا أساسية</h2>
                    <ul class="benefits-list">
                        <li><strong>الخصوصية:</strong> من يملك البيانات وكيف تُستخدم؟</li>
                        <li><strong>التحيّز:</strong> النماذج قد تعكس تحيّزات البيانات</li>
                        <li><strong>الشفافية:</strong> هل نفهم لماذا اتُّخذ قرار؟</li>
                        <li><strong>العمل والمجتمع:</strong> أتمتة، مهارات جديدة، وعدالة</li>
                        <li><strong>المعلومات المضلّلة:</strong> نصوص وصور مزيفة</li>
                    </ul>
                </section>
                <section>
                    <h2 id="practice">ممارسة مسؤولة</h2>
                    <p>اسألوا دائماً: هل الاستخدام قانوني؟ هل يحترم الناس؟ هل يمكن التحقق من النتيجة؟</p>
                </section>
""",
    "ai-future": """
                <h1>مستقبل الذكاء الاصطناعي</h1>
                <p class="article-meta">🚀 الدرس 8</p>
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=400&fit=crop" alt="مستقبل" class="article-header-image">
                <section>
                    <h2 id="trends">اتجاهات</h2>
                    <ul class="benefits-list">
                        <li>مساعدات أذكى في العمل والتعليم والرعاية</li>
                        <li>تكامل أعمق مع الهواتف والخدمات</li>
                        <li>تنظيم وقوانين حول السلامة والخصوصية</li>
                        <li>حاجة متزايدة لمهارات نقدية وبشرية</li>
                    </ul>
                </section>
                <section>
                    <h2 id="you">ماذا يعني لكم؟</h2>
                    <p>تعلّم الأساسيات والقدرة على صياغة أوامر جيدة أصبحا مهارات عامة — مثل معرفة القراءة الرقمية.</p>
                </section>
""",
    "glossary": """
                <h1>قاموس مصطلحات الذكاء الاصطناعي</h1>
                <p class="article-meta">📖 الدرس 9</p>
                <section>
                    <h2 id="a">مصطلحات أساسية</h2>
                    <ul class="benefits-list">
                        <li><strong>AI:</strong> ذكاء اصطناعي</li>
                        <li><strong>ML:</strong> تعلّم آلة</li>
                        <li><strong>NLP:</strong> معالجة لغة طبيعية</li>
                        <li><strong>LLM:</strong> نموذج لغوي كبير</li>
                        <li><strong>Prompt:</strong> أمر / تعليمات للنموذج</li>
                        <li><strong>Training:</strong> تدريب النموذج على بيانات</li>
                        <li><strong>Inference:</strong> استخدام النموذج بعد التدريب</li>
                        <li><strong>Hallucination:</strong> مخرجات تبدو صحيحة لكنها خاطئة</li>
                        <li><strong>Bias:</strong> تحيّز في البيانات أو النتائج</li>
                        <li><strong>Fine-tuning:</strong> ضبط نموذج جاهز على مهمة أضيق</li>
                    </ul>
                </section>
""",
}

CONTENT_HI = {
    "intro-to-ai": """
                <h1>कृत्रिम बुद्धिमत्ता का परिचय</h1>
                <p class="article-meta">📚 पढ़ने का समय: 12 मिनट | स्तर: शुरुआती</p>
                <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=400&fit=crop" alt="एआई" class="article-header-image">
                <section>
                    <h2 id="what-is-ai">एआई क्या है?</h2>
                    <p>कृत्रिम बुद्धिमत्ता (AI) कंप्यूटर विज्ञान की शाखा है जो ऐसी प्रणालियाँ बनाती है जो आमतौर पर मानवीय बुद्धि वाले काम कर सकें: सीखना, तर्क, समस्या-समाधान, भाषा समझना और धारणा।</p>
                    <ul class="benefits-list">
                        <li><strong>सीखना:</strong> अनुभव से नया ज्ञान</li>
                        <li><strong>तर्क:</strong> जानकारी से निष्कर्ष</li>
                        <li><strong>समस्या-समाधान:</strong> नई स्थितियों में समाधान</li>
                        <li><strong>भाषा:</strong> प्राकृतिक भाषा समझना और बनाना</li>
                        <li><strong>धारणा:</strong> चित्र, ध्वनि और परिवेश पहचानना</li>
                    </ul>
                    <div class="info-card tip">
                        <strong>💡 सामान्य प्रोग्रामिंग से अंतर:</strong>
                        <p>सामान्य प्रोग्रामिंग में स्पष्ट नियम लिखे जाते हैं। एआई उदाहरणों और डेटा से सीखता है।</p>
                    </div>
                </section>
                <section>
                    <h2 id="how-ai-works">यह कैसे काम करता है?</h2>
                    <p>अधिकांश आधुनिक प्रणालियाँ <strong>उदाहरणों से सीखने</strong> पर आधारित हैं: डेटा → प्रशिक्षण → मॉडल → नई स्थितियों में उपयोग।</p>
                </section>
                <section>
                    <h2 id="types">एआई के प्रकार</h2>
                    <ul class="benefits-list">
                        <li><strong>संकीर्ण (ANI):</strong> एक विशिष्ट कार्य</li>
                        <li><strong>सामान्य (AGI):</strong> व्यापक मानवीय-जैसी क्षमताएँ — अभी शोध लक्ष्य</li>
                        <li><strong>मशीन लर्निंग / डीप लर्निंग:</strong> आज की मुख्य विधियाँ</li>
                    </ul>
                </section>
""",
    "ai-history": """
                <h1>एआई का इतिहास</h1>
                <p class="article-meta">📅 पाठ 2</p>
                <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=400&fit=crop" alt="इतिहास" class="article-header-image">
                <section>
                    <h2 id="timeline">संक्षिप्त समयरेखा</h2>
                    <div class="timeline">
                        <div class="timeline-item"><span class="year">1837</span><p><strong>बैबेज और लवलेस</strong> – प्रोग्राम योग्य गणना मशीन का विचार।</p></div>
                        <div class="timeline-item"><span class="year">1950</span><p><strong>एलन ट्यूरिंग</strong> – ट्यूरिंग टेस्ट।</p></div>
                        <div class="timeline-item"><span class="year">1956</span><p><strong>डार्टमाउथ</strong> – «Artificial Intelligence» शब्द का जन्म।</p></div>
                        <div class="timeline-item"><span class="year">1997</span><p><strong>Deep Blue</strong> शतरंज में जीत।</p></div>
                        <div class="timeline-item"><span class="year">2012+</span><p>डीप लर्निंग का उदय।</p></div>
                        <div class="timeline-item"><span class="year">2022–2026</span><p>बड़े भाषा मॉडल रोज़मर्रा के उपकरण बने।</p></div>
                    </div>
                </section>
""",
    "machine-learning": """
                <h1>मशीन लर्निंग</h1>
                <p class="article-meta">🔮 पाठ 3</p>
                <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=400&fit=crop" alt="मशीन लर्निंग" class="article-header-image">
                <section>
                    <h2 id="what">क्या है?</h2>
                    <p>मशीन लर्निंग (ML) से कंप्यूटर डेटा से प्रदर्शन सुधारता है — हर नियम हाथ से लिखे बिना।</p>
                </section>
                <section>
                    <h2 id="types">मुख्य प्रकार</h2>
                    <ul class="benefits-list">
                        <li><strong>सुपरवाइज़्ड:</strong> लेबल वाले उदाहरण</li>
                        <li><strong>अनसुपरवाइज़्ड:</strong> पैटर्न खोजना</li>
                        <li><strong>रीइनफोर्समेंट:</strong> इनाम/दंड से सीखना</li>
                        <li><strong>डीप लर्निंग:</strong> बहु-परतीय न्यूरल नेटवर्क</li>
                    </ul>
                </section>
""",
    "ai-daily-life": """
                <h1>रोज़मर्रा की ज़िंदगी में एआई</h1>
                <p class="article-meta">💡 पाठ 4</p>
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=400&fit=crop" alt="रोज़मर्रा" class="article-header-image">
                <section>
                    <h2 id="examples">कहाँ मिलता है?</h2>
                    <ul class="benefits-list">
                        <li>फ़िल्म/संगीत सुझाव</li>
                        <li>वॉइस असिस्टेंट और अनुवाद</li>
                        <li>फ़ोन कैमरा सुधार</li>
                        <li>मानचित्र और यातायात अनुमान</li>
                        <li>बैंकिंग धोखाधड़ी पहचान</li>
                        <li>स्पैम फ़िल्टर</li>
                    </ul>
                </section>
""",
    "ai-tools": """
                <h1>व्यावहारिक एआई उपकरण</h1>
                <p class="article-meta">🛠️ पाठ 5</p>
                <section>
                    <h2 id="chat">चैट और लेखन</h2>
                    <ul class="benefits-list">
                        <li><strong>ChatGPT / Claude / Gemini:</strong> लेखन, सारांश, विचार-मंथन</li>
                        <li>स्पष्ट प्रॉम्प्ट लिखें; दर्शक और स्वर बताएँ</li>
                    </ul>
                </section>
                <section>
                    <h2 id="tips">सुरक्षित उपयोग</h2>
                    <ul class="benefits-list">
                        <li>संवेदनशील डेटा साझा न करें</li>
                        <li>महत्वपूर्ण तथ्यों की जाँच करें</li>
                        <li>आउटपुट को मसौदा मानें</li>
                    </ul>
                </section>
""",
    "prompt-engineering": """
                <h1>प्रॉम्प्ट इंजीनियरिंग</h1>
                <p class="article-meta">✍️ पाठ 6</p>
                <section>
                    <h2 id="what">प्रॉम्प्ट क्या है?</h2>
                    <p>प्रॉम्प्ट वह निर्देश है जो आप मॉडल को देते हैं। जितना स्पष्ट, उतना बेहतर परिणाम।</p>
                </section>
                <section>
                    <h2 id="formula">उपयोगी सूत्र</h2>
                    <div class="example-box">
                        <ol>
                            <li><strong>भूमिका</strong></li>
                            <li><strong>कार्य</strong></li>
                            <li><strong>संदर्भ</strong> (दर्शक, लंबाई, स्वर)</li>
                            <li><strong>प्रारूप</strong> (सूची, तालिका, चरण)</li>
                        </ol>
                    </div>
                </section>
""",
    "ai-ethics": """
                <h1>एआई नैतिकता</h1>
                <p class="article-meta">⚖️ पाठ 7</p>
                <section>
                    <h2 id="topics">मुख्य मुद्दे</h2>
                    <ul class="benefits-list">
                        <li><strong>गोपनीयता</strong></li>
                        <li><strong>पक्षपात (Bias)</strong></li>
                        <li><strong>पारदर्शिता</strong></li>
                        <li><strong>रोज़गार और समाज</strong></li>
                        <li><strong>गलत सूचना</strong></li>
                    </ul>
                </section>
""",
    "ai-future": """
                <h1>एआई का भविष्य</h1>
                <p class="article-meta">🚀 पाठ 8</p>
                <section>
                    <h2 id="trends">रुझान</h2>
                    <ul class="benefits-list">
                        <li>काम, शिक्षा और स्वास्थ्य में स्मार्ट सहायक</li>
                        <li>नियम और सुरक्षा पर ज़्यादा ध्यान</li>
                        <li>मानवीय और आलोचनात्मक कौशल की माँग</li>
                    </ul>
                </section>
""",
    "glossary": """
                <h1>एआई शब्दावली</h1>
                <p class="article-meta">📖 पाठ 9</p>
                <section>
                    <h2 id="a">मुख्य शब्द</h2>
                    <ul class="benefits-list">
                        <li><strong>AI:</strong> कृत्रिम बुद्धिमत्ता</li>
                        <li><strong>ML:</strong> मशीन लर्निंग</li>
                        <li><strong>NLP:</strong> प्राकृतिक भाषा प्रसंस्करण</li>
                        <li><strong>LLM:</strong> बड़ा भाषा मॉडल</li>
                        <li><strong>Prompt:</strong> मॉडल को दिया निर्देश</li>
                        <li><strong>Training:</strong> डेटा पर प्रशिक्षण</li>
                        <li><strong>Hallucination:</strong> गलत पर विश्वसनीय लगने वाला उत्तर</li>
                        <li><strong>Bias:</strong> पक्षपात</li>
                    </ul>
                </section>
""",
}


def lang_switcher(meta, slug, suffix):
    he = f"{slug}.html"
    en = f"{slug}-en.html"
    ar = f"{slug}-ar.html"
    hi = f"{slug}-hi.html"
    if suffix == "ar":
        return f'''<nav class="lang-switcher" aria-label="{meta['lang_aria']}">
                <a href="{he}" hreflang="he" lang="he">עברית</a>
                <a href="{en}" hreflang="en" lang="en">English</a>
                <span class="lang-active" aria-current="page">{meta['active']}</span>
                <a href="{hi}" hreflang="hi" lang="hi">हिन्दी</a>
            </nav>'''
    return f'''<nav class="lang-switcher" aria-label="{meta['lang_aria']}">
                <a href="{he}" hreflang="he" lang="he">עברית</a>
                <a href="{en}" hreflang="en" lang="en">English</a>
                <a href="{ar}" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">{meta['active']}</span>
            </nav>'''


def lesson_menu_html(meta, suffix):
    items = []
    for slug, label in meta["lesson_menu"]:
        items.append(f'<li><a href="{slug}-{suffix}.html">{label}</a></li>')
    return "\n                        ".join(items)


def page_nav(meta, suffix, slug):
    idx = f"../index-{suffix}.html"
    return f'''            <ul class="nav-links">
                <li><a href="{idx}">{meta['home']}</a></li>
                <li class="dropdown">
                    <a href="{idx}#topics" class="dropdown-toggle">{meta['lessons']}</a>
                    <ul class="dropdown-menu">
                        {lesson_menu_html(meta, suffix)}
                    </ul>
                </li>
                <li><a href="glossary-{suffix}.html">{meta['glossary_nav']}</a></li>
                <li><a href="ai-tools-{suffix}.html">{meta['tools_nav']}</a></li>
                <li><a href="{idx}#about">{meta['about']}</a></li>
            </ul>'''


def article_nav(meta, suffix, slug):
    slugs = [s for s, _ in LESSONS]
    i = slugs.index(slug)
    prev_html = ""
    next_html = ""
    if i > 0:
        ps = slugs[i - 1]
        prev_html = f'<a href="{ps}-{suffix}.html" class="btn">→ {meta["read_more_prev"]}: {meta["lesson_titles"][ps]}</a>'
    if i < len(slugs) - 1:
        ns = slugs[i + 1]
        next_html = f'<a href="{ns}-{suffix}.html" class="btn btn-primary">{meta["next"]}: {meta["lesson_titles"][ns]} ←</a>'
    return f'<div class="article-nav">{prev_html}{next_html}</div>'


def build_lesson(meta, content_map, suffix, slug):
    title = meta["lesson_titles"][slug]
    body = content_map[slug]
    extra_style = ""
    if suffix == "hi":
        extra_style = "body { direction: ltr; } "
    extra_style += f"body {{ font-family: {meta['font_family']}; }}"
    html = f'''<!DOCTYPE html>
<html lang="{meta['lang']}" dir="{meta['dir']}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {meta['logo']} · {meta['byline']}</title>
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="article.css">
    <link href="https://fonts.googleapis.com/css2?family={meta['font']}&display=swap" rel="stylesheet">
    <style>{extra_style}</style>
</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">
                <a href="../index-{suffix}.html">
                    <img src="../images/colorful%20digital%20media%20sy.png" alt="" class="logo-icon">
                    <span class="logo-stack">
                        <span class="logo-text">{meta['logo']}</span>
                        <span class="logo-byline">{meta['byline']}</span>
                    </span>
                </a>
            </div>
{page_nav(meta, suffix, slug)}
            <form class="nav-search" id="site-search" role="search">
                <input type="search" name="q" placeholder="{meta['search_ph']}" aria-label="{meta['search_aria']}" />
                <button type="submit" aria-label="{meta['search_aria']}">🔍</button>
            </form>
            {lang_switcher(meta, slug, suffix)}
            <button type="button" class="mobile-menu-btn" aria-label="{meta['menu']}"><span></span><span></span><span></span></button>
        </nav>
    </header>
    <main class="article">
        <div class="container">
            <div class="breadcrumb"><a href="../index-{suffix}.html">{meta['home']}</a> / <span>{title}</span></div>
            <article class="article-content">
{body}
                {article_nav(meta, suffix, slug)}
            </article>
        </div>
    </main>
    <footer class="footer">
        <div class="container">
            <p>{meta['footer']}</p>
            <p class="footer-contact">{meta['contact']}: <a href="tel:+972522603831">+972522603831</a> | {meta['email']}: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
        </div>
    </footer>
    <script src="../script.js"></script>
</body>
</html>
'''
    path = PAGES / f"{slug}-{suffix}.html"
    path.write_text(html, encoding="utf-8")
    print("wrote", path.name)


def build_search(meta, suffix):
    titles = meta["lesson_titles"]
    pages_js = [
        f"        {{ url: 'index-{suffix}.html', title: '{meta['home']}' }}",
    ]
    for slug, _ in LESSONS:
        pages_js.append(f"        {{ url: 'pages/{slug}-{suffix}.html', title: '{titles[slug]}' }}")
    pages_block = ",\n".join(pages_js)
    if suffix == "ar":
        h1, ph, loading, nores, enter, jump = (
            "البحث عن كلمات ومصطلحات",
            "أدخل كلمة أو مصطلحاً...",
            "جاري البحث...",
            "لا نتائج لـ",
            "أدخل كلمة أو مصطلحاً للبحث.",
            "↵ الانتقال إلى القسم",
        )
        submit_url = "search-ar.html"
        he, en, ar, hi = "search.html", "search-en.html", "search-ar.html", "search-hi.html"
        switcher = f'''<nav class="lang-switcher" aria-label="{meta['lang_aria']}">
                <a href="{he}" hreflang="he" lang="he">עברית</a>
                <a href="{en}" hreflang="en" lang="en">English</a>
                <span class="lang-active" aria-current="page">{meta['active']}</span>
                <a href="{hi}" hreflang="hi" lang="hi">हिन्दी</a>
            </nav>'''
        style_extra = f"body {{ font-family: {meta['font_family']}; }}"
        border = ""
    else:
        h1, ph, loading, nores, enter, jump = (
            "शब्द और शब्द खोजें",
            "कोई शब्द या पद लिखें...",
            "खोज जारी...",
            "कोई परिणाम नहीं:",
            "खोजने के लिए शब्द लिखें।",
            "↵ अनुभाग पर जाएँ",
        )
        submit_url = "search-hi.html"
        he, en, ar, hi = "search.html", "search-en.html", "search-ar.html", "search-hi.html"
        switcher = f'''<nav class="lang-switcher" aria-label="{meta['lang_aria']}">
                <a href="{he}" hreflang="he" lang="he">עברית</a>
                <a href="{en}" hreflang="en" lang="en">English</a>
                <a href="{ar}" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">{meta['active']}</span>
            </nav>'''
        style_extra = f"body {{ direction: ltr; font-family: {meta['font_family']}; }} .search-results .result-item {{ border-right: none; border-left: 4px solid var(--primary); }}"
        border = ""

    menu = lesson_menu_html(meta, suffix).replace(f'href="', f'href="pages/')
    # fix double pages/ if any
    menu = menu.replace('href="pages/pages/', 'href="pages/')

    html = f'''<!DOCTYPE html>
<html lang="{meta['lang']}" dir="{meta['dir']}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{h1} | {meta['logo']} · {meta['byline']}</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family={meta['font']}&display=swap" rel="stylesheet">
    <style>
        .search-page {{ padding: 6rem 0 4rem; }}
        .search-page h1 {{ margin-bottom: 1rem; text-align: center; }}
        .search-form-wrap {{ max-width: 500px; margin: 0 auto 2rem; }}
        .search-form-wrap input {{ width: 100%; padding: 0.75rem 1rem; font-size: 1.1rem; border-radius: var(--radius-sm); border: 1px solid var(--border); }}
        .search-results {{ max-width: 700px; margin: 0 auto; }}
        .search-results .result-item {{ margin-bottom: 1.5rem; padding: 1rem; background: var(--surface); border-radius: var(--radius-sm); border-right: 4px solid var(--primary); }}
        .search-results .result-item h3 a {{ color: var(--primary); }}
        .search-results .snippet {{ color: var(--text-light); }}
        .search-results .no-results, .search-results .loading {{ text-align: center; padding: 2rem; color: var(--text-light); }}
        {style_extra}
    </style>
</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">
                <a href="index-{suffix}.html">
                    <img src="images/colorful%20digital%20media%20sy.png" alt="" class="logo-icon">
                    <span class="logo-stack">
                        <span class="logo-text">{meta['logo']}</span>
                        <span class="logo-byline">{meta['byline']}</span>
                    </span>
                </a>
            </div>
            <ul class="nav-links">
                <li><a href="index-{suffix}.html">{meta['home']}</a></li>
                <li class="dropdown">
                    <a href="index-{suffix}.html#topics" class="dropdown-toggle">{meta['lessons']}</a>
                    <ul class="dropdown-menu">
                        {menu}
                    </ul>
                </li>
                <li><a href="pages/glossary-{suffix}.html">{meta['glossary_nav']}</a></li>
                <li><a href="pages/ai-tools-{suffix}.html">{meta['tools_nav']}</a></li>
                <li><a href="index-{suffix}.html#about">{meta['about']}</a></li>
            </ul>
            <form class="nav-search" id="site-search" role="search">
                <input type="search" name="q" placeholder="{meta['search_ph']}" aria-label="{meta['search_aria']}" />
                <button type="submit" aria-label="{meta['search_aria']}">🔍</button>
            </form>
            {switcher}
            <button type="button" class="mobile-menu-btn" aria-label="{meta['menu']}"><span></span><span></span><span></span></button>
        </nav>
    </header>
    <main class="section search-page">
        <div class="container">
            <h1>{h1}</h1>
            <div class="search-form-wrap">
                <form id="search-form" role="search">
                    <input type="search" name="q" id="search-query" placeholder="{ph}" aria-label="{meta['search_aria']}" autofocus />
                </form>
            </div>
            <div id="search-results" class="search-results"></div>
        </div>
    </main>
    <footer class="footer">
        <div class="container">
            <p>{meta['footer']}</p>
            <p class="footer-contact">{meta['contact']}: <a href="tel:+972522603831">+972522603831</a> | {meta['email']}: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>
        </div>
    </footer>
    <script>
(function () {{
    var PAGES = [
{pages_block}
    ];
    var resultsEl = document.getElementById('search-results');
    var form = document.getElementById('search-form');
    var input = document.getElementById('search-query');
    var basePath = (function () {{
        if (window.location.protocol === 'file:') return '';
        var p = window.location.pathname || '';
        return p.indexOf('/') === -1 ? '' : p.replace(/\\/[^/]*$/, '/');
    }})();
    function getQuery() {{
        return (new URLSearchParams(window.location.search).get('q') || '').trim();
    }}
    function runSearch(q) {{
        if (!q) {{ resultsEl.innerHTML = '<p class="no-results">{enter}</p>'; return; }}
        resultsEl.innerHTML = '<p class="loading">{loading}</p>';
        if (input) input.value = q;
        var found = [];
        Promise.all(PAGES.map(function (p) {{
            return fetch(basePath + p.url).then(function (r) {{ return r.text(); }}).then(function (html) {{
                var doc = new DOMParser().parseFromString(html, 'text/html');
                [].forEach.call(doc.querySelectorAll('script, style'), function (el) {{ el.remove(); }});
                var text = ((doc.querySelector('main') || doc.body).innerText || '').replace(/\\s+/g, ' ');
                var idx = text.toLowerCase().indexOf(q.toLowerCase());
                if (idx !== -1) {{
                    var sn = text.slice(Math.max(0, idx - 80), idx + q.length + 80);
                    found.push({{ title: p.title, url: p.url, snippet: sn }});
                }}
            }}).catch(function () {{}});
        }})).then(function () {{
            if (!found.length) {{ resultsEl.innerHTML = '<p class="no-results">{nores} “' + q + '”.</p>'; return; }}
            resultsEl.innerHTML = found.map(function (r) {{
                return '<div class="result-item"><h3><a href="' + r.url + '">' + r.title + '</a></h3><p class="snippet">' + r.snippet + '</p></div>';
            }}).join('');
        }});
    }}
    if (form) form.addEventListener('submit', function (e) {{
        e.preventDefault();
        var q = (input && input.value || '').trim();
        if (q) window.location.href = '{submit_url}?q=' + encodeURIComponent(q);
    }});
    runSearch(getQuery());
}})();
    </script>
    <script src="script.js"></script>
</body>
</html>
'''
    path = ROOT / f"search-{suffix}.html"
    path.write_text(html, encoding="utf-8")
    print("wrote", path.name)


def main():
    for slug, _ in LESSONS:
        build_lesson(AR, CONTENT_AR, "ar", slug)
        build_lesson(HI, CONTENT_HI, "hi", slug)
    build_search(AR, "ar")
    build_search(HI, "hi")
    print("done")


if __name__ == "__main__":
    main()
