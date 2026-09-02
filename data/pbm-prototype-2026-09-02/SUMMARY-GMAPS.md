# Google Maps Prototype — Gyms in Tricity + Zirakpur, 2026-09-02

**Cost:** $4.24 total (4 actor runs, ~5 min total runtime)
**Actor:** compass/crawler-google-places
**Output:** `tricity-zirakpur-gyms-2026-09-02.csv` (792 unique gyms, 17 fields each)

#### Headline numbers

| | |
|---|---|
| Raw records pulled | 1,059 |
| Classified as gym/fitness | 947 |
| Unique (deduped by phone/placeId) | **792** |
| Active (not closed) | 760 |
| With website | 347 (43.8%) — audit-hook targets |
| With phone | 634 (80.1%) — direct-call ready |
| With 50+ reviews | 385 — priority targets |

#### City breakdown

| City | Unique gyms |
|---|---|
| Chandigarh | 305 |
| Mohali | 187 |
| Zirakpur | 161 |
| Panchkula | 108 |
| Other | 31 |

#### Top priority targets (≥1,000 reviews)

| Name | City | Reviews | Rating | Has Website |
|---|---|---|---|---|
| R fitness Gym & Swimming Pool | Chandigarh | 6,664 | 4.8 | No |
| Pro Ultimate Gyms | Panchkula | 1,655 | 4.9 | Yes |
| Pro Ultimate Gyms Sector 38 | Chandigarh | 1,578 | 4.9 | No |
| ULTIMATE FITNESS | Mohali | 1,470 | 4.8 | Yes |
| Pro Ultimate Gyms Sector 91 | Mohali | 1,412 | 4.9 | Yes |
| Burn Gym Sector 8 | Panchkula | 1,384 | 4.7 | Yes |
| Pro Ultimate Gyms Sec 46 | Chandigarh | 1,359 | 4.7 | Yes |
| Burn Gym Phase 5 | Mohali | 1,356 | 4.6 | Yes |
| Wao Fitness | Chandigarh | 1,312 | 4.9 | No |
| Olympic Physiotherapy & Fitness | Panchkula | 1,191 | 5.0 | Yes |
| Pro Ultimate Gyms Dhakoli | Zirakpur | 1,117 | 4.8 | Yes |
| Burn Gym Phase 9 | Mohali | 1,088 | 4.7 | Yes |

**Multi-location chains detected** — these are the highest-value targets because they have a central marketing budget AND multiple audit sites:
- **Pro Ultimate Gyms** — 4 locations across Panchkula, Chandigarh, Mohali, Zirakpur
- **Burn Gym** — 3 locations across Panchkula, Mohali

#### Next step — audit the leads

For each gym with a website (347), we need to run the next step in the pipeline:

1. `curl` homepage → grep for `gtag`, `fbq(`, `analytics.js`, schema markup, lead form
2. Check PageSpeed Insights API for CWV score
3. Look up the FB/IG page from the website → confirm if they're running ads
4. Score per your formula (Layer 1-4) and prioritize ≥8s for custom outreach

**Estimated cost for next step:**
- Website audit (347 sites): free (curl) + PageSpeed API (free tier)
- FB/IG lookup: ~$5 via Apify (Instagram profile scraper, batch 347 profiles)
- Total: ~$5

**Expected yield:** from 792 gyms × 38% with websites × ~10% running ads badly × 60% high-deal-value = **~18-25 qualified leads** for personal outreach.

#### Recommendations

1. **Start with the 347 gyms that have one** — these are pre-filtered as "has digital presence to audit"
2. **Prioritize Pro Ultimate Gyms + Burn Gym** — multi-location = single close = 4-7 audit deliverables
3. **Add 'physiotherapy + fitness' as a secondary category** — Olympic Physio at 1,191 reviews is hybrid: clinic + gym = high deal value (medical-adjacent)

#### File

`C:\Users\kunal\pbm-launch-dashboard\data\pbm-prototype-2026-09-02\tricity-zirakpur-gyms-2026-09-02.csv` (792 rows, 17 cols)