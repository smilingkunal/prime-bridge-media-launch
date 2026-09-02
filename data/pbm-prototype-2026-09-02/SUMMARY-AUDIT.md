# Website Audit Pipeline — Final Results, 2026-09-02

**Cost:** $0 (Python urllib only, no API calls)
**Speed:** 266 URLs in 48 seconds (parallel, 20 workers)
**Actor:** None — direct HTTP via urllib

#### Pipeline summary

| Step | Tool | Output |
|---|---|---|
| 1. Filter gyms with real websites | regex | 266 (excluded 81 IG/YT/App links) |
| 2. HTTP audit each site | Python urllib + ThreadPoolExecutor | 226 returned HTML, 40 timeout/error |
| 3. Detect tracking/schema/form/responsive | regex + string search | 17 signals per site |
| 4. Score per buying-signals playbook | additive model | 792 leads → 129 addressable |

#### Final tier breakdown

| Tier | Score | Action | Count |
|---|---|---|---|
| **Tier 1** | ≥9 | Personal outreach with custom audit (call + WhatsApp) | **10** |
| **Tier 2** | 7-8 | Nurture sequence (3-email + IG DM) | 18 |
| **Tier 3** | 5-6 | Low-touch drip (1 message) | 101 |
| **Drop** | <5 | Skip | 137 |

**129 addressable leads out of 266 audited websites (48%).**

#### Tier 1 — Priority personal outreach

| # | Name | City | Reviews | Website Issue |
|---|---|---|---|---|
| 1 | **ULTIMATE FITNESS** | Mohali | 1,470 | Parked domain (GoDaddy placeholder) + zero tracking + no form |
| 2 | **Elite Edge Gym and Spa** | Chandigarh | 302 | Zero tracking, no schema, no form, not responsive |
| 3 | **Healing Hands Chiro & Wellness** | Chandigarh | 239 | Hybrid clinic+fitness, zero tracking, no form |
| 4 | **Shrug Life CF** | Kansal/Mohali | 109 | Zero tracking, no schema, no form, not responsive |
| 5 | **Gym13 Sector 22** | Chandigarh | 222 | Zero tracking + parked domain |
| 6 | **YoKalp (Pilates & Yoga)** | Chandigarh | 202 | Parked domain + zero tracking |
| 7 | **YoKalp (Pilates & Yoga)** | Mohali | 196 | Parked domain + zero tracking (different location) |
| 8 | **Yokalp Pilates & Yoga** | Panchkula | 163 | Parked domain + zero tracking (3rd YoKalp location) |
| 9 | **Infinity Lift** | Zirakpur | 103 | Parked domain + zero tracking |
| 10 | **YogAahar** | Chandigarh | 19 | Zero tracking, no form, not responsive |

**Note: "YoKalp" appears as 3 separate franchise locations — same parent company, 561 combined reviews. Multi-location = single close.**

#### City distribution (Tier 1)

| City | Tier 1 |
|---|---|
| Chandigarh | 5 |
| Mohali (incl. Sahibzada Ajit Singh Nagar) | 3 |
| Kansal | 1 |
| Panchkula | 1 |
| Zirakpur | 1 |

#### What the audit detected

- **15 parked domains** — businesses that paid for hosting/URL but lost it (or never set up). Highest urgency.
- **~70%** of audited sites have **zero conversion tracking** (no Meta Pixel, no GA4) — strongest audit hook.
- **~75%** have **no contact form or WhatsApp CTA** — every visitor bounces.
- **~60%** lack **local-business schema** — losing map pack ranking.
- **~40%** are **not mobile-responsive** by viewport-meta standard.

#### Files produced

| File | Content |
|---|---|
| `audit-real-sites.csv` | 266 gyms (filtered, no IG/YT) |
| `audit-raw.csv` | 266 raw audit results (17 signals) |
| `audit-scored.csv` | 266 ranked by score |
| `tier-1-priority.csv` | 10 leads for personal outreach |
| `tier-2-nurture.csv` | 18 leads for nurture sequence |
| `tier-3-drip.csv` | 101 leads for drip |
| `tier-1-outreach-drafts.md` | 10 personalized outreach messages ready to send |

#### Recommended next actions

1. **Send 10 Tier-1 messages today** — WhatsApp is faster than email for India. Use the drafts as templates but personalize the opening line per business.
2. **Book 3-5 audit calls this week** — each call is ~15 min, shows the 3 broken things on their site, then closes on retainer.
3. **Set up Tier 2 nurture drip** — 18 leads for a 3-email sequence ("Quick observation about your site" → "Here's the audit" → "Case study + offer").
4. **Skip Apify Meta Ad Library scrape** — we already have enough signal density. Direct outreach to Tier 1 is faster than automating.

#### Total prototype cost

- Meta Ad Library (initial wrong direction): $0.34
- Google Maps (4 cities): $4.24
- Website audit (266 sites): $0.00
- **Total: $4.58**

**Outcome: 10 hot leads ready to contact today, 18 nurture, 101 drip — across the entire Tricity+Zirakpur gym market for under $5.**