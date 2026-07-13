template = """<svg width="1180" height="340" viewBox="0 0 1180 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgBase" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg_color}"/>
      <stop offset="100%" stop-color="{bg_color}"/>
    </linearGradient>

    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}" stop-opacity="0.1"/>
      <stop offset="45%" stop-color="{accent_2}" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="{accent_2}" stop-opacity="0.9"/>
      <stop offset="55%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <animateTransform attributeName="gradientTransform" type="translate"
                          values="-1180 0; 1180 0; -1180 0" dur="5s" repeatCount="indefinite"/>
    </linearGradient>
    
    <linearGradient id="pillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_1}"/>
      <stop offset="100%" stop-color="{accent_3}"/>
    </linearGradient>
    
    <filter id="pillGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="marqueeClip">
      <rect x="0" y="0" width="1060" height="300" rx="16"/>
    </clipPath>
  </defs>

  <g transform="translate(60, 20)">
    <!-- Container -->
    <rect width="1060" height="300" rx="16" fill="{panel_fill}" opacity="0.8"/>
    <rect width="1060" height="300" rx="16" fill="none" stroke="{border_color}" stroke-width="1.5"/>
    <rect width="1060" height="300" rx="16" fill="none" stroke="url(#borderShimmer)" stroke-width="1.5"/>

    <g clip-path="url(#marqueeClip)">
{tracks}
    </g>
    
    <!-- Fades -->
    <rect x="0" y="0" width="100" height="300" fill="url(#leftFade)" rx="16"/>
    <rect x="960" y="0" width="100" height="300" fill="url(#rightFade)" rx="16"/>
  </g>
  
  <defs>
    <linearGradient id="leftFade" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="{panel_fill}" stop-opacity="1"/>
        <stop offset="100%" stop-color="{panel_fill}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="rightFade" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="{panel_fill}" stop-opacity="0"/>
        <stop offset="100%" stop-color="{panel_fill}" stop-opacity="1"/>
    </linearGradient>
  </defs>
</svg>"""

pill_template = """
        <g transform="translate({x}, 0)">
          <rect width="{w}" height="44" rx="22" fill="{pill_bg}" stroke="url(#pillGrad)" stroke-width="1" stroke-opacity="0.5" filter="url(#pillGlow)"/>
          <text x="{mid}" y="28" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="16" font-weight="600" fill="{text_primary}">{name}</text>
        </g>"""

row_1 = ["GoLang", "Python", "TypeScript", "JavaScript", "Java", "Kotlin", "SQL", "React.js", "Tailwind CSS", "Vite", "Prometheus", "Grafana", "Linux", "GitHub Actions"]
row_2 = ["LangChain", "LangGraph", "PyTorch", "TensorFlow", "Groq", "FAISS", "Scikit-learn", "OpenAI", "Ollama", "HuggingFace"]
row_3 = ["Node.js", "FastAPI", "Express.js", "Fastify", "WebSockets", "RabbitMQ", "PostgreSQL", "Redis", "MongoDB", "Docker", "BullMQ", "AstraDB"]

def generate_track(items, y_pos, direction_left=True, vars_dict=None):
    pill_group = ""
    current_x = 0
    # build a single continuous row
    for item in items:
        w = len(item) * 11 + 40
        pill_group += pill_template.format(x=current_x, w=w, mid=w/2, name=item, **vars_dict)
        current_x += w + 20
    
    total_width = current_x
    
    # We duplicate it 3 times to make infinite scrolling seamless
    full_row = f"<g>{pill_group}</g>"
    full_row += f"<g transform='translate({total_width}, 0)'>{pill_group}</g>"
    full_row += f"<g transform='translate({total_width*2}, 0)'>{pill_group}</g>"
    
    # SVG animateTransform
    if direction_left:
        # Move left
        anim = f'<animateTransform attributeName="transform" type="translate" from="0,{y_pos}" to="-{total_width},{y_pos}" dur="{total_width/50}s" repeatCount="indefinite"/>'
    else:
        # Move right
        anim = f'<animateTransform attributeName="transform" type="translate" from="-{total_width},{y_pos}" to="0,{y_pos}" dur="{total_width/50}s" repeatCount="indefinite"/>'
        
    return f"""
      <g>
        {anim}
        {full_row}
      </g>
    """

def generate_arsenal(vars_dict):
    tracks = ""
    tracks += generate_track(row_1, 50, direction_left=True, vars_dict=vars_dict)
    tracks += generate_track(row_2, 120, direction_left=False, vars_dict=vars_dict)
    tracks += generate_track(row_3, 190, direction_left=True, vars_dict=vars_dict)
    
    return template.format(tracks=tracks, **vars_dict)


dark_vars = {
    "bg_color": "#030712",
    "panel_fill": "#0F172A",
    "border_color": "rgba(255,255,255,.08)",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "accent_1": "#7C3AED",
    "accent_2": "#22D3EE",
    "accent_3": "#10B981",
    "pill_bg": "#0B1220"
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
    "pill_bg": "#FFFFFF"
}

with open("arsenal_dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_arsenal(dark_vars))

with open("arsenal_light.svg", "w", encoding="utf-8") as f:
    f.write(generate_arsenal(light_vars))
