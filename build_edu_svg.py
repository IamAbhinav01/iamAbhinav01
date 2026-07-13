template = """<svg width="1180" height="420" viewBox="0 0 1180 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgBase" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg_color}"/>
      <stop offset="100%" stop-color="{bg_color}"/>
    </linearGradient>

    <linearGradient id="traceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{accent_1}"/>
      <stop offset="50%" stop-color="{accent_2}"/>
      <stop offset="100%" stop-color="{accent_3}"/>
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <g transform="translate(60, 20)">
    
    <!-- Timeline Trace -->
    <path d="M 50 30 L 50 350" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
    <path d="M 50 30 L 50 350" fill="none" stroke="url(#traceGrad)" stroke-width="3" filter="url(#glow)">
        <animate attributeName="stroke-dasharray" values="0, 1000; 320, 1000" dur="2s" fill="freeze"/>
    </path>
    
    <!-- Ambient Data Packets traveling down the line -->
    <circle cx="50" cy="30" r="2.5" fill="#FFFFFF" filter="url(#glow)">
        <animate attributeName="cy" values="30; 350" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0; 1; 0" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="50" cy="30" r="2.5" fill="#FFFFFF" filter="url(#glow)">
        <animate attributeName="cy" values="30; 350" dur="2.5s" begin="1.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0; 1; 0" dur="2.5s" begin="1.5s" repeatCount="indefinite"/>
    </circle>

    <!-- Vodafone-Idea -->
    <g transform="translate(50, 40)">
      <circle cx="0" cy="20" r="8" fill="{panel_fill}" stroke="{accent_1}" stroke-width="3">
        <animate attributeName="r" values="8;10;8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <g transform="translate(40, 0)">
        <rect width="900" height="90" rx="12" fill="{panel_fill}" opacity="0.8"/>
        <rect width="900" height="90" rx="12" fill="none" stroke="{border_color}"/>
        <text x="24" y="32" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="{text_primary}">Vodafone-Idea VOIS × AICTE</text>
        <text x="876" y="30" text-anchor="end" font-family="-apple-system, sans-serif" font-size="14" fill="{text_secondary}">Oct 2023 – Nov 2023</text>
        <text x="24" y="58" font-family="-apple-system, sans-serif" font-size="16" fill="{accent_2}">Data Analysis Intern</text>
        <text x="24" y="78" font-family="-apple-system, sans-serif" font-size="14" fill="{text_secondary}">► Scalable NLP + CV inference pipelines via REST APIs · Async serving optimization</text>
      </g>
    </g>

    <!-- LPU -->
    <g transform="translate(50, 160)">
      <circle cx="0" cy="20" r="8" fill="{panel_fill}" stroke="{accent_2}" stroke-width="3">
        <animate attributeName="r" values="8;10;8" dur="2s" begin="0.6s" repeatCount="indefinite"/>
      </circle>
      <g transform="translate(40, 0)">
        <rect width="900" height="80" rx="12" fill="{panel_fill}" opacity="0.8"/>
        <rect width="900" height="80" rx="12" fill="none" stroke="{border_color}"/>
        <text x="24" y="32" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="{text_primary}">Lovely Professional University</text>
        <text x="876" y="30" text-anchor="end" font-family="-apple-system, sans-serif" font-size="14" fill="{text_secondary}">Aug 2023 – Present</text>
        <text x="24" y="58" font-family="-apple-system, sans-serif" font-size="16" fill="{accent_2}">B.Tech — Computer Science &amp; Engineering</text>
        <text x="876" y="58" text-anchor="end" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="{accent_3}">CGPA: 8.00</text>
      </g>
    </g>
    
    <!-- Amrita -->
    <g transform="translate(50, 270)">
      <circle cx="0" cy="20" r="8" fill="{panel_fill}" stroke="{accent_3}" stroke-width="3">
        <animate attributeName="r" values="8;10;8" dur="2s" begin="1.2s" repeatCount="indefinite"/>
      </circle>
      <g transform="translate(40, 0)">
        <rect width="900" height="80" rx="12" fill="{panel_fill}" opacity="0.8"/>
        <rect width="900" height="80" rx="12" fill="none" stroke="{border_color}"/>
        <text x="24" y="32" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="{text_primary}">Amrita Vidyalayam</text>
        <text x="876" y="30" text-anchor="end" font-family="-apple-system, sans-serif" font-size="14" fill="{text_secondary}">May 2022 – May 2023</text>
        <text x="24" y="58" font-family="-apple-system, sans-serif" font-size="16" fill="{accent_2}">Intermediate (PCMB)</text>
        <text x="876" y="58" text-anchor="end" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="{accent_3}">Score: 86.6%</text>
      </g>
    </g>

  </g>
</svg>"""

dark_vars = {
    "bg_color": "#030712",
    "panel_fill": "#0F172A",
    "border_color": "rgba(255,255,255,.08)",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "accent_1": "#7C3AED",
    "accent_2": "#22D3EE",
    "accent_3": "#10B981",
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
}

with open("edu_dark.svg", "w", encoding="utf-8") as f:
    f.write(template.format(**dark_vars))

with open("edu_light.svg", "w", encoding="utf-8") as f:
    f.write(template.format(**light_vars))
