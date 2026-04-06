# Club Bar Website - Setup Guide

## Overview
This is a complete WordPress theme and plugin setup for a modern club/bar website featuring:
- Hero video/banner section
- About us section
- Upcoming events listing
- Event reservations system
- DJ management
- Responsive design

## Project Structure

```
club-bar-website/
├── wp-content/
│   ├── themes/
│   │   └── club-bar-theme/
│   │       ├── style.css           # Theme styles
│   │       ├── functions.php       # Theme functions
│   │       ├── header.php          # Header template
│   │       ├── footer.php          # Footer template
│   │       ├── index.php           # Default template
│   │       ├── front-page.php      # Home page template
│   │       └── js/
│   │           └── main.js         # JavaScript functionality
│   └── plugins/
│       └── club-events/
│           └── club-events.php     # Reservations plugin
```

## Installation

1. **Copy project files** to your WordPress installation
2. **Activate the theme:**
   - Go to WordPress Admin → Appearance → Themes
   - Activate "Club Bar Theme"

3. **Activate the plugin:**
   - Go to WordPress Admin → Plugins
   - Activate "Club Events & Reservations"

## Creating Content

### 1. Set Up Hero Video
- Upload a video file (mp4, webm format recommended)
- Replace the video source in `front-page.php` line for the `<video>` tag
- Example: `<source src="<?php echo get_template_directory_uri(); ?>/assets/your-video.mp4">`

### 2. Create Events
- Go to WordPress Admin → Events → Add New
- Fill in event details:
  - **Title:** Event name
  - **Content:** Event description
  - **Meta Fields (Custom Fields):**
    - `event_date`: Date and time of event
    - `dj_name`: Name of performing DJ

### 3. Create DJ Profiles
- Go to WordPress Admin → DJs → Add New
- Add DJ information and profile image

### 4. Set Home Page
- Go to WordPress Admin → Settings → Reading
- Select "A static page"
- Set "Homepage" to a page using the "Front Page" template

### 5. Create Navigation Menu
- Go to WordPress Admin → Appearance → Menus
- Create a new menu with links to:
  - Home
  - Events
  - About
  - Contact
- Set as "Primary Menu"

## Theme Colors

Edit the CSS variables in `style.css`:

```css
:root {
  --primary-color: #ff006e;      /* Pink/Magenta */
  --secondary-color: #1a1a1a;    /* Dark background */
  --accent-color: #00d9ff;       /* Cyan */
  --light-text: #ffffff;         /* White */
  --dark-text: #1a1a1a;          /* Dark */
}
```

## Features

### Hero Section
- Fullscreen video background
- Call-to-action button
- Smooth animations

### Events Grid
- Responsive card layout
- Event date and DJ information
- Quick reservation buttons
- Smooth hover effects

### Reservation System
- Integrated booking form
- Form validation
- Email confirmations
- Admin panel to view reservations

### Responsive Design
- Mobile-friendly
- Adapts to all screen sizes
- Touch-friendly buttons and forms

## Customization

### Change Color Scheme
Edit the CSS variables in `wp-content/themes/club-bar-theme/style.css`

### Add New Sections
1. Edit `front-page.php`
2. Add HTML structure
3. Add corresponding CSS in `style.css`

### Add More Custom Fields
Edit `functions.php` and use WordPress Meta API:
```php
$value = get_post_meta( post_id, 'field_name', true );
```

## Plugins Recommended

- **WP Mail SMTP** - For reliable email delivery
- **Contact Form 7** - For additional forms
- **Elementor** - For page building
- **Yoast SEO** - For search optimization
- **WooCommerce** - For selling tickets

## Support & Maintenance

- Keep WordPress and plugins updated
- Regular backups
- Monitor security
- Update content regularly

## Notes

- Replace placeholder images and videos with your own
- Customize event dates and DJ information
- Update club contact information in footer
- Test responsiveness on mobile devices

