# PCB Pro - Professional PCB Sales Website

A responsive, minimal, and clean UI for a website that sells PCB designs to B2B customers.

## Features

- **Responsive Design**: Mobile-first approach that works seamlessly across all device sizes (320px to 1920px+)
- **Hero Section**: Eye-catching hero with compelling headline, animated statistics, and 3D PCB card showcase
- **Smooth Animations**: Professional animations including fade-ins, parallax effects, and hover interactions
- **Clean Design**: Minimalist UI with plenty of white space and a professional color scheme
- **B2B Focus**: Professional tone and design elements appropriate for business customers

## Technical Implementation

### Technologies Used
- **HTML5**: Semantic markup for improved accessibility and SEO
- **CSS3**: Modern styling with CSS Grid, Flexbox, and custom animations
- **Vanilla JavaScript**: No dependencies, fast load times, and optimized performance

### Key Features

#### 1. Navigation
- Fixed navigation bar with blur effect
- Mobile-responsive hamburger menu
- Smooth scroll to sections
- Active link highlighting based on scroll position

#### 2. Hero Section
- Animated background with circuit pattern
- Fade-up animations for content reveal
- Animated statistics counter
- 3D PCB card showcase with float animations
- Mouse tracking parallax effect
- Scroll indicator

#### 3. Services Section
- Grid layout with service cards
- Hover effects with elevation
- Icon animations
- Scroll-triggered fade-in animations

#### 4. Features Section
- Two-column layout with feature list and specifications
- Technical specifications card
- Staggered reveal animations

#### 5. Contact Section
- Contact form with validation
- Contact information display
- Form submission feedback

#### 6. Footer
- Branding and copyright information
- Quick links
- Responsive layout

## File Structure

```
.
├── index.html          # Main HTML structure
├── styles.css          # All styling and animations
├── script.js           # Interactive functionality
└── PCB_WEBSITE_README.md   # This file
```

## Usage

### Viewing the Website

Simply open `index.html` in a modern web browser. No build process or server required.

```bash
# Open directly in browser
open index.html

# Or use a local server for development
python3 -m http.server 8000
# Then visit http://localhost:8000
```

### Customization

#### Colors
Edit the CSS custom properties in `styles.css`:

```css
:root {
    --primary-color: #0066FF;
    --secondary-color: #00FF88;
    --text-primary: #1A1A1A;
    /* ... other colors ... */
}
```

#### Content
Update the HTML content in `index.html`:
- Modify headlines and descriptions
- Update contact information
- Change service offerings
- Add or remove sections

#### Animations
Adjust animation timing in `styles.css`:

```css
--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
```

## Responsive Breakpoints

- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Optimizations

- **Throttled scroll events**: Reduces CPU usage during scrolling
- **Intersection Observer API**: Efficient scroll-triggered animations
- **CSS animations over JavaScript**: Hardware-accelerated animations
- **Will-change property**: Optimizes animation performance
- **Reduced motion support**: Respects user accessibility preferences

## Accessibility

- Semantic HTML5 elements
- ARIA labels for interactive elements
- Keyboard navigation support
- Focus states for all interactive elements
- Reduced motion media query support

## Future Enhancements

Consider adding:
- Image optimization and lazy loading for actual PCB images
- Backend integration for form submission
- Blog or case studies section
- Customer testimonials
- Product catalog with filtering
- Live chat support
- Multi-language support

## License

This project is part of the PCB Pro sales platform.

## Credits

Designed and developed for professional B2B PCB sales.
