# Clarix — Studio d'agents IA

Site vitrine de Clarix. Next.js 14 (App Router) · Tailwind CSS · Framer Motion · TypeScript.

DA : éditorial technique « à la suisse » — papier teinté, encre, un bleu cobalt en aplats, coins vifs, grille de composition visible, gros typographique assuré.

## Démarrer

```bash
npm install
npm run dev
```

Puis ouvrir http://localhost:3000

> Le premier build télécharge les polices (Archivo, Archivo Expanded, Space Mono) via `next/font` — une connexion internet est nécessaire au build.

## Design tokens

Définis dans `tailwind.config.ts` :

- `paper` `#E8E6DF` — fond papier teinté (ni blanc cru ni noir)
- `ink` `#16171B` — encre
- `cobalt` `#1B33E6` — accent, posé en aplats
- `line` / `mut` — filets et texte secondaire (rgba)

Polices (variables CSS via `app/layout.tsx`) : `--font-exp` (titres), `--font-sans` (texte), `--font-mono` (labels) → utilitaires Tailwind `font-exp`, `font-sans`, `font-mono`.

## Où sont les effets

- **Curseur réticule + coordonnées** → `components/ReticleCursor.tsx`. Viseur `+` avec coordonnées x/y en monospace ; au survol d'un `a`, `button` ou `[data-cursor]`, il s'ouvre en crochets de cadrage `[ ]`. Désactivé sur écran tactile.
- **Scroll / parallax** → `Hero.tsx` (fiche technique qui dérive), `Footer.tsx` (signature CLARIX qui glisse), et `Reveal.tsx` (révélation au scroll, réutilisé partout).
- **Image duotone art-directée** → `Showcase.tsx`. Filtre SVG `#clarix-duo` (cobalt → papier) + trame demi-teinte. Remplacer `public/showcase.svg` par une vraie photo (`.jpg`/`.png`) : le duotone s'applique automatiquement.
- **Lignes qui s'inversent** → `Capabilities.tsx` (hover → fond cobalt).
- **Marquee** → `Ticker.tsx`.

`prefers-reduced-motion` est respecté (animations coupées).

## Structure

```
app/        layout.tsx · page.tsx · globals.css
components/ ReticleCursor · Backdrop · Ticker · Nav · Hero
            Capabilities · Showcase · Manifesto · Process · Footer
            Reveal · Mark
public/     showcase.svg (placeholder à remplacer)
```

## À remplacer

- Coordonnées : e-mail / téléphone dans `Footer.tsx`.
- Visuel : `public/showcase.svg` → vraie photo.
- Chiffres / textes : à ajuster selon le réel.

## Pistes pour continuer avec Claude Code

- Ajouter une page `/agents` (détail des cas d'usage) et une page `/contact` avec formulaire.
- Brancher un vrai formulaire (Resend, ou une route API `app/api/contact/route.ts`).
- Remplacer le placeholder par une photo et, si besoin, passer à `next/image` (configurer le domaine dans `next.config.mjs`).
- Variante du curseur ou réglage du cobalt (un cran plus profond) dans les tokens.
