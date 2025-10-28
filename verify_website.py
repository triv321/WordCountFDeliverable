#!/usr/bin/env python3
"""
Verification script for PCB Pro website requirements.
"""

def verify_website():
    """Verify that the PCB sales website meets all requirements."""
    
    print("=" * 60)
    print("PCB Pro Website Verification")
    print("=" * 60)
    
    results = []
    
    # Check if required files exist
    import os
    
    required_files = ['index.html', 'styles.css', 'script.js']
    print("\n1. Checking required files...")
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"   {status} {file}")
        results.append(exists)
    
    # Check HTML structure
    print("\n2. Checking HTML structure...")
    with open('index.html', 'r') as f:
        html_content = f.read()
        
        required_sections = [
            ('<!DOCTYPE html>', 'DOCTYPE declaration'),
            ('<meta name="viewport"', 'Responsive viewport meta tag'),
            ('class="navbar"', 'Navigation bar'),
            ('class="hero"', 'Hero section'),
            ('class="services"', 'Services section'),
            ('class="features"', 'Features section'),
            ('class="contact"', 'Contact section'),
            ('class="footer"', 'Footer'),
        ]
        
        for pattern, description in required_sections:
            exists = pattern in html_content
            status = "✓" if exists else "✗"
            print(f"   {status} {description}")
            results.append(exists)
    
    # Check CSS features
    print("\n3. Checking CSS features...")
    with open('styles.css', 'r') as f:
        css_content = f.read()
        
        css_features = [
            ('@media', 'Responsive breakpoints'),
            ('animation:', 'CSS animations'),
            ('transition:', 'Smooth transitions'),
            (':hover', 'Hover effects'),
            ('grid', 'CSS Grid layout'),
            ('flex', 'Flexbox layout'),
            ('@keyframes', 'Keyframe animations'),
        ]
        
        for pattern, description in css_features:
            exists = pattern in css_content
            status = "✓" if exists else "✗"
            print(f"   {status} {description}")
            results.append(exists)
    
    # Check JavaScript functionality
    print("\n4. Checking JavaScript functionality...")
    with open('script.js', 'r') as f:
        js_content = f.read()
        
        js_features = [
            ('addEventListener', 'Event listeners'),
            ('IntersectionObserver', 'Scroll animations'),
            ('querySelector', 'DOM manipulation'),
            ('throttle', 'Performance optimization'),
            ('animateCounter', 'Counter animation'),
            ('scroll', 'Scroll handling'),
        ]
        
        for pattern, description in js_features:
            exists = pattern in js_content
            status = "✓" if exists else "✗"
            print(f"   {status} {description}")
            results.append(exists)
    
    # Check responsive design
    print("\n5. Checking responsive design features...")
    responsive_features = [
        ('@media (max-width: 768px)', 'Mobile breakpoint'),
        ('@media (max-width: 968px)', 'Tablet breakpoint'),
        ('@media (max-width: 480px)', 'Small mobile breakpoint'),
        ('menu-toggle', 'Mobile menu'),
    ]
    
    for pattern, description in responsive_features:
        exists = pattern in css_content
        status = "✓" if exists else "✗"
        print(f"   {status} {description}")
        results.append(exists)
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    percentage = (passed / total) * 100
    
    print(f"Results: {passed}/{total} checks passed ({percentage:.1f}%)")
    
    if percentage == 100:
        print("✓ All requirements met!")
    elif percentage >= 90:
        print("⚠ Most requirements met, minor issues detected")
    else:
        print("✗ Some requirements not met")
    
    print("=" * 60)
    
    return percentage == 100

if __name__ == '__main__':
    import sys
    success = verify_website()
    sys.exit(0 if success else 1)
