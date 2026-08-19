#!/usr/bin/env python3
"""Build complete Elementor data for YouTube Ads and Meta Ads pages."""
import json

# Import the helper functions
import sys
sys.path.insert(0, "C:/Users/kunal/pbm-launch-dashboard")
from build_local_seo_complete import (
    make_industries_section, make_pricing_section, make_faq_section, make_cta_section
)

# ============================================
# YOUTUBE ADS
# ============================================
youtube_ads_data = []

# HERO
youtube_ads_data.append({
    "id": "pbm_svc_hero",
    "elType": "section",
    "settings": {
        "_title": "Hero",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "100", "right": "30", "bottom": "100", "left": "30", "isLinked": False},
        "background_background": "gradient",
        "background_color": "#004CB1",
        "background_color_b": "#003380",
        "background_gradient_angle": {"unit": "deg", "size": 135}
    },
    "elements": [
        {
            "id": "pbm_svc_hero_heading",
            "elType": "widget",
            "settings": {
                "title": "YouTube Ads Agency in Chandigarh-Tricity",
                "header_size": "h1",
                "align": "center",
                "title_color": "#FFFFFF",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 48},
                "typography_font_weight": "700",
                "typography_line_height": {"unit": "em", "size": 1.2}
            },
            "elements": [], "widgetType": "heading"
        },
        {
            "id": "pbm_svc_hero_subheading",
            "elType": "widget",
            "settings": {
                "editor": "<p>Reach 2.5 million Tricity viewers on YouTube. Target by city + interest + intent. Pay only when they watch. Get leads at \u20b9100-500 each.</p>",
                "align": "center",
                "text_color": "#FFFFFF",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 18},
                "typography_font_weight": "400",
                "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
            },
            "elements": [], "widgetType": "text-editor"
        },
        {
            "id": "pbm_svc_hero_cta",
            "elType": "widget",
            "settings": {
                "text": "Get a free strategy",
                "selected_icon": {"value": "fas fa-arrow-right", "library": "fa-solid"},
                "icon_align": "right", "icon_indent": {"unit": "px", "size": 12},
                "background_color": "#FFFFFF",
                "button_text_color": "#004CB1",
                "hover_color": "#FFFFFF",
                "button_background_hover_color": "#FFB800",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 16},
                "typography_font_weight": "600",
                "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
                "align": "center",
                "link": {"url": "/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""}
            },
            "elements": [], "widgetType": "button"
        }
    ]
})

# INTRO
youtube_ads_data.append({
    "id": "pbm_svc_intro",
    "elType": "section",
    "settings": {
        "_title": "Introduction",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "40", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#FFFFFF"
    },
    "elements": [
        {
            "id": "pbm_svc_intro_heading",
            "elType": "widget",
            "settings": {
                "title": "Why YouTube Ads are Tricity's most underused growth channel",
                "header_size": "h2",
                "align": "left",
                "title_color": "#1A1A1A",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 36},
                "typography_font_weight": "700"
            },
            "elements": [], "widgetType": "heading"
        },
        {
            "id": "pbm_svc_intro_text",
            "elType": "widget",
            "settings": {
                "editor": "<p>Every month, <strong>2.5 million people in Chandigarh-Mohali-Panchkula</strong> open YouTube. They watch for an average of 35 minutes per session. They're watching how-to videos, music, product reviews, local news \u2014 and importantly, your competitors' ads.</p><p>But here's the thing: <strong>almost no Tricity business is running YouTube ads</strong>. YouTube ads have a reputation for being 'expensive' (they're actually the cheapest CPM in India), 'hard to set up' (they're easier than Meta ads), and 'only for big brands' (they work brilliantly for \u20b930K/month budgets).</p><p>We run YouTube ads for local businesses in Tricity. Our clients get <strong>CPV of \u20b90.02-0.10</strong> and <strong>leads at \u20b9100-500 each</strong> \u2014 numbers that would make a Google Ads consultant cry.</p>",
                "text_color": "#444444",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": 17},
                "typography_line_height": {"unit": "em", "size": 1.7},
                "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
            },
            "elements": [], "widgetType": "text-editor"
        }
    ]
})

# STATS
youtube_ads_data.append({
    "id": "pbm_svc_stats",
    "elType": "section",
    "settings": {
        "_title": "Stats / Social Proof",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "40", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#F7F8FA"
    },
    "elements": [
        {
            "id": "pbm_svc_stats_row",
            "elType": "column",
            "settings": {"content_width": {"unit": "%", "size": 100}},
            "elements": [
                {"id": "pbm_svc_stats_1", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_stats_1_widget", "elType": "widget",
                    "settings": {"title_text": "2.5M", "description_text": "Tricity viewers watching YouTube every month",
                                  "title_color": "#004CB1", "description_color": "#666666",
                                  "title_typography_typography": "custom",
                                  "title_typography_font_size": {"unit": "px", "size": 48},
                                  "title_typography_font_weight": "700", "align": "center"},
                    "elements": [], "widgetType": "counter"}]},
                {"id": "pbm_svc_stats_2", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_stats_2_widget", "elType": "widget",
                    "settings": {"title_text": "\u20b90.02", "description_text": "average cost per view (CPV) on TrueView",
                                  "title_color": "#004CB1", "description_color": "#666666",
                                  "title_typography_typography": "custom",
                                  "title_typography_font_size": {"unit": "px", "size": 48},
                                  "title_typography_font_weight": "700", "align": "center"},
                    "elements": [], "widgetType": "counter"}]},
                {"id": "pbm_svc_stats_3", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_stats_3_widget", "elType": "widget",
                    "settings": {"title_text": "\u20b9100-500", "description_text": "cost per lead for our local business clients",
                                  "title_color": "#004CB1", "description_color": "#666666",
                                  "title_typography_typography": "custom",
                                  "title_typography_font_size": {"unit": "px", "size": 48},
                                  "title_typography_font_weight": "700", "align": "center"},
                    "elements": [], "widgetType": "counter"}]}
            ]
        }
    ]
})

# PROCESS (5 steps for YouTube Ads)
youtube_ads_data.append({
    "id": "pbm_svc_process",
    "elType": "section",
    "settings": {
        "_title": "Our 5-Step Process",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#FFFFFF"
    },
    "elements": [
        {"id": "pbm_svc_process_heading", "elType": "widget",
         "settings": {"title": "Our 5-step YouTube Ads system", "header_size": "h2",
                      "align": "center", "title_color": "#1A1A1A",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 36},
                      "typography_font_weight": "700"},
         "elements": [], "widgetType": "heading"},
        {"id": "pbm_svc_process_subheading", "elType": "widget",
         "settings": {"editor": "<p style=\"text-align: center;\">From strategy to scale in 5 weeks</p>",
                      "text_color": "#666666",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 17},
                      "_margin": {"unit": "px", "top": "10", "right": "0", "bottom": "40", "left": "0", "isLinked": False}},
         "elements": [], "widgetType": "text-editor"},
        {
            "id": "pbm_svc_process_row1",
            "elType": "column",
            "settings": {"content_width": {"unit": "%", "size": 100}},
            "elements": [
                {"id": "pbm_svc_process_1", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_1_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-1", "library": "fa-solid"},
                                  "title_text": "Strategy + audience research",
                                  "description_text": "60-min call + 5-page strategy doc. Who, what, where, how much \u2014 all documented before we spend \u20b91.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_2", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_2_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-2", "library": "fa-solid"},
                                  "title_text": "Video creative",
                                  "description_text": "Use your existing video, we direct your iPhone shoot, or we produce custom (\u20b915-30K). Most winners are 20-30 sec iPhone clips.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_3", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_3_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-3", "library": "fa-solid"},
                                  "title_text": "Campaign structure + targeting",
                                  "description_text": "TrueView for action, layered targeting (location > demo > interest > behavior), custom intent audiences, placement exclusions.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]}
            ]
        },
        {
            "id": "pbm_svc_process_row2",
            "elType": "column",
            "settings": {"content_width": {"unit": "%", "size": 100}, "_margin": {"unit": "px", "top": "30", "right": "0", "bottom": "0", "left": "0", "isLinked": False}},
            "elements": [
                {"id": "pbm_svc_process_4", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 50}},
                 "elements": [{"id": "pbm_svc_process_4_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-4", "library": "fa-solid"},
                                  "title_text": "Creative testing + iteration",
                                  "description_text": "Multiple video lengths (6-30 sec), hooks, CTAs, landing page variants. Kill bottom 50% after 2 weeks, scale top 50%.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_5", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 50}},
                 "elements": [{"id": "pbm_svc_process_5_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-5", "library": "fa-solid"},
                                  "title_text": "Conversion tracking + optimization",
                                  "description_text": "Full Google Ads conversion tracking, GA4 events, call tracking, offline conversion uploads. Weekly bid + creative refreshes.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]}
            ]
        }
    ]
})

# INDUSTRIES
youtube_industries = [
    ("fas fa-stethoscope", "Doctors + Clinics",
     "Patient leads at \u20b9150-400 each. Best for: dental implants, cosmetic procedures, IVF, hair transplant, eye surgery."),
    ("fas fa-utensils", "Restaurants + Cafes",
     "Food video ads targeting foodies in your delivery radius. People watch food videos 3x longer than average YouTube videos."),
    ("fas fa-cut", "Salons + Spas",
     "Before/after transformations, stylist showcases, treatment demos. Visual content that converts browsers to bookers."),
    ("fas fa-home", "Real Estate (brokers + developers)",
     "Property walkthroughs, location showcases, amenity tours. Target high-intent buyers in your budget range."),
]
youtube_ads_data.append(make_industries_section(youtube_industries, "pbm_svc_industries_yt"))

# PRICING (YouTube: ₹8k/campaign + 10% if ad budget > ₹1L)
youtube_pricing = [
    {
        "title": "Starter",
        "desc": "Test the channel",
        "price": "\u20b98,000",
        "period": "/campaign",
        "features": [
            "1 campaign setup",
            "Up to 2 ad groups",
            "Basic audience research",
            "1 round of creative review",
            "Weekly performance check"
        ]
    },
    {
        "title": "Growth",
        "desc": "Most popular",
        "price": "\u20b98,000 + 10%",
        "period": "if ad budget > \u20b91L/mo",
        "popular": True,
        "features": [
            "Full campaign management",
            "Multi-ad-group structure",
            "Advanced targeting + retargeting",
            "Bi-weekly creative refresh",
            "Conversion tracking setup",
            "Weekly performance reports",
            "10% mgmt fee on budgets > \u20b91L/mo"
        ]
    },
    {
        "title": "Pro",
        "desc": "Multi-campaign scaling",
        "price": "Custom",
        "period": "/month",
        "features": [
            "Everything in Growth",
            "Multiple campaigns + audiences",
            "Custom video production coordination",
            "Weekly creative refresh",
            "Dedicated account manager",
            "Quarterly strategy reviews"
        ]
    }
]
youtube_ads_data.append(make_pricing_section(youtube_pricing, "pbm_svc_pricing_yt"))

# FAQ (YouTube-specific)
youtube_faq = [
    ("Can I just run YouTube ads myself?",
     "Yes, you can. But most business owners burn \u20b950K-1,00,000 on testing before figuring out what works. We have data from 30+ campaigns and can usually get to profitable in 2-4 weeks vs 2-4 months of solo testing."),
    ("Do I need a professional video?",
     "No. We've gotten \u20b90.03 CPV from iPhone footage. The video just needs to be vertical, well-lit, and the first 3 seconds must hook the viewer. We'll direct your iPhone shoot for free \u2014 we send you a shot list, you film, we edit."),
    ("How long until I get leads?",
     "You can get leads in week 1. Whether they're <em>good</em> leads depends on your offer and sales process. We optimize for <em>qualified</em> leads, not just any lead. Our healthcare clients get patient leads at \u20b9150-400 each that book consultations."),
    ("What about YouTube Shorts?",
     "Yes, we include Shorts in every strategy. Shorts get even cheaper CPVs (\u20b90.01-0.05) and are huge in India. We test both long-form in-stream and Shorts to find what works for your business."),
    ("What's the minimum ad budget?",
     "\u20b930,000/month is the minimum for meaningful testing. Below that, you don't have enough data to optimize. We also recommend 3-month minimum commitment \u2014 the algorithm needs 2-4 weeks to learn your audience. We don't run campaigns under \u20b930K budget.")
]
youtube_ads_data.append(make_faq_section(youtube_faq, "pbm_svc_faq_yt"))

# FINAL CTA
youtube_ads_data.append(make_cta_section(
    heading="Ready to reach 2.5M Tricity viewers on YouTube?",
    subheading="Book a free 30-minute call. We'll research your industry's CPV benchmarks, identify your target audience, and send you a custom 90-day YouTube strategy. No commitment."
))

# Save
with open("C:/Users/kunal/pbm-launch-dashboard/youtube-ads-final.json", "w") as f:
    json.dump(youtube_ads_data, f, indent=2)
print(f"YouTube Ads FINAL: {len(json.dumps(youtube_ads_data))} bytes, {len(youtube_ads_data)} sections")


# ============================================
# META ADS
# ============================================
meta_ads_data = []

# HERO
meta_ads_data.append({
    "id": "pbm_svc_hero",
    "elType": "section",
    "settings": {
        "_title": "Hero",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "100", "right": "30", "bottom": "100", "left": "30", "isLinked": False},
        "background_background": "gradient",
        "background_color": "#004CB1",
        "background_color_b": "#003380",
        "background_gradient_angle": {"unit": "deg", "size": 135}
    },
    "elements": [
        {"id": "pbm_svc_hero_heading", "elType": "widget",
         "settings": {"title": "Meta Ads Agency in Chandigarh-Tricity (Facebook + Instagram)", "header_size": "h1",
                      "align": "center", "title_color": "#FFFFFF",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 48},
                      "typography_font_weight": "700", "typography_line_height": {"unit": "em", "size": 1.2}},
         "elements": [], "widgetType": "heading"},
        {"id": "pbm_svc_hero_subheading", "elType": "widget",
         "settings": {"editor": "<p>Get calls, bookings, and store visits from real customers in your area \u2014 not vanity metrics. Facebook + Instagram ads that work for local businesses.</p>",
                      "align": "center", "text_color": "#FFFFFF",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 18},
                      "typography_font_weight": "400",
                      "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "30", "left": "0", "isLinked": False}},
         "elements": [], "widgetType": "text-editor"},
        {"id": "pbm_svc_hero_cta", "elType": "widget",
         "settings": {"text": "Get a free strategy", "selected_icon": {"value": "fas fa-arrow-right", "library": "fa-solid"},
                      "icon_align": "right", "icon_indent": {"unit": "px", "size": 12},
                      "background_color": "#FFFFFF", "button_text_color": "#004CB1",
                      "hover_color": "#FFFFFF", "button_background_hover_color": "#FFB800",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 16},
                      "typography_font_weight": "600",
                      "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                      "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
                      "align": "center", "link": {"url": "/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""}},
         "elements": [], "widgetType": "button"}
    ]
})

# INTRO
meta_ads_data.append({
    "id": "pbm_svc_intro",
    "elType": "section",
    "settings": {
        "_title": "Introduction",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "40", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#FFFFFF"
    },
    "elements": [
        {"id": "pbm_svc_intro_heading", "elType": "widget",
         "settings": {"title": "What are Meta Ads (and why most Tricity businesses run them wrong)",
                      "header_size": "h2", "align": "left", "title_color": "#1A1A1A",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 36},
                      "typography_font_weight": "700"},
         "elements": [], "widgetType": "heading"},
        {"id": "pbm_svc_intro_text", "elType": "widget",
         "settings": {"editor": "<p><strong>Meta Ads</strong> = Facebook Ads + Instagram Ads. Both managed from Meta Business Suite, same targeting, one campaign.</p><p>Most Tricity businesses run them wrong. The default campaign objective is 'engagement' \u2014 it optimizes for likes and comments, not leads. They target 'Chandigarh, 18-65' (1.2M people, no signal). They use stock photos with generic copy. The result: lots of impressions, zero calls.</p><p>We run <strong>conversion-optimized campaigns</strong> for local businesses. Lead gen, store traffic, WhatsApp messages, e-commerce. Tight targeting at the start, let Meta's algorithm find lookalikes after 2-3 weeks. Multiple creative variations tested weekly. Our clients get <strong>leads at \u20b950-500</strong> \u2014 vs \u20b9200-2000 from 'engagement' campaigns that most agencies run.</p>",
                      "text_color": "#444444", "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 17},
                      "typography_line_height": {"unit": "em", "size": 1.7},
                      "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "0", "left": "0", "isLinked": False}},
         "elements": [], "widgetType": "text-editor"}
    ]
})

# STATS
meta_ads_data.append({
    "id": "pbm_svc_stats",
    "elType": "section",
    "settings": {
        "_title": "Stats / Social Proof",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "40", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#F7F8FA"
    },
    "elements": [
        {"id": "pbm_svc_stats_row", "elType": "column",
         "settings": {"content_width": {"unit": "%", "size": 100}},
         "elements": [
            {"id": "pbm_svc_stats_1", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
             "elements": [{"id": "pbm_svc_stats_1_widget", "elType": "widget",
                "settings": {"title_text": "\u20b950-500", "description_text": "average cost per qualified lead for our clients",
                              "title_color": "#004CB1", "description_color": "#666666",
                              "title_typography_typography": "custom",
                              "title_typography_font_size": {"unit": "px", "size": 48},
                              "title_typography_font_weight": "700", "align": "center"},
                "elements": [], "widgetType": "counter"}]},
            {"id": "pbm_svc_stats_2", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
             "elements": [{"id": "pbm_svc_stats_2_widget", "elType": "widget",
                "settings": {"title_text": "2-5%", "description_text": "average landing page conversion rate (industry avg: 1-2%)",
                              "title_color": "#004CB1", "description_color": "#666666",
                              "title_typography_typography": "custom",
                              "title_typography_font_size": {"unit": "px", "size": 48},
                              "title_typography_font_weight": "700", "align": "center"},
                "elements": [], "widgetType": "counter"}]},
            {"id": "pbm_svc_stats_3", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
             "elements": [{"id": "pbm_svc_stats_3_widget", "elType": "widget",
                "settings": {"title_text": "40-70%", "description_text": "cost-per-result reduction from month 1 to month 3",
                              "title_color": "#004CB1", "description_color": "#666666",
                              "title_typography_typography": "custom",
                              "title_typography_font_size": {"unit": "px", "size": 48},
                              "title_typography_font_weight": "700", "align": "center"},
                "elements": [], "widgetType": "counter"}]}
        ]}
    ]
})

# PROCESS (5 steps for Meta Ads)
meta_ads_data.append({
    "id": "pbm_svc_process",
    "elType": "section",
    "settings": {
        "_title": "Our 5-Step Process",
        "content_width": {"unit": "px", "size": 1200},
        "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
        "background_background": "classic",
        "background_color": "#FFFFFF"
    },
    "elements": [
        {"id": "pbm_svc_process_heading", "elType": "widget",
         "settings": {"title": "Our 5-step Meta Ads system", "header_size": "h2",
                      "align": "center", "title_color": "#1A1A1A",
                      "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 36},
                      "typography_font_weight": "700"},
         "elements": [], "widgetType": "heading"},
        {"id": "pbm_svc_process_subheading", "elType": "widget",
         "settings": {"editor": "<p style=\"text-align: center;\">From strategy to scale in 5 weeks</p>",
                      "text_color": "#666666", "typography_typography": "custom",
                      "typography_font_size": {"unit": "px", "size": 17},
                      "_margin": {"unit": "px", "top": "10", "right": "0", "bottom": "40", "left": "0", "isLinked": False}},
         "elements": [], "widgetType": "text-editor"},
        {
            "id": "pbm_svc_process_row1", "elType": "column",
            "settings": {"content_width": {"unit": "%", "size": 100}},
            "elements": [
                {"id": "pbm_svc_process_1", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_1_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-1", "library": "fa-solid"},
                                  "title_text": "Strategy + audience research",
                                  "description_text": "10-page strategy doc. Customer avatars, competitor research, funnel structure, budget allocation \u2014 before we spend \u20b91.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_2", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_2_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-2", "library": "fa-solid"},
                                  "title_text": "Creative production",
                                  "description_text": "10-15 ad copy variations, 4-6 static images, 2-3 short videos (15-30 sec vertical for Reels).",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_3", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 33}},
                 "elements": [{"id": "pbm_svc_process_3_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-3", "library": "fa-solid"},
                                  "title_text": "Funnel build + landing pages",
                                  "description_text": "Dedicated landing pages (one offer, one form, one CTA). Funnel conversion: 2-5% vs industry average 1-2%.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]}
            ]
        },
        {
            "id": "pbm_svc_process_row2", "elType": "column",
            "settings": {"content_width": {"unit": "%", "size": 100}, "_margin": {"unit": "px", "top": "30", "right": "0", "bottom": "0", "left": "0", "isLinked": False}},
            "elements": [
                {"id": "pbm_svc_process_4", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 50}},
                 "elements": [{"id": "pbm_svc_process_4_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-4", "library": "fa-solid"},
                                  "title_text": "Launch + iterate",
                                  "description_text": "4 campaigns: awareness, traffic, conversion, retargeting. Daily monitoring week 1, weekly after. Kill losers, scale winners.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]},
                {"id": "pbm_svc_process_5", "elType": "section", "settings": {"_inline_size": {"unit": "%", "size": 50}},
                 "elements": [{"id": "pbm_svc_process_5_widget", "elType": "widget",
                    "settings": {"selected_icon": {"value": "fas fa-5", "library": "fa-solid"},
                                  "title_text": "Scale + optimize",
                                  "description_text": "20% budget increases on winners, duplicate to new audiences, test new placements, monthly strategy reviews.",
                                  "icon_color": "custom", "icon_color_custom": "#004CB1",
                                  "title_color": "#1A1A1A", "description_color": "#666666"},
                    "elements": [], "widgetType": "icon-box"}]}
            ]
        }
    ]
})

# INDUSTRIES
meta_industries = [
    ("fas fa-stethoscope", "Doctors + Clinics",
     "Patient acquisition: \u20b9150-500 per lead. Lead gen for appointments. Best for: dental, dermatology, ortho, eye, hair, weight loss."),
    ("fas fa-utensils", "Restaurants + Cafes",
     "Store traffic + delivery ads. Show the food, drive the orders. Cost per order: \u20b930-100."),
    ("fas fa-cut", "Salons + Spas",
     "Lead gen + WhatsApp messages. Discover on Instagram, book via WhatsApp. Cost per booking: \u20b980-300."),
    ("fas fa-home", "Real Estate",
     "Lead gen for property inquiries. Target high-intent buyers in your budget range. Cost per qualified lead: \u20b9500-2,500."),
]
meta_ads_data.append(make_industries_section(meta_industries, "pbm_svc_industries_meta"))

# PRICING (Meta Ads at ₹20k-80k/month, similar structure to YouTube)
meta_pricing = [
    {
        "title": "Starter",
        "desc": "Single objective",
        "price": "\u20b920,000",
        "period": "/month",
        "features": [
            "1 campaign objective (lead gen OR traffic)",
            "Up to 3 ad sets",
            "Basic audience research",
            "1 round of creative/month",
            "Bi-weekly check-ins"
        ]
    },
    {
        "title": "Growth",
        "desc": "Most popular",
        "price": "\u20b950,000",
        "period": "/month",
        "popular": True,
        "features": [
            "Full-funnel campaigns (awareness + traffic + conversion + retargeting)",
            "Unlimited ad sets",
            "Advanced targeting + lookalikes",
            "2-3 creative variations tested weekly",
            "Meta Pixel + CAPI setup",
            "Weekly performance reports",
            "Landing page recommendations"
        ]
    },
    {
        "title": "Pro",
        "desc": "Multi-campaign + e-commerce",
        "price": "\u20b980,000+",
        "period": "/month",
        "features": [
            "Everything in Growth",
            "Multi-campaign + multi-objective",
            "Custom creative production",
            "Daily optimization",
            "Dedicated account manager",
            "Monthly strategy reviews",
            "Quarterly business reviews"
        ]
    }
]
meta_ads_data.append(make_pricing_section(meta_pricing, "pbm_svc_pricing_meta"))

# FAQ (Meta-specific)
meta_faq = [
    ("Facebook or Instagram?",
     "Both \u2014 we run them as one campaign. The audience overlap on Facebook + Instagram is huge in Tricity (most people use both). We let Meta's algorithm optimize placement across both. If your target is 18-35, we'll bias toward Instagram. If 35+, Facebook. If 18-65, both equally."),
    ("Do I need a big following?",
     "No. Organic following and paid ads are completely separate. You can have 200 followers and run Meta Ads to 100,000 targeted people in your service area. In fact, some of our best-performing accounts have under 500 followers."),
    ("Can I run ads from my personal Facebook?",
     "No. You need a Meta Business Suite account + a Facebook Page + an ad account. We set all this up for you as part of the campaign setup. Takes 30 minutes."),
    ("What's the difference between 'boosting' and running Meta Ads?",
     "Boosting = \u20b9500 to show your post to your followers + their friends. Almost always a waste. Real Meta Ads = custom audience, custom creative, conversion objective, proper tracking, ongoing optimization. Vastly different results. We never boost \u2014 ever."),
    ("Can you do WhatsApp ads specifically?",
     "Yes \u2014 click-to-WhatsApp ads are some of our highest-converting campaigns. Average cost per qualified conversation: \u20b915-50. Perfect for lead gen, appointment booking, and direct sales.")
]
meta_ads_data.append(make_faq_section(meta_faq, "pbm_svc_faq_meta"))

# FINAL CTA
meta_ads_data.append(make_cta_section(
    heading="Ready to get real customers from Facebook + Instagram?",
    subheading="Book a free 30-minute call. We'll audit your current Meta presence, identify your best 3 target audiences, and send you a custom 90-day Meta Ads strategy. No commitment."
))

# Save
with open("C:/Users/kunal/pbm-launch-dashboard/meta-ads-final.json", "w") as f:
    json.dump(meta_ads_data, f, indent=2)
print(f"Meta Ads FINAL: {len(json.dumps(meta_ads_data))} bytes, {len(meta_ads_data)} sections")

print("Done")
