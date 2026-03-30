import os

def update_file():
    target_file = "index.html"
    with open(target_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Define new content
    new_vars = """  --shop-pink:  #F2A7B8;
  --shop-light: #FDF0F4;
  --shop-berry: #8B3A52;
  --shop-ivory: #FDF6F0;
  --shop-white: #FFFFFF;
  --shop-dark:  #1E0A10;
  --shop-rose:  #C4687A;
  --shop-muted: #A07080;
"""

    new_css = """/* BLOB BACKGROUND */
.hero-wrapper {
  position: relative;
  min-height: 100vh;
  padding-top: 72px;
  background: var(--shop-ivory);
  overflow: hidden;
  display: flex;
  align-items: center;
}

.blob-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  opacity: 0.55;
}

.blob-svg {
  width: 100%;
  height: 100%;
  position: absolute;
  inset: 0;
}

.b1 { animation: blobMove1 9s ease-in-out infinite; }
.b2 { animation: blobMove2 11s ease-in-out infinite; }
.b3 { animation: blobMove3 8s ease-in-out infinite; }
.b4 { animation: blobMove4 13s ease-in-out infinite; }
.b5 { animation: blobMove5 10s ease-in-out infinite; }

@keyframes blobMove1 { 0%,100%{cx:200;cy:250;r:130} 33%{cx:260;cy:200;r:150} 66%{cx:180;cy:320;r:110} }
@keyframes blobMove2 { 0%,100%{cx:380;cy:200;r:100} 33%{cx:320;cy:260;r:120} 66%{cx:420;cy:150;r:90} }
@keyframes blobMove3 { 0%,100%{cx:300;cy:380;r:120} 33%{cx:250;cy:420;r:100} 66%{cx:350;cy:300;r:140} }
@keyframes blobMove4 { 0%,100%{cx:150;cy:400;r:80} 50%{cx:200;cy:350;r:100} }
@keyframes blobMove5 { 0%,100%{cx:450;cy:350;r:90} 50%{cx:400;cy:420;r:110} }

/* HERO INNER LAYOUT */
.hero-inner {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  padding: 5rem 6rem 5rem 5rem;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}

/* LEFT COLUMN */
.hero-text-col {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--shop-berry);
  margin-bottom: 1.8rem;
  opacity: 0;
  animation: fadeSlideUp 0.7s cubic-bezier(0.16,1,0.3,1) 0.2s forwards;
}

.eyebrow-line {
  display: inline-block;
  width: 2rem;
  height: 1.5px;
  background: var(--shop-berry);
  flex-shrink: 0;
}

/* HEADLINE — word by word reveal */
.hero-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3.2rem, 5.5vw, 6rem);
  font-weight: 300;
  font-style: italic;
  line-height: 1.05;
  color: var(--shop-dark);
  margin-bottom: 1.8rem;
}

.word-row {
  display: block;
  overflow: hidden;
}

.word-wrap {
  display: inline-block;
  overflow: hidden;
}

.word {
  display: inline-block;
  opacity: 0;
  transform: translateY(110%);
}

.word-row:nth-child(1) .word { animation: wordUp 0.9s cubic-bezier(0.16,1,0.3,1) 0.4s forwards; }
.word-row:nth-child(2) .word { animation: wordUp 0.9s cubic-bezier(0.16,1,0.3,1) 0.65s forwards; }
.word-row:nth-child(3) .word { animation: wordUp 0.9s cubic-bezier(0.16,1,0.3,1) 0.9s forwards; }

.pink-word { color: var(--shop-berry); }

.hero-body {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.95rem;
  font-weight: 300;
  color: var(--shop-muted);
  line-height: 1.85;
  max-width: 38ch;
  margin-bottom: 2.4rem;
  opacity: 0;
  animation: fadeSlideUp 0.7s cubic-bezier(0.16,1,0.3,1) 1.1s forwards;
}

/* CTAs */
.hero-ctas {
  display: flex;
  gap: 1.4rem;
  align-items: center;
  margin-bottom: 2rem;
  opacity: 0;
  animation: fadeSlideUp 0.7s cubic-bezier(0.16,1,0.3,1) 1.25s forwards;
}

.cta-main {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  background: var(--shop-berry);
  color: var(--shop-ivory);
  padding: 1rem 2.2rem;
  text-decoration: none;
  transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}
.cta-main:hover {
  background: var(--shop-rose);
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(139,58,82,0.25);
}

.cta-sub {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 400;
  letter-spacing: 0.08em;
  color: var(--shop-muted);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  transition: color 0.25s, gap 0.25s;
}
.cta-sub:hover { color: var(--shop-berry); gap: 0.7rem; }

/* BADGES */
.hero-badges {
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
  opacity: 0;
  animation: fadeSlideUp 0.7s cubic-bezier(0.16,1,0.3,1) 1.4s forwards;
}

.badge {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.65rem;
  font-weight: 400;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--shop-berry);
  border: 1px solid rgba(139,58,82,0.25);
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  background: rgba(242,167,184,0.12);
  transition: background 0.2s;
}
.badge:hover { background: rgba(242,167,184,0.28); }

/* RIGHT COLUMN — tilt card */
.hero-visual-col {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  animation: fadeSlideUp 0.9s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;
}

.tilt-card-wrap {
  position: relative;
  width: 380px;
  border-radius: 2px;
  transform-style: preserve-3d;
  transition: transform 0.1s ease-out;
  will-change: transform;
  cursor: none;
}

.clip-reveal-box {
  position: relative;
  overflow: hidden;
  clip-path: inset(0 100% 0 0);
  animation: clipWipe 1.2s cubic-bezier(0.77,0,0.175,1) 0.6s forwards;
  border-radius: 2px;
}

.hero-food-img {
  width: 100%;
  height: 520px;
  object-fit: cover;
  display: block;
  transform: scale(1.08);
  animation: imgSettle 1.4s cubic-bezier(0.16,1,0.3,1) 0.6s forwards;
}

.img-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(30,10,16,0.35) 0%, transparent 60%);
}

.card-label {
  position: absolute;
  bottom: 1.2rem;
  left: 1.2rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.65rem;
  font-weight: 400;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(253,246,240,0.75);
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.card-dot { color: var(--shop-pink); }

/* FLOATING PILL BADGES */
.float-pill {
  position: absolute;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.68rem;
  font-weight: 400;
  letter-spacing: 0.06em;
  color: var(--shop-berry);
  background: var(--shop-white);
  border: 1px solid rgba(196,104,122,0.3);
  padding: 0.45rem 1rem;
  border-radius: 999px;
  box-shadow: 0 4px 20px rgba(139,58,82,0.1);
  white-space: nowrap;
}

.fp1 { top: 8%; right: -8%; animation: pillFloat 6s ease-in-out infinite; }
.fp2 { top: 45%; left: -12%; animation: pillFloat 8s ease-in-out 1s infinite; }
.fp3 { bottom: 12%; right: -6%; animation: pillFloat 7s ease-in-out 0.5s infinite; }

/* DUAL SCROLL STRIPS */
.dual-strips {
  background: var(--shop-dark);
  padding: 1rem 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.strip { overflow: hidden; }

.strip-track {
  display: flex;
  gap: 0.6rem;
  width: max-content;
}

.strip-left .strip-track  { animation: scrollLeft  28s linear infinite; }
.strip-right .strip-track { animation: scrollRight 22s linear infinite; }

.dual-strips:hover .strip-track { animation-play-state: paused; }

.strip-item {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 2px solid rgba(242,167,184,0.25);
  transition: border-color 0.3s, transform 0.3s;
}

.strip-item:hover {
  border-color: var(--shop-pink);
  transform: scale(1.1);
}

.strip-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* ── KEYFRAMES ── */
@keyframes wordUp {
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes clipWipe {
  to { clip-path: inset(0 0% 0 0); }
}

@keyframes imgSettle {
  to { transform: scale(1); }
}

@keyframes pillFloat {
  0%,100% { transform: translateY(0px); }
  50%     { transform: translateY(-10px); }
}

@keyframes scrollLeft {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

@keyframes scrollRight {
  from { transform: translateX(-50%); }
  to   { transform: translateX(0); }
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .hero-inner { grid-template-columns: 1fr; padding: 3rem 1.5rem; gap: 3rem; }
  .tilt-card-wrap { width: 100%; }
  .hero-food-img { height: 320px; }
  .fp1, .fp2, .fp3 { display: none; }
  .hero-title { font-size: clamp(2.8rem, 9vw, 4rem); }
}
"""

    new_html = """  <div class="hero-wrapper">

    <!-- BACKGROUND BLOB — always morphing -->
    <div class="blob-bg" aria-hidden="true">
      <svg class="blob-svg" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="goo">
            <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur"/>
            <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="goo"/>
          </filter>
        </defs>
        <g filter="url(#goo)">
          <circle class="b1" cx="200" cy="250" r="130" fill="#F2A7B8"/>
          <circle class="b2" cx="380" cy="200" r="100" fill="#F9D0DA"/>
          <circle class="b3" cx="300" cy="380" r="120" fill="#EDBED0"/>
          <circle class="b4" cx="150" cy="400" r="80"  fill="#F2A7B8"/>
          <circle class="b5" cx="450" cy="350" r="90"  fill="#F9D0DA"/>
        </g>
      </svg>
    </div>

    <!-- HERO CONTENT -->
    <div class="hero-inner">

      <!-- LEFT: text -->
      <div class="hero-text-col">
        <p class="hero-eyebrow">
          <span class="eyebrow-line"></span>
          Koramangala, Bangalore
        </p>

        <h1 class="hero-title" id="heroTitle">
          <span class="word-row"><span class="word-wrap"><span class="word">Baked</span></span><span class="word-wrap"><span class="word"> fresh,</span></span></span>
          <span class="word-row"><span class="word-wrap"><span class="word pink-word">with love,</span></span></span>
          <span class="word-row"><span class="word-wrap"><span class="word">for you.</span></span></span>
        </h1>

        <p class="hero-body">
          A little pink café in the heart of Koramangala — making things that taste like someone actually cared.
        </p>

        <div class="hero-ctas">
          <a href="menu.html" class="cta-main">Explore Menu</a>
          <a href="https://wa.me/918884449239" class="cta-sub" target="_blank">
            Order on WhatsApp
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg>
          </a>
        </div>

        <div class="hero-badges">
          <span class="badge">Open Daily</span>
          <span class="badge">Fresh Every Morning</span>
          <span class="badge">Custom Cakes</span>
        </div>
      </div>

      <!-- RIGHT: tilt card with clip reveal -->
      <div class="hero-visual-col">
        <div class="tilt-card-wrap" id="tiltCard">
          <div class="clip-reveal-box">
            <img
              class="hero-food-img"
              src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&h=900&fit=crop&crop=center"
              alt="Freshly baked cake"
            />
            <div class="img-overlay"></div>
          </div>
          <div class="card-label">
            <span>Freshly Baked</span>
            <span class="card-dot">·</span>
            <span>Made Daily</span>
          </div>
        </div>

        <!-- floating pill badges around the card -->
        <div class="float-pill fp1">Lotus Cheesecake ✨</div>
        <div class="float-pill fp2">Devil's Chocolate 🍫</div>
        <div class="float-pill fp3">Blueberry Cake 🫐</div>
      </div>

    </div>
  </div>

  <!-- DUAL SCROLL STRIPS — replaces marquee -->
  <div class="dual-strips">
    <div class="strip strip-left">
      <div class="strip-track">
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1551024601-bec78aea704b?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1519985176271-adb1088fa94c?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1572490122747-3a3cca73e5eb?w=200&h=200&fit=crop" alt=""/></div>
        <!-- duplicate for seamless loop -->
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1551024601-bec78aea704b?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1519985176271-adb1088fa94c?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1572490122747-3a3cca73e5eb?w=200&h=200&fit=crop" alt=""/></div>
      </div>
    </div>
    <div class="strip strip-right">
      <div class="strip-track">
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1524351199678-941a58a3df50?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=200&h=200&fit=crop" alt=""/></div>
        <!-- duplicate -->
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1524351199678-941a58a3df50?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=200&h=200&fit=crop" alt=""/></div>
        <div class="strip-item"><img src="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=200&h=200&fit=crop" alt=""/></div>
      </div>
    </div>
  </div>
"""

    new_js = """    // ── 3D MAGNETIC TILT ──
    const tiltCard = document.getElementById('tiltCard');
    if (tiltCard) {
      tiltCard.addEventListener('mousemove', (e) => {
        const rect = tiltCard.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width  - 0.5;
        const y = (e.clientY - rect.top)  / rect.height - 0.5;
        tiltCard.style.transform =
          `perspective(900px) rotateY(${x * 14}deg) rotateX(${-y * 10}deg) scale(1.02)`;
      });
      tiltCard.addEventListener('mouseleave', () => {
        tiltCard.style.transition = 'transform 0.7s cubic-bezier(0.16,1,0.3,1)';
        tiltCard.style.transform  = 'perspective(900px) rotateY(0deg) rotateX(0deg) scale(1)';
        setTimeout(() => { tiltCard.style.transition = 'transform 0.1s ease-out'; }, 700);
      });
    }

    // ── NAV SHRINK ──
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
      if (!nav) return;
      nav.style.padding    = window.scrollY > 60 ? '0.75rem 4rem' : '1.2rem 4rem';
      nav.style.transition = 'padding 0.4s ease';
    });
"""

    # Add the new variables right after :root {
    root_start = -1
    for i, line in enumerate(lines):
        if ":root {" in line:
            root_start = i
            break
    
    if root_start != -1:
        lines.insert(root_start + 1, new_vars)

    # find CSS target block
    css_start, css_end = -1, -1
    for i, line in enumerate(lines):
        if "/* HERO */" in line and css_start == -1:
            css_start = i
        if "@media (max-width: 768px) {" in line and css_start != -1 and css_end == -1:
            css_end = i + 5 # 5 lines down is the closing brace
            break

    if css_start != -1 and css_end != -1:
        lines = lines[:css_start] + [new_css] + lines[css_end:]

    # find HTML target block
    html_start, html_end = -1, -1
    for i, line in enumerate(lines):
        if "<!-- HERO -->" in line and html_start == -1:
            html_start = i
        if "<!-- ABOUT -->" in line and html_end == -1:
            html_end = i - 1
            break
            
    if html_start != -1 and html_end != -1:
        lines = lines[:html_start] + [new_html] + lines[html_end:]

    # find JS target block
    js_start, js_end = -1, -1
    for i, line in enumerate(lines):
        if "// ── FLOATING CIRCLES ──" in line and js_start == -1:
            js_start = i
        if "// Scroll reveal" in line and js_end == -1:
            js_end = i - 1 # up to the blank line before Scroll reveal
            break
            
    if js_start != -1 and js_end != -1:
        lines = lines[:js_start] + [new_js] + lines[js_end:]
        
    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    update_file()
