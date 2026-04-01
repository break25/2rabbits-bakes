import os

def update_file():
    target_file = "c:\\Users\\Admin\\Documents\\2 rabit-website\\index.html"
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. HTML Replacement
    old_html = """        <div class="tilt-card-wrap" id="tiltCard">
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
        </div>"""
        
    new_html = """        <div class="rabbit-stage" id="tiltCard">
          <div class="rabbit-glow"></div>
          <svg class="rabbit-svg" viewBox="0 0 320 400" xmlns="http://www.w3.org/2000/svg" fill="none">
            
            <!-- left ear -->
            <ellipse class="ear ear-left" cx="110" cy="110" rx="28" ry="70"
              stroke="#8B3A52" stroke-width="2.5"
              transform="rotate(-12 110 110)"/>
            <ellipse cx="110" cy="115" rx="14" ry="52"
              fill="#F9D0DA" opacity="0.6"
              transform="rotate(-12 110 115)"/>

            <!-- right ear -->
            <ellipse class="ear ear-right" cx="210" cy="105" rx="28" ry="70"
              stroke="#8B3A52" stroke-width="2.5"
              transform="rotate(12 210 105)"/>
            <ellipse cx="210" cy="110" rx="14" ry="52"
              fill="#F9D0DA" opacity="0.6"
              transform="rotate(12 210 110)"/>

            <!-- body -->
            <ellipse cx="160" cy="290" rx="85" ry="95"
              fill="#FDF0F4" stroke="#8B3A52" stroke-width="2.5"/>

            <!-- head -->
            <circle cx="160" cy="185" r="75"
              fill="#FDF0F4" stroke="#8B3A52" stroke-width="2.5"/>

            <!-- cheek blush left -->
            <ellipse cx="125" cy="200" rx="18" ry="10" fill="#F2A7B8" opacity="0.5"/>
            <!-- cheek blush right -->
            <ellipse cx="195" cy="200" rx="18" ry="10" fill="#F2A7B8" opacity="0.5"/>

            <!-- eyes -->
            <circle class="eye" cx="140" cy="178" r="6" fill="#8B3A52"/>
            <circle cx="142" cy="176" r="2" fill="white"/>
            <circle class="eye" cx="180" cy="178" r="6" fill="#8B3A52"/>
            <circle cx="182" cy="176" r="2" fill="white"/>

            <!-- nose -->
            <ellipse cx="160" cy="196" rx="5" ry="3.5" fill="#C4687A"/>

            <!-- mouth -->
            <path d="M150 202 Q160 212 170 202"
              stroke="#8B3A52" stroke-width="1.8" stroke-linecap="round"/>

            <!-- tummy circle -->
            <ellipse cx="160" cy="295" rx="48" ry="55"
              fill="#F9D0DA" opacity="0.5" stroke="#C4687A"
              stroke-width="1.2" stroke-dasharray="4 4"/>

            <!-- little cake held by rabbit -->
            <rect x="135" y="310" width="50" height="32"
              rx="3" fill="#F2A7B8" stroke="#8B3A52" stroke-width="1.8"/>
            <rect x="130" y="306" width="60" height="10"
              rx="2" fill="#C4687A" stroke="#8B3A52" stroke-width="1.5"/>
            <!-- candle -->
            <rect x="157" y="292" width="6" height="16"
              rx="2" fill="#FDF6F0" stroke="#8B3A52" stroke-width="1.2"/>
            <!-- flame -->
            <ellipse class="flame" cx="160" cy="290" rx="4" ry="6" fill="#F2A7B8" opacity="0.9"/>

            <!-- left arm -->
            <path d="M82 265 Q60 280 75 310"
              stroke="#8B3A52" stroke-width="2.5" stroke-linecap="round"/>
            <!-- right arm -->
            <path d="M238 265 Q260 280 245 310"
              stroke="#8B3A52" stroke-width="2.5" stroke-linecap="round"/>

            <!-- tiny stars around rabbit -->
            <text class="star s1" x="48"  y="155" font-size="14" fill="#C4687A" opacity="0.7">✦</text>
            <text class="star s2" x="258" y="140" font-size="10" fill="#F2A7B8" opacity="0.8">✦</text>
            <text class="star s3" x="70"  y="320" font-size="8"  fill="#8B3A52" opacity="0.5">✦</text>
            <text class="star s4" x="260" y="310" font-size="12" fill="#C4687A" opacity="0.6">✦</text>

          </svg>
        </div>"""

    if old_html in content:
        content = content.replace(old_html, new_html)
    else:
        print("Could not find HTML to replace.")

    # 2. CSS Replacement - removing old tilt CSS and adding new rabbit CSS
    old_css = """/* RIGHT COLUMN — tilt card */
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

.card-dot { color: var(--shop-pink); }"""

    new_css_rabbit = """/* RIGHT COLUMN — tilt card */
.hero-visual-col {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  animation: fadeSlideUp 0.9s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;
}

.rabbit-stage {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
  transform-style: preserve-3d;
  transition: transform 0.1s ease-out;
  will-change: transform;
}

.rabbit-glow {
  position: absolute;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(242,167,184,0.45) 0%, transparent 70%);
  animation: glowPulse 4s ease-in-out infinite;
  pointer-events: none;
}

.rabbit-svg {
  width: 100%;
  max-width: 340px;
  height: auto;
  animation: rabbitBounce 3.5s ease-in-out infinite;
  filter: drop-shadow(0 20px 40px rgba(139,58,82,0.12));
}

.ear-left { animation: earWiggleL 3.5s ease-in-out infinite; transform-origin: 110px 160px; }
.ear-right { animation: earWiggleR 3.5s ease-in-out infinite; transform-origin: 210px 160px; }
.flame { animation: flameFlicker 0.8s ease-in-out infinite alternate; transform-origin: 160px 290px; }
.eye { animation: blink 5s ease-in-out infinite; }

.star { animation: starTwinkle 3s ease-in-out infinite; }
.s1 { animation-delay: 0s; }
.s2 { animation-delay: 0.8s; }
.s3 { animation-delay: 1.4s; }
.s4 { animation-delay: 2s; }

@keyframes rabbitBounce {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-14px); }
}

@keyframes earWiggleL {
  0%, 100% { transform: rotate(0deg); }
  20%       { transform: rotate(-6deg); }
  40%       { transform: rotate(3deg); }
}

@keyframes earWiggleR {
  0%, 100% { transform: translateX(0deg); }
  20%       { transform: rotate(6deg); }
  40%       { transform: rotate(-3deg); }
}

@keyframes flameFlicker {
  from { transform: scaleY(1) scaleX(1); opacity: 0.9; }
  to   { transform: scaleY(1.3) scaleX(0.8); opacity: 0.6; }
}

@keyframes glowPulse {
  0%, 100% { transform: scale(1); opacity: 0.6; }
  50%       { transform: scale(1.15); opacity: 0.9; }
}

@keyframes blink {
  0%, 90%, 100% { transform: scaleY(1); }
  95%            { transform: scaleY(0.1); }
}

@keyframes starTwinkle {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50%       { opacity: 1;   transform: scale(1.2); }
}"""

    if old_css in content:
        content = content.replace(old_css, new_css_rabbit)
    else:
        print("Could not find CSS to replace.")
        
    # Also remove `.tilt-card-wrap` from responsive css (max-width: 900px)
    res_css_old = ".tilt-card-wrap { width: 100%; }"
    if res_css_old in content:
        content = content.replace(res_css_old, ".rabbit-stage { width: 100%; }")

    res_css_old_img = ".hero-food-img { height: 320px; }"
    if res_css_old_img in content:
        content = content.replace(res_css_old_img, "")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_file()
