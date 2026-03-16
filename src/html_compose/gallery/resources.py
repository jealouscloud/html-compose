class IframeScripts:
    parent = """
// Iframe auto-sizing: uses adoptedStyleSheets to survive HTML morphs
window._iframeSizer ??= (() => {
  const SELECTOR = "iframe.o-showcase-content";
  const sheet = new CSSStyleSheet();
  document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];

  const sync = () => {
    const rules = [];
    for (const frame of document.querySelectorAll(SELECTOR)) {
      const height = frame.contentDocument?.body?.scrollHeight;
      if (height && frame.id) rules.push(`#${CSS.escape(frame.id)} { height: ${height}px; }`);
    }
    // Only update when we have heights - preserves rules when iframe not yet ready
    if (rules.length) sheet.replaceSync(rules.join("\\n"));
  };

  const resizeObs = new ResizeObserver(sync);

  const observe = () => {
    for (const frame of document.querySelectorAll(SELECTOR)) {
      if (frame.contentDocument?.body) resizeObs.observe(frame.contentDocument.body);
      frame.onload = () => {
        if (frame.contentDocument?.body) resizeObs.observe(frame.contentDocument.body);
        sync();
      };
    }
    sync();
  };

  // MutationObserver runs indefinitely (never disconnected)
  new MutationObserver(observe).observe(document.body, { childList: true, subtree: true, attributes: true });
  return { observe };
})();
window._iframeSizer.observe();"""


NAV_STYLES = """
:host {
  display: block;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 14px;
  padding: 12px 0;
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
details {
  margin: 0;
}
summary {
  cursor: pointer;
  padding: 6px 16px;
  color: #333;
  font-weight: 500;
  user-select: none;
}
summary:hover {
  background: #f5f5f5;
}
details > ul {
  padding-left: 12px;
}
details details summary {
  font-weight: 400;
  color: #666;
  padding: 4px 16px;
  font-size: 13px;
}
a {
  display: block;
  padding: 4px 16px;
  color: #0066cc;
  text-decoration: none;
  font-size: 13px;
}
a:hover {
  background: #e8f4fc;
}
"""

GALLERY_STYLES = """
/* Gallery base styles */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #f5f5f5;
  color: #333;
}

/* Main layout */
.o-gallery-container {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  height: 100vh;
}

/* Left navigation panel */
.o-left-panel {
  flex: 0 0 240px;
  overflow-y: auto;
  overflow-x: hidden;
  background: #fff;
  border-right: 1px solid #e0e0e0;
}

/* Hide the empty right panel */
.o-right-panel {
  display: none;
}

/* Center content panel */
.o-center-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding: 24px;
  overflow-y: auto;
  background: #f5f5f5;
}

/* Showcase card container */
.o-showcase-card {
  flex-shrink: 0;  /* Don't shrink - overflow and scroll instead */
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* Showcase header */
.o-showcase-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  color: #555;
  background: #fafafa;
  border-bottom: 1px solid #e0e0e0;
}

.o-showcase-title {
  flex: 1;
}

.o-showcase-link {
  color: #888;
  text-decoration: none;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 13px;
}

.o-showcase-link:hover {
  background: #e8e8e8;
  color: #333;
}

/* Showcase content container */
.o-showcase-content {
  background: #fff;
}

/* Iframe showcases */
iframe.o-showcase-content {
  display: block;
  border: none;
  width: 100%;
  flex-shrink: 0;
  overflow: hidden;
}
"""
