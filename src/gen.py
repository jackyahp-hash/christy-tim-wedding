import textwrap

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;500;700&family=Noto+Serif+TC:wght@300;500;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,500;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">'

COMMON_CSS = '''
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{overflow-x:hidden;-webkit-font-smoothing:antialiased}
.num{font-family:'Plus Jakarta Sans',sans-serif;font-variant-numeric:tabular-nums}
.zh{word-break:keep-all;line-break:strict}
section{padding:110px 6vw;position:relative}.wrap{max-width:1080px;margin:0 auto}
.rv{opacity:0;transform:translateY(40px);transition:opacity 1s cubic-bezier(.2,.7,.2,1),transform 1s cubic-bezier(.2,.7,.2,1)}.rv.in{opacity:1;transform:none}
.tilt{transform-style:preserve-3d;will-change:transform;position:relative}
.tilt .glare{position:absolute;inset:0;border-radius:inherit;pointer-events:none;mix-blend-mode:overlay;opacity:0;transition:opacity .4s}
.tilt:hover .glare{opacity:1}
.sh{display:flex;align-items:baseline;gap:18px;margin-bottom:48px;flex-wrap:wrap}.sh .n{font-size:14px;letter-spacing:.3em}
form.rsvp{display:grid;gap:16px;max-width:560px}form.rsvp label{display:grid;gap:6px;font-size:14px}
form.rsvp input,form.rsvp select,form.rsvp textarea{font:inherit;padding:12px 14px;border-radius:6px;border:1px solid currentColor;background:transparent;color:inherit}
form.rsvp select option{color:#222}
details{border-bottom:1px solid currentColor;padding:18px 0}details summary{cursor:pointer;list-style:none;font-weight:500}details p{margin-top:10px;opacity:.8;line-height:1.8}

/* 個人化賓客專屬卡片 (Personalized Guest Badge) */
.guest-box{display:none;margin:12px auto 20px;padding:8px 20px;border-radius:30px;background:rgba(255,255,255,.12);backdrop-filter:blur(8px);border:1px solid currentColor;max-width:max-content;font-size:14px;letter-spacing:.15em;animation:glowGuest 3s infinite alternate}
@keyframes glowGuest{from{box-shadow:0 0 10px rgba(255,255,255,.1)}to{box-shadow:0 0 25px rgba(212,168,73,.45)}}

/* 相片畫廊 Gallery */
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.gal>div{aspect-ratio:4/5;border-radius:8px;position:relative;overflow:hidden;cursor:pointer;background:#222}
.gal>div img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .7s cubic-bezier(.25,.8,.25,1),filter .7s}
.gal>div:hover img{transform:scale(1.06);filter:brightness(1.05)}
.gal>div span{position:absolute;left:14px;bottom:12px;font-size:12px;letter-spacing:.15em;z-index:2;background:rgba(0,0,0,.45);backdrop-filter:blur(4px);padding:4px 10px;border-radius:20px;pointer-events:none}
.gal>div:after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.6) 0%,transparent 45%);opacity:.85;pointer-events:none}

.grid2{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.map{aspect-ratio:16/9;border-radius:10px;position:relative;overflow:hidden}
.ph{opacity:.7;font-size:.9em}

/* 倒數計時模組 */
.cd-section{margin:36px 0 20px;text-align:center}
.cd-title{font-size:13px;letter-spacing:.3em;text-transform:uppercase;opacity:.8;margin-bottom:16px}
.countdown-box{display:inline-flex;gap:14px;flex-wrap:wrap;justify-content:center}
.cd-unit{min-width:76px;padding:14px 10px;border-radius:10px;border:1px solid currentColor;background:rgba(255,255,255,.04);backdrop-filter:blur(6px);text-align:center}
.cd-val{font-size:clamp(26px,4vw,38px);font-weight:700;line-height:1}
.cd-lbl{font-size:11px;letter-spacing:.2em;opacity:.75;margin-top:6px;text-transform:uppercase}

/* 加入日曆按鈕 */
.cal-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:20px}
.cal-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 18px;border-radius:30px;font-size:13px;letter-spacing:.15em;text-decoration:none;border:1px solid currentColor;color:inherit;transition:all .3s;cursor:pointer;background:transparent}
.cal-btn:hover{background:rgba(255,255,255,.15);transform:translateY(-2px)}
.cal-btn svg{width:16px;height:16px;fill:currentColor}

/* 懸浮浪漫音樂播放器 */
.bgm-btn{position:fixed;top:22px;right:22px;z-index:90;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.3);background:rgba(18,18,18,.65);backdrop-filter:blur(10px);color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 10px 25px rgba(0,0,0,.35);transition:all .3s}
.bgm-btn:hover{transform:scale(1.08);background:rgba(18,18,18,.85)}
.bgm-btn.playing svg{animation:spinMusic 6s linear infinite}
.bgm-tooltip{position:absolute;right:52px;white-space:nowrap;font-size:11px;letter-spacing:.15em;background:rgba(0,0,0,.75);padding:4px 10px;border-radius:12px;opacity:0;pointer-events:none;transition:opacity .3s;color:#fff}
.bgm-btn:hover .bgm-tooltip{opacity:1}
@keyframes spinMusic{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}

/* 慶祝祝賀按鈕 (Celebration Confetti) */
.celebrate-btn{position:fixed;bottom:24px;right:22px;z-index:90;padding:12px 20px;border-radius:30px;background:linear-gradient(135deg,#c8102e,#d4a849);color:#fff;font-family:'Plus Jakarta Sans','Noto Serif TC',serif;font-size:13px;letter-spacing:.15em;font-weight:600;display:inline-flex;align-items:center;gap:8px;border:none;cursor:pointer;box-shadow:0 10px 30px rgba(0,0,0,.5);transition:all .3s}
.celebrate-btn:hover{transform:translateY(-3px) scale(1.04);box-shadow:0 15px 35px rgba(212,168,73,.5)}
.celebrate-btn:active{transform:scale(.96)}
#confettiCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:99}

/* 全螢幕相片燈箱 (Lightbox) */
.lightbox{position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:100;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .35s;padding:24px}
.lightbox.open{opacity:1;pointer-events:auto}
.lightbox img{max-width:90vw;max-height:82vh;object-fit:contain;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.8);transition:transform .3s}
.lightbox .lb-cap{color:#f0f0f0;font-size:14px;letter-spacing:.2em;margin-top:16px;text-align:center;font-family:'Plus Jakarta Sans','Noto Serif TC',sans-serif}
.lightbox .lb-close{position:absolute;top:24px;right:28px;background:none;border:none;color:#fff;font-size:32px;cursor:pointer;line-height:1;opacity:.8;transition:opacity .2s}
.lightbox .lb-close:hover{opacity:1}
.lightbox .lb-prev,.lightbox .lb-next{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.1);border:none;color:#fff;width:50px;height:50px;border-radius:50%;display:grid;place-items:center;cursor:pointer;font-size:20px;transition:background .2s}
.lightbox .lb-prev{left:24px}.lightbox .lb-next{right:24px}
.lightbox .lb-prev:hover,.lightbox .lb-next:hover{background:rgba(255,255,255,.25)}

/* 故事時間軸相片 */
.story-photo{width:100%;height:180px;border-radius:6px;overflow:hidden;margin-top:14px;position:relative;cursor:pointer}
.story-photo img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}
.story-photo:hover img{transform:scale(1.05)}

@media(max-width:760px){
  section{padding:80px 6vw}.grid2{grid-template-columns:1fr}
  .gal{grid-template-columns:1fr 1fr}
  .lightbox .lb-prev{left:10px}.lightbox .lb-next{right:10px}
  .celebrate-btn{bottom:18px;right:16px;padding:10px 16px;font-size:12px}
}
@media(max-width:480px){
  .gal{grid-template-columns:1fr}
  .countdown-box{gap:8px}
  .cd-unit{min-width:64px;padding:10px 6px}
  .cd-val{font-size:24px}
}
body.shot{min-height:0}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}}
'''

COMMON_JS = '''
<!-- 相片燈箱組件 -->
<div class="lightbox" id="lightbox">
  <button class="lb-close" id="lbClose" aria-label="關閉">&times;</button>
  <button class="lb-prev" id="lbPrev" aria-label="上一張">&#10094;</button>
  <img id="lbImg" src="" alt="婚禮相片">
  <div class="lb-cap" id="lbCap"></div>
  <button class="lb-next" id="lbNext" aria-label="下一張">&#10095;</button>
</div>

<!-- 浪漫音樂播放器 -->
<div class="bgm-btn" id="bgmBtn" title="浪漫背景音樂 BGM">
  <span class="bgm-tooltip">浪漫音樂 BGM</span>
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M9 18V5l12-2v13"></path>
    <circle cx="6" cy="18" r="3"></circle>
    <circle cx="18" cy="16" r="3"></circle>
  </svg>
</div>

<!-- 送上祝福互動按鈕與畫布 -->
<canvas id="confettiCanvas"></canvas>
<button class="celebrate-btn" id="celebrateBtn" type="button">
  <span>🥂 送上祝福</span>
  <span id="wishCountBadge" style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;font-size:11px">168</span>
</button>

<script>
// 1. 視口滾動動畫觀察器
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

// 2. 3D Tilt 卡片效果
document.querySelectorAll('.tilt').forEach(card=>{
  if(!card.querySelector('.glare')){const g=document.createElement('div');g.className='glare';card.appendChild(g)}
  const g=card.querySelector('.glare');let tx=0,ty=0,x=0,y=0,vx=0,vy=0,raf=null,gx=50,gy=50;
  const step=()=>{const k=.08,d=.78;vx=(vx+(tx-x)*k)*d;vy=(vy+(ty-y)*k)*d;x+=vx;y+=vy;
    card.style.transform=`perspective(1000px) rotateX(${y}deg) rotateY(${x}deg)`;
    g.style.background=`radial-gradient(circle at ${gx}% ${gy}%,rgba(255,255,255,.75),rgba(255,255,255,0) 55%)`;
    if(Math.abs(vx)+Math.abs(vy)+Math.abs(tx-x)+Math.abs(ty-y)>.01)raf=requestAnimationFrame(step);else raf=null};
  const kick=()=>{if(!raf)raf=requestAnimationFrame(step)};
  card.addEventListener('pointermove',e=>{if(e.pointerType!=='mouse')return;const r=card.getBoundingClientRect(),px=(e.clientX-r.left)/r.width,py=(e.clientY-r.top)/r.height;tx=(px-.5)*16;ty=(.5-py)*16;gx=px*100;gy=py*100;kick()});
  card.addEventListener('pointerleave',()=>{tx=0;ty=0;kick()});
});

// 3. RSVP 表單回覆處理
document.querySelectorAll('form.rsvp').forEach(f=>f.addEventListener('submit',e=>{
  e.preventDefault();
  const o=f.querySelector('.ok');
  if(o){o.hidden=false;o.style.display='block'}
  const btn=f.querySelector('button');
  if(btn){btn.disabled=true;btn.textContent='已成功送出 · Thank you!'}
  triggerConfetti(window.innerWidth/2, window.innerHeight*0.7);
}));

if(location.hash.includes('shot'))document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));
addEventListener('scroll',()=>document.documentElement.style.setProperty('--sy',scrollY),{passive:true});

// 4. 2027.01.23 倒數計時器
const weddingDate = new Date('2027-01-23T00:00:00+08:00').getTime();
const updateCd = () => {
  const now = new Date().getTime();
  const diff = weddingDate - now;
  if(diff <= 0) {
    document.querySelectorAll('.cd-val-d').forEach(e=>e.textContent='0');
    document.querySelectorAll('.cd-val-h').forEach(e=>e.textContent='0');
    document.querySelectorAll('.cd-val-m').forEach(e=>e.textContent='0');
    document.querySelectorAll('.cd-val-s').forEach(e=>e.textContent='0');
    return;
  }
  const d = Math.floor(diff / (1000 * 60 * 60 * 24));
  const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const s = Math.floor((diff % (1000 * 60)) / 1000);
  document.querySelectorAll('.cd-val-d').forEach(e=>e.textContent=d);
  document.querySelectorAll('.cd-val-h').forEach(e=>e.textContent=String(h).padStart(2,'0'));
  document.querySelectorAll('.cd-val-m').forEach(e=>e.textContent=String(m).padStart(2,'0'));
  document.querySelectorAll('.cd-val-s').forEach(e=>e.textContent=String(s).padStart(2,'0'));
};
setInterval(updateCd, 1000);
updateCd();

// 5. 專屬賓客姓名解析 (Personalized URL ?to=名稱 或 ?guest=名稱)
const urlParams = new URLSearchParams(window.location.search);
const guestName = urlParams.get('to') || urlParams.get('guest');
if(guestName) {
  document.querySelectorAll('.guest-name-slot').forEach(el => {
    el.textContent = guestName;
  });
  document.querySelectorAll('.guest-box').forEach(el => {
    el.style.display = 'inline-block';
  });
  const nameInput = document.querySelector('form.rsvp input[placeholder*="你的名字"]');
  if(nameInput && !nameInput.value) nameInput.value = guestName;
}

// 6. 送上祝福特效 (Canvas Confetti & Particles)
const canvas = document.getElementById('confettiCanvas');
const ctx = canvas ? canvas.getContext('2d') : null;
let particles = [];

function resizeCanvas() {
  if(!canvas) return;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function triggerConfetti(originX, originY) {
  if(!canvas || !ctx) return;
  const colors = ['#d4a849', '#f7e3a1', '#c8102e', '#ffffff', '#e8cfc4', '#8fa587'];
  for(let i=0; i<50; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = 4 + Math.random() * 8;
    particles.push({
      x: originX || window.innerWidth - 60,
      y: originY || window.innerHeight - 60,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed - 3,
      size: 4 + Math.random() * 6,
      color: colors[Math.floor(Math.random() * colors.length)],
      alpha: 1,
      rotation: Math.random() * 360,
      rotSpeed: (Math.random() - 0.5) * 10
    });
  }
}

function updateParticles() {
  if(!ctx || !canvas) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for(let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.vy += 0.2; // 重力
    p.alpha -= 0.012;
    p.rotation += p.rotSpeed;
    
    if(p.alpha <= 0) {
      particles.splice(i, 1);
      continue;
    }
    
    ctx.save();
    ctx.globalAlpha = p.alpha;
    ctx.translate(p.x, p.y);
    ctx.rotate(p.rotation * Math.PI / 180);
    ctx.fillStyle = p.color;
    ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size * 1.5);
    ctx.restore();
  }
  requestAnimationFrame(updateParticles);
}
requestAnimationFrame(updateParticles);

let wishCount = parseInt(localStorage.getItem('ct_wishes') || '168', 10);
const wishBadge = document.getElementById('wishCountBadge');
if(wishBadge) wishBadge.textContent = wishCount;

const celBtn = document.getElementById('celebrateBtn');
if(celBtn) {
  celBtn.addEventListener('click', (e) => {
    wishCount += 1;
    localStorage.setItem('ct_wishes', wishCount);
    if(wishBadge) wishBadge.textContent = wishCount;
    const r = celBtn.getBoundingClientRect();
    triggerConfetti(r.left + r.width/2, r.top);
  });
}

// 7. 相片燈箱功能 (Lightbox)
const lb = document.getElementById('lightbox');
const lbImg = document.getElementById('lbImg');
const lbCap = document.getElementById('lbCap');
const lbClose = document.getElementById('lbClose');
const lbPrev = document.getElementById('lbPrev');
const lbNext = document.getElementById('lbNext');

let galleryItems = [];
let currentIdx = 0;

const initLightbox = () => {
  const photoEls = [...document.querySelectorAll('.gal>div, .story-photo, .fr .img')];
  galleryItems = photoEls.map(el => {
    const img = el.querySelector('img');
    const span = el.querySelector('span, b, .zh');
    return {
      src: img ? img.src : '',
      cap: span ? span.textContent.trim() : (el.getAttribute('data-cap') || 'Christy & Tim · Wedding Moments')
    };
  }).filter(item => item.src);

  photoEls.forEach(el => {
    el.addEventListener('click', () => {
      const img = el.querySelector('img');
      if(!img) return;
      const idx = galleryItems.findIndex(item => item.src === img.src);
      if(idx !== -1) openLightbox(idx);
    });
  });
};

const openLightbox = (idx) => {
  currentIdx = idx;
  lbImg.src = galleryItems[currentIdx].src;
  lbCap.textContent = galleryItems[currentIdx].cap;
  lb.classList.add('open');
};

const closeLightbox = () => lb.classList.remove('open');
const showPrev = (e) => { e.stopPropagation(); currentIdx = (currentIdx - 1 + galleryItems.length) % galleryItems.length; openLightbox(currentIdx); };
const showNext = (e) => { e.stopPropagation(); currentIdx = (currentIdx + 1) % galleryItems.length; openLightbox(currentIdx); };

if(lbClose) lbClose.addEventListener('click', closeLightbox);
if(lbPrev) lbPrev.addEventListener('click', showPrev);
if(lbNext) lbNext.addEventListener('click', showNext);
if(lb) lb.addEventListener('click', (e) => { if(e.target === lb || e.target === lbImg) closeLightbox(); });
document.addEventListener('keydown', (e) => {
  if(!lb.classList.contains('open')) return;
  if(e.key === 'Escape') closeLightbox();
  if(e.key === 'ArrowLeft') showPrev(e);
  if(e.key === 'ArrowRight') showNext(e);
});
setTimeout(initLightbox, 200);

// 8. 加入日曆 iCal (.ics) 下載功能
window.downloadICS = function() {
  const icsData = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Christy & Tim//Wedding 2027//ZH',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    'UID:wedding-christy-tim-20270123@wedding',
    'DTSTAMP:20261017T000000Z',
    'DTSTART;VALUE=DATE:20270123',
    'DTEND;VALUE=DATE:20270124',
    'SUMMARY:Christy & Tim 婚禮慶典 · Wedding Day',
    'DESCRIPTION:0123 ↔ 0321 由 3.21 到 1.23，倒轉都係我哋。誠邀見證 Christy & Tim 婚禮！',
    'LOCATION:Hong Kong (Venue TBC)',
    'STATUS:CONFIRMED',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\\r\\n');
  const blob = new Blob([icsData], { type: 'text/calendar;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'christy-tim-wedding-20270123.ics';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};

// 9. 輕柔浪漫鋼琴和弦 BGM (Web Audio API 合成，零外部依賴)
let audioCtx = null;
let isPlaying = false;
let bgmTimer = null;
const bgmBtn = document.getElementById('bgmBtn');

const weddingMelody = [
  // Canon / Romantic chords: D - A - Bm - F#m - G - D - G - A
  {f: 293.66, d: 1.6}, {f: 369.99, d: 0.8}, {f: 440.00, d: 0.8},
  {f: 220.00, d: 1.6}, {f: 329.63, d: 0.8}, {f: 440.00, d: 0.8},
  {f: 246.94, d: 1.6}, {f: 293.66, d: 0.8}, {f: 369.99, d: 0.8},
  {f: 185.00, d: 1.6}, {f: 277.18, d: 0.8}, {f: 369.99, d: 0.8},
  {f: 196.00, d: 1.6}, {f: 293.66, d: 0.8}, {f: 392.00, d: 0.8},
  {f: 146.83, d: 1.6}, {f: 293.66, d: 0.8}, {f: 369.99, d: 0.8},
  {f: 196.00, d: 1.6}, {f: 246.94, d: 0.8}, {f: 293.66, d: 0.8},
  {f: 220.00, d: 2.4}
];

function playNote(freq, dur, time) {
  if(!audioCtx) return;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = 'triangle';
  osc.frequency.setValueAtTime(freq, time);
  
  gain.gain.setValueAtTime(0.001, time);
  gain.gain.exponentialRampToValueAtTime(0.08, time + 0.05);
  gain.gain.exponentialRampToValueAtTime(0.0001, time + dur);
  
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(time);
  osc.stop(time + dur);
}

function startMusicLoop() {
  if(!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  if(audioCtx.state === 'suspended') audioCtx.resume();
  
  let now = audioCtx.currentTime + 0.1;
  weddingMelody.forEach(note => {
    playNote(note.f, note.d, now);
    playNote(note.f * 1.5, note.d * 0.8, now + 0.1);
    now += note.d * 0.7;
  });
  
  const totalDur = (now - audioCtx.currentTime) * 1000;
  bgmTimer = setTimeout(() => {
    if(isPlaying) startMusicLoop();
  }, totalDur);
}

if(bgmBtn) {
  bgmBtn.addEventListener('click', () => {
    if(!isPlaying) {
      isPlaying = true;
      bgmBtn.classList.add('playing');
      bgmBtn.setAttribute('title', '點擊暫停背景音樂');
      startMusicLoop();
    } else {
      isPlaying = false;
      bgmBtn.classList.remove('playing');
      bgmBtn.setAttribute('title', '點擊播放浪漫背景音樂');
      clearTimeout(bgmTimer);
    }
  });
}
</script>'''

def page(title, css, body, js=''):
    return f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>{FONTS}<style>{COMMON_CSS}{css}</style></head><body>{body}{COMMON_JS}{js}</body></html>'

def countdown_html(title="WEDDING COUNTDOWN · 婚禮倒計時"):
    return f'''<div class="cd-section rv">
  <div class="cd-title num">{title}</div>
  <div class="countdown-box num">
    <div class="cd-unit"><div class="cd-val cd-val-d">000</div><div class="cd-lbl">天 DAYS</div></div>
    <div class="cd-unit"><div class="cd-val cd-val-h">00</div><div class="cd-lbl">時 HRS</div></div>
    <div class="cd-unit"><div class="cd-val cd-val-m">00</div><div class="cd-lbl">分 MIN</div></div>
    <div class="cd-unit"><div class="cd-val cd-val-s">00</div><div class="cd-lbl">秒 SEC</div></div>
  </div>
</div>'''

def guest_greeting_html(default_label="誠邀親朋好友"):
    return f'''<div class="guest-box num">
  <span>DEAR </span><strong class="guest-name-slot">{default_label}</strong><span> · 誠邀光臨</span>
</div>'''

def calendar_html():
    gcal_url = "https://calendar.google.com/calendar/render?action=TEMPLATE&text=Christy+%26+Tim+Wedding+%E5%A9%9A%E7%A6%AE%E5%BA%86%E5%85%B8&dates=20270123T030000Z/20270123T150000Z&details=0123+%E2%86%94+0321+%E7%94%B1+3.21+%E5%88%B0+1.23%EF%BC%8C%E5%80%92%E8%BD%89%E9%83%BD%E4%BF%82%E6%88%91%E5%93%87%E3%80%82Christy+%26+Tim+%E7%B5%90%E5%A9%9A%E5%A4%A7%E5%96%9C%E4%B9%8B%E6%97%A5%EF%BC%81&location=Hong+Kong"
    return f'''<div class="cal-actions rv">
  <a class="cal-btn" href="{gcal_url}" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM9 14H7v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2zm-8 4H7v-2h2v2zm4 4H7v-2h2v2zm4 0h-2v-2h2v2z"/></svg>
    加到 Google 日曆
  </a>
  <button class="cal-btn" onclick="downloadICS()" type="button">
    <svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
    下載 Apple / iCal (.ics)
  </button>
</div>'''

def seal(id, top, mid, bot, fill, ink, size=150, font="'Noto Serif TC',serif"):
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}" aria-hidden="true"><defs><path id="c{id}" d="M28,100 a72,72 0 0,1 144,0"/><path id="b{id}" d="M18,100 a82,82 0 0,0 164,0"/></defs>
<circle cx="100" cy="100" r="96" fill="{fill}"/><circle cx="100" cy="100" r="86" fill="none" stroke="{ink}" stroke-width="1.5" stroke-dasharray="2 4"/>
<text font-family="{font}" font-size="15" letter-spacing="5" fill="{ink}"><textPath href="#c{id}" startOffset="50%" text-anchor="middle">{top}</textPath></text>
<text font-family="{font}" font-size="15" letter-spacing="5" fill="{ink}"><textPath href="#b{id}" startOffset="50%" text-anchor="middle" dominant-baseline="hanging">{bot}</textPath></text>
<text x="100" y="114" text-anchor="middle" font-family="{font}" font-size="42" font-weight="700" fill="{ink}">{mid}</text></svg>'''

FAQ = [
    ("可以帶小朋友嗎？ Can we bring kids?", "歡迎全家蒞臨，但請提前於 RSVP 告知人數以便我們安排座位 · Please let us know the guest count in RSVP so we can arrange seats!"),
    ("有冇泊車位？ Is parking available?", "場地提供代客泊車及鄰近停車場優惠，詳細停車指引稍後透過電郵/WhatsApp 發送 · Parking info will be sent closer to the date."),
    ("禮物 / 人情安排？ Gifts?", "大家的祝福與蒞臨是最好的禮物。若想送上心意，現場設有人情箱與電子禮金（PayMe / FPS）· Your presence is our best present!"),
    ("RSVP 截止日期？ RSVP deadline?", "請於 2026 年 11 月 30 日前填妥回覆，讓我們為大家準備最佳筵席 · Please RSVP by 30 Nov 2026.")
]

def faq():
    return ''.join(f'<details class="rv"><summary class="zh">{q}</summary><p class="zh">{a}</p></details>' for q,a in FAQ)

def rsvp(btn):
    return f'''<form class="rsvp rv"><label>姓名 Name<input required placeholder="你的名字 Your name"></label>
<label>出席 Attendance<select><option>欣然出席 Joyfully attend</option><option>未能出席 Regretfully decline</option></select></label>
<label>人數 Guests<input class="num" type="number" min="1" max="6" value="1"></label>
<label>晚宴點歌 Song Request 🎶<input placeholder="你最想在晚宴聽到邊首歌？ Favorite song for party"></label>
<label>飲食需要 Dietary notes<textarea rows="3" placeholder="素食 / 過敏 / 其他備註 Vegetarian / allergies"></textarea></label>
<button class="{btn}">送出回覆 Send RSVP</button><p class="ok zh" hidden style="color:#d4a849;font-weight:700;margin-top:10px">多謝你的回覆！我們期待在 2027.01.23 與你相聚！❤️<br><span style="font-size:12px;opacity:.8">（示範表單，已收錄回覆）</span></p></form>'''

# 故事節點（包含照片 URL）
STORY_PHOTOS = [
    "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1606800052052-a08af7148866?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=800&q=80"
]

STORY = [
    ("03.21", "Tim 的生日 · Tim's birthday", "故事由呢個春天日子開始。一組奇妙的數字 03.21，在時光裡悄悄埋下了相遇的伏線。", STORY_PHOTOS[0]),
    ("初遇", "相遇與心動 · First met", "那天在微風微醺的咖啡香裡初次相遇，對視的一刻，好像彼此已經認識了很久。", STORY_PHOTOS[1]),
    ("求婚", "承諾終生 · The proposal", "在滿天星光下許下相伴一生的誓約。「執子之手，與子偕老」，未來的每一天都有你。", STORY_PHOTOS[2]),
    ("2027.01.23", "婚禮大喜 · The wedding", "由 3.21 到 1.23 — 數字倒轉，剛好係我哋。翻轉歲月，愛意始終如一。", STORY_PHOTOS[3])
]

DATE = "2027.01.23"
