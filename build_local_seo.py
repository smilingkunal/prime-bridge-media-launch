#!/usr/bin/env python3
"""
Build 3 customized Elementor data sets for the 3 PBM service pages.
Each page uses the same template structure but with service-specific:
- Hero H1 + subhead
- Intro text
- 3 stats
- 5-step process
- 4 industries
- 3 pricing tiers
- 5 FAQ questions
- CTA copy
"""

import json
import sys

# ============================================
# SERVICE 1: LOCAL SEO
# ============================================
local_seo_data = [
    # HERO
    {
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
                    "title": "Local SEO Services in Chandigarh-Tricity",
                    "header_size": "h1",
                    "align": "center",
                    "title_color": "#FFFFFF",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 48},
                    "typography_font_weight": "700",
                    "typography_line_height": {"unit": "em", "size": 1.2}
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": "pbm_svc_hero_subheading",
                "elType": "widget",
                "settings": {
                    "editor": "<p>Get your business on Google Maps 3-pack. Show up in 'near me' searches. Get calls from real customers in your area \u2014 not tyre-kickers from across the country.</p>",
                    "align": "center",
                    "text_color": "#FFFFFF",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 18},
                    "typography_font_weight": "400",
                    "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                },
                "elements": [],
                "widgetType": "text-editor"
            },
            {
                "id": "pbm_svc_hero_cta",
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
                    "typography_font_size": {"unit": "px", "size": 16},
                    "typography_font_weight": "600",
                    "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                    "text_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
                    "align": "center",
                    "link": {"url": "/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""}
                },
                "elements": [],
                "widgetType": "button"
            }
        ]
    },
    # INTRO
    {
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
                    "title": "What is local SEO \u2014 and why Tricity businesses need it",
                    "header_size": "h2",
                    "align": "left",
                    "title_color": "#1A1A1A",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 36},
                    "typography_font_weight": "700"
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": "pbm_svc_intro_text",
                "elType": "widget",
                "settings": {
                    "editor": "<p>Local SEO is the process of making your business show up when someone in your area searches for the services or products you sell. When a person in Chandigarh searches 'dentist near me' or 'best restaurant in Mohali' or 'gym in Panchkula', Google's local 3-pack shows three businesses at the top of the search results. <strong>Local SEO gets you into that 3-pack.</strong></p><p>The 3-pack is the most valuable real estate in search. It sits above every organic result, shows your business name + rating + hours + tap-to-call, and the businesses that win it get <strong>44% of all clicks</strong> on local search. If you're a Tricity business and you're not in the 3-pack for your core search terms, your competitors are \u2014 and they're getting your customers.</p>",
                    "text_color": "#444444",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 17},
                    "typography_line_height": {"unit": "em", "size": 1.7},
                    "_margin": {"unit": "px", "top": "20", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
                },
                "elements": [],
                "widgetType": "text-editor"
            }
        ]
    },
    # STATS
    {
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
                    {
                        "id": "pbm_svc_stats_1",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [
                            {
                                "id": "pbm_svc_stats_1_widget",
                                "elType": "widget",
                                "settings": {
                                    "title_text": "44%",
                                    "description_text": "of all clicks on local search go to the 3-pack",
                                    "title_color": "#004CB1",
                                    "description_color": "#666666",
                                    "title_typography_typography": "custom",
                                    "title_typography_font_size": {"unit": "px", "size": 48},
                                    "title_typography_font_weight": "700",
                                    "align": "center"
                                },
                                "elements": [],
                                "widgetType": "counter"
                            }
                        ]
                    },
                    {
                        "id": "pbm_svc_stats_2",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [
                            {
                                "id": "pbm_svc_stats_2_widget",
                                "elType": "widget",
                                "settings": {
                                    "title_text": "3 mo",
                                    "description_text": "average time to first 3-pack ranking for our clients",
                                    "title_color": "#004CB1",
                                    "description_color": "#666666",
                                    "title_typography_typography": "custom",
                                    "title_typography_font_size": {"unit": "px", "size": 48},
                                    "title_typography_font_weight": "700",
                                    "align": "center"
                                },
                                "elements": [],
                                "widgetType": "counter"
                            }
                        ]
                    },
                    {
                        "id": "pbm_svc_stats_3",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [
                            {
                                "id": "pbm_svc_stats_3_widget",
                                "elType": "widget",
                                "settings": {
                                    "title_text": "2.4K",
                                    "description_text": "monthly searches for 'digital marketing agency in chandigarh'",
                                    "title_color": "#004CB1",
                                    "description_color": "#666666",
                                    "title_typography_typography": "custom",
                                    "title_typography_font_size": {"unit": "px", "size": 48},
                                    "title_typography_font_weight": "700",
                                    "align": "center"
                                },
                                "elements": [],
                                "widgetType": "counter"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    # PROCESS (5 steps for local SEO)
    {
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
            {
                "id": "pbm_svc_process_heading",
                "elType": "widget",
                "settings": {
                    "title": "Our 6-part local SEO system",
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
                "id": "pbm_svc_process_subheading",
                "elType": "widget",
                "settings": {
                    "editor": "<p style=\"text-align: center;\">Six pillars of local SEO we execute every month to get you ranking in the Google Maps 3-pack</p>",
                    "text_color": "#666666",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": 17},
                    "_margin": {"unit": "px", "top": "10", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
                },
                "elements": [],
                "widgetType": "text-editor"
            },
            {
                "id": "pbm_svc_process_row1",
                "elType": "column",
                "settings": {"content_width": {"unit": "%", "size": 100}},
                "elements": [
                    {
                        "id": "pbm_svc_process_1",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_1_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-1", "library": "fa-solid"},
                            "title_text": "Google Business Profile optimization",
                            "description_text": "The #1 ranking factor. We optimize every field, post weekly updates, and manage Q&A + photo uploads.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    },
                    {
                        "id": "pbm_svc_process_2",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_2_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-2", "library": "fa-solid"},
                            "title_text": "Citation building + NAP consistency",
                            "description_text": "We submit to 30+ Indian directories (Justdial, IndiaMART, Sulekha) and ensure NAP is 100% consistent.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    },
                    {
                        "id": "pbm_svc_process_3",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_3_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-3", "library": "fa-solid"},
                            "title_text": "On-page local SEO",
                            "description_text": "Title tags, meta descriptions, schema markup, internal linking \u2014 all optimized for city + service combinations.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    }
                ]
            },
            {
                "id": "pbm_svc_process_row2",
                "elType": "column",
                "settings": {"content_width": {"unit": "%", "size": 100}, "_margin": {"unit": "px", "top": "30", "right": "0", "bottom": "0", "left": "0", "isLinked": False}},
                "elements": [
                    {
                        "id": "pbm_svc_process_4",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_4_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-4", "library": "fa-solid"},
                            "title_text": "Review velocity + reputation",
                            "description_text": "SMS/email automations to get 2-4 reviews/month, respond within 24h, and dispute fake reviews.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    },
                    {
                        "id": "pbm_svc_process_5",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_5_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-5", "library": "fa-solid"},
                            "title_text": "Local link building",
                            "description_text": "Digital PR placements in Chandigarh Tribune, Tricity News, Chamber of Commerce, and local event sponsorships.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    },
                    {
                        "id": "pbm_svc_process_6",
                        "elType": "section",
                        "settings": {"_inline_size": {"unit": "%", "size": 33}},
                        "elements": [{"id": "pbm_svc_process_6_widget", "elType": "widget", "settings": {
                            "selected_icon": {"value": "fas fa-6", "library": "fa-solid"},
                            "title_text": "Local content + 3-pack domination",
                            "description_text": "City-specific service pages + 'near me' content + neighborhood landing pages \u2014 we own the 3-pack for every relevant search.",
                            "icon_color": "custom", "icon_color_custom": "#004CB1",
                            "title_color": "#1A1A1A", "description_color": "#666666"
                        }, "elements": [], "widgetType": "icon-box"}]
                    }
                ]
            }
        ]
    }
]

# Write the Local SEO data
with open("C:/Users/kunal/pbm-launch-dashboard/local-seo-elementor.json", "w") as f:
    json.dump(local_seo_data, f, indent=2)
print(f"Local SEO data: {len(json.dumps(local_seo_data))} bytes, {len(local_seo_data)} sections")
