#!/usr/bin/env python3
"""Build 3 complete customized Elementor data sets for the 3 PBM service pages."""
import json
import sys

def make_industries_section(industries_data, section_id="pbm_svc_industries"):
    """industries_data = list of 4 tuples (icon, name, description)"""
    cols = []
    for i, (icon, name, desc) in enumerate(industries_data):
        cols.append({
            "id": f"pbm_svc_industries_{i+1}",
            "elType": "section",
            "settings": {"_inline_size": {"unit": "%", "size": 25}},
            "elements": [{
                "id": f"pbm_svc_industries_{i+1}_widget",
                "elType": "widget",
                "settings": {
                    "selected_icon": {"value": icon, "library": "fa-solid"},
                    "title_text": name,
                    "description_text": desc,
                    "icon_color": "custom", "icon_color_custom": "#004CB1",
                    "title_color": "#1A1A1A", "description_color": "#666666",
                    "align": "left"
                },
                "elements": [],
                "widgetType": "icon-box"
            }]
        })
    return {
        "id": section_id,
        "elType": "section",
        "settings": {
            "_title": "Industries We Serve",
            "content_width": {"unit": "px", "size": 1200},
            "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
            "background_background": "classic",
            "background_color": "#F7F8FA"
        },
        "elements": [
            {
                "id": section_id + "_heading",
                "elType": "widget",
                "settings": {
                    "title": "Industries we serve best in Tricity",
                    "header_size": "h2",
                    "align": "center",
                    "title_color": "#1A1A1A",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 36},
                    "typography_font_weight": "700"
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": section_id + "_row",
                "elType": "column",
                "settings": {
                    "content_width": {"unit": "%", "size": 100},
                    "_margin": {"unit": "px", "top": "40", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
                },
                "elements": cols
            }
        ]
    }


def make_pricing_section(pricing_data, section_id="pbm_svc_pricing"):
    """pricing_data = list of 3 dicts: {title, desc, price, features, popular, button_text}"""
    cols = []
    for i, p in enumerate(pricing_data):
        settings = {
            "title_text": p["title"],
            "description_text": p["desc"],
            "price": p["price"],
            "period": p.get("period", "/month"),
            "features_list": p["features"],
            "button_text": p.get("button_text", "Get started"),
            "button_link": {"url": "/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""},
            "title_color": "#1A1A1A",
            "description_color": "#666666",
            "price_color": "#004CB1",
            "period_color": "#666666",
            "features_title_color": "#1A1A1A",
            "features_text_color": "#444444",
            "ribbon_title": "POPULAR" if p.get("popular") else "",
            "ribbon_background_color": "#FFB800",
            "ribbon_text_color": "#1A1A1A",
            "background_background": "classic",
            "background_color": "#EFF5FF" if p.get("popular") else "#F7F8FA",
            "button_background_color": "#004CB1",
            "button_text_color": "#FFFFFF",
            "button_hover_color": "#003380",
            "highlight": "yes" if p.get("popular") else None
        }
        if not p.get("popular"):
            del settings["ribbon_background_color"]
            del settings["ribbon_text_color"]
            del settings["highlight"]
        cols.append({
            "id": f"pbm_svc_pricing_{i+1}",
            "elType": "section",
            "settings": {"_inline_size": {"unit": "%", "size": 33}},
            "elements": [{
                "id": f"pbm_svc_pricing_{i+1}_widget",
                "elType": "widget",
                "settings": settings,
                "elements": [],
                "widgetType": "price-table"
            }]
        })
    return {
        "id": section_id,
        "elType": "section",
        "settings": {
            "_title": "Pricing Tiers",
            "content_width": {"unit": "px", "size": 1200},
            "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
            "background_background": "classic",
            "background_color": "#FFFFFF"
        },
        "elements": [
            {
                "id": section_id + "_heading",
                "elType": "widget",
                "settings": {
                    "title": "Pricing",
                    "header_size": "h2",
                    "align": "center",
                    "title_color": "#1A1A1A",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 36},
                    "typography_font_weight": "700"
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": section_id + "_subheading",
                "elType": "widget",
                "settings": {
                    "editor": "<p style=\"text-align: center;\">No long-term contracts. Pay monthly. Cancel anytime.</p>",
                    "text_color": "#666666",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 16},
                    "_margin": {"unit": "px", "top": "10", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
                },
                "elements": [],
                "widgetType": "text-editor"
            },
            {
                "id": section_id + "_row",
                "elType": "column",
                "settings": {"content_width": {"unit": "%", "size": 100}},
                "elements": cols
            }
        ]
    }


def make_faq_section(faq_data, section_id="pbm_svc_faq"):
    """faq_data = list of 5 tuples (question, answer)"""
    tabs = []
    for i, (q, a) in enumerate(faq_data):
        tabs.append({
            "tab_title": q,
            "tab_content": a,
            "element_id": f"faq{i+1}"
        })
    return {
        "id": section_id,
        "elType": "section",
        "settings": {
            "_title": "FAQ",
            "content_width": {"unit": "px", "size": 1000},
            "padding": {"unit": "px", "top": "80", "right": "30", "bottom": "80", "left": "30", "isLinked": False},
            "background_background": "classic",
            "background_color": "#F7F8FA"
        },
        "elements": [
            {
                "id": section_id + "_heading",
                "elType": "widget",
                "settings": {
                    "title": "Frequently asked questions",
                    "header_size": "h2",
                    "align": "center",
                    "title_color": "#1A1A1A",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 36},
                    "typography_font_weight": "700"
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": section_id + "_accordion",
                "elType": "widget",
                "settings": {
                    "tabs": tabs,
                    "faq_schema": "yes",
                    "title_color": "#1A1A1A",
                    "content_color": "#444444",
                    "active_item_color": "#004CB1",
                    "border_color": "#E0E0E0"
                },
                "elements": [],
                "widgetType": "accordion"
            }
        ]
    }


def make_cta_section(section_id="pbm_svc_cta", heading="Ready to get started?",
                       subheading="Book a free 15-minute call. No commitment. Get a custom local SEO strategy for your Tricity business."):
    return {
        "id": section_id,
        "elType": "section",
        "settings": {
            "_title": "Final CTA",
            "content_width": {"unit": "px", "size": 1200},
            "padding": {"unit": "px", "top": "100", "right": "30", "bottom": "100", "left": "30", "isLinked": False},
            "background_background": "gradient",
            "background_color": "#004CB1",
            "background_color_b": "#003380",
            "background_gradient_angle": {"unit": "deg", "size": 135}
        },
        "elements": [
            {
                "id": section_id + "_heading",
                "elType": "widget",
                "settings": {
                    "title": heading,
                    "header_size": "h2",
                    "align": "center",
                    "title_color": "#FFFFFF",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 40},
                    "typography_font_weight": "700"
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": section_id + "_subheading",
                "elType": "widget",
                "settings": {
                    "editor": f"<p style=\"text-align: center;\">{subheading}</p>",
                    "text_color": "#FFFFFF",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 17},
                    "_margin": {"unit": "px", "top": "15", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                },
                "elements": [],
                "widgetType": "text-editor"
            },
            {
                "id": section_id + "_button",
                "elType": "widget",
                "settings": {
                    "text": "Get a free strategy",
                    "selected_icon": {"value": "fas fa-arrow-right", "library": "fa-solid"},
                    "icon_align": "right",
                    "icon_indent": {"unit": "px", "size": 12},
                    "background_color": "#FFFFFF",
                    "button_text_color": "#004CB1",
                    "hover_color": "#FFFFFF",
                    "button_background_hover_color": "#FFB800",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 18},
                    "typography_font_weight": "600",
                    "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                    "text_padding": {"unit": "px", "top": "18", "right": "36", "bottom": "18", "left": "36", "isLinked": False},
                    "align": "center",
                    "link": {"url": "/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""}
                },
                "elements": [],
                "widgetType": "button"
            }
        ]
    }


# ============================================
# LOCAL SEO COMPLETE DATA
# ============================================
local_seo_complete = json.load(open("C:/Users/kunal/pbm-launch-dashboard/local-seo-elementor.json"))

# Add industries
local_seo_industries = [
    ("fas fa-stethoscope", "Doctors + Clinics",
     "Patient volume growth of 30-180% in 90 days. Compliance with Google Healthcare guidelines included."),
    ("fas fa-utensils", "Restaurants + Cafes",
     "40-200% increase in 'request directions' clicks. Menu schema + photo optimization + review velocity."),
    ("fas fa-cut", "Salons + Spas",
     "2-4x more phone calls and bookings. Service-specific landing pages and Google Posts for offers."),
    ("fas fa-dumbbell", "Gyms + Fitness Studios",
     "50-150% more trial sign-ups. Class schedule schema + photo optimization + local event coverage."),
]
local_seo_complete.append(make_industries_section(local_seo_industries, "pbm_svc_industries_local"))

# Add pricing (Local SEO at ₹30,000/month)
local_seo_pricing = [
    {
        "title": "Starter",
        "desc": "Single location",
        "price": "₹30,000",
        "period": "/month",
        "features": [
            "Google Business Profile optimization",
            "15 directory citations",
            "5 SEO-optimized service pages",
            "2-4 new reviews/month",
            "Monthly ranking report"
        ]
    },
    {
        "title": "Growth",
        "desc": "Most popular",
        "price": "₹45,000",
        "period": "/month",
        "popular": True,
        "features": [
            "Everything in Starter",
            "30 directory citations",
            "10 SEO-optimized service pages",
            "4-6 new reviews/month",
            "Local link building (2 links/month)",
            "2 blog posts/month"
        ]
    },
    {
        "title": "Pro",
        "desc": "Multi-location",
        "price": "₹75,000",
        "period": "/month",
        "features": [
            "Everything in Growth",
            "Unlimited directory citations",
            "Unlimited SEO pages",
            "6-10 new reviews/month per location",
            "Local link building (4+ links/month)",
            "4 blog posts/month",
            "Multi-location management"
        ]
    }
]
local_seo_complete.append(make_pricing_section(local_seo_pricing, "pbm_svc_pricing_local"))

# Add FAQ (service-specific for Local SEO)
local_seo_faq = [
    ("How long until I see results in the 3-pack?",
     "60-120 days for non-competitive niches (doctors, salons, restaurants, gyms). 120-180 days for competitive niches (lawyers, real estate, schools). You'll see GBP insights (calls, profile views) within 2-4 weeks of starting."),
    ("Do I keep my Google Business Profile if I stop working with you?",
     "Yes. Your Google Business Profile is yours, always \u2014 we never take ownership or lock you out. All GBP access, login credentials, and historical data remain with you regardless of your relationship with us."),
    ("What if I have multiple locations?",
     "We manage all your locations from a single dashboard. Each location gets its own GBP, citation set, and review system. Pricing scales with locations, not linearly \u2014 we offer 20-30% volume discount for multi-location businesses."),
    ("Can I do this myself?",
     "You can. Local SEO is 40-80 hours of work per month, ongoing \u2014 citations, reviews, content, links, GBP posts. Most business owners hire us because their time is better spent on their business. We'll happily share our checklist if you want to try."),
    ("What industries do you specialize in?",
     "Local service businesses: doctors, dentists, restaurants, salons, spas, gyms, lawyers, real estate agents, schools, accountants, and home services (plumbers, electricians, contractors). If you serve a local area and depend on local search, we're a great fit.")
]
local_seo_complete.append(make_faq_section(local_seo_faq, "pbm_svc_faq_local"))

# Add final CTA
local_seo_complete.append(make_cta_section(
    heading="Ready to dominate Chandigarh's local search?",
    subheading="Book a free 15-minute call. We'll audit your current GBP, citations, and 3-pack ranking, then send you a custom 90-day plan. No commitment."
))

# Save
with open("C:/Users/kunal/pbm-launch-dashboard/local-seo-final.json", "w") as f:
    json.dump(local_seo_complete, f, indent=2)
print(f"Local SEO FINAL: {len(json.dumps(local_seo_complete))} bytes, {len(local_seo_complete)} sections")

print("Done")
