profile_code = """class AbhinavSunil:
    \"\"\"Full-Stack Engineer · AI Builder · Systems Architect · LPU B.Tech CSE 🇮🇳\"\"\"

    identity = {
        "role"       : "Full-Stack Engineer & AI Builder",
        "focus"      : "Distributed Systems · LLM Pipelines · Cloud Infrastructure",
        "shipping"   : [
            "AeroMind       →  5-svc distributed flight booking platform",
            "coderX         →  6-svc autonomous AI competitive programming judge",
            "KitchenELITE   →  RAG culinary AI + custom recommendation model",
            "MedVision AI   →  Two-stage clinical scan triage engine",
            "NimbusCodex    →  Ephemeral cloud IDE + Docker orchestration",
            "RateLimiter    →  Distributed token-bucket on Redis + Lua",
        ],
        "experience" : "Vodafone-Idea VOIS × AICTE — Data Analysis Intern",
        "certified"  : [
            "Oracle Cloud Infrastructure 2025 — Gen AI Professional  ✅",
            "Introduction to Machine Learning — NPTEL               ✅",
            "Introduction to Generative AI — Google                 ✅",
            "Introduction to C Programming — NPTEL                  ✅",
        ],
        "achievements": [
            "🏆 5th Place @ Code-A-Haunt 3.0 Hackathon, LPU (100+ teams)",
            "🧩 300+ LeetCode problems solved",
            "⭐ 5-Star HackerRank Python Rating",
        ],
    }

    stack = {
        "languages"  : ["CPP", "Python", "JavaScript", "SQL"],
        "backend"    : ["GoLang", "Node.js", "Express.js", "FastAPI", "Fastify"],
        "ai_ml"      : ["LangChain", "LangGraph", "PyTorch", "Groq", "HuggingFace"],
        "frontend"   : ["React.js", "Tailwind CSS", "Vite"],
        "databases"  : ["MongoDB", "Redis", "MySQL", "AstraDB"],
        "infra"      : ["Docker", "RabbitMQ", "BullMQ", "Prometheus", "Grafana", "Linux"],
    }

    def mantra(self) -> str:
        return "Ship fast. Build to scale. Let the systems do the talking. 🚀"
"""

template = """<svg width="1180" height="740" viewBox="0 0 1180 740" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}" stop-opacity="0.1"/>
      <stop offset="45%" stop-color="{accent_2}" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="{accent_2}" stop-opacity="0.8"/>
      <stop offset="55%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{accent_3}" stop-opacity="0.1"/>
      <animateTransform attributeName="gradientTransform" type="translate"
                          values="-1180 0; 1180 0; -1180 0" dur="5s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- VS Code Window -->
  <g transform="translate(60, 30)">
    <rect width="1060" height="680" rx="16" fill="{panel_fill}" opacity="0.9"/>
    <rect width="1060" height="680" rx="16" fill="none" stroke="{border_color}" stroke-width="1.5"/>
    <rect width="1060" height="680" rx="16" fill="none" stroke="url(#borderShimmer)" stroke-width="1.5"/>
    
    <!-- Titlebar -->
    <rect width="1060" height="40" rx="16" fill="{bg_color}" opacity="0.6"/>
    <rect y="24" width="1060" height="16" fill="{bg_color}" opacity="0.6"/>
    <circle cx="24" cy="20" r="6" fill="#FF5F56"/>
    <circle cx="44" cy="20" r="6" fill="#FFBD2E"/>
    <circle cx="64" cy="20" r="6" fill="#27C93F"/>
    <text x="530" y="25" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" fill="{text_secondary}">profile.py — IamAbhinav01</text>
    <line x1="0" y1="40" x2="1060" y2="40" stroke="{border_color}" stroke-width="1"/>

    <!-- Code Content -->
    <g transform="translate(30, 80)">
{code_lines}
    </g>
  </g>
</svg>"""

import html
def get_colored_code(lines, vars_dict):
    out = []
    y = 0
    for line in lines:
        if not line.strip():
            y += 22
            continue
        
        # Simple regex-based syntax highlighting approximation
        escaped = html.escape(line).replace(' ', '&nbsp;')
        # We will manually construct tspan elements
        # For simplicity, we just color by rudimentary rules in this script
        line_content = line
        
        tspan_str = ""
        in_string = False
        parts = line.split('"')
        
        if line.strip().startswith('class') or line.strip().startswith('def '):
            idx = line.find(' ')
            tspan_str += f'<tspan fill="{vars_dict["code_kw"]}">{html.escape(line[:idx])}</tspan>'
            tspan_str += f'<tspan fill="{vars_dict["code_fn"]}">{html.escape(line[idx:])}</tspan>'
        elif '"""' in line:
            tspan_str += f'<tspan fill="{vars_dict["code_str"]}">{html.escape(line)}</tspan>'
        else:
            for i, p in enumerate(parts):
                if i % 2 == 1: # inside string
                    tspan_str += f'<tspan fill="{vars_dict["code_str"]}">"{html.escape(p)}"</tspan>'
                else: # outside string
                    p_esc = html.escape(p)
                    # color keywords
                    for kw in ['return ', 'identity', 'stack', 'focus', 'role', 'shipping', 'experience', 'certified', 'achievements', 'languages', 'backend', 'ai_ml', 'frontend', 'databases', 'infra']:
                        p_esc = p_esc.replace(kw, f'</tspan><tspan fill="{vars_dict["code_kw"]}">{kw}</tspan><tspan fill="{vars_dict["text_primary"]}">')
                    tspan_str += f'<tspan fill="{vars_dict["text_primary"]}">{p_esc}</tspan>'

        # Fix spacing (SVG handles leading spaces poorly in tspan if not xml:space="preserve")
        # We use standard text element and absolute dy or we can use xml:space
        # Actually using xml:space="preserve" on the text element is easier
        out.append(f'<text x="0" y="{y}" font-family="\'SFMono-Regular\', Consolas, monospace" font-size="14.5" xml:space="preserve">{tspan_str}</text>')
        y += 22
    return "\n".join(out)

dark_vars = {
    "bg_color": "#030712",
    "panel_fill": "#0F172A",
    "border_color": "rgba(255,255,255,.08)",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "accent_1": "#7C3AED",
    "accent_2": "#22D3EE",
    "accent_3": "#10B981",
    "code_kw": "#C084FC",
    "code_fn": "#22D3EE",
    "code_str": "#34D399"
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
    "code_kw": "#4F46E5",
    "code_fn": "#06B6D4",
    "code_str": "#059669"
}

for mode, v in [("dark", dark_vars), ("light", light_vars)]:
    code_svg = get_colored_code(profile_code.split('\n'), v)
    with open(f"profile_{mode}.svg", "w", encoding="utf-8") as f:
        f.write(template.format(code_lines=code_svg, **v))
