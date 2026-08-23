# Tools Pro Web — Project Guide

Ye folder aapki Blogger website **toolsproweb.site** ka complete organized project hai.
Yahan se aap theme update kar sakte hain, naye tool pages bana sakte hain, aur sab kuch ek jagah manage ho ga.

---

## 📁 Folder Structure

```
toolsproweb/
├── README.md                    ← ye guide
│
├── theme/
│   └── toolsproweb-theme.xml    ← Blogger THEME (Restore yahan se karein)
│
├── data/
│   ├── tools.json               ← saare 230 tools (name, url, icon)
│   └── categories.json          ← 11 categories ki settings
│
├── pages/                       ← har tool ka page yahan banega
│   ├── binary/                  ← /p/ascii-to-binary.html waghera
│   ├── converters/
│   ├── generators/
│   ├── image-pdf/
│   ├── calculators/
│   ├── seo/
│   ├── text/
│   ├── units/
│   ├── dev/
│   ├── web/
│   └── youtube/
│
├── assets/
│   ├── css/theme.css            ← CSS source (reference)
│   ├── js/                      ← reusable JS (tools ke liye)
│   └── icons/icons.svg          ← 193 SVG icons library
│
└── build/
    └── build.py                 ← theme build/regenerate script
```

---

## 🔄 Kaam ka flow (Workflow)

### 1. Theme update karna (design, colors, layout)
- **File:** `theme/toolsproweb-theme.xml`
- Isme `<b:skin>` ke andar CSS hai, neeche HTML/JS
- Edit karne ke baad: **Blogger → Theme → Restore → ye file upload**

### 2. Naya tool add karna (homepage list mein)
- **File:** `data/tools.json`
- Apni category mein entry add karein:
```json
{"name": "My New Tool", "url": "/p/my-new-tool.html", "icon": null, "img": null}
```
- `icon` = SVG symbol id (assets/icons/icons.svg se), ya `img` = image URL
- Phir mujhe kahein "theme rebuild karo" — main nayi XML bana dunga

### 3. Tool ka working page banana
- `pages/` ke andar uski category folder mein HTML file banayein
- Example: `pages/text/word-counter.html`
- Page ka content Blogger → **Pages → New Page → HTML view** mein paste karein
- **Permalink zaroori hai:** `/p/...` wala URL tools.json ke `url` se match karna chahiye

---

## 🔗 Permalink Rule (Bohat Zaroori!)

Blogger page ka URL automatically title se banta hai, magar aap **custom permalink** set kar sakte hain:

| Tool | Page ka permalink |
|------|-------------------|
| ASCII to Binary | `/p/ascii-to-binary.html` |
| Word Counter | `/p/word-counter.html` |

Blogger mein: **Page editor → right side → Permalink → Custom permalink** → sirf slug likhein (jaise `ascii-to-binary`)

Agar URL match nahi hua to homepage se click karne par **404** aayega.

---

## ✏️ Common edits — kahan karein

| Kya change karna hai | File | Kahan |
|----------------------|------|-------|
| Colors (Royal Blue) | theme XML | `<b:skin>` mein `:root` variables |
| Site title / logo text | theme XML | `.logo-text` wala block |
| Hero heading | theme XML | `<section class='hero'>` |
| Stats numbers | theme XML | `<section class='stats'>` |
| Footer links | theme XML | `<footer class='tpw-footer'>` |
| Tools ki list | data/tools.json | category ke andar |
| Category names | data/categories.json | — |
| Icons | assets/icons/icons.svg | new `<symbol>` add karein |

---

## 🚀 Naye updates ke liye

Jab bhi kuch change karna ho, mujhe (OpenHands) bata dein:
- "Word Counter ka working page banao" → main `pages/text/word-counter.html` bana dunga
- "Theme ka color change karo" → main XML update kar dunga
- "5 naye tools add karo" → data update + rebuild

Har baar final file wahi rahegi: **`theme/toolsproweb-theme.xml`** — bas Blogger par Restore.

---

## 📝 Notes
- Theme XML hi Blogger ko chahiye — `data/`, `pages/`, `assets/` sirf aapke development ke liye hain (Blogger par upload NAHI hote)
- Tool pages Blogger ke **Pages** section mein individually paste hote hain
- icons.svg ki icons Blogger CDN se bhi serve ho sakti hain agar aap chahein
