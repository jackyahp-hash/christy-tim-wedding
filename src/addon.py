import re,sys
RM="@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}}"
MCSS='''.shot .mband,.shot .scrub{height:auto!important}.shot .mband .stk{position:relative;height:760px}.shot .scrub .stk2{position:relative;height:auto;padding:40px 0}
@media(max-width:760px){.vine{opacity:.35;left:-30px}}.mband{height:180vh;position:relative}.mband .stk{position:sticky;top:0;height:100vh;display:grid;place-items:center;perspective:1400px;overflow:hidden}
.mcoin{position:relative;transform-style:preserve-3d;font-family:'Plus Jakarta Sans';font-variant-numeric:tabular-nums;font-weight:200;font-size:clamp(90px,22vw,300px);line-height:1}
.mcoin span{display:block;backface-visibility:hidden}.mcoin .b{position:absolute;inset:0;transform:rotateY(180deg)}
.mcap{position:absolute;bottom:12vh;width:100%;text-align:center;letter-spacing:.3em;font-size:14px;word-break:keep-all}
.mrefl{transform:scaleY(-1);opacity:.12;mask-image:linear-gradient(transparent 40%,#000);-webkit-mask-image:linear-gradient(transparent 40%,#000);font-family:'Plus Jakarta Sans';font-weight:200;font-size:clamp(90px,22vw,300px);line-height:1;font-variant-numeric:tabular-nums;margin-top:-.15em}'''
def mband(cap):
    return f'''<div class="mband"><div class="stk"><div><div class="mcoin" id="mcoin"><span class="f">1.23</span><span class="b">3.21</span></div><div class="mrefl" id="mrefl">1.23</div></div><p class="mcap zh">{cap}</p></div></div>'''
MJS='''<script>if(location.hash.includes('shot'))document.documentElement.classList.add('shot');(()=>{const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;const b=document.querySelector('.mband'),c=document.getElementById('mcoin'),r=document.getElementById('mrefl');if(!b)return;
let t=0,cur=0;const tick=()=>{const rc=b.getBoundingClientRect(),p=Math.min(1,Math.max(0,-rc.top/(rc.height-innerHeight)));t=p*180;cur+=(t-cur)*(RM?1:.12);c.style.transform=`rotateY(${cur}deg)`;r.textContent=cur>90?'3.21':'1.23';if(Math.abs(t-cur)>.1)requestAnimationFrame(tick);else ticking=false};
let ticking=false;addEventListener('scroll',()=>{if(!ticking){ticking=true;requestAnimationFrame(tick)}},{passive:true});
if(location.hash.includes('shot')){c.style.transform='rotateY(20deg)'}})();</script>'''
def inject(fn,css,html_after_story,body_end,anchor):
    s=open(fn).read()
    s=s.replace('</style>',MCSS+css+RM+'</style>',1)
    i=s.index(anchor); j=s.index('</section>',i)+len('</section>')
    s=s[:j]+html_after_story+s[j:]
    s=s.replace('</body>',MJS+body_end+'</body>')
    open(fn,'w').write(s)
