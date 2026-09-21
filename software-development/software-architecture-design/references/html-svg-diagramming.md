# HTML+CSS+SVG Architecture Diagramming Reference

Self-contained architecture diagrams using the C4 model, rendered as standalone HTML files with inline CSS and inline SVG. No external libraries, no internet access, no rendering tools required.

## Why Self-Contained HTML+CSS+SVG

- **Zero dependencies** — no Mermaid.js, no PlantUML server, no npm install; any browser opens the file
- **Text-readable** — HTML and SVG are text; LLMs can parse, diff, and reason about the structure
- **Version-controllable** — diffs show exactly what changed in the diagram
- **Inline in Hermes** — use `::preview{file="diagram.html"}` to render diagrams directly in chat
- **Portable** — email it, commit it, open it on any device with a browser

## C4 Levels

| Level | Question | When to Use |
|-------|----------|-------------|
| 1. Context | What is the system and who uses it? | Stakeholder overview, system boundaries |
| 2. Container | What are the deployable pieces? | Developer overview, technology stack |
| 3. Component | What's inside each container? | Internal module structure |
| 4. Deployment | Where does it run? | Infrastructure, topology |
| —. Data Flow | How does data move? | Primary use case walkthroughs |

## HTML Scaffold

Every diagram is a complete HTML document. Use this scaffold as the starting point:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Architecture Diagram: <Name></title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #fafafa;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }
    svg { max-width: 100%; height: auto; }

    /* C4 element fills — distinct color per element type */
    .person       { fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; }
    .system       { fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; }
    .system-ext   { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; stroke-dasharray: 6 4; }
    .container    { fill: #f3e5f5; stroke: #7b1fa2; stroke-width: 2; }
    .component    { fill: #e0f2f1; stroke: #00695c; stroke-width: 2; }
    .deploy-node  { fill: #eceff1; stroke: #455a64; stroke-width: 2; }
    .queue        { fill: #fce4ec; stroke: #c62828; stroke-width: 2; }

    /* Typography */
    .title    { font-size: 20px; font-weight: 700; fill: #1a1a1a; }
    .label    { font-size: 14px; font-weight: 600; fill: #1a1a1a; }
    .tech     { font-size: 12px; font-weight: 400; fill: #555; }
    .desc     { font-size: 11px; font-weight: 400; fill: #666; }

    /* Connectors */
    .arrow       { stroke: #455a64; stroke-width: 1.5; fill: none; }
    .arrow-text  { font-size: 11px; fill: #455a64; }
    .boundary    { fill: none; stroke: #90a4ae; stroke-width: 1.5; stroke-dasharray: 8 4; }
  </style>
</head>
<body>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520">
    <!-- SVG content goes here -->
  </svg>
</body>
</html>
```

## SVG Primitives

### Box (rect)

```svg
<rect x="50" y="100" width="160" height="80" rx="8" class="system"/>
<text x="130" y="135" text-anchor="middle" class="label">Label</text>
<text x="130" y="155" text-anchor="middle" class="desc">Description</text>
```

**Element classes:** `person`, `system`, `system-ext`, `container`, `component`, `deploy-node`, `queue`

### Technology annotation

Add a smaller line below the label showing the technology from Task 5:

```svg
<rect x="50" y="100" width="160" height="90" rx="8" class="container"/>
<text x="130" y="130" text-anchor="middle" class="label">Order Service</text>
<text x="130" y="148" text-anchor="middle" class="tech">Python / FastAPI</text>
<text x="130" y="168" text-anchor="middle" class="desc">Order processing</text>
```

### Arrow with label

Requires a `<marker>` definition in `<defs>`:

```svg
<defs>
  <marker id="arrow" markerWidth="10" markerHeight="7"
          refX="10" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
  </marker>
</defs>

<line x1="210" y1="140" x2="350" y2="180" class="arrow" marker-end="url(#arrow)"/>
<text x="280" y="155" text-anchor="middle" class="arrow-text">calls</text>
```

### System boundary (dashed container)

Groups elements that belong to the same system:

```svg
<rect x="340" y="80" width="380" height="320" rx="8" class="boundary"/>
<text x="530" y="100" text-anchor="middle" class="label">Order Management System</text>
<!-- Place container/component rects inside this boundary -->
```

### Database (cylinder)

```svg
<g>
  <path d="M 420,350 a 50,8 0 1,0 100,0 l 0,40 a 50,8 0 1,1 -100,0 z" class="container"/>
  <ellipse cx="470" cy="350" rx="50" ry="8" class="container"/>
  <text x="470" y="375" text-anchor="middle" class="label">Database</text>
  <text x="470" y="393" text-anchor="middle" class="tech">PostgreSQL</text>
</g>
```

### Message queue (parallelogram)

```svg
<polygon points="350,350 530,350 510,390 330,390" class="queue"/>
<text x="430" y="365" text-anchor="middle" class="label">Message Queue</text>
<text x="430" y="383" text-anchor="middle" class="tech">Kafka</text>
```

## Worked Example: Context Diagram (Complete HTML)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Context Diagram — Order Management System</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
           background: #fafafa; display: flex; justify-content: center; padding: 2rem; }
    svg { max-width: 100%; height: auto; }
    .person     { fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; }
    .system     { fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; }
    .system-ext { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; stroke-dasharray: 6 4; }
    .title      { font-size: 20px; font-weight: 700; fill: #1a1a1a; }
    .label      { font-size: 14px; font-weight: 600; fill: #1a1a1a; }
    .desc       { font-size: 11px; font-weight: 400; fill: #666; }
    .arrow      { stroke: #455a64; stroke-width: 1.5; fill: none; }
    .arrow-text { font-size: 11px; fill: #455a64; }
  </style>
</head>
<body>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520">
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="7"
              refX="10" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
      </marker>
    </defs>

    <text x="450" y="30" text-anchor="middle" class="title">System Context — Order Management System</text>

    <!-- Customer -->
    <rect x="50" y="180" width="140" height="80" rx="8" class="person"/>
    <text x="120" y="215" text-anchor="middle" class="label">Customer</text>
    <text x="120" y="235" text-anchor="middle" class="desc">Places orders online</text>

    <!-- Admin -->
    <rect x="50" y="320" width="140" height="80" rx="8" class="person"/>
    <text x="120" y="355" text-anchor="middle" class="label">Admin</text>
    <text x="120" y="375" text-anchor="middle" class="desc">Manages products</text>

    <!-- OMS (System) -->
    <rect x="360" y="220" width="180" height="100" rx="8" class="system"/>
    <text x="450" y="258" text-anchor="middle" class="label">Order Management</text>
    <text x="450" y="278" text-anchor="middle" class="label">System</text>
    <text x="450" y="298" text-anchor="middle" class="desc">Processes customer orders</text>

    <!-- Payment Gateway (External) -->
    <rect x="670" y="100" width="170" height="80" rx="8" class="system-ext"/>
    <text x="755" y="135" text-anchor="middle" class="label">Payment Gateway</text>
    <text x="755" y="155" text-anchor="middle" class="desc">Processes payments</text>

    <!-- Email Service (External) -->
    <rect x="670" y="250" width="170" height="80" rx="8" class="system-ext"/>
    <text x="755" y="285" text-anchor="middle" class="label">Email Service</text>
    <text x="755" y="305" text-anchor="middle" class="desc">Sends confirmations</text>

    <!-- Inventory System (External) -->
    <rect x="670" y="400" width="170" height="80" rx="8" class="system-ext"/>
    <text x="755" y="435" text-anchor="middle" class="label">Inventory System</text>
    <text x="755" y="455" text-anchor="middle" class="desc">Tracks stock levels</text>

    <!-- Arrows -->
    <line x1="190" y1="220" x2="360" y2="248" class="arrow" marker-end="url(#arrow)"/>
    <text x="275" y="225" text-anchor="middle" class="arrow-text">Places orders</text>

    <line x1="190" y1="360" x2="360" y2="292" class="arrow" marker-end="url(#arrow)"/>
    <text x="275" y="335" text-anchor="middle" class="arrow-text">Manages</text>

    <line x1="540" y1="240" x2="670" y2="140" class="arrow" marker-end="url(#arrow)"/>
    <text x="605" y="178" text-anchor="middle" class="arrow-text">Processes payment</text>

    <line x1="540" y1="270" x2="670" y2="290" class="arrow" marker-end="url(#arrow)"/>
    <text x="605" y="270" text-anchor="middle" class="arrow-text">Sends emails</text>

    <line x1="540" y1="300" x2="670" y2="440" class="arrow" marker-end="url(#arrow)"/>
    <text x="605" y="380" text-anchor="middle" class="arrow-text">Checks stock</text>
  </svg>
</body>
</html>
```

## Worked Example: Container Diagram (SVG body)

Use the same HTML scaffold; replace the `<svg>` content:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
    </marker>
  </defs>

  <text x="450" y="30" text-anchor="middle" class="title">Container Diagram — Order Management System</text>

  <!-- Customer -->
  <rect x="30" y="200" width="130" height="70" rx="8" class="person"/>
  <text x="95" y="230" text-anchor="middle" class="label">Customer</text>
  <text x="95" y="248" text-anchor="middle" class="desc">Places orders</text>

  <!-- System boundary -->
  <rect x="210" y="60" width="470" height="460" rx="8" class="boundary"/>
  <text x="445" y="82" text-anchor="middle" class="label">Order Management System</text>

  <!-- Web App -->
  <rect x="240" y="110" width="150" height="85" rx="8" class="container"/>
  <text x="315" y="140" text-anchor="middle" class="label">Web App</text>
  <text x="315" y="158" text-anchor="middle" class="tech">React</text>
  <text x="315" y="178" text-anchor="middle" class="desc">Customer-facing UI</text>

  <!-- API Gateway -->
  <rect x="430" y="110" width="150" height="85" rx="8" class="container"/>
  <text x="505" y="140" text-anchor="middle" class="label">API Gateway</text>
  <text x="505" y="158" text-anchor="middle" class="tech">Node.js</text>
  <text x="505" y="178" text-anchor="middle" class="desc">REST, auth, routing</text>

  <!-- Order Service -->
  <rect x="240" y="240" width="150" height="85" rx="8" class="container"/>
  <text x="315" y="270" text-anchor="middle" class="label">Order Service</text>
  <text x="315" y="288" text-anchor="middle" class="tech">Python / FastAPI</text>
  <text x="315" y="308" text-anchor="middle" class="desc">Order processing</text>

  <!-- Inventory Service -->
  <rect x="430" y="240" width="150" height="85" rx="8" class="container"/>
  <text x="505" y="270" text-anchor="middle" class="label">Inventory Service</text>
  <text x="505" y="288" text-anchor="middle" class="tech">Go</text>
  <text x="505" y="308" text-anchor="middle" class="desc">Stock management</text>

  <!-- Database (cylinder) -->
  <g>
    <path d="M 260,400 a 55,8 0 1,0 110,0 l 0,45 a 55,8 0 1,1 -110,0 z" class="container"/>
    <ellipse cx="315" cy="400" rx="55" ry="8" class="container"/>
    <text x="315" y="425" text-anchor="middle" class="label">Database</text>
    <text x="315" y="443" text-anchor="middle" class="tech">PostgreSQL</text>
  </g>

  <!-- Message Queue (parallelogram) -->
  <polygon points="430,395 590,395 570,440 410,440" class="queue"/>
  <text x="500" y="415" text-anchor="middle" class="label">Message Queue</text>
  <text x="500" y="433" text-anchor="middle" class="tech">Kafka</text>

  <!-- Payment Gateway (External) -->
  <rect x="730" y="110" width="140" height="75" rx="8" class="system-ext"/>
  <text x="800" y="140" text-anchor="middle" class="label">Payment Gateway</text>
  <text x="800" y="160" text-anchor="middle" class="desc">Processes payments</text>

  <!-- Arrows -->
  <line x1="160" y1="235" x2="240" y2="150" class="arrow" marker-end="url(#arrow)"/>
  <text x="200" y="185" text-anchor="middle" class="arrow-text">uses</text>

  <line x1="390" y1="150" x2="430" y2="150" class="arrow" marker-end="url(#arrow)"/>
  <text x="410" y="142" text-anchor="middle" class="arrow-text">calls</text>

  <line x1="505" y1="195" x2="315" y2="240" class="arrow" marker-end="url(#arrow)"/>
  <text x="410" y="220" text-anchor="middle" class="arrow-text">routes to</text>

  <line x1="505" y1="195" x2="505" y2="240" class="arrow" marker-end="url(#arrow)"/>
  <text x="520" y="220" text-anchor="middle" class="arrow-text">routes to</text>

  <line x1="315" y1="325" x2="315" y2="392" class="arrow" marker-end="url(#arrow)"/>
  <text x="335" y="360" text-anchor="middle" class="arrow-text">reads/writes</text>

  <line x1="505" y1="325" x2="505" y2="392" class="arrow" marker-end="url(#arrow)"/>
  <text x="525" y="360" text-anchor="middle" class="arrow-text">reads/writes</text>

  <line x1="390" y1="283" x2="410" y2="415" class="arrow" marker-end="url(#arrow)"/>
  <text x="415" y="365" text-anchor="middle" class="arrow-text">publishes</text>

  <line x1="580" y1="150" x2="730" y2="148" class="arrow" marker-end="url(#arrow)"/>
  <text x="655" y="140" text-anchor="middle" class="arrow-text">payment</text>
</svg>
```

## Worked Example: Component Diagram (SVG body)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
    </marker>
  </defs>

  <text x="400" y="30" text-anchor="middle" class="title">Component Diagram — Order Service</text>

  <!-- Container boundary -->
  <rect x="80" y="60" width="640" height="300" rx="8" class="boundary"/>
  <text x="400" y="82" text-anchor="middle" class="label">Order Service</text>

  <!-- Controller -->
  <rect x="120" y="120" width="160" height="85" rx="6" class="component"/>
  <text x="200" y="150" text-anchor="middle" class="label">Order Controller</text>
  <text x="200" y="168" text-anchor="middle" class="tech">FastAPI</text>
  <text x="200" y="188" text-anchor="middle" class="desc">Handles HTTP requests</text>

  <!-- Service -->
  <rect x="320" y="120" width="160" height="85" rx="6" class="component"/>
  <text x="400" y="150" text-anchor="middle" class="label">Order Service</text>
  <text x="400" y="168" text-anchor="middle" class="tech">Python</text>
  <text x="400" y="188" text-anchor="middle" class="desc">Business logic</text>

  <!-- Repository -->
  <rect x="520" y="120" width="160" height="85" rx="6" class="component"/>
  <text x="600" y="150" text-anchor="middle" class="label">Order Repository</text>
  <text x="600" y="168" text-anchor="middle" class="tech">SQLAlchemy</text>
  <text x="600" y="188" text-anchor="middle" class="desc">Database access</text>

  <!-- Event Publisher -->
  <rect x="320" y="250" width="160" height="85" rx="6" class="component"/>
  <text x="400" y="280" text-anchor="middle" class="label">Event Publisher</text>
  <text x="400" y="298" text-anchor="middle" class="tech">aiokafka</text>
  <text x="400" y="318" text-anchor="middle" class="desc">Publishes domain events</text>

  <!-- Arrows -->
  <line x1="280" y1="162" x2="320" y2="162" class="arrow" marker-end="url(#arrow)"/>
  <text x="300" y="155" text-anchor="middle" class="arrow-text">calls</text>

  <line x1="480" y1="162" x2="520" y2="162" class="arrow" marker-end="url(#arrow)"/>
  <text x="500" y="155" text-anchor="middle" class="arrow-text">uses</text>

  <line x1="400" y1="205" x2="400" y2="250" class="arrow" marker-end="url(#arrow)"/>
  <text x="420" y="230" text-anchor="middle" class="arrow-text">publishes</text>
</svg>
```

## Worked Example: Deployment Diagram (SVG body)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
    </marker>
  </defs>

  <text x="450" y="30" text-anchor="middle" class="title">Deployment Diagram — Order Management System</text>

  <!-- Production (AWS) -->
  <rect x="40" y="60" width="580" height="400" rx="8" class="deploy-node"/>
  <text x="330" y="85" text-anchor="middle" class="label">Production — AWS</text>

  <!-- EKS Cluster -->
  <rect x="70" y="110" width="420" height="220" rx="8" class="deploy-node"/>
  <text x="280" y="135" text-anchor="middle" class="label">EKS Cluster (us-east-1)</text>

  <!-- API Gateway container -->
  <rect x="100" y="155" width="130" height="75" rx="8" class="container"/>
  <text x="165" y="183" text-anchor="middle" class="label">API Gateway</text>
  <text x="165" y="201" text-anchor="middle" class="tech">Node.js</text>
  <text x="165" y="218" text-anchor="middle" class="desc">REST API</text>

  <!-- Order Service container -->
  <rect x="260" y="155" width="130" height="75" rx="8" class="container"/>
  <text x="325" y="183" text-anchor="middle" class="label">Order Service</text>
  <text x="325" y="201" text-anchor="middle" class="tech">Python</text>
  <text x="325" y="218" text-anchor="middle" class="desc">Processing</text>

  <!-- Inventory Service container -->
  <rect x="420" y="155" width="130" height="75" rx="8" class="container"/>
  <text x="485" y="183" text-anchor="middle" class="label">Inventory Svc</text>
  <text x="485" y="201" text-anchor="middle" class="tech">Go</text>
  <text x="485" y="218" text-anchor="middle" class="desc">Stock mgmt</text>

  <!-- RDS -->
  <rect x="70" y="370" width="540" height="70" rx="8" class="deploy-node"/>
  <text x="340" y="395" text-anchor="middle" class="label">RDS</text>
  <g>
    <path d="M 280,410 a 50,8 0 1,0 100,0 l 0,20 a 50,8 0 1,1 -100,0 z" class="container"/>
    <ellipse cx="330" cy="410" rx="50" ry="8" class="container"/>
    <text x="330" y="425" text-anchor="middle" class="label">PostgreSQL</text>
  </g>

  <!-- Arrows -->
  <line x1="165" y1="230" x2="325" y2="155" class="arrow" marker-end="url(#arrow)"/>
  <text x="245" y="185" text-anchor="middle" class="arrow-text">routes to</text>

  <line x1="165" y1="230" x2="485" y2="155" class="arrow" marker-end="url(#arrow)"/>
  <text x="325" y="215" text-anchor="middle" class="arrow-text">routes to</text>

  <line x1="325" y1="230" x2="330" y2="395" class="arrow" marker-end="url(#arrow)"/>
  <text x="350" y="320" text-anchor="middle" class="arrow-text">reads/writes</text>
</svg>
```

## Worked Example: Data Flow Diagram (SVG body)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 380">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#455a64"/>
    </marker>
  </defs>

  <text x="450" y="30" text-anchor="middle" class="title">Data Flow — Place Order Use Case</text>

  <!-- Row 1: main flow -->
  <rect x="20" y="80" width="130" height="65" rx="8" class="person"/>
  <text x="85" y="110" text-anchor="middle" class="label">Customer</text>
  <text x="85" y="128" text-anchor="middle" class="desc">Submits order</text>

  <rect x="200" y="80" width="130" height="65" rx="8" class="container"/>
  <text x="265" y="110" text-anchor="middle" class="label">API Gateway</text>
  <text x="265" y="128" text-anchor="middle" class="desc">Validates, routes</text>

  <rect x="380" y="80" width="130" height="65" rx="8" class="container"/>
  <text x="445" y="110" text-anchor="middle" class="label">Order Service</text>
  <text x="445" y="128" text-anchor="middle" class="desc">Creates order</text>

  <rect x="560" y="80" width="130" height="65" rx="8" class="system-ext"/>
  <text x="625" y="110" text-anchor="middle" class="label">Inventory Svc</text>
  <text x="625" y="128" text-anchor="middle" class="desc">Checks stock</text>

  <rect x="740" y="80" width="130" height="65" rx="8" class="system-ext"/>
  <text x="805" y="110" text-anchor="middle" class="label">Payment GW</text>
  <text x="805" y="128" text-anchor="middle" class="desc">Charges card</text>

  <!-- Row 2: async flow -->
  <rect x="380" y="200" width="130" height="65" rx="8" class="queue"/>
  <text x="445" y="230" text-anchor="middle" class="label">Message Queue</text>
  <text x="445" y="248" text-anchor="middle" class="desc">OrderCreated</text>

  <rect x="560" y="200" width="130" height="65" rx="8" class="container"/>
  <text x="625" y="230" text-anchor="middle" class="label">Fulfillment</text>
  <text x="625" y="248" text-anchor="middle" class="desc">Ships order</text>

  <rect x="740" y="200" width="130" height="65" rx="8" class="system-ext"/>
  <text x="805" y="230" text-anchor="middle" class="label">Email Service</text>
  <text x="805" y="248" text-anchor="middle" class="desc">Sends receipt</text>

  <rect x="200" y="290" width="130" height="65" rx="8" class="container"/>
  <text x="265" y="320" text-anchor="middle" class="label">Database</text>
  <text x="265" y="338" text-anchor="middle" class="desc">Persists order</text>

  <!-- Arrows row 1 -->
  <line x1="150" y1="112" x2="200" y2="112" class="arrow" marker-end="url(#arrow)"/>
  <line x1="330" y1="112" x2="380" y2="112" class="arrow" marker-end="url(#arrow)"/>
  <line x1="510" y1="112" x2="560" y2="112" class="arrow" marker-end="url(#arrow)"/>
  <line x1="690" y1="112" x2="740" y2="112" class="arrow" marker-end="url(#arrow)"/>

  <!-- Row 1 → row 2 -->
  <line x1="445" y1="145" x2="445" y2="200" class="arrow" marker-end="url(#arrow)"/>
  <text x="470" y="175" text-anchor="middle" class="arrow-text">publishes</text>

  <!-- Payment return -->
  <line x1="805" y1="145" x2="625" y2="200" class="arrow" marker-end="url(#arrow)"/>
  <text x="730" y="170" text-anchor="middle" class="arrow-text">returns status</text>

  <!-- Row 2 arrows -->
  <line x1="510" y1="232" x2="560" y2="232" class="arrow" marker-end="url(#arrow)"/>
  <text x="535" y="225" text-anchor="middle" class="arrow-text">notifies</text>
  <line x1="690" y1="232" x2="740" y2="232" class="arrow" marker-end="url(#arrow)"/>
  <text x="715" y="225" text-anchor="middle" class="arrow-text">sends</text>

  <!-- To database -->
  <line x1="445" y1="145" x2="330" y2="290" class="arrow" marker-end="url(#arrow)"/>
  <text x="350" y="220" text-anchor="middle" class="arrow-text">persists</text>
</svg>
```

## Best Practices

1. **One level per diagram.** A context diagram with containers crammed in is unreadable. One altitude per diagram.
2. **Use the CSS classes consistently.** `person`, `system`, `system-ext`, `container`, `component`, `deploy-node`, `queue` — each has a distinct color. Don't improvise new colors; the consistency aids reading.
3. **Keep it simple.** Don't cram a 50-microservice system into one diagram. Break into multiple focused diagrams per subsystem.
4. **Annotate with technology.** The `tech` text line on each container/component is where Task 5's technology decisions show up.
5. **Use `system-ext` (dashed border) for external dependencies.** This makes system boundaries explicit — critical for the interface contracts in Task 4.
6. **Every module from Task 3 must appear.** The container/component diagrams are the visual proof that the decomposition is complete.
7. **Test in a browser.** After writing the file, open it in any browser to verify layout. Adjust coordinates if elements overlap.
8. **Use `::preview` in Hermes.** Render diagrams inline in chat with `::preview{file="diagrams/context-diagram.html"}`.
9. **Save each diagram as a separate `.html` file.** One file per diagram type — don't combine multiple diagrams in one file.

## Rendering

Self-contained HTML+CSS+SVG diagrams render in:
- Any web browser (double-click the file)
- Hermes desktop preview pane (`::preview{file="path/to/diagram.html"}`)
- VS Code with HTML preview extension
- Any environment that can display HTML (email, wiki, iframe)
