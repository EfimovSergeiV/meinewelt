# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Install PNPM
```bash
curl -fsSL https://get.pnpm.io/install.sh | sh - 
```

## Setup

Make sure to install the dependencies:

```bash
# pnpm
pnpm install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm run dev
```

## Production

Build the application for production:

```bash
# pnpm
pnpm run build

# PM2
pm2 start ecosystem.config.cjs
# Watch app
pm2 start ecosystem.config.cjs --watch
pm2 save
```

Locally preview production build:

```bash
# pnpm
pnpm run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
