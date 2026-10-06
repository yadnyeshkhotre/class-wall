# Contributing

This repository works the way a real engineering team works. These are the house rules.

## The flow
1. Never commit straight to `main`. `main` is what users see.
2. Start from an up-to-date `main`, then create a branch: `add-<username>`, `feature/<thing>`, `fix/<thing>`.
3. Make small commits with clear messages.
4. Push your branch and open a pull request.
5. The robots check it first (GitHub Actions). Then a human reviews it.
6. A maintainer merges it. The website updates by itself.

## Commit messages (Conventional Commits)
Write them so they complete the sentence *"If applied, this commit will…"*

| Prefix | Use it for | Example |
|---|---|---|
| `feat:` | something new | `feat: add Asha's card` |
| `fix:` | fixing a bug | `fix: correct GitHub username in card` |
| `docs:` | documentation only | `docs: explain how to sync a fork` |
| `style:` | formatting, no logic change | `style: tidy card spacing` |
| `refactor:` | restructuring without changing behaviour | `refactor: split render function` |
| `chore:` | housekeeping | `chore: update workflow version` |

## Reviews
- Be kind and specific. Review the code, not the person.
- Prefix small, optional suggestions with `nit:`.
- Authors: reply to every comment, even if it's just "done in a1b2c3d".

## Never commit
Passwords, API keys, `.env` files, or other people's personal data.
