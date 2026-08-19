# -*- coding: utf-8 -*-
"""Generate ai-tools-hi.html and glossary-hi.html with Hindi content."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"

NAV = '''            <ul class="nav-links">
                <li><a href="../index-hi.html">होम</a></li>
                <li class="dropdown">
                    <a href="../index-hi.html#topics" class="dropdown-toggle">पाठ ▾</a>
                    <ul class="dropdown-menu">
                        <li><a href="intro-to-ai-hi.html">1. एआई का परिचय</a></li>
                        <li><a href="ai-history-hi.html">2. एआई का इतिहास</a></li>
                        <li><a href="machine-learning-hi.html">3. मशीन लर्निंग</a></li>
                        <li><a href="ai-daily-life-hi.html">4. रोज़मर्रा की ज़िंदगी में एआई</a></li>
                        <li><a href="ai-tools-hi.html">5. व्यावहारिक उपकरण</a></li>
                        <li><a href="prompt-engineering-hi.html">6. प्रॉम्प्ट इंजीनियरिंग</a></li>
                        <li><a href="ai-ethics-hi.html">7. एआई नैतिकता</a></li>
                        <li><a href="ai-future-hi.html">8. एआई का भविष्य</a></li>
                        <li><a href="glossary-hi.html">9. शब्दावली</a></li>
                    </ul>
                </li>
                <li><a href="glossary-hi.html">शब्दावली</a></li>
                <li><a href="ai-tools-hi.html">उपकरण</a></li>
                <li><a href="../index-hi.html#about">परिचय</a></li>
            </ul>
            <form class="nav-search" id="site-search" role="search">
                <input type="search" name="q" placeholder="खोजें..." aria-label="खोजें" />
                <button type="submit" aria-label="खोजें">🔍</button>
            </form>'''

FOOTER = '''            <p class="site-version" aria-label="version">B0.14 · שחר הפקות AI · के लिए निर्मित: COMBE</p>
            <p>© 2026 एआई सीखना – Sam Shahar</p>
            <p class="footer-contact">फ़ोन: <a href="tel:+972522603831">+972522603831</a> | ईमेल: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>'''

HEAD = '''    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>body { direction: ltr; font-family: 'Noto Sans Devanagari', sans-serif; }</style>'''

def lang_switcher(slug):
    return f'''            <nav class="lang-switcher" aria-label="भाषा चुनें">
                <a href="{slug}.html" hreflang="he" lang="he">עברית</a>
                <a href="{slug}-en.html" hreflang="en" lang="en">English</a>
                <a href="{slug}-ar.html" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">हिन्दी</span>
            </nav>'''

def apply_shell(html, slug, title, breadcrumb):
    html = re.sub(r'<html lang="en"[^>]*>', '<html lang="hi" dir="ltr" data-version="B0.14">', html, 1)
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Heebo[^"]*" rel="stylesheet">\s*<style>body \{ direction: ltr; \}</style>',
        HEAD, html, 1)
    html = html.replace('AI Learning', 'एआई सीखना')
    html = html.replace('Built for: COMBE', 'के लिए निर्मित: COMBE')
    html = html.replace('../index-en.html', '../index-hi.html')
    html = re.sub(r'<span class="logo-text">.*?</span>\s*<span class="logo-byline">.*?</span>\s*<span class="logo-dedication">',
                  '<span class="logo-text">एआई सीखना</span>\n                        <span class="logo-byline">שחר הפקות AI · B0.14</span>\n                        <span class="logo-dedication">',
                  html, 1, flags=re.S)
    html = re.sub(r'<ul class="nav-links">.*?</form>', NAV, html, 1, flags=re.S)
    html = re.sub(r'<nav class="lang-switcher" aria-label="Language">.*?</nav>', lang_switcher(slug), html, 1, flags=re.S)
    html = html.replace('aria-label="Menu"', 'aria-label="मेनू"')
    html = html.replace('alt="Logo"', 'alt="लोगो"')
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | एआई सीखना · שחר הפקות AI · B0.14 · के लिए निर्मित: COMBE</title>', html, 1)
    html = re.sub(r'<div class="breadcrumb"><a href="../index-hi.html">Home</a> / <span>.*?</span></div>',
                  f'<div class="breadcrumb"><a href="../index-hi.html">होम</a> / <span>{breadcrumb}</span></div>', html, 1)
    html = re.sub(r'<p class="site-version"[^>]*>.*?</p>\s*<p>©.*?</p>\s*<p class="footer-contact">.*?</p>', FOOTER, html, 1, flags=re.S)
    # fix internal links
    for page in ['intro-to-ai','ai-history','machine-learning','ai-daily-life','ai-tools','prompt-engineering','ai-ethics','ai-future','glossary']:
        html = html.replace(f'{page}-en.html', f'{page}-hi.html')
    return html

# Translation dictionary - longest first
TRANS = {}

def add(*pairs):
    for en, hi in pairs:
        TRANS[en] = hi

add(
    ("Practical Tools", "व्यावहारिक उपकरण"),
    ("Practical AI Tools – User Guide", "व्यावहारिक एआई उपकरण – उपयोगकर्ता मार्गदर्शिका"),
    ("🛠️ Reading time: 10 min | Level: Everyone | Updated January 2026", "🛠️ पढ़ने का समय: 10 मिनट | स्तर: सभी के लिए | जनवरी 2026 अपडेट"),
    ("Tech tools - practical AI", "तकनीकी उपकरण - व्यावहारिक एआई"),
    ("Why get to know AI tools?", "एआई उपकरण क्यों जानें?"),
    ("AI tools are now accessible to everyone. They can save you time,\n                        help with creativity, and solve problems that once required experts.",
     "एआई उपकरण अब सभी के लिए सुलभ हैं। वे समय बचा सकते हैं,\n                        रचनात्मकता में मदद कर सकते हैं, और ऐसी समस्याएँ हल कर सकते हैं जिनके लिए पहले विशेषज्ञ चाहिए थे।"),
    ("Here are the most popular tools and how to use them:", "यहाँ सबसे लोकप्रिय उपकरण और उनका उपयोग कैसे करें:"),
    ("Note:", "नोट:"),
    ("Pricing and limits may change – check each tool’s official site for current plans.",
     "मूल्य और सीमाएँ बदल सकती हैं – वर्तमान योजनाओं के लिए प्रत्येक उपकरण की आधिकारिक साइट देखें।"),
    ("💬 Smart chatbots", "💬 स्मार्ट चैटबॉट"),
    ("The tool that started the revolution in November 2022. As of 2026 ChatGPT is powered by GPT-5 and GPT-5.2 (including built-in \"thinking\" mode), handles natural conversation, answers complex questions, and performs a huge range of tasks.",
     "नवंबर 2022 में क्रांति शुरू करने वाला उपकरण। 2026 तक ChatGPT GPT-5 और GPT-5.2 (अंतर्निहित \"thinking\" मोड सहित) द्वारा संचालित है, प्राकृतिक बातचीत, जटिल प्रश्नों के उत्तर और विशाल कार्यों की श्रृंखला करता है।"),
    ("What you can do:", "आप क्या कर सकते हैं:"),
    ("Writing:", "लेखन:"),
    ("Learning:", "सीखना:"),
    ("Coding:", "कोडिंग:"),
    ("Translation:", "अनुवाद:"),
    ("Analysis:", "विश्लेषण:"),
    ("Creativity:", "रचनात्मकता:"),
    ("💰 Pricing:", "💰 मूल्य:"),
    ("Free:", "मुफ़्त:"),
    ("💡 Usage tips:", "💡 उपयोग सुझाव:"),
    ("Unique strengths:", "विशिष्ट ताकत:"),
    ("Strengths:", "ताकत:"),
    ("Examples:", "उदाहरण:"),
    ("Highlights:", "मुख्य बिंदु:"),
    ("🎨 Image generation", "🎨 छवि निर्माण"),
    ("✍️ Writing and editing", "✍️ लेखन और संपादन"),
    ("🎥 Video and audio", "🎥 वीडियो और ऑडियो"),
    ("⚡ Productivity", "⚡ उत्पादकता"),
    ("📌 Tips for better use", "📌 बेहतर उपयोग के सुझाव"),
    ("⚠️ Remember:", "⚠️ याद रखें:"),
    ("Summary – where to start? 📝", "सारांश – कहाँ से शुरू करें? 📝"),
    ("📝 Test yourself", "📝 अपनी जाँच करें"),
    ("Answer 10 questions to check your understanding of AI tools.", "एआई उपकरणों की समझ जाँचने के लिए 10 प्रश्नों के उत्तर दें।"),
    ("Check answers", "उत्तर जाँचें"),
    ("Your results", "आपके परिणाम"),
    ("Correct answers", "सही उत्तर"),
    ("Success rate", "सफलता दर"),
    ("Try again", "फिर से कोशिश करें"),
    ("→ 4. AI in Daily Life", "→ 4. रोज़मर्रा की ज़िंदगी में एआई"),
    ("6. Prompt Engineering – Next ←", "6. प्रॉम्प्ट इंजीनियरिंग – अगला ←"),
    ("Phone:", "फ़ोन:"),
    ("Email:", "ईमेल:"),
    ("Artificial Intelligence Glossary", "कृत्रिम बुद्धिमत्ता शब्दावली"),
    ("Glossary", "शब्दावली"),
    ("📖 Over 100 terms with short explanations – arranged by lesson order", "📖 100+ शब्द संक्षिप्त व्याख्या के साथ – पाठ क्रम में"),
    ("On this page you will find definitions of key concepts from the world of artificial intelligence. Terms are arranged in the <strong>chronological order of the lessons</strong> in the course: 1 Intro ← 2 History ← 3 Machine Learning ← 4 AI in Daily Life ← 5 Tools ← 6 Prompt Engineering ← 7 Ethics ← 8 Future. Each entry shows the term in English (and often the Hebrew in the source).",
     "इस पृष्ठ पर कृत्रिम बुद्धिमत्ता की दुनिया के मुख्य अवधारणाओं की परिभाषाएँ मिलेंगी। शब्द पाठ्यक्रम में <strong>पाठों के कालानुक्रमिक क्रम</strong> में हैं: 1 परिचय ← 2 इतिहास ← 3 मशीन लर्निंग ← 4 रोज़मर्रा ← 5 उपकरण ← 6 प्रॉम्प्ट ← 7 नैतिकता ← 8 भविष्य। प्रत्येक प्रविष्टि में हिन्दी और अंग्रेज़ी तकनीकी शब्द दिखते हैं।"),
    ("Lesson 1 – Intro to AI: General terms", "पाठ 1 – एआई परिचय: सामान्य शब्द"),
    ("Lesson 2 – History of AI", "पाठ 2 – एआई का इतिहास"),
    ("Lesson 3 – Machine Learning", "पाठ 3 – मशीन लर्निंग"),
    ("Lesson 3 – Neural networks and deep learning", "पाठ 3 – न्यूरल नेटवर्क और डीप लर्निंग"),
    ("Lessons 4–5 – Language, text, and language models", "पाठ 4–5 – भाषा, पाठ और भाषा मॉडल"),
    ("Lesson 4 – AI in daily life: Images, video, and vision", "पाठ 4 – रोज़मर्रा में एआई: छवि, वीडियो और विज़न"),
    ("Lessons 5–6 – Prompts and tools", "पाठ 5–6 – प्रॉम्प्ट और उपकरण"),
    ("Lesson 7 – Ethics, safety, and impact", "पाठ 7 – नैतिकता, सुरक्षा और प्रभाव"),
    ("Lesson 8 – Future and more techniques", "पाठ 8 – भविष्य और अधिक तकनीकें"),
    ("→ 8. The Future of AI", "→ 8. एआई का भविष्य"),
    ("Back to Home ←", "होम पर वापस ←"),
)

# Glossary term titles and definitions
GLOSSARY = [
    ("Artificial Intelligence (AI)", "कृत्रिम बुद्धिमत्ता (AI)", "कंप्यूटर विज्ञान की वह शाखा जो ऐसी प्रणालियाँ बनाती है जो सामान्यतः मानवीय बुद्धि वाले कार्य करें: सीखना, समझ, समस्या-समाधान और निर्णय।"),
    ("Algorithm", "एल्गोरिदम", "किसी समस्या को हल करने या कार्य करने के चरणों का निर्धारित क्रम। एआई में: मॉडल द्वारा उपयोग किए नियम और गणना।"),
    ("Model", "मॉडल", "प्रशिक्षण के दौरान बनाया गया गणितीय/Computational प्रतिनिधित्व, नए डेटा पर भविष्यवाणी या inference के लिए।"),
    ("Training", "प्रशिक्षण", "एल्गोरिदम द्वारा डेटा से सीखने की प्रक्रिया: पैरामीटर समायोजित करके मॉडल प्रदर्शन सुधार।"),
    ("Inference", "इnference (अनुमान)", "प्रशिक्षित मॉडल का उपयोग नए इनपुट के लिए भविष्यवाणी/उत्तर देने के लिए, पैरामीटर अपडेट किए बिना।"),
    ("Data", "डेटा", "जानकारी जिससे प्रणाली सीखती या प्रसंस्करण करती है – पाठ, छवि, संख्या, उपयोगकर्ता इनपुट आदि।"),
    ("Parameter", "पैरामीटर", "प्रशिक्षण में सीखा मान (जैसे neural network में weights)। बड़े मॉडल में अरबों पैरामीटर।"),
    ("Narrow AI", "संकीर्ण एआई", "एक कार्य या सीमित क्षेत्र में उत्कृष्ट एआई (चेहरा पहचान, अनुवाद, गेम) – AGI के विपरीत।"),
    ("Artificial General Intelligence (AGI)", "सामान्य कृत्रिम बuddhimatta (AGI)", "मानव-स्तरीय बuddhimatta – विस्तृत कार्यों और क्षेत्रों में सीखने और करने की क्षमता।"),
    ("Artificial Superintelligence (ASI)", "कृत्रिम सुपरइंटेलिजेंस (ASI)", "सैद्धांतिक: मानवता से हर प्रासंगिक क्षेत्र में अधिक बuddhimatta वाली प्रणाली। आज मौजूद नहीं।"),
    ("Automation", "स्वचालन", "मानव हस्तक्षेप के बिना कार्य करना। एआई दोहराए जाने वाले प्रक्रियाओं और कंटेंट निर्माण को automate करता है।"),
]

def translate(html):
    for en, hi in sorted(TRANS.items(), key=lambda x: -len(x[0])):
        html = html.replace(en, hi)
    return html

def build_tools():
    html = apply_shell(
        (PAGES / "ai-tools-en.html").read_text(encoding="utf-8"),
        "ai-tools", "व्यावहारिक उपकरण", "व्यावहारिक उपकरण")
    html = translate(html)
    (PAGES / "ai-tools-hi.html").write_text(html, encoding="utf-8")
    print("ai-tools-hi.html written", len(html))

def build_glossary():
    html = apply_shell(
        (PAGES / "glossary-en.html").read_text(encoding="utf-8"),
        "glossary", "शब्दावली", "शब्दावली")
    html = translate(html)
    # Replace glossary term blocks
    for en_title, hi_title, hi_def in GLOSSARY:
        html = html.replace(f"<h3 id=", f"<h3 id=", html)  # keep ids
        html = re.sub(
            rf'<h3 id="[^"]*">{re.escape(en_title)}</h3>\s*<p>[^<]*</p>',
            f'<h3>{hi_title}</h3>\n                    <p>{hi_def}</p>',
            html, count=1)
    (PAGES / "glossary-hi.html").write_text(html, encoding="utf-8")
    print("glossary-hi.html written (partial terms)", len(html))

if __name__ == "__main__":
    build_tools()
    build_glossary()
