template = """<svg width="1180" height="80" viewBox="0 0 1180 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgBase" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg_color}"/>
      <stop offset="100%" stop-color="{bg_color}"/>
    </linearGradient>

    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}" stop-opacity="0.15"/>
      <stop offset="30%" stop-color="{accent_2}" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="{bg_color}" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}"/>
      <stop offset="50%" stop-color="{accent_2}"/>
      <stop offset="100%" stop-color="{accent_3}"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-1180 0; 1180 0; -1180 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <g transform="translate(60, 10)">
    <!-- Glass panel -->
    <rect width="1060" height="60" rx="12" fill="{panel_fill}" opacity="0.6"/>
    <rect width="1060" height="60" rx="12" fill="url(#barGrad)"/>
    
    <!-- Glowing Left Accent -->
    <rect x="0" y="0" width="6" height="60" rx="3" fill="url(#lineGrad)" filter="url(#glow)"/>
    
    <!-- Title Text -->
    <text x="30" y="38" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" letter-spacing="2" fill="{text_primary}">{title}</text>
    
    <!-- Subtle tech decoration -->
    <circle cx="1020" cy="30" r="3" fill="{accent_2}" opacity="0.5">
        <animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1035" cy="30" r="3" fill="{accent_3}" opacity="0.5">
        <animate attributeName="opacity" values="0.2;1;0.2" dur="2s" begin="0.5s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>"""

headers = [
    ("01", "SYSTEM PROFILE"),
    ("02", "TECH ARSENAL"),
    ("03", "FEATURED PROJECTS"),
    ("04", "NEURAL ACTIVITY METRICS"),
    ("05", "ACHIEVEMENT NODES"),
    ("06", "EXPERIENCE & EDUCATION"),
    ("07", "CONTRIBUTION SERPENTINE"),
    ("08", "ESTABLISH CONNECTION")
]

dark_vars = {
    "bg_color": "#030712",
    "panel_fill": "#0F172A",
    "text_primary": "#F8FAFC",
    "accent_1": "#7C3AED",
    "accent_2": "#22D3EE",
    "accent_3": "#10B981",
}

light_vars = {
    "bg_color": "#FFFFFF",
    "panel_fill": "#F8FAFC",
    "text_primary": "#0F172A",
    "accent_1": "#2563EB",
    "accent_2": "#06B6D4",
    "accent_3": "#10B981",
}

for i, title in headers:
    full_title = f"{i} — {title}"
    for mode, vars_dict in [("dark", dark_vars), ("light", light_vars)]:
        with open(f"header_{i}_{mode}.svg", "w", encoding="utf-8") as f:
            f.write(template.format(title=full_title, **vars_dict))
