# Prime Bridge Media — Week 1 Launch Dashboard

> Live tracker for the PBM Phase 1 launch. 7-day sprint, Tricity + Zirakpur.
> Hosted on GitHub Pages: `https://kunaldahiya.github.io/prime-bridge-media-launch/`

## What's inside

- **`index.html`** — single-page dashboard, dark terminal style, no build step
- **`data.json`** — all tasks, KPIs, risks, checklists. Edit this file to update the dashboard.
- **`CNAME`** — (optional) custom domain mapping

## How to update

1. Edit `data.json` — add new tasks, tick items to `done: true`, update KPIs
2. Commit + push
3. GitHub Pages auto-rebuilds in ~30 seconds
4. Hard-refresh the dashboard (Cmd/Ctrl+Shift+R)

The dashboard also persists checkbox state in your browser's localStorage, so the
data.json `done: true` is the source of truth for visitors who haven't interacted.

## Local preview

```bash
# any static server works; e.g.
python -m http.server 8000
# then open http://localhost:8000
```

## Source of truth

Tasks are mirrored from the Obsidian note:
`Prime Bridge Media/SEO/Launch/00 - Week 1 Content Pack.md`

When you tick something in the dashboard, also update the Obsidian note (and vice versa).
The `meta.last_updated` field in `data.json` should be bumped each time you edit.

## Sprint details

- **Start:** 2026-08-18
- **End:** 2026-08-25
- **Owner:** Kunal Dahiya
- **Coverage:** Chandigarh, Mohali, Panchkula, Zirakpur
- **Services:** Local SEO, YouTube Ads, Meta Ads, WordPress
- **Niches:** Doctors, Restaurants, Salons, Gyms, Lawyers, Real Estate
