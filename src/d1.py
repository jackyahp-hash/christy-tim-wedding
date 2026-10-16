from gen import *

css = '''
body{background:#7a0f14;color:#f6e7c8;font-family:'Noto Serif TC','Songti TC',serif}
.gold{background:linear-gradient(100deg,#b8862f,#f7e3a1 40%,#c99a3e 60%,#fff1c4 80%,#a8772a);-webkit-background-clip:text;background-clip:text;color:transparent}
.pat{position:absolute;inset:0;opacity:.08;background-image:radial-gradient(circle at 50% 50%,transparent 18px,#f7e3a1 19px,#f7e3a1 20px,transparent 21px);background-size:56px 56px;pointer-events:none}
#intro{position:fixed;inset:0;z-index:50;background:#5c0a0e;display:grid;place-items:center;transition:opacity 1s .2s,visibility 1s .2s}
#intro.done{opacity:0;visibility:hidden}
#intro .cd{font-size:120px;font-weight:300}#intro .cd span{display:inline-block;opacity:0;animation:pop 1.8s forwards}
@keyframes pop{0%{opacity:0;transform:scale(.6)}20%{opacity:1;transform:none}80%{opacity:1}100%{opacity:.25}}
.hero{min-height:min(100vh,960px);display:grid;place-items:center;text-align:center;overflow:hidden}
.card{width:min(560px,92vw);aspect-ratio:3/4.2;perspective:1600px;margin:0 auto;cursor:pointer}
.card .inner{position:absolute;inset:0;border-radius:10px;background:#9b1219;box-shadow:0 40px 80px rgba(0,0,0,.45),inset 0 0 0 10px #8a0f15,inset 0 0 0 12px #d4a849;display:grid;place-items:center;padding:40px}
.flap{position:absolute;inset:0 0 50% 0;transform-origin:top;background:linear-gradient(#a8151d,#8d1017);border-radius:10px 10px 0 0;background-image:linear-gradient(#a8151d,#8d1017),repeating-linear-gradient(45deg,transparent 0 10px,#d4a84915 10px 11px);border:1px solid #d4a849;transition:transform 1.4s cubic-bezier(.6,0,.2,1);display:grid;place-items:end center;padding-bottom:0;backface-visibility:hidden;z-index:3}
.flap2{inset:50% 0 0 0;transform-origin:bottom;border-radius:0 0 10px 10px;place-items:start center}
.card.open .flap{transform:rotateX(-178deg)}.card.open .flap2{transform:rotateX(178deg)}
.sealx{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:5;transition:opacity .5s,transform .6s;filter:drop-shadow(0 6px 10px #0006)}.card.open .sealx{opacity:0;transform:translate(-50%,-50%) scale(1.4);pointer-events:none}
.names{font-size:clamp(44px,8vw,82px);font-weight:900;letter-spacing:.08em;line-height:1.1}
.mir{display:flex;justify-content:center;gap:22px;align-items:center;font-size:28px;margin:22px 0;letter-spacing:.2em}
.mir .r{transform:scaleX(-1);display:inline-block;opacity:.55}
.hint{margin-top:28px;font-size:13px;letter-spacing:.4em;opacity:.7}
.sh h2{font-size:clamp(30px,4vw,44px);font-weight:700;letter-spacing:.15em}.sh .n{color:#d4a849}
.tl{position:relative;padding-left:40px;border-left:1px solid #d4a84966}.tl .it{margin-bottom:48px;position:relative}
.tl .it:before{content:'';position:absolute;left:-46px;top:6px;width:11px;height:11px;transform:rotate(45deg);background:#d4a849}
.tl .d{font-size:26px;color:#f7e3a1}.tl h3{font-weight:500;margin:6px 0;font-size:20px}.tl p{opacity:.75;line-height:1.9}
.panel{border:1px solid #d4a84988;padding:36px;border-radius:6px;background:linear-gradient(160deg,#8d1017,#6e0c11)}
.panel h3{font-size:22px;margin-bottom:12px;color:#f7e3a1}.panel p{line-height:2}
.map{background:repeating-linear-gradient(0deg,#6a0b10 0 38px,#7c0e14 38px 40px),repeating-linear-gradient(90deg,transparent 0 38px,#7c0e14 38px 40px);border:1px solid #d4a84966}
.map svg{position:absolute;left:50%;top:50%;transform:translate(-50%,-60%)}
.map p{position:absolute;bottom:16px;width:100%;text-align:center}
.dress{display:flex;gap:18px;margin-top:20px;flex-wrap:wrap}.dress i{width:64px;height:64px;border-radius:50%;box-shadow:0 0 0 2px #d4a849}
.gal>div{border:1px solid #d4a84988;box-shadow:0 10px 30px rgba(0,0,0,.4)}
.cd-unit{border-color:#d4a84988;background:rgba(92,10,14,.6)}
.cd-val{color:#f7e3a1}
.cal-btn{border-color:#d4a849;color:#f7e3a1}
.cal-btn:hover{background:#d4a84925;color:#fff}
button.b{font:inherit;padding:14px;background:linear-gradient(100deg,#b8862f,#f7e3a1,#b8862f);color:#5c0a0e;border:0;border-radius:4px;font-weight:700;letter-spacing:.2em;cursor:pointer}
form.rsvp input,form.rsvp select,form.rsvp textarea{border-color:#d4a84988}
footer{text-align:center;padding:60px 6vw 80px;opacity:.8}
'''

xi = seal('x', 'CHRISTY · TIM', '囍', '0123 ↔ 0321', '#c8102e', '#f7e3a1', 170)

# 東方雅緻故事時間軸（附相片）
story = ''.join(f'''<div class="it rv">
  <div class="d num">{d}</div>
  <h3 class="zh">{t}</h3>
  <p class="zh">{p}</p>
  <div class="story-photo" data-cap="{t}"><img src="{img}" alt="{t}" loading="lazy"></div>
</div>''' for d, t, p, img in STORY)

# 東方雅緻相片畫廊（6 張真實婚禮/中式浪漫高畫質相片）
oriental_photos = [
    ("https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=1000&q=80", "唯美中式婚紗 · 鳳冠霞帔"),
    ("https://images.unsplash.com/photo-1606800052052-a08af7148866?auto=format&fit=crop&w=1000&q=80", "敬茶金器 · 長輩祝福"),
    ("https://images.unsplash.com/photo-1544078751-58fee2d8a03b?auto=format&fit=crop&w=1000&q=80", "執手同心 · 嫣然一笑"),
    ("https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1000&q=80", "春風拂面 · 歲月靜好"),
    ("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1000&q=80", "紅綢相繫 · 兩姓聯姻"),
    ("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=1000&q=80", "執子之手 · 與子偕老")
]

gal = ''.join(f'''<div class="rv" data-cap="{cap}">
  <img src="{url}" alt="{cap}" loading="lazy">
  <span>{cap}</span>
</div>''' for url, cap in oriental_photos)

body = f'''<div id="intro"><div class="cd gold num"><span style="animation-delay:.1s">1</span> <span style="animation-delay:.6s">2</span> <span style="animation-delay:1.1s">3</span></div></div>
<section class="hero"><div class="pat"></div><div>
<div class="card tilt" id="card"><div class="inner"><div>
<p class="zh" style="letter-spacing:.5em;opacity:.8">謹訂於</p>
<div class="names gold zh">Christy<br><span style="font-size:.5em">&amp;</span><br>Tim</div>
<div class="mir num gold"><span>1·2·3</span><span style="font-size:16px">↔</span><span>3·2·1</span></div>
<p class="zh">舉行婚禮 · 敬備喜筵</p><p class="num" style="margin-top:10px;letter-spacing:.25em">2027.01.23</p><p class="zh" style="margin-top:6px;letter-spacing:.2em;font-size:14px">二〇二七年一月二十三日 · 星期六</p>
</div></div><div class="flap"></div><div class="flap flap2"></div><div class="sealx">{xi}</div></div>
<p class="hint zh">輕觸喜帖 · TAP TO OPEN</p></div></section>

<!-- 婚禮倒計時 -->
<section style="padding:40px 6vw 0"><div class="wrap">{countdown_html("吉日倒計 · COUNTDOWN TO WEDDING")}</div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">01</span><h2 class="gold zh">我們的故事</h2><span>Our Story</span></div><p class="rv zh" style="font-size:22px;margin-bottom:40px;color:#f7e3a1">由 <span class="num">3.21</span> 到 <span class="num">1.23</span> — 一組倒轉的數字，一段剛剛好的緣份。</p><div class="tl">{story}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">02</span><h2 class="gold zh">婚禮詳情</h2><span>Wedding Day</span></div><div class="grid2">
<div class="panel tilt rv"><h3 class="zh">證婚儀式 Ceremony</h3><p class="zh">日期：<span class="num">2027.01.23</span>（星期六）<br>時間：<span class="num">15:00</span>（下午三時正）<br>地點：香港文華東方酒店 / 中式典雅宴會廳<br><span style="opacity:.7;font-size:13px">Mandarin Oriental Hong Kong (Venue TBC)</span></p></div>
<div class="panel tilt rv"><h3 class="zh">喜筵晚宴 Banquet</h3><p class="zh">恭候：<span class="num">18:00</span> · 入席：<span class="num">19:30</span><br>敬備喜酌 · 恭候光臨<br>地址：香港中環干諾道中 5 號<br><span style="opacity:.7;font-size:13px">5 Connaught Road Central, Central, Hong Kong</span></p></div></div>
{calendar_html()}
</div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">03</span><h2 class="gold zh">場地地圖</h2><span>Venue</span></div><div class="map rv"><svg width="60" height="80" viewBox="0 0 60 80"><path d="M30 78C30 78 4 44 4 28a26 26 0 0152 0c0 16-26 50-26 50z" fill="#d4a849"/><text x="30" y="36" text-anchor="middle" font-size="22" fill="#7a0f14" font-family="Noto Serif TC">囍</text></svg><p class="zh" style="display:flex;justify-content:center;align-items:center;gap:12px;width:100%"><a href="https://maps.google.com/?q=Mandarin+Oriental+Hong+Kong" target="_blank" rel="noopener" style="color:#f7e3a1;text-decoration:underline">在 Google 地圖打開 (Open in Google Maps) →</a></p></div></div></section>

<section><div class="wrap grid2"><div class="rv"><div class="sh"><span class="n num">04</span><h2 class="gold zh">衣著建議</h2></div><p class="zh" style="line-height:2">誠邀各位親朋好友盛裝出席！建議色調參考：酒紅、香檳金、象牙白或雅緻深色正裝。<br>Dress Code: Cocktail / Black Tie Optional (Ruby Red, Gold & Ivory).</p><div class="dress"><i style="background:#7a0f14" title="酒紅"></i><i style="background:#d4a849" title="香檳金"></i><i style="background:#f6e7c8" title="象牙白"></i><i style="background:#2b2b2b" title="雅緻黑"></i></div></div>
<div class="rv"><div class="sh"><span class="n num">05</span><h2 class="gold zh">回覆出席</h2></div>{rsvp('b')}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">06</span><h2 class="gold zh">相片集</h2><span>Gallery · 點擊相片放大</span></div><div class="gal">{gal}</div></div></section>

<section><div class="wrap"><div class="sh rv"><span class="n num">07</span><h2 class="gold zh">常見問題</h2><span>FAQ</span></div>{faq()}</div></section>

<footer class="zh"><div style="display:inline-block">{seal('f','CHRISTY · TIM','囍','0123 ↔ 0321','none','#d4a849',110)}</div><p class="num" style="margin-top:12px;letter-spacing:.3em">0123 ↔ 0321</p></footer>'''

js = '''<script>const it=document.getElementById('intro');setTimeout(()=>it.classList.add('done'),2300);if(location.hash.includes('shot'))it.remove();
const c=document.getElementById('card');c.addEventListener('click',()=>c.classList.toggle('open'));if(location.hash.includes('open'))c.classList.add('open');</script>'''

open('01-oriental.html', 'w').write(page('Christy & Tim · 囍', css, body, js))
