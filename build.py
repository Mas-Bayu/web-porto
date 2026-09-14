#!/usr/bin/env python3
"""Build the portfolio HTML file."""

head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Byu's | Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'dark-burgundy': '#2D0B0B',
                        'surface-burgundy': '#421212',
                        'border-burgundy': '#7A2828',
                        'warm-cream': '#FFF0DD',
                        'muted-rose': '#E8B8B8',
                        'coral-rose': '#E57373',
                        'crimson-red': '#CD4646',
                        'deep-maroon': '#7A2828',
                    },
                    fontFamily: {
                        'display': ['Playfair Display', 'serif'],
                        'body': ['Inter', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style>
        html { scroll-behavior: smooth; }
        body { font-family: 'Inter', sans-serif; background-color: #2D0B0B; color: #FFF0DD; }
        .gradient-text { background: linear-gradient(135deg, #E57373 0%, #CD4646 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .card-glow { transition: all 0.3s ease; }
        .card-glow:hover { box-shadow: 0 0 30px rgba(229, 115, 115, 0.3); transform: translateY(-5px); }
        .btn-glow { transition: all 0.3s ease; position: relative; overflow: hidden; }
        .btn-glow::before { content: ''; position: absolute; top: 0; left: -200%; width: 200%; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent); transition: left 0.5s ease; }
        .btn-glow:hover::before { left: 100%; }
        .skill-badge { transition: all 0.2s ease; }
        .skill-badge:hover { transform: scale(1.05); }
        .project-card-header { background: linear-gradient(135deg, #E57373 0%, #CD4646 100%); }
        .project-card-header:hover { background: linear-gradient(135deg, #CD4646 0%, #E57373 100%); }
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } }
        .animate-float { animation: float 3s ease-in-out infinite; }
        .nav-link { position: relative; }
        .nav-link::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -8px; left: 0; background-color: #E57373; transition: width 0.3s ease; }
        .nav-link:hover::after { width: 100%; }
    </style>
</head>
<body class="bg dark-burgundy min-h-screen">
"""

navbar = """
    <!-- Navigation Bar -->
    <nav id="navbar" class="fixed top-0 w-full z-50 bg-dark-burgundy/90 backdrop-blur-sm transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 py-3 sm:px-6">
            <div class="flex items-center justify-between">
                <a href="#" class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-full bg-coral-rose flex items-center justify-center">
                        <span class="text-warm-cream font-display font-bold text-lg">DD</span>
                    </div>
                    <span class="ml-2 text-warm-cream font-display font-semibold text-xl hidden sm:block">Developer</span>
                </a>

                <div class="hidden md:flex items-center gap-8">
                    <a href="#about" class="nav-link text-muted-rose hover:text-warm-cream transition-colors duration-200">About</a>
                    <a href="#skills" class="nav-link text-muted-rose hover:text-warm-cream transition-colors duration-200">Skills</a>
                    <a href="#projects" class="nav-link text-muted-rose hover:text-warm-cream transition-colors duration-200">Projects</a>
                    <a href="#contact" class="nav-link text-muted-rose hover:text-warm-cream transition-colors duration-200">Contact</a>
                </div>

                <a href="#contact" class="hidden md:inline-flex btn-glow px-6 py-2.5 bg-coral-rose text-warm-cream font-semibold rounded-full hover:bg-crimson-red transition-colors duration-200">Hire Me</a>

                <button id="mobile-menu-btn" class="md:hidden p-2 rounded-full text-warm-cream hover:bg-surface-burgundy transition-colors" aria-label="Toggle menu">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h20M4 12h20M4 18h20" />
                    </svg>
                </button>
            </div>
        </div>

        <div id="mobile-menu" class="md:hidden fixed inset-0 w-full h-full bg-dark-burgundy z-40 flex-col items-center justify-center gap-6 px-8 transition-all duration-300 hidden">
            <a href="#about" class="text-muted-rose hover:text-warm-cream text-lg font-semibold transition-colors mobile-nav-link">About</a>
            <a href="#skills" class="text-muted-rose hover:text-warm-cream text-lg font-semibold transition-colors mobile-nav-link">Skills</a>
            <a href="#projects" class="text-muted-rose hover:text-warm-cream text-lg font-semibold transition-colors mobile-nav-link">Projects</a>
            <a href="#contact" class="text-muted-rose hover:text-warm-cream text-lg font-semibold transition-colors mobile-nav-link">Contact</a>
            <a href="#contact" class="btn-glow px-8 py-3 bg-coral-rose text-warm-cream font-semibold rounded-full hover:bg-crimson-red transition-colors mobile-nav-link">Hire Me</a>
        </div>
    </nav>
"""

hero = """
    <!-- Hero Section -->
    <section id="hero" class="min-h-screen flex items-center justify-center px-6 sm:px-2 pt-20 md:pt-0 bg-surface-burgundy/50">
        <div class="max-w-4xl text-center">
            <div class="flex justify-center gap-4 mb-8">
                <a href="#" class="w-10 h-10 rounded-full bg-surface-burgundy flex items-center justify-center text-coral-rose hover:bg-coral-rose hover:text-warm-cream transition-all duration-200"><i class="fab fa-github"></i></a>
                <a href="#" class="w-10 h-10 rounded-full bg-surface-burgundy flex items-center justify-center text-coral-rose hover:bg-coral-rose hover:text-warm-cream transition-all duration-200"><i class="fab fa-linkedin-in"></i></a>
                <a href="#" class="w-10 h-10 rounded-full bg-surface-burgundy flex items-center justify-center text-coral-rose hover:bg-coral-rose hover:text-warm-cream transition-all duration-200"><i class="fab fa-twitter"></i></a>
                <a href="#" class="w-10 h-10 rounded-full bg-surface-burgundy flex items-center justify-center text-coral-rose hover:bg-coral-rose hover:text-warm-cream transition-all duration-200"><i class="fab fa-dribbble"></i></a>
            </div>
            <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-bold text-warm-cream mb-6 leading-tight">
                Hi. I'm a <span class="gradient-text">Uni Student at University of The People</span>.<br>
                I've Been Building <br class="sm:hidden">
                <span class="gradient-text">Projects to gain Experience</span> That Matter.
            </h1>
            <p class="text-muted-rose text-lg sm:text-xl mb-10 max-w-2xl mx-auto">
                I'm passionate at creating projects that would give me experiences in the world of IT/Web Development.
            </p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mt-8">
                <a href="#projects" class="btn-glow px-8 py-4 bg-coral-rose text-warm-cream font-semibold rounded-full hover:bg-crimson-red transition-colors duration-200">
                    <i class="far fa-eye mr-2"></i> View Work
                </a>
                <a href="#contact" class="btn-glow px-8 py-4 bg-surface-burgundy text-warm-cream font-semibold rounded-full border-2 border-coral-rose hover:bg-coral-rose transition-colors duration-200">
                    <i class="far fa-envelope mr-2"></i> Get in Touch
                </a>
            </div>
        </div>
    </section>
"""

about = """
    <!-- About Section -->
    <section id="about" class="py-20 px-6 sm:px-2 bg-surface-burgundy/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-warm-cream mb-4">About Me</h2>
                <div class="w-24 h-1 bg-coral-rose mx-auto rounded-full"></div>
            </div>
            <div class="grid md:grid-cols-2 gap-12 items-center mb-20">
                <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-8 card-glow">
                    <h3 class="font-display text-2xl font-semibold text-warm-cream mb-4">Who I Am</h3>
                    <p class="text-muted-rose leading-relaxed mb-4">I'm a junior programmer that just started to step inside the IT industries to begin my journey as a full-fledge developer. Over the last few months, I've been learning online on how to code using react and python by myself, transitioning from understanding the concepts, learning how to type syntax to actually building projects with the programming language I've learned.</p>
                    <p class="text-muted-rose leading-relaxed">At University of The People, I'm currently taking computer science as my major. I haven't really started any courses at my Uni just yet, but I'm taking an early step by learning programming languages outside of my college schedules to get a headstart from everyone in my class.</p>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-6 text-center card-glow">
                        <div class="text-4xl font-bold gradient-text mb-2">3+</div>
                        <div class="text-muted-rose text-sm">Months Experience</div>
                    </div>
                    <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-6 text-center card-glow">
                        <div class="text-4xl font-bold gradient-text mb-2">3+</div>
                        <div class="text-muted-rose text-sm">Projects Completed</div>
                    </div>
                    <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-6 text-center card-glow">
                        <div class="text-4xl font-bold gradient-text mb-2">30+</div>
                        <div class="text-muted-rose text-sm">Happy Clients</div>
                    </div>
                    <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-6 text-center card-glow">
                        <div class="text-4xl font-bold gradient-text mb-2">100%</div>
                        <div class="text-muted-rose text-sm">Commitment</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

skills = """
    <!-- Skills Section -->
    <section id="skills" class="py-20 px-6 sm:px-2 bg-surface-burgundy/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-warm-cream mb-4">My Skills</h2>
                <div class="w-24 h-1 bg-coral-rose mx-auto rounded-full"></div>
                <p class="text-muted-rose mt-4 max-w-2xl mx-auto">Technologies and tools I work with to bring ideas to life</p>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
"""

skill_items = [
    ("fa-html5", "HTML5"),
    ("fa-css3-alt", "CSS3"),
    ("fa-js-square", "JavaScript"),
    ("fa-react", "React"),
    ("fa-vuejs", "Vue.js"),
    ("fa-node-js", "Node.js"),
    ("fa-git-alt", "Git"),
    ("fa-figma", "Figma"),
    ("fa-sass", "SASS"),
    ("fa-bootstrap", "Bootstrap"),
]

for icon, name in skill_items:
    skills += f"""
                <div class="skill-badge bg-surface-burgundy border border-border-burgundy rounded-xl p-4 flex flex-col items-center gap-3 card-glow">
                    <div class="w-12 h-12 rounded-lg bg-dark-burgundy flex items-center justify-center">
                        <i class="fab {icon} text-2xl text-coral-rose"></i>
                    </div>
                    <span class="text-muted-rose text-sm font-medium">{name}</span>
                </div>
"""

# Tailwind SVG icon
skills += """
                <div class="skill-badge bg-surface-burgundy border border-border-burgundy rounded-xl p-4 flex flex-col items-center gap-3 card-glow">
                    <div class="w-12 h-12 rounded-lg bg-dark-burgundy flex items-center justify-center">
                        <svg class="w-6 h-6 text-coral-rose" viewBox="0 0 24 24" fill="currentColor"><path d="M12.001,4.8c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 C13.666,10.618,15.027,12,18.001,12c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C16.337,6.182,14.976,4.8,12.001,4.8z M6.001,12c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 c1.177,1.194,2.538,2.576,5.512,2.576c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C10.337,13.382,8.976,12,6.001,12z"/></svg>
                    </div>
                    <span class="text-muted-rose text-sm font-medium">Tailwind</span>
                </div>
                <div class="skill-badge bg-surface-burgundy border border-border-burgundy rounded-xl p-4 flex flex-col items-center gap-3 card-glow">
                    <div class="w-12 h-12 rounded-lg bg-dark-burgundy flex items-center justify-center">
                        <span class="text-coral-rose font-bold text-lg">TS</span>
                    </div>
                    <span class="text-muted-rose text-sm font-medium">TypeScript</span>
                </div>
            </div>
        </div>
    </section>
"""

projects_data = [
    ("Business Web", '<i class="fas fa-globe text-4xl text-warm-cream animate-float"></i>', "PT. Singaman Power Export", "A single landing page website for a local business of P3Mi that is officially listed in the database of BP2MI.", ["HTML", "CSS", "Tailwind"]),
    ("Music Player", '<i class="fas fa-headphones text-4xl text-warm-cream animate-float"></i>', "Music Player", "A simple music/audio player with a few features that only plays curtain songs that is available inside the project file.", ["JavaScript", "HTML", "CSS"]),
    ("Pokemon Index", '<svg class="w-12 h-12 text-warm-cream animate-float" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="5" aria-label="Poké Ball icon" role="img"><circle cx="32" cy="32" r="26"/><path d="M6 32h52"/><circle cx="32" cy="32" r="9"/></svg>', "Pokemon Index", "An index of old generation pokemons that can be searched by name of the pokemon in the old generations of pokemons.", ["React", "Vite"]),
]

projects = """
    <!-- Projects Section -->
    <section id="projects" class="py-20 px-6 sm:px-2 bg-surface-burgundy/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-warm-cream mb-4">My Projects</h2>
                <div class="w-24 h-1 bg-coral-rose mx-auto rounded-full"></div>
                <p class="text-muted-rose mt-4 max-w-2xl mx-auto">A selection of projects that showcase my skills and passion for web development</p>
            </div>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
"""

for badge, icon_html, title, desc, tags in projects_data:
    tags_html = "".join(f'<span class="bg-dark-burgundy text-muted-rose text-xs px-3 py-1 rounded-full">{t}</span>' for t in tags)
    projects += f"""
                <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl overflow-hidden card-glow">
                    <div class="project-card-header p-6 relative transition-all duration-300">
                        <div class="absolute top-4 left-4">
                            <span class="bg-dark-burgundy/80 text-coral-rose text-xs font-semibold px-3 py-1 rounded-full">{badge}</span>
                        </div>
                        <div class="flex items-center justify-center h-24">
                            {icon_html}
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-warm-cream font-semibold text-xl mb-2">{title}</h3>
                        <p class="text-muted-rose text-sm mb-4">{desc}</p>
                        <div class="flex flex-wrap gap-2 mb-4">{tags_html}</div>
                        <div class="flex gap-3">
                            <a href="#" class="btn-glow flex-1 text-center py-2 bg-coral-rose text-warm-cream text-sm font-medium rounded-lg hover:bg-crimson-red transition-colors">
                                <i class="fas fa-external-link-alt mr-1"></i> Live Demo
                            </a>
                            <a href="#" class="btn-glow flex-1 text-center py-2 bg-dark-burgundy border border-border-burgundy text-muted-rose text-sm font-medium rounded-lg hover:bg-surface-burgundy hover:text-warm-cream transition-colors">
                                <i class="fab fa-github mr-1"></i> GitHub
                            </a>
                        </div>
                    </div>
                </div>
"""

projects += """
            </div>
        </div>
    </section>
"""

contact = """
    <!-- Contact Section -->
    <section id="contact" class="py-20 px-6 sm:px-2 bg-surface-burgundy/50">
        <div class="max-w-4xl mx-auto text-center">
            <div class="mb-12">
                <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-warm-cream mb-4">Let's Work Together</h2>
                <div class="w-24 h-1 bg-coral-rose mx-auto rounded-full"></div>
                <p class="text-muted-rose mt-6 text-lg max-w-xl mx-auto">Have a project in mind? I'd love to hear about it. Let's discuss how we can bring your ideas to life.</p>
            </div>
            <div class="bg-surface-burgundy border border-border-burgundy rounded-2xl p-8 sm:p-12 card-glow">
                <div class="grid sm:grid-cols-2 gap-6 mb-8">
                    <div class="flex items-center gap-4 p-4 bg-dark-burgundy rounded-xl">
                        <div class="w-12 h-12 rounded-full bg-coral-rose flex items-center justify-center flex-shrink-0">
                            <i class="fas fa-envelope text-warm-cream"></i>
                        </div>
                        <div class="text-left">
                            <div class="text-muted-rose text-sm">Email</div>
                            <div class="text-warm-cream font-medium">hello@developer.com</div>
                        </div>
                    </div>
                    <div class="flex items-center gap-4 p-4 bg-dark-burgundy rounded-xl">
                        <div class="w-12 h-12 rounded-full bg-coral-rose flex items-center justify-center flex-shrink-0">
                            <i class="fas fa-map-marker-alt text-warm-cream"></i>
                        </div>
                        <div class="text-left">
                            <div class="text-muted-rose text-sm">Location</div>
                            <div class="text-warm-cream font-medium">San Francisco, CA</div>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="mailto:hello@developer.com" class="btn-glow px-8 py-4 bg-coral-rose text-warm-cream font-semibold rounded-full hover:bg-crimson-red transition-colors duration-200 inline-flex items-center justify-center">
                        <i class="far fa-paper-plane mr-2"></i> Send Message
                    </a>
                    <a href="#" class="btn-glow px-8 py-4 bg-dark-burgundy border border-border-burgundy text-muted-rose font-semibold rounded-full hover:bg-surface-burgundy hover:text-warm-cream transition-colors duration-200 inline-flex items-center justify-center">
                        <i class="fas fa-file-download mr-2"></i> Download CV
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

footer = """
    <!-- Footer -->
    <footer class="py-8 px-6 border-t border-border-burgundy">
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="text-muted-rose text-sm">
                &copy; 2024 Developer. All rights reserved.
            </div>
            <div class="flex gap-4">
                <a href="#" class="w-8 h-8 rounded-full bg-surface-burgundy flex items-center justify-center text-muted-rose hover:text-coral-rose hover:bg-dark-burgundy transition-all"><i class="fab fa-github text-sm"></i></a>
                <a href="#" class="w-8 h-8 rounded-full bg-surface-burgundy flex items-center justify-center text-muted-rose hover:text-coral-rose hover:bg-dark-burgundy transition-all"><i class="fab fa-linkedin-in text-sm"></i></a>
                <a href="#" class="w-8 h-8 rounded-full bg-surface-burgundy flex items-center justify-center text-muted-rose hover:text-coral-rose hover:bg-dark-burgundy transition-all"><i class="fab fa-twitter text-sm"></i></a>
            </div>
        </div>
    </footer>
"""

script = """
    <script>
        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('flex');
        });

        // Close mobile menu when clicking a link
        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenu.classList.remove('flex');
            });
        });

        // Navbar scroll effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-lg');
            } else {
                navbar.classList.remove('shadow-lg');
            }
        });

        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.card-glow, .skill-badge').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>
"""

# Build the complete HTML
html = head + navbar + hero + about + skills + projects + contact + footer + script

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Portfolio HTML file created successfully! ({len(html)} bytes)")
