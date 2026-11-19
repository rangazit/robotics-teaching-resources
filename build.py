#!/usr/bin/env python3
"""Build README.md and docs/index.html from resources.yaml.

Usage:  python build.py           # write README.md and docs/index.html
        python build.py --check   # fail if the generated files are not up to date (used by CI)
"""
import json, sys, pathlib, html
import yaml

ROOT = pathlib.Path(__file__).resolve().parent
MATS = [("book", "Book"), ("slides", "Slides"), ("notes", "Notes"), ("video", "Video"),
        ("exercises", "Exercises"), ("solutions", "Solutions"), ("code", "Code")]
ICON = {"free": "✅", "partial": "◐", "paid": "💲", "none": "—", "unknown": "?"}
WORD = {"free": "free", "partial": "partial", "paid": "paid", "none": "not available", "unknown": "unknown"}


def load():
    d = yaml.safe_load((ROOT / "resources.yaml").read_text(encoding="utf-8"))
    res = d["resources"]
    by = {r["id"]: r for r in res}
    errors = []
    for r in res:
        for k in ("uses_books", "uses_software", "derived_from", "related"):
            for x in r.get(k, []):
                if x not in by: errors.append("%s: %s -> unknown id %s" % (r["id"], k, x))
        for t in r.get("topics", []):
            if t not in d["topics"]: errors.append("%s: unknown topic %s" % (r["id"], t))
        for m, v in r.get("materials", {}).items():
            if m not in dict(MATS): errors.append("%s: unknown material %s" % (r["id"], m))
            if v.get("status") not in ICON: errors.append("%s: bad status for %s" % (r["id"], m))
    if errors:
        sys.exit("resources.yaml has errors:\n  " + "\n  ".join(errors))
    # reverse links
    for r in res:
        r["used_by"] = []; r["derivatives"] = []
    for r in res:
        for k in ("uses_books", "uses_software"):
            for x in r.get(k, []): by[x]["used_by"].append(r["id"])
        for x in r.get("derived_from", []): by[x]["derivatives"].append(r["id"])
    return d, res, by


def url_of(r):
    if r.get("url"): return r["url"]
    offs = r.get("offerings") or []
    return offs[0]["url"] if offs else ""


# ------------------------------------------------------------------ README
def md_link(r):
    return "[%s](%s)" % (r["name"].replace("|", "/"), url_of(r))


def readme(d, res, by):
    L = ["# Online resources for teaching robotics and autonomous systems", "",
         "A curated, checked list of courses, textbooks, videos, exercises and software for teaching an "
         "introductory university course on robotics and autonomous systems.",
         "",
         "**Interactive version** (filters, search, connections between resources): "
         "https://rangazit.github.io/robotics-teaching-resources/", "",
         "Availability: ✅ free and complete · ◐ partial · 💲 paid · — not available · ? unknown. "
         "Courses that are offered in several ways (for example a university course and its MOOC) are listed once, "
         "with all their offerings.", "",
         "## Contents", ""]
    for g in d["groups"]:
        L.append("- [%s](#%s)" % (g["name"], g["name"].lower().replace(" ", "-").replace(",", "")))
    L += ["- [Which course uses which book and software](#which-course-uses-which-book-and-software)",
          "- [How to contribute](#how-to-contribute)", ""]
    topics = d["topics"]
    for g in d["groups"]:
        items = [r for r in res if r["group"] == g["id"] and not r.get("hidden")]
        L += ["## " + g["name"], "", g["description"], ""]
        if g["id"] == "software":
            L += ["| Software | Developer | License | Used by | Notes |", "|---|---|---|---|---|"]
            for r in items:
                ub = ", ".join(by[x]["name"] for x in r["used_by"]) or ""
                L.append("| %s | %s | %s | %s | %s |" % (md_link(r), r.get("institution", r.get("people", "")),
                                                        r.get("license", ""), ub, r.get("note", "")))
            L.append("")
            continue
        L += ["| Resource | Year | " + " | ".join(n for _, n in MATS) + " | Software | Topics |",
              "|---|---|" + "|".join([":-:"] * len(MATS)) + "|---|---|"]
        for r in items:
            m = r.get("materials", {})
            cells = [ICON[m[k]["status"]] if k in m else "" for k, _ in MATS]
            sw = ", ".join(by[x]["name"] for x in r.get("uses_software", []))
            who = r.get("institution", "")
            L.append("| %s<br><sub>%s</sub> | %s | %s | %s | %s |" % (
                md_link(r), who, r.get("year", ""), " | ".join(cells), sw,
                ", ".join(topics[t] for t in r.get("topics", []))))
        L.append("")
        L.append("<details><summary>Details: offerings, sources of each material, notes</summary>")
        L.append("")
        for r in items:
            L.append("**%s** — %s%s" % (r["name"], r.get("people", ""), (" (%s)" % r["institution"]) if r.get("institution") else ""))
            L.append("")
            for o in r.get("offerings", []):
                L.append("- %s: %s%s" % ("Offering", "[%s](%s)" % (o["name"], o["url"]), " — " + o["cost"] if o.get("cost") else ""))
            mv = ["%s: %s%s" % (n, WORD[r["materials"][k]["status"]], (" (%s)" % r["materials"][k]["via"]) if r["materials"][k].get("via") else "")
                  for k, n in MATS if k in r.get("materials", {})]
            if mv: L.append("- Materials: " + "; ".join(mv))
            links = []
            if r.get("uses_books"): links.append("Textbook: " + ", ".join(by[x]["name"] for x in r["uses_books"]))
            if r.get("derived_from"): links.append("Built for: " + ", ".join(by[x]["name"] for x in r["derived_from"]))
            if r["used_by"]: links.append("Used by: " + ", ".join(by[x]["name"] for x in r["used_by"]))
            if links: L.append("- " + " · ".join(links))
            if r.get("note"): L.append("- " + r["note"].strip())
            L.append("")
        L += ["</details>", ""]
    # matrix
    courses = [r for r in res if r["group"] in ("course", "mooc", "learning", "labs", "video") and (r.get("uses_books") or r.get("uses_software"))]
    cols = [x for x in by if by[x]["group"] in ("book", "software") and by[x]["used_by"]]
    L += ["## Which course uses which book and software", "",
          "| Course | " + " | ".join(by[c].get("short", by[c]["name"]) for c in cols) + " |",
          "|---|" + "|".join([":-:"] * len(cols)) + "|"]
    for r in courses:
        u = set(r.get("uses_books", [])) | set(r.get("uses_software", []))
        L.append("| %s | %s |" % (r.get("short", r["name"]), " | ".join("●" if c in u else "" for c in cols)))
    L += ["", "## How to contribute", "",
          "All data is in [`resources.yaml`](resources.yaml). Edit or add an entry, run `python build.py`, and open a "
          "pull request. The README and the web page are generated from the YAML file; do not edit them by hand. "
          "The format of an entry is described at the top of the YAML file.", "",
          "Last checked: %s." % d.get("checked", "November 2026"), ""]
    return "\n".join(L)


# ------------------------------------------------------------------ web page
def page(d, res, by):
    data = {"groups": d["groups"], "topics": d["topics"], "mats": MATS, "resources": res}
    tpl = (ROOT / "page_template.html").read_text(encoding="utf-8")
    return tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))


def main():
    d, res, by = load()
    outs = {ROOT / "README.md": readme(d, res, by), ROOT / "docs" / "index.html": page(d, res, by)}
    if "--check" in sys.argv:
        stale = [str(p.relative_to(ROOT)) for p, t in outs.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale: sys.exit("Generated files are out of date, run python build.py: " + ", ".join(stale))
        print("up to date"); return
    for p, t in outs.items():
        p.parent.mkdir(exist_ok=True); p.write_text(t, encoding="utf-8")
    print("wrote README.md and docs/index.html (%d resources)" % len(res))


if __name__ == "__main__":
    main()
