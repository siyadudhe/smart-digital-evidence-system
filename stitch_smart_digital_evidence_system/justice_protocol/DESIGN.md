---
name: Justice Protocol
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#331200'
  on-tertiary-container: '#cf6721'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#ffdbca'
  tertiary-fixed-dim: '#ffb68e'
  on-tertiary-fixed: '#331200'
  on-tertiary-fixed-variant: '#763300'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Public Sans
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  gutter-md: 24px
  margin-page: 32px
  container-max: 1440px
  sidebar-width: 280px
---

## Brand & Style

The design system is engineered for the high-stakes environment of digital forensics and law enforcement. The brand personality is **authoritative, meticulous, and impenetrable**. It prioritizes cognitive clarity over decorative flair, ensuring that investigators can navigate complex datasets without fatigue.

The design style follows a **Modern Corporate** aesthetic with **Minimalist** influences. It utilizes a structured "Information First" hierarchy, characterized by:
- **Functional Density:** Optimized for data-heavy dashboard views common in evidence management.
- **Visual Integrity:** A focus on alignment and grid-based layouts to convey order and legal compliance.
- **Restrained Interaction:** Micro-interactions are purposeful and subtle, providing confirmation of high-consequence actions (like evidence locking or deletion) without distraction.

## Colors

The palette is anchored in **Dark Navy Blue** to establish an immediate sense of institutional security and trust. **Charcoal Grey** serves as the functional secondary tone for secondary navigation and utility elements.

- **Primary (Navy):** Used for primary actions, sidebar backgrounds, and headers to anchor the UI.
- **Secondary (Charcoal):** Applied to supporting text, borders, and icon states.
- **Background (Light Grey):** A soft `#F8FAFC` prevents eye strain during long shifts while providing enough contrast against white cards.
- **Accents (Gold/Red):** Gold is reserved for "Authority" actions and high-priority case markers. Red is strictly utilized for "Destructive" actions, critical alerts, and chain-of-custody violations.

## Typography

The design system utilizes **Public Sans**, an institutional-grade typeface designed for clarity and neutrality. It provides the legibility required for dense evidentiary reports and tabular data.

- **Headlines:** Use tight letter spacing and heavy weights to denote section starts.
- **Body:** Standardized at 14px for data density; 16px is reserved for long-form case notes.
- **Labels:** Uppercase labels with slight letter-spacing are used for metadata headers (e.g., "CASE ID", "TIMESTAMP") to differentiate them from user-generated content.

## Layout & Spacing

This design system employs a **Fixed-Fluid Hybrid Grid**. The primary sidebar navigation is fixed at 280px, while the main content area utilizes a 12-column fluid grid that caps at 1440px to prevent excessive line lengths in data tables.

- **Spacing Rhythm:** Based on a 4px baseline. Most components use 16px or 24px padding.
- **Mobile Adaptation:** At the 768px breakpoint, the sidebar collapses into a hamburger menu or bottom navigation, and page margins reduce to 16px.
- **Data Density:** In "Table View," vertical padding is reduced to 8px to maximize the visibility of evidence logs.

## Elevation & Depth

To maintain a serious, professional tone, depth is conveyed through **Tonal Layers** supplemented by **Ambient Shadows**.

- **Surface Levels:** The background is the lowest level. Content cards sit on top, rendered in pure white with a 1px border (`#E2E8F0`).
- **Shadow Character:** Shadows are extremely subtle—high blur (12px-20px) and low opacity (4-6%). They should appear as a soft glow rather than a harsh drop shadow.
- **Interaction Depth:** On hover, cards may lift slightly (increase shadow spread) to indicate interactivity, but modal overlays are the only elements allowed to use significant elevation to focus user attention during evidence submission.

## Shapes

The shape language is **Balanced and Approachable**. A 0.5rem (8px) corner radius is applied to all primary UI elements, including buttons, input fields, and cards. This softens the "institutional" feel without appearing overly casual or playful.

- **Standard (8px):** Primary containers and buttons.
- **Large (16px):** Main dashboard cards and modal containers.
- **Full (Pill):** Used exclusively for status badges (e.g., "Active," "Closed," "Pending") to differentiate them from actionable buttons.

## Components

### Buttons & Inputs
- **Buttons:** Solid navy for primary actions. Ghost buttons (navy border, transparent fill) for secondary actions. Icons should always accompany text in primary actions to ensure clarity.
- **Inputs:** White backgrounds with a subtle 1px border. Focus states use a 2px navy ring. Leading icons are mandatory for search and date-picker fields.

### Evidence Cards
- Cards must include a header section with a `label-md` category and a status badge. 
- High-priority cards (urgent cases) feature a 4px left-border accent in **Gold**.

### Tables & Lists
- **Structured Tables:** Use zebra-striping with the neutral background color for readability. The header row is pinned and uses a slightly darker tint of the neutral color.
- **Badges:** Small, pill-shaped indicators. "Evidence Secured" uses green; "Missing Documentation" uses gold; "Flagged" uses red.

### Navigation
- **Sidebar:** Dark navy background with high-contrast white text. Active states use a subtle "left-indicator" bar and a slight background highlight.
- **Breadcrumbs:** Required on all sub-pages to maintain the user's sense of location within deep case hierarchies.