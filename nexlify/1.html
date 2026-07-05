import { useState, useEffect, useRef } from "react";

// ── Utility ──────────────────────────────────────────────────────────────────
const useInView = (threshold = 0.15) => {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) { setVisible(true); obs.disconnect(); } },
      { threshold }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, [threshold]);
  return [ref, visible];
};

// ── Animated gradient orbs ────────────────────────────────────────────────────
const Orbs = () => (
  <div style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0, overflow: "hidden" }}>
    <div style={{
      position: "absolute", top: "-20%", left: "-10%", width: 700, height: 700, borderRadius: "50%",
      background: "radial-gradient(circle, rgba(124,58,237,0.18) 0%, transparent 70%)",
      animation: "orbFloat 14s ease-in-out infinite alternate"
    }} />
    <div style={{
      position: "absolute", bottom: "-15%", right: "-10%", width: 600, height: 600, borderRadius: "50%",
      background: "radial-gradient(circle, rgba(59,130,246,0.16) 0%, transparent 70%)",
      animation: "orbFloat 18s ease-in-out infinite alternate-reverse"
    }} />
    <div style={{
      position: "absolute", top: "40%", left: "50%", width: 400, height: 400, borderRadius: "50%",
      background: "radial-gradient(circle, rgba(168,85,247,0.10) 0%, transparent 70%)",
      animation: "orbFloat 22s ease-in-out infinite alternate"
    }} />
  </div>
);

// ── Grid overlay ──────────────────────────────────────────────────────────────
const Grid = () => (
  <div style={{
    position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0,
    backgroundImage: `
      linear-gradient(rgba(124,58,237,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(124,58,237,0.04) 1px, transparent 1px)
    `,
    backgroundSize: "60px 60px"
  }} />
);

// ── Navbar ────────────────────────────────────────────────────────────────────
const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  useEffect(() => {
    const h = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", h);
    return () => window.removeEventListener("scroll", h);
  }, []);
  const links = ["Services", "Portfolio", "Pricing", "About", "Contact"];
  const scroll = (id) => { document.getElementById(id.toLowerCase())?.scrollIntoView({ behavior: "smooth" }); setOpen(false); };
  return (
    <nav style={{
      position: "fixed", top: 0, left: 0, right: 0, zIndex: 100,
      transition: "all 0.4s ease",
      background: scrolled ? "rgba(8,8,18,0.85)" : "transparent",
      backdropFilter: scrolled ? "blur(20px)" : "none",
      borderBottom: scrolled ? "1px solid rgba(124,58,237,0.15)" : "1px solid transparent",
      padding: "0 5%"
    }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", display: "flex", alignItems: "center", justifyContent: "space-between", height: 72 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{
            width: 36, height: 36, borderRadius: 10,
            background: "linear-gradient(135deg, #7c3aed, #3b82f6)",
            display: "flex", alignItems: "center", justifyContent: "center",
            fontSize: 18, fontWeight: 900, color: "#fff", fontFamily: "'Sora', sans-serif",
            boxShadow: "0 0 20px rgba(124,58,237,0.5)"
          }}>N</div>
          <span style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 22, background: "linear-gradient(90deg, #fff, #a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>Nexlify</span>
        </div>
        {/* Desktop links */}
        <div style={{ display: "flex", gap: 36, alignItems: "center" }} className="desktop-nav">
          {links.map(l => (
            <button key={l} onClick={() => scroll(l)}
              style={{ background: "none", border: "none", cursor: "pointer", color: "rgba(255,255,255,0.7)", fontFamily: "'Poppins', sans-serif", fontSize: 14, fontWeight: 500, transition: "color 0.3s", padding: 0 }}
              onMouseEnter={e => e.target.style.color = "#a78bfa"}
              onMouseLeave={e => e.target.style.color = "rgba(255,255,255,0.7)"}
            >{l}</button>
          ))}
          <button onClick={() => scroll("Contact")} style={{
            background: "linear-gradient(135deg, #7c3aed, #3b82f6)", border: "none", cursor: "pointer",
            color: "#fff", fontFamily: "'Poppins', sans-serif", fontSize: 13, fontWeight: 600,
            padding: "10px 24px", borderRadius: 50, transition: "all 0.3s",
            boxShadow: "0 4px 20px rgba(124,58,237,0.4)"
          }}
            onMouseEnter={e => { e.target.style.transform = "translateY(-2px)"; e.target.style.boxShadow = "0 8px 30px rgba(124,58,237,0.6)"; }}
            onMouseLeave={e => { e.target.style.transform = "translateY(0)"; e.target.style.boxShadow = "0 4px 20px rgba(124,58,237,0.4)"; }}
          >Get Started</button>
        </div>
        {/* Hamburger */}
        <button onClick={() => setOpen(!open)} className="hamburger" style={{ background: "none", border: "none", cursor: "pointer", display: "none", flexDirection: "column", gap: 5, padding: 8 }}>
          {[0,1,2].map(i => <div key={i} style={{ width: 24, height: 2, background: "#a78bfa", borderRadius: 2, transition: "all 0.3s" }} />)}
        </button>
      </div>
      {/* Mobile menu */}
      {open && (
        <div style={{ background: "rgba(8,8,18,0.97)", backdropFilter: "blur(20px)", borderTop: "1px solid rgba(124,58,237,0.2)", padding: "20px 5%" }}>
          {links.map(l => (
            <button key={l} onClick={() => scroll(l)} style={{ display: "block", width: "100%", textAlign: "left", background: "none", border: "none", cursor: "pointer", color: "rgba(255,255,255,0.8)", fontFamily: "'Poppins', sans-serif", fontSize: 16, fontWeight: 500, padding: "12px 0", borderBottom: "1px solid rgba(255,255,255,0.05)" }}>{l}</button>
          ))}
        </div>
      )}
      <style>{`
        @media (max-width: 768px) { .desktop-nav { display: none !important; } .hamburger { display: flex !important; } }
        @keyframes orbFloat { 0% { transform: translate(0,0) scale(1); } 100% { transform: translate(40px,60px) scale(1.1); } }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes shimmer { 0% { background-position: -200% center; } 100% { background-position: 200% center; } }
        @keyframes pulse { 0%,100% { box-shadow: 0 0 20px rgba(124,58,237,0.4); } 50% { box-shadow: 0 0 40px rgba(124,58,237,0.8); } }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        @keyframes float { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-12px); } }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }
        body { background: #080812; color: #fff; font-family: 'Poppins', sans-serif; overflow-x: hidden; }
        ::-webkit-scrollbar { width: 6px; } ::-webkit-scrollbar-track { background: #080812; } ::-webkit-scrollbar-thumb { background: #7c3aed; border-radius: 3px; }
        input, textarea { outline: none; }
        .reveal { opacity: 0; transform: translateY(40px); transition: opacity 0.7s ease, transform 0.7s ease; }
        .reveal.visible { opacity: 1; transform: translateY(0); }
      `}</style>
    </nav>
  );
};

// ── Hero ──────────────────────────────────────────────────────────────────────
const Hero = () => {
  const scroll = (id) => document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  return (
    <section id="hero" style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", position: "relative", padding: "120px 5% 80px", overflow: "hidden" }}>
      {/* Floating ring */}
      <div style={{ position: "absolute", top: "15%", right: "8%", width: 280, height: 280, borderRadius: "50%", border: "1px solid rgba(124,58,237,0.25)", animation: "spin 20s linear infinite", zIndex: 1 }} />
      <div style={{ position: "absolute", top: "18%", right: "11%", width: 200, height: 200, borderRadius: "50%", border: "1px solid rgba(59,130,246,0.2)", animation: "spin 30s linear infinite reverse", zIndex: 1 }} />

      <div style={{ maxWidth: 1200, width: "100%", margin: "0 auto", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 60, alignItems: "center", position: "relative", zIndex: 2 }} className="hero-grid">
        <div>
          <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: "rgba(124,58,237,0.15)", border: "1px solid rgba(124,58,237,0.3)", borderRadius: 50, padding: "6px 16px", marginBottom: 28, animation: "fadeIn 0.8s ease both" }}>
            <div style={{ width: 8, height: 8, borderRadius: "50%", background: "#7c3aed", animation: "pulse 2s infinite" }} />
            <span style={{ fontFamily: "'Poppins', sans-serif", fontSize: 13, color: "#a78bfa", fontWeight: 500 }}>Premium Digital Agency</span>
          </div>
          <h1 style={{
            fontFamily: "'Sora', sans-serif", fontWeight: 800, lineHeight: 1.1, marginBottom: 24,
            fontSize: "clamp(2.2rem, 5vw, 3.8rem)",
            animation: "fadeUp 0.9s ease 0.1s both"
          }}>
            We Build{" "}
            <span style={{
              background: "linear-gradient(135deg, #a78bfa, #60a5fa, #a78bfa)",
              backgroundSize: "200% auto",
              WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent",
              animation: "shimmer 3s linear infinite"
            }}>Modern Websites</span>{" "}
            That Help Businesses Grow
          </h1>
          <p style={{ color: "rgba(255,255,255,0.6)", fontSize: "clamp(1rem, 1.8vw, 1.15rem)", lineHeight: 1.7, marginBottom: 40, maxWidth: 520, animation: "fadeUp 0.9s ease 0.2s both" }}>
            Premium web design and development solutions for startups, restaurants, and modern brands.
          </p>
          <div style={{ display: "flex", gap: 16, flexWrap: "wrap", animation: "fadeUp 0.9s ease 0.3s both" }}>
            <button onClick={() => scroll("contact")} style={{
              background: "linear-gradient(135deg, #7c3aed, #3b82f6)", border: "none", cursor: "pointer",
              color: "#fff", fontFamily: "'Poppins', sans-serif", fontSize: 15, fontWeight: 600,
              padding: "14px 32px", borderRadius: 50, transition: "all 0.3s",
              boxShadow: "0 6px 30px rgba(124,58,237,0.5)"
            }}
              onMouseEnter={e => { e.target.style.transform = "translateY(-3px) scale(1.03)"; e.target.style.boxShadow = "0 12px 40px rgba(124,58,237,0.7)"; }}
              onMouseLeave={e => { e.target.style.transform = "translateY(0) scale(1)"; e.target.style.boxShadow = "0 6px 30px rgba(124,58,237,0.5)"; }}
            >Get Started →</button>
            <button onClick={() => scroll("portfolio")} style={{
              background: "transparent", border: "1px solid rgba(255,255,255,0.2)", cursor: "pointer",
              color: "#fff", fontFamily: "'Poppins', sans-serif", fontSize: 15, fontWeight: 500,
              padding: "14px 32px", borderRadius: 50, transition: "all 0.3s", backdropFilter: "blur(10px)"
            }}
              onMouseEnter={e => { e.target.style.borderColor = "rgba(167,139,250,0.6)"; e.target.style.background = "rgba(124,58,237,0.1)"; }}
              onMouseLeave={e => { e.target.style.borderColor = "rgba(255,255,255,0.2)"; e.target.style.background = "transparent"; }}
            >View Portfolio</button>
          </div>
          {/* Stats */}
          <div style={{ display: "flex", gap: 40, marginTop: 56, flexWrap: "wrap", animation: "fadeUp 0.9s ease 0.4s both" }}>
            {[["50+", "Projects Done"], ["98%", "Client Satisfaction"], ["3+", "Years Experience"]].map(([n, l]) => (
              <div key={l}>
                <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 28, background: "linear-gradient(135deg, #a78bfa, #60a5fa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>{n}</div>
                <div style={{ color: "rgba(255,255,255,0.5)", fontSize: 13 }}>{l}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Hero visual */}
        <div style={{ position: "relative", display: "flex", justifyContent: "center", alignItems: "center" }} className="hero-visual">
          <div style={{ position: "relative", animation: "float 5s ease-in-out infinite", zIndex: 2 }}>
            {/* Main browser mockup */}
            <div style={{
              width: "min(420px, 90vw)", background: "rgba(255,255,255,0.04)", borderRadius: 20,
              border: "1px solid rgba(124,58,237,0.25)", backdropFilter: "blur(20px)",
              overflow: "hidden", boxShadow: "0 30px 80px rgba(0,0,0,0.6), 0 0 60px rgba(124,58,237,0.15)"
            }}>
              {/* Browser bar */}
              <div style={{ background: "rgba(255,255,255,0.06)", padding: "12px 16px", display: "flex", alignItems: "center", gap: 8, borderBottom: "1px solid rgba(255,255,255,0.08)" }}>
                {["#ef4444","#f59e0b","#22c55e"].map(c => <div key={c} style={{ width: 10, height: 10, borderRadius: "50%", background: c }} />)}
                <div style={{ flex: 1, background: "rgba(255,255,255,0.08)", borderRadius: 6, height: 22, marginLeft: 8, display: "flex", alignItems: "center", padding: "0 12px" }}>
                  <span style={{ color: "rgba(255,255,255,0.4)", fontSize: 11 }}>nexlify.com</span>
                </div>
              </div>
              {/* Mock content */}
              <div style={{ padding: 24 }}>
                <div style={{ background: "linear-gradient(135deg, rgba(124,58,237,0.3), rgba(59,130,246,0.2))", borderRadius: 12, height: 120, marginBottom: 16, display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <span style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 18, color: "#a78bfa" }}>✦ Nexlify</span>
                </div>
                {[80, 60, 70].map((w, i) => <div key={i} style={{ background: "rgba(255,255,255,0.08)", borderRadius: 6, height: 12, width: `${w}%`, marginBottom: 10 }} />)}
                <div style={{ display: "flex", gap: 10, marginTop: 16 }}>
                  {["linear-gradient(135deg,#7c3aed,#3b82f6)", "rgba(255,255,255,0.1)"].map((bg, i) => (
                    <div key={i} style={{ background: bg, borderRadius: 8, height: 32, flex: i === 0 ? 1 : 0.6 }} />
                  ))}
                </div>
              </div>
            </div>
            {/* Floating badge 1 */}
            <div style={{
              position: "absolute", top: -20, right: -30, background: "rgba(255,255,255,0.06)", border: "1px solid rgba(124,58,237,0.3)",
              backdropFilter: "blur(16px)", borderRadius: 14, padding: "10px 16px", display: "flex", alignItems: "center", gap: 8,
              animation: "float 7s ease-in-out infinite", boxShadow: "0 8px 30px rgba(0,0,0,0.4)"
            }}>
              <div style={{ width: 32, height: 32, borderRadius: 8, background: "linear-gradient(135deg,#7c3aed,#3b82f6)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 16 }}>⚡</div>
              <div>
                <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 13 }}>Performance</div>
                <div style={{ color: "#22c55e", fontSize: 12 }}>99 / 100</div>
              </div>
            </div>
            {/* Floating badge 2 */}
            <div style={{
              position: "absolute", bottom: -18, left: -24, background: "rgba(255,255,255,0.06)", border: "1px solid rgba(59,130,246,0.3)",
              backdropFilter: "blur(16px)", borderRadius: 14, padding: "10px 16px", display: "flex", alignItems: "center", gap: 8,
              animation: "float 9s ease-in-out infinite reverse", boxShadow: "0 8px 30px rgba(0,0,0,0.4)"
            }}>
              <span style={{ fontSize: 22 }}>🚀</span>
              <div>
                <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 13 }}>Live in 7 Days</div>
                <div style={{ color: "#a78bfa", fontSize: 12 }}>Guaranteed</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <style>{`
        @media (max-width: 900px) { .hero-grid { grid-template-columns: 1fr !important; text-align: center; } .hero-visual { display: none !important; } }
      `}</style>
    </section>
  );
};

// ── Section wrapper ───────────────────────────────────────────────────────────
const Section = ({ id, children, style = {} }) => {
  const [ref, visible] = useInView();
  return (
    <section id={id} ref={ref} className={`reveal ${visible ? "visible" : ""}`}
      style={{ padding: "100px 5%", position: "relative", zIndex: 2, ...style }}>
      <div style={{ maxWidth: 1200, margin: "0 auto" }}>{children}</div>
    </section>
  );
};

const SectionLabel = ({ text }) => (
  <div style={{ display: "flex", justifyContent: "center", marginBottom: 16 }}>
    <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: "rgba(124,58,237,0.12)", border: "1px solid rgba(124,58,237,0.25)", borderRadius: 50, padding: "5px 16px" }}>
      <span style={{ color: "#a78bfa", fontSize: 13, fontWeight: 500 }}>{text}</span>
    </div>
  </div>
);

const SectionTitle = ({ children, sub }) => (
  <div style={{ textAlign: "center", marginBottom: 64 }}>
    <h2 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: "clamp(2rem, 4vw, 3rem)", marginBottom: 16, lineHeight: 1.2 }}>{children}</h2>
    {sub && <p style={{ color: "rgba(255,255,255,0.55)", fontSize: "clamp(1rem, 1.5vw, 1.1rem)", maxWidth: 600, margin: "0 auto" }}>{sub}</p>}
  </div>
);

// ── Services ──────────────────────────────────────────────────────────────────
const services = [
  { icon: "🌐", title: "Business Websites", desc: "Stunning, conversion-focused websites that represent your brand professionally online." },
  { icon: "🍽️", title: "Restaurant Websites", desc: "Beautiful menus, online reservations, and ordering systems for food businesses." },
  { icon: "🎨", title: "Portfolio Websites", desc: "Showcasing your creative work with style, elegance, and modern design systems." },
  { icon: "🚀", title: "Landing Pages", desc: "High-converting landing pages designed to turn visitors into paying customers." },
  { icon: "🤖", title: "AI Integrations", desc: "Smart chatbots, automation, and AI-powered features built into your platform." },
  { icon: "📊", title: "Dashboard & Admin Panels", desc: "Custom dashboards and admin systems that make managing your business effortless." },
];

const Services = () => (
  <Section id="services">
    <SectionLabel text="What We Do" />
    <SectionTitle sub="Everything your business needs to establish a dominant online presence.">Our Premium Services</SectionTitle>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: 24 }}>
      {services.map(({ icon, title, desc }, i) => (
        <div key={title} style={{
          background: "rgba(255,255,255,0.03)", border: "1px solid rgba(255,255,255,0.07)", borderRadius: 20,
          padding: 32, transition: "all 0.4s ease", cursor: "default",
          animationDelay: `${i * 0.07}s`
        }}
          onMouseEnter={e => { e.currentTarget.style.background = "rgba(124,58,237,0.1)"; e.currentTarget.style.borderColor = "rgba(124,58,237,0.35)"; e.currentTarget.style.transform = "translateY(-6px)"; e.currentTarget.style.boxShadow = "0 20px 60px rgba(124,58,237,0.15)"; }}
          onMouseLeave={e => { e.currentTarget.style.background = "rgba(255,255,255,0.03)"; e.currentTarget.style.borderColor = "rgba(255,255,255,0.07)"; e.currentTarget.style.transform = "translateY(0)"; e.currentTarget.style.boxShadow = "none"; }}
        >
          <div style={{ width: 52, height: 52, borderRadius: 14, background: "linear-gradient(135deg, rgba(124,58,237,0.3), rgba(59,130,246,0.2))", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 24, marginBottom: 20 }}>{icon}</div>
          <h3 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 18, marginBottom: 10 }}>{title}</h3>
          <p style={{ color: "rgba(255,255,255,0.55)", lineHeight: 1.7, fontSize: 14 }}>{desc}</p>
        </div>
      ))}
    </div>
  </Section>
);

// ── Why Choose ───────────────────────────────────────────────────────────────
const features = [
  { icon: "✦", title: "Modern UI/UX", desc: "Pixel-perfect design that wows visitors and builds instant trust." },
  { icon: "⚡", title: "Fast Performance", desc: "Optimized for speed — 90+ Lighthouse scores guaranteed." },
  { icon: "📱", title: "Mobile Responsive", desc: "Flawless on every device from mobile to ultrawide monitors." },
  { icon: "🔍", title: "SEO Friendly", desc: "Built with search engines in mind to help you get discovered." },
  { icon: "💎", title: "Premium Design", desc: "Award-winning aesthetics that set you apart from competitors." },
  { icon: "🛡️", title: "Reliable Support", desc: "Ongoing support and maintenance so you're never left alone." },
];

const WhyChoose = () => (
  <Section id="why" style={{ background: "rgba(124,58,237,0.03)" }}>
    <SectionLabel text="Why Nexlify" />
    <SectionTitle sub="We combine cutting-edge technology with stunning design to deliver websites that truly perform.">Built to Outperform</SectionTitle>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 20 }}>
      {features.map(({ icon, title, desc }) => (
        <div key={title} style={{ display: "flex", gap: 16, padding: 24, background: "rgba(255,255,255,0.025)", border: "1px solid rgba(255,255,255,0.06)", borderRadius: 16, transition: "all 0.3s" }}
          onMouseEnter={e => { e.currentTarget.style.borderColor = "rgba(124,58,237,0.3)"; e.currentTarget.style.background = "rgba(124,58,237,0.07)"; }}
          onMouseLeave={e => { e.currentTarget.style.borderColor = "rgba(255,255,255,0.06)"; e.currentTarget.style.background = "rgba(255,255,255,0.025)"; }}
        >
          <div style={{ width: 44, height: 44, borderRadius: 12, background: "linear-gradient(135deg,#7c3aed,#3b82f6)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 18, flexShrink: 0 }}>{icon}</div>
          <div>
            <h4 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 15, marginBottom: 6 }}>{title}</h4>
            <p style={{ color: "rgba(255,255,255,0.5)", fontSize: 13, lineHeight: 1.6 }}>{desc}</p>
          </div>
        </div>
      ))}
    </div>
  </Section>
);

// ── Portfolio ────────────────────────────────────────────────────────────────
const projects = [
  { title: "LuxeEats", category: "Restaurant", desc: "Elegant dining experience platform with online reservations and seasonal menus.", color: "#7c3aed", emoji: "🍽️" },
  { title: "Fundora", category: "Startup", desc: "Investment platform with real-time data dashboards and portfolio tracking.", color: "#3b82f6", emoji: "📈" },
  { title: "Artisan Co.", category: "Portfolio", desc: "Minimal creative portfolio for an award-winning design studio.", color: "#a855f7", emoji: "🎨" },
  { title: "SwiftLaunch", category: "Landing Page", desc: "High-converting SaaS landing page that tripled trial signups in 30 days.", color: "#06b6d4", emoji: "🚀" },
  { title: "MedConnect", category: "Business", desc: "Healthcare platform connecting patients with specialists across the country.", color: "#10b981", emoji: "🏥" },
  { title: "Novalytics", category: "Dashboard", desc: "Real-time analytics dashboard with AI-powered insights and custom reports.", color: "#f59e0b", emoji: "📊" },
];

const Portfolio = () => (
  <Section id="portfolio">
    <SectionLabel text="Our Work" />
    <SectionTitle sub="A curated selection of our finest digital creations — built to impress and designed to convert.">Featured Projects</SectionTitle>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))", gap: 24 }}>
      {projects.map(({ title, category, desc, color, emoji }) => (
        <div key={title} style={{
          background: "rgba(255,255,255,0.03)", border: "1px solid rgba(255,255,255,0.07)", borderRadius: 20,
          overflow: "hidden", cursor: "pointer", transition: "all 0.4s ease", position: "relative"
        }}
          onMouseEnter={e => { e.currentTarget.style.transform = "translateY(-8px)"; e.currentTarget.style.boxShadow = `0 24px 70px rgba(0,0,0,0.5), 0 0 0 1px ${color}40`; }}
          onMouseLeave={e => { e.currentTarget.style.transform = "translateY(0)"; e.currentTarget.style.boxShadow = "none"; }}
        >
          <div style={{
            height: 180, background: `linear-gradient(135deg, ${color}33, ${color}11)`,
            display: "flex", alignItems: "center", justifyContent: "center", fontSize: 56, position: "relative",
            borderBottom: `1px solid ${color}22`
          }}>
            {emoji}
            <div style={{ position: "absolute", top: 14, right: 14, background: `${color}22`, border: `1px solid ${color}44`, borderRadius: 50, padding: "4px 12px" }}>
              <span style={{ color, fontSize: 12, fontWeight: 600 }}>{category}</span>
            </div>
          </div>
          <div style={{ padding: 24 }}>
            <h3 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 18, marginBottom: 8 }}>{title}</h3>
            <p style={{ color: "rgba(255,255,255,0.5)", fontSize: 14, lineHeight: 1.6 }}>{desc}</p>
            <div style={{ marginTop: 16, display: "inline-flex", alignItems: "center", gap: 6, color, fontSize: 13, fontWeight: 600 }}>View Case Study →</div>
          </div>
        </div>
      ))}
    </div>
  </Section>
);

// ── Testimonials ─────────────────────────────────────────────────────────────
const testimonials = [
  { name: "Sarah Mitchell", role: "CEO, LuxeEats", text: "Nexlify transformed our restaurant's online presence completely. Reservations went up 200% in the first month alone!", avatar: "SM" },
  { name: "James Owusu", role: "Founder, Fundora", text: "The level of detail and design quality blew us away. Our investors were seriously impressed with our new platform.", avatar: "JO" },
  { name: "Priya Sharma", role: "Creative Director", text: "Professional, fast, and incredibly talented. Nexlify delivered beyond what we even imagined possible.", avatar: "PS" },
];

const Testimonials = () => (
  <Section id="testimonials" style={{ background: "rgba(59,130,246,0.03)" }}>
    <SectionLabel text="Client Love" />
    <SectionTitle sub="Don't take our word for it — here's what our clients have to say.">What Our Clients Say</SectionTitle>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: 24 }}>
      {testimonials.map(({ name, role, text, avatar }) => (
        <div key={name} style={{
          background: "rgba(255,255,255,0.04)", border: "1px solid rgba(255,255,255,0.08)",
          backdropFilter: "blur(20px)", borderRadius: 20, padding: 32, transition: "all 0.3s"
        }}
          onMouseEnter={e => { e.currentTarget.style.borderColor = "rgba(124,58,237,0.3)"; e.currentTarget.style.background = "rgba(124,58,237,0.07)"; }}
          onMouseLeave={e => { e.currentTarget.style.borderColor = "rgba(255,255,255,0.08)"; e.currentTarget.style.background = "rgba(255,255,255,0.04)"; }}
        >
          <div style={{ color: "#f59e0b", fontSize: 20, marginBottom: 16 }}>★★★★★</div>
          <p style={{ color: "rgba(255,255,255,0.75)", lineHeight: 1.75, fontSize: 15, marginBottom: 24, fontStyle: "italic" }}>"{text}"</p>
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <div style={{ width: 44, height: 44, borderRadius: "50%", background: "linear-gradient(135deg,#7c3aed,#3b82f6)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 14 }}>{avatar}</div>
            <div>
              <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 14 }}>{name}</div>
              <div style={{ color: "#a78bfa", fontSize: 13 }}>{role}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  </Section>
);

// ── Pricing ──────────────────────────────────────────────────────────────────
const plans = [
  {
    name: "Starter", price: "$499", period: "one-time", popular: false, color: "#3b82f6",
    features: ["5-Page Website", "Mobile Responsive", "Basic SEO Setup", "Contact Form", "2 Revisions", "30-Day Support"]
  },
  {
    name: "Professional", price: "$999", period: "one-time", popular: true, color: "#7c3aed",
    features: ["10-Page Website", "Custom Animations", "Advanced SEO", "CMS Integration", "E-commerce Ready", "Unlimited Revisions", "3-Month Support"]
  },
  {
    name: "Premium", price: "$1,999", period: "one-time", popular: false, color: "#a855f7",
    features: ["Unlimited Pages", "AI Integrations", "Full E-commerce", "Custom Dashboard", "Priority Development", "Unlimited Revisions", "12-Month Support", "Performance Guarantee"]
  },
];

const Pricing = () => (
  <Section id="pricing">
    <SectionLabel text="Pricing" />
    <SectionTitle sub="Transparent pricing. No hidden fees. No surprises. Just results.">Simple, Honest Pricing</SectionTitle>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 24, alignItems: "center" }}>
      {plans.map(({ name, price, period, popular, color, features }) => (
        <div key={name} style={{
          background: popular ? `linear-gradient(135deg, rgba(124,58,237,0.2), rgba(59,130,246,0.1))` : "rgba(255,255,255,0.03)",
          border: popular ? "1px solid rgba(124,58,237,0.5)" : "1px solid rgba(255,255,255,0.07)",
          borderRadius: 24, padding: popular ? "40px 32px" : "32px 28px",
          position: "relative", transition: "all 0.3s",
          boxShadow: popular ? "0 20px 60px rgba(124,58,237,0.2)" : "none",
          transform: popular ? "scale(1.04)" : "scale(1)"
        }}
          onMouseEnter={e => { e.currentTarget.style.transform = popular ? "scale(1.04) translateY(-4px)" : "translateY(-4px)"; }}
          onMouseLeave={e => { e.currentTarget.style.transform = popular ? "scale(1.04)" : "translateY(0)"; }}
        >
          {popular && <div style={{ position: "absolute", top: -14, left: "50%", transform: "translateX(-50%)", background: "linear-gradient(135deg,#7c3aed,#3b82f6)", borderRadius: 50, padding: "5px 18px", fontSize: 12, fontWeight: 700, whiteSpace: "nowrap", boxShadow: "0 4px 20px rgba(124,58,237,0.5)" }}>⭐ Most Popular</div>}
          <div style={{ marginBottom: 24 }}>
            <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 18, marginBottom: 8 }}>{name}</div>
            <div style={{ display: "flex", alignItems: "baseline", gap: 4 }}>
              <span style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 40, background: `linear-gradient(135deg,${color},#60a5fa)`, WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>{price}</span>
              <span style={{ color: "rgba(255,255,255,0.4)", fontSize: 13 }}>{period}</span>
            </div>
          </div>
          <div style={{ marginBottom: 28 }}>
            {features.map(f => (
              <div key={f} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
                <div style={{ width: 18, height: 18, borderRadius: "50%", background: `${color}22`, border: `1px solid ${color}44`, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0, fontSize: 10, color }}>✓</div>
                <span style={{ color: "rgba(255,255,255,0.7)", fontSize: 14 }}>{f}</span>
              </div>
            ))}
          </div>
          <button onClick={() => document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" })} style={{
            width: "100%", background: popular ? "linear-gradient(135deg,#7c3aed,#3b82f6)" : "rgba(255,255,255,0.06)",
            border: popular ? "none" : "1px solid rgba(255,255,255,0.12)", borderRadius: 12, padding: "14px",
            color: "#fff", fontFamily: "'Poppins', sans-serif", fontWeight: 600, fontSize: 14, cursor: "pointer", transition: "all 0.3s"
          }}
            onMouseEnter={e => { if (!popular) { e.target.style.background = "rgba(124,58,237,0.2)"; e.target.style.borderColor = "rgba(124,58,237,0.4)"; } else { e.target.style.opacity = "0.9"; } }}
            onMouseLeave={e => { if (!popular) { e.target.style.background = "rgba(255,255,255,0.06)"; e.target.style.borderColor = "rgba(255,255,255,0.12)"; } else { e.target.style.opacity = "1"; } }}
          >Get Started</button>
        </div>
      ))}
    </div>
  </Section>
);

// ── About ────────────────────────────────────────────────────────────────────
const About = () => (
  <Section id="about" style={{ background: "rgba(124,58,237,0.03)" }}>
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 80, alignItems: "center" }} className="about-grid">
      <div>
        <SectionLabel text="Our Story" />
        <h2 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: "clamp(1.8rem, 3.5vw, 2.8rem)", lineHeight: 1.2, marginBottom: 24, marginTop: 16 }}>
          We Started with a Simple{" "}
          <span style={{ background: "linear-gradient(135deg,#a78bfa,#60a5fa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>Mission</span>
        </h2>
        <p style={{ color: "rgba(255,255,255,0.6)", lineHeight: 1.8, marginBottom: 20 }}>
          Nexlify was founded on a belief: every business, no matter how small, deserves a world-class digital presence. We saw too many great companies held back by outdated, underperforming websites.
        </p>
        <p style={{ color: "rgba(255,255,255,0.6)", lineHeight: 1.8, marginBottom: 32 }}>
          So we built a studio that combines elite design talent with technical excellence — delivering premium websites that not only look incredible but actually drive real business results.
        </p>
        <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
          {[["50+", "Projects"], ["25+", "Happy Clients"], ["3+", "Years"]].map(([n, l]) => (
            <div key={l} style={{ background: "rgba(124,58,237,0.1)", border: "1px solid rgba(124,58,237,0.2)", borderRadius: 14, padding: "16px 24px", textAlign: "center" }}>
              <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 26, background: "linear-gradient(135deg,#a78bfa,#60a5fa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>{n}</div>
              <div style={{ color: "rgba(255,255,255,0.5)", fontSize: 13 }}>{l}</div>
            </div>
          ))}
        </div>
      </div>
      <div style={{ position: "relative" }}>
        <div style={{ background: "linear-gradient(135deg, rgba(124,58,237,0.15), rgba(59,130,246,0.1))", border: "1px solid rgba(124,58,237,0.2)", borderRadius: 24, padding: 40, backdropFilter: "blur(10px)" }}>
          {["Strategy & Discovery", "Design & Prototyping", "Development & Launch", "Support & Growth"].map((step, i) => (
            <div key={step} style={{ display: "flex", alignItems: "center", gap: 16, marginBottom: i < 3 ? 24 : 0 }}>
              <div style={{ width: 36, height: 36, borderRadius: 10, background: "linear-gradient(135deg,#7c3aed,#3b82f6)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 14, flexShrink: 0 }}>0{i + 1}</div>
              <div>
                <div style={{ fontFamily: "'Sora', sans-serif", fontWeight: 600, fontSize: 15 }}>{step}</div>
                {i < 3 && <div style={{ height: 1, background: "linear-gradient(90deg, rgba(124,58,237,0.3), transparent)", marginTop: 20, marginLeft: -52 }} />}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
    <style>{`@media (max-width: 768px) { .about-grid { grid-template-columns: 1fr !important; gap: 40px !important; } }`}</style>
  </Section>
);

// ── Contact ──────────────────────────────────────────────────────────────────
const Contact = () => {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [sent, setSent] = useState(false);
  const submit = () => { if (form.name && form.email && form.message) { setSent(true); setForm({ name: "", email: "", message: "" }); setTimeout(() => setSent(false), 4000); } };
  const inputStyle = { width: "100%", background: "rgba(255,255,255,0.05)", border: "1px solid rgba(255,255,255,0.1)", borderRadius: 12, padding: "14px 18px", color: "#fff", fontFamily: "'Poppins', sans-serif", fontSize: 14, transition: "border-color 0.3s" };
  return (
    <Section id="contact">
      <SectionLabel text="Get In Touch" />
      <SectionTitle sub="Ready to build something amazing? Let's talk about your project.">Start Your Project</SectionTitle>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 60, alignItems: "start" }} className="contact-grid">
        <div>
          <h3 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 22, marginBottom: 24 }}>Let's Build Something Great</h3>
          <p style={{ color: "rgba(255,255,255,0.55)", lineHeight: 1.8, marginBottom: 36 }}>Whether you have a detailed brief or just a rough idea, we're here to help you bring your vision to life.</p>
          {[
            { icon: "📧", label: "Email Us", value: "hello@nexlify.com" },
            { icon: "💬", label: "WhatsApp", value: "+1 (555) 000-0000" },
            { icon: "📍", label: "Location", value: "Available Worldwide" },
          ].map(({ icon, label, value }) => (
            <div key={label} style={{ display: "flex", gap: 16, alignItems: "center", marginBottom: 20 }}>
              <div style={{ width: 44, height: 44, borderRadius: 12, background: "rgba(124,58,237,0.15)", border: "1px solid rgba(124,58,237,0.2)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 18, flexShrink: 0 }}>{icon}</div>
              <div>
                <div style={{ color: "rgba(255,255,255,0.4)", fontSize: 12 }}>{label}</div>
                <div style={{ fontWeight: 600, fontSize: 15 }}>{value}</div>
              </div>
            </div>
          ))}
          <a href="https://wa.me/15550000000" style={{
            display: "inline-flex", alignItems: "center", gap: 10, marginTop: 16,
            background: "linear-gradient(135deg,#22c55e,#16a34a)", borderRadius: 50, padding: "12px 24px",
            color: "#fff", textDecoration: "none", fontFamily: "'Poppins', sans-serif", fontWeight: 600, fontSize: 14,
            boxShadow: "0 6px 24px rgba(34,197,94,0.35)", transition: "all 0.3s"
          }}
            onMouseEnter={e => { e.currentTarget.style.transform = "translateY(-3px)"; e.currentTarget.style.boxShadow = "0 12px 36px rgba(34,197,94,0.5)"; }}
            onMouseLeave={e => { e.currentTarget.style.transform = "translateY(0)"; e.currentTarget.style.boxShadow = "0 6px 24px rgba(34,197,94,0.35)"; }}
          >💬 Chat on WhatsApp</a>
        </div>
        <div style={{ background: "rgba(255,255,255,0.03)", border: "1px solid rgba(255,255,255,0.08)", borderRadius: 24, padding: 36 }}>
          {sent ? (
            <div style={{ textAlign: "center", padding: "40px 0" }}>
              <div style={{ fontSize: 48, marginBottom: 16 }}>🎉</div>
              <h3 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, marginBottom: 8 }}>Message Sent!</h3>
              <p style={{ color: "rgba(255,255,255,0.55)" }}>We'll get back to you within 24 hours.</p>
            </div>
          ) : (
            <>
              {[{ ph: "Your Name", key: "name" }, { ph: "Your Email", key: "email" }].map(({ ph, key }) => (
                <div key={key} style={{ marginBottom: 16 }}>
                  <input placeholder={ph} value={form[key]} onChange={e => setForm(p => ({ ...p, [key]: e.target.value }))}
                    style={inputStyle}
                    onFocus={e => e.target.style.borderColor = "rgba(124,58,237,0.5)"}
                    onBlur={e => e.target.style.borderColor = "rgba(255,255,255,0.1)"}
                  />
                </div>
              ))}
              <textarea placeholder="Tell us about your project..." value={form.message} onChange={e => setForm(p => ({ ...p, message: e.target.value }))}
                rows={5} style={{ ...inputStyle, resize: "vertical", marginBottom: 20 }}
                onFocus={e => e.target.style.borderColor = "rgba(124,58,237,0.5)"}
                onBlur={e => e.target.style.borderColor = "rgba(255,255,255,0.1)"}
              />
              <button onClick={submit} style={{
                width: "100%", background: "linear-gradient(135deg,#7c3aed,#3b82f6)", border: "none", borderRadius: 12,
                padding: "15px", color: "#fff", fontFamily: "'Poppins', sans-serif", fontWeight: 700, fontSize: 15,
                cursor: "pointer", transition: "all 0.3s", boxShadow: "0 6px 24px rgba(124,58,237,0.4)"
              }}
                onMouseEnter={e => { e.target.style.transform = "translateY(-2px)"; e.target.style.boxShadow = "0 12px 36px rgba(124,58,237,0.6)"; }}
                onMouseLeave={e => { e.target.style.transform = "translateY(0)"; e.target.style.boxShadow = "0 6px 24px rgba(124,58,237,0.4)"; }}
              >Send Message →</button>
            </>
          )}
        </div>
      </div>
      <style>{`@media (max-width: 768px) { .contact-grid { grid-template-columns: 1fr !important; gap: 40px !important; } }`}</style>
    </Section>
  );
};

// ── Footer ───────────────────────────────────────────────────────────────────
const Footer = () => (
  <footer style={{ borderTop: "1px solid rgba(124,58,237,0.15)", padding: "60px 5% 30px", position: "relative", zIndex: 2 }}>
    <div style={{ maxWidth: 1200, margin: "0 auto" }}>
      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr 1fr 1fr", gap: 40, marginBottom: 60 }} className="footer-grid">
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 16 }}>
            <div style={{ width: 36, height: 36, borderRadius: 10, background: "linear-gradient(135deg,#7c3aed,#3b82f6)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Sora', sans-serif", fontWeight: 900, fontSize: 18, boxShadow: "0 0 20px rgba(124,58,237,0.5)" }}>N</div>
            <span style={{ fontFamily: "'Sora', sans-serif", fontWeight: 800, fontSize: 20, background: "linear-gradient(90deg,#fff,#a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>Nexlify</span>
          </div>
          <p style={{ color: "rgba(255,255,255,0.45)", lineHeight: 1.7, fontSize: 14, maxWidth: 260, marginBottom: 24 }}>Premium web design and development for businesses ready to grow digitally.</p>
          <div style={{ display: "flex", gap: 12 }}>
            {["𝕏", "in", "fb", "ig"].map(s => (
              <div key={s} style={{ width: 36, height: 36, borderRadius: 10, background: "rgba(255,255,255,0.05)", border: "1px solid rgba(255,255,255,0.08)", display: "flex", alignItems: "center", justifyContent: "center", cursor: "pointer", fontSize: 13, fontWeight: 700, color: "rgba(255,255,255,0.5)", transition: "all 0.3s" }}
                onMouseEnter={e => { e.target.style.background = "rgba(124,58,237,0.2)"; e.target.style.borderColor = "rgba(124,58,237,0.4)"; e.target.style.color = "#a78bfa"; }}
                onMouseLeave={e => { e.target.style.background = "rgba(255,255,255,0.05)"; e.target.style.borderColor = "rgba(255,255,255,0.08)"; e.target.style.color = "rgba(255,255,255,0.5)"; }}
              >{s}</div>
            ))}
          </div>
        </div>
        {[
          { title: "Services", links: ["Business Websites", "Restaurant Websites", "Portfolio Sites", "Landing Pages", "AI Integrations"] },
          { title: "Company", links: ["About Us", "Portfolio", "Pricing", "Blog", "Contact"] },
          { title: "Legal", links: ["Privacy Policy", "Terms of Service", "Cookie Policy"] },
        ].map(({ title, links }) => (
          <div key={title}>
            <h4 style={{ fontFamily: "'Sora', sans-serif", fontWeight: 700, fontSize: 15, marginBottom: 20 }}>{title}</h4>
            {links.map(l => <div key={l} style={{ color: "rgba(255,255,255,0.45)", fontSize: 14, marginBottom: 10, cursor: "pointer", transition: "color 0.3s" }}
              onMouseEnter={e => e.target.style.color = "#a78bfa"}
              onMouseLeave={e => e.target.style.color = "rgba(255,255,255,0.45)"}
            >{l}</div>)}
          </div>
        ))}
      </div>
      <div style={{ borderTop: "1px solid rgba(255,255,255,0.06)", paddingTop: 24, display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 12 }}>
        <span style={{ color: "rgba(255,255,255,0.3)", fontSize: 13 }}>© 2025 Nexlify. All rights reserved.</span>
        <span style={{ color: "rgba(255,255,255,0.3)", fontSize: 13 }}>Built with ♥ for ambitious businesses</span>
      </div>
    </div>
    <style>{`@media (max-width: 768px) { .footer-grid { grid-template-columns: 1fr 1fr !important; } }`}</style>
  </footer>
);

// ── App ───────────────────────────────────────────────────────────────────────
export default function App() {
  useEffect(() => {
    // Google Fonts
    const link = document.createElement("link");
    link.href = "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Poppins:wght@400;500;600;700&display=swap";
    link.rel = "stylesheet";
    document.head.appendChild(link);
  }, []);

  return (
    <div style={{ background: "#080812", color: "#fff", minHeight: "100vh" }}>
      <Grid />
      <Orbs />
      <Navbar />
      <Hero />
      <Services />
      <WhyChoose />
      <Portfolio />
      <Testimonials />
      <Pricing />
      <About />
      <Contact />
      <Footer />
    </div>
  );
}