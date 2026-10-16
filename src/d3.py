from gen import *

css = '''
body{background:#0e0d0c;color:#ece4d4;font-family:'Plus Jakarta Sans','Noto Serif TC',sans-serif;font-weight:300}
.ch{color:#d9bf8c}.serif{font-family:'Playfair Display','Noto Serif TC',serif}
#lead{position:fixed;inset:0;z-index:50;background:#0e0d0c;display:grid;place-items:center;transition:opacity .8s,visibility .8s}
#lead.done{opacity:0;visibility:hidden}
#lead svg{width:220px}#lead .sw{transform-origin:110px 110px;animation:sweep 1s linear 3}
@keyframes sweep{to{transform:rotate(360deg)}}
#lead .n{font-size:90px;font-weight:700}
.hero{min-height:min(100vh,960px);display:grid;place-items:center;text-align:center;overflow:hidden;background:radial-gradient(ellipse at 50% 40%,#2a241b,#0e0d0c 70%)}
.hero h1{font-size:clamp(48px,9vw,120px);font-weight:400;letter-spacing:.02em}
.big{display:flex;justify-content:center;align-items:center;gap:3vw;font-size:clamp(60px,12vw,160px);font-weight:200;line-height:1;margin-bottom:20px}
.big .m{transform:scaleX(-1);display:inline-block;opacity:.25}
.grain{position:fixed;inset:0;pointer-events:none;opacity:.07;z-index:40;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.sh h2{font-family:'Playfair Display','Noto Serif TC';font-weight:400;font-size:clamp(32px,4.5vw,52px)}.sh .n{color:#d9bf8c}
.strip{display:flex;gap:0;overflow-x:auto;background:#1b1916;padding:34px 0;scroll-snap-type:x mandatory;transform:translateX(calc(var(--sy,0)*-.05px + 60px))}
.strip::before,.strip::after{content:''}
.film{background:#1b1916;position:relative;padding:30px 0}
.film:before,.film:after{content:'';position:absolute;left:0;right:0;height:14px;background:repeating-linear-gradient(90deg,transparent 0 12px,#0e0d0c 12px 26px);}
.film:before{top:8px}.film:after{bottom:8px}
.frames{display:flex;gap:14px;overflow-x:auto;padding:0 6vw;scroll-snap-type:x mandatory;scrollbar-width:none}
.fr{flex:0 0 320px;scroll-snap-align:center;background:#0e0d0c;padding:14px;border-radius:4px;border:1px solid #d9bf8c33;cursor:pointer}
.fr .img{aspect-ratio:3/2;border-radius:2px;position:relative;overflow:hidden}
.fr .img img{width:100%;height:100%;object-fit:cover;display:block;filter:sepia(.2) contrast(1.05);transition:transform .5s}
.fr:hover .img img{transform:scale(1.05)}
.fr .img b{position:absolute;right:10px;top:8px;font-size:12px;color:#d9bf8c;font-weight:500;background:rgba(0,0,0,.6);padding:2px 6px;border-radius:3px;backdrop-filter:blur(2px)}
.fr .d{font-size:22px;margin-top:12px}.fr h3{font-weight:500;font-size:16px;margin:6px 0}.fr p{font-size:14px;opacity:.7;line-height:1.7}
.pass{display:grid;grid-template-columns:2.2fr 1fr;background:linear-gradient(135deg,#f3ead7,#e2d3b2);color:#1b1916;border-radius:18px;max-width:900px;margin:0 auto;box-shadow:0 40px 80px #000a;overflow:hidden}
.pass .main{padding:36px 40px;border-right:2px dashed #1b191655;position:relative}
.pass .stub{padding:36px 28px;display:grid;align-content:space-between;gap:20px}
.pass .lab{font-size:11px;letter-spacing:.25em;opacity:.6}.pass .v{font-size:20px;font-weight:600}
.route{display:flex;align-items:center;gap:18px;margin:22px 0}.route .c{font-family:'Playfair Display';font-size:clamp(28px,4vw,46px);font-weight:700}
.route .ln{flex:1;height:1px;background:#1b1916;position:relative;min-width:40px}.route .ln:after{content:'✈';position:absolute;left:50%;top:-12px;font-size:18px}
.pf{display:grid;grid-template-columns:repeat(4,auto);gap:18px 26px}
.bars{height:54px;background:repeating-linear-gradient(90deg,#1b1916 0 2px,transparent 2px 4px,#1b1916 4px 7px,transparent 7px 9px,#1b1916 9px 10px,transparent 10px 13px)}
.det{border:1px solid #d9bf8c44;padding:34px;border-radius:12px;background:#161412}
.det h3{font-family:'Playfair Display','Noto Serif TC';font-weight:400;font-size:24px;margin-bottom:12px;color:#d9bf8c}.det p{line-height:1.9}
.map{background:radial-gradient(circle at 55% 45%,#d9bf8c33,transparent 30%),repeating-radial-gradient(circle at 55% 45%,transparent 0 30px,#d9bf8c18 30px 31px),#161412;border:1px solid #d9bf8c33}
.map p{position:absolute;bottom:16px;width:100%;text-align:center;font-size:14px;opacity:.7}
.cd-unit{border-color:#d9bf8c55;background:rgba(27,25,22,.8);color:#ece4d4}
.cd-val{color:#d9bf8c}
.cal-btn{border-color:#d9bf8c;color:#d9bf8c}
.cal-btn:hover{background:#d9bf8c20;color:#fff}
button.b{font:inherit;padding:14px;background:#d9bf8c;color:#0e0d0c;border:0;border-radius:40px;font-weight:600;letter-spacing:.2em;cursor:pointer}
button.b:hover{background:#f3ead7}
form.rsvp input,form.rsvp select,form.rsvp textarea{border-color:#d9bf8c55}
details{border-color:#d9bf8c33}
footer{text-align:center;padding:60px 6vw 90px;font-size:13px;letter-spacing:.3em;opacity:.7}
@media(max-width:760px){.pass{grid-template-columns:1fr}.pass .main{border-right:0;border-bottom:2px dashed #1b191655;padding:28px 24px}.pf{grid-template-columns:repeat(2,auto)}.fr{flex-basis:78vw}.route{gap:10px}.route .c{font-size:24px}.route .ln{min-width:24px}}
'''

# 菲林 35mm 故事相片 (4 格故事)
film_story_photos = [
    ("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80", "FRAME 01A · 03.21 遇見"),
    ("https://images.unsplash.com/photo-1529636798458-92182e662485?auto=format&fit=crop&w=800&q=80", "FRAME 02A · 黑白光影 初心"),
    ("https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=800&q=80", "FRAME 03A · 夕陽許諾 誓約"),
    ("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?auto=format&fit=crop&w=800&q=80", "FRAME 04A · 2027.01.23 永遠")
]

frames = ''.join(f'''<div class="fr tilt rv" data-cap="{film_story_photos[i][1]}">
  <div class="img">
    <img src="{film_story_photos[i][0]}" alt="{t}" loading="lazy">
    <b class="num">{i+1:02d}A</b>
  </div>
  <div class="d num ch">{d}</div>
  <h3 class="zh">{t}</h3>
  <p class="zh">{p}</p>
</div>''' for i, (d, t, p, _) in enumerate(STORY))

# 菲林 6 張拍立得/電影感相片
film_photos = [
    ("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=1000&q=80", "35mm · 街角回眸"),
    ("https://images.unsplash.com/photo-1529636798458-92182e662485?auto=format&fit=crop&w=1000&q=80", "B&W · 光影留白"),
    ("https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=1000&q=80", "Golden Hour · 奔向黃昏"),
    ("https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=1000&q=80", "Ring Detail · 恆久印記"),
    ("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?auto=format&fit=crop&w=1000&q=80", "Candid · 最自然的你"),
    ("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=1000&q=80", "Forever Love · 相伴同行")
]

gal = ''.join(f'''<div class="rv" data-cap="{cap}">
  <img src="{url}" alt="{cap}" loading="lazy">
  <span class="num">{cap}</span>
</div>''' for url, cap in film_photos)

stamp = seal('t', 'ADMIT TWO', '0123', '↔ 0321 ↔', 'none', '#8a6d45', 110, "'Plus Jakarta Sans',sans-serif")

body = f'''<div class="grain"></div><div id="lead"><div style="position:relative;display:grid;place-items:center"><svg viewBox="0 0 220 220"><circle cx="110" cy="110" r="100" fill="none" stroke="#d9bf8c55"/><circle cx="110" cy="110" r="80" fill="none" stroke="#d9bf8c33"/><line x1="0" y1="110" x2="220" y2="110" stroke="#d9bf8c33"/><line x1="110" y1="0" x2="110" y2="220" stroke="#d9bf8c33"/><path class="sw" d="M110 110 L110 10 A100 100 0 0 1 210 110z" fill="#d9bf8c22"/></svg><div class="n num ch" id="cnt" style="position:absolute">3</div></div></div>
<section class="hero"><div class="rv"><div class="big num ch"><span>1.23</span><span style="font-size:.3em;opacity:.6">↔</span><span>3.21</span></div>
<p style="letter-spacing:.6em;font-size:13px" class="ch">A LOVE STORY IN 35MM · 愛情菲林</p><h1 class="serif">Christy &amp; Tim</h1><p style="margin-top:18px;letter-spacing:.3em"><span class="num">SAT 23 JAN 2027</span> · <span class="zh">地點待定 Venue TBC</span></p></div></section>

<!-- 菲林倒數計時 -->
<section style="padding:40px 6vw 0"><div class="wrap">{countdown_html("COUNTDOWN TO TAKE OFF · 啟程倒計時")}</div></section>

<section style="padding-left:0;padding-right:0"><div class="wrap" style="padding:0 6vw"><div class="sh rv"><span class="n num">01</span><h2>Our Story</h2><span class="zh">我們的故事</span></div><p class="rv zh serif" style="font-size:22px;margin-bottom:36px;font-style:italic">由 <span class="num">3.21</span> 到 <span class="num">1.23</span> — rewind the reel, the numbers read the same way back.</p></div>
<div class="film"><div class="frames">{frames}</div></div><p class="zh" style="text-align:center;margin-top:14px;font-size:12px;opacity:.5;letter-spacing:.2em">← 左右拖動 SWIPE 膠卷 · 點擊相片放大 →</p></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">02</span><h2>Boarding Pass</h2><span class="zh">登機證 · 邀請</span></div>
<div class="pass tilt rv"><div class="main"><div class="lab">INVITATION · 誠邀閣下登上愛情航班</div>{guest_greeting_html("貴賓 GUEST")}
<div class="route"><span class="c">CHRISTY &amp; TIM</span><span class="ln"></span><span class="c">FOREVER</span></div>
<div class="pf"><div><div class="lab">PASSENGER</div><div class="v zh guest-name-slot">貴賓 GUEST</div></div><div><div class="lab">DATE</div><div class="v num">2027.01.23</div></div><div><div class="lab">BOARDING</div><div class="v num">15:30</div></div><div><div class="lab">FLIGHT</div><div class="v num">CT0123</div></div><div><div class="lab">GATE</div><div class="v zh">LOVE01</div></div></div></div>
<div class="stub"><div><div class="lab">SEAT</div><div class="v num">03 · 21</div></div>{stamp}<div class="bars"></div></div></div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">03</span><h2>The Day</h2><span class="zh">婚禮詳情</span></div><div class="grid2">
<div class="det tilt rv"><h3>Ceremony · 菲林放映與證婚</h3><p class="zh"><span class="num">2027.01.23 · 15:30</span><br>神秘菲林放映場地 (Venue TBC)<br>地址稍後透過登機確認發送<br><span style="opacity:.7;font-size:13px">見證 35mm 菲林故事定格一刻</span></p></div>
<div class="det tilt rv"><h3>Banquet · 慶祝晚宴</h3><p class="zh">迎賓入場 <span class="num">18:00</span> · 晚宴 <span class="num">19:30</span><br>私人宴會酒會空間 (Venue TBC)<br>音樂、美酒、菲林與老朋友<br><span style="opacity:.7;font-size:13px">Cocktails &amp; Dinner with Christy &amp; Tim</span></p></div></div>
{calendar_html()}
</div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">04</span><h2>Venue</h2><span class="zh">場地與導航</span></div><div class="map rv"><p class="zh" style="display:flex;justify-content:center;align-items:center;gap:12px;width:100%"><a href="https://maps.google.com/?q=The+Murray+Hong+Kong" target="_blank" rel="noopener" style="color:#d9bf8c;font-weight:600;text-decoration:underline">在 Google 地圖打開 (Open in Google Maps) →</a></p></div></div></section>

<section><div class="wrap grid2"><div class="rv"><div class="sh"><span class="n num">05</span><h2>Dress Code</h2></div><p class="zh" style="line-height:1.9">Black Tie Optional / Cinematic Retro<br>電影感復古正裝。<br>建議色調：經典黑、香檳金、暖大地深啡。</p><div style="display:flex;gap:14px;margin-top:20px"><i style="width:56px;height:56px;border-radius:50%;background:#000;box-shadow:0 0 0 1px #d9bf8c" title="經典黑"></i><i style="width:56px;height:56px;border-radius:50%;background:#d9bf8c" title="香檳金"></i><i style="width:56px;height:56px;border-radius:50%;background:#5a4630" title="深啡色"></i></div></div>
<div class="rv"><div class="sh"><span class="n num">06</span><h2>RSVP</h2></div>{rsvp('b')}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">07</span><h2>Gallery</h2><span class="zh">菲林相片集 · 點擊查看大圖</span></div><div class="gal">{gal}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">08</span><h2>FAQ</h2><span class="zh">常見問題</span></div>{faq()}</div></section>

<footer class="num">CT0123 ↔ 0321 · THE END · 完</footer>'''

js = '''<script>const L=document.getElementById('lead'),c=document.getElementById('cnt');let n=3;const t=setInterval(()=>{n--;if(n>0)c.textContent=n;else{clearInterval(t);L.classList.add('done')}},800);if(location.hash.includes('shot'))L.remove();</script>'''

open('03-film.html', 'w').write(page('Christy & Tim · Forever', css, body, js))
