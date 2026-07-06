#!/usr/bin/env python3
"""
Patches index.html to:
  1. Add Next.js, Express, Prisma, and Stripe API to the About section's tech pills
  2. Insert Resonate as the top (first) featured project

Usage:
    python3 patch_portfolio.py index.html

This edits the file in place. A backup is saved as index.html.bak first.
"""

import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python3 patch_portfolio.py index.html")
    sys.exit(1)

path = sys.argv[1]

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

shutil.copyfile(path, path + ".bak")

# --- 1. Add new tech pills ---
old_pills = '''          <span class="tech-pill">SQLAlchemy</span>
        </div>'''

new_pills = '''          <span class="tech-pill">SQLAlchemy</span>
          <span class="tech-pill core">Next.js</span>
          <span class="tech-pill core">Express</span>
          <span class="tech-pill">Prisma</span>
          <span class="tech-pill core">Stripe API</span>
        </div>'''

if old_pills not in content:
    print("WARNING: tech-pill anchor not found — skipping that edit. File may already be modified.")
else:
    content = content.replace(old_pills, new_pills, 1)
    print("Added Next.js, Express, Prisma, and Stripe API tech pills.")

# --- 2. Insert Resonate as the top featured project ---
old_anchor = '''    <div class="projects-grid">

      <!-- Beauty Empire Salon Featured -->'''

resonate_card = '''    <div class="projects-grid">

      <!-- Resonate Featured -->
      <div class="project-card featured">
        <div>
          <div class="proj-tag">Featured Project · Full-Stack E-Commerce</div>
          <h3 class="proj-title">Resonate</h3>
          <p class="proj-desc">
            A complete e-commerce platform built to demonstrate real full-stack ability, not just a
            styled storefront. Real PostgreSQL database, a JWT-protected admin panel to manage products
            and orders, and an actual Stripe integration handling checkout in test mode — the same
            payment flow a live store would use.
          </p>
          <div class="proj-features">
            <span class="proj-feature">Real Stripe Checkout integration — hosted payment page, test mode</span>
            <span class="proj-feature">Admin panel: manage products & orders behind JWT auth</span>
            <span class="proj-feature">Product search, sort, and live low-stock tracking</span>
            <span class="proj-feature">Customer order tracking by ID + email, no account needed</span>
            <span class="proj-feature">Deployed across three services — Vercel, Render, and Neon</span>
          </div>
          <div class="proj-tech">
            <span class="proj-tech-tag">Next.js</span>
            <span class="proj-tech-tag">Express</span>
            <span class="proj-tech-tag">PostgreSQL</span>
            <span class="proj-tech-tag">Prisma</span>
            <span class="proj-tech-tag">Stripe</span>
            <span class="proj-tech-tag">Vercel</span>
            <span class="proj-tech-tag">Render</span>
          </div>
          <a href="https://resonate-demo-six.vercel.app" target="_blank" class="proj-link">View Live Site →</a>
          <a href="https://github.com/Obito324HX/resonate-demo" target="_blank" class="proj-link" style="margin-left:1.25rem;">GitHub →</a>
        </div>

        <div style="display:flex;flex-direction:column;gap:1rem;">
          <img src="covers/resonate-cover.svg" alt="Resonate e-commerce storefront preview" style="width:100%;border-radius:8px;display:block;border:1px solid var(--border);"/>

          <div class="proj-right" style="flex-direction:row;flex-wrap:wrap;gap:1px;background:var(--border);border:1px solid var(--border);">
            <div class="proj-stat" style="flex:1;border:none;border-radius:0;">
              <div class="proj-stat-val">Stripe</div>
              <div class="proj-stat-label">Test-Mode Checkout</div>
            </div>
            <div class="proj-stat" style="flex:1;border:none;border-radius:0;border-left:1px solid var(--border);">
              <div class="proj-stat-val">3</div>
              <div class="proj-stat-label">Services Deployed</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Beauty Empire Salon Featured -->'''

if old_anchor not in content:
    print("WARNING: projects-grid anchor not found — skipping that edit. File may already be modified.")
else:
    content = content.replace(old_anchor, resonate_card, 1)
    print("Inserted Resonate as the top featured project.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nDone. Original saved as {path}.bak")
