# Meta Ad Library Prototype — Gym keyword, IN, 2026-09-02

**Cost:** $0.34 (496 ads, 131s runtime)
**Actor:** curious_coder/facebook-ads-library-scraper

## Headline findings

1. **Keyword "gym" returns ~95% noise.** The Ad Library matches any ad whose text/copy contains the word "gym", regardless of whether the advertiser IS a gym. Amazon product ads for "gym shoes", audiobooks mentioning "Gym में workout", supplement brands, equipment manufacturers — all surface.
2. **No geo filter at query time.** Even with `scrapeAdDetails=true`, the per-ad `location_audience` array is only populated for EU-targeted ads (DSA disclosure). Indian ad geo isn't exposed.
3. **Of 349 unique advertisers found:** only ~10 are recognizable gym chains. The rest are D2C brands, apps, or noise.
4. **Zero hits for Chandigarh/Mohali/Panchkula/Zirakpur.** Cannot identify local gyms from this dataset.

## Classification breakdown (unique ads: 349)

| Label | Count | % |
|---|---|---|
| unknown | 254 | 72.8% |
| possible_local_trainer | 38 | 10.9% |
| noise | 31 | 8.9% |
| inconclusive_d2c | 16 | 4.6% |
| real_gym | 10 | 2.9% |

## Conclusion — do NOT scale this approach

The Meta Ad Library keyword search is the wrong tool for finding local gyms running ads in a specific city. The intended "filter advertisers by location" requires either:

- A. **Switch source to Google Maps Scraper** — search "gym" in Chandigarh → get ~80-150 real local gyms → then check EACH gym's FB page to see if they're running ads.
- B. **Use Instagram Graph API via Apify** — search IG by geo + niche hashtag → get real local businesses. Better geo fidelity.
- C. **Switch the entire wedge.** The strongest signal isn't "running Meta ads" — for the gym vertical in Tricity, the strongest signal is likely "active Instagram with low engagement + no GBP" or "Real Estate brokerage with no CRM."

## Recommended next step

Pivot to **Google Maps approach (option A)**. Cost: ~$0.40 for gyms in 6 zips. This gives us the actual local business list. THEN check each for active Meta ads + site issues.
