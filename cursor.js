/* ── 2 Rabbits Bakes — Blush Particle Trail Cursor ──
 * 18 blush-pink dots that daisy-chain after the mouse
 * Each dot lerps toward the one ahead — creating a
 * soft, breathing, fading ribbon. No frameworks needed.
 * Touch devices: fully skipped, default behaviour kept.
 */
(function () {

  // ── Skip on touch / mobile ──────────────────────────
  const isTouch = window.matchMedia('(hover: none)').matches
    || navigator.maxTouchPoints > 0;
  if (isTouch) return;

  // ── Config ──────────────────────────────────────────
  const NUM_DOTS   = 18;
  const LERP_LEAD  = 0.18;   // lead dot responsiveness
  const LERP_STEP  = 0.012;  // each subsequent dot is slightly lazier
  const DOT_SIZE   = 8;      // px
  const OP_FRONT   = 0.85;
  const OP_BACK    = 0.10;
  const COLOR      = '#fce8ef';

  // ── State ────────────────────────────────────────────
  let mouseX = -200, mouseY = -200;  // off-screen until first move
  let started = false;

  // ── Build dots ───────────────────────────────────────
  const positions = Array.from({ length: NUM_DOTS }, () => ({
    x: -200, y: -200
  }));

  const elements = positions.map((_, i) => {
    const el = document.createElement('div');
    // opacity fades from front → tail
    const t = i / (NUM_DOTS - 1);
    const opacity = OP_FRONT + t * (OP_BACK - OP_FRONT);

    Object.assign(el.style, {
      width:           `${DOT_SIZE}px`,
      height:          `${DOT_SIZE}px`,
      background:      COLOR,
      borderRadius:    '50%',
      position:        'fixed',
      top:             '0',
      left:            '0',
      pointerEvents:   'none',
      zIndex:          '10000',
      opacity:         String(opacity),
      willChange:      'transform',
      // No transition — we drive position ourselves via rAF
    });

    document.body.appendChild(el);
    return el;
  });

  // ── Mouse tracking ────────────────────────────────────
  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    if (!started) {
      // Snap all dots to cursor on very first move
      positions.forEach(p => { p.x = mouseX; p.y = mouseY; });
      started = true;
    }
  });

  // ── Animation loop ────────────────────────────────────
  function lerp(a, b, t) { return a + (b - a) * t; }

  function tick() {
    if (started) {
      // Dot 0 chases the actual mouse
      const lerpFactor0 = LERP_LEAD;
      positions[0].x = lerp(positions[0].x, mouseX, lerpFactor0);
      positions[0].y = lerp(positions[0].y, mouseY, lerpFactor0);

      // Each subsequent dot chases the one before it,
      // with a slightly lower lerp factor → creates the ribbon lag
      for (let i = 1; i < NUM_DOTS; i++) {
        const factor = Math.max(LERP_LEAD - i * LERP_STEP, 0.04);
        positions[i].x = lerp(positions[i].x, positions[i - 1].x, factor);
        positions[i].y = lerp(positions[i].y, positions[i - 1].y, factor);
      }

      // Apply transforms — center each dot (offset by half its size)
      const half = DOT_SIZE / 2;
      for (let i = 0; i < NUM_DOTS; i++) {
        elements[i].style.transform =
          `translate3d(${positions[i].x - half}px,${positions[i].y - half}px,0)`;
      }
    }

    requestAnimationFrame(tick);
  }

  // Start the loop — it will idle (no-op) until first mouse move
  requestAnimationFrame(tick);

})();
