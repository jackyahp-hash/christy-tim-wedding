from gen import *

css = '''
body{background:#f7f2e7;color:#3d4a3a;font-family:'Cormorant Garamond','Noto Serif TC',serif;font-size:19px}
h1,h2{font-family:'Playfair Display','Noto Serif TC',serif;font-weight:400}
#env{position:fixed;inset:0;z-index:50;background:#e9e2d0;display:grid;place-items:center;transition:opacity 1.2s,visibility 1.2s}
#env.done{opacity:0;visibility:hidden}
.envl{width:min(520px,86vw);aspect-ratio:1.5;position:relative;background:#efe6d2;box-shadow:0 30px 60px rgba(60,70,50,.25);cursor:pointer}
.envl .fl{position:absolute;inset:0 0 40% 0;background:#e3d8bf;clip-path:polygon(0 0,100% 0,50% 100%);transform-origin:top;transition:transform 1s cubic-bezier(.6,0,.2,1)}
.envl.open .fl{transform:rotateX(180deg)}
.envl .wax{position:absolute;left:50%;top:60%;transform:translate(-50%,-50%);transition:opacity .4s;filter:drop-shadow(0 4px 6px rgba(0,0,0,.3))}
.envl.open .wax{opacity:0}
.envl p{position:absolute;bottom:14px;width:100%;text-align:center;font-size:14px;letter-spacing:.3em;color:#7d8a6f}
.hero{min-height:min(100vh,960px);display:grid;place-items:center;text-align:center;overflow:hidden}
.flo{position:absolute;pointer-events:none;transform:translateY(calc(var(--sy,0)*-.15px))}
.hero h1{font-size:clamp(56px,10vw,132px);line-height:.95;font-style:italic;color:#4f6249}
.hero h1 em{font-size:.45em;display:block;margin:10px 0;color:#b59a6b}
.mirror{display:flex;gap:28px;justify-content:center;align-items:center;margin-top:34px}
.mirror .num{font-size:40px;font-weight:300;color:#7d8a6f}.mirror .bar{width:60px;height:1px;background:#b59a6b}
.sh h2{font-size:clamp(36px,5vw,56px);font-style:italic}.sh .n{color:#b59a6b}
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.tl .it{background:#fffdf7;padding:24px;border-radius:6px;box-shadow:0 12px 30px rgba(60,70,50,.08);transition:transform .4s}
.tl .it:hover{transform:translateY(-6px)}
.tl .d{font-size:30px;color:#b59a6b;font-weight:300}.tl h3{font-family:'Playfair Display','Noto Serif TC';font-weight:400;margin:10px 0;font-size:20px}.tl p{font-size:16px;line-height:1.7;opacity:.8}
.cardp{background:#fffdf7;padding:44px;border:1px solid #d9cfb5;outline:1px solid #d9cfb5;outline-offset:-10px}
.cardp h3{font-family:'Playfair Display','Noto Serif TC';font-weight:400;font-size:28px;font-style:italic;margin-bottom:14px}.cardp p{line-height:1.9}
.map{background:#e6e8d8}
.sw{display:flex;gap:14px;margin-top:20px}.sw i{width:56px;height:80px;border-radius:30px 30px 4px 4px}
.gal>div{border-radius:200px 200px 10px 10px;box-shadow:0 16px 36px rgba(60,70,50,.15);border:2px solid #fffdf7}
.gal span{color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.6)}
.cd-unit{border-color:#b59a6b88;background:rgba(255,253,247,.8);color:#3d4a3a}
.cd-val{color:#4f6249}
.cal-btn{border-color:#4f6249;color:#4f6249}
.cal-btn:hover{background:#4f624915}
button.b{font:inherit;font-size:16px;padding:14px;background:#4f6249;color:#f7f2e7;border:0;border-radius:40px;letter-spacing:.2em;cursor:pointer}
button.b:hover{background:#3d4a3a}
form.rsvp input,form.rsvp select,form.rsvp textarea{border-color:#c7bd9f;background:#fffdf7}
footer{text-align:center;padding:60px 6vw 90px}
@media(max-width:760px){.tl{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.tl{grid-template-columns:1fr}.mirror{gap:12px}.mirror .bar{width:24px}.mirror .num{font-size:30px}.hero p{letter-spacing:.12em!important}}
'''

def flower(x, y, s, rot, c1='#c9a9a6', c2='#e8cfc4'):
    petals = ''.join(f'<ellipse cx="0" cy="-22" rx="14" ry="24" fill="{c1 if i%2 else c2}" opacity=".55" transform="rotate({i*60})"/>' for i in range(6))
    leaves = f'<ellipse cx="-40" cy="20" rx="30" ry="10" fill="#8fa587" opacity=".5" transform="rotate(30)"/><ellipse cx="40" cy="26" rx="34" ry="9" fill="#a9b99a" opacity=".5" transform="rotate(-25)"/>'
    return f'<svg class="flo" style="left:{x};top:{y};width:{s}px" viewBox="-80 -80 160 160"><defs><filter id="wc"><feTurbulence baseFrequency=".04" numOctaves="3" seed="{int(s)}"/><feDisplacementMap in="SourceGraphic" scale="9"/><feGaussianBlur stdDeviation=".8"/></filter></defs><g filter="url(#wc)" transform="rotate({rot})">{leaves}{petals}<circle r="8" fill="#d8b874" opacity=".7"/></g></svg>'

wax = seal('w', 'CHRISTY & TIM', 'C&amp;T', '0123 · 0321', '#8a2f2f', '#f1d9b5', 120, "'Playfair Display',serif")

# Garden 故事卡片相片
garden_story_photos = [
    "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=800&q=80"
]

story = ''.join(f'''<div class="it tilt rv">
  <div class="d num">{d}</div>
  <h3 class="zh">{t}</h3>
  <p class="zh">{p}</p>
  <div class="story-photo" data-cap="{t}"><img src="{garden_story_photos[i]}" alt="{t}" loading="lazy"></div>
</div>''' for i, (d, t, p, _) in enumerate(STORY))

# Garden 相片畫廊（6 張拱門形法式花園草地相片）
garden_photos = [
    ("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=1000&q=80", "法式花園 · 捧花誓言"),
    ("https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=1000&q=80", "微風晨光 · 純白頭紗"),
    ("https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=1000&q=80", "草坪慢步 · 隨風歡笑"),
    ("https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?auto=format&fit=crop&w=1000&q=80", "綠蔭樹影 · 甜蜜相擁"),
    ("https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=1000&q=80", "花藝誓約 · 承諾永恆"),
    ("https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=1000&q=80", "向陽盛開 · 幸福笑靨")
]

gal = ''.join(f'''<div class="rv" data-cap="{cap}">
  <img src="{url}" alt="{cap}" loading="lazy">
  <span>{cap}</span>
</div>''' for url, cap in garden_photos)

body = f'''<div id="env"><div><div class="envl tilt" id="envl"><div class="fl"></div><div class="wax">{wax}</div><p>CLICK THE SEAL · 撳火漆印開信</p></div></div></div>
<section class="hero">{flower('-40px','8%',300,10)}{flower('78%','58%',340,-30,'#b8c4a6','#dde3cf')}{flower('82%','2%',180,50)}{flower('4%','70%',200,80,'#d8b874','#efe0bd')}
<div class="rv"><p style="letter-spacing:.5em;font-size:14px" class="zh">TOGETHER WITH THEIR FAMILIES · 誠邀</p>
<h1>Christy<em>&amp;</em>Tim</h1>
<div class="mirror"><span class="num">1.23</span><span class="bar"></span><span style="font-style:italic;color:#b59a6b">mirrored</span><span class="bar"></span><span class="num">3.21</span></div>
<p style="margin-top:22px;letter-spacing:.3em"><span class="num">SAT 23 JAN 2027</span> · <span class="zh">地點待定 Venue TBC</span></p></div></section>

<!-- 花園風倒數計時 -->
<section style="padding:40px 6vw 0"><div class="wrap">{countdown_html("COUNTDOWN TO OUR CELEBRATION · 婚禮倒計時")}</div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">01</span><h2>Our Story</h2><span class="zh">我們的故事</span></div><p class="rv zh" style="font-size:24px;font-style:italic;margin-bottom:40px">From 3.21 to 1.23 — 由 <span class="num">3.21</span> 到 <span class="num">1.23</span>，一組鏡像數字。</p><div class="tl">{story}</div></div></section>

<section style="background:#eef0e4"><div class="wrap"><div class="sh rv"><span class="n num">02</span><h2>The Day</h2><span class="zh">婚禮詳情</span></div><div class="grid2">
<div class="cardp tilt rv"><h3>Ceremony · 草地證婚</h3><p class="zh"><span class="num">2027.01.23</span> · 下午 <span class="num">15:30</span><br>戶外花園草坪 Outdoor Garden Lawn<br>香港淺水灣 Repulse Bay (Venue TBC)<br><span style="opacity:.7;font-size:14px">於花草樹木與親友見證下立下誓約</span></p></div>
<div class="cardp tilt rv"><h3>Reception · 晚宴酒會</h3><p class="zh">雞尾酒會 Cocktails <span class="num">17:30</span><br>晚宴入席 Dinner <span class="num">19:00</span><br>Fine-dining &amp; Garden Toast<br>敬備美酒佳餚，共度星光之夜</p></div></div>
{calendar_html()}
</div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">03</span><h2>Venue</h2><span class="zh">場地</span></div><div class="map rv">{flower('8%','10%',160,0,'#b8c4a6','#dde3cf')}<svg style="position:absolute;inset:0" width="100%" height="100%"><path d="M0 200 C200 120 400 300 700 180 S1000 260 1200 150" stroke="#fffdf7" stroke-width="18" fill="none"/><circle cx="55%" cy="45%" r="12" fill="#8a2f2f"/></svg><p class="zh" style="display:flex;justify-content:center;align-items:center;gap:12px;width:100%"><a href="https://maps.google.com/?q=The+Repulse+Bay+Hong+Kong" target="_blank" rel="noopener" style="color:#4f6249;font-weight:600;text-decoration:underline">在 Google 地圖打開 (Open in Google Maps) →</a></p></div></div></section>

<section><div class="wrap grid2"><div class="rv"><div class="sh"><span class="n num">04</span><h2>Attire</h2></div><p class="zh">Dress Code: Garden Elegant / Pastel Tones<br>戶外草坪婚禮，建議女士穿著粗跟或平底鞋履。<br>建議色調參考：鼠尾草綠、柔粉、象牙白、香檳杏色。</p><div class="sw"><i style="background:#8fa587" title="鼠尾草綠"></i><i style="background:#e8cfc4" title="柔粉"></i><i style="background:#efe6d2" title="象牙白"></i><i style="background:#b59a6b" title="香檳杏"></i></div></div>
<div class="rv"><div class="sh"><span class="n num">05</span><h2>RSVP</h2></div>{rsvp('b')}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">06</span><h2>Gallery</h2><span class="zh">花園相片集 · 點擊放大查看</span></div><div class="gal">{gal}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">07</span><h2>FAQ</h2><span class="zh">常見問題</span></div>{faq()}</div></section>

<footer><div style="display:inline-block">{seal('f2','CHRISTY & TIM','C&amp;T','0123 · 0321','none','#b59a6b',110,"'Playfair Display',serif")}</div></footer>'''

js = '''<script>const env=document.getElementById('env'),e=document.getElementById('envl');const go=()=>{e.classList.add('open');setTimeout(()=>env.classList.add('done'),1100)};e.addEventListener('click',go);setTimeout(go,2600);if(location.hash.includes('shot'))env.remove();</script>'''

open('02-garden.html', 'w').write(page('Christy & Tim · Garden', css, body, js))
