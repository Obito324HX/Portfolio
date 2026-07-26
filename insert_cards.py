import io

anchor = '''        </div>
      </div>


      <div class="project-card" style="grid-template-columns:1fr;">
        <div>
          <div class="proj-tag teal">Web App</div>'''

new_cards = '''        </div>
      </div>

      <!-- Lantern & Wok -->
      <div class="project-card featured">
        <div>
          <div class="proj-tag">Featured Project · Demo</div>
          <h3 class="proj-title">Lantern & Wok</h3>
          <p class="proj-desc">
            A dark, moody rooftop restaurant concept built for lounge-style Pan-Asian dining —
            full digital menu, photo gallery, and reservation flow, built mobile-first instead
            of cutting corners the way most template demos do.
          </p>
          <div class="proj-features">
            <span class="proj-feature">Full digital menu across small plates, mains, and the bar list</span>
            <span class="proj-feature">Reservation form built for real bookings, not just a contact page</span>
            <span class="proj-feature">Photo gallery with a full-screen lightbox for browsing dishes</span>
            <span class="proj-feature">Cursor-reactive "lantern glow" hero — a signature interaction tied to the name</span>
            <span class="proj-feature">Fully responsive with a working mobile navigation menu</span>
          </div>
          <div class="proj-tech">
            <span class="proj-tech-tag">HTML</span>
            <span class="proj-tech-tag">CSS</span>
            <span class="proj-tech-tag">JavaScript</span>
            <span class="proj-tech-tag">GitHub Pages</span>
          </div>
          <a href="https://obito324hx.github.io/lantern-wok/" target="_blank" class="proj-link">View Live Demo →</a>
        </div>

        <div style="display:flex;flex-direction:column;gap:1rem;">
          <img src="covers/lantern-wok-cover.png" alt="Lantern & Wok website preview" style="width:100%;border-radius:12px;display:block;border:1px solid var(--border);"/>

          <div class="proj-right" style="flex-direction:row;flex-wrap:wrap;gap:0.75rem;">
            <div class="proj-stat" style="flex:1;">
              <div class="proj-stat-val">Live</div>
              <div class="proj-stat-label">Status</div>
            </div>
            <div class="proj-stat" style="flex:1;">
              <div class="proj-stat-val">Demo</div>
              <div class="proj-stat-label">For Restaurants</div>
            </div>
          </div>
        </div>
      </div>

      <!-- The Tide House -->
      <div class="project-card featured">
        <div>
          <div class="proj-tag">Featured Project · Demo</div>
          <h3 class="proj-title">The Tide House</h3>
          <p class="proj-desc">
            A bright, daytime coastal Mediterranean restaurant concept — built for international
            outreach with USD pricing and a design language completely distinct from Lantern &amp;
            Wok, showing range across moods for the same kind of business.
          </p>
          <div class="proj-features">
            <span class="proj-feature">Full à la carte menu plus three set-menu tiers, priced in USD</span>
            <span class="proj-feature">Horizontal scroll-snap photo gallery with a full-screen lightbox</span>
            <span class="proj-feature">Reservation form with date, time, party size, and seating preference</span>
            <span class="proj-feature">Ambient "tide" wave dividers and a sunlight-on-water hero animation</span>
            <span class="proj-feature">Fully responsive with a working mobile navigation menu</span>
          </div>
          <div class="proj-tech">
            <span class="proj-tech-tag">HTML</span>
            <span class="proj-tech-tag">CSS</span>
            <span class="proj-tech-tag">JavaScript</span>
            <span class="proj-tech-tag">GitHub Pages</span>
          </div>
          <a href="https://obito324hx.github.io/the-tide-house/" target="_blank" class="proj-link">View Live Demo →</a>
        </div>

        <div style="display:flex;flex-direction:column;gap:1rem;">
          <img src="covers/tide-house-cover.png" alt="The Tide House website preview" style="width:100%;border-radius:12px;display:block;border:1px solid var(--border);"/>

          <div class="proj-right" style="flex-direction:row;flex-wrap:wrap;gap:0.75rem;">
            <div class="proj-stat" style="flex:1;">
              <div class="proj-stat-val">Live</div>
              <div class="proj-stat-label">Status</div>
            </div>
            <div class="proj-stat" style="flex:1;">
              <div class="proj-stat-val">Demo</div>
              <div class="proj-stat-label">International</div>
            </div>
          </div>
        </div>
      </div>


      <div class="project-card" style="grid-template-columns:1fr;">
        <div>
          <div class="proj-tag teal">Web App</div>'''

with io.open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if content.count(anchor) != 1:
    raise SystemExit(f"Anchor found {content.count(anchor)} times, expected exactly 1 — aborting, no changes made.")

content = content.replace(anchor, new_cards)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inserted successfully.")
