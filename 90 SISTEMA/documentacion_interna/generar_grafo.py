"""Genera el grafo real de la boveda E-100 en HTML autonomous.

No modifica la boveda: solo lee. Sirve para ver la topologia real y detectar
notas huerfanas, nodos puente y carpetas densas.

Uso:
    python -m documentacion_interna.generar_grafo
    python -m documentacion_interna.generar_grafo --salir ruta.html
"""
import html
import json
import os
import re
import sys
from collections import Counter, defaultdict

RAIZ = r"C:\Users\Admin\Downloads\syn\Mente Maestra E-100"
SALIDA_DEF = r"C:\Temp\STAGING_20261004\CERTIFICACION\grafo_boveda.html"
JSON_SALIDA = r"C:\Temp\STAGING_20261004\CERTIFICACION\grafo_boveda.json"

RE_ENLACE = re.compile(r"\[\[([^\]|#]+)")
RE_TAG = re.compile(r"(?:^|\s)#([\w/-]+)")
SIN_CONEXION = {".obsidian"}


def recolectar():
    notas = []
    for dp, dns, fs in os.walk(RAIZ):
        dns[:] = [d for d in dns if d not in SIN_CONEXION and d != ".trash"]
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, RAIZ).replace("\\", "/")
            try:
                txt = open(full, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            enlaces = [m.strip() for m in RE_ENLACE.findall(txt)]
            tags = sorted(set(RE_TAG.findall(txt)))
            notas.append({
                "id": rel,
                "nombre": fn[:-3],
                "carpeta": rel.split("/")[0] if "/" in rel else "(raiz)",
                "bytes": len(txt.encode("utf-8")),
                "enlaces": enlaces,
                "tags": tags,
            })
    return notas


def construir(notas):
    por_nombre = defaultdict(list)
    for n in notas:
        base = n["id"][:-3] if n["id"].lower().endswith(".md") else n["id"]
        for k in (n["nombre"], n["id"], base, base.lower(), n["nombre"].lower()):
            por_nombre[k].append(n["id"])

    aristas = set()
    rotas = Counter()
    for n in notas:
        for e in n["enlaces"]:
            cand = por_nombre.get(e) or por_nombre.get(e.lower())
            if not cand:
                rotas[e] += 1
                continue
            if len(cand) == 1:
                otro = cand[0]
            else:
                eb = e.lower().rstrip("/")
                otro = next((c for c in cand
                             if c.lower().rstrip("/").endswith(eb)), cand[0])
            if otro != n["id"]:
                aristas.add((n["id"], otro))
    return aristas, rotas


def html_grafo(notas, aristas, rotas, filas):
    grado = Counter()
    for a, b in aristas:
        grado[a] += 1
        grado[b] += 1
    PAL = {
        "01_DIARIO_DE_GUERRA": "#00FF66", "02_ALEMANIA_ZETTELKASTEN": "#FFCC00",
        "03_PROGRAMACION_Y_LOGICA": "#00F0FF", "04_LITERATURA_Y_FUENTES": "#C9D1D9",
        "05_PROTOCOLOS_Y_SISTEMAS": "#5B92E5", "06_FE_Y_FILOSOFIA": "#B392F0",
        "07_TABLERO": "#FF0055", "10 PROYECTOS": "#FF8C42", "20 AREAS": "#8B949E",
        "30 RECURSOS": "#8B949E", "40 ARCHIVOS X": "#6E7681",
        "90 SISTEMA": "#7EE787", "00_INBOX_TEMPORAL": "#F0883E",
        "10.02 MONOGRAFIA": "#F778BA", "00 ENTRADA (Inbox)": "#F0883E",
    }
    nodos, aristas_js = [], []
    # inicializacion en espiral (phyllotaxis): evita el arranque degenerado en (0,0)
    N = len(notas)
    import math as _m
    for i, n in enumerate(notas):
        g = grado.get(n["id"], 0)
        r = 4 + min(20, g * 1.5)
        ang = i * 2.39996323  # golden angle
        rad = 26 * _m.sqrt(i + 1)
        nodos.append({
            "x": round(_m.cos(ang) * rad, 1), "y": round(_m.sin(ang) * rad, 1),
            "id": n["id"], "label": n["nombre"],
            "r": round(r, 1), "g": g, "carpeta": n["carpeta"],
            "color": PAL.get(n["carpeta"], "#8B949E"),
        })
    for a, b in aristas:
        aristas_js.append([a, b])

    filas = "".join(
        f"<tr><td>{html.escape(n['carpeta'])}</td><td>{n['total']}</td>"
        f"<td>{n['con']}</td><td>{n['pct']:.0f}%</td>"
        f"<td><div class='bar'><i style='width:{n['pct']:.0f}%'></i></div></td></tr>"
        for n in sorted(filas, key=lambda x: x["pct"]))
    huerf = "".join(f"<li>{html.escape(o)}</li>" for o in _huerfanas(grado)) or "<li>ninguna</li>"
    rotas_html = "".join(
        f"<li><code>{html.escape(t)}</code> &times;{c}</li>"
        for t, c in rotas.most_common(40)) or "<li>ninguno</li>"

    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<title>Grafo real - Boveda E-100</title>
<style>
 body{{background:#0b0e14;color:#c9d1d9;font:14px/1.5 'Segoe UI',sans-serif;margin:0;padding:24px}}
 h1{{color:#00f0ff;font-size:20px;margin:0 0 4px}}
 .sub{{color:#8b949e;margin-bottom:18px}}
 .wrap{{display:grid;grid-template-columns:1fr 380px;gap:20px}}
 .card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:14px}}
 h2{{color:#00f0ff;font-size:13px;margin:0 0 10px;text-transform:uppercase;letter-spacing:.8px}}
 .kpi{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}}
 .kpi div{{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:10px 14px;min-width:104px}}
 .kpi b{{display:block;font-size:21px;color:#00f0ff}}
 .kpi span{{color:#8b949e;font-size:11px}}
 table{{width:100%;border-collapse:collapse;font-size:12px}}
 th,td{{text-align:left;padding:5px 6px;border-bottom:1px solid #21262d}}
 th{{color:#8b949e;font-weight:600}}
 .bar{{background:#21262d;height:5px;border-radius:3px;overflow:hidden}}
 .bar i{{display:block;height:100%;background:#00ff66}}
 ul{{margin:0;padding-left:18px;font-size:12px;max-height:290px;overflow:auto}}
 li{{margin-bottom:3px}}
 code{{color:#ff7b72;font-size:11px}}
 svg{{width:100%;height:520px;background:#0d1117;border-radius:6px}}
 .lg{{display:flex;gap:9px;flex-wrap:wrap;font-size:10.5px;color:#8b949e;margin-top:9px}}
 .lg i{{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:3px}}
</style></head><body>
<h1>Grafo real de la boveda E-100</h1>
<div class="sub">Generado el {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')} &middot; solo lectura &middot; la boveda NO se modifica</div>
<div class="kpi" id="kpi"></div>
<div class="wrap">
 <div class="card"><h2>Topologia</h2><svg id="g"></svg><div class="lg" id="lg"></div></div>
 <div>
  <div class="card" style="margin-bottom:14px"><h2>Densidad por carpeta</h2>
   <table><thead><tr><th>Carpeta</th><th>Notas</th><th>Con enlaces</th><th>%</th><th></th></tr></thead>
   <tbody>{filas}</tbody></table></div>
  <div class="card" style="margin-bottom:14px"><h2>Notas huerfanas (0 enlaces)</h2><ul>{huerf}</ul></div>
  <div class="card"><h2>Enlaces rotos (destino inexistente)</h2><ul>{rotas_html}</ul></div>
 </div>
</div>
<script>
const nodos={json.dumps(nodos, ensure_ascii=False)};
const aristas={json.dumps(aristas_js, ensure_ascii=False)};
const grado=Object.fromEntries(nodos.map(n=>[n.id,n.g]));
const con=nodos.filter(n=>n.g>0).length, tot=nodos.length;
const n_rotos={len(rotas)};
document.getElementById('kpi').innerHTML=[
 ['Notas',{len(nodos)}],['Con enlaces',con],['Densidad',(100*con/{len(nodos)}).toFixed(1)+'%'],
 ['Aristas',{len(aristas_js)}],['Nodos puente',nodos.filter(function(n){{return n.g>=4;}}).length],
 ['Tipos rotos',n_rotos],['Huerfanas',nodos.filter(function(n){{return n.g===0;}}).length]
].map(function(kv){{return '<div><b>'+kv[1]+'</b><span>'+kv[0]+'</span></div>';}}).join('');
document.getElementById('lg').innerHTML=[...new Set(nodos.map(n=>n.carpeta))]
 .map(c=>`<span><i style="background:${{(nodos.find(n=>n.carpeta===c)||{{}}).color}}"></i>${{c}}</span>`).join('');
const svg=document.getElementById('g'), NS='http://www.w3.org/2000/svg';
const W=svg.clientWidth||900,H=520;
svg.setAttribute('viewBox',`0 0 ${{W}} ${{H}}`);
const mk=(t,a)=>{{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;}};
for(const [a,b] of aristas){{
 const A=nodos.find(n=>n.id===a),B=nodos.find(n=>n.id===b);
 svg.appendChild(mk('line',{{x1:A.x,y1:A.y,x2:B.x,y2:B.y,
  stroke:Math.min(A.g,B.g)>2?'#00f0ff':'#30363d','stroke-width':Math.min(A.g,B.g)>2?1.1:.6,
  opacity:Math.min(A.g,B.g)>2?.55:.32}}));
}}
for(const n of nodos){{
 const c=mk('circle',{{cx:n.x,cy:n.y,r:n.r,fill:n.color,
  opacity:n.g>0?.92:.34,stroke:n.g>=4?'#fff':'none','stroke-width':n.g>=4?1.1:0}});
 c.appendChild(mk('title',{{}})).textContent=`${{n.label}}\\n${{n.carpeta}} · ${{n.g}} enlace(s)`;
 svg.appendChild(c);
 if(n.g>=3){{const t=mk('text',{{x:n.x,y:n.y-n.r-4,'text-anchor':'middle',
  fill:'#c9d1d9','font-size':8.5}});t.textContent=n.label.slice(0,26);svg.appendChild(t);}}
}}
// fuerza dirigida: repulsion global + springs por arista + gravedad suave
const idx=new Map(nodos.map((n,i)=>[n.id,i]));
const ED=aristas.map(([u,v])=>[idx.get(u),idx.get(v)]).filter(p=>p[0]!==undefined&&p[1]!==undefined);
for(const n of nodos){{n.vx=0;n.vy=0;}}
let temp=1;
for(let it=0;it<600;it++){{
  // repulsion (N^2 pero N~355 => 126k pares, 600 iter = 75M, aceptable en JS)
  for(let i=0;i<nodos.length;i++){{
    const a=nodos[i];
    for(let j=i+1;j<nodos.length;j++){{
      const b=nodos[j];
      let dx=a.x-b.x, dy=a.y-b.y;
      let d2=dx*dx+dy*dy;
      if(d2<0.01){{dx=(Math.random()-0.5)*0.6;dy=(Math.random()-0.5)*0.6;d2=dx*dx+dy*dy;}}
      const d=Math.sqrt(d2);
      const f=Math.min(9,2600/d2)*temp;
      const ux=dx/d, uy=dy/d;
      a.vx+=ux*f;a.vy+=uy*f;b.vx-=ux*f;b.vy-=uy*f;
    }}
  }}
  // springs
  for(const [i,j] of ED){{
    const a=nodos[i],b=nodos[j];
    const dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||0.01;
    const f=(d-165)*0.016*temp;
    const ux=dx/d,uy=dy/d;
    a.vx+=ux*f;a.vy+=uy*f;b.vx-=ux*f;b.vy-=uy*f;
  }}
  // gravedad suave al centro + borde
  for(const n of nodos){{
    n.vx+=(W/2-n.x)*0.0022*temp;
    n.vy+=(H/2-n.y)*0.0022*temp;
    n.vx*=0.82; n.vy*=0.82;               // damping
    n.x+=n.vx; n.y+=n.vy;
    n.x=Math.max(30,Math.min(W-30,n.x));
    n.y=Math.max(22,Math.min(H-22,n.y));
  }}
  temp=Math.max(0.02,1-it/600);            // enfriamiento
}}
function pintar(){{
 const N=nodos;
 svg.querySelectorAll('line').forEach(function(l,i){{
  const e=aristas[i];const A=N[idx.get(e[0])],B=N[idx.get(e[1])];
  l.setAttribute('x1',A.x);l.setAttribute('y1',A.y);
  l.setAttribute('x2',B.x);l.setAttribute('y2',B.y);}});
 svg.querySelectorAll('circle').forEach(function(c,i){{
  c.setAttribute('cx',N[i].x);c.setAttribute('cy',N[i].y);}});
 const etiq=N.filter(function(x){{return x.g>=3;}});
 svg.querySelectorAll('text').forEach(function(t,i){{
  const n=etiq[i]; if(!n)return;
  t.setAttribute('x',n.x);t.setAttribute('y',n.y-n.r-4);}});
}}
pintar();
</script></body></html>"""


def _huerfanas(grado):
    return {n for n in grado if False}  # se completa abajo


def main():
    salir = SALIDA_DEF
    if "--salir" in sys.argv:
        salir = sys.argv[sys.argv.index("--salir") + 1]
    notas = recolectar()
    aristas, rotas = construir(notas)

    grado = Counter()
    for a, b in aristas:
        grado[a] += 1
        grado[b] += 1
    from collections import defaultdict as dd
    por_carpeta = dd(lambda: {"total": 0, "con": 0})
    huerfanas = []
    for n in notas:
        c = por_carpeta[n["carpeta"]]
        c["total"] += 1
        if grado.get(n["id"], 0) > 0:
            c["con"] += 1
        else:
            huerfanas.append(n["id"])
    filas = []
    for k, v in por_carpeta.items():
        filas.append({"carpeta": k, "total": v["total"], "con": v["con"],
                      "pct": 100 * v["con"] / v["total"]})

    doc = html_grafo(notas, aristas, rotas, filas)
    doc = doc.replace("<li>ninguna</li>",
                      "".join(f"<li>{html.escape(h)}</li>" for h in huerfanas[:60])
                      or "<li>ninguna</li>")
    open(salir, "w", encoding="utf-8").write(doc)

    json.dump({"notas": len(notas), "aristas": len(aristas),
               "con_enlaces": sum(1 for n in notas if grado.get(n["id"], 0)),
               "huerfanas": huerfanas,
               "por_carpeta": {k: dict(v) for k, v in por_carpeta.items()},
               "enlaces_rotos": dict(rotas)},
              open(JSON_SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    con = sum(1 for n in notas if grado.get(n["id"], 0))
    print(f"notas          : {len(notas)}")
    print(f"con enlaces    : {con} ({100*con/len(notas):.1f}%)")
    print(f"aristas        : {len(aristas)}")
    print(f"huerfanas      : {len(huerfanas)}")
    print(f"enlaces rotos  : {len(rotas)} tipos distintos")
    print(f"escrito        : {salir}")


if __name__ == "__main__":
    main()




