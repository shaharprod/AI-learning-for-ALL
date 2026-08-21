/* תפריט נגישות לפי ת"י 5568 / WCAG + קישורי מדיניות בפוטר */
(function () {
    var STORAGE_KEY = 'combe_a11y_v1';
    var lang = (document.documentElement.lang || 'he').toLowerCase().slice(0, 2);
    var inPages = (window.location.pathname || '').indexOf('/pages/') !== -1
        || (window.location.href || '').indexOf('/pages/') !== -1;
    var base = inPages ? '../' : '';
    var suffix = { en: '-en', ar: '-ar', hi: '-hi', ru: '-ru' }[lang] || '';

    var i18n = {
        he: {
            skip: 'דלג לתוכן הראשי',
            open: 'תפריט נגישות',
            title: 'תפריט נגישות',
            fontUp: 'הגדלת טקסט',
            fontDown: 'הקטנת טקסט',
            contrast: 'ניגודיות גבוהה',
            gray: 'גווני אפור',
            links: 'הדגשת קישורים',
            readable: 'גופן קריא',
            stopAnim: 'עצירת אנימציה',
            cursor: 'סמן גדול',
            reset: 'איפוס הגדרות',
            statement: 'להצהרת הנגישות',
            privacy: 'מדיניות פרטיות',
            a11y: 'הצהרת נגישות',
            terms: 'תנאי שימוש',
            legalNav: 'מסמכים משפטיים'
        },
        en: {
            skip: 'Skip to main content',
            open: 'Accessibility menu',
            title: 'Accessibility menu',
            fontUp: 'Increase text',
            fontDown: 'Decrease text',
            contrast: 'High contrast',
            gray: 'Grayscale',
            links: 'Highlight links',
            readable: 'Readable font',
            stopAnim: 'Stop animations',
            cursor: 'Large cursor',
            reset: 'Reset settings',
            statement: 'Accessibility statement',
            privacy: 'Privacy policy',
            a11y: 'Accessibility statement',
            terms: 'Terms of use',
            legalNav: 'Legal documents'
        },
        ar: {
            skip: 'تخطٍ إلى المحتوى الرئيسي',
            open: 'قائمة إمكانية الوصول',
            title: 'قائمة إمكانية الوصول',
            fontUp: 'تكبير النص',
            fontDown: 'تصغير النص',
            contrast: 'تباين عالٍ',
            gray: 'تدرج رمادي',
            links: 'إبراز الروابط',
            readable: 'خط واضح',
            stopAnim: 'إيقاف الحركة',
            cursor: 'مؤشر كبير',
            reset: 'إعادة الضبط',
            statement: 'بيان إمكانية الوصول',
            privacy: 'سياسة الخصوصية',
            a11y: 'بيان إمكانية الوصول',
            terms: 'شروط الاستخدام',
            legalNav: 'مستندات قانونية'
        },
        hi: {
            skip: 'मुख्य सामग्री पर जाएँ',
            open: 'सुगम्यता मेनू',
            title: 'सुगम्यता मेनू',
            fontUp: 'टेक्स्ट बड़ा करें',
            fontDown: 'टेक्स्ट छोटा करें',
            contrast: 'उच्च कंट्रास्ट',
            gray: 'ग्रेस्केल',
            links: 'लिंक हाइलाइट',
            readable: 'पढ़ने योग्य फ़ॉन्ट',
            stopAnim: 'एनिमेशन रोकें',
            cursor: 'बड़ा कर्सर',
            reset: 'सेटिंग रीसेट',
            statement: 'सुगम्यता विवरण',
            privacy: 'गोपनीयता नीति',
            a11y: 'सुगम्यता विवरण',
            terms: 'उपयोग की शर्तें',
            legalNav: 'कानूनी दस्तावेज़'
        },
        ru: {
            skip: 'К основному содержимому',
            open: 'Меню доступности',
            title: 'Меню доступности',
            fontUp: 'Увеличить текст',
            fontDown: 'Уменьшить текст',
            contrast: 'Высокий контраст',
            gray: 'Оттенки серого',
            links: 'Выделить ссылки',
            readable: 'Читаемый шрифт',
            stopAnim: 'Остановить анимацию',
            cursor: 'Большой курсор',
            reset: 'Сбросить настройки',
            statement: 'Заявление о доступности',
            privacy: 'Политика конфиденциальности',
            a11y: 'Заявление о доступности',
            terms: 'Условия использования',
            legalNav: 'Юридические документы'
        }
    };
    var t = i18n[lang] || i18n.he;

    function loadState() {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}') || {};
        } catch (e) {
            return {};
        }
    }
    function saveState(state) {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        } catch (e) { /* ignore */ }
    }

    var CLASSES = {
        contrast: 'a11y-contrast',
        gray: 'a11y-gray',
        links: 'a11y-links',
        readable: 'a11y-readable',
        stopAnim: 'a11y-stop-anim',
        cursor: 'a11y-cursor'
    };

    function applyState(state) {
        var html = document.documentElement;
        Object.keys(CLASSES).forEach(function (key) {
            html.classList.toggle(CLASSES[key], !!state[key]);
        });
        html.classList.remove('a11y-font-1', 'a11y-font-2', 'a11y-font-3');
        var level = parseInt(state.font, 10) || 0;
        if (level > 0) html.classList.add('a11y-font-' + Math.min(level, 3));
    }

    function ready(fn) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fn);
        } else {
            fn();
        }
    }

    ready(function () {
        var state = loadState();
        applyState(state);

        var main = document.querySelector('main, .article, #home, .hero');
        if (main && !main.id) main.id = 'main-content';
        var mainId = (main && main.id) ? main.id : 'home';

        var skip = document.createElement('a');
        skip.className = 'skip-link';
        skip.href = '#' + mainId;
        skip.textContent = t.skip;
        document.body.insertBefore(skip, document.body.firstChild);

        var footer = document.querySelector('footer .container') || document.querySelector('footer');
        if (footer && !footer.querySelector('.footer-legal')) {
            var legal = document.createElement('nav');
            legal.className = 'footer-legal';
            legal.setAttribute('aria-label', t.legalNav);
            legal.innerHTML =
                '<a href="' + base + 'privacy' + suffix + '.html">' + t.privacy + '</a>' +
                '<a href="' + base + 'accessibility' + suffix + '.html">' + t.a11y + '</a>' +
                '<a href="' + base + 'terms' + suffix + '.html">' + t.terms + '</a>';
            var contact = footer.querySelector('.footer-contact');
            if (contact) footer.insertBefore(legal, contact);
            else footer.appendChild(legal);
        }

        var fab = document.createElement('button');
        fab.type = 'button';
        fab.className = 'a11y-fab';
        fab.setAttribute('aria-label', t.open);
        fab.setAttribute('aria-expanded', 'false');
        fab.setAttribute('aria-controls', 'a11y-panel');
        fab.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6zm-1 7h2c2.2 0 4 1.8 4 4v9h-3v-8h-4v8H7v-9c0-2.2 1.8-4 4-4z"/></svg>';

        var panel = document.createElement('div');
        panel.id = 'a11y-panel';
        panel.className = 'a11y-panel';
        panel.setAttribute('role', 'dialog');
        panel.setAttribute('aria-labelledby', 'a11y-title');
        panel.innerHTML =
            '<h2 id="a11y-title">' + t.title + '</h2>' +
            '<div class="a11y-actions">' +
            '<button type="button" data-act="fontUp">' + t.fontUp + '</button>' +
            '<button type="button" data-act="fontDown">' + t.fontDown + '</button>' +
            '<button type="button" data-act="contrast" aria-pressed="false">' + t.contrast + '</button>' +
            '<button type="button" data-act="gray" aria-pressed="false">' + t.gray + '</button>' +
            '<button type="button" data-act="links" aria-pressed="false">' + t.links + '</button>' +
            '<button type="button" data-act="readable" aria-pressed="false">' + t.readable + '</button>' +
            '<button type="button" data-act="stopAnim" aria-pressed="false">' + t.stopAnim + '</button>' +
            '<button type="button" data-act="cursor" aria-pressed="false">' + t.cursor + '</button>' +
            '</div>' +
            '<button type="button" class="a11y-reset" data-act="reset">' + t.reset + '</button>' +
            '<a class="a11y-statement" href="' + base + 'accessibility' + suffix + '.html">' + t.statement + '</a>';

        function syncPressed() {
            panel.querySelectorAll('[data-act][aria-pressed]').forEach(function (btn) {
                btn.setAttribute('aria-pressed', state[btn.getAttribute('data-act')] ? 'true' : 'false');
            });
        }
        syncPressed();

        function openPanel() {
            panel.classList.add('open');
            fab.setAttribute('aria-expanded', 'true');
            var first = panel.querySelector('button');
            if (first) first.focus();
        }
        function closePanel() {
            panel.classList.remove('open');
            fab.setAttribute('aria-expanded', 'false');
            fab.focus();
        }

        fab.addEventListener('click', function () {
            if (panel.classList.contains('open')) closePanel();
            else openPanel();
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && panel.classList.contains('open')) {
                e.preventDefault();
                closePanel();
            }
        });

        panel.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-act]');
            if (!btn) return;
            var act = btn.getAttribute('data-act');
            if (act === 'fontUp') state.font = Math.min((parseInt(state.font, 10) || 0) + 1, 3);
            else if (act === 'fontDown') state.font = Math.max((parseInt(state.font, 10) || 0) - 1, 0);
            else if (act === 'reset') state = {};
            else state[act] = !state[act];
            saveState(state);
            applyState(state);
            syncPressed();
        });

        document.body.appendChild(panel);
        document.body.appendChild(fab);
    });
})();
