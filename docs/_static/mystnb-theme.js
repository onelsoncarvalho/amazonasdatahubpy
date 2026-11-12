(() => {
  "use strict";

  const STYLE_ID = "amazonasdatahub-mystnb-theme";

  const css = `
    /* LIGHT THEME */
    html[data-theme="light"] .cell_input,
    html[data-theme="light"] .cell_input .highlight,
    html[data-theme="light"] .cell_input pre {
      background-color: #ffffff !important;
      color: #1F2328 !important;
    }

    /* DARK THEME */
    html[data-theme="dark"] .cell_input,
    html[data-theme="dark"] .cell_input .highlight,
    html[data-theme="dark"] .cell_input pre {
      background-color: #0d1117 !important;
      color: #E6EDF3 !important;
    }

    /* Preserve Pygments syntax highlighting */
    html[data-theme="light"] .cell_input .highlight span {
      color: inherit;
    }

    html[data-theme="dark"] .cell_input .highlight span {
      color: inherit;
    }

    /* Dark theme syntax colors */
    html[data-theme="dark"] .cell_input .highlight .c,
    html[data-theme="dark"] .cell_input .highlight .c1,
    html[data-theme="dark"] .cell_input .highlight .cm {
      color: #8B949E !important;
    }

    html[data-theme="dark"] .cell_input .highlight .k,
    html[data-theme="dark"] .cell_input .highlight .kd {
      color: #FF7B72 !important;
    }

    html[data-theme="dark"] .cell_input .highlight .s,
    html[data-theme="dark"] .cell_input .highlight .s1,
    html[data-theme="dark"] .cell_input .highlight .s2 {
      color: #A5D6FF !important;
    }

    html[data-theme="dark"] .cell_input .highlight .m,
    html[data-theme="dark"] .cell_input .highlight .mi,
    html[data-theme="dark"] .cell_input .highlight .mf {
      color: #79C0FF !important;
    }

    html[data-theme="dark"] .cell_input .highlight .nf {
      color: #D2A8FF !important;
    }

    html[data-theme="dark"] .cell_input .highlight .nc,
    html[data-theme="dark"] .cell_input .highlight .kt {
      color: #FFA657 !important;
    }

    html[data-theme="dark"] .cell_input .highlight .o {
      color: #FF7B72 !important;
    }
  `;

  function applyTheme() {
    let style = document.getElementById(STYLE_ID);

    if (!style) {
      style = document.createElement("style");
      style.id = STYLE_ID;
      document.head.appendChild(style);
    }

    style.textContent = css;
  }

  applyTheme();

  new MutationObserver(applyTheme).observe(
    document.documentElement,
    {
      attributes: true,
      attributeFilter: ["data-theme"]
    }
  );
})();
