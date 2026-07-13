import re

dark_template = """<svg width="1180" height="610" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Developer profile hero banner">
  <defs>
    <clipPath id="cardClip">
      <rect x="0" y="0" width="1180" height="610" rx="28"/>
    </clipPath>

    <linearGradient id="bgBase" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg_color}"/>
      <stop offset="100%" stop-color="{bg_color}"/>
    </linearGradient>

    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}"/>
      <stop offset="50%" stop-color="{accent_2}"/>
      <stop offset="100%" stop-color="{accent_3}"/>
      <animate attributeName="x1" values="-20%;120%;-20%" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="80%;220%;80%" dur="7s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ascii_1}"/>
      <stop offset="100%" stop-color="{ascii_2}"/>
      <animate attributeName="x1" values="-30%;130%;-30%" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="70%;230%;70%" dur="5s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_1}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{accent_2}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{accent_2}" stop-opacity="0.9"/>
      <stop offset="55%" stop-color="{accent_3}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{accent_3}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
                          values="-1180 0; 1180 0; -1180 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>

    <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{glow_1}" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="{glow_1}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{glow_2}" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="{glow_2}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{glow_3}" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="{glow_3}" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="glassSheen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{sheen_color}" stop-opacity="0.10"/>
      <stop offset="18%" stop-color="{sheen_color}" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="{sheen_color}" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="pillGlow" x="-40%" y="-100%" width="180%" height="300%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="iconGlow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softBlur" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="40"/>
    </filter>

    <filter id="noiseFilter">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/>
      <feColorMatrix in="n" type="matrix"
        values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.4 0"/>
    </filter>

      <clipPath id="clipRole_0">
        <rect x="0" y="0" height="29">
          <animate attributeName="width" dur="12.0s" repeatCount="indefinite"
                   keyTimes="0.00000;0.08000;0.16000;0.20000;1.00000" values="0.00;224.20;224.20;0.00;0.00" calcMode="linear"/>
        </rect>
      </clipPath>

      <clipPath id="clipRole_1">
        <rect x="0" y="0" height="29">
          <animate attributeName="width" dur="12.0s" repeatCount="indefinite"
                   keyTimes="0.00000;0.20000;0.28000;0.36000;0.40000;1.00000" values="0.00;0.00;200.60;200.60;0.00;0.00" calcMode="linear"/>
        </rect>
      </clipPath>

      <clipPath id="clipRole_2">
        <rect x="0" y="0" height="29">
          <animate attributeName="width" dur="12.0s" repeatCount="indefinite"
                   keyTimes="0.00000;0.40000;0.48000;0.56000;0.60000;1.00000" values="0.00;0.00;118.00;118.00;0.00;0.00" calcMode="linear"/>
        </rect>
      </clipPath>

      <clipPath id="clipRole_3">
        <rect x="0" y="0" height="29">
          <animate attributeName="width" dur="12.0s" repeatCount="indefinite"
                   keyTimes="0.00000;0.60000;0.68000;0.76000;0.80000;1.00000" values="0.00;0.00;271.40;271.40;0.00;0.00" calcMode="linear"/>
        </rect>
      </clipPath>

      <clipPath id="clipRole_4">
        <rect x="0" y="0" height="29">
          <animate attributeName="width" dur="12.0s" repeatCount="indefinite"
                   keyTimes="0.00000;0.80000;0.88000;0.96000;1.00000" values="0.00;0.00;224.20;224.20;0.00" calcMode="linear"/>
        </rect>
      </clipPath>
  </defs>

  <g clip-path="url(#cardClip)">
    <rect x="0" y="0" width="1180" height="610" fill="{bg_color}"/>

    <!-- floating ambient glow blobs -->
    <circle cx="120" cy="90" r="260" fill="url(#glow2)" filter="url(#softBlur)">
      <animate attributeName="cx" values="120;220;120" dur="13s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="90;180;90" dur="16s" repeatCount="indefinite"/>
    </circle>
    <circle cx="950" cy="120" r="300" fill="url(#glow1)" filter="url(#softBlur)">
      <animate attributeName="cx" values="950;830;950" dur="15s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="120;240;120" dur="11s" repeatCount="indefinite"/>
    </circle>
    <circle cx="700" cy="520" r="280" fill="url(#glow3)" filter="url(#softBlur)">
      <animate attributeName="cx" values="700;600;700" dur="17s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="520;430;520" dur="14s" repeatCount="indefinite"/>
    </circle>

    <!-- tiny floating particles -->
    {particles}

    <!-- noise texture overlay -->
    <rect x="0" y="0" width="1180" height="610" filter="url(#noiseFilter)" opacity="{noise_opacity}">
      <animate attributeName="opacity" values="{noise_opacity_1};{noise_opacity_2};{noise_opacity_1}" dur="2.4s" repeatCount="indefinite"/>
    </rect>

    <!-- LEFT PANEL -->
    <g>
      <rect x="24" y="24" width="448" height="562" rx="20"
            fill="{panel_fill}" fill-opacity="0.82"/>
      <rect x="24" y="24" width="448" height="562" rx="20"
            fill="url(#glassSheen)"/>
      <rect x="24" y="24" width="448" height="562" rx="20" fill="none"
            stroke="{border_color}" stroke-width="1"/>
      <rect x="24" y="24" width="448" height="562" rx="20" fill="none"
            stroke="url(#borderShimmer)" stroke-width="1.4"/>

      <g transform="translate(50,66)">
      <text x="0" y="0" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">     .--------------.
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.25s" fill="freeze"/>
      </text>

      <text x="0" y="20" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">    /  .----------.  \
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.39s" fill="freeze"/>
      </text>

      <text x="0" y="40" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">   |  |  o      o  |  |
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.53s" fill="freeze"/>
      </text>

      <text x="0" y="60" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">   |  |      ..     |  |
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.67s" fill="freeze"/>
      </text>

      <text x="0" y="80" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">   |  |   \____/   |  |
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.81s" fill="freeze"/>
      </text>

      <text x="0" y="100" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">    \  '----------'  /
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="0.95s" fill="freeze"/>
      </text>

      <text x="0" y="120" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">     '-.__________.-'
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="1.09s" fill="freeze"/>
      </text>

      <text x="0" y="140" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="15" fill="url(#asciiGrad)" opacity="0" font-weight="600"
            letter-spacing="0.5">        [ ONLINE ]
        <animate attributeName="opacity" from="0" to="1" dur="0.55s" begin="1.23s" fill="freeze"/>
      </text>
      <rect x="-8" y="-4" width="290" height="5" fill="{accent_2}" opacity="0.10">
        <animate attributeName="y" values="-4;160;-4" dur="3.6s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.02;0.16;0.02" dur="3.6s" repeatCount="indefinite"/>
      </rect></g>

      <text x="50" y="226" font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
            font-size="15" fill="{text_secondary}" opacity="0">
        Hi 👋
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.9s" fill="freeze"/>
      </text>
      <text x="50" y="256" font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
            font-size="27" font-weight="700" fill="{text_primary}" opacity="0">
        I'm Abhinav Sunil
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="2.1s" fill="freeze"/>
      </text>

      <g transform="translate(50,266)">
      <g clip-path="url(#clipRole_0)">
        <text x="0" y="19" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
              font-size="19" fill="url(#accentGrad)" font-weight="600">Full-Stack Engineer</text>
      </g>

      <g clip-path="url(#clipRole_1)">
        <text x="0" y="19" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
              font-size="19" fill="url(#accentGrad)" font-weight="600">Systems Architect</text>
      </g>

      <g clip-path="url(#clipRole_2)">
        <text x="0" y="19" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
              font-size="19" fill="url(#accentGrad)" font-weight="600">AI Builder</text>
      </g>

      <g clip-path="url(#clipRole_3)">
        <text x="0" y="19" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
              font-size="19" fill="url(#accentGrad)" font-weight="600">Open Source Contributor</text>
      </g>

      <g clip-path="url(#clipRole_4)">
        <text x="0" y="19" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
              font-size="19" fill="url(#accentGrad)" font-weight="600">Distributed Systems</text>
      </g>
      <rect x="272" y="0" width="3" height="21" fill="url(#accentGrad)" rx="1.5">
        <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.45;0.5;0.95;1"
                 dur="0.9s" repeatCount="indefinite"/>
      </rect></g>

      <g transform="translate(50,306)">
      <g transform="translate(0,0)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.60s" fill="freeze"/>
        <animateTransform attributeName="transform" type="translate" additive="sum"
                           from="-14,0" to="0,0" dur="0.5s" begin="1.60s" fill="freeze"/>
        <circle cx="6" cy="-4" r="9" fill="url(#accentGrad)" opacity="0.16"/>
        <text x="6" y="-1" text-anchor="middle" font-size="10" fill="url(#accentGrad)"
              font-family="'SFMono-Regular',Consolas,monospace" font-weight="700">◉</text>
        <text x="24" y="1" font-size="14" fill="{text_secondary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">India</text>
      </g>
      <g transform="translate(0,27)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.78s" fill="freeze"/>
        <animateTransform attributeName="transform" type="translate" additive="sum"
                           from="-14,0" to="0,0" dur="0.5s" begin="1.78s" fill="freeze"/>
        <circle cx="6" cy="-4" r="9" fill="url(#accentGrad)" opacity="0.16"/>
        <text x="6" y="-1" text-anchor="middle" font-size="10" fill="url(#accentGrad)"
              font-family="'SFMono-Regular',Consolas,monospace" font-weight="700">■</text>
        <text x="24" y="1" font-size="14" fill="{text_secondary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">B.Tech Computer Science</text>
      </g>
      <g transform="translate(0,54)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.96s" fill="freeze"/>
        <animateTransform attributeName="transform" type="translate" additive="sum"
                           from="-14,0" to="0,0" dur="0.5s" begin="1.96s" fill="freeze"/>
        <circle cx="6" cy="-4" r="9" fill="url(#accentGrad)" opacity="0.16"/>
        <text x="6" y="-1" text-anchor="middle" font-size="10" fill="url(#accentGrad)"
              font-family="'SFMono-Regular',Consolas,monospace" font-weight="700">◆</text>
        <text x="24" y="1" font-size="14" fill="{text_secondary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">Distributed Systems &amp; AI</text>
      </g>
      <g transform="translate(0,81)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="2.14s" fill="freeze"/>
        <animateTransform attributeName="transform" type="translate" additive="sum"
                           from="-14,0" to="0,0" dur="0.5s" begin="2.14s" fill="freeze"/>
        <circle cx="6" cy="-4" r="9" fill="url(#accentGrad)" opacity="0.16"/>
        <text x="6" y="-1" text-anchor="middle" font-size="10" fill="url(#accentGrad)"
              font-family="'SFMono-Regular',Consolas,monospace" font-weight="700">●</text>
        <text x="24" y="1" font-size="14" fill="{text_secondary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">github.com/IamAbhinav01</text>
      </g>
      <g transform="translate(0,108)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="2.32s" fill="freeze"/>
        <animateTransform attributeName="transform" type="translate" additive="sum"
                           from="-14,0" to="0,0" dur="0.5s" begin="2.32s" fill="freeze"/>
        <circle cx="6" cy="-4" r="9" fill="url(#accentGrad)" opacity="0.16"/>
        <text x="6" y="-1" text-anchor="middle" font-size="10" fill="url(#accentGrad)"
              font-family="'SFMono-Regular',Consolas,monospace" font-weight="700">✉</text>
        <text x="24" y="1" font-size="14" fill="{text_secondary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">abhinavsunil@hotmail.com</text>
      </g></g>
      
      <g transform="translate(50,446)">
      {skills}
      </g>

      <g transform="translate(50,546)">
      <g transform="translate(0,0)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.60s" fill="freeze"/>
        <circle cx="18" cy="18" r="18" fill="{icon_bg}" stroke="url(#accentGrad)"
                stroke-opacity="0.5" stroke-width="1.3" filter="url(#iconGlow)">
          <animate attributeName="stroke-opacity" values="0.3;0.7;0.3" dur="3s"
                   begin="4.60s" repeatCount="indefinite"/>
        </circle>
        <text x="18" y="22.5" text-anchor="middle" font-size="12" font-weight="700" fill="{text_primary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">GH</text>
      </g>
      <g transform="translate(54,0)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.72s" fill="freeze"/>
        <circle cx="18" cy="18" r="18" fill="{icon_bg}" stroke="url(#accentGrad)"
                stroke-opacity="0.5" stroke-width="1.3" filter="url(#iconGlow)">
          <animate attributeName="stroke-opacity" values="0.3;0.7;0.3" dur="3s"
                   begin="4.72s" repeatCount="indefinite"/>
        </circle>
        <text x="18" y="22.5" text-anchor="middle" font-size="12" font-weight="700" fill="{text_primary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">in</text>
      </g>
      <g transform="translate(108,0)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.84s" fill="freeze"/>
        <circle cx="18" cy="18" r="18" fill="{icon_bg}" stroke="url(#accentGrad)"
                stroke-opacity="0.5" stroke-width="1.3" filter="url(#iconGlow)">
          <animate attributeName="stroke-opacity" values="0.3;0.7;0.3" dur="3s"
                   begin="4.84s" repeatCount="indefinite"/>
        </circle>
        <text x="18" y="22.5" text-anchor="middle" font-size="12" font-weight="700" fill="{text_primary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">X</text>
      </g>
      <g transform="translate(162,0)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.96s" fill="freeze"/>
        <circle cx="18" cy="18" r="18" fill="{icon_bg}" stroke="url(#accentGrad)"
                stroke-opacity="0.5" stroke-width="1.3" filter="url(#iconGlow)">
          <animate attributeName="stroke-opacity" values="0.3;0.7;0.3" dur="3s"
                   begin="4.96s" repeatCount="indefinite"/>
        </circle>
        <text x="18" y="22.5" text-anchor="middle" font-size="12" font-weight="700" fill="{text_primary}"
              font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">W</text>
      </g></g>
    </g>

    <!-- RIGHT PANEL -->
    <g>
      <rect x="494" y="24" width="662" height="562" rx="20"
            fill="{panel_fill}" fill-opacity="0.7"/>
      <rect x="494" y="24" width="662" height="562" rx="20"
            fill="url(#glassSheen)"/>
      <rect x="494" y="24" width="662" height="562" rx="20" fill="none"
            stroke="{border_color}" stroke-width="1"/>
      <rect x="494" y="24" width="662" height="562" rx="20" fill="none"
            stroke="url(#borderShimmer)" stroke-width="1.4"/>

      
    <g transform="translate(524,64)">
      <rect x="0" y="0" width="602" height="260" rx="16" fill="{code_bg}"
            stroke="{border_color}"/>
      <rect x="0" y="0" width="602" height="34" rx="16" fill="{code_bg}"/>
      <rect x="0" y="18" width="602" height="16" fill="{code_bg}"/>
      <line x1="0" y1="34" x2="602" y2="34" stroke="{border_color}"/>
      
      <circle cx="14" cy="14" r="5.5" fill="#FF5F56"/>
      <circle cx="32" cy="14" r="5.5" fill="#FFBD2E"/>
      <circle cx="50" cy="14" r="5.5" fill="#27C93F"/>
      <text x="301.0" y="18.5" text-anchor="middle" font-size="12" fill="{text_secondary}"
            font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">portfolio.tsx</text>
      <g transform="translate(24,64)">
        
      <text x="0" y="0" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.00s" fill="freeze"/>
        <tspan fill="{code_kw}">const </tspan><tspan fill="{text_primary}">dev</tspan><tspan fill="{text_secondary}"> = </tspan><tspan fill="{code_fn}">createEngineer</tspan><tspan fill="{text_secondary}">({{</tspan>
      </text>
      <text x="0" y="24" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.28s" fill="freeze"/>
        <tspan fill="{text_secondary}">  name</tspan><tspan fill="{text_secondary}">: </tspan><tspan fill="{code_str}">'Abhinav Sunil'</tspan><tspan fill="{text_secondary}">,</tspan>
      </text>
      <text x="0" y="48" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.56s" fill="freeze"/>
        <tspan fill="{text_secondary}">  stack</tspan><tspan fill="{text_secondary}">: [</tspan><tspan fill="{code_str}">'Go'</tspan><tspan fill="{text_secondary}">, </tspan><tspan fill="{code_str}">'Python'</tspan><tspan fill="{text_secondary}">],</tspan>
      </text>
      <text x="0" y="72" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.84s" fill="freeze"/>
        <tspan fill="{text_secondary}">  passion</tspan><tspan fill="{text_secondary}">: </tspan><tspan fill="{code_str}">'building scalable AI'</tspan>
      </text>
      <text x="0" y="96" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.12s" fill="freeze"/>
        <tspan fill="{text_secondary}">}})</tspan>
      </text>
      <text x="0" y="120" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.40s" fill="freeze"/>
        <tspan fill="{text_secondary}"></tspan>
      </text>
      <text x="0" y="144" font-family="'SFMono-Regular',Consolas,Menlo,monospace"
            font-size="14.5" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="2.68s" fill="freeze"/>
        <tspan fill="{code_kw}">export default </tspan><tspan fill="{text_primary}">dev</tspan><tspan fill="{text_secondary}">.ship();</tspan>
      </text>
        
      <rect x="235" y="132" width="8" height="16" fill="{accent_2}" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="2.96s" fill="freeze"/>
        <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.45;0.5;0.95;1" dur="1s"
                  begin="3.26s" repeatCount="indefinite"/>
      </rect>
      </g>
    </g>
      <g>
      <circle cx="825.0" cy="474" r="110" fill="none" stroke="url(#accentGrad)" stroke-opacity="0.18" stroke-width="1"/>
      <circle cx="825.0" cy="474" r="7" fill="url(#accentGrad)" opacity="0.85" filter="url(#iconGlow)">
        <animate attributeName="r" values="6;8;6" dur="2.6s" repeatCount="indefinite"/>
      </circle>
      <g>
        <animateMotion dur="14s" repeatCount="indefinite" begin="-0.00s"
                        path="M 935.0,474 A 110,110 0 1,1 715.0,474 A 110,110 0 1,1 935.0,474"/>
        <circle r="15" fill="{icon_bg}" stroke="url(#accentGrad)" stroke-opacity="0.6" stroke-width="1.2"/>
        <text y="4" text-anchor="middle" font-size="11" font-weight="700" fill="{text_primary}"
              font-family="'SFMono-Regular',Consolas,monospace">Go</text>
      </g>
      <g>
        <animateMotion dur="14s" repeatCount="indefinite" begin="-2.80s"
                        path="M 935.0,474 A 110,110 0 1,1 715.0,474 A 110,110 0 1,1 935.0,474"/>
        <circle r="15" fill="{icon_bg}" stroke="url(#accentGrad)" stroke-opacity="0.6" stroke-width="1.2"/>
        <text y="4" text-anchor="middle" font-size="11" font-weight="700" fill="{text_primary}"
              font-family="'SFMono-Regular',Consolas,monospace">Py</text>
      </g>
      <g>
        <animateMotion dur="14s" repeatCount="indefinite" begin="-5.60s"
                        path="M 935.0,474 A 110,110 0 1,1 715.0,474 A 110,110 0 1,1 935.0,474"/>
        <circle r="15" fill="{icon_bg}" stroke="url(#accentGrad)" stroke-opacity="0.6" stroke-width="1.2"/>
        <text y="4" text-anchor="middle" font-size="11" font-weight="700" fill="{text_primary}"
              font-family="'SFMono-Regular',Consolas,monospace">TS</text>
      </g>
      <g>
        <animateMotion dur="14s" repeatCount="indefinite" begin="-8.40s"
                        path="M 935.0,474 A 110,110 0 1,1 715.0,474 A 110,110 0 1,1 935.0,474"/>
        <circle r="15" fill="{icon_bg}" stroke="url(#accentGrad)" stroke-opacity="0.6" stroke-width="1.2"/>
        <text y="4" text-anchor="middle" font-size="11" font-weight="700" fill="{text_primary}"
              font-family="'SFMono-Regular',Consolas,monospace">AI</text>
      </g>
      <g>
        <animateMotion dur="14s" repeatCount="indefinite" begin="-11.20s"
                        path="M 935.0,474 A 110,110 0 1,1 715.0,474 A 110,110 0 1,1 935.0,474"/>
        <circle r="15" fill="{icon_bg}" stroke="url(#accentGrad)" stroke-opacity="0.6" stroke-width="1.2"/>
        <text y="4" text-anchor="middle" font-size="11" font-weight="700" fill="{text_primary}"
              font-family="'SFMono-Regular',Consolas,monospace">DB</text>
      </g></g>
    </g>

    <!-- outer card border shimmer -->
    <rect x="1" y="1" width="1178" height="608" rx="28" fill="none"
          stroke="{border_color}" stroke-width="1.5"/>
    <rect x="1" y="1" width="1178" height="608" rx="28" fill="none"
          stroke="url(#borderShimmer)" stroke-width="1.6"/>
  </g>
</svg>"""

skills = [
    ("GoLang", 73, 0, 0),
    ("Python", 73, 81, 0),
    ("Node.js", 81, 162, 0),
    ("TypeScript", 104, 251, 0),
    ("React", 66, 0, 34),
    ("Tailwind", 88, 74, 34),
    ("Docker", 73, 170, 34),
    ("Postgres", 88, 251, 34),
    ("Git", 50, 0, 68),
    ("PyTorch", 81, 58, 68),
    ("LangChain", 96, 147, 68)
]

skill_template = """      <g transform="translate({x},{y})" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.45s" begin="{begin}s" fill="freeze"/>
        <rect x="0" y="0" width="{w}" height="26" rx="13" fill="{pill_bg}"
              stroke="url(#accentGrad)" stroke-opacity="0.55" stroke-width="1" filter="url(#pillGlow)">
          <animate attributeName="stroke-opacity" values="0.35;0.75;0.35" dur="3.4s"
                   begin="{anim_begin}s" repeatCount="indefinite"/>
        </rect>
        <text x="{mid}" y="17.5" text-anchor="middle" font-size="12.5" font-weight="600"
              fill="{text_primary}" font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">{name}</text>
      </g>"""

def gen_particles(color):
    ps = []
    points = [
        (80, 60), (177, 113), (274, 166), (371, 219), (468, 272), (565, 325),
        (662, 378), (759, 431), (856, 484), (953, 537), (1050, 70), (1147, 123),
        (144, 176), (241, 229), (338, 282), (435, 335), (532, 388), (629, 441)
    ]
    import random
    random.seed(42)
    for i, (cx, cy) in enumerate(points):
        r = random.choice([1.4, 2.0, 2.6])
        dur_y = random.randint(6, 10)
        dur_op = random.randint(4, 7)
        ps.append(f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.35">
      <animate attributeName="cy" values="{cy};{cy-40};{cy}" dur="{dur_y}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.1;0.6;0.1" dur="{dur_op}s" repeatCount="indefinite"/>
    </circle>''')
    return "".join(ps)

def gen_skills(pill_bg, text_primary):
    out = []
    base_begin = 2.60
    anim_base = 3.20
    for i, (name, w, x, y) in enumerate(skills):
        begin = f"{(base_begin + i*0.08):.2f}"
        anim_begin = f"{(anim_base + (i%4)*0.4):.2f}"
        out.append(skill_template.format(
            x=x, y=y, w=w, mid=w/2, name=name,
            begin=begin, anim_begin=anim_begin,
            pill_bg=pill_bg, text_primary=text_primary
        ))
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
    "ascii_1": "#22D3EE",
    "ascii_2": "#7C3AED",
    "glow_1": "#3B82F6",
    "glow_2": "#7C3AED",
    "glow_3": "#10B981",
    "glow_opacity": "0.35",
    "sheen_color": "#FFFFFF",
    "particles": gen_particles("#22D3EE"),
    "noise_opacity": "0.035",
    "noise_opacity_1": "0.021",
    "noise_opacity_2": "0.049",
    "pill_bg": "#0B1220",
    "icon_bg": "#111827",
    "code_bg": "#111827",
    "code_kw": "#C084FC",
    "code_fn": "#22D3EE",
    "code_str": "#34D399",
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
    "ascii_1": "#06B6D4",
    "ascii_2": "#2563EB",
    "glow_1": "#2563EB",
    "glow_2": "#06B6D4",
    "glow_3": "#10B981",
    "glow_opacity": "0.15",
    "sheen_color": "#000000",
    "particles": gen_particles("#06B6D4"),
    "noise_opacity": "0.015",
    "noise_opacity_1": "0.01",
    "noise_opacity_2": "0.02",
    "pill_bg": "#FFFFFF",
    "icon_bg": "#FFFFFF",
    "code_bg": "#FFFFFF",
    "code_kw": "#4F46E5",
    "code_fn": "#06B6D4",
    "code_str": "#059669",
}

with open("e:/IamAbhinav01/dark.svg", "w", encoding="utf-8") as f:
    vars_d = dark_vars.copy()
    vars_d["skills"] = gen_skills(vars_d["pill_bg"], vars_d["text_primary"])
    f.write(dark_template.format(**vars_d))

with open("e:/IamAbhinav01/light.svg", "w", encoding="utf-8") as f:
    vars_l = light_vars.copy()
    vars_l["skills"] = gen_skills(vars_l["pill_bg"], vars_l["text_primary"])
    f.write(dark_template.format(**vars_l))
