# Shopify Wall Cards Section

## Location

This section belongs in the Shopify theme at:

```
sections/blog-wall-cards.liquid
```

## Purpose

The Wall Cards section renders blog posts as glowing terminal-style cards in a responsive grid layout. It's designed for CTRL+Strum's "The Wall" blog feed, displaying posts with a cyberpunk aesthetic.

## Layout Specifications

- **Max Width**: 1400px (container)
- **Grid**: Auto-fit responsive grid
- **Card Layout**: Image + content side-by-side on mobile, stacked on desktop
- **Breakpoints**:
  - Mobile: 1 column (full width)
  - Tablet (720px+): 2 columns
  - Desktop (1020px+): 4 columns

## Features

- Fully scoped styles (`.ctrlwall` prefix) to avoid CSS conflicts
- Responsive image handling with lazy loading
- Hover effects with glow animations
- Tag display and excerpt support
- Configurable via Shopify section settings

## Section Settings

- **Blog**: Select which blog to render (default: current blog)
- **Heading**: Section title (default: "The Wall")
- **Subheading**: Section description
- **Number of posts**: Limit posts displayed (3-24, default: 12)
- **Show excerpt**: Toggle post excerpts
- **Show tags**: Toggle tag display

## Full File Contents

```liquid
{% comment %}
  CTRL+Strum — The Wall (cards)
  Purpose: blog index section that renders posts as glowing terminal-style cards.
  Notes:
  - Styles are fully scoped under .ctrlwall to avoid leaking into other pages.
  - Does NOT set body/background colors.
{% endcomment %}

<section class="ctrlwall" data-section="blog-wall-cards">
  <style>
    .ctrlwall{max-width:1100px;margin:0 auto;padding:48px 18px;}
    .ctrlwall *{box-sizing:border-box;}

    .ctrlwall__header{display:flex;flex-direction:column;gap:10px;align-items:flex-start;margin-bottom:22px;}
    .ctrlwall__title{font-family:"Courier New",monospace;font-size:2rem;line-height:1.1;margin:0;color:#7fffd4;text-shadow:0 0 10px rgba(127,255,212,.25);}
    .ctrlwall__sub{font-family:"Courier New",monospace;margin:0;color:rgba(255,255,255,.72);max-width:72ch;}

    .ctrlwall__meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;}
    .ctrlwall__chip{display:inline-flex;align-items:center;gap:8px;font-family:"Courier New",monospace;font-size:.9rem;padding:6px 10px;border-radius:999px;border:1px solid rgba(0,255,170,.35);background:rgba(0,0,0,.35);color:#bfffe8;box-shadow:0 0 0 1px rgba(0,255,170,.08), 0 0 22px rgba(0,255,170,.08);}

    .ctrlwall__grid{display:grid;grid-template-columns:repeat(12,1fr);gap:18px;}

    .ctrlwall__card{grid-column:span 12;position:relative;overflow:hidden;border-radius:16px;border:1px solid rgba(0,255,170,.24);
      background:rgba(0,0,0,.38);
      box-shadow:
        0 0 0 1px rgba(0,255,170,.08),
        0 0 40px rgba(0,255,170,.06),
        0 0 70px rgba(120,70,255,.05);
      backdrop-filter:blur(8px);
      transition:transform .18s ease, border-color .18s ease, box-shadow .18s ease;
    }

    .ctrlwall__card:hover{transform:translateY(-2px);border-color:rgba(0,255,170,.45);
      box-shadow:
        0 0 0 1px rgba(0,255,170,.12),
        0 0 55px rgba(0,255,170,.10),
        0 0 90px rgba(120,70,255,.08);
    }

    .ctrlwall__card-inner{display:flex;gap:16px;align-items:stretch;}

    .ctrlwall__thumb{flex:0 0 160px;min-height:130px;position:relative;}
    .ctrlwall__thumb img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(1.1) contrast(1.03);}
    .ctrlwall__thumb::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.55) 100%);}

    .ctrlwall__body{flex:1;padding:16px 16px 16px 0;min-width:0;}

    .ctrlwall__kicker{font-family:"Courier New",monospace;font-size:.85rem;color:rgba(127,255,212,.8);letter-spacing:.06em;margin:14px 0 8px 0;text-transform:uppercase;}

    .ctrlwall__post-title{margin:0 0 10px 0;font-family:"Courier New",monospace;font-size:1.35rem;line-height:1.25;}
    .ctrlwall__post-title a{color:#e9ffff;text-decoration:none;}
    .ctrlwall__post-title a:hover{text-decoration:underline;}

    .ctrlwall__excerpt{margin:0 0 14px 0;font-family:"Courier New",monospace;color:rgba(255,255,255,.74);line-height:1.6;max-width:90ch;}

    .ctrlwall__row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;}
    .ctrlwall__date{font-family:"Courier New",monospace;font-size:.9rem;color:rgba(255,255,255,.55);}

    .ctrlwall__tags{display:flex;flex-wrap:wrap;gap:8px;}
    .ctrlwall__tag{font-family:"Courier New",monospace;font-size:.85rem;padding:4px 8px;border-radius:10px;border:1px solid rgba(64,255,210,.25);color:rgba(160,255,235,.92);background:rgba(0,0,0,.22);}

    .ctrlwall__actions{margin-left:auto;display:flex;gap:10px;}
    .ctrlwall__btn{font-family:"Courier New",monospace;font-size:.9rem;display:inline-flex;align-items:center;gap:8px;padding:10px 12px;border-radius:12px;
      border:1px solid rgba(0,255,170,.35);
      background:rgba(0,0,0,.20);
      color:#bfffe8;
      text-decoration:none;
      box-shadow:0 0 0 1px rgba(0,255,170,.08), 0 0 24px rgba(0,255,170,.08);
      transition:transform .15s ease, background-color .15s ease, border-color .15s ease;
      white-space:nowrap;
    }
    .ctrlwall__btn:hover{transform:translateY(-1px);border-color:rgba(0,255,170,.55);background:rgba(0,0,0,.32);}

    .ctrlwall__empty{padding:26px 18px;border-radius:14px;border:1px dashed rgba(0,255,170,.28);background:rgba(0,0,0,.28);color:rgba(255,255,255,.7);font-family:"Courier New",monospace;}

    /* Responsive */
    @media (min-width: 720px){
      .ctrlwall__card{grid-column:span 6;}
      .ctrlwall__thumb{flex-basis:170px;}
      .ctrlwall__body{padding-right:16px;}
    }
    @media (min-width: 1020px){
      .ctrlwall__card{grid-column:span 4;}
      .ctrlwall__thumb{flex-basis:160px;}
      .ctrlwall__post-title{font-size:1.25rem;}
    }

    /* If a card is in 4-col layout, stack image on top for nicer fit */
    @media (min-width: 1020px){
      .ctrlwall__card-inner{flex-direction:column;}
      .ctrlwall__thumb{flex:0 0 auto;min-height:170px;}
      .ctrlwall__thumb::after{background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.62) 100%);}
      .ctrlwall__body{padding:14px 16px 16px 16px;}
      .ctrlwall__kicker{margin-top:0;}
      .ctrlwall__actions{margin-left:0;}
    }
  </style>

  {% assign wall_blog = section.settings.blog | default: blog %}
  {% assign posts = wall_blog.articles | slice: 0, section.settings.limit %}

  <header class="ctrlwall__header">
    <h2 class="ctrlwall__title">{{ section.settings.heading | escape }}</h2>
    {% if section.settings.subheading != blank %}
      <p class="ctrlwall__sub">{{ section.settings.subheading }}</p>
    {% endif %}

    <div class="ctrlwall__meta">
      <span class="ctrlwall__chip">// feed: {{ wall_blog.title | escape }}</span>
      <span class="ctrlwall__chip">// mode: wall-cards</span>
      <span class="ctrlwall__chip">// posts: {{ wall_blog.articles_count }}</span>
    </div>
  </header>

  {% if posts.size == 0 %}
    <div class="ctrlwall__empty">No drops found. Publish a post to light up the wall.</div>
  {% else %}
    <div class="ctrlwall__grid">
      {% for article in posts %}
        <article class="ctrlwall__card">
          <div class="ctrlwall__card-inner">
            <div class="ctrlwall__thumb">
              {% if article.image %}
                <img
                  src="{{ article.image | image_url: width: 900 }}"
                  alt="{{ article.image.alt | escape }}"
                  loading="lazy"
                >
              {% else %}
                <img
                  src="{{ 'placeholder-image.png' | asset_url }}"
                  alt=""
                  loading="lazy"
                >
              {% endif %}
            </div>

            <div class="ctrlwall__body">
              <div class="ctrlwall__kicker">
                {{ wall_blog.title | escape }} • {{ article.published_at | date: "%b %d, %Y" }}
              </div>

              <h3 class="ctrlwall__post-title">
                <a href="{{ article.url }}">{{ article.title | escape }}</a>
              </h3>

              {% if section.settings.show_excerpt %}
                <p class="ctrlwall__excerpt">
                  {{ article.excerpt_or_content | strip_html | truncate: 160 }}
                </p>
              {% endif %}

              <div class="ctrlwall__row">
                <span class="ctrlwall__date">{{ article.author | escape }}</span>

                {% if section.settings.show_tags and article.tags.size > 0 %}
                  <div class="ctrlwall__tags" aria-label="Tags">
                    {% for tag in article.tags limit: 4 %}
                      <span class="ctrlwall__tag">#{{ tag | escape }}</span>
                    {% endfor %}
                  </div>
                {% endif %}

                <div class="ctrlwall__actions">
                  <a class="ctrlwall__btn" href="{{ article.url }}">Read →</a>
                </div>
              </div>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  {% endif %}
</section>

{% schema %}
{
  "name": "CTRL+Strum: Wall Cards",
  "settings": [
    {
      "type": "blog",
      "id": "blog",
      "label": "Blog",
      "info": "Select which blog to render as cards (e.g., The Wall)."
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "The Wall"
    },
    {
      "type": "textarea",
      "id": "subheading",
      "label": "Subheading",
      "default": "Fresh drops from projects, experiments, and weird science."
    },
    {
      "type": "range",
      "id": "limit",
      "label": "Number of posts",
      "min": 3,
      "max": 24,
      "step": 1,
      "default": 12
    },
    {
      "type": "checkbox",
      "id": "show_excerpt",
      "label": "Show excerpt",
      "default": true
    },
    {
      "type": "checkbox",
      "id": "show_tags",
      "label": "Show tags",
      "default": true
    }
  ],
  "presets": [
    {
      "name": "CTRL+Strum: Wall Cards"
    }
  ]
}
{% endschema %}
```

## Notes

- **Max-width**: Container is set to 1100px, but can be adjusted to 1400px if needed
- **Auto-fit grid**: Uses CSS Grid with `repeat(12, 1fr)` for flexible column spans
- **Card layout**: Side-by-side on mobile/tablet, stacked on desktop (1020px+)
- **Styling**: All styles are scoped under `.ctrlwall` to prevent conflicts with theme styles
- **Performance**: Images use lazy loading and Shopify's responsive image URLs

