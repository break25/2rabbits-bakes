import os

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_css = """    /* HERO */
    .hero {
      display: grid;
      grid-template-columns: 1fr 1fr;
      min-height: 100vh;
      padding-top: 72px;
    }

    .hero-left {
      background: #2E1A1E;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 5rem 4rem 5rem 5rem;
      position: relative;
      overflow: hidden;
    }

    /* subtle grain texture on dark panel */
    .hero-left::after {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      opacity: 0.5;
    }

    .hero-eyebrow {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.68rem;
      font-weight: 500;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #C4848E;
      margin-bottom: 2rem;
      opacity: 0;
      animation: fadeUpHero 0.6s ease 0.1s forwards;
    }

    .hero-heading {
      margin-bottom: 1.8rem;
    }

    .hero-line {
      overflow: hidden;
      line-height: 1.05;
    }

    .hero-line span {
      display: block;
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(3rem, 5vw, 5rem);
      font-weight: 300;
      font-style: italic;
      color: #FFF8F5;
      opacity: 0;
      transform: translateY(100%);
    }

    .hero-line span.pink { color: #F4B8C1; }

    .hero-line:nth-child(1) span { animation: lineUp 0.8s cubic-bezier(0.16,1,0.3,1) 0.3s forwards; }
    .hero-line:nth-child(2) span { animation: lineUp 0.8s cubic-bezier(0.16,1,0.3,1) 0.55s forwards; }
    .hero-line:nth-child(3) span { animation: lineUp 0.8s cubic-bezier(0.16,1,0.3,1) 0.8s forwards; }

    .hero-sub {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.9rem;
      font-weight: 300;
      color: rgba(255,248,245,0.45);
      line-height: 1.75;
      max-width: 36ch;
      margin-bottom: 2.5rem;
      opacity: 0;
      animation: fadeUpHero 0.6s ease 1.1s forwards;
    }

    .hero-actions {
      display: flex;
      gap: 1.5rem;
      align-items: center;
      opacity: 0;
      animation: fadeUpHero 0.6s ease 1.3s forwards;
    }

    .btn-primary {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.72rem;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #2E1A1E;
      background: #F4B8C1;
      padding: 0.9rem 2rem;
      text-decoration: none;
      transition: background 0.25s, transform 0.25s;
      display: inline-block;
    }
    .btn-primary:hover { background: #C4848E; color: #FFF8F5; transform: translateY(-2px); }

    .btn-ghost {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.72rem;
      font-weight: 400;
      letter-spacing: 0.1em;
      color: rgba(255,248,245,0.5);
      text-decoration: none;
      transition: color 0.2s;
    }
    .btn-ghost:hover { color: #F4B8C1; }

    /* RIGHT PANEL */
    .hero-right {
      background: #FDE8EC;
      position: relative;
      overflow: hidden;
      cursor: none;
    }

    .float-field {
      position: absolute;
      inset: 0;
    }

    /* floating circles injected by JS */
    .float-circle {
      position: absolute;
      border-radius: 50%;
      overflow: hidden;
      border: 3px solid rgba(196,132,142,0.4);
      animation: floatOrbit var(--dur) ease-in-out var(--delay) infinite;
      opacity: 0;
      animation-fill-mode: forwards;
    }

    .float-circle img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .hero-right-label {
      position: absolute;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%);
      font-family: 'DM Sans', sans-serif;
      font-size: 0.68rem;
      font-weight: 400;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #9E5A63;
      display: flex;
      align-items: center;
      gap: 0.8rem;
      white-space: nowrap;
      opacity: 0;
      animation: fadeUpHero 0.6s ease 1.5s forwards;
    }

    .hero-right-label .dot { color: #C4848E; }

    /* MARQUEE STRIP */
    .marquee-strip {
      background: #2E1A1E;
      padding: 0.85rem 0;
      overflow: hidden;
      white-space: nowrap;
    }

    .marquee-track {
      display: inline-flex;
      gap: 2rem;
      animation: marqueeScroll 25s linear infinite;
    }

    .marquee-strip:hover .marquee-track { animation-play-state: paused; }

    .marquee-track span {
      font-family: 'Cormorant Garamond', serif;
      font-size: 0.95rem;
      font-style: italic;
      color: rgba(244,184,193,0.8);
      letter-spacing: 0.06em;
      flex-shrink: 0;
    }

    .marquee-track .mdot {
      color: rgba(196,132,142,0.4);
      font-style: normal;
    }

    /* KEYFRAMES */
    @keyframes lineUp {
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeUpHero {
      from { opacity: 0; transform: translateY(16px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes marqueeScroll {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }

    @keyframes floatOrbit {
      0%   { transform: translateY(0px) rotate(0deg); opacity: 0.85; }
      25%  { transform: translateY(-18px) rotate(2deg); opacity: 1; }
      50%  { transform: translateY(-8px) rotate(-1deg); opacity: 0.9; }
      75%  { transform: translateY(-22px) rotate(3deg); opacity: 1; }
      100% { transform: translateY(0px) rotate(0deg); opacity: 0.85; }
    }

    /* CURSOR TRAIL */
    .cursor-dot {
      position: fixed;
      border-radius: 50%;
      background: rgba(196,132,142,0.6);
      pointer-events: none;
      z-index: 9999;
      transform: translate(-50%, -50%);
      transition: width 0.2s ease, height 0.2s ease, opacity 0.4s ease;
    }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      .hero { grid-template-columns: 1fr; }
      .hero-right { height: 50vw; min-height: 280px; }
      .hero-left { padding: 3rem 1.5rem; }
      .hero-line span { font-size: clamp(2.2rem, 8vw, 3.2rem); }
    }
"""
new_html = """  <!-- HERO -->
  <section class="hero" id="home">

    <!-- LEFT PANEL — dark ink -->
    <div class="hero-left">
      <p class="hero-eyebrow">Koramangala, Bangalore</p>
      <div class="hero-heading">
        <div class="hero-line"><span>Baked fresh,</span></div>
        <div class="hero-line"><span class="pink">with love,</span></div>
        <div class="hero-line"><span>for you.</span></div>
      </div>
      <p class="hero-sub">A little pink café making things that taste like someone actually cared.</p>
      <div class="hero-actions">
        <a href="menu.html" class="btn-primary">See Our Menu</a>
        <a href="https://wa.me/918884449239" class="btn-ghost" target="_blank">Order via WhatsApp →</a>
      </div>
    </div>

    <!-- RIGHT PANEL — pink, floating circles -->
    <div class="hero-right" id="heroRight">
      <div class="float-field" id="floatField"></div>
      <div class="hero-right-label">
        <span>Open Daily</span>
        <span class="dot">·</span>
        <span>Fresh Every Morning</span>
      </div>
    </div>

  </section>

  <!-- MARQUEE — sits right below hero -->
  <div class="marquee-strip">
    <div class="marquee-track">
      <span>Freshly Baked</span><span class="mdot">·</span>
      <span>Made with Love</span><span class="mdot">·</span>
      <span>Pink Café</span><span class="mdot">·</span>
      <span>Koramangala</span><span class="mdot">·</span>
      <span>Custom Cakes</span><span class="mdot">·</span>
      <span>Open Daily</span><span class="mdot">·</span>
      <span>Freshly Baked</span><span class="mdot">·</span>
      <span>Made with Love</span><span class="mdot">·</span>
      <span>Pink Café</span><span class="mdot">·</span>
      <span>Koramangala</span><span class="mdot">·</span>
      <span>Custom Cakes</span><span class="mdot">·</span>
      <span>Open Daily</span><span class="mdot">·</span>
    </div>
  </div>
"""

new_js = """    // ── FLOATING CIRCLES ──
    const photos = [
      'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1572490122747-3a3cca73e5eb?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=300&h=300&fit=crop&crop=center',
      'https://images.unsplash.com/photo-1519985176271-adb1088fa94c?w=300&h=300&fit=crop&crop=center',
    ];

    const sizes = [80, 110, 70, 130, 90, 75, 115];
    const positions = [
      { top: '8%',  left: '12%' },
      { top: '18%', left: '58%' },
      { top: '42%', left: '22%' },
      { top: '55%', left: '68%' },
      { top: '72%', left: '38%' },
      { top: '30%', left: '78%' },
      { top: '80%', left: '10%' },
    ];
    const durations = ['7s','9s','6s','11s','8s','10s','7.5s'];
    const delays    = ['0s','1.2s','0.6s','2s','1.5s','0.3s','1.8s'];

    const field = document.getElementById('floatField');
    if (field) {
      photos.forEach((src, i) => {
        const s = sizes[i];
        const el = document.createElement('div');
        el.className = 'float-circle';
        el.style.cssText = `width:${s}px;height:${s}px;top:${positions[i].top};left:${positions[i].left};--dur:${durations[i]};--delay:${delays[i]};`;
        const img = document.createElement('img');
        img.src = src;
        img.alt = '';
        img.loading = 'lazy';
        el.appendChild(img);
        field.appendChild(el);
      });
    }

    // ── PINK CURSOR TRAIL (hero right panel only) ──
    const heroRight = document.getElementById('heroRight');
    if (heroRight) {
      heroRight.addEventListener('mousemove', (e) => {
        const dot = document.createElement('div');
        dot.className = 'cursor-dot';
        const size = Math.random() * 12 + 6;
        dot.style.cssText = `width:${size}px;height:${size}px;left:${e.clientX}px;top:${e.clientY}px;opacity:0.7;`;
        document.body.appendChild(dot);
        setTimeout(() => { dot.style.opacity = '0'; dot.style.width = '2px'; dot.style.height = '2px'; }, 80);
        setTimeout(() => dot.remove(), 500);
      });
    }

    // ── NAV SHRINK ON SCROLL ──
    const nav = document.querySelector('nav');
    if (nav) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 60) {
          nav.style.padding = '0.9rem 4rem';
          nav.style.boxShadow = '0 4px 24px var(--shadow)';
        } else {
          nav.style.padding = '1.4rem 4rem';
          nav.style.boxShadow = 'none';
        }
      });
    }
"""

new_lines = lines[:116] + [new_css + "\\n"] + lines[314:925] + [new_html + "\\n"] + lines[956:1122] + [new_js + "\\n"] + lines[1127:]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
