// Main JavaScript: Interactions, Filtering, Video Control & AJAX
document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic copyright year
    const yearElem = document.getElementById('current-year');
    if (yearElem) {
        yearElem.textContent = new Date().getFullYear();
    }

    // Header transparent-to-scrolled state
    const siteHeader = document.querySelector('.site-header');
    if (siteHeader) {
        const checkScroll = () => {
            if (window.scrollY > 40) {
                siteHeader.classList.add('scrolled');
            } else {
                siteHeader.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', checkScroll, { passive: true });
        checkScroll();
    }

    // 2. Ensure Background Video Autoplays
    const video = document.getElementById('hero-bg-video');
    if (video) {
        video.play().catch(() => {
            // Autoplay policy fallback: muted is already set on the element
        });
    }

    // 3. Mobile Navigation Menu Toggle
    const mobileToggle = document.getElementById('mobile-toggle');
    const navLinks = document.getElementById('nav-links');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            navLinks.classList.toggle('active');
            const expanded = navLinks.classList.contains('active');
            mobileToggle.setAttribute('aria-expanded', expanded.toString());
        });

        // Close on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!navLinks.contains(e.target) && !mobileToggle.contains(e.target) && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // 4. Project Category Filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card-clean');

    if (filterButtons.length && projectCards.length) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.getAttribute('data-filter');

                projectCards.forEach(card => {
                    const cardCat = card.getAttribute('data-category');
                    if (filter === 'all' || cardCat === filter) {
                        card.style.display = 'flex';
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(10px)';
                        requestAnimationFrame(() => {
                            card.style.transition = 'all 0.3s ease';
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        });
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // 5. Contact Form Validation & AJAX Submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        const submitBtn = document.getElementById('submit-btn');
        const formInputs = contactForm.querySelectorAll('input, textarea');

        formInputs.forEach(input => {
            input.addEventListener('input', () => validateField(input));
            input.addEventListener('blur', () => validateField(input));
        });

        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            let isValid = true;
            formInputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });

            if (!isValid) return;

            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());

            if (submitBtn) {
                const originalHtml = submitBtn.innerHTML;
                submitBtn.disabled = true;
                submitBtn.innerHTML = `<span>Transmitting...</span>`;

                try {
                    const response = await fetch('/api/contact', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify(data)
                    });

                    const result = await response.json().catch(() => ({}));

                    if (response.ok && (result.success || result.message)) {
                        showNotification(result.message || 'Message received! Pratyush will follow up shortly.', 'success');
                        contactForm.reset();
                        formInputs.forEach(input => input.classList.remove('valid', 'invalid'));
                    } else {
                        showNotification(result.error || 'Unable to transmit message. Please try again.', 'error');
                    }
                } catch (err) {
                    console.error('Contact error:', err);
                    showNotification('Network connection error. Please try again.', 'error');
                } finally {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalHtml;
                }
            }
        });
    }
});

// Helper: Real-time Field Validation
function validateField(input) {
    let valid = true;
    const value = input.value.trim();
    const errorMsg = input.parentElement.querySelector('.error-message');

    if (input.id === 'name') {
        valid = value.length >= 2;
    } else if (input.id === 'email') {
        const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        valid = emailRe.test(value);
    } else if (input.id === 'message') {
        valid = value.length >= 10;
    } else if (input.hasAttribute('required')) {
        valid = value.length > 0;
    }

    if (valid) {
        input.classList.remove('invalid');
        input.classList.add('valid');
        if (errorMsg) errorMsg.style.display = 'none';
    } else {
        input.classList.remove('valid');
        input.classList.add('invalid');
        if (errorMsg) errorMsg.style.display = 'block';
    }

    return valid;
}

// Helper: Toast Notifications
function showNotification(message, type = 'success') {
    const existing = document.querySelector('.notification');
    if (existing) existing.remove();

    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    document.body.appendChild(notification);

    requestAnimationFrame(() => {
        notification.classList.add('show');
    });

    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 350);
    }, 4500);
}
