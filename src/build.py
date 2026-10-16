import subprocess,sys,os
from addon import *
for d in ['d1','d2','d3']: subprocess.run([sys.executable,os.path.join(os.path.dirname(__file__),d+'.py')],check=True)
s=open('03-film.html').read();import re;open('03-film.html','w').write(re.sub(r'\.strip\{[^}]*\}','',s))
# ---------- 東方 ----------
cloud=lambda x,y,w,o,sp:f'<svg class="px" data-sp="{sp}" style="left:{x};top:{y};width:{w}px;opacity:{o}" viewBox="0 0 200 80"><path d="M20 60c-14 0-14-20 0-20 0-16 22-22 30-8 6-18 36-18 40 2 10-10 30-4 28 10 16-2 22 16 6 16z" fill="none" stroke="#d4a849" stroke-width="2"/><path d="M60 52c0-8 12-8 12 0" fill="none" stroke="#d4a849" stroke-width="1.5"/></svg>'
lant=lambda x,y,w,sp:f'<svg class="px lant" data-sp="{sp}" style="left:{x};top:{y};width:{w}px" viewBox="0 0 60 120"><line x1="30" y1="0" x2="30" y2="18" stroke="#d4a849"/><rect x="18" y="16" width="24" height="6" rx="2" fill="#d4a849"/><ellipse cx="30" cy="52" rx="26" ry="32" fill="#c8102e"/><ellipse cx="30" cy="52" rx="26" ry="32" fill="url(#lg)"/><path d="M30 20v64M16 26q-8 26 0 52M44 26q8 26 0 52" stroke="#d4a84988" fill="none"/><rect x="18" y="82" width="24" height="6" rx="2" fill="#d4a849"/><path d="M24 88v24M30 88v28M36 88v24" stroke="#d4a849"/><text x="30" y="60" text-anchor="middle" font-size="18" fill="#f7e3a1" font-family="Noto Serif TC">囍</text></svg>'
css1='''
.gold{background-size:250% 100%!important;animation:foil 5s ease-in-out infinite}
@keyframes foil{0%,100%{background-position:0% 0}50%{background-position:100% 0}}
.hero .px{position:absolute;pointer-events:none;will-change:transform}
.lant{animation:sway 4s ease-in-out infinite alternate;transform-origin:top center}@keyframes sway{from{rotate:-4deg}to{rotate:4deg}}
.lant ellipse:nth-of-type(1){filter:drop-shadow(0 0 18px #ff5a3c88)}
.card .inner:after{content:'';position:absolute;inset:0;border-radius:10px;background:linear-gradient(110deg,transparent 35%,#fff6 50%,transparent 65%);background-size:300% 100%;animation:sweep 4.5s ease-in-out infinite;pointer-events:none;mix-blend-mode:overlay}
@keyframes sweep{0%{background-position:120% 0}60%,100%{background-position:-60% 0}}
.stamp{display:block;margin:0 auto 10px;opacity:0;transform:scale(2.4) rotate(-14deg)}
.in .stamp,.stamp.in{animation:press .9s cubic-bezier(.3,1.6,.5,1) .2s forwards}
@keyframes press{0%{opacity:0;transform:scale(2.4) rotate(-14deg)}55%{opacity:1;transform:scale(.92) rotate(-8deg)}100%{opacity:.95;transform:scale(1) rotate(-8deg)}}
.stampwrap{text-align:center;padding:30px 0 0}
form.rsvp{background:linear-gradient(170deg,#c8102e,#8d1017);padding:90px 30px 30px;border-radius:14px;position:relative;box-shadow:0 30px 60px #0007;overflow:hidden}
form.rsvp:before{content:'';position:absolute;left:-10%;right:-10%;top:-150px;height:220px;border-radius:0 0 50% 50%;background:linear-gradient(#a8151d,#7a0f14);box-shadow:0 4px 0 #d4a849}
form.rsvp:after{content:'囍';position:absolute;left:50%;top:42px;transform:translateX(-50%);width:56px;height:56px;border-radius:50%;background:radial-gradient(#f7e3a1,#c99a3e);color:#8d1017;display:grid;place-items:center;font-size:26px;font-weight:900;box-shadow:0 4px 10px #0006}
form.rsvp label{position:relative}
.panel{background-image:linear-gradient(160deg,#8d1017,#6e0c11),repeating-linear-gradient(45deg,transparent 0 12px,#d4a84910 12px 13px)!important}
@media(max-width:760px){.hero .px.hidem{display:none}}
'''
hero_deco='<svg width="0" height="0" style="position:absolute"><defs><radialGradient id="lg" cx=".35" cy=".35"><stop offset="0" stop-color="#ffb08a" stop-opacity=".7"/><stop offset="1" stop-color="#7a0f14" stop-opacity=".2"/></radialGradient></defs></svg>'+cloud('4%','14%',240,.5,.25)+cloud('70%','70%',300,.4,.4)+cloud('62%','10%',160,.35,.15)+cloud('10%','76%',180,.3,.5)+lant('10%','4%',70,.6)+lant('84%','0%',90,.35)+lant('80%','40%',50,.8).replace('class="px lant"','class="px lant hidem"')
js1='''<script>(()=>{const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;if(RM)return;const els=[...document.querySelectorAll('.hero .px')];let tk=false;
addEventListener('scroll',()=>{if(tk)return;tk=true;requestAnimationFrame(()=>{const y=scrollY;if(y<innerHeight*1.2)els.forEach(e=>e.style.transform=`translateY(${-y*e.dataset.sp}px)`);tk=false})},{passive:true})})();</script>'''
from gen import seal
s=open('01-oriental.html').read()
s=s.replace('<section class="hero"><div class="pat"></div>','<section class="hero"><div class="pat"></div>'+hero_deco)
stamp='<div class="stampwrap rv"><svg class="stamp" width="130" height="130" viewBox="0 0 200 200"><rect x="10" y="10" width="180" height="180" rx="14" fill="none" stroke="#e0313f" stroke-width="8"/><rect x="24" y="24" width="152" height="152" rx="6" fill="#c8102e" opacity=".85"/><text x="100" y="128" text-anchor="middle" font-size="96" font-weight="900" fill="#f6e7c8" font-family="Noto Serif TC">囍</text><text x="100" y="168" text-anchor="middle" font-size="16" letter-spacing="4" fill="#f6e7c8" font-family="Plus Jakarta Sans">0123 · 0321</text></svg><p class="zh" style="letter-spacing:.4em;font-size:13px;opacity:.8">百年好合 · 2027.01.23</p></div>'
s=s.replace('<span>Wedding Day</span></div><div class="grid2">','<span>Wedding Day</span></div>'+stamp+'<div class="grid2" style="margin-top:30px">')
open('01-oriental.html','w').write(s)
inject('01-oriental.html',css1,mband('由 3.21 到 1.23 · 倒轉都係我哋'),js1,'Our Story')
# ---------- Garden ----------
petals=''.join(f'<i class="pt" style="left:{(i*37)%100}%;animation-delay:{-(i*1.7)%12:.1f}s;animation-duration:{10+(i*3)%7}s;--dx:{(i%5-2)*40}px;background:{["#e8cfc4","#c9a9a6","#f3e2d7","#dde3cf"][i%4]}"></i>' for i in range(14))
css2='''
.pt{position:absolute;top:-30px;width:14px;height:18px;border-radius:14px 0 14px 0;opacity:.7;pointer-events:none;animation:fall linear infinite;will-change:transform}
@keyframes fall{0%{transform:translate(0,-5vh) rotate(0)}100%{transform:translate(var(--dx),105vh) rotate(540deg)}}
@media(max-width:760px){.pt:nth-child(n+8){display:none}}
.vine{position:absolute;left:2vw;top:0;height:100%;width:120px;pointer-events:none;overflow:visible}
.vine path{fill:none;stroke:#8fa587;stroke-width:2}.vine .lf{fill:#a9b99a;opacity:0;transition:opacity .6s}
.tl .it{background-image:radial-gradient(#0000 60%,#b59a6b10),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='p'%3E%3CfeTurbulence baseFrequency='.8' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .6 0 0 0 0 .55 0 0 0 0 .4 0 0 0 .06 0'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23p)'/%3E%3C/svg%3E")!important;position:relative;padding-top:86px!important}
.tl .it:after{content:'';position:absolute;top:-10px;left:50%;width:70px;height:22px;transform:translateX(-50%) rotate(-3deg);background:#e8dcc0cc;box-shadow:0 1px 2px #0002}
.pf{position:absolute;top:14px;right:16px;width:64px;height:64px;opacity:.85;filter:saturate(.7) sepia(.15)}
.envl .wax{transition:none}.halfL,.halfR{position:absolute;left:0;top:0;transition:transform 1s cubic-bezier(.5,0,.3,1),opacity 1s}
.halfL{clip-path:polygon(0 0,52% 0,46% 30%,55% 55%,45% 75%,50% 100%,0 100%)}.halfR{clip-path:polygon(52% 0,100% 0,100% 100%,50% 100%,45% 75%,55% 55%,46% 30%)}
.envl .wax{width:120px;height:120px}.envl.crack .halfL{transform:translate(-30px,40px) rotate(-25deg);opacity:0}.envl.crack .halfR{transform:translate(30px,50px) rotate(20deg);opacity:0}
.envl.open .wax{opacity:1!important}
'''
from gen import seal as S
wax=S('w','CHRISTY & TIM','C&amp;T','0123 · 0321','#8a2f2f','#f1d9b5',120,"'Playfair Display',serif")
def pf(c1,c2,seed):
    p=''.join(f'<ellipse cx="0" cy="-16" rx="9" ry="16" fill="{c1 if k%2 else c2}" transform="rotate({k*72})"/>' for k in range(5))
    return f'<svg class="pf" viewBox="-40 -40 80 80"><path d="M0 0 Q{8+seed} 20 {seed} 38" stroke="#7d8a6f" fill="none"/><ellipse cx="{seed+6}" cy="24" rx="8" ry="3" fill="#8fa587" transform="rotate(30 {seed+6} 24)"/>{p}<circle r="4" fill="#d8b874"/></svg>'
s=open('02-garden.html').read()
s=s.replace('<section class="hero">','<section class="hero">'+petals,1)
oldw=s[s.index('<div class="wax">'):s.index('</div>',s.index('<div class="wax">'))+6]
s=s.replace(oldw,f'<div class="wax"><div class="halfL">{wax}</div><div class="halfR">{wax.replace("cw","cw2").replace("bw","bw2")}</div></div>')
cols=[('#e8cfc4','#c9a9a6'),('#dde3cf','#a9b99a'),('#efe0bd','#d8b874'),('#f3e2d7','#c9a9a6')]
parts=s.split('<div class="it tilt rv">')
s=parts[0]+''.join('<div class="it tilt rv">'+pf(*cols[k%4],k*3-4)+p for k,p in enumerate(parts[1:]))
vine='<svg class="vine" viewBox="0 0 120 1000" preserveAspectRatio="none"><path id="vp" d="M60 0 C10 120 110 220 60 340 S10 560 60 680 S110 880 60 1000"/>'+''.join(f'<ellipse class="lf" data-at="{a}" cx="{x}" cy="{y}" rx="14" ry="6" transform="rotate({r} {x} {y})"/>' for a,x,y,r in [(.15,40,140,-30),(.3,80,300,25),(.45,36,480,-20),(.6,84,640,30),(.75,38,800,-25),(.9,80,940,20)])+'</svg>'
i=s.index('<span class="zh">我們的故事</span>');k=s.rfind('<section>',0,i)
s=s[:k]+'<section style="overflow:hidden">'+vine+s[k+9:]
s=s.replace("const go=()=>{e.classList.add('open')","const go=()=>{e.classList.add('crack');setTimeout(()=>e.classList.add('open'),500)")
s=s.replace("setTimeout(()=>env.classList.add('done'),1100)","setTimeout(()=>env.classList.add('done'),1700)")
open('02-garden.html','w').write(s)
js2='''<script>(()=>{const v=document.querySelector('.vine'),p=document.getElementById('vp'),L=p.getTotalLength(),lf=[...v.querySelectorAll('.lf')];p.style.strokeDasharray=L;
const up=()=>{const r=v.getBoundingClientRect();let k=Math.min(1,Math.max(0,(innerHeight*.8-r.top)/r.height));if(location.hash.includes('shot')||matchMedia('(prefers-reduced-motion: reduce)').matches)k=1;p.style.strokeDashoffset=L*(1-k);lf.forEach(e=>e.style.opacity=k>e.dataset.at?1:0)};
let tk=false;addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(()=>{up();tk=false})}},{passive:true});up()})();</script>'''
inject('02-garden.html',css2,mband('From 3.21 to 1.23 · mirrored, like pressed petals'),js2,'Our Story')
# ---------- Film ----------
css3='''
.hero:before{content:'';position:absolute;left:50%;top:-10%;width:140%;height:120%;transform:translateX(-50%);background:conic-gradient(from 168deg at 50% 0%,transparent 0deg,#fff3d61a 8deg,#fff3d633 12deg,#fff3d61a 16deg,transparent 24deg);animation:flick 3.2s steps(1) infinite;pointer-events:none}
.hero:after{content:'';position:absolute;inset:0;background:#fff3d6;opacity:0;animation:flick2 5s steps(1) infinite;pointer-events:none;mix-blend-mode:overlay}
@keyframes flick{0%,100%{opacity:1}7%{opacity:.6}9%{opacity:1}43%{opacity:.85}45%{opacity:1}71%{opacity:.5}72%{opacity:1}}
@keyframes flick2{0%,100%{opacity:0}31%{opacity:.05}32%{opacity:0}77%{opacity:.08}78%{opacity:0}}
.scrub{height:260vh;position:relative}.scrub .stk2{position:sticky;top:0;height:100vh;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.scrub .frames{overflow:visible;will-change:transform;padding-left:8vw}.fr{flex-basis:360px}
.ctr{font-size:12px;letter-spacing:.3em;color:#d9bf8c;text-align:center;margin-top:16px}
.tk{display:grid;grid-template-columns:1fr 70px;border-radius:14px;overflow:visible;position:relative}
.tk form.rsvp{background:#161412;padding:28px;border-radius:14px 0 0 14px;border:1px solid #d9bf8c44;border-right:2px dashed #d9bf8c66}
.tk .stb{background:#d9bf8c;color:#0e0d0c;border-radius:0 14px 14px 0;display:grid;place-items:center;writing-mode:vertical-rl;letter-spacing:.3em;font-weight:600;font-size:13px;transform-origin:0% 100%;transition:transform 1.1s cubic-bezier(.5,-.3,.4,1),opacity 1.1s}
.tk.torn .stb{transform:translate(30px,40px) rotate(24deg);opacity:.0}
.tk.torn form.rsvp{animation:jolt .3s}@keyframes jolt{30%{transform:translateX(-4px) rotate(-.4deg)}}
.gal>div{background-clip:content-box!important;padding:12px 12px 46px;background-color:#f3ead7;border-radius:3px;box-shadow:0 20px 40px #0008;rotate:var(--r,0deg)}
.gal>div:before{content:'';position:absolute;inset:12px 12px 46px;background:#2a241b;transition:opacity 3.5s ease-in 0.3s}
.gal>div.in:before{opacity:0}
.gal>div:after{content:'';position:absolute;inset:12px 12px 46px;backdrop-filter:sepia(1) blur(6px) brightness(1.6);-webkit-backdrop-filter:sepia(1) blur(6px) brightness(1.6);transition:backdrop-filter 4s,-webkit-backdrop-filter 4s;pointer-events:none}
.gal>div.in:after{backdrop-filter:none;-webkit-backdrop-filter:none}
.gal span{color:#5a4630!important;bottom:14px!important;font-family:'Playfair Display';font-style:italic;letter-spacing:.05em!important;font-size:14px!important}
@media(max-width:760px){.scrub{height:auto}.scrub .stk2{position:static;height:auto}.scrub .frames{overflow-x:auto;transform:none!important;padding-left:6vw}.fr{flex-basis:78vw}.tk{grid-template-columns:1fr 46px}.tk form.rsvp{padding:20px}}
'''
s=open('03-film.html').read()
a=s.index('<div class="film">');b=s.index('</section>',a)
film=s[a:b]
if '<p class="zh" style="text-align:center;margin-top:14px;font-size:12px;opacity:.5;letter-spacing:.2em">← 左右拖動 SWIPE' in film:
    film=re.sub(r'<p class="zh"[^>]*>← 左右拖動 SWIPE[^<]*</p>','<p class="ctr num" id="fc">FRAME 01 / 04 · 0123 ↔ 0321</p></div></div>',film)
    film=film.replace('<div class="film">','<div class="scrub"><div class="stk2"><div class="film">')
s=s[:a]+film+s[b:]
fs=s.index('<form class="rsvp rv">');fe=s.index('</form>',fs)+7
s=s[:fs]+'<div class="tk rv">'+s[fs:fe].replace('class="rsvp rv"','class="rsvp"')+'<div class="stb num">ADMIT ONE · CT0123</div></div>'+s[fe:]
rots=['-2deg','1.5deg','-1deg','2deg','-1.5deg','1deg']
if '<div class="rv" data-cap="' in s:
    parts=s.split('<div class="rv" data-cap="')
    s=parts[0]+''.join(f'<div class="rv" style="--r:{rots[k%6]}" data-cap="'+p for k,p in enumerate(parts[1:]))
elif '<div class="rv" style="background:' in s:
    parts=s.split('<div class="rv" style="background:')
    s=parts[0]+''.join(f'<div class="rv" style="--r:{rots[k%6]};background:'+p for k,p in enumerate(parts[1:]))
open('03-film.html','w').write(s)
js3='''<script>(()=>{const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;const sc=document.querySelector('.scrub'),fr=sc.querySelector('.frames'),fc=document.getElementById('fc');
const up=()=>{if(innerWidth<=760)return;const r=sc.getBoundingClientRect(),p=Math.min(1,Math.max(0,-r.top/(r.height-innerHeight)));const max=fr.scrollWidth-innerWidth*.84;fr.style.transform=`translateX(${-p*Math.max(0,max)}px)`;const n=Math.min(4,1+Math.floor(p*4));fc.textContent=`FRAME 0${n} / 04 · `+(p>.5?'0321 ↔ 0123':'0123 ↔ 0321')};
let tk=false;addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(()=>{up();tk=false})}},{passive:true});up();
const f=document.querySelector('.tk form');f.addEventListener('submit',()=>f.parentNode.classList.add('torn'));})();</script>'''
inject('03-film.html',css3,mband('REWIND · 3.21 → 1.23 · 倒帶都係你'),js3,'Our Story')
