# -*- coding: utf-8 -*-
"""Regenera el espejo HOY.md + TABLERO_SEMANAL.md desde APIs en vivo.

Uso: python "90 SISTEMA/sync-tablero.py" desde la raiz de la boveda.
- Lee claves de opencode.json (no hay secretos aquí).
- Solo escribe los dos tableros; preserva las secciones manuales
  (Regla X / Score X / Conexiones).
- No toca Notion ni Todoist. Reversible vía git.
"""
import datetime
import json
import pathlib
import urllib.request

V = pathlib.Path(__file__).resolve().parent.parent
HOY = V / "07_TABLERO" / "HOY.md"
SEM = V / "07_TABLERO" / "TABLERO_SEMANAL.md"
CFG = json.load(open(r"C:\Users\Admin\.config\opencode\opencode.json", encoding="utf-8-sig"))
TK = CFG["mcp"]["todoist"]["env"]["API_KEY"]
NH = {"Authorization": json.loads(CFG["mcp"]["notion"]["env"]["OPENAPI_MCP_HEADERS"])["Authorization"],
      "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
DB = {"PIPELINE": "033b38a4-c0ce-828c-88c9-01218ac45ad2",
      "INVASION": "619cd431-feac-4960-b652-b4d0cfbc3286",
      "ORDEN": "5dbcdb21-8b47-4f27-8ffd-5cb541e8a2ee"}


def get(url, headers):
    r = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(r, timeout=25) as x:
        return json.load(x)


def post(url, payload):
    r = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=NH, method="POST")
    with urllib.request.urlopen(r, timeout=25) as x:
        return json.load(x)


def notion_titles(did):
    out = []
    q = post("https://api.notion.com/v1/databases/" + did + "/query", {"page_size": 50})
    for p in q.get("results", []):
        name, date = "", ""
        for v in p.get("properties", {}).values():
            if v.get("type") == "title":
                name = "".join([s["plain_text"] for s in v.get("title", [])]) or "(sin título)"
            elif v.get("type") == "date" and v.get("date") and not date:
                date = v["date"].get("start", "")
        out.append(name + (" → " + date if date else ""))
    return out


def main():
    projs = {p["id"]: p["name"] for p in get("https://api.todoist.com/api/v1/projects?limit=50",
              {"Authorization": "Bearer " + TK}).get("results", [])}
    raw = get("https://api.todoist.com/api/v1/tasks?limit=100", {"Authorization": "Bearer " + TK})
    tl = raw.get("results", raw) if isinstance(raw, dict) else raw
    tasks = []
    for z in tl:
        if z.get("is_completed"):
            continue
        line = "- [ ] " + z.get("content", "") + " — " + projs.get(z.get("project_id"), "?")
        if z.get("due") and z["due"].get("date"):
            line += " (vence " + z["due"]["date"] + ")"
        tasks.append(line)
    pipe = notion_titles(DB["PIPELINE"])
    inv = notion_titles(DB["INVASION"])
    orb = notion_titles(DB["ORDEN"])
    hoy = datetime.date.today().isoformat()
    fin = (datetime.date.today() + datetime.timedelta(days=7)).isoformat()

    hoy_head = ("# 🎯 HOY — Tablero mínimo\n\n"
                "> Rincón espejo: ves tus tareas sin salir de Obsidian. No se gestiona aquí; se gestiona en Notion/Todoist.\n"
                "> Sincronizado: " + hoy + " (script sync-tablero.py)\n\n"
                "## Todoist (" + str(len(tasks)) + " abiertas)\n" + "\n".join(tasks) + "\n\n"
                "## Notion (fechas registradas en Notion — revisión pendiente)\n"
                "**ORDEN DE BATALLA** (" + str(len(orb)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in orb)
                + "**INVASIÓN SEMANAL** (" + str(len(inv)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in inv)
                + "**PIPELINE DE ENTREGABLES** (" + str(len(pipe)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in pipe) + "\n")
    sem_head = ("# 🗓️ TABLERO SEMANAL — Vista mínima\n\n"
                "> Espejo semanal regenerado por script desde Todoist + Notion. Solo lectura mental: aquí ves, allá gestionas.\n"
                "> Sincronizado: " + hoy + " (ventana hasta " + fin + ")\n\n"
                "## Todoist abiertas (" + str(len(tasks)) + ")\n" + "\n".join(tasks) + "\n\n"
                "## Notion por base (fechas registradas — revisión pendiente)\n"
                "**ORDEN DE BATALLA** (" + str(len(orb)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in orb)
                + "**INVASIÓN SEMANAL** (" + str(len(inv)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in inv)
                + "**PIPELINE DE ENTREGABLES** (" + str(len(pipe)) + " filas, verificado " + hoy + "):\n"
                + "".join("  - " + t + "\n" for t in pipe) + "\n")

    for path, head, marker in ((HOY, hoy_head, "## Regla X del día"), (SEM, sem_head, "## Score X")):
        old = path.read_text(encoding="utf-8")
        tail = old[old.index(marker):] if marker in old else ""
        path.write_text(head + tail, encoding="utf-8")
    print("HOY tareas=" + str(len(tasks)) + " PIPELINE=" + str(len(pipe)) + " INV=" + str(len(inv)) + " ORDEN=" + str(len(orb)))


if __name__ == "__main__":
    main()
