import json

projects = [
    {"title": "AeroMind", "icon": "🛫", "desc": "5 svc · pessimistic locks · idempotency · RabbitMQ", "link": "https://github.com/IamAbhinav01/AeroMind-Distributed-Flight-Reservation-System"},
    {"title": "coderX", "icon": "🤖", "desc": "6 svc · LLM judge · Dockerode sandbox · BullMQ", "link": "https://github.com/IamAbhinav01/coderX"},
    {"title": "RateLimiter", "icon": "🚦", "desc": "token bucket · atomic Lua scripts · zero races", "link": "https://github.com/IamAbhinav01/RateLimiter"},
    {"title": "NimbusCodex", "icon": "☁️", "desc": "pre-warmed pools · WebSocket exec · cgroup isolation", "link": "https://github.com/IamAbhinav01/NimbusCodex"},
    {"title": "KitchenELITE", "icon": "🍳", "desc": "RAG · FAISS · 500K recipes · HF Spaces deploy", "link": "https://github.com/IamAbhinav01/KITCHENELITEAI----cullinary-expertise"},
    {"title": "MedVision AI", "icon": "🏥", "desc": "EfficientNet-B4→B3 cascade · async FastAPI inference", "link": "https://github.com/IamAbhinav01/Med_Vision"}
]

template = """<svg width="1180" height="380" viewBox="0 0 1180 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgBase" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg_color}"/>
      <stop offset="100%" stop-color="{bg_color}"/>
    </linearGradient>

    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}" stop-opacity="0.1"/>
      <stop offset="45%" stop-color="{accent_2}" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="{accent_2}" stop-opacity="0.8"/>
      <stop offset="55%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <animateTransform attributeName="gradientTransform" type="translate"
                          values="-1180 0; 1180 0; -1180 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    
    <linearGradient id="glassSheen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{sheen_color}" stop-opacity="0.10"/>
      <stop offset="18%" stop-color="{sheen_color}" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="{sheen_color}" stop-opacity="0"/>
    </linearGradient>
    
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1180" height="380" fill="{bg_color}" rx="20"/>

  <g transform="translate(40, 40)">
{cards}
  </g>
</svg>"""

card_template = """
    <!-- Card {i} -->
    <a href="{link}" target="_blank">
      <g transform="translate({x}, {y})">
        <rect width="340" height="130" rx="16" fill="{panel_fill}" fill-opacity="0.8"/>
        <rect width="340" height="130" rx="16" fill="url(#glassSheen)"/>
        <rect width="340" height="130" rx="16" fill="none" stroke="{border_color}" stroke-width="1.5"/>
        <rect width="340" height="130" rx="16" fill="none" stroke="url(#borderShimmer)" stroke-width="2">
          <animate attributeName="opacity" values="0.3;1;0.3" dur="{dur}s" repeatCount="indefinite"/>
        </rect>
        
        <!-- Icon -->
        <text x="20" y="45" font-size="28">{icon}</text>
        
        <!-- Title -->
        <text x="65" y="42" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="{text_primary}">{title}</text>
        
        <!-- Desc -->
        <text x="20" y="70" font-family="-apple-system, sans-serif" font-size="13.5" fill="{text_secondary}">
            <tspan x="20" dy="0">{desc_1}</tspan>
            <tspan x="20" dy="18">{desc_2}</tspan>
            <tspan x="20" dy="18">{desc_3}</tspan>
        </text>
      </g>
    </a>
"""

def generate_projects(vars_dict):
    cards_str = ""
    for i, p in enumerate(projects):
        col = i % 3
        row = i // 3
        x = col * (340 + 40)
        y = row * (130 + 40)
        dur = 4 + (i * 0.5)
        # wrap text roughly for desc
        words = p['desc'].split(' · ')
        desc_1 = ' · '.join(words[:2]) if len(words) > 1 else words[0]
        desc_2 = ' · '.join(words[2:4]) if len(words) > 3 else (' · '.join(words[2:]) if len(words) > 2 else '')
        desc_3 = ' · '.join(words[4:]) if len(words) > 4 else ''
        
        cards_str += card_template.format(
            i=i, x=x, y=y, dur=dur,
            title=p['title'], icon=p['icon'], desc_1=desc_1, desc_2=desc_2, desc_3=desc_3, link=p['link'],
            **vars_dict
        )
    return template.format(cards=cards_str, **vars_dict)

dark_vars = {
    "bg_color": "#030712",
    "panel_fill": "#0F172A",
    "border_color": "rgba(255,255,255,.08)",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "accent_1": "#7C3AED",
    "accent_2": "#22D3EE",
    "accent_3": "#10B981",
    "sheen_color": "#FFFFFF"
}

light_vars = {
    "bg_color": "#FFFFFF",
    "panel_fill": "#F8FAFC",
    "border_color": "rgba(15,23,42,.08)",
    "text_primary": "#0F172A",
    "text_secondary": "#475569",
    "accent_1": "#2563EB",
    "accent_2": "#06B6D4",
    "accent_3": "#10B981",
    "sheen_color": "#000000"
}

with open("projects_dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_projects(dark_vars))

with open("projects_light.svg", "w", encoding="utf-8") as f:
    f.write(generate_projects(light_vars))
