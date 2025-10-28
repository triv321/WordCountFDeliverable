// Mobile Menu Toggle
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.getElementById('navMenu');

menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Navbar scroll effect
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// Animated Counter for Hero Stats
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;

    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };

    updateCounter();
}

// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            
            // Animate counters when hero stats are visible
            if (entry.target.classList.contains('hero-stats')) {
                const counters = entry.target.querySelectorAll('.stat-number');
                counters.forEach(counter => {
                    if (!counter.classList.contains('animated')) {
                        animateCounter(counter);
                        counter.classList.add('animated');
                    }
                });
            }
        }
    });
}, observerOptions);

// Observe service cards for scroll animation
const serviceCards = document.querySelectorAll('.service-card');
serviceCards.forEach((card, index) => {
    card.classList.add('scroll-reveal');
    card.style.transitionDelay = `${index * 0.1}s`;
    observer.observe(card);
});

// Observe feature items
const featureItems = document.querySelectorAll('.feature-item');
featureItems.forEach((item, index) => {
    item.classList.add('scroll-reveal');
    item.style.transitionDelay = `${index * 0.1}s`;
    observer.observe(item);
});

// Observe specs card
const specsCard = document.querySelector('.specs-card');
if (specsCard) {
    specsCard.classList.add('scroll-reveal');
    observer.observe(specsCard);
}

// Observe hero stats for counter animation
const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
    observer.observe(heroStats);
}

// API Configuration
const API_URL = 'http://localhost:5000';

// Contact Form Handling
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const button = contactForm.querySelector('button[type="submit"]');
        const originalText = button.textContent;
        
        // Disable button during submission
        button.disabled = true;
        button.textContent = 'Sending...';
        
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);
        
        try {
            // Submit to API
            const response = await fetch(`${API_URL}/api/contact`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (result.success) {
                // Show success message
                button.textContent = '✓ Message Sent!';
                button.style.background = 'var(--secondary-color)';
                
                // Reset form
                contactForm.reset();
                
                // Track analytics
                trackAnalytics('contact_form_success', {
                    company: data.company
                });
            } else {
                // Show error message
                button.textContent = '✗ Error: ' + result.error;
                button.style.background = '#ff4444';
            }
        } catch (error) {
            console.error('Form submission error:', error);
            // Fallback to local storage if API is not available
            localStorage.setItem('pending_contact', JSON.stringify(data));
            button.textContent = '✓ Saved Locally';
            button.style.background = '#ffaa00';
            contactForm.reset();
        }
        
        // Reset button after 3 seconds
        setTimeout(() => {
            button.disabled = false;
            button.textContent = originalText;
            button.style.background = '';
        }, 3000);
    });
}

// Track analytics to API
async function trackAnalytics(eventType, eventData) {
    try {
        await fetch(`${API_URL}/api/analytics`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                event_type: eventType,
                event_data: eventData
            })
        });
    } catch (error) {
        console.log('Analytics tracking skipped (API not available)');
    }
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Only prevent default and smooth scroll for on-page anchors
        if (href !== '#' && href !== '#privacy' && href !== '#terms') {
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = target.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Parallax effect for hero background
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    
    if (hero && scrolled < hero.offsetHeight) {
        const circuitPattern = document.querySelector('.circuit-pattern');
        if (circuitPattern) {
            circuitPattern.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    }
});

// Add hover effect to PCB cards
const pcbCards = document.querySelectorAll('.pcb-card');
pcbCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.zIndex = '10';
    });
    
    card.addEventListener('mouseleave', () => {
        setTimeout(() => {
            card.style.zIndex = '';
        }, 300);
    });
});

// Lazy loading for performance
if ('IntersectionObserver' in window) {
    const lazyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                if (element.dataset.src) {
                    element.src = element.dataset.src;
                }
                lazyObserver.unobserve(element);
            }
        });
    });

    document.querySelectorAll('[data-src]').forEach(element => {
        lazyObserver.observe(element);
    });
}

// Add subtle mouse tracking effect to hero section
const hero = document.querySelector('.hero');
const heroVisual = document.querySelector('.hero-visual');

if (hero && heroVisual) {
    hero.addEventListener('mousemove', (e) => {
        const rect = hero.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width;
        const y = (e.clientY - rect.top) / rect.height;
        
        const moveX = (x - 0.5) * 20;
        const moveY = (y - 0.5) * 20;
        
        pcbCards.forEach((card, index) => {
            const depth = (index + 1) * 0.3;
            card.style.transform = `translate(${moveX * depth}px, ${moveY * depth}px)`;
        });
    });
    
    hero.addEventListener('mouseleave', () => {
        pcbCards.forEach(card => {
            card.style.transform = '';
        });
    });
}

// Performance optimization: Throttle scroll events
function throttle(func, wait) {
    let waiting = false;
    return function() {
        if (!waiting) {
            func.apply(this, arguments);
            waiting = true;
            setTimeout(() => {
                waiting = false;
            }, wait);
        }
    };
}

// Apply throttling to scroll handlers
const throttledScrollHandler = throttle(() => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    
    if (hero && scrolled < hero.offsetHeight) {
        const circuitPattern = document.querySelector('.circuit-pattern');
        if (circuitPattern) {
            circuitPattern.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    }
}, 16);

window.addEventListener('scroll', throttledScrollHandler);

// Add active state to navigation links based on scroll position
const sections = document.querySelectorAll('section[id]');

function updateActiveNavLink() {
    const scrollY = window.pageYOffset;
    
    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', throttle(updateActiveNavLink, 100));

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Add entrance animations to elements
    const animatedElements = document.querySelectorAll('.animate-fade-up, .animate-fade-left');
    
    // Trigger animations after a short delay
    setTimeout(() => {
        animatedElements.forEach(element => {
            element.style.opacity = '0';
        });
    }, 100);
    
    // Add loading state
    document.body.classList.add('loaded');
    
    // Track page view
    trackAnalytics('page_view', {
        page: window.location.pathname,
        referrer: document.referrer,
        userAgent: navigator.userAgent
    });
});

// Handle viewport resize for responsive adjustments
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // Close mobile menu on resize to desktop
        if (window.innerWidth > 768) {
            menuToggle.classList.remove('active');
            navMenu.classList.remove('active');
        }
    }, 250);
});

// Prevent animations from running on page load
window.addEventListener('load', () => {
    setTimeout(() => {
        document.body.classList.add('animations-enabled');
    }, 500);
});

// Add pulse animation to CTA buttons
const ctaButtons = document.querySelectorAll('.hero-cta .btn-primary');
ctaButtons.forEach(button => {
    setInterval(() => {
        button.style.animation = 'pulse 0.5s';
        setTimeout(() => {
            button.style.animation = '';
        }, 500);
    }, 5000);
});

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    // Press 'Escape' to close mobile menu
    if (e.key === 'Escape' && navMenu.classList.contains('active')) {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
    }
});

// Track user engagement
let scrollDepth = 0;
window.addEventListener('scroll', throttle(() => {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset;
    const newScrollDepth = Math.round((scrollTop + windowHeight) / documentHeight * 100);
    
    if (newScrollDepth > scrollDepth) {
        scrollDepth = newScrollDepth;
        console.log('Scroll depth:', scrollDepth + '%');
    }
}, 1000));
