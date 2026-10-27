"""Builds index-type-lov.html: the prototype with Collateral type picked from a LOV instead of tiles.

It is a comparison copy only; index.html (tiles) is the agreed design. Re-run after changing index.html:
    python3 design/prototype/build-type-lov.py
"""
from pathlib import Path

here = Path(__file__).parent
s = (here / "index.html").read_text()


def swap(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)


swap("<title>Collateral Management Prototype</title>",
     "<title>Collateral Management Prototype (type LOV)</title>")
swap('<span class="sample-pill">Prototype · sample data</span>',
     '<span class="sample-pill">Prototype · type LOV variant</span>')

# Step 2: one library LOV on the form grid, with the type's description under it
swap('<div class="card-body"><div class="types" role="radiogroup" aria-labelledby="s2" id="types"></div></div>',
     '<div class="card-body"><div class="ugrid"><div class="field full" style="--cw:280px"><label for="typeBtn">Collateral type<span class="req">*</span></label>'
     '<div id="types"></div><div class="hint" id="typeHint"></div></div></div></div>')

i = s.index("function renderTypes(){")
j = s.index("/* scroll so the whole card", i)
s = s[:i] + '''function renderTypes(){
  const t=typeBy(S.type);
  $("#types").innerHTML=`<button type="button" class="lookup-btn" id="typeBtn" data-typelov ${S.customer?"":"disabled"}>${t?`<span class="lov-v"><b>${t.code}</b> - ${esc(t.lovDesc)}</span>`:`<span class="ph">${S.customer?"Search and select":"Find the customer first"}</span>`}<span class="lov-ic">${icon("search")}</span></button>`;
  $("#typeHint").textContent=t?t.d:"Each type opens its own form.";
}
''' + s[j:]

i = s.index('$("#types").addEventListener("click",e=>{const b=e.target.closest(".tile")')
j = s.index("\n", s.index('$("#types").addEventListener("keydown"', i))
s = s[:i] + '''$("#types").addEventListener("click",e=>{const b=e.target.closest("[data-typelov]");if(!b||b.disabled)return;
  openLov("Collateral types",TYPES.map(t=>({code:t.code,desc:t.lovDesc})),r=>{
    if(S.type!==r.code){S.type=r.code;S.values={};S.lookups={};S.errors={};S.showErrors=false}
    renderAll();scrollToCard($("#formCard"));
  },undefined,b);});''' + s[j:]

(here / "index-type-lov.html").write_text(s)
print("wrote", here / "index-type-lov.html")
