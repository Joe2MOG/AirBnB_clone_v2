# Task 5 — AI Dynamic Web Lab Generation for Core CSS Concepts

## Overview

This task demonstrates the use of AI to generate interactive web pages for learning and experimenting with core CSS concepts.

The project contains two interactive HTML labs:

1. **Refined Box Model Lab** — demonstrates the CSS Box Model and the `display` property.
2. **Flexbox and Grid Playground** — demonstrates CSS Flexbox and Grid layout properties.

Both labs use HTML, CSS, and JavaScript in a single HTML file.

---

## Files

### `refined-box-model.html`

An interactive CSS Box Model laboratory.

The page contains:

- **Box 1** and **Box 2**
- Individual **margin** controls for:
  - Top
  - Right
  - Bottom
  - Left
- Individual **padding** controls for:
  - Top
  - Right
  - Bottom
  - Left
- Individual **border-width** controls for:
  - Top
  - Right
  - Bottom
  - Left
- A **width** slider
- A **corner-radius** slider
- A `display` dropdown
- Real-time JavaScript updates

The available `display` values are:

```text
block
inline-block
inline
```

The lab helps demonstrate how content, padding, borders, and margins affect the size and position of an element.

---

### `flexbox-grid-playground.html`

An interactive playground for CSS Flexbox and Grid.

The page contains:

- One **container**
- Five **items** inside the container
- A `display` dropdown
- A `flex-direction` dropdown
- A `justify-content` dropdown
- An `align-items` dropdown
- A `grid-template-columns` dropdown

The available `display` values are:

```text
block
flex
grid
```

---

## Flexbox and Grid Playground — Details

### Container

The container holds five items and is the target of all the CSS property changes controlled by the dropdowns.

### Item Count

There are **five items** inside the container.

### Display Dropdown

The `display` dropdown switches the container between:

```text
block
flex
grid
```

### Flexbox Controls

When the container is set to `flex`, the following controls become useful:

- `flex-direction`
- `justify-content`
- `align-items`

Available `flex-direction` values:

```text
row
row-reverse
column
column-reverse
```

Available `justify-content` values:

```text
flex-start
flex-end
center
space-between
space-around
space-evenly
```

Available `align-items` values:

```text
stretch
flex-start
flex-end
center
baseline
```

### Grid Controls

When the container is set to `grid`, the `grid-template-columns` dropdown becomes useful.

Available `grid-template-columns` values:

```text
none
repeat(1, 1fr)
repeat(2, 1fr)
repeat(3, 1fr)
repeat(4, 1fr)
repeat(5, 1fr)
1fr 2fr
100px 1fr 100px
```

---

## How the Labs Work

Both labs rely on:

- **HTML** for structure
- **CSS** for styling the boxes, container, and items
- **JavaScript** for reading control values and applying them to the elements in real time

No build tools, frameworks, or external libraries are required.

---

## Usage

1. Open either HTML file in a web browser.
2. Adjust the sliders, dropdowns, and inputs.
3. Observe how the layout and element dimensions change in real time.

---



