# 🐰 2 Rabbits Bakes

> *"🌸Pink Café 🍰Freshly Baked – Made with Love ❤️"*

A soft, feminine, whimsical bakery website built with pure HTML, CSS & vanilla JavaScript. No frameworks, no build steps — just deploy and go.

---

## ✨ Features

- **Fully responsive** — mobile, tablet, desktop
- **Scroll animations** — gentle reveal on scroll
- **Animated hero** — floating bunnies, soft blobs, marquee strip
- **Menu grid** — 6 product cards with hover effects
- **Testimonials section** — soft glassmorphism cards
- **How to Order** — 4-step process
- **Zero dependencies** — one HTML file, Google Fonts via CDN
- **GitHub Pages ready** — deploy in 60 seconds

---

## 🚀 Deploy to GitHub Pages (Free Hosting)

### Step 1 — Create a GitHub Repository
1. Go to [github.com](https://github.com) → **New repository**
2. Name it `2rabbits-bakes` (or whatever you like)
3. Set to **Public**
4. Click **Create repository**

### Step 2 — Upload the file
Option A — via GitHub website:
1. Click **Add file → Upload files**
2. Drag in `index.html`
3. Click **Commit changes**

Option B — via terminal:
```bash
git init
git add index.html
git commit -m "🐰 Initial launch"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/2rabbits-bakes.git
git push -u origin main
```

### Step 3 — Enable GitHub Pages
1. Go to your repo → **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `/ (root)`
4. Click **Save**

Your site will be live at:
`https://YOUR_USERNAME.github.io/2rabbits-bakes/`

> ⏱ Takes ~1–2 minutes to go live after saving.

---

## 🎨 Customisation Guide

### Change colours
Edit the CSS variables at the top of `index.html`:

```css
:root {
  --blush: #FADADD;       /* main background pink */
  --rose: #D4697A;        /* buttons & accents */
  --cream: #FFF5F0;       /* section backgrounds */
  --lavender: #E8D5F5;    /* highlight accent */
  --charcoal: #3D2C2C;    /* text color */
}
```

### Update your Instagram handle
Search for `@2rabbitsbakes` and replace with your actual handle.
Also update all `href="https://www.instagram.com"` links to your profile URL.

### Update prices
Find the `.menu-price` spans and update the `₹` values.

### Update your WhatsApp
Replace `https://wa.me` with `https://wa.me/91XXXXXXXXXX` (your number).

### Replace placeholder content
- **About section**: Update the story text to yours
- **Testimonials**: Replace with real customer reviews
- **Menu cards**: Add your actual items, descriptions & prices
- **Footer**: Update city, email, contact details

---

## 📁 File Structure

```
2rabbits-bakes/
└── index.html          ← entire site in one file
```

That's it! One file = full website.

---

## 🌐 Custom Domain (Optional)

If you have a domain like `2rabbitsbakes.in`:

1. In your repo, create a file called `CNAME`
2. Inside it, just write: `2rabbitsbakes.in`
3. At your domain registrar, add a CNAME record:
   - Name: `www`
   - Value: `YOUR_USERNAME.github.io`

---

## 💌 Made with love by

Designed for 2 Rabbits Bakes 🐰🌸
