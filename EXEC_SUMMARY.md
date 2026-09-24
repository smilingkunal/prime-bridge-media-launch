# PBM Operations Setup — Executive Summary

**Status:** Pre-operations. Infrastructure 40% built; automation 30% wired.  
**Target:** ₹3–5L MRR (Oct '26), ₹1Cr (Dec '27)  
**Blocker count:** 4 critical | **Gap analysis:** 14 identified  
**ETA to "ops ready":** 2–3 weeks  

---

## What's Working

✅ **Website live** — primebridgemedia.com cached, ranked for brand keywords  
✅ **WordPress + Rank Math** — schema, metadata, pillar structure ready  
✅ **n8n imported** — workflow exists, just needs credentials  
✅ **Python pipeline** — 10 passing tests, content validation working  
✅ **VPS running** — nginx, PHP, MariaDB, Caddy SSL, n8n Docker  
✅ **Lead tracker sheet** — 5-week playbook, manual daily calls documented  

## What's Not Working (Critical)

🔴 **n8n is inactive** — credentials not wired. Phase 0 incomplete. Content factory never ran.  
🔴 **Lead CRM is manual** — Google Sheet only. No scoring, no automation, no forecasting.  
🔴 **Lead gen at scale** — Apify MCP installed but no workflow. Enrichment manual-only.  
🔴 **Hermes cron may not fire** — "Gateway running" unverified. No scheduled jobs active.  

## What's Missing (High impact)

| Gap | Blocker? | Fix time | Why it matters |
|---|---|---|---|
| **n8n credentials** | YES | 1h | Unblocks 10+ posts/mo, daily drafts |
| **CRM + scoring** | YES | 2h setup + config | Stop wasting sales time on unqualified leads |
| **Cron verification** | YES | 30m | All automation depends on this |
| **Lead-gen workflow** | NO | 1 day | 50+ leads/week auto-flowing to CRM |
| **Email campaign** | NO | 1 day | Execute outreach at scale, track replies |
| **Weekly SEO report** | NO | 1 day | Visibility into rank movements, alerts |
| **KPI dashboard** | NO | 1 day | Daily visibility into ₹1Cr pace |

## This Week (Sept 24–30)

Do these 5 things. Nothing else moves without them:

1. **Get n8n ready** (90 min)
   - Log into n8n, complete owner-account setup
   - Add 3 credentials: OpenRouter, Pexels, WordPress app password
   - Wire them to 6 workflow nodes
   - Run one dry-run with Doctors × Chandigarh topic

2. **Move Lead Tracker to Airtable** (2 hr)
   - Export Google Sheet
   - Import to Airtable free tier
   - Add ICP scoring formula: GBP reviews + website age + social presence
   - Auto-filter ICP ≥7 into "qualified" view

3. **Verify Hermes cron** (30 min)
   - Terminal: `hermes cron status`
   - Confirm: "Gateway is running — cron jobs will fire automatically"
   - If not: `hermes gateway install && hermes gateway start`

4. **Schedule VPS backups** (45 min)
   - WordPress: daily snapshot (1 click in DO console)
   - n8n config: weekly export
   - Add monitoring: UptimeRobot free tier

5. **Build Obsidian vault structure** (1 hr)
   - Create folders: Site / SEO / Funnels / Blog / Images / Ops / State
   - Copy from pbm-orchestrator spec
   - Connect to n8n outputs

**Time commitment:** 5 hours  
**Unblocks:** 70% of remaining work

---

## Next Week (Oct 1–7)

Once blockers cleared:

6. **Build lead-gen bot** (1 day)  
   - n8n: Apify scraper → Email finder → Verifier → Airtable
   - Schedule: Monday 08:00 IST
   - Auto-add ICP ≥7 to Lead Tracker

7. **Wire email campaign** (1 day)  
   - n8n: template render → Resend send → webhook tracking
   - Test: send 5 personal emails, verify delivery + replies
   - Deploy approval gate

8. **One keyword map** (1 day)  
   - Doctors × Chandigarh: 50–100 keywords, 5–8 pillars
   - Content briefs for top 3
   - Use as template for other 27 niche×city

---

## Costs

| Item | Monthly |
|---|---|
| OpenRouter (1–2 LLM calls/day) | ~$20 |
| Pexels premium (750 images/mo) | $10 |
| Airtable | $10–20 (or free) |
| UptimeRobot monitoring | $0 |
| **Total new spend** | ~$40–50/mo |

---

## Proof Points (this week)

By Friday Sept 27, you'll have:
- ✓ n8n running ≥1 successful dry-run
- ✓ Airtable CRM with 10+ leads scored
- ✓ Cron status confirmed as "Gateway running"
- ✓ VPS backups scheduled
- ✓ Obsidian vault live with bot write paths mapped

This is when you know you're on track. If any of these 5 don't ship by Fri, the whole ops plan slips by 1 week.

---

## Then What?

Once blockers ship, the remaining gaps fall like dominoes:

- Lead gen workflows feed CRM automatically → sales team can focus on meetings, not list-building
- Email campaigns execute at scale → 50 outreaches/week, not 5
- Weekly SEO reports auto-generate → visibility into rank trends without manual checking
- KPI dashboard shows daily progress → you know on Sept 30 if ₹3–5L is still realistic

**Without these, you're still in "scrappy founder" mode — managing everything manually, can't scale past 10 leads/week, can't forecast anything.**

**With these, you're in "operations" mode — systems running, you measure instead of grind.**

---

**Bottom line:** 5 hours of setup this week unlocks 2–3 months of velocity. The gap analysis has full specs. Pick the top 3 and get going.
